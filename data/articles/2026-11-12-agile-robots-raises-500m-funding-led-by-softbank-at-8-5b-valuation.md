# Agile Robots raises $500M funding led by SoftBank at $8.5B valuation
https://siliconangle.com/2026/11/12/agile-robots-raises-500m-funding-led-by-softbank-at-8-5b-valuation/

这轮融资说明的是 Physical AI 资本流向的一个变化:钱开始更多地流向已经有大量工业部署、有硬件产线的公司,而不只是押注纯人形机器人概念。

文章指出,德国机器人公司 Agile Robots 完成 5 亿美元 F 轮融资,估值 85 亿美元,由软银领投,Nvidia、日立和 T Capital 参与,累计融资达到 20 亿美元。公司 2018 年从德国航空航天中心(DLR)分拆出来,产品覆盖人形和移动机器人、机械臂、灵巧手以及控制它们的 AI 模型。核心技术是力敏感操作:旗舰机械臂 Diana 7 的七个轴都配有力矩传感器,可以感知并调整抓取、提起和操作物体所需的力度。人形机器人 Agile One 于 2025 年 11 月发布,定位工业优先,其中 Agile One SN 配备双 Wuji 五指灵巧手,并预配置了 Nvidia Isaac GR00T 模型。文章提到,公司已部署约 2 万套工业机器人方案,覆盖汽车、消费电子、物流等行业,旗下有 Franka Robotics、Idealworks、BÄR Automation 和 Krause Automation 等子公司;今年初在慕尼黑附近开设的工厂每年可生产最多 1 万台足式和轮式人形机器人。融资将用于进入美国、扩大工程团队和产能。

把这家公司拆开看,它其实有三层能力:第一是硬件,机械臂、灵巧手和带力矩传感器的关节;第二是集成能力,通过收购的几家自动化集成商把机器人真正装进产线;第三是 AI 模型和软件,其中一部分直接建立在 Nvidia 的 GR00T 上。

个人看法:这和 style_reference 第七篇 RoboReward 的结论正好呼应——机器人操作真正的瓶颈是力、触觉和力矩这些视觉无法感知的信息,而 Agile Robots 的核心卖点恰恰是全关节力矩传感。之前写过 [Path Robotics 融资 3 亿美元](2026-11-10-industrial-automation-startup-path-robotics-raises-300m-in-funding.md)、[Agility Robotics 登陆纳斯达克](2026-11-05-humanoid-robot-maker-agility-robotics-debuts-on-the-nasdaq-after-spac-merger.md),工业场景已经成为资本最认可的落地方向。对机器人板块来说,受益的层次会是:第一层是力矩传感器、谐波减速器和灵巧手这些核心零部件,因为不管谁的人形机器人胜出都需要它们;第二层是有真实部署数据和集成能力的整机厂商,Agile 的 2 万套部署本身就是训练数据来源;第三层是机器人基础模型和仿真平台,Nvidia 同时作为投资人和 GR00T 提供者,在这一层的卡位越来越深,这也挂到 AI板块。另外,软银在同一周因为燃气轮机押注亏损、又领投机器人,说明它在调整 AI 相关的押注方向。

现在仍是一级市场估值,工厂年产 1 万台是产能而非销量。值得跟踪的是 Agile One 在汽车或电子工厂里的实际付费部署数量。
