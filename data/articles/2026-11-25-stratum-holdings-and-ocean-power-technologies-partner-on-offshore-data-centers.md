# Stratum Holdings and Ocean Power Technologies partner on offshore data centers
https://www.datacenterdynamics.com/en/news/stratum-holdings-and-ocean-power-technologies-partner-on-offshore-data-centers/

这条新闻本身很小,但它属于一个越来越清晰的趋势:当陆地上的电力和散热成为 AI 算力扩张的硬约束,一部分玩家开始把"能自带电、自带冷却介质"的地方当成新的数据中心选址,太空是一个方向,海上是另一个方向。

文章指出,Stratum Holdings 与 Ocean Power Technologies(OPT)签署协议,共同探索由波浪能、风能和太阳能供电的海上数据中心,第一阶段研究把 OPT 的 PowerBuoy 平台和 Stratum 的 GPU 基础设施(包括 Nvidia B300)结合起来。PowerBuoy 本来是为偏远海域和水下应用提供可再生电力和实时数据通信的浮标平台。OPT 将做一份技术和商业可行性评估,涵盖发电和储能需求、热管理、通信能力、平台集成以及可能的部署地点。文章特别强调,第一阶段只做可行性和规划,不包括设备制造、GPU 集成、海上部署或海试,目标行业是国防安全、油气、环境监测和科学勘探。

两家公司本身的背景也值得说清楚。文章提到 Stratum 前身是一家名为 La Rosa Holdings 的房地产公司,本月刚把原有地产业务卖掉转做 AI 云,10 月购入了一批 B300 并以长期租赁方式出租,集群规模不明。Stratum CEO 的说法是"AI 算力需求的增长快于陆地上可用的电力和冷却",这句话本身没错,但出自一家刚刚转型、规模未知的公司,更像是一种定位叙事。文章同时列出了一串同样在做浮动数据中心的公司:Optimal Transit 的自供电"Kraaken"方案、Keppel 在新加坡建设的 25MW 浮动设施(预计 2028 年上线)、利用波浪能的 Panthalassa,以及浮式风电公司 Aikido、Seatrium、Mocean、Atomarine 等。

个人看法:这件事和 [海上算力是沉是浮那篇](2026-11-23-the-coming-wave-is-compute-at-sea-ready-to-sink-or-swim.md) 讨论的是同一个赛道,也和 [意大利初创公司做海上储能给数据中心供电](2026-11-17-italian-startup-targets-data-centers-with-offshore-energy-storage.md) 呼应,而它的逻辑和 SpaceX 轨道数据中心几乎是镜像:都是用"自带能源 + 自然散热"去绕开地面电网和土地审批。但先找瓶颈的话,海上方案的瓶颈和太空方案一样,不在 GPU,而在三件事:第一是功率密度,一个 PowerBuoy 的发电能力是给传感器和通信设备设计的,和一个 B300 机柜动辄上百千瓦的需求差着数量级,这次可行性研究首先要回答的就是发电和储能能不能对得上;第二是可靠性和维护,盐雾、海浪和腐蚀环境下的服务器维护成本,和太空数据中心的"坏了怎么修"是同一个问题;第三是数据回传,远海平台的通信带宽决定了它只适合"数据本来就在海上产生"的场景。这也解释了为什么目标客户是国防、油气和海洋监测,而不是通用云计算——和太空数据中心第一批客户是军方和遥感公司的判断完全一致。

所以投资上真正受益的不会是 Stratum 这类刚转型的小公司,受益的层次会是:第一层是有成熟海工能力的平台和船厂,比如 Keppel、Seatrium,它们无论哪个技术路线胜出都能接到浮动平台的订单;第二层是海洋能源和储能,包括波浪能、浮式风电和配套的储能系统,这挂在能源板块上;第三层是适合边缘场景的紧凑型、耐恶劣环境的计算和通信设备,海上平台本质上是一个高功率的 edge 节点,这挂在 edge AI 板块上;GPU 这一层照例是背景受益,但量太小不改变 Nvidia 的基本面。这只是可行性研究阶段,不包含任何硬件和海试,只能观望。但值得关注的是 Keppel 新加坡那座 25MW 设施 2028 年能否按期上线,那会是这个赛道第一个真正可以验证经济性的样本。
