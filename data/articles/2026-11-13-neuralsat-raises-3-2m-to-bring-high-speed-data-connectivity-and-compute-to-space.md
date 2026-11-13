# NeuralSat raises $3.2M to bring high-speed data connectivity and compute to space
https://siliconangle.com/2026/11/13/neuralsat-raises-3-2m-to-bring-high-speed-data-connectivity-and-compute-to-space/

这篇文章讨论的是太空算力里一个比"把数据中心搬上轨道"更务实的方向：与其在太空里建大型 AI 数据中心，不如先做卫星之间的数据中继和边缘计算网络，让本来就产生在太空里的数据就近处理、就近转发。这条路线如果走通，太空计算的第一批真实收入可能来自"网络"而不是"算力集群"。

文章指出，德国初创公司 NeuralSat GmbH 完成 290 万欧元（约 320 万美元）的 pre-seed 融资，由 Capnamic 和 Bayern Kapital 领投，ZOHO.VC、Robin Capital、不来梅的发展银行 BAB、Mission E 和 KIEMIS Holding 跟投。公司 2026 年初才成立，计划建设一个由 72 颗卫星组成的数据中继与处理网络，让其他卫星运营商把计算和通信卸载上来，通过光学和高频无线电链路提供最高每秒 50GB 的传输能力，支持实时边缘处理、为商业和国防客户托管负载，以及对地观测、信号情报这类对时间敏感的任务。融资将用于加速第一个在轨演示节点，计划 2027 年 10 月发射，之后再开始部署商业运营卫星。

文章把它放进了一个正在升温的竞争格局里：加拿大的 Kepler Communications 1 月推出了首个商业太空数据中继服务，8 月又发布了下一代光学中继网络；被量子计算公司 IonQ 在 2026 年初收购的 Skyloom 已经在低轨部署了 84 个光学终端和一套中继架构；Starcloud（前身 Lumen Orbit）8 月以 23 亿美元估值融资 2.5 亿美元，2025 年底已经在轨测试过 Nvidia H100，现在正与 Nvidia 合作开发航天级芯片。文章也提到了物理约束：太空没有空气带走热量，只能靠大面积散热面辐射散热，加上发射载荷重量限制，太空计算未必能替代地面数据中心，但适合做边缘计算。在延迟上，文章给出的数据是，数据下传到地面往返需要 4 到 30 多毫秒，卫星间通信略快，约 3 到 30 毫秒；真正的优势在长距离传输上，星间链路比下传地面再走光缆网络快约 30% 到 50%。

个人看法：这篇和最近写过的 [Owlo Cloud 发布欧洲轨道算力计划](2026-11-13-owlo-cloud-emerges-from-stealth-promising-european-scalable-orbital-compute-ai.md)、[SpaceX 为轨道数据中心定制 Nvidia Vera Rubin 机柜](2026-11-12-spacex-developing-custom-nvidia-vera-rubin-rack-dubbed-kessel-for-its-orbital-da.md) 以及 [Google 第一颗数据中心卫星上线](2026-11-01-google-s-first-data-center-satellite-is-online-and-writing-poetry.md) 放在一起看，太空算力其实已经分成了两条路线：一条是 SpaceX、Starcloud 这种"大算力上天"，瓶颈是散热、辐射和维护；另一条是 NeuralSat、Kepler 这种"网络优先"，瓶颈是星间光链路的成本和星座部署的资金。后者和 style_reference 第一篇结尾的判断更吻合——最先商业化的是本来就发生在太空里的计算任务，第一批客户是遥感公司和国防部门。

从投资角度看，受益的层次会是：第一层是星间光通信终端和高频射频器件，因为不管哪家中继网络胜出，都要大量采购光学终端，IonQ 收购 Skyloom 也说明有人在提前卡这个位置，这利好太空经济板块；第二层是航天级计算芯片，Nvidia 与 Starcloud 的合作说明 GPU 厂商在往太空延伸，同时在轨低功耗推理也挂在 edge AI板块上，因为卫星上做实时处理本质上就是功耗和重量受限的边缘推理；第三层是发射服务，72 颗卫星的星座需要可负担的发射。但需要清楚的是，NeuralSat 只是 320 万美元的 pre-seed，连演示节点都要到 2027 年 10 月，这是一个非常早期的标的，信号意义大于商业意义。

现在还在观望阶段，但值得关注的是 2027 年 10 月 NeuralSat 的在轨演示能不能如期发射、实测速率能否接近每秒 50GB，以及 Kepler 和 Skyloom 有没有拿到对地观测或国防客户的大额中继合同——这会是"网络优先"路线是否先于"大算力上天"兑现的具体信号。
