# Dell bets liquid-cooled, software-defined storage can keep AI factories fed
https://siliconangle.com/2026/11/17/poweredge-nodes-turn-software-defined-storage-ai-dellatsc26/

先说明利益相关:这是 theCUBE 在 SC26 上的访谈,文末披露该段由 Dell 赞助,受访者是 Dell 产品与工程高级副总裁 George Papadopoulos,下面的"业界首个"等说法都是 Dell 自述,未经独立验证。

这篇文章背后的命题是:AI 工厂的密度已经高到连存储都要液冷了。如果"100% 液冷数据中心"成为新建 AI 设施的默认设计,那么液冷就不再只是 GPU 机柜的配套,而是会延伸到网络、存储乃至整栋楼的每一个发热单元,散热这一层的市场边界会被重新划定。

文章指出,随着负载从训练转向推理和 agent,存储而不只是计算开始决定 AI 工厂把数据变成 token 的速度。Papadopoulos 说,agent 类负载更多是小 I/O 操作而不是流式读写,客户所需的存储类型会很快变化,所以客户希望今天买的存储以后能改作他用。Dell 的答案是 Dell Exascale Storage,一套以授权软件形式运行在 PowerEdge 服务器上的软件定义存储,可以在同一节点上部署文件、块、对象或并行文件"人格",并随需求切换;软硬件分离也让 Dell 能更快把新一代 PowerEdge 推向市场。在散热上,Papadopoulos 称客户已经在规划 100% 液冷的数据中心,这个要求现在延伸到存储,包括给硬盘液冷;Dell 在 SC26 上发布了一款 2U、32 盘位、100% 液冷的节点,称其为面向机柜级 AI 的首款直接液冷存储。文章还提到,这种灵活性对 neocloud 运营商尤其重要,因为它们需要每一笔采购都有"退出路径",不被锁定在某种存储类型上。

个人看法:这篇和今天早些时候的 [Dell Agentic Data Gateway](2026-11-17-dell-puts-a-single-gateway-between-enterprise-ai-agents-and-the-data-they-crave.md) 是同一场 SC26 赞助访谈的两段,那篇讲数据层治理,这篇讲存储硬件,合起来是 Dell 想把"AI 工厂"从卖 GPU 服务器扩展到卖整个机柜的完整故事。和 [英伟达在 SC26 讲"agent 是新科学家"](2026-11-17-nvidia-at-sc26-agents-are-the-new-scientists-and-they-need-a-lab.md) 一起看,推理和 agent 负载对存储的要求从"大块顺序读写"变成"大量小 I/O",这一点是有技术依据的,不完全是营销。

先找瓶颈。这篇其实点出了两个瓶颈:第一是功率密度带来的散热瓶颈,第一篇 SpaceX 太空数据中心和 IEEE 能源那篇都提到过,除了 GPU 本身,冷却是数据中心最大的能耗来源,现在连存储都要液冷,说明风冷在高密度机柜里已经没有余量;第二是负载快速变化带来的采购风险,neocloud 不敢把钱押在一种固定存储架构上。受益的层次会是:第一层是液冷基础设施,Vertiv、Schneider 这类 CDU 和冷板供应商,以及冷却液供应商,液冷从 GPU 扩展到存储意味着单个机柜里需要接液冷的部件更多;第二层是存储介质,如果 agent 负载以小 I/O 为主,高性能 NVMe SSD 比机械硬盘更受益,Micron、SK hynix、Samsung 的企业级 SSD 业务会被带动;第三层才是 Dell 这样的整机和存储软件厂商,软件定义存储能提高它的粘性,但这一层竞争也最激烈,VAST Data、Pure Storage、WEKA 都在做类似的事情。这些主要挂在 AI板块,同时液冷带来的是更高效的能耗利用,间接挂在能源板块。这篇只是厂商访谈,值得跟踪的是这款液冷存储节点的实际出货和客户案例,而不是发布本身。
