# Nokia, Nscale, Skeleton, Telia, and Verda form gigafactory consortium
https://www.datacenterdynamics.com/en/news/nokia-nscale-skeleton-telia-and-verda-form-gigafactory-consortium/

这篇文章反映的是欧洲 AI 基础设施的一个结构性特点:欧洲没有能单独扛起超大规模数据中心的本土 hyperscaler,所以只能靠"拼团"——把网络设备商、电信运营商、GPU 云和电力电子公司绑在一起,去争取欧盟的公共资金。如果这种联合体模式成为主流,欧洲 AI 算力的建设节奏将更多由政策招标而不是市场需求决定。

文章指出,Nokia、Nscale、Skeleton、Telia 和 Verda 宣布成立 AI Gigafactory Northern(AIGF Northern),计划在北欧和波罗的海地区的多个站点建设 AI gigafactory 数据中心,并打算参与欧洲高性能计算联合执行体(EuroHPC Joint Undertaking)发布的 AI Gigafactory 联合体招标。规划站点包括芬兰奥卢、爱沙尼亚 Iru 和拉脱维亚 Valmiera,瑞典站点尚未确定。

联合体的分工基本覆盖了一个 AI 数据中心的几个子系统:第一是网络,Nokia 提供连接和网络基础设施;第二是算力与云平台,Nscale 提供云平台和 AI 基础设施经验,Verda 提供 AI 云能力;第三是电信运营,Telia 及其子公司 Telia Cygate 负责连接、数据传输、基础设施运维和云方案;第四是电力,Skeleton 贡献高功率系统。文章还提到,这些站点会把大规模 AI 计算与主权云、AI 平台服务、连接和脱碳能源结合在一起。Nokia Defense 董事长 Mikko Hautala 在声明里反复强调"可信、可控、可扩展"和"技术主权",这说明这类项目的首要卖点是主权而不是成本。

个人看法:这篇和 Nscale 的几篇旧文能连成一条线——[Nscale 在 2.5 个月内上线两座数据中心和 25,000 块 GPU](2026-11-13-nscale-brings-online-two-data-centers-and-25-000-gpus-in-2-5-months.md) 说明它的执行速度,而 [Microsoft 放弃在得州扩大与 Nscale 的算力合同](2026-11-05-microsoft-declined-option-for-expanded-compute-contract-in-texas-with-nscale.md) 和 [NVIDIA 考虑为 Nscale 西弗吉尼亚项目做担保](2026-11-01-nvidia-weighs-playing-the-cosigner-for-nscale-s-ai-data-center-in-west-virginia.md) 则暴露出它的客户集中度和融资压力。从这个角度看,加入一个瞄准欧盟公共资金的联合体,对 Nscale 来说是在私人大客户之外找一条更稳的需求来源。Telia 和 Nokia 也不是第一次一起出现,之前 [Telia、Nokia 与 QMill 在 5G 网络中演示量子加密](2026-11-17-telia-nokia-and-qmill-demonstrate-quantum-powered-encryption-in-a-5g-network.md) 也是两家搭档。

按"先找瓶颈"的思路,北欧做 AI 数据中心本身有电价低、气候冷、可再生能源比例高的优势,真正卡住的是两件事:一是资金规模,单个 gigafactory 动辄数十亿欧元;二是电网接入和功率波动。这个联合体里最能说明问题的是 Skeleton 的加入——它做的是超级电容和高功率储能系统,而 AI 训练负载的特点恰恰是毫秒级的功率剧烈波动,这对电网和 UPS 都是冲击,需要高功率密度的缓冲器件来平滑。所以受益的层次会是:第一层仍然是 GPU 和网络设备,NVIDIA 以及 Nokia 自身的数据中心网络业务;第二层是电力电子和储能,Skeleton 这类超级电容厂商,以及 Schneider、Vertiv、ABB 等配电与 UPS 厂商;第三层是北欧本地的电力和电网运营商。板块上,这篇利好 AI板块(欧洲主权算力带来新增 GPU 需求)和能源板块(AI 负载的功率波动把高功率储能推到了前台)。

不过现在还只是"打算投标",能否中标、欧盟资金到位节奏如何都不确定,只能观望。值得跟踪的是 EuroHPC 这一轮 AI Gigafactory 招标的结果和每个联合体获得的资金规模。
