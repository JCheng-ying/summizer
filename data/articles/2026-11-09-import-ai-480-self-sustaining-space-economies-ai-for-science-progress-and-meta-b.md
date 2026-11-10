# Import AI 480: Self-sustaining space economies; AI for science progress, and Meta builds perfect hands for a superintelligence
https://importai.substack.com/p/import-ai-480-self-sustaining-space

这一期 Import AI 的几条内容放在一起看，其实指向同一个命题：AI 的下一阶段扩张，越来越受制于物理世界——要么是机器人需要的触觉数据，要么是训练需要的电力和集中算力，要么是更远期把工业搬到地球之外。

第一条是 AI for Science。文章指出，AI 科研创业公司 Physical Superintelligence（PSI）用内部研究系统、运行一个未公开的 Anthropic 模型，证明了 Scott Aaronson 和 Andris Ambainis 在 2008 年提出的猜想，这个猜想关于量子计算机何时能比经典计算机指数级更快。系统在运行第三天就得到完整证明，并被 Lean 证明助手逐步验证通过，之后又两次改进了结果。作者 Jack Clark 把这称为"奇点的早期"：机器扩展人类知识边界的速度，开始超过人类理解这些结果的速度。这件事我们在 [AI-assisted proof settles longstanding question about quantum speedups](2026-11-08-ai-assisted-proof-settles-longstanding-question-about-quantum-speedups.md) 那篇已经写过，这里不重复。

第二条是 Meta Reality Labs Research 发布的 Tactus 手套，这是一款为采集自然操作数据而设计的纺织触觉 + 位姿传感手套。文章介绍了三个设计重点：第一是 3D 针织的贴合形态，指尖叠层只有 1.5 毫米，尽量不干扰自然的抓握；第二是根据接触研究在关键部位布置电容式触觉传感器，并提供校准过的指尖力测量；第三是融合 IMU 的姿态追踪，在手和物体互相遮挡时——也就是操作数据最有价值的时候——仍能保持精度。Clark 的视角比较科幻：这正是一个失控 AI 会花钱雇人类戴上、为它执行任务并收集数据的硬件。

第三条是 NASA 肯尼迪航天中心 2016 年的一篇论文，讨论在月球自举一个能自我复制的工业体系需要多少质量。论文的基准情形是向月球发射 41 吨，低速情形只要 12 吨，但工业规模小两个数量级、收益延后八年。Clark 按 Starship 100 吨近地轨道运力加多次在轨加注估算，把 12 到 41 吨送上月球的标价成本大约在 15 亿到 42 亿美元之间。论文设想六代制造：从气体、水、粗合金、陶瓷、太阳能电池开始，逐步到塑料橡胶、化学品、先进材料，最后在月球本地制造包括电子器件在内的所有材料；需要送去的设备包括挖掘机、处理挥发物和固体的化工厂、金属陶瓷精炼、增材制造、可能含小型核反应堆的电站，以及负责组装维护的"robonauts"。有意思的是，论文当年预测 AI 到 2030 年才达到"老鼠级"，而 Clark 认为今天已经接近人类级。

第四条是由前 OpenAI 和 Google 人员创立的 Core Automation 发布的分布式训练实验：一个约 320 亿总参数、32 倍稀疏的 MoE 模型，在相距约 9000 英里的两个集群上训练，一边是美国的 160 块 B300，一边是亚洲的 160 块 GB300，两边加速器、并行方式和 batch size 都不同，每 50 步分片错峰同步一次。作者引用 Core Automation 的原话：部署算力的最大瓶颈不是芯片本身，而是电力、电网设备和土地；真正卡住多数机构的，是能不能把一个个"算力孤岛"拼成一次前沿训练。他们甚至提出未来可以先在几颗卫星上预训练一个小模型，与地面基线对比。

个人看法：这期内容和我之前写的 SpaceX 太空数据中心那篇逻辑是连起来的。Core Automation 那句"瓶颈是电力、电网设备和土地"几乎就是我们这段时间反复看到的主线（比如 [Europe’s AI ambitions are hitting a power bottleneck](2026-11-01-europe-s-ai-ambitions-are-hitting-a-power-bottleneck.md)）。如果单个超大园区越来越难拿到电和地，那么解决这个瓶颈的路径大概有三种：1. 自建电源（燃气轮机、燃料电池）；2. 把训练拆散到多个中小园区，靠分布式训练算法和长距离光互联拼起来；3. 更远期把算力搬上轨道。第二条路线如果成熟，受益的不再只是超大规模园区开发商，而是第一层的长距离光互联和数据中心互联厂商，比如 Ciena、Marvell、Broadcom 这类，利好 AI 板块里的网络层；同时它也降低了"必须拥有一个吉瓦级园区才能训前沿模型"的门槛。

Tactus 手套则补上了机器人数据链条里最缺的一块：触觉和力数据。之前 RoboReward 那篇提到视觉无法区分抓纸杯和抓树莓所需的力度差别，这种手套正是在解决这个瓶颈，利好机器人板块里做灵巧手和触觉传感的公司。月球工业化那部分则是太空经济板块的远期叙事，它的真正前提是 Starship 级别的低成本运力和高度自主的机器人，两者都还在验证期，只能观望。值得关注的是 Core Automation 会不会公布更大规模的跨洲训练结果，因为这会直接改变市场对"超大单体数据中心"的估值逻辑。
