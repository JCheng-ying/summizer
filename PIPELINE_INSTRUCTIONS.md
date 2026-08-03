# Summizer 执行说明(给运行这个流水线的 Claude 看)

这份文档是给"定期跑一遍 Summizer"的 Claude 会话看的操作手册。每次运行都是一个全新的会话,
不记得之前发生过什么,所以每次都要完整照着这份说明走一遍。

## 背景

用户定期关注机器人/科技领域的三个信息源(The Robot Report - Haptics 分类、ScienceDaily -
Robotics、IEEE Spectrum - Robotics)。这套工具的目标:

1. 自动发现新文章,读全文,产出一篇中文成品分析文章(技术白话讲解 + 技术进步角度 + 投资角度),
   供用户复制去发布到自己的网站/平台。
2. 从文章里抽取公司/技术/机构等实体和它们之间的关系(合作/竞争/投资/收购等),持续累积进
   一个知识图谱,可视化成一张力导向关系图。

Python 脚本只负责"抓取 RSS、抓全文、存储、去重、渲染图谱"这些机械性工作,不调用任何外部
AI API —— **文章撰写和实体/关系抽取由你(运行这个任务的 Claude)直接完成**,不需要
ANTHROPIC_API_KEY。

这套流水线可能在两种环境里运行:本地 Mac(用户自己开的 Claude Code 会话,项目路径固定在
`/Users/chengjiaying/Desktop/Summizer`)、或者云端定时任务(每次都是全新 clone 这个仓库的
沙盒,没有本地那个 `.venv`,也没有权限访问用户 Mac)。两种情况下产出的文章/图谱数据都是通过
这个 git 仓库同步的 —— 云端跑完之后必须把变更 commit + push 回去,用户本地才能在自己电脑上
`git pull` 看到最新结果。

## 步骤

1. 进入项目目录,准备好 Python 环境:
   ```bash
   cd "/Users/chengjiaying/Desktop/Summizer"   # 本地路径;云端沙盒里就是 repo 根目录
   ```
   - 如果存在 `.venv`(本地场景):`source .venv/bin/activate`
   - 如果不存在 `.venv`(云端全新沙盒):`pip install -r requirements.txt` 直接装到全局环境即可

2. 获取新文章:
   ```bash
   python -m src.main new-items --limit 5
   ```
   输出是一个 JSON 数组,每个元素是 `{title, link, source_name, published, categories, rss_content, full_text}`。
   `full_text` 是已经抓取好的正文全文。如果数组为空,说明没有新文章,直接结束,不用往下做。

   `--limit` 控制单次最多处理几篇,避免一次处理过多。默认 5,如果新文章明显是突发情况
   (比如第一次运行、或者长时间没跑积压了很多),可以自己判断要不要加大。

3. 对每一篇新文章依次处理:

   ### 3a. 撰写分析文章

   用 Write 工具把下面结构的 Markdown 写入
   `data/articles/<YYYY-MM-DD>-<英文slug>.md`(日期用今天,slug 从标题生成,小写连字符,
   可以用 `python -c "from src.pipeline import slugify; print(slugify('原标题'))"` 生成)。

   文章必须基于 `full_text` 的真实内容撰写,不要编造原文没有的事实、数字或公司名。结构:

   ```markdown
   # {吸引人但不夸张的中文标题}

   **原文:** [{原文标题}]({原文链接}) · {来源名称}{发布日期(如果有)}

   ## 一句话摘要
   (一到两句话,说清楚这篇文章讲了什么进展)

   ## 技术白话讲清楚
   (面向没有工程背景的读者,用最简单的语言和类比,讲清楚文章中出现的关键技术概念和术语。
   不要堆术语,假设读者是聪明但外行的人)

   ## 技术进步角度
   (这项进展相对于现有技术的突破点是什么、解决了什么具体问题、技术成熟度大概处于什么阶段
   ——实验室/原型/量产前/已商用、还有哪些明显局限没解决)

   ## 投资角度
   (这项进展可能利好/利空产业链的哪些环节、可能受益或承压的公司(基于原文提到的公司,不要
   编造原文没提到的公司)、这是否改变了某个细分赛道的竞争格局、后续值得跟踪的信号是什么、
   有哪些不确定性和风险。明确这是研究性参考,不构成投资建议)

   ## 关键要点
   - (3-5条 bullet,提炼全文最值得记住的点)

   ---
   *本文由 AI 基于公开报道自动生成,用于个人投研参考,不构成投资建议。*
   ```

   ### 3b. 抽取实体与关系

   只抽取原文中真实出现、有实际依据的实体和关系,不要编造或过度推测。如果文章没有明确的
   公司间关系(比如纯学术研究报道),relationships 可以是空数组 —— 这种情况可以跳过 3c,
   直接执行 3d(mark-seen)。

   把结果按下面的 schema 写成 JSON,存到一个临时文件(比如
   `/tmp/summizer_extraction_<n>.json`):

   ```json
   {
     "entities": [
       {"name": "实体名(用最常见/官方的英文名或通用简称)", "type": "company | technology | institution | product | person", "sector": "如 haptics / humanoid robotics / sensors / space economy / AI 等"}
     ],
     "relationships": [
       {"source": "实体名", "target": "实体名", "type": "partnership | competition | investment | acquisition | supplier | customer | research_collaboration | subsidiary", "description": "一句中文说明这段关系的具体内容,源自原文"}
     ]
   }
   ```

   同时把这篇文章的 item 对象(new-items 输出里对应的那个元素,原样即可,包含 full_text
   也没关系)存到另一个临时文件,比如 `/tmp/summizer_item_<n>.json`。

   ### 3c. 合并进知识图谱

   ```bash
   python -m src.main merge-graph --item-file /tmp/summizer_item_<n>.json --extraction-file /tmp/summizer_extraction_<n>.json
   ```
   这一步会把实体/关系合并进 `data/graph.json`,并把这篇文章标记为已读(不会再被
   `new-items` 返回)。

   ### 3d. 如果没有可抽取的关系

   直接标记已读,不用建图谱:
   ```bash
   python -m src.main mark-seen --url "<文章链接>" --title "<文章标题>"
   ```

4. 所有新文章处理完之后,重新生成图谱可视化:
   ```bash
   python -m src.main graph
   ```

5. **只有在云端定时任务里运行时**(不是用户本地手动开的会话),才需要执行这一步 —— 把这次
   跑出来的结果同步回 GitHub,这样用户本地 `git pull` 就能看到。云端沙盒是全新环境,没有
   git 身份,先配置一个机器人身份(不要用用户本人的名义提交):
   ```bash
   git config user.email "summizer-bot@users.noreply.github.com"
   git config user.name "Summizer Bot"
   git add data/ web/
   git commit -m "Summizer: 自动更新 $(date +%Y-%m-%d) 的文章与图谱"
   git push
   ```
   如果这一步新文章数量是 0(第 2 步 `new-items` 输出为空),不用 commit/push,直接结束。
   本地手动运行时跳过这一步,文件已经在本地了,不需要 git 操作。

6. 结束时用几句话总结这次跑了几篇文章、生成了哪些文章文件、图谱新增了哪些实体/关系,方便
   用户回来查看时快速了解产出。

## 注意事项

- 每篇文章的分析和抽取要分开独立完成,不要图快把多篇文章的内容混在一起写。
- 全文如果抓取失败或者过短(new-items 已经在源头过滤了小于 300 字符的),不会出现在结果里,
  不用额外处理。
- 不要自动把生成的文章发布到任何网站或社交平台 —— 只生成文件,发布由用户自己手动完成。
- 图谱里的实体名尽量归一化(比如避免同一家公司出现 "SpaceX" 和 "SpaceX Inc." 两种写法),
  `src/graph_store.py` 里的 `normalize()` 会做一些基础的后缀清理,但同名判断主要还是靠你
  抽取时用词一致。
