# Google planning 1.2GW data center near Châteauroux, France - report
https://www.datacenterdynamics.com/en/news/google-planning-12gw-data-center-near-ch%C3%A2teauroux-france-report/

这篇报道的核心不是"Google 又要建一个数据中心",而是一个更值得注意的现象:在欧洲,超大规模云厂商已经开始提前七八年去排队电网接入,用并网申请来"占位"未来的算力产能。如果电网接入时间成了以年计、甚至接近十年的长周期,那么决定一家云厂商未来算力上限的,就不再是它今天能买多少 GPU,而是它几年前提交了多少并网申请。

文章指出,据法国媒体 Mediapart 报道,Google 子公司 Tricolore Computing 已经为位于 Villedieu-sur-Indre 的一个 1.2GW 数据中心项目提交了并网申请,法国输电运营商 RTE 给出的回应是一个 6,700 万欧元的接入方案,预计需要七到八年才能完成。不过,当地市长 Xavier Elbaz 说,他和 Google 有过沟通,但被告知这个计划已经搁置,因为 Google 正在集中精力推进它在同一区域的另一个项目;而且现有土地所有者此前表示过不愿把地卖给 Google。Google 发言人对 DCD 的回应是:Google 会持续在区域内探索土地和电网机会以预判未来的基础设施需求,对 Ozans 或任何其他场址都尚未做出最终决定,这些都属于探索性的长期规划,而不是同时推进的项目。Mediapart 还报道,过去几个月 Google 接触了 Indre 省的多个市镇寻找场址,意图是给已确认的 Ozans 项目建一个"镜像数据中心"。

背景方面,文章提到 Google 此前将为 Châteauroux 东南的 Ozans 商业园区支付 5,850 万欧元,这块 195 英亩的土地最多可承载 500MW 数据中心,也有报道称可能扩大到 1.1GW,这会是 Google 在法国的第一个自建数据中心,目前仍在法国国家公共辩论委员会(CNDP)主导的公众咨询中。本月早些时候,[Engie 与 Google 签署了能源供应谅解备忘录](2026-11-16-engie-could-supply-power-to-planned-google-data-center-in-ch-teauroux-france.md),Engie 将为项目提供能源并参与可行性讨论和公众咨询。文章最后指出,Google 目前在法国没有任何自建数据中心,依赖的是 Equinix、Digital Realty、Global Switch 等第三方设施,以及通过与法国 IT 公司 Thales 合作提供的主权云。

需要说清楚的是,这条新闻本身是二手报道,而且各方说法并不一致:Mediapart 说的是"镜像数据中心",Google 官方说的是"探索性长期规划、不是同时推进的项目",市长说的是"已搁置",地主还不愿意卖地。所以 1.2GW 这个数字目前只代表一份并网申请上写的容量,不代表一个已经确定的项目。

个人看法:先找瓶颈。这条新闻把欧洲数据中心的瓶颈暴露得非常直接——不是资金(6,700 万欧元的接入费对 Google 不值一提),也不是芯片,而是电网接入的时间:七到八年。这意味着一个今天提交申请的项目,最早也要到 2033 年前后才能通电,而那时的 GPU 已经换了好几代。这和之前几篇是同一条线索:[挪威直接暂停受理新数据中心并网申请](2026-11-09-norway-halts-grid-connection-applications-for-new-data-centers.md)、[Merlin 因电网问题暂停毕尔巴鄂附近两个数据中心](2026-11-19-merlin-pauses-development-on-two-data-centers-near-bilbao-spain-due-to-grid-issu.md)、[Box2Bit 把 150MW 并网容量转让给 Blackstone](2026-11-16-box2bit-transfers-150mw-grid-connection-to-blackstone-and-exits-pila.md),再加上美国 [PJM 想把并网时间压缩到 12 个月](2026-11-20-pjm-plan-could-cut-data-center-and-power-plant-grid-connection-times-to-12-month.md)——欧美两边都在说明,并网权正在变成一种稀缺资产,大厂的理性做法就是"多点提交申请、先占队列、后决定建不建"。Google 用子公司名义在多个市镇找地,正是这种逻辑。不过这也带来一个副作用:大量投机性的并网申请会挤占电网规划资源,类似之前 [英国央行质疑没有电力保障的数据中心贷款](2026-11-05-bank-of-england-queries-speculative-data-center-loans-tied-to-projects-without-t.md) 关注的问题,监管方迟早会对"占位式"申请设门槛。

从投资角度看,受益的层次会是:第一层是能缩短"通电时间"的那一层,也就是输电和变电设备,RTE 的 6,700 万欧元接入工程最终会落到变压器、高压开关、电缆这些设备上,Siemens Energy、Hitachi Energy、Prysmian、Nexans 这类公司是解决并网瓶颈最直接的受益者,利好能源板块;第二层是能源供应和灵活性,Engie 已经在 Ozans 项目里拿到了首选供应商位置,如果镜像项目也推进,1.2GW 的电力需求对法国这样以核电为主的电网是实打实的增量,EDF 的核电和 Engie 的多技术电源组合都会受益,同样是能源板块;第三层才是 AI 板块的算力本身,Google 的 TPU 产能扩张最终需要这些场址,但七八年的时间尺度意味着这条新闻对 AI 板块的短期算力供给没有影响,反而提醒我们,第三方托管商(Equinix、Digital Realty)手里已经通电的存量容量在这段时间里会更值钱。

现在这个项目连"是否存在"都还有争议,只能观望。值得关注的后续信号是 Ozans 项目的 CNDP 公众咨询结论——如果 Ozans 顺利通过、Google 正式扩到 1.1GW,那么 Villedieu-sur-Indre 的镜像项目才有可能真正启动;另外也可以留意 RTE 或法国监管方是否会针对大型数据中心的并网申请出台新的排队或保证金规则。
