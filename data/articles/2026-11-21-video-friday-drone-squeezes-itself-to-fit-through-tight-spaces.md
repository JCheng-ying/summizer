# Video Friday: Drone Squeezes Itself to Fit Through Tight Spaces
https://spectrum.ieee.org/video-friday-morphing-robots-quadrotor

这期 Video Friday 是 IEEE Spectrum 每周的机器人视频合集,大部分是研究演示和宣传片段,这里只挑几条和产业相关的写。

文章介绍的第一个项目是一种可变形四旋翼无人机:研究者同时优化机身几何结构和两侧机臂接触时的弯折方式,原型机接触时可以从 31.3 厘米收窄到 14.1 厘米,穿过 15 厘米的开口。第二条比较有实际意义的是 PHD-Hand,一只用刚性连杆而不是肌腱驱动的灵巧手,作者的出发点是大多数平价灵巧手都用肌腱,需要反复重新张紧和更换;这只手每根手指有三个主动自由度,能抓取和操作多种物体,整只手 3D 打印,零件成本不到 650 美元。第三条是 Walden Robotics 联合创始人兼 CTO Ben Burchfiel 在 CMU 机器人研究所的讲座,文章介绍 Walden 今年 1 月成立,两个月后就把第一台机器人部署进生产制造线,至今仍在运行,机器人队伍一直在"边工作边学习",公司的核心信念是最好的物理 AI 来自基于真实工作的持续部署-学习循环。此外还有可以互相抓握组成链条、环和分支结构的软体蛇形机器人 TeCoBots,以及 Astribot 的多机器人上下文共享框架 CoMind。

个人看法:这期里我最关注两条。PHD-Hand 针对的是灵巧手的一个真实工程瓶颈——肌腱驱动的维护成本,如果刚性连杆能以低于 650 美元的成本做到接近人手的灵巧度,对研究和小批量部署都是降本路径,和之前 [This disembodied hand is all the robot you need](2026-10-08-this-disembodied-hand-is-all-the-robot-you-need.md) 讨论的"灵巧手才是核心"是一个方向。Walden 则代表了另一种数据路线:不靠仿真或遥操作攒数据,而是直接部署到工厂,在真实生产中持续学习,和 [Walden Robotics partners with Toyota on practical humanoids](2026-08-03-walden-robotics-partners-with-toyota-on-practical-humanoids.md) 联系起来看,它从成立到部署的速度很快。对机器人板块来说,这两条都是方向性的小信号:瓶颈在灵巧操作的成本和真实场景数据,受益的会是低成本执行器和传感器供应链,以及能拿到真实工厂部署场景的整机公司。都是早期进展,值得关注的是 Walden 有没有公开它的部署规模或客户数据。
