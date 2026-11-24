# NewYork GreenCloud submits application to build 14.4MW biomass powered data center in Ione, California
https://www.datacenterdynamics.com/en/news/newyork-greencloud-submits-application-to-build-144mw-biomass-powered-data-center-in-ione-california/

这条新闻规模很小,但它代表了 AI 数据中心找电的一个新方向:不只是去建新电厂,而是去"复活"那些因为经济性不好而闲置的旧电厂,把电厂本身变成算力园区。如果这种模式跑得通,很多搁浅的小型发电资产会因为 AI 负载重新获得价值。

文章指出,NewYork GreenCloud 已经提交申请,要在加州 Ione 一座现有生物质电厂旁建设 14.4MW 的数据中心,建筑面积约 13,000 平方英尺,采用闭式循环冷却,公司在申请中强调"不会使用大量耗水的标准冷却塔"。这座 Buena Vista 生物质电厂由 NewYork GreenCloud 在今年 1 月收购,目前容量 18MW,公司计划扩容到 41MW,以表后(behind-the-meter)方式直接给数据中心供电,多余电力卖给电网。项目还需要经过规划委员会听证才能获批。文章交代了电厂的历史:最初是燃煤电厂,1990 年代中期退役,2009 年改造为生物质电厂,后来因为严重的财务困难而闲置。公司宣称项目把"生物质热解"能源系统和高密度算力结合起来,以降低 AI 负载的碳足迹;热解是在高温低氧条件下把有机废弃物转化为能源和生物炭,支持者认为生物炭可以把碳长期封存。NewYork GreenCloud 总部在纽约州 Plattsburgh,2024 年成立,Ione 是它的第一个数据中心项目;去年底它宣布与 Atlas Cloud AI 合作,在 Ione 托管 288 台 HGX B300 系统、共 2,304 块 Nvidia Blackwell GPU,协议期四年,计划 2026 年 2 月前全面部署,初始投资 2.5 亿美元。

这里有一个时间线上的矛盾值得指出:按文章的说法,GPU 集群原计划在 2026 年 2 月前全面部署,但直到现在数据中心本身还停留在提交申请、等待听证的阶段。也就是说,这个项目的算力合作远远跑在了许可和建设前面,这在新成立的 AI 基础设施公司里并不罕见,但意味着原定时间表已经明显落后。

个人看法:这篇和 [Nocera 入股 BitRock](2026-11-24-taiwanese-ai-infrastructure-firm-nocera-takes-22m-stake-in-canadian-ai-data-cent.md) 是同一天的两种"自带电"方案:BitRock 用天然气,GreenCloud 用生物质,共同点都是绕开并网排队,把数据中心直接放在发电机旁边。之前写过 [Ascend Analytics 的表后资产估值赞助文](2026-11-17-sponsored-ascend-analytics-launches-behind-the-meter-asset-valuation-for-data-ce.md),当时那篇是厂商视角在推销表后发电的概念,今天这两条则是具体项目在落地。

按"先找瓶颈"来拆,这个项目真正的瓶颈不是 GPU,而是三件事:第一是发电容量,18MW 的电厂要扩到 41MW 才能在供应 14.4MW 算力负载(加上冷却和损耗)的同时有余电上网,扩容本身就是工程和融资难题;第二是燃料供应,生物质电厂的经济性取决于附近农林废弃物能否稳定、低价供应,这正是这座电厂当年闲置的原因之一,加上数据中心并不能改变燃料成本;第三是许可,加州的规划听证和环保审查周期很长。所以我会把它挂在能源板块,判断偏中性:它说明闲置的小型发电资产因 AI 需求重新被定价,受益的层次是生物质与热解设备、闭式液冷和干冷设备以及能处理表后接入的配电设备商;对 AI 板块则只是边际供给,2,304 块 GPU 对整体算力影响有限。

需要克制的是,"负碳 AI 工厂"是公司自己的宣传口径,生物炭的固碳效果和整个系统的碳收支都没有经过独立核算。值得跟踪的是规划委员会听证的结果,以及 Atlas Cloud AI 那份四年合同是否还在执行,这两件事能说明这种"旧电厂 + AI"的模式到底是可复制的,还是只是一个讲故事的项目。
