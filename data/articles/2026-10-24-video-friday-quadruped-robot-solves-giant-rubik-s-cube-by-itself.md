# Video Friday: Quadruped Robot Solves Giant Rubik's Cube by Itself
https://spectrum.ieee.org/video-friday-rubiks-cube-robot

这期 Video Friday 照例以短视频花絮为主,标题里 ETH Zurich 机器人系统实验室的四足机器人只用脚就自主解开一个巨型魔方,算是趣味担当。真正有信息量的是三条:Hybrid Robotics 的 SuperMimic 把动作跟踪训练的算力成本压低了三个数量级,Generative Bionics 宣布与 AMD 合作建设欧洲最大的"Physical AI Data Factory",以及 RAI Institute 的肌腱驱动机械手。

先说 SuperMimic。文章引用的数据是:在单块 GPU 上训练三小时,SuperMimic 的回报就超过了一个用 128 块 GPU 训练七天的最先进动作跟踪基线,GPU 小时数减少了 1000 倍以上;在 129514 条基准动作里只失败 25 条,基线失败 179 条;在两块 GPU 上训练 9.8 小时后实现零失败。需要注意这是项目方自己给出的数字,视频简介里没有更多评测细节。

第二条是 Generative Bionics。文章只有一句话:10 月 21 日在 CES Unveiled Milan 上,Generative Bionics 宣布计划建设欧洲最大的 Physical AI Data Factory,AMD 作为其 AI 基础设施合作伙伴。规模、投资额和时间表文中都没有给出。

第三条是 RAI Institute(Robotics and AI Institute)发表在《Science Robotics》上的 AthenaZero:两只三指机械手由肌腱驱动,每根手指的电机放在躯干里,通过柔性线缆传力,这样手本身很轻;手指可以交错握持,既能拿鸡蛋也能拿锤子;闭合时间约 80 毫秒,力量也大,再加上高精度的气压式压力传感器,也能做到轻柔抓握。

其余几条一笔带过:Reflex 是一个三阶段框架,让人形机器人学会接住下落的杯子、躲开推车、接住抛来的箱子这类约一秒内的视觉反应式全身控制;KAIST 的 KAIST Humanoid v0.9 用机载视觉推动最重 35 公斤、举起最重 20 公斤的物体,摆出"KAIST"字样;ETH Zurich 软体机器人实验室把实验室培养的骨骼肌和 3D 打印软支架放在同一个仿真框架里协同优化,厘米级生物执行器的运动范围比同等组织体积的以往系统高出最多 11 倍;Grain Weevil 把两台粮仓机器人连成一台,由一名操作员控制,做到最多三台机器人的工作量;NASA 发布了月球车和机器人漫游车在月球基地早期阶段的作用;Persona AI 的 Michael Perry 在 Humanoids Summit Seoul 2026 上讲为什么要选择双足人形形态;另外还有 Unitree、Parallel Systems 和单电机无人机的视频。

个人看法:ETH 那条生物混合执行器正好可以和同一天的 [MIT scientists build a tiny robot that swims using living muscle cells](2026-10-24-mit-scientists-build-a-tiny-robot-that-swims-using-living-muscle-cells.md) 放在一起看:MIT 是把肌肉做薄,让每个细胞出力效率更高;ETH 是把肌肉和支架一起在仿真里优化,而不是先长肌肉再搭骨架。两条路线都在攻同一个瓶颈——活体肌肉出力太小——但都还是学术阶段。

这期里我更在意的是 SuperMimic 和 Generative Bionics 这两条放在一起形成的张力。目前来看,降低具身智能训练成本大概有三条路:1. 算法效率,也就是 SuperMimic 这种同样效果少用 1000 倍算力的方法;2. 数据效率,比如上周 [Video Friday: When Two Robots Become One](2026-10-19-video-friday-when-two-robots-become-one.md) 里 DeepMind 用视频直接生成仿真;3. 堆基础设施,也就是 Generative Bionics 这种建"Physical AI Data Factory"的做法。表面上第一条会削弱第三条的必要性,但用"先找瓶颈"的方法看,单个动作跟踪任务的算力成本降下来,并不等于整个行业的算力需求下降——训练变便宜之后,研究者会去跑更多动作、更多机器人形态、更大规模的仿真,这和过去大模型训练效率提升之后总算力需求反而继续增长是同一个逻辑。所以 AI 板块里算力基础设施这一层仍然是确定性更高的受益方,而 AMD 这次作为 Physical AI 数据工厂的基础设施合作伙伴出现,说明这一层的竞争不只是 Nvidia 一家,只是目前只有一句宣布,没有规模和订单金额,只能先记下来。

机器人板块这边,真正卡住人形机器人落地的瓶颈之一是灵巧手——既要快、要有力,又要能轻柔抓握易碎物体,还要足够轻不拖累手臂。AthenaZero 把电机移到躯干、用肌腱传力,是解决"手太重"这个具体问题的一种设计,而气压式压力传感器则对应了之前 [Robots Are Learning to Feel](2026-09-10-robots-are-learning-to-feel.md) 里讨论的触觉瓶颈。受益的层次会是:第一层是灵巧手和执行器本身(电机、线缆传动、减速器);第二层是触觉/压力传感器供应商;第三层才是整机。但 RAI Institute 是研究机构,不是上市公司,这条更多是技术路线上的信号。现在还早,值得跟踪的是 Generative Bionics 的数据工厂会不会公布具体的算力规模和时间表,以及 SuperMimic 这类方法能不能从动作跟踪推广到更复杂的操作任务。
