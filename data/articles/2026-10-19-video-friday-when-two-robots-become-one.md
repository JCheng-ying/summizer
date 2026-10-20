# Video Friday: When Two Robots Become One
https://spectrum.ieee.org/video-friday-reconfigurable-robots

这期 Video Friday(10 月 16 日)照例以一句话花絮为主,标题里的"两个机器人合体"(JSK Lab)和 Pollen 的 Microduck 合唱只是趣味内容。真正有信息量的是两条:Google DeepMind 用 Gemini 4 Argon 从人类视频直接生成仿真并迁移到真实人形机器人,以及 NASA Perseverance 打破地外行驶距离纪录。

先说 DeepMind 这条。文章指出,在一次内部测试中,DeepMind 机器人研究人员让 Gemini 4 Argon 观看一段人类玩沙包投掷游戏(cornhole)的视频,模型凭借视频理解和推理能力,在 MuJoCo 里搭建了一个虚拟仿真,计算出需要的物理参数和全身控制,让 Apptronik 的 Apollo 2 人形机器人在真实世界里连续投中七次。DeepMind 把这条流程叫做 Video-to-Sim-to-Real,并声称它能把几周的手工建模压缩到几个小时,"把普通视频变成物理 AI 的无限训练场"。需要注意这是公司自己发布的内部测试视频,只有一个任务、一个结果,没有更多评测细节。

第二条是 Perseverance。文章提到,截至 2026 年 10 月 11 日,Perseverance 已经行驶了 45.22 公里,超过 Opportunity 保持的 45.16 公里,成为在其他星球表面行驶距离最长的载具;它用五年半走完了 Opportunity 花了将近 15 年走完的距离。同一期还有欧洲 Rosalind Franklin 火星车在地球上排练"下着陆器"这一步,模拟低重力、20 度斜坡和坡道下的障碍物。

其余几条一笔带过:Boston Dynamics 展示了 Atlas 的车间,强调自己加工零件、在同一个屋檐下做装配和维修,以提高"把复杂设计变成能走的硬件"的制造速度;DEEP Robotics 的 Lynx M20S 四足机器人跟着科研团队进入中国哀牢山做生物多样性考察,探路、背设备、拍野生动物;Disney Research 发布了 Kamino,一个 GPU 加速的物理求解器,能不做简化近似地仿真带运动学闭环的复杂机械系统(并联机构、连杆、关节耦合的多肢机器人);ETH Zurich 的 WildOS 做未建图户外环境里的开放词汇目标搜索;还有 Sharpa 的恢复动作视频,编辑的评价是动作很厉害但比人慢太多,价值主要在新奇感。

个人看法:DeepMind 这条和今天另一篇 [The Robot Report 关于 Atlas 的评论文章](2026-10-19-the-rise-of-the-machines-is-canceled-why-humanoids-with-ai-are-helpers-not-enemies.md)正好对上——那篇里 Atlas 的训练还要靠人戴 VR 遥操作、穿动捕服一条条录数据,再在仿真里放大;而 Video-to-Sim-to-Real 想做的,是把"数据采集"这个最重人力的环节直接替换成"看普通视频"。如果这条路线能在更多任务上复现,它攻的就是机器人基础模型目前最确定的瓶颈:真实世界的高质量训练数据太贵。所以受益层次可以这样拆:**AI板块**里,第一层是能做视频理解加物理推理的前沿多模态模型本身,第二层是跑大规模仿真的 GPU 和仿真软件(MuJoCo、以及这期 Disney Kamino 这类 GPU 物理求解器,都在把仿真本身变成算力需求);**机器人板块**里受益的是像 Apptronik 这样和 DeepMind 深度绑定的整机厂,它们能最早拿到这套数据管线。但一个沙包投掷任务离工厂里的接触式操作还差得很远——投掷主要是抛物线和全身协调,而工厂任务的难点在接触力和摩擦,这一点视频里看不出来。现在还只能观望,值得关注的是 DeepMind 后续有没有在操作类任务、而不是投掷类任务上公布 Video-to-Sim-to-Real 的成功率数据。
