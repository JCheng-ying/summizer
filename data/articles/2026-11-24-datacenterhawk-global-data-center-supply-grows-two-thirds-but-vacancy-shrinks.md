# DatacenterHawk: Global data center supply grows two-thirds, but vacancy shrinks
https://www.datacenterdynamics.com/en/news/datacenterhawk-global-data-center-supply-grows-two-thirds-but-vacancy-shrinks/

这组数据回答的是"AI 数据中心是不是建过头了"这个问题的另一面:供给端创了纪录,但需求吸收得比建得还快。如果这个判断成立,那么当下市场担心的"产能过剩"至少在托管(colocation)这一层还没有出现,真正稀缺的仍然是能尽快交付的、已经通电的容量。

文章指出,根据 DatacenterHawk 的 2026 年第三季度全球数据中心市场报告,已投运的托管容量(已建成或已预租)在第三季度达到 77GW,已经超过 2025 年全年的 51GW,全年供给增长接近三分之二。但与此同时,空置率几乎减半,从去年的 3.5% 降到 1.8%,新容量一建好就被吸收。另外还有 9.4GW 今年在建的托管电力容量尚未租出。分地区看,全球每个主要区域的租赁量都已超过 2025 年全年;按体量算增长最快的是中东,其次是欧洲和亚太并列,拉美第三,北美最后。但绝对量上北美仍然遥遥领先,第三季度租出创纪录的 13.5GW,亚太 3.4GW,欧洲 1.1GW,中东只有 232MW,拉美 11MW。吸收量前四的市场都在美国,其中三个在德州:新罕布什尔的 Portsmouth 居首,之后是 Austin、Dallas-Fort Worth 和 West Texas;北美以外只有墨尔本挤进第五。

文章还给了三个结构性变化。第一是亚太,第三季度租赁量已超过 2025 年全年,租金明显上涨,DatacenterHawk 把它归因于区域内容量稀缺,neocloud 愿意为更快交付支付溢价。第二是欧洲,北欧的租赁份额升到接近一半(49%),超过了传统的 FLAPD 市场(法兰克福、伦敦、阿姆斯特丹、巴黎、都柏林),后者只占今年至今租赁量的 23%。第三是超大规模云厂商现在租的比自己建的多:租赁容量从 2025 年的 37GW 增长到 2026 年的 52GW,自建容量也在增长,从 30GW 到 39GW。

个人看法:这篇和 [Cleanview 的 Q3 美国开工数据](2026-11-18-cleanview-us-data-center-construction-slows-in-q3-2026-following-record-breaking.md) 放在一起看比较有意思。Cleanview 看到的是第三季度新开工环比回落,DatacenterHawk 看到的是投运和租赁都在创新高、空置率跌到 1.8%——两者并不矛盾,一个是"开工"的节奏,一个是"成品"的吸收,恰恰说明问题不在需求,而在能多快把容量交付出来。先找瓶颈:1.8% 的空置率意味着市场上几乎没有"现货",所以真正的瓶颈是"已通电、可立即交付"的容量,而 neocloud 在亚太愿意付溢价换速度,就是这个瓶颈的价格信号。目前来看超大规模云厂商获取容量有三种方式:1. 自建,控制力强但周期长,受电网接入和许可审批拖累;2. 向托管商长期预租,把建设风险转给开发商,今年这一项增长更快;3. 通过 neocloud 间接获取算力,也就是 CoreWeave、Nebius 这一层。租赁超过自建,说明大厂在用资产负债表外的方式换速度,这一点利好托管商,但也意味着开发商承担了更多融资和建设风险,和之前 [NVIDIA 澄清何时继续为 neocloud 融资](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md) 讨论的是同一条风险链。

欧洲的变化我觉得更值得注意。北欧拿走近一半租赁量,本质上是电力和气候在选址:便宜的水电风电和自然冷却。但北欧本身也不是没有约束,挪威此前已经 [暂停新数据中心的并网申请](2026-11-09-norway-halts-grid-connection-applications-for-new-data-centers.md),而 [CBRE 认为米兰将超过都柏林](2026-11-17-cbre-milan-set-to-overtake-dublin-as-fifth-largest-data-center-market-in-europe-.md) 也说明 FLAPD 之外的二线市场在接力——FLAPD 份额下滑,很大程度上是因为这些城市拿不到电,而不是没人想去。

所以受益的层次会是:对 AI 板块,第一层仍然是 GPU 和网络,空置率这么低,说明已建成的容量都会被填满,最终转化为 Nvidia、AMD、Broadcom 的芯片采购;第二层是托管商和开发商,Equinix、Digital Realty 以及 NTT DATA、AirTrunk 这类在亚太、北欧有现成通电园区的运营商议价能力最强,能涨租;对能源板块,第三层是能缩短"拿到电"时间的环节,包括变压器、开关设备、现场发电和储能,德州连续占据吸收榜前列,也和德州相对快的电力接入有关。这里需要说明,DatacenterHawk 只统计托管市场,不覆盖超大规模厂商自建之外的全部需求,文章也没有披露租金涨幅的具体数字。

现在一个季度的低空置率还不足以说明周期没有拐点。值得跟踪的信号是那 9.4GW 在建未租容量的去化速度,如果它在接下来一两个季度也被迅速租走,说明需求真的跑在供给前面;如果开始积压,那才是要警惕的时候。
