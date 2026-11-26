# 8,208 GPUs deployed by Sharon AI for ESDS Software Solution in Australia
https://www.datacenterdynamics.com/en/news/8208-gpus-deployed-by-sharon-ai-for-esds-software-solution-in-australia/

这篇文章的价值不在 8208 块 GPU 这个数字本身，而在于它把一家小型 neocloud 的商业模型拆得非常透明：合同、交付、验收、计费、现金流，每一个环节的时间差都写出来了。这正好可以用来检验一个最近反复出现的问题——neocloud 的增长到底是真需求，还是靠资本开支提前透支出来的。

文章指出，Sharon AI 已经在悉尼为印度云服务商 ESDS Software Solution 安装了 8208 块 Nvidia B300 组成的集群，目前正在做最后测试，预计 12 月中旬交付，2027 年 1 月开始计费。这份合同是 2026 年 4 月签的，为期五年，Sharon AI 当时称合同金额为 12.5 亿美元。原本收入预计在 2026 年第三季度开始确认，但双方同意推迟到测试完成之后再验收。ESDS 每月向 Sharon AI 支付约 2100 万美元，同时从它自己的客户那里收取约 3000 万美元，也就是说 ESDS 每月有约 900 万美元的税前、扣除运营成本前收入，而且它已经把这部分算力以 take-or-pay 的方式转租给了下游客户。

文章接着拆了 Sharon AI 的财务：截至 9 月 30 日，公司的不动产和设备资产达到 16.8 亿美元，而 2025 年 12 月只有 8840 万美元，其中 13.85 亿是"在建工程"。公司在澳大利亚和新西兰共有 129MW 合同容量，包括 GreenSquareDC 的 15MW、Equinix 悉尼 SYD3 和 SYD5 的容量、NextDC 墨尔本 M3 的 72MW，以及新西兰一个未披露提供商的 14MW。第三季度收入 993 万美元，去年同期只有约 50.7 万美元，但运营亏损达到 3746 万美元。公司在财报里明确说自己处于"投资阶段"，投资活动现金流出持续超过经营现金流入。剩余履约义务为 38 亿美元，35% 预计在 24 个月内实现。另外 Nvidia 自己对 Sharon AI 有一份六年期 take-or-pay 承诺，支撑一个 72MW、4 万块 GB300 的部署，计划 2027 年初开始调试。

个人看法：这篇和 [AI data centers are becoming harder to build and neoclouds are feeling it](2026-11-25-ai-data-centers-are-becoming-harder-to-build-and-neoclouds-are-feeling-it.md)、[Nebius tests the neocloud playbook](2026-11-12-nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending.md) 讲的是同一种结构，只是规模更小、数字更清楚。我会把 neocloud 的风险拆成三段：第一段是建设风险，GPU 到货、机房就绪、通电，Sharon AI 13.85 亿的在建工程就卡在这一段；第二段是验收风险，这次 ESDS 收入从 Q3 推到 1 月，说明"装好了"和"能收钱"之间可能隔着一个季度；第三段是对手方风险，ESDS 自己也是转租方，它的 900 万月毛利依赖下游客户按 take-or-pay 付款，这是一条层层转包的链条。另外，Nvidia 用 take-or-pay 给 Sharon AI 托底，又是 [Nvidia clarifies when it will and won't keep financing neoclouds](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md) 里讨论的那种"供应商为客户背书"的循环融资。

先找瓶颈：这里的瓶颈是现金，而不是需求，合同在、算力也已经转租出去了，但钱要等到 2027 年才进来。所以对 AI 板块来说，这条信息说明需求侧确实有真实订单，算力基础设施（GPU、机房托管方如 NextDC、Equinix）仍然是确定性受益方；但小型 neocloud 本身的股权风险很高，属于高杠杆押注。值得跟踪的信号很具体：12 月中旬 ESDS 是否如期验收、1 月是否真正开始计费。
