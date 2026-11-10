# Hardware-testing and engineering startup Nominal raises $240M at $3B valuation
https://siliconangle.com/2026/11/09/ai-powered-hardware-testing-and-engineering-startup-nominal-raises-240m-at-3b-valuation/

这轮融资背后的命题是：AI 在软件开发里已经很普遍，但在火箭发动机、无人机、自动驾驶汽车这类"硬件"的研发里，真正拖慢迭代的往往不是设计，而是测试——每一次试验产生海量异构数据，工程师要花大量时间把它们拼起来才能知道哪里出了问题。如果 AI 能把"测试—分析—改设计"的循环压缩，硬件迭代速度会接近软件。

文章指出，Nominal 完成 2.4 亿美元 C 轮融资，由 Lightspeed Venture Partners 和 Insight Partners 领投，估值从今年 3 月 B-2 轮（融资 8000 万美元）时的 10 亿美元翻了三倍到 30 亿美元；其他投资方包括 Lux Capital、Sequoia、General Catalyst、Founders Fund、Avenir、Salesforce Ventures、M13 和 Lockheed Martin Ventures。文章解释了它解决的问题：硬件测试会产生传感器读数、日志、视频和仿真结果等数据流，问题不在于收集更多数据，而在于把这些来自不同测试系统的数据放在一起分析，还原出一次试验的全貌。Nominal 的平台把这些信息整合起来，自动化测试，并由名为 Nominal Analyst 的 AI agent 基于底层证据做调查分析，帮助比较不同试验、对照需求核查结果。平台支持 API、Model Context Protocol 和 SQL，开发者也可以在上面构建自己的应用和 agent。应用对象包括飞机、火箭发动机、自动驾驶汽车、无人机和能源系统；目前超过 80 家商业和政府机构使用，包括七大国防承包商中的五家，客户有 Anduril、军舰制造商 Huntington Ingalls（HII）以及高速飞行器公司 Hermeus。CEO Cameron McCord 强调"工程师始终掌控"。

个人看法：这篇和今天 [agentic robotics](2026-11-09-can-agentic-robotics-solve-robotics-data-scaling-problem.md) 那篇其实在讲同一件事的两面：一个是让 agent 写机器人控制代码，一个是让 agent 分析硬件测试数据，共同点都是把 LLM 在软件和数据处理上的能力"迁移"到物理世界的工程流程里。之前 [Shield AI 收购 Echodyne](2026-11-05-autonomous-combat-drone-maker-shield-ai-buys-radar-startup-echodyne-for-5-3b.md) 那篇也能看出国防科技公司正在快速扩张，而 Nominal 的客户结构正好踩在这个周期上。我觉得 AI 进入硬件研发大概有三个环节：1. 设计阶段的生成式设计和仿真（EDA、CAE 软件的 AI 化）；2. 测试和验证阶段的数据整合与分析（Nominal 所在的环节）；3. 生产和运维阶段的预测性维护。第二个环节过去最缺标准化工具，因为每家公司的测试台都是自己拼起来的。

投资角度先找瓶颈：硬件研发的瓶颈是"测试数据到工程结论"的周期。受益层次是：第一层是需要高频迭代的硬件公司本身，尤其是国防科技、商业航天和无人机，它们的研发速度会直接受益，利好太空经济板块（火箭发动机、高速飞行器）和机器人板块（无人机、自动驾驶）；第二层是测试测量和数据采集硬件供应商，比如 National Instruments（现属 Emerson）、Keysight 这类，因为 AI 分析的前提是高质量的传感器数据；第三层是 Nominal 这类工程软件平台，但它仍是一级市场标的。需要提醒的是，3 月到 11 月估值翻三倍，反映的是国防科技赛道的热度，和中期选举后的 AI 股回调形成对比。值得跟踪的是 Nominal 是否扩展到半导体、汽车等民用大规模制造领域，以及传统 CAE/测试厂商的回应。
