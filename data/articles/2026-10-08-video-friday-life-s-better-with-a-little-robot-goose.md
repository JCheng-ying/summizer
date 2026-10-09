# Video Friday: Life’s Better With a Little Robot Goose
https://spectrum.ieee.org/video-friday-goose-household-robots

这期 Video Friday(9 月 25 日那一期)大多是一句话花絮,有信息量的主要是三条:Unitree 灵巧手的定价、Universal Robots 的新一代协作机器人,以及 Skydio 的固定翼无人机。其余一笔带过。

先说 Unitree。文章里只有一句话:"精密仿生灵巧手,起售价 6500 美元"。没有自由度、负载、寿命等任何参数,但价格本身就是信息——[Atlas 新手](2026-10-01-atlas-robot-s-new-hand-may-outperform-humanlike-designs.md)那篇里 Boston Dynamics 的判断是,高度仿人的灵巧手要么脆弱要么昂贵,所以大多停留在研究和演示阶段;Unitree 给仿生灵巧手公开标出一个四位数美元的起售价,是在从"昂贵"这一端往下压。同一期里 Unitree 还有一条:9 月 22 日 WorldSkills Shanghai 2026 开幕式上,19 台 Unitree 人形机器人与 120 名舞者同台,称是全尺寸通用人形机器人规模最大的一次演出,由全 AI 驱动的自主机器人集群完成并全球直播——这是 Unitree 自己的表述,属于展示性质。

再说 Universal Robots。文章指出,作为 UR 系列的演进,g-Series 的设计目标是加快机器人被集成进完整自动化系统的速度:它与摄像头、更高功率的末端执行器(EOAT)和控制系统更直接地连接,省掉外部走线和额外硬件。这条值得记,是因为它指向的瓶颈不是机械臂本体性能,而是集成成本——协作机器人部署里大量时间花在外围接线和系统集成上。

Skydio 发布了 F10,一款外形不对称的固定翼无人机,用一条机械臂完成自主发射和回收。不过编辑特别指出,根据机身 LED 闪烁的频率判断,视频里的回收(很可能还有发射)被明显加速过,所以实际动作速度要打折扣看。

其余花絮:ULOHA 把示范学习带到水下双臂上,自制了主从遥操作硬件并扩展了 LeRobot,把遥操作、示范采集和自主操作连起来,演示包括双臂合抬、臂间传递、开容器,还研究了气泡和动作执行时序对学到的行为的影响;苏黎世大学 Robotics and Perception Group 展示了只靠"告诉无人机你喜不喜欢它的飞法"来训练特技飞行;Boston Dynamics 的机械工程师 Diane Heinle 讲了 Stretch 的耐久测试,以及团队如何在实验室短时间内模拟零件多年的磨损;Astribot 放了长程操作和触觉引导动作的合作演示;LimX Dynamics 演示了怎么把人形机器人装进箱子;IEEE Spectrum 回顾了 30 年前的 Honda P2(髋、膝、踝使用电机和液压,重量超过 300 磅)。编辑对一段 MIT CSAIL 关于"什么是 Physical AI"的视频的评语也值得留意:他个人认为 Physical AI 大体上就是机器人学一直以来的样子,只不过现在什么都得带上"AI"。

个人看法:这期对**机器人板块**有用的是一个关于"瓶颈在哪一层"的侧面印证。灵巧手这一层正在同时发生两件事:一边是价格下探(Unitree 的 6500 美元起售价),一边是学术界开始把商用手当通用平台用(同一天读的[会走路的机械手](2026-10-08-this-disembodied-hand-is-all-the-robot-you-need.md),用的就是现成的商用手)。本体价格往下走,意味着价值会继续向本体以外转移——手上的触觉感知和采数据的方式,也就是[机器人触觉大盘点](2026-09-10-robots-are-learning-to-feel.md)里说的那个瓶颈;而 Universal Robots 的 g-Series 说明在已经成熟的协作臂市场,竞争点已经移到了集成效率上。Boston Dynamics 讲 Stretch 耐久测试那条虽然只是问答视频,但方向和前面一致:真正在卖的产品,拼的是寿命和可维护性。不过 Unitree 这条只有一个价格、没有任何性能和出货数据,不能据此判断产品成熟度,只能当作一个价格锚点记下来,后续看其他灵巧手厂商是否跟进公开定价。这期没有可以加进图谱的公司间合作或投资关系。
