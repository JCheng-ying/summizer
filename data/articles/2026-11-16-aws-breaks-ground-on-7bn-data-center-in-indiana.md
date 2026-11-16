# AWS breaks ground on $7bn data center in Indiana
https://www.datacenterdynamics.com/en/news/aws-breaks-ground-on-7bn-data-center-in-indiana/

这条新闻本身只是一次开工仪式,但把它和同一篇里 AWS 在北弗吉尼亚买地的消息放在一起看,背后的命题更清楚:超大规模云厂商的选址逻辑已经从"哪里有光纤和客户"转向"哪里有电、哪里的社区愿意让我建"。Amazon 一边在印第安纳这种电网和地方政府都欢迎的地区成片扩张,一边在传统核心市场弗吉尼亚趁禁令投票之前抢地,两件事其实是同一个约束的两种应对。

文章指出,AWS 在印第安纳州西北部 Jasper County 的 Wheatfield 正式开工建设代号 Project Rise 的数据中心,投资 70 亿美元,由 Ryan Construction 承建,工期预计需要数年。AWS 将预先缴纳 9800 万美元税款,并在未来 30 年内再贡献 7 亿美元。园区规划最多九栋建筑,占地 304 英亩,这块地是当地电力公司 NIPSCO(Northern Indiana Public Service Company)卖给 AWS 的,距离 NIPSCO 的 Schahfer 发电站仅半英里。园区主要采用风冷,一年中只有约 2% 的最热时段使用水冷。AWS 在 New Carlisle、Hobart 和 Wheatfield 三地的数据中心合计投资 330 亿美元;这些项目属于 AWS 在 2025 年 11 月追加的 150 亿美元印第安纳投资承诺,目标是为该州增加 2.4GW 容量。文章还提到,本月早些时候有报道称 AWS 正在考察印第安纳州 Posey 县的另一个项目。

值得注意的是这个项目的三个细节,恰好对应了数据中心落地的三个约束。第一是电力,土地直接从公用事业公司手里买、紧挨着现有发电站,意味着并网距离最短,这比任何电网扩建方案都快;NIPSCO 的发言人在开工仪式上强调"对电力系统的投资"会提升可靠性,说明电力公司本身是这个项目的积极参与方,而不是被动接入方。第二是水,主要风冷、只在约 2% 的时间用水,这是直接回应近来各地对数据中心耗水的反对。第三是社区关系,AWS 的经济发展负责人用"成为 Jasper County 大家庭的一员"来描述项目,并把 9800 万美元预付税款放在最前面讲——这和 [DCD Connect Virginia 的会议总结](2026-11-13-dcd-connect-virginia-2026-it-s-all-about-the-power-and-public-perception.md) 里从业者反思"带着数据和支票来"的做法几乎是同一套话术,区别只是这一次在印第安纳是被接受的。

文章后半部分转向弗吉尼亚。AWS 近期在 Loudoun 和 Fairfax 两县买地花费超过 1.7 亿美元:在 Loudoun 以约 9979 万美元买下 Wade Drive 一处 23 英亩的停产混凝土厂,计划建 100 英尺高的数据中心(2023 年 7 月它已以 3444 万美元买下隔壁 25 英亩);在 Fairfax 以 7200 万美元买下 Hazel Park Court 一块 13 英亩的地块,当地规划允许最高 75 英尺的数据中心。文章指出,Loudoun 是 AWS 2006 年第一批数据中心所在地,如今 Amazon 在弗吉尼亚已有数十栋自有或租赁建筑,并在向更多县扩张。但 Loudoun 县监事会将在 11 月 17 日就暂停数据中心一年进行投票,今年早些时候也有弗吉尼亚州参议员提出全州三年暂停。

个人看法:这两段放在一起,我读出来的是"存量许可正在变成稀缺资产"。Loudoun 一年暂停的投票就在明天,AWS 在投票前完成大额买地,而且买的是已经有工业用途、规划允许数据中心的地块——如果禁令通过,这些已有规划许可的土地会比新地块值钱得多。这和之前 [Ottawa, Kansas 的十年禁令](2026-11-11-10-year-data-center-moratorium-approved-in-ottawa-kansas.md)、[过半美国超大规模项目遇到监管阻力](2026-11-05-more-than-half-of-us-hyperscale-data-center-projects-face-regulatory-friction-af.md) 是同一条线,区别是这次能看到头部云厂商是如何提前布局去对冲这个风险的。

先找瓶颈:这篇文章里的瓶颈不是 GPU,也不是资金——[Amazon 第三季度财报](2026-11-01-despite-cloud-boom-amazon-s-stock-falls-on-disappointing-earnings-and-revenue-mi.md) 已经说明它在以 2200 亿美元的年度资本开支扩张,Forrester 认为它面临的是产能约束而不是需求约束。真正的瓶颈是"能通电且被允许的土地"。解决这个瓶颈的那一层,受益的层次会是:第一层是愿意并且有能力配合大负荷接入的受监管电力公司,比如这篇里的 NIPSCO(母公司是 NiSource),逻辑和 [DTE Energy 把五年投资计划提高到 440 亿美元](2026-11-08-dte-energy-ups-five-year-utility-investment-plan-to-44bn-cites-data-center-deman.md) 一样——数据中心负荷直接扩大了它们可获准回报的资产基数,这是能源板块最直接的受益方;第二层是园区内部的电力和散热设备,风冷为主的设计意味着对高效空气侧散热和配电的需求,Vertiv、Eaton、Schneider 这类公司仍然是确定性的供应商;第三层才是 AI 板块的算力层,2.4GW 的印第安纳容量最终要装进 Trainium 和 GPU,对 Amazon 自研芯片链条和 Nvidia 都是长期需求。所以我会把这篇挂在能源板块和 AI 板块。

需要留余地的是,这篇是常规开工新闻,没有披露电力合同条款、具体装机容量或建设时间表,"数年工期"意味着它对当下的算力供给没有影响。值得跟踪的是明天 Loudoun 的投票结果:如果一年暂停通过,北弗吉尼亚的存量地块和已在建项目会进一步溢价,超大规模云厂商向印第安纳、俄亥俄这类"愿意说 yes"的州迁移的速度也会加快。
