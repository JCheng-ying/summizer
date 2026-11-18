# Scripts can’t run AI factories: Dell moves cluster management from the server to the rack
https://siliconangle.com/2026/11/18/supercomputing-needs-rack-scale-management-dell-says-dellatsc26/

(利益相关说明:这篇是 theCUBE 在 SC26 上的访谈,原文披露这一段由 Dell 赞助,受访者都是 Dell 的产品管理负责人,下面涉及的产品规格和带宽增长数字都来自 Dell 自己的说法,未经独立验证。)

这篇文章背后的命题是:AI 基础设施的瓶颈正在从"买不买得到"转向"跑不跑得稳"。过去两年整个行业讨论的是 GPU 供给、HBM 产能、电力接入,默认只要硬件到位,算力就自然产生;但当一个集群从几百台服务器长到几万块 GPU、几十万个设备,真正卡住产出的是交付之后的运维——机柜、交换机、GPU、冷却系统能不能持续健康地运行。如果这个判断成立,AI 基础设施的价值就会有一部分从硬件本身转移到"让硬件持续可用"的那一层软件和服务上。

文章指出,Dell 电信系统业务产品管理副总裁 Andrew Vaz 的观察是,客户的需求已经从"采购供给"转向"真正把这些非常复杂的 AI 集群和数据中心立起来并运行起来",而且用几段脚本、手工、老办法去管理这些东西已经不可能了,工具集变得越来越重要。Dell 在 SC26 上发布了两个工具来回应这件事:Dell OpenManage Rack Scale 和 Dell Fabric Manager。

文章提出的核心变化是管理单元的升级。Dell AI 计算与网络方案产品管理总监 Saurabh Kapoor 的说法是,前一代产品 OpenManage Enterprise 是为服务器设计的,当时服务器就是计算单元;但过去 18 个月里世界很快转向了更大的系统,"机柜才是新的单位"。像 Nvidia 的 NVL72 这样的机柜,把计算、电源架、交换机和冷却液分配单元(CDU)打包成一个整体,所以管理软件也必须把一整个机柜当作一个对象来看。按文章给出的数字,OpenManage Rack Scale 首个版本就能管理 10 万个设备,而前代产品的上限是 8000 台服务器。可以把这件事理解为:一个 NVL72 机柜里任何一个部件出问题,影响的都不是一台服务器,而是 72 块 GPU 组成的整个 NVLink 域,所以故障的"爆炸半径"变大了,管理粒度必须跟着变。

第二个支柱是可观测性。文章指出,Dell 的 iDRAC 控制器从每台服务器上采集超过 320 项指标,另外有一个 AI 辅助的聊天机器人可以通过本地部署的大语言模型来查询这些遥测数据。Vaz 举了两个例子来说明为什么每一层都必须上报状态:第一是冷却,一次冷却液泄漏就可能毁掉价值数百万美元的设备;第二是网络,比如一个光模块快要坏了,用今天已有的指标是诊断不出来的,需要采集系统遥测数据、做关联分析、跑算法、训练模型,才能理解到底在发生什么。也就是说,预测性维护本身也变成了一个 AI 问题。

第三个支柱是网络。文章认为压力最终集中在网络上。Dell Fabric Manager 把和 Nvidia、AMD 一起验证过的参考设计转成可以直接部署的蓝图,并且可以适配不同的网络操作系统和交换芯片。Vaz 还提到,Agentic AI 正在改变流量形态,行业原本预测企业带宽会增长 3.5 倍,而他们实际看到的是九到十倍,流量"东西南北各个方向都在增长"。这个数字是受访者口头说法,没有给出统计口径,只能当作方向性信号看待。

个人看法:这篇文章和前一天读到的 [Dell bets liquid-cooled, software-defined storage can keep AI factories fed](2026-11-17-dell-bets-liquid-cooled-software-defined-storage-can-keep-ai-factories-fed.md) 以及 [Dell puts a single gateway between enterprise AI agents and the data they crave](2026-11-17-dell-puts-a-single-gateway-between-enterprise-ai-agents-and-the-data-they-crave.md) 可以连起来看:Dell 在 SC26 上的整体叙事是,自己不只是卖服务器的整机厂,而是要卖"AI 工厂"从存储、数据网关到机柜级运维的全套。这和之前写过的 Import AI 那篇里腾讯 ARGUS 监控万卡集群的逻辑是一样的——GPU 数量之外,调度、监控、自动诊断这一层软件正在变成规模化的前提条件。目前来看,集群运维这件事有三种做法:1. 硬件厂商自带管理软件,也就是 Dell 这次的路线,优点是和自家硬件、遥测接口深度绑定,缺点是在多厂商混合的环境里覆盖不全;2. 超大规模云厂商和大模型公司自研,比如腾讯 ARGUS,只服务自己;3. 独立的 DCIM/可观测性软件厂商,跨品牌但拿不到最底层的硬件遥测。对于大多数企业客户和新兴 neocloud 来说,第一种可能是最现实的,这也是 Dell 想把软件做成护城河的原因。

按"先找瓶颈,再找解决瓶颈的那一层"来拆:这篇文章里的瓶颈不是 GPU,而是机柜级系统的可用性——冷却泄漏、光模块故障、网络拥塞都会让一整个 NVLink 域停摆。受益的层次会是:第一层仍然是算力本身,NVL72 这种机柜级产品越普及,Nvidia 的系统级锁定越深,AMD 也在跟进类似的机柜方案;第二层是网络和光互联,如果 Agentic AI 带来的带宽增长真的接近九到十倍而不是 3.5 倍,交换机(Arista,参考之前的 [Arista's record quarter](2026-11-05-arista-s-record-quarter-shows-the-network-has-become-central-to-ai.md) 和 [Arista takes aim at distributed inference](2026-11-17-arista-takes-aim-at-the-next-ai-network-battleground-distributed-inference.md))、交换芯片(Broadcom、Marvell)和光模块厂商(Coherent、Lumentum 等)都是直接受益方,而光模块作为易损件的故障率问题也意味着替换需求;第三层是冷却和电源,文章专门点出冷却泄漏的损失,说明液冷 CDU 的可靠性和监测本身有价值,和之前 [Samsung 洽购 Modine](2026-11-13-samsung-in-talks-to-acquire-data-center-cooling-company-modine-manufacturing-rep.md)、[ZutaCore 的两相冷却](2026-11-16-sponsored-zutacore-unveils-z-o-at-sc26-zero-h-o-near-zero-cooling-energy.md) 是同一条线,Vertiv、Schneider 这种同时做电源和热管理的公司会更受益,这挂在能源板块上;第四层才是 Dell 这类整机厂自己,软件化能不能改善整机厂一向偏薄的利润率,是需要用财报去验证的事。所以这篇主要利好 AI 板块(算力基础设施和运维软件层),次要利好能源板块(冷却与电源系统的可靠性需求)。

不过也要克制一点:这是 Dell 赞助的访谈,10 万设备管理规模和九到十倍带宽增长都是厂商自己的说法,没有客户案例和第三方数据支撑。值得跟踪的信号是,后续 Dell 的财报里 AI 服务器订单是否开始搭配软件和服务收入单独披露,以及光模块厂商是否在财报里提到 AI 集群带来的替换和运维需求上升。
