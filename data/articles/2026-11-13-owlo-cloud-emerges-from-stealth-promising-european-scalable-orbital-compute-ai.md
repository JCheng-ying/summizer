# OwlO Cloud emerges from stealth promising European scalable orbital compute & AI
https://www.datacenterdynamics.com/en/news/owlo-cloud-emerges-from-stealth-promising-european-scalable-orbital-compute-ai/

（说明：这篇主要基于 OwlO Cloud CEO 接受 DCD 独家采访的说法，公司规划和市场判断都来自公司自身，未经独立验证，公司也没有透露融资情况。）

这篇文章值得一读，不是因为又出现了一家轨道数据中心创业公司，而是因为它提出了一个和主流叙事明显不同的商业逻辑：轨道算力不一定要和地面数据中心比拼"谁的电更便宜、谁的散热更好"，而可以只做一件地面做不了的事——在数据产生的地方就地处理太空数据。如果这个逻辑成立，轨道算力的第一批真实需求会是 edge 计算，而不是 AI 训练。

文章指出，卢森堡的太空初创公司 OwlO Cloud 结束隐身状态，宣布与卫星制造商 Thales Alenia Space（Thales 和 Leonardo 的合资公司）以及卢森堡的太空网络初创公司 Edge Aerospace 分别签署了合作备忘录，目标是在 2030 年前建成一个包含十多颗"Orbital Cloud Node"卫星的计算星座，从 2030 年起为欧洲太空供应链提供兆瓦级的弹性算力，使用的是 Edge Aerospace 为轨道数据中心设计的多千瓦级太空计算机。OwlO 也参加过 Thales Alenia Space 的太空业务加速器项目。

文章认为，OwlO 刻意和美国同行的叙事拉开距离。很多轨道数据中心公司宣称凭借太空中独有的太阳能和辐射散热，可以让地面数据中心过时，这类说法已经被一些有分量的声音否定。OwlO CEO Jason Aspiotis 的说法则务实得多：第一，它不和地面算力竞争，所以不需要解决大规模卫星扩展的问题，单个节点只是 10kW 级别；第二，它也不追求和地面数据中心一样的算力单价；第三，它的单位经济性基准是"把 EB 级数据传回地球的成本"，以及原始数据没有被及时处理成情报所造成的机会成本，服务对象是国防、民用、科研和商业的太空数据用户，具体场景包括对地观测、海上监视、灾害响应和安全防务。他预计到 2035 年需要在轨道上解决数十兆瓦的算力需求。文章还提到，今年欧洲航天局等机构开始以前所未有的热情支持军民两用和主权能力，轨道算力在欧洲论坛上被讨论得越来越多。

个人看法：这和 style_reference 第一篇讨论 SpaceX 太空数据中心时文章最后的判断几乎一致——真正最先商业化的，是那些本来就发生在太空里的计算任务，第一批客户是国防、遥感和航天机构，而不是普通互联网用户。把最近几篇放在一起看，轨道算力现在大概分成三种路线：1.SpaceX 这类"把 AI 训练和推理搬上天"的大规模路线，比如 [SpaceX 为轨道数据中心定制 Kessel 机柜](2026-11-12-spacex-developing-custom-nvidia-vera-rubin-rack-dubbed-kessel-for-its-orbital-da.md)；2.Google 这类大厂的技术验证，比如 [Google 第一颗数据中心卫星上线](2026-11-01-google-s-first-data-center-satellite-is-online-and-writing-poetry.md)；3.OwlO 这种只做在轨 edge 处理、服务太空数据本身的小规模路线。先找瓶颈：对第三种路线来说，瓶颈不是散热板面积，而是下行链路带宽和地面站资源——数据量涨得比下行带宽快。所以解决这个瓶颈的那一层才是受益者：第一层是太空级的低功耗算力和抗辐射芯片，这直接挂到 edge AI板块，因为在轨处理本质上就是功耗受限环境下的边缘推理（AMD 的 Xilinx 太空级 FPGA、Microchip 的抗辐射处理器都在这条链上）；第二层是卫星平台和星间链路，Thales Alenia Space 这类卫星制造商，以及做光学星间通信的公司，属于太空经济板块；第三层是遥感数据的下游用户和数据服务商。和 [Novaspace 预测 2035 年前将发射 6500 颗对地观测卫星](2026-08-22-new-novaspace-forecast-6-500-eo-satellites-to-launch-by-2035.md) 放在一起看，对地观测卫星数量的增长就是在轨处理需求的来源。

不过现在还非常早，OwlO 签的只是备忘录，没有披露融资，2030 年的星座计划也只停留在规划阶段。值得关注的是它接下来几个月宣布的新合作伙伴里，有没有欧洲航天局或国防机构这样的实际付费客户，因为对这条路线来说，第一份政府订单比任何技术指标都更能证明需求是真实的。
