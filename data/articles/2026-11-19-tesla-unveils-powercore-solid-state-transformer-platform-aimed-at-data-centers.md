# Tesla unveils Powercore solid-state transformer platform aimed at data centers
https://www.datacenterdynamics.com/en/news/tesla-unveils-powercore-solid-state-transformer-platform-aimed-at-data-centers/

这篇新闻背后的命题是：AI 数据中心的电力瓶颈正在从"有没有电"下沉到"电怎么进机柜"这一层，而变压器这个过去最不起眼的设备，已经成了整条供应链里交付周期最长的一环之一。谁能绕开传统变压器，谁就握住了一部分数据中心上线节奏的主动权。

文章指出，Tesla 发布的 Powercore 是一套中压系统，把固态变压器（SST）、开关柜和逆变器集成进同一个机箱，直流侧支持 800VDC 到 2,000VDC，交流侧支持 10kV 到 34.5kV，在 34.5kV 下最高可输出 7.4MW。Tesla 称产品在美国工厂制造，预计明年开始投运，工作温度范围 -40°C 到 55°C，质保最长 25 年。需要注意这些都是厂商自己的说法，尚未看到独立验证。

拆开来看，Powercore 对数据中心的价值主张其实有三层。第一是简化供电链路：传统做法是从中压馈线经过多级降压才到机柜，而文章说 Powercore 直接从馈线取电，通过一次变换输出 800VDC 给服务器。这和 Nvidia 正在推的 800VDC 机柜供电架构是同一个方向，所以文章特别提到 Tesla 正在与 Nvidia 合作，按 DSX Ready 计划认证这套系统；截至 9 月，Tesla 的 Megapack 2XL 已是该计划认证的三套储能系统之一。第二是电网稳定性：Powercore 可以和 Megapack 搭配，用构网型（grid-forming）控制提供合成惯量和无功支撑。Tesla 能源与充电负责人 AJ Booth 的说法是，AI 训练负载波动剧烈，加上 Powercore 和 Megapack 之后，局部电网反而比不建数据中心时更"硬"。第三是保护速度：Tesla 称 Powercore 内置了业内首个固态断路器，100 微秒内切断故障，比传统设备快一千倍。

文章最关键的一句其实是 Tesla 的定位：传统变压器的供货周期因为数据中心需求已经拉长到最长四年，Powercore 被包装成绕开这条供应链的方案。文章也列出了竞争格局，新玩家有 DG Matrix 和 Heron Power，传统电力设备商有 Eaton 和 Siemens。

个人看法：这件事和前两天写过的 [Intersect 与 Heron Power 签 1.5GW 变压器供货协议](2026-11-17-intersect-signs-1-5gw-transformer-supply-deal-with-heron-power.md) 是同一条线索的两个侧面：固态变压器正在从概念变成采购清单上的品类，而且开始出现大额订单和大厂入场。按照"先找瓶颈，再找解决瓶颈的那一层"的思路，这里的瓶颈非常具体，就是中压到机柜这一段的电力电子设备交付周期，而不是发电量本身。受益的层次会是：第一层是能拿出量产能力的 SST 整机厂商，Tesla 的优势在于它本来就有 Megapack 的储能制造和电力电子规模，Eaton、Siemens、Schneider、ABB 这类传统厂商则有渠道和认证优势，Heron Power、DG Matrix 这类初创公司要证明的是量产和可靠性；第二层是 SST 上游的功率半导体，固态变压器的核心是高压 SiC/GaN 开关器件，Wolfspeed、onsemi、Infineon、STMicro 这条线会跟着受益；第三层是 800VDC 生态，也就是 Nvidia 主导的下一代机柜供电标准，服务器电源、母线、直流断路器都要重新设计，Vertiv、Delta 这类电源厂商会被卷进来。

这条新闻主要利好能源板块，因为它直接解决数据中心的电力接入和电网稳定问题，而且储能+构网控制的组合让数据中心从"电网负担"变成某种"电网资产"，这对审批和并网节奏都有意义。间接利好 AI 板块，因为供电链路缩短意味着数据中心建设周期可能缩短。但需要克制：Powercore 明年才开始投运，7.4MW 一台对于动辄几百 MW 的园区意味着要大规模部署，固态变压器在 25 年寿命内的实际可靠性还没有长期运行数据，传统变压器之所以慢，部分原因恰恰是它可靠。现在还是观望阶段，值得关注的是 Nvidia DSX Ready 认证是否落地，以及第一个公开的大型数据中心客户订单。
