# STTGDC launches 22MW data center in Noida, India
https://www.datacenterdynamics.com/en/news/sttgdc-launches-22mw-data-center-in-noida-india/

这是一条篇幅不长的投产新闻,但它把印度 AI 算力落地的方式说得很具体:不是超大规模云厂商自建,而是本土 neocloud 租用托管运营商的机房、往里放 GPU。

文章指出,亚太数据中心运营商 STTGDC 上周在北方邦 Noida 启用了 NOI2 数据中心,容量 22MW。Noida 园区的 1 号楼是 17MW,3 号楼在建,计划 28MW。印度本土 neocloud Neysa 将在 NOI2 租用容量,放置约 9000 块 GPU。STTGDC 印度业务在全国 10 个城市、34 座设施中共有超过 600MW 的关键 IT 负载在运营或开发中。印度区 CEO Bimal Khandelwal 表示,印度的数字化增长和 AI 普及正在带来更大规模、更算力密集的负载需求,公司在"需求之前投资"。资本结构上,投资机构 KKR 和新加坡电信运营商 Singtel 在今年 2 月从 ST Telemedia 手中完成了对 STT GDC 的全资收购,之后公司更名为 STTGDC。

个人看法:这条新闻可以和 [AirTrunk 的能源协议](2026-11-13-airtrunk-signs-1gw-energy-deal-with-european-energy-australia.md) 放在一起看,那篇里提到 AirTrunk 今年收购了印度运营商 Lumina CloudInfra 进入印度市场,说明亚太大型平台都在加码印度。先找瓶颈:印度市场的瓶颈不是土地和资本,KKR 和 Singtel 这样的买家愿意出钱;更可能是电力和 GPU 的获取。粗略估算,9000 块 GPU 如果是当代高端加速卡,加上服务器、网络和散热,整机功耗大致在十几到二十 MW 的量级,基本就能吃掉 NOI2 一栋楼的大部分容量(这是我自己的估算,原文没有给出 GPU 型号)。也就是说在印度,单个 neocloud 租户就能填满一栋楼,托管容量很快会变成稀缺资源。

所以对 AI 板块的受益层次是:第一层仍然是 GPU 供应方,Nvidia 是 Neysa 这类本土 neocloud 最直接的上游;第二层是像 STTGDC 这样手里有成规模已通电容量的托管运营商,它们是"有电的楼"的持有者;第三层是 Neysa 这类 neocloud,它们的价值取决于能不能把 GPU 卖成稳定的推理和训练服务。对能源板块的影响是间接的,600MW 的印度管线最终都要落到当地电网和备用电源上,但这篇没有提供电源方面的细节,我不单独挂能源信号。整体看这还是一条常规投产新闻,规模不大,值得跟踪的是 Noida 3 号楼的 28MW 是否也会被单一 AI 租户提前锁定。
