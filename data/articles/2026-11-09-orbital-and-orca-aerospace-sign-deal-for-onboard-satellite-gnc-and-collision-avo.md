# Orbital and Orca Aerospace sign deal for onboard satellite GNC and collision-avoidance AI
https://www.datacenterdynamics.com/en/news/orbital-and-orca-aerospace-sign-deal-for-onboard-satellite-gnc-and-collision-avoidance-ai/

这条新闻背后的命题是：如果未来轨道上真的会有成千上万颗卫星组成的"太空数据中心"，那么它最大的运营成本可能不是发射，也不是芯片，而是地面上那一屋子盯着每颗卫星做决策的人。要让轨道算力规模化，卫星必须自己管自己。

文章指出，轨道数据中心初创公司 Orbital Compute 与做卫星星载运营软件的 Orca Aerospace 达成战略合作，双方称价值最高 2000 万美元，目标是让 Orbital 的星座"自我运营"。Orbital 计划 2028 年发射第一颗卫星，并已向 FCC 申报到 2031 年部署 10 万颗卫星、10GW 算力的星座。Orca 在每颗卫星上运行一个小型星载 AI 模型，连接卫星的制导、导航与控制（GNC）软件和地面控制，每颗卫星自主规划和执行机动、任务分配和故障响应，只有软件认为必要时才叫人。具体架构是三层：Orca OS 提出故障响应和机动方案，一个独立程序把方案转成指令，再由"安全内核"按任务规则审核后批准或拦截，覆盖从轨道提升、编队飞行、碰撞规避到再入的全过程；地面保留两套半自主的监管系统。Orbital 认为，即使是 1000 颗卫星的星座，每天也有数千个决策，地面团队会成为项目最大的经常性成本，而 Orca 的方案可以把这部分成本降低约 10 倍。

文章同时给出了不少保留信息：Orbital 原定 2027 年发射、搭载 Nvidia Blackwell 芯片的探路任务已推迟到 2028 年；公司今年 6 月才走出隐身状态，迄今只公布了由 a16z 的 Speedrun 加速器领投的 500 万美元种子轮，如何支付 2000 万美元的 Orca 合同并不清楚，公司拒绝回答融资问题。背景方面，目前在轨活跃卫星估计超过 16900 颗，其中 11150 颗是 Starlink，另有约 3000 颗失效卫星；Starlink 上个月刚提出共享追踪数据的 Stargaze 项目。文章也提醒，在网络安全风险前所未有、轨道日益拥挤的时期，把无法手动关闭的系统自动化，可能会引起太空可持续性倡导者的担忧。

个人看法：这正好接上我之前写 SpaceX 太空数据中心时提出的问题——太空基础设施坏了怎么办、怎么维护。当时我列了三种方式：并行冗余、模块化更换、机器人在轨维修；这篇补充的是第四个维度，即"运营自主化"：不是修硬件，而是让每颗卫星自己处理日常运维和避碰。和 [Google 第一颗数据中心卫星上线](2026-11-01-google-s-first-data-center-satellite-is-online-and-writing-poetry.md)、[SpaceXAI 规划 6GW 数据中心](2026-11-08-spacexai-plans-data-center-in-arizona-musk-s-firm-claims-it-will-have-6gw-capaci.md) 放在一起看，轨道算力的叙事正在从"能不能把 GPU 送上去"走向"上去以后怎么低成本运营"。

投资角度先找瓶颈：轨道星座规模化的瓶颈之一是运营人力成本和碰撞风险，而解决它的层次是：第一层是星载计算和抗辐射芯片，因为每颗卫星都要跑 AI 模型，这把 edge AI 板块延伸到了太空，Nvidia 尝试把 Blackwell 送上轨道就是信号；第二层是空间态势感知和碰撞规避软件与数据服务（Orca 这类自主软件，以及 LeoLabs、Slingshot 这类追踪数据公司），利好太空经济板块；第三层才是轨道数据中心运营商本身，而它们目前大多还停留在 FCC 申报和 PPT 阶段。坦白说，一家只融了 500 万美元的公司签 2000 万美元合同、申报 10 万颗卫星，离兑现非常远，只能观望。值得跟踪的是 Orbital 能否完成下一轮融资，以及 2028 年探路卫星是否真的上天。
