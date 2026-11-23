# Details shared of AWS' 300MW data center in Kozani, Greece
https://www.datacenterdynamics.com/en/news/details-shared-of-aws-300mw-data-center-in-kozani-greece/

这条新闻最值得注意的不是 AWS 又在欧洲建了一个数据中心,而是它建在哪里:一座刚刚关闭的燃煤电厂旧址上。AI 数据中心最稀缺的资源已经不是土地或者建筑,而是现成的高压电网接入能力,而退役的大型火电厂恰好留下了这种能力。如果这个模式被复制,欧洲大量退役煤电厂可能会变成数据中心的"电力入口"。

文章援引希腊媒体 OT.gr 对环境影响评估(EIA)文件的报道指出,这个位于希腊北部科扎尼的园区设计电力容量 300MW(其中 IT 容量 240MW),由四栋相同的建筑、共 20 个数据大厅组成,未来可以扩展到 1GW。项目由 AWS 和希腊公共电力公司(PPC)合作开发,选址是 PPC 旗下的 Agios Dimitrios 燃煤电厂旧址——这座电厂曾是希腊最大的电厂,今年早些时候关闭。园区占地约 45 公顷,四栋建筑总面积 77,360 平方米,每栋高 36 米。

文章提出,这个项目可以利用旧电厂留下的基础设施:园区将通过两条新的地下电缆线路接入 Agios Dimitrios 现有的 400kV 变电站,使用的正是原来 1.55GW 燃煤电厂所需要的输电容量。冷却方面,根据当地气候,60% 到 90% 的冷却负荷使用水冷,其余为风冷,年用水量约 20.3 万立方米。时间表上,PPC 预计很快会拿到接入国家电力系统的条件,300MW 协议预计在 2027 年第一季度敲定,随后订购设备,2027 年夏天开工,2028 年底完工。投资上,PPC 投入 10 亿欧元,AWS 为 IT 基础设施投入类似金额,AWS 拥有扩展到 1GW 的选择权,并在 2027 年 5 月前对这部分容量享有排他权。文章还提到,AWS 在希腊没有云区域,但在 2026 年 7 月于雅典开设了一个 Local Zone,并在 2024 年 11 月签了四份电力购买协议,覆盖 Vermio、Mesokorfi 和 Koukouras 等风电场。

这个项目的结构可以拆成三部分理解:第一是电网接入,旧电厂的 400kV 变电站和输电容量是最难复制的资产,新建一条同等级的输电线路往往要好几年审批;第二是能源供给,AWS 通过风电 PPA 补充绿色电力,但 300MW 到 1GW 的负荷显然不是这几个几十 MW 级别的风电场能覆盖的,大部分仍然要靠电网;第三是冷却,以水冷为主意味着每年 20 万立方米级别的用水,这在地中海地区可能会成为后续审批和社区关注的焦点。

个人看法:这篇和 style_reference 里写过的 AI × Energy 主线完全一致,也和最近 AWS 的一连串动作可以连起来看:[AWS breaks ground on $7bn data center in Indiana](2026-11-16-aws-breaks-ground-on-7bn-data-center-in-indiana.md)、[Amazon to invest $7bn into Indian renewable projects by 2030](2026-11-17-amazon-to-invest-7bn-into-indian-renewable-projects-by-2030.md),以及 [Blackstone acquires majority stake in AWS joint venture](2026-11-16-blackstone-digital-infrastructure-trust-acquires-majority-stake-in-aws-joint-ven.md)。按"先找瓶颈"的方法,这里的瓶颈非常明确就是并网容量,而解决这个瓶颈的不是 AWS,而是手里握着电网接入点的电力公司——PPC 自己掏 10 亿欧元建园区,本质上是把一个即将搁浅的资产(关闭的煤电厂)重新变现成数据中心的电力入口。所以受益的层次会是:第一层是拥有存量电网接入点和发电资产的公用事业公司,这对能源板块是很直接的利好,电力公司从"卖电"延伸到"卖接入";第二层是高压电气设备,包括变电站改造、地下高压电缆、开关设备(Siemens Energy、Schneider、ABB、Prysmian 这类厂商);第三层才是数据中心内部的冷却和电源系统(Vertiv、Schneider);对 AI 板块来说,这是超大规模云厂商资本开支继续往外扩的又一个证据,只是这个项目 2028 年底才完工,对近期需求没有影响。现在还在早期阶段,协议都还没正式签,值得关注的是 2027 年第一季度 300MW 协议能否如期敲定,以及 AWS 会不会在 2027 年 5 月排他期结束前行使 1GW 扩展权——那会是判断它对南欧算力需求有多大信心的一个具体信号。
