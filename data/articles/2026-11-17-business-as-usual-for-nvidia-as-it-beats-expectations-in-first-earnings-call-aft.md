# Business as usual for Nvidia as it beats expectations in first earnings call after Jensen Huang’s resignation
https://siliconangle.com/2026/11/17/business-as-usual-for-nvidia-as-it-beats-expectations-in-its-first-earnings-call-after-jensen-huangs-resignation/

这次财报真正要回答的问题不是"英伟达这季赚了多少",而是"AI 基础设施周期的需求端,会不会因为一家公司的治理危机而松动"。如果在创始人突然离开、股价连跌六周、华盛顿政治风向变化的情况下,英伟达依然能上调全年指引,那说明这一轮周期的驱动力已经不依赖某一个人,而是来自客户侧真实的资本开支计划。

文章指出,英伟达第三财季调整后每股收益 2.68 美元,高于华尔街预期的 2.48 美元;收入 1158.4 亿美元,同比增长超过 103%,高于 1091 亿美元的一致预期。其中数据中心业务收入 1076 亿美元,高于市场预期的 1018.7 亿美元。对本季度,英伟达预计收入增长约 90% 至 1300 亿美元,虽然环比增速放缓,但仍高于 1251 亿美元的预期。最受关注的是全年指引:投资者原本担心公司会放弃此前对截至 2028 年 1 月财年 70% 增长的预测,结果临时 CEO Colette Kress 反而把它上调到 75%,并强调这个预测"考虑了数据中心就绪情况、客户需求的强度和持久性,以及客户获取资本的能力"。盘后股价上涨超过 4%,止住了一周的跌势,但文章也提醒,本月股价仍下跌 24%,上周五完成了自 2012 年以来最长的连续六周下跌,而且这轮下跌在黄仁勋丑闻曝光前几周就已经开始,背后还有对 AI 行业放缓的担忧和中期选举后华盛顿的政治变化。

文章提出了几个比总量更有信息量的细节。第一是客户结构,Kress 表示 OpenAI、Anthropic 等前沿实验室预计今年占数据中心收入约 15%,说明它们越来越多地自建数据中心而不是从云厂商租用;她还提到 Anthropic 的年化收入在 10 月底达到 1810 亿美元。第二是 neocloud 的融资结构,文章指出 neocloud 购买芯片的大量资金来自一张复杂的融资网络,其中很多可以追溯回英伟达自己;Kress 说公司仍在帮助 neocloud 和前沿实验室获取土地、电力和数据中心容量,并可能在满足一定条件时与 neocloud 分享收入,目前对 neocloud 的总承诺超过 320 亿美元、期限到 2032 年,但只有在客户拿到融资、算力实际部署运行后才会生效。第三是毛利率,非 GAAP 毛利率 74.9%,高于 74% 的预期,但环比仍在下降,公司归因于最新一代 Rubin GPU 的产能爬坡。人事方面,董事长 Harvey Jones 在会上重申董事会无意让黄仁勋回任 CEO,而黄仁勋在 X 上表示如果董事会认为合适他愿意回来;Susquehanna 分析师 Chris Rolland 则认为他可能以顾问等其他身份回归。

个人看法:这次财报和今天早些时候写的 [董事会不让黄仁勋复职](2026-11-17-nvidia-says-it-doesn-t-plan-to-reappoint-jensen-huang-as-ceo.md)、[开源战略不变](2026-11-17-nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huang-s-exit.md) 是同一场电话会的不同切面,放在一起看,英伟达给市场的信号很一致:人事问题切割,业务口径不变。我在 [周二该回答的问题](2026-11-16-all-the-questions-nvidia-should-answer-on-tuesday-but-probably-won-t.md) 那篇里关心的几件事,这次有了部分答案——需求和指引没问题,但对 neocloud 的融资支持并没有收缩,反而给出了 320 亿美元承诺和"收入分成"的新提法。

先找瓶颈。从这份财报看,GPU 本身已经不是瓶颈,Kress 在指引里列出的三个约束本身就很说明问题:第一是数据中心就绪,也就是土地、电力和机房能不能按时交付;第二是需求的持久性;第三是客户获取资本的能力。也就是说,真正卡住出货节奏的,是下游客户能不能建好机房、能不能融到钱。这和之前 [Nebius 400 亿美元扩张](2026-11-12-nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending.md)、[英伟达为 Nscale 做担保人](2026-11-01-nvidia-weighs-playing-the-cosigner-for-nscale-s-ai-data-center-in-west-virginia.md) 是同一条线:英伟达在用自己的资产负债表去疏通客户侧的资金瓶颈。这种做法短期撑住了收入,但也意味着一部分需求是"供应商融资"出来的,一旦资金面收紧,这部分最先受影响。

所以对 AI板块 我会分三层看。第一层是英伟达和它的上游(台积电、SK hynix、Micron 的 HBM),75% 的全年指引说明订单能见度仍然很高,Rubin 爬坡压低毛利率反而说明新一代产品在放量,这一层仍是确定性最强的。第二层是 neocloud 和前沿实验室自建,前沿实验室占 15% 意味着 OpenAI、Anthropic 这类客户正在变成直接买家,CoreWeave、Nebius 这类 neocloud 则高度依赖英伟达的融资支持,它们的弹性最大,风险也最大——320 亿美元承诺"有条件生效",本身就提示了它们的融资并不轻松。第三层是解决"数据中心就绪"这个瓶颈的那一层,也就是电力和机房建设,这也是我会把信号同时挂到能源板块的原因:英伟达明确在帮客户找土地和电力,说明电网接入和现场发电仍是出货的前置条件,Vertiv、Eaton、GE Vernova 以及 [Anthropic 签燃气发电机](2026-11-09-anthropic-signs-3-4bn-gas-generator-deal-to-support-1-7gw-of-data-center-power.md) 这类现场电源方案都在这一层。

现在还早,一份好财报止住了跌势,但没有改变股价已经处在 2025 年 7 月以来低位这个事实。值得跟踪的是下一季的毛利率能不能在 Rubin 爬坡后回升,以及 neocloud 承诺里有多少真正"生效",这两个数字比收入增速更能说明这一轮周期的质量。
