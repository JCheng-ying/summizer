# Summizer

定期从机器人/科技领域的几个信息源里发现新文章,交给 Claude 读全文、写成中文投研分析文章,
同时把文章里提到的公司/技术/机构关系持续累积进一张可视化的知识图谱。

## 信息源

机器人/AI 综合:
- The Robot Report - Haptics 分类(用主站 `/feed/` 按 category 过滤,因为分类专属 feed 被 Cloudflare 拦截)
- ScienceDaily - Robotics
- IEEE Spectrum - Robotics
- Import AI(Substack)—— 偏宏观/产业,适合投资角度分析
- DeepLearning.AI - The Batch,Research 标签 —— 偏研究类文章(没有 RSS,`src/sources.py`
  里对这个源做的是轻量 HTML 列表页抓取,不是 feedparser)
- TechCrunch - Artificial Intelligence 分类
- SiliconANGLE —— 偏企业级 AI/云/基础设施

太空经济板块:
- SpaceNews
- NASASpaceFlight.com

量子计算板块:
- The Quantum Insider

能源板块 / AI 基础设施:
- DataCenterDynamics

没有加 CNBC 通用科技版和 SEC EDGAR——前者覆盖面太杂(消费电子、社交媒体八卦都混在一起),
后者是财报文件库不是文章流,不适合现有的 RSS/HTML 列表抓取机制。

## 架构

Python 只做机械性的工作,**不调用任何付费 AI API**——抓取全文之后交给正在跑这个任务的
Claude(Claude Code 会话)直接阅读、撰写、抽取,不需要 `ANTHROPIC_API_KEY`。

```
src/sources.py       RSS 抓取 + 分类过滤
src/state.py          已读文章去重(data/seen_urls.json)
src/fetch_article.py  全文抓取(trafilatura,失败时退回 RSS 摘要)
src/graph_store.py    知识图谱的合并/持久化(data/graph.json)
src/graph_viz.py       生成力导向关系图(web/graph.html,自包含,不依赖 CDN)
src/pipeline.py         把以上几块串起来的辅助函数
src/main.py               CLI 入口
```

## 安装

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 首次使用

先建立基线,把当前 RSS 源里已有的文章标记为已读,避免第一次运行就处理几十篇历史文章:

```bash
python -m src.main init
```

## 日常运行

**不要自己手动跑 Python 分析部分** —— 把 [PIPELINE_INSTRUCTIONS.md](PIPELINE_INSTRUCTIONS.md)
丢给 Claude Code,让它按说明检查新文章、撰写分析、更新图谱。这个仓库已经配置了定时任务
自动做这件事(见下方"定时任务")。

如果想手动触发一次,直接开一个 Claude Code 会话说"按 PIPELINE_INSTRUCTIONS.md 跑一遍
Summizer"即可。

生成的文章在 `data/articles/`,是可以直接复制发布的成品 Markdown。写作逻辑不是固定模板,
严格照着 [style_reference.md](style_reference.md) 里用户自己写过的三篇分析去模仿(连续论述 +
"个人看法"显式标注 + 分层价值链投资分析 + 和其他文章互相引用),每次运行前都会重读这份文件。

查看知识图谱:**必须用真正的桌面浏览器(Safari/Chrome)打开 `web/graph.html`,通过 Finder
双击**,不要通过 Claude 聊天里的链接/自带预览窗口打开——Claude 自带的预览对项目文件夹之外
的本地文件只做静态快照,不会执行页面里的 JavaScript,打开会看到一个空壳(标题和侧边栏文字
在,但图谱和筛选按钮都不显示)。用 Finder 打开这个路径 `web/graph.html`,双击文件即可。支持
拖动节点、滚轮缩放、按关系类型/实体类型筛选、搜索、点击节点或连线查看关系来源和原文链接。
左上角有六个板块的切换 tab(机器人/AI/能源/量子计算/太空经济/edge AI),切换后只显示挂了这个
板块标签的实体,并列出这个板块最近的利好/利空信号(每条链到具体文章)。

图谱除了逐篇文章积累的实体关系,还有一层"板块底图"(每个板块热门/冷门股票 + 上下游供应链/
竞争关系),这层数据靠 [SECTOR_MAP_INSTRUCTIONS.md](SECTOR_MAP_INSTRUCTIONS.md) 定期刷新
(建议按季度财报节奏),和逐篇文章的更新是两条独立线。

## 定时任务

目标是用 `/schedule`(claude.ai 云端 routine)每天自动跑一遍,通过这个 GitHub 仓库同步结果——
但目前卡在 claude.ai 的 GitHub 连接器上(连接 GitHub 账号后仍然 403,看起来是平台侧问题,
不是账号权限配置错误),还没建成。当前用本地 `CronCreate` 应急(每天 7:13 跑一次),但这
只在某个 Claude Code 会话开着时有效,最长 7 天失效,不是真正的长期自动化。GitHub 连接器
问题解决后需要回来用 `/schedule` 补建云端 routine。

## 关于知识图谱的准确性

图谱里的实体关系是 Claude 从文章原文里抽取的,只收录原文明确提到的关系,不做推测编造。
同一家公司如果在不同文章里的英文名写法不完全一致(比如 "SpaceX" vs "SpaceX Inc."),
`graph_store.normalize()` 会做基础的后缀清理,但主要还是依赖抽取时用词保持一致。

## 免责声明

所有生成的文章和图谱内容仅用于个人投研参考,不构成投资建议。文章不会被自动发布到任何
网站或平台,发布环节由你自己手动完成。
