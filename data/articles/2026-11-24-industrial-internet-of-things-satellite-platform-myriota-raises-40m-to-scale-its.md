# Industrial internet of things satellite platform Myriota raises $40M to scale its constellation and expand
https://siliconangle.com/2026/11/24/industrial-internet-of-things-satellite-platform-myriota-raises-40m-to-scale-its-constellation-and-expand/

这篇融资新闻背后的命题是：太空经济里最先跑通商业模式的，未必是宽带和数据中心这类高带宽、高资本开支的方向，而可能是低带宽、低功耗、海量终端的工业物联网连接。当 AI 走向物理世界，它需要的不只是算力，还有来自矿山、油罐、牧场、离网光伏这些偏远现场的持续数据，而地面网络恰恰覆盖不到这些地方。

文章指出，澳大利亚公司 Myriota 宣布完成 C 轮第一部分 4000 万美元融资，由 Main Sequence Ventures、Hostplus 和澳大利亚国家重建基金公司（National Reconstruction Fund Corporation）共同领投，Funds SA 作为新投资者加入，公司累计融资超过 1.075 亿美元，本轮预计在 2027 年初完成交割。资金将用于扩建太空基础设施，包括研发和发射下一代卫星。文章介绍，Myriota 成立于 2015 年，它的平台不是单纯卖卫星链路，而是把四样东西打包：第一是卫星连接；第二是低功耗终端设备；第三是现场安装工具；第四是设备群管理软件。同一套核心技术既能追踪矿山设备和挂车，也能监测燃料罐、牲畜饮水和离网光伏。过去 12 个月，公司推出了 HyperPulse（一种覆盖全球的 5G 非地面网络 NTN 加地面网络服务）和 AssetHawk（坚固、长寿命的资产追踪器），并扩展到工业燃料等新垂直领域，目前在北美和拉美监测燃料部署，之后会扩展到 EMEA 和亚太。CEO Ben Cade 的说法是，随着 AI 进入物理世界，来自现场的数据会变得更加关键。文章也点明了竞争格局：这个市场由 Iridium、Orbcomm、Viasat 等老牌运营商主导，同时有越来越多厂商在做更便宜、基于标准的工业传感器连接。

这里有一个技术上值得说清楚的点：5G NTN 是 3GPP 把卫星纳入蜂窝标准体系的方向，意义在于终端芯片可以复用标准化的蜂窝模组，而不是每家卫星运营商各用一套私有协议和专用终端。这正是文章说的"更便宜、基于标准的连接"的底层逻辑——当终端成本和功耗降下来，追踪一个油罐、一个水槽在经济上才划算，工业 IoT 的规模才能从几万台扩展到几百万台。

个人看法：工业 IoT 卫星这条线，我觉得瓶颈并不在卫星本身，而在单个终端的经济性和部署成本。Myriota 的打法是把终端、安装、软件一起打包成交钥匙服务，本质上是在解决"装得起、维护得起"的问题，这比单纯多发几颗卫星更关键。这一点和之前 [Sophia Space 在 Kepler 星座上部署在轨计算软件](2026-11-20-sophia-space-launches-orbital-computing-software-across-kepler-satellite-constel.md)、[Google 的数据中心卫星上线](2026-11-01-google-s-first-data-center-satellite-is-online-and-writing-poetry.md)形成了一个对照：那几篇讨论的是把高算力搬上天，属于高资本开支、远期兑现的方向；而 Myriota 是低带宽、按设备收费、现在就有收入的方向。另一个和此前 [Deutsche Telekom 回应 SpaceX 直连手机挑战](2026-11-08-deutsche-telekom-ceo-welcomes-spacex-terrestrial-challenge-warns-it-will-cost-mu.md)类似的地方是，卫星和地面网络正在通过 NTN 标准走向融合，而不是各自为战。

从投资角度，受益的层次会是：第一层是卫星制造与发射，小卫星平台和拼车发射服务商（比如 Rocket Lab、SpaceX 的 Transporter 拼车任务）会因为这类中小星座的补星和换代需求受益，这直接挂在太空经济板块上；第二层是支持 NTN 的终端芯片和模组厂商，比如 Qualcomm、MediaTek、Nordic Semiconductor 这类做低功耗蜂窝/NTN 芯片的公司，这一层同时挂在 edge AI板块，因为现场传感器正是边缘数据的源头；第三层是能源板块里的离网场景，文章提到的离网光伏和燃料监测说明能源资产的远程运维正在数字化，但这一层只是 Myriota 的应用场景，对能源板块的拉动比较间接。需要提醒的是，4000 万美元在卫星行业是相当小的一轮，Iridium、Orbcomm、Viasat 的规模优势仍然很明显，Myriota 能否在价格和标准化上真正切出份额还需要时间验证。

现在还早，太空经济板块里这一细分方向的体量也不大，只能观望。值得关注的信号是 Myriota 下一代卫星的发射时间表和合作发射商，以及 C 轮剩余部分在 2027 年初交割时的规模——如果后续有大型能源或矿业公司的批量部署订单出现，那会是工业 IoT 卫星从试点走向规模化的一个更硬的证据。
