# Anthropic signs $3.4bn gas generator deal to support 1.7GW of data center power
https://www.datacenterdynamics.com/en/news/anthropic-signs-34bn-gas-generator-deal-to-support-17gw-of-data-center-power/

这条新闻背后的命题是：前沿 AI 实验室正在被迫沿着产业链往下走。过去它们只租云算力，后来开始直接签数据中心，现在连发电设备都要自己买。当一家一向"只租不买"的公司开始囤燃气发电机组，说明电力已经成为比 GPU 更难拿到的资源。

文章指出（DCD 援引《金融时报》），Anthropic 签下一笔 34 亿美元的 Caterpillar 燃气发电机组交易，容量 1.7GW，合作方是德州设备供应商 OnePWR Solutions。OnePWR 两年前就下了这批订单，赶在最近一轮涨价之前，但缺乏完成交易的融资；Anthropic 没有只当 OnePWR 的客户，而是直接接手了 Caterpillar 的设备订单，发电机预计两年内到货，OnePWR 负责在 Anthropic 的数据中心做安装、工程和施工。文章称这是已知前沿实验室单笔最大的发电设备采购，目的是对数据中心组合有更大控制权。同时文章罗列了 Anthropic 的算力承诺：本月早些时候披露截至 2045 年的云和数据中心承诺达 8954 亿美元；据招股书，向 Google 租算力承诺 1213 亿美元、SpaceX 1205 亿、Amazon 1100 亿、Microsoft 449 亿；neocloud 方面与 Nscale 签了 446 亿美元（至 2033 年）、与 Lambda 签了 413 亿（至 2034 年），但 Nscale 需要为 Nvidia GPU 争取到合格融资，Lambda 需要及时落实设施租约；另外还有与 Fluidstack 的 500 亿美元协议以及与 TeraWulf、Hut 8 的合同。

TechCrunch 对同一事件的报道补充了两个视角：一是燃气轮机的交付积压已经排到 2030 年代初，电网接入排队同样漫长，所以这笔采购看起来像"最后手段"；二是风险——Google、Amazon、Microsoft、Meta 都在规划现场燃气电厂，美国数据中心到 2035 年的天然气消耗可能超过德国和日本之和，有分析师认为部分市场气价到本世纪末可能涨两倍以上，那时 Anthropic 可能会后悔。

个人看法：这篇和之前 [Caterpillar 扩产大型往复式发动机和燃气轮机](2026-11-05-caterpillar-seeking-to-expand-production-of-large-reciprocating-engines-and-turb.md)、[NTT Data 与 Bloom Energy 的燃料电池协议](2026-11-08-ntt-data-signs-900mw-fuel-cell-supply-deal-with-bloom-energy.md) 以及今天的 [挪威暂停数据中心并网](2026-11-09-norway-halts-grid-connection-applications-for-new-data-centers.md) 是一条完整的链：电网接不进去，就自己发电；燃气轮机排队到 2030 年代，谁手里有在途订单谁就有议价权，OnePWR 的订单之所以值钱，恰恰因为它是"锁定了旧价格和交付位置的在途产能"。我觉得 AI 数据中心获取电力的方式目前有三种：1. 等电网（最便宜但最慢，且越来越受政治约束）；2. 现场燃气发电（最快，但有气价和排放风险）；3. 燃料电池、储能、未来的小型核电等替代方案（规模和成本还在验证）。

投资角度先找瓶颈：瓶颈是发电设备的交付产能，而不是电力需求本身。那么受益的层次是：第一层是燃气发电设备制造商，Caterpillar、GE Vernova、Siemens Energy、Mitsubishi Heavy 这类掌握交付位置的公司，定价权在它们手里，利好能源板块；第二层是天然气上游和中游，钻探、管道、液化运营商，因为现场发电最终是把天然气变成算力；第三层是像 OnePWR 这样做现场电力 EPC 的集成商。对 AI 板块来说，这既是需求强劲的证据，也是成本上升的信号——前沿实验室的资本开支正在从轻资产租赁转向重资产，这在 IPO 前夕会被投资人仔细审视。值得跟踪的是 Anthropic 后续招股材料里是否单列发电资产，以及美国天然气价格走势。
