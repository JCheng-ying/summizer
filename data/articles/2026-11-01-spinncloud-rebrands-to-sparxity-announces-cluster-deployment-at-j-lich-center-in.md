# SpiNNcloud rebrands to Sparxity, announces cluster deployment at Jülich center in Germany
https://www.datacenterdynamics.com/en/news/spinncloud-rebrands-to-sparxity-announces-cluster-deployment-at-j%C3%BClich-center-in-germany/

这是一条短新闻,文中的性能数字均为公司自己的设计目标,尚未上线验证。

它的意义在于:稀疏计算这条非主流路线开始进入大型超算中心。如果 AI 的能耗瓶颈持续,专用架构才有机会,而这是少数不靠继续堆 GPU 的尝试之一。

文章指出,德国类脑超算公司 SpiNNcloud 更名为 Sparxity,并宣布在于利希超算中心(JSC)部署一套原生稀疏计算机架系统,项目金额为数百万美元量级,用于运行稀疏机器学习模型和大规模 HPC 模拟。系统名为 Jubis,采用事件驱动方式,只在有事件发生时才计算。公司称其设计目标是稀疏求解器快十倍,事件驱动机器学习能耗低 18 倍,优化问题求解时间缩短 20 倍,上线后将开放给更广泛的 HPC 和 AI 应用。

个人看法:这和 [Scientists find a way to slash computer memory energy use by orders of magnitude](2026-09-10-scientists-find-a-way-to-slash-computer-memory-energy-use-by-orders-of-magnitude.md) 一样,是从计算架构上解决能耗的方向。目前来看,解决 AI 能耗瓶颈有三条路:1. 增加供电,也就是这批几篇能源文章讲的;2. 提高 GPU 能效;3. 换架构,比如类脑、光计算和稀疏计算。第三条路的问题在软件生态,模型都是按稠密硬件设计的,这也是这家公司 CEO 自己说的。所以这篇对 AI 板块只算一个小信号,对能源板块几乎不构成实际影响。规模只有数百万美元,和动辄数百亿美元的数据中心不是一个量级。值得跟踪的是 Jubis 上线后的实测能效,以及有没有主流模型真的用稀疏架构跑起来。
