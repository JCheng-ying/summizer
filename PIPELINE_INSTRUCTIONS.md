# Summizer 执行说明(给运行这个流水线的 Claude 看)

这份文档是给"定期跑一遍 Summizer"的 Claude 会话看的操作手册。每次运行都是一个全新的会话,
不记得之前发生过什么,所以每次都要完整照着这份说明走一遍。

## 背景

用户定期关注机器人/AI/太空经济/量子计算/能源等领域的十一个信息源,具体列表见
[README.md](README.md#信息源),配置在 `src/sources.py` 里。这套工具的目标:

1. 自动发现新文章,读全文,产出一篇中文成品分析文章,写作逻辑严格照着仓库根目录
   `style_reference.md` 里用户自己的写作风格模仿(连续论述 + 系统性拆解 + 显式"个人看法" +
   分层价值链投资分析),供用户复制去发布到自己的网站/平台。
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

   **先完整读一遍仓库根目录的 `style_reference.md`**——这是用户自己写过的三篇分析,是必须
   模仿的写作逻辑(不是模仿话题)。核心是:连续论述而不是固定小标题模板;开篇先点出这篇文章
   背后更大的命题;转述原文时明确用"文章指出/文章提出";系统性拆解用"第一…第二…第三…"嵌在
   段落里而不是 bullet list;技术解释要精确,类比是补充不是替代;**"个人看法:"要显式标出来**,
   专门放自己的框架、投资角度分析、和其他文章/话题的联系;投资角度是分层价值链拆解,允许点名
   原文没提到但确实在产业链上下游的公司;结尾要克制,不用"关键要点"式总结句。完整规则和例子
   都在 `style_reference.md` 里,照着那份文件的逻辑写,不要用旧的固定栏目模板。

   写文章前,先用 Glob/Read 扫一眼 `data/articles/` 目录里已有文件的标题,看这篇新文章有没有
   在产业链约束、技术路线、公司等方面和已有文章相关——如果有,要在文中明确点出联系(参考
   `style_reference.md` 里第三篇结尾"和第一篇的…类似"那种写法)。

   用 Write 工具把文章写入 `data/articles/<YYYY-MM-DD>-<英文slug>.md`(日期用今天,slug 从
   标题生成,小写连字符,可以用
   `python -c "from src.pipeline import slugify; print(slugify('原标题'))"` 生成)。标题
   直接用原文标题即可,链接放标题下面一行,然后直接进入正文——不需要额外的摘要行或免责声明
   footer。

   文章必须基于 `full_text` 的真实内容撰写,不要编造原文没有的事实、数字或对这篇新闻本身的
   公司名(投资角度延展产业链上下游公司时例外,见 style_reference.md 规则 7)。

   ### 3b. 抽取实体与关系

   只抽取原文中真实出现、有实际依据的实体和关系,不要编造或过度推测。如果文章没有明确的
   公司间关系(比如纯学术研究报道),relationships 可以是空数组 —— 这种情况可以跳过 3c,
   直接执行 3d(mark-seen)。

   把结果按下面的 schema 写成 JSON,存到一个临时文件(比如
   `/tmp/summizer_extraction_<n>.json`)。`sector_tags` 只能从这六个里选(见
   `src/graph_store.py` 的 `CANONICAL_SECTORS`,和 `style_reference.md` 规则 12 是同一套):
   机器人板块、AI板块、能源板块、量子计算板块、太空经济板块、edge AI板块 —— 一个实体可以挂
   多个,不相关的板块不要硬挂。`hot` 只在你确实知道这家公司是知名大盘股/极高知名度时填
   `"hot"`,不确定就留空,不要瞎猜;`ticker` 同理,不确定就留 `null`。

   ```json
   {
     "entities": [
       {"name": "实体名(用最常见/官方的英文名或通用简称)", "type": "company | technology | institution | product | person", "sector": "如 haptics / humanoid robotics 这种细分描述", "sector_tags": ["机器人板块"], "hot": "hot 或 cold 或不填", "ticker": "TSLA 或 null"}
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

   ### 3d. 如果没有可抽取的公司关系

   直接标记已读,不用建图谱:
   ```bash
   python -m src.main mark-seen --url "<文章链接>" --title "<文章标题>"
   ```

   ### 3e. 记录板块利好/利空信号

   这一步和 3b/3c 是分开的、独立的一步,不是互斥关系——只要文章的"个人看法"投资角度段落里
   点名了某个板块,就要执行这一步(不管前面 3b 有没有具体公司关系可抽取)。对文章里提到的
   每一个板块,各跑一次:
   ```bash
   python -m src.main record-signal --sector "机器人板块" --description "一句中文说明为什么这篇文章利好/利空这个板块(呼应文章里"个人看法"段落的判断)" --item-file /tmp/summizer_item_<n>.json
   ```
   一篇文章可能对应零到多个板块信号,原样照抄文章里已经写好的板块判断即可,不用重新想。

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
