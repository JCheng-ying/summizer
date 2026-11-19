# ChronoScale and STN form JV to develop data center campus in Odessa, Texas
https://www.datacenterdynamics.com/en/news/chronoscale-and-stn-form-jv-to-develop-data-center-campus-in-odessa-texas/

这笔交易背后的命题是：前沿 AI 实验室的算力采购，已经从"租几千张卡"变成了"签几百 MW、几十亿美元的多年合同"，而撑起这类合同的不再只是 GPU，而是一整套资本结构——合资、可转换优先股、客户本身参与融资。谁能把资本和交付能力打包，谁才能接到这种单子。

文章指出，Applied Digital 分拆出来的云业务公司 ChronoScale 与 STN（一家 AI 基础设施、GPU 云和企业 IT 公司）在德州敖德萨的数据中心项目上组建 50/50 合资公司，双方各出资 3.9 亿美元，项目将为一家未具名的"领先前沿 AI 实验室"提供算力。STN 是这个园区的原始开发商，2026 年夏天已经在现场部署了一个 Elemental 集装箱式模块化数据中心，容量 2MW、装有 1,024 张 Nvidia B300 GPU，看起来园区规划是部署多个这样的模块。项目分三期，第一期已下单，计划 2027 年上半年部署；各期 GPU 配置不同，合同收入平均每 MW 2,080 万美元，六年总价值预计 75 亿美元。

融资结构是这篇文章最值得细看的地方。文章提到 ChronoScale 另外获得 7.5 亿美元融资，其中 2.5 亿美元是股权，另有最高 5 亿美元的可转换优先股额度，部分普通股最初通过 Applied Digital 持有的票据结构发行。出资方包括那家前沿 AI 实验室本身、Nutanix、Empery Digital 和一家存储基础设施公司；高盛担任独家资本市场顾问和主配售代理。ChronoScale 的来历也有点特别：Applied Digital 1 月宣布分拆计划，通过把云业务与外骨骼公司 Ekso Bionics 合并的方式实现，Applied 保留约 97% 股权，分拆于 5 月 5 日完成。

个人看法：这里有三个信号需要分开看。第一，客户亲自下场出钱。前沿 AI 实验室既是 75 亿美元合同的买方，又是 ChronoScale 的股权投资方，这和 [CoreWeave 转向客户预付款和更短合同来为增长融资](2026-11-11-coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth.md) 是同一个趋势：neocloud 的资本成本太高，只能让客户分担资金压力，这本身说明资金是当前 neocloud 扩张的真实瓶颈。第二，每 MW 2,080 万美元的合同收入（六年）说明 GPU 云的单位经济性仍然可观，这是 AI 算力需求没有降温的硬数据。第三，结构的复杂度本身是风险：可转换优先股、票据结构、通过外骨骼公司借壳分拆，这些都意味着普通股东排在资本结构的后面。

所以按"先找瓶颈"的思路，这笔交易里的瓶颈是资本，而解决瓶颈的那一层是愿意提供结构化融资的客户和金融机构；对 Applied Digital 来说，它之前在 [美国唯一愿意接纳数据中心的小镇建设](2026-11-10-applied-digital-is-building-in-the-only-us-town-to-say-yes-to-data-centers.md) 时解决的是选址瓶颈，现在 ChronoScale 解决的是资本瓶颈。利好 AI 板块，因为 75 亿美元、几百 MW 级别的承诺直接转化为 GPU（文章提到 B300，后续期次配置不同）、网络和存储的采购，Nvidia、Dell/Supermicro 这类整机厂以及存储厂都在链条上；利好能源板块，因为德州西部敖德萨靠近二叠纪盆地，模块化数据中心逐期扩张意味着对当地电力和燃气发电的需求，这一点原文没有展开，是我的推测。

需要克制的是客户没有具名、第一期 2027 年上半年才部署，六年合同的履约能力要看 ChronoScale 能否按期交付。值得跟踪的是这家前沿实验室是谁，以及第一期能不能按时上线。
