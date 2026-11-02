# Video Friday: Spot Plays to Show Its Whole-Body Manipulation
https://spectrum.ieee.org/video-friday-whole-body-manipulation

这期 Video Friday 照例是短视频合集,标题里 RAI 的全身操作视频(从标题看是用 Spot 搬轮胎)是看点,但真正有信息量的是三条:RAI 视频里暴露的感知失败、Luxonis 的 OAK 4 FFC 视觉计算板,以及 TU Delft 的 MonoRace 无人机击败人类世界冠军。

第一条是 RAI 的全身操作。文章作者认为操作质量很高,但看不出躯干有没有直接参与——人类搬重物或形状别扭的东西时经常会用躯干去顶。更有意思的是视频里引用的一句失败说明:深度图里任何一团"blob"都可能被当成轮胎,不管是路过的人还是地上的杂物,有几次机器人丢下轮胎去追别的东西了。作者对"别的东西"这个模糊说法也表示了怀疑。

第二条是 Luxonis 发布的 OAK 4 FFC,一块 70×53 毫米的视觉计算板,让人形机器人和无人机开发者可以把最多五个摄像头装在机器人需要的任何位置;同步、双目深度和 AI 推理都在板上完成,标定也是从场景中自动完成,不需要棋盘格。

第三条是 TU Delft MAVLab 团队 2025 年 4 月在阿布扎比 A2RL 无人机竞速锦标赛上的 MonoRace 算法:赢得了 AI Grand Challenge,随后击败了三名人类 FPV 世界冠军。无人机只用一个机载摄像头和一个 IMU 做状态估计,机载神经网络直接把估计的状态映射成电机指令,研究发表在《Science Robotics》上。

其余一笔带过:ETH Zurich 机器人系统实验室提出了以接触为中心的人形移动学习框架,把人类动作数据当作先验、再用强化学习适应没见过的地形;Pollen Robotics 的 Reachy Mini 加了轮子,和之前 [Video Friday: Meet Microduck](2026-09-01-video-friday-meet-microduck.md) 里的 Microduck 有了比赛的梗;MangDang 预告 Mini Pupper 4;ROBOTIS 展示了用 DYNAMIXEL 驱动的单指到五指多种机械手及 VR 遥操作;bluZenit 的 monkeyBot 2.0 可以沿工业管道垂直和水平攀爬;Generalist 的清洁演示被作者吐槽"能不能清理一次真正脏的东西";Robotiq 出了新的触觉夹爪;ANYbotics 发布 ANYmal X;LimX Dynamics 展示打网球;DEEP Robotics 的 Lite3 四足和 LYNX M20 轮腿机器人在广西玉龙河景区协同做文旅服务;此外还有 Starship 早期原型、BruBotics 的柔顺手、仿生两栖机器人 SAWbot,以及 IROS 2026 的演讲视频。近期会议是 11 月 9 日至 12 日奥斯汀的 CoRL 2026,和 12 月 6 日至 9 日圣克拉拉的 Humanoids 2026。

个人看法:RAI 那条失败说明其实比成功演示更有价值,它说明全身操作的瓶颈并不在力控和运动本身,而在感知——只靠深度图的"blob"去认目标,一旦场景里有其他物体就会认错。这和 [Pegasus 1.6 brings video understanding to physical AI, says TwelveLabs](2026-10-08-pegasus-1-6-brings-video-understanding-to-physical-ai-says-twelvelabs.md) 里讨论的"机器人需要语义理解而不只是几何感知"是同一个问题。

Luxonis 和 MonoRace 放在一起看,指向的是同一个方向:把感知和决策全部放到机器人本体上完成。目前来看,机器人感知计算大概有三种部署方式:1. 云端或外接工作站推理,延迟高,不适合竞速和高动态操作;2. 一个集中的机载主控芯片处理所有摄像头,比如 Nvidia Jetson 这一类;3. 分布式的端侧视觉模组,每块板子自己完成同步、深度和推理,OAK 4 FFC 就是这一路。MonoRace 用一个摄像头加一个 IMU、端到端神经网络直接输出电机指令就能赢人类世界冠军,说明在高动态场景里,低延迟的端侧推理本身就是性能的来源。所以这期最直接挂上的是 edge AI 板块,受益的层次是:第一层是端侧 AI 视觉芯片和模组(Luxonis 这类模组厂,以及上游的视觉 SoC 供应商),第二层是摄像头和 IMU 传感器,第三层才是整机。机器人板块方面,Robotiq 的触觉夹爪、ROBOTIS 的多指手和 DEEP Robotics 的文旅落地都在补"末端执行器"和"真实场景部署"这两块短板,但都只是视频级别的信息,没有订单或出货数字。

这期整体信息密度不高,值得跟踪的是 11 月的 CoRL 2026 上会不会有更多关于全身操作中感知失败的系统性讨论,以及 OAK 4 FFC 这类分布式视觉模组有没有被人形机器人整机厂实际采用。
