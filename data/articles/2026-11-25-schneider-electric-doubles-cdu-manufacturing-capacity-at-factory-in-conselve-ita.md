# Schneider Electric doubles CDU manufacturing capacity at factory in Conselve, Italy
https://www.datacenterdynamics.com/en/news/schneider-electric-liquid-cooling-conselve-italy-cdu/

这条新闻看起来只是一次工厂扩产,但它反映的是 AI 数据中心供应链里一个正在变化的事实:液冷已经从"高端选配"变成了需要按产能规划的基础设施,而且供应链开始本地化。如果 Schneider 这样的头部厂商要专门为欧洲翻倍 CDU 产能,说明欧洲高密度 AI 机柜的订单可见度已经足够支撑重资产投入,液冷设备本身正在成为数据中心建设节奏里的一个潜在瓶颈。

文章指出,Schneider Electric 将把意大利 Conselve 工厂的冷却液分配单元(CDU)产能翻倍,从 2027 年 1 月起生效;同时在年底前把"Big Chiller"大型冷水机组的制造能力提升 50%。工厂还在新建一个先进冷却测试实验室,目标是 2027 年 12 月投入使用,建成后测试能力是现在的三倍,可以验证最高 4MW 的冷水机组、最高 5MW 的 Motivair by Schneider Electric CDU,以及最高 800kW 的 CRAH(机房空气处理机)和风墙系统。Schneider 欧洲安全电源与数据中心业务高级副总裁 Damien Dhellemmes 的说法是,AI 正在根本性改变客户设计和运营数据中心的方式,带来了对先进液冷技术前所未有的需求,扩产是为了把关键技术和能力放到离欧洲客户更近的地方。文章还提到,这座工厂是 Schneider 在 2010 年收购 Uniflair 时获得的,Uniflair 在 1980 年代建了它。

同一周,Schneider 还发布了一套基于电力电子的配电产品组合,用于保护、变换和控制,面向越来越多直流化的电气系统。文章指出,这套产品用半导体开关、传感、数字控制和通信,在交直流混合架构里保护、转换和管理电力;按 Schneider 的说法,和传统机械开关相比,电力电子器件可以在微秒级完成断流、切换或变换,同时提供系统级的状态参数和诊断。

这里需要把两件事放在一起看。第一,CDU 是液冷系统里的"心脏",负责把设施侧冷水和机柜侧冷却液隔开、做换热和流量压力控制,单台从几百 kW 到 5MW 的跨度,说明液冷正在从机柜级走向行级甚至整个数据厅级的集中式方案,这和 [CoolIT 与 Ecolab 推出 3MW CDU](2026-11-18-coolit-ecolab-launch-3mw-cdu.md) 是同一个趋势。第二,冷水机组扩产 50% 和 800kW 风墙的测试能力说明,即使是液冷数据中心也不是完全不要风冷,芯片直冷带走大部分热量,剩余部分仍要靠空气侧和冷水机组,散热系统是"液冷 + 风冷 + 冷源"三层叠加。至于电力电子产品,本质上是在回应 800V 直流供电这类新架构——机柜功率上到几百 kW 以后,传统交流配电的转换损耗和机械开关的响应速度都成了约束,这一点和 [Vertiv 推出中压 UPS](2026-11-23-vertiv-launches-medium-voltage-ups-for-ai-data-center-sector.md) 指向的是同一个问题。

个人看法:先找瓶颈。今天 AI 数据中心的瓶颈在电力之后,第二个就是散热:GPU 机柜功率密度上升后,风冷物理上已经不够,液冷设备的产能、交付周期和测试验证能力都开始成为约束。Schneider 这次同时扩产能和扩测试能力,后者其实更关键——5MW 级 CDU 这种设备需要在出厂前做满负载验证,测试能力不足本身就会卡交付。这和之前几篇也能串起来:[三星传闻收购 Modine](2026-11-13-samsung-in-talks-to-acquire-data-center-cooling-company-modine-manufacturing-rep.md)、[ABB 以 26.5 亿美元收购风机公司 Ziehl-Abegg](2026-11-24-abb-to-acquire-cooling-fan-company-ziehl-abegg-for-2-65bn.md),再加上这次 Schneider 自建产能,说明大型电气设备公司正在通过收购和扩产两种方式把散热能力收进自己体系里,散热正在从独立细分行业变成电气巨头的标配业务线。

从投资角度看,受益的层次会是:第一层是直接解决散热瓶颈的整套液冷供应商,Schneider(含 Motivair)、Vertiv、以及 CoolIT、Modine 这类,能同时提供 CDU、冷水机组和空气侧设备的公司议价能力最强,这一层挂在 AI 板块的基础设施逻辑上;第二层是电力电子和直流配电,包括 Schneider、ABB、Eaton,以及上游的功率半导体厂商,比如 Infineon、STMicroelectronics、onsemi、Wolfspeed 这类做 SiC/GaN 器件的公司,因为半导体开关替代机械开关,增量需求直接落在功率器件上,这一层同时利好 AI 板块和能源板块,因为直流化和电力电子本身也是电网侧储能、光伏并网的核心技术;第三层是冷却液和换热部件,比如之前写过的 [Chemours 两相液冷液](2026-11-05-chemours-releases-two-fluids-for-two-phase-liquid-cooling.md),随着液冷普及会有稳定的耗材需求。

需要克制的一点是,这是一条公司自己宣布的扩产新闻,没有披露投资金额,也没有说具体对应哪些客户或订单,产能翻倍是从什么基数翻倍也不清楚。值得关注的后续信号是 2027 年 1 月新产能投产后,Schneider 在财报里对液冷业务的增速和交付周期的表述;如果交付周期明显缩短,说明欧洲液冷的供应瓶颈在松动,如果扩产后仍然排单,说明需求比现在看到的还要大。
