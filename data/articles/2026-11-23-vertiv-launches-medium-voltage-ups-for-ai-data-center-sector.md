# Vertiv launches medium-voltage UPS for AI data center sector
https://www.datacenterdynamics.com/en/news/vertiv-launches-medium-voltage-ups-for-ai-data-center-sector/

需要先说明:这是一条以厂商发布会内容为主的新闻,文中效率、储能时长等指标都来自 Vertiv 自己,目前未经独立验证。但它背后的命题值得写:AI 数据中心的供电保护正在从机房内部的低压 UPS,往上移到电网接入点的中压层,而推动这件事的不只是功率变大,还有 AI 训练负载那种剧烈波动对电网本身的冲击。

文章指出,Vertiv 推出了 PowerNexus MV UPS,这是一套户外中压平台,把三件事放进同一个系统:第一是不间断电源本身;第二是故障穿越(fault ride-through),也就是电网出现扰动或上游故障时保持负载不掉电;第三是 AI 功率平滑,用来吸收 AI 负载的快速波动。Vertiv 称这套设备安装在公用电网接入点,峰值运行效率最高可达 98.5%,配合电池储能可支持最长四小时的电池供电运行,因此可以显著减少对柴油发电机的依赖;输出电压质量按 IEC 62040-3 标准达到 Class 1。同时 Vertiv 还提供一套电力系统 CAD 模型,让客户在部署前先模拟系统行为和与电网的动态交互。Vertiv 电源管理业务高级副总裁 Kyle Keeper 把数据中心面临的问题概括为三点:并网排队推迟部署和收入、室内空间限制算力密度、电网要求不断变化。

文章提到,Vertiv 已经和 QTS、SoftBank 以及 Rosendin 在其位于意大利 Bologna 的全球电力研发和客户体验中心完成了几个演示项目,QTS 设施运营高级副总裁表示在概念验证中确认了系统在动态负载变化和电压扰动下能保持稳定供电。Vertiv 还计划在 Bologna 建一个中压实验室,用于中压 UPS、中压转 800VDC 以及电池储能等架构的全电压验证。文章最后点出竞争格局:GE Vernova、Tesla 和 On.energy 近几个月都推出了类似的中压 UPS 产品。

个人看法:这条新闻和前几天写的 [Tesla 发布 Powercore 固态变压器平台](2026-11-19-tesla-unveils-powercore-solid-state-transformer-platform-aimed-at-data-centers.md) 是同一个趋势的两个产品:数据中心的电力架构正在被重新设计,从"中压进来、多级降压、低压 UPS、再到机柜"的老链路,走向"中压直接保护、中压直转 800VDC"的新链路。按照"先找瓶颈,再找解决瓶颈的那一层"来看,这里卡住的不是发电量,而是三件更具体的事情。第一是负载波动:AI 训练在同步计算和通信之间来回切换,功率会在短时间内大幅跳变,电网运营商越来越不愿意接这种负载,功率平滑本质上是让数据中心"更像一个正常用户",这也是 [PJM 加快并网](2026-11-20-pjm-plan-could-cut-data-center-and-power-plant-grid-connection-times-to-12-month.md) 这类改革能落地的前提;第二是室内空间,把 UPS 搬到室外中压侧,省出来的机房面积可以放更多机柜;第三是柴油机,四小时电池备用如果成立,会逐步替代柴油备用电源,这在排放和许可审批上都更容易通过,和刚写的 [Alberta 新规](2026-11-23-alberta-gov-t-proposes-new-rules-for-large-load-data-centers.md) 这种越来越严格的地方规则方向一致。

受益的层次会是:第一层是能拿出中压电力电子整套方案的设备商,Vertiv、Schneider、Eaton、ABB、Siemens 这类传统厂商和 GE Vernova、Tesla 这类从能源侧切进来的厂商正在同一个赛道上竞争,目前看还没有谁占绝对优势;第二层是长时储能,中压 UPS 要替代柴油机就必须搭配几个小时的电池,储能电芯和系统集成商(包括 Tesla Megapack、Fluence 以及宁德时代这类电芯厂)会直接受益;第三层是功率半导体,中压变换和 800VDC 都离不开 SiC 器件,Wolfspeed、onsemi、Infineon 这条线会跟着走。所以我会把这条新闻挂在能源板块和 AI 板块上:能源板块是因为储能和中压电力电子的需求被拉起来了;AI 板块是因为这类设备直接决定数据中心能多快并网、能塞多少算力,属于 AI 基础设施里解决具体瓶颈的那一层,而不是蹭概念。不过中压 UPS 这个品类刚起步,参与者短时间内从一两家变成四五家,价格和毛利很可能会被压,值得关注的是后续有没有超大规模云厂商的大额批量订单落到某一家头上,那会比演示项目更说明问题。
