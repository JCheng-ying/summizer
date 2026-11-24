# Taiwanese AI infrastructure firm Nocera takes $22m stake in Canadian AI data center developer BitRock
https://www.datacenterdynamics.com/en/news/taiwanese-ai-infrastructure-firm-nocera-takes-22m-stake-in-canadian-ai-data-center-developer-bitrock/

这笔交易金额不大,但它把一个越来越普遍的判断说得很直白:在 AI 基础设施里,真正稀缺的资产已经不是 GPU,也不是土地,而是"现在就能用的电"。投资方之所以愿意给一个还没建成第一座数据中心的开发商出钱,核心理由是它不需要排队等电网。

文章指出,台湾 AI 基础设施公司 Nocera 将以 2,200 万美元购入加拿大 AI 数据中心开发商 BitRock 的股份,获得 44% 股权,并拥有委派董事、定期获取财务报告和参与重大决策的权利,双方目前签的是有约束力的意向书(LOI),正式投资协议尚未签署。这笔钱用于 BitRock 第一座数据中心:位于 Alberta、占地 37 英亩的 10MW 设施,由四个 2.5MW 预制计算模块组成,长期规划扩展到 200MW,按客户需求每次增加 10MW;后续阶段"按各自情况单独评估和融资"。BitRock 的模式是现场天然气发电自供电,它称已经拥有发电设备,并已获得在 Alberta 发电和供电的许可;园区目标 PUE 为 1.225,N+1 冗余,采用托管(colocation)模式,由 BitRock 提供已通电的机房空间和运维。Nocera 的亚洲区负责人 Andrew Teng 的原话是"电力是 AI 基础设施里的稀缺资产"。文章还提到 Nocera 今年的其他动作:6 月与美国 Digital Innovations Group 建立风险投资平台合作,7 月宣布入股英国储能和电力优化公司 INERGX,同月收购台湾 Crucial 内存分销商 QMAX Technology 30% 的控股权益。

把 BitRock 的模式拆开看,它其实是在用三件事绕开电网瓶颈:第一是电源自有,发电设备和发电许可都已经在手,不用等输电升级;第二是模块化,10MW 一个单元、2.5MW 一个预制模块,资本开支跟着客户需求一点点投,而不是一次性押注 200MW;第三是选址,Alberta 本身天然气资源丰富,并且已经立法鼓励数据中心自带电源。这三点合起来,本质上是把"数据中心项目"变成了"带算力负载的小型燃气电厂项目"。

个人看法:这条新闻和昨天写的 [Alberta 拟出台大负荷数据中心新规](2026-11-23-alberta-gov-t-proposes-new-rules-for-large-load-data-centers.md) 正好对上,文章里那句"省政府要求开发者自己解决电"就是指那套自带电源框架;新规把输电成本和发电责任都压给开发商,BitRock 这种一开始就自带燃气发电的小项目反而是规则的受益者。它也和 [Anthropic 签 34 亿美元燃气发电机协议](2026-11-09-anthropic-signs-3-4bn-gas-generator-deal-to-support-1-7gw-of-data-center-power.md) 是同一条线索,只是规模差了两个数量级:从 GW 级的大厂到 10MW 级的小开发商,"表后燃气发电"正在成为默认方案。不过也要记住 [SoftBank 巨亏可能给 AI 天然气野心封顶](2026-11-12-softbank-s-billion-dollar-loss-may-have-put-a-cap-on-ai-s-natural-gas-ambitions.md) 那篇提出的风险:燃气自供电的项目对资本的依赖很强,资本情绪一转向,第二、第三期就未必能融到钱,这次交易里"后续阶段单独评估融资"其实已经埋下了这个不确定性。

按"先找瓶颈,再找解决瓶颈的那一层",这里的瓶颈非常明确,就是并网等待时间。受益的层次会是:第一层是现场发电设备,也就是燃气发电机组和往复式内燃机、小型燃气轮机供应商,比如 Caterpillar、Wärtsilä、Cummins 这一类,因为每一个 10MW 模块都需要对应的发电容量和冗余;第二层是预制模块化数据中心和配电设备,Vertiv、Schneider、Eaton 这类能把电源、配电和冷却打包成预制模块的公司,正好匹配"10MW 一段"的扩张节奏;第三层是储能和电力优化,燃气机组响应 AI 负载的快速波动并不灵活,需要电池做缓冲,这也解释了 Nocera 为什么同时去投 INERGX;第四层才是上面的 GPU 和托管客户。所以我会把它挂在能源板块(偏正面,现场发电和模块化供电的需求更具体了),以及 AI 板块(偏中性,10MW 对整体算力供给影响很小,但说明中小资本也在涌入"自带电"的算力项目)。

需要克制的地方是,这只是一份 LOI,BitRock 还没有建成任何设施,Nocera 本身也在同时做内存分销、储能和风险投资,更像一家在 AI 主题下多处布局的控股平台。值得跟踪的是正式协议能否按时签署,以及第一个 10MW 模块是否真的能拿到签约租户,这比 200MW 的远期规划更能说明问题。
