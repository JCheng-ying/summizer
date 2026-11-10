# Nvidia looks to tap Brightspeed central offices for inference network - report
https://www.datacenterdynamics.com/en/news/nvidia-looks-to-tap-brightspeed-central-offices-for-inference-network-report/

这条报道背后的命题是：AI 推理会不会像当年的 CDN 一样，从集中式大园区下沉到离用户更近的地方？如果会，那么电信运营商手里那些因为铜缆退网而闲置的老机房，可能会成为一种新的 AI 基础设施资产。

文章援引 The Information 的报道指出，Nvidia 向 Brightspeed 的母公司 Apollo Global Management 提出，把这家美国宽带运营商的老旧局端机房（central offices）改造为推理网络的边缘计算节点，双方正在交换信息、安排实地考察。Brightspeed 在美国有约 130 栋建筑，据报道这些站点合计可以容纳最多 1GW 的 GPU 算力，但需要大规模升级电力和冷却设施，可能还要变更许可；首批改造容量最早可能在 2027 年一季度上线，站点里还会部署 Groq 的硬件——Nvidia 与这家 AI 芯片初创公司有一项重要的技术授权。

文章解释了为什么局端机房会空出来：Brightspeed 成立于 2021 年，是 Apollo 收购 Lumen 在 20 个州的本地交换运营商业务后组建的，一直在把铜缆网络升级为光纤，而光纤网络需要的汇聚节点比铜缆少得多。全球运营商处理这些旧机房的方式不一：有的直接退出，市中心的拿去改住宅；Telefónica、Ziply 等则在改造为边缘托管设施。但文章也指出了硬伤：这些设施非常老旧、功率密度很低，而且原本不是按交流电设计的，改造工作量很大，很多运营商早已通过售后回租把产权卖掉了。文章最后提到，两家公司此时处境都不轻松：Brightspeed 刚换了 CEO，有报道称其接近破产；Nvidia CEO 黄仁勋则深陷与疑似中国间谍的婚外情丑闻。

个人看法：这篇和之前 [Akamai 拿到 Anthropic 大单](2026-11-09-akamai-predicts-revenue-to-exceed-7bn-in-2028-driven-by-cloud-infrastructure-ser.md) 可以放在一起看，都是"分布式推理"这条线索：训练需要吉瓦级集中园区，但推理更看重延迟和就近部署。目前推理下沉大概有三种载体：1. CDN/边缘网络公司的现有节点（Akamai）；2. 电信运营商的局端机房和基站机房（这篇的 Brightspeed）；3. 终端设备本身（手机、PC、汽车上的端侧模型）。第二种的优势是位置好、光纤到位、有冗余，劣势是电力密度太低，1GW 分摊到 130 栋楼，平均每栋接近 8MW，对一个原本为电话交换设计的机房来说是数量级的改造。

投资角度先找瓶颈：这里的瓶颈不是 GPU，而是"老机房的电力和冷却升级"，以及运营商自身的资金状况。如果这类改造真的大规模推开，受益层次会是：第一层是机房电力和冷却改造设备，包括直流转交流的电源系统、UPS、配电以及适合小空间的液冷方案（Vertiv、Eaton、Schneider 这类），这挂能源板块；第二层是推理芯片，Nvidia 和这次被点名的 Groq 低延迟推理架构，利好 AI 板块；第三层是拥有大量局端机房产权的运营商和基础设施基金。对 edge AI 板块，这是一个"推理边缘化"有大厂主动推进的信号。不过目前只是报道中的意向，Brightspeed 财务状况不佳、Nvidia 正处于丑闻之中，都可能让事情搁浅。值得跟踪的是 2027 年一季度是否真有首批站点上线，以及其他运营商（如 AT&T、Verizon、Lumen）有没有类似动作。
