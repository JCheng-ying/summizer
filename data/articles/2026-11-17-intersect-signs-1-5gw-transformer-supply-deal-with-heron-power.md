# Intersect signs 1.5GW transformer supply deal with Heron Power
https://www.datacenterdynamics.com/en/news/intersect-signs-15gw-transformer-supply-deal-with-heron-power/

这篇新闻讨论的其实是 AI 数据中心电力系统里一个经常被忽略的瓶颈:不是发电,而是"把电变成服务器能用的电"的那一层设备——变压器。过去两年数据中心的交付周期里,大型变压器的排产经常是最长的一项,如果固态变压器能把这一环换掉,改变的不只是一个零部件,而是整个"speed to power"的节奏。

文章指出,Alphabet 旗下的清洁能源和数据中心开发商 Intersect 与美国固态中压变压器制造商 Heron Power 签署产能协议,预留 1.5GW 的 Heron Link 变压器,预计 2028 年开始交付。这些设备将在 Heron 位于加州 Morgan Hill 的 Factory One 生产,工厂设计年产能为 1 万台 Heron Link,对应超过 40GW,量产预计在 2027 年底开始。Intersect 创始人兼 CEO Sheldon Kimber 的说法是,这个平台会通过提高能量传输效率来加快"speed to power",同时减少维护和停机时间。文章还提到,两家公司此前已经有超过 18 个月的技术和商业合作。

技术上,文章描述 Heron Link 是一种基于最新宽禁带半导体的模块化兆瓦级功率转换器,单台 5MW,主打高功率密度和易维护(这些是公司自己的说法)。这里值得拆开说一下它和传统变压器的区别:传统工频变压器本质上是铁芯加铜线圈,靠电磁感应在 50/60Hz 下变压,体积大、重量大、依赖取向硅钢和大量铜,而且是按订单定制、排产很长;固态变压器则是用 SiC/GaN 这类宽禁带功率半导体做高频开关转换,中间经过高频变压和整流逆变,体积和重量都可以大幅缩小,还能直接输出直流,天然适合接储能电池和光伏这类直流源。这就是为什么文章强调它对"可再生能源储能和数据中心开发商"都有意义。

文章还给出了 Heron 的客户清单:上个月和 Vantage 签了在其 hyperscale 数据中心组合里部署超过 1GW 变压器的协议;去年 6 月和 Crusoe 签了意向书,为德州的 Stargate 数据中心园区提供功率转换技术。Heron 由前 Tesla 高管 Drew Baglino 在 2024 年创立。至于 Intersect,它在德州和加州有 2.2GW 运营中的光伏和 2.4GWh 运营或在建的储能,2024 年开始和 Google 合作开发数据中心配套的可再生能源和储能,去年 12 月被 Alphabet 以据报道 47.5 亿美元收购,今年 3 月完成交割;今年 6 月,双方在德州 Gray 和 Roberts 两县开工建设 Meitner Energy Center,把数据中心和新增发电设施建在同一地点。

个人看法:这条新闻和之前几篇正好能串起来。[Google 与 Quaise 签地热 PPA](2026-11-17-google-inks-50mw-geothermal-ppa-with-quaise-in-oregon.md) 那篇说明 hyperscaler 在锁定发电端;[Caterpillar 扩产大型往复式发动机和燃气轮机](2026-11-05-caterpillar-seeking-to-expand-production-of-large-reciprocating-engines-and-turb.md) 说明现场发电设备也在被抢;而这篇说明连电力转换设备也开始被"预留产能"。Alphabet 的做法很清楚:收购 Intersect 把"发电+储能+数据中心"三件事放在一个公司里,然后再从源头锁定变压器产能,这是一种向电力供应链上游垂直整合的思路,和 [behind-the-meter 资产估值那篇](2026-11-17-sponsored-ascend-analytics-launches-behind-the-meter-asset-valuation-for-data-ce.md) 讲的"数据中心自带电源"趋势一致。

从瓶颈的角度,我目前看到解决电力转换瓶颈的方式有三种:1. 传统变压器厂商扩产,比如 Hitachi Energy、Siemens Energy、Eaton、Schneider 等,确定性高但扩产慢;2. 固态变压器这种新路线,用半导体产能替代硅钢和铜线圈的产能,Heron 是这一路的代表,好处是理论上可以像电子产品一样批量生产,风险是还没有量产(2027 年底才开始);3. 架构层面的改变,比如数据中心内部转向 800V 直流配电,减少交流-直流转换的层级,这和 NVIDIA 推的高压直流供电方向是一致的,固态变压器天然能输出直流,所以第 2 和第 3 条其实是互相加强的。

所以受益的层次会是:第一层是能源板块里的电力设备,不管是传统变压器还是固态变压器,"把电送进机柜"这一层的订单都在被提前锁定;第二层是宽禁带功率半导体,固态变压器的核心是 SiC/GaN 器件,如果这条路线真的跑通,Wolfspeed、onsemi、Infineon 这类 SiC 器件厂商会多出一个兆瓦级的新应用场景;第三层是储能,因为固态变压器的直流特性让储能接入更顺畅,和 Intersect 本身的光伏加储能组合是配套的。对 AI 板块,这仍然是在缓解算力扩张的物理约束,但属于间接利好。需要注意的是,Heron 是一家 2024 年成立、还没量产的初创公司,1.5GW 是"预留产能"而不是已交付的设备,真正值得跟踪的信号是 2027 年底 Factory One 能否按时量产,以及首批设备在 Vantage 或 Stargate 园区的实际运行可靠性。
