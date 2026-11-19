# China-based AI robotics biotech firm MegaRobo raises $200M to accelerate scientific discovery
https://siliconangle.com/2026/11/19/china-based-ai-robotics-biotech-firm-megarobo-raises-200m-to-accelerate-scientific-discovery/

这篇融资新闻背后的命题是:AI for Science 的瓶颈正在从"模型能不能提出好假设"转向"谁来做实验验证"。模型可以在一夜之间生成上万条蛋白质序列,但每一条都需要湿实验去确认,如果实验仍然靠研究员手工移液、培养、成像,模型的产出速度就会被实验室的人手卡住。把实验室变成可编程的、机器人执行的基础设施,就是这类公司在押注的东西。

文章指出,MegaRobo 成立于 2016 年,做的是让 AI 软件可以运行物理实验的机器人系统,以及面向制造业的精密测量与检测工具。这一轮融资 2 亿美元,投资方包括阿曼投资局(Oman Investment Authority)、Asia Investment Capital、Granite Asia、创新工场(Sinovation Ventures)和招银国际(CMB International),公司累计融资 6 亿美元,其中 2022 年 C 轮接近 3 亿美元。创始人兼 CEO Daniel Huang 的说法是,第一代 AI 从人类已积累的知识中学习,下一代 AI 将越来越多地通过在物理世界中行动来学习,也就是通过实验、生产和持续反馈。产品上可以拆成三层:第一是 Megalaxy Lab,一个连接 AI 的实验平台,研究人员和 AI agent 可以配置实验、把实验路由到自动化实验室系统、跟踪执行、拿到结构化的机器可读结果,再直接喂给下一轮科学推理;第二是具体仪器,比如自动化细胞成像仪 CellVue T2000、样品制备工作站 Auflo 和细胞培养自动化系统 Seloris;第三是正在开发的 One Intelligence Stack,定位为连接仪器、机器、材料工艺和真实世界反馈的共同技术底座。文章还提到,MegaRobo 与腾讯云和 Twist Bioscience 等合作伙伴推出全球 AI 蛋白设计挑战 Poreva Open,向所有模型和方法开放,由 Megalaxy 为超过 1 万条蛋白设计序列提供湿实验验证。

这个"配置—执行—结构化结果—下一轮推理"的循环,本质上就是把强化学习里的环境交互搬进了实验室:模型是 policy,实验室是环境,实验结果就是反馈信号。区别在于实验室环境的一次交互可能需要几天,而且每次都要消耗真实试剂,所以谁能把单次实验的成本和时延压下来,谁就决定了整个循环能转多快。

个人看法:这篇和最近几篇可以串成一条线。[Import AI 481 里提到的给 AI 用的湿实验室](2026-11-16-import-ai-481-ai-sub-contractors-a-wet-lab-for-ai-and-subterfuge-during-developm.md)、[NVIDIA 在 SC26 上说 agent 是新的科学家、它们需要一个实验室](2026-11-17-nvidia-at-sc26-agents-are-the-new-scientists-and-they-need-a-lab.md),以及 [Isomorphic Labs 融资 50 亿美元推进临床](2026-11-17-isomorphic-labs-raises-5b-as-it-looks-to-take-drug-candidates-to-clinical-trials.md),讲的都是同一件事:AI 科学发现的闭环里,"实验执行"这一环正在变成稀缺资源。这让我想到目前 AI for Science 的价值大概分在三个位置:1. 模型和算力,负责生成假设,这是已经被充分定价的一层;2. 自动化实验执行,负责验证假设,也就是 MegaRobo 这类公司;3. 数据,实验产生的结构化失败与成功数据会反过来成为训练下一代科学模型的稀缺资产,这和 [RoboReward 用失败样本训练奖励模型](https://www.deeplearning.ai/the-batch/better-reward-models-for-robots) 的逻辑是相通的——真正值钱的不只是成功结果,而是大量带标签的失败。

先找瓶颈。这里的瓶颈是实验通量和标准化:手工实验慢、不可复现、结果不是机器可读的。解决这个瓶颈的层次才是受益方:第一层是实验室自动化硬件,液体处理、细胞培养、成像这类仪器,MegaRobo 之外,海外类似位置的还有 Thermo Fisher、Danaher 旗下的实验自动化业务,以及 Recursion 这种自建机器人实验室的药物发现公司;第二层是机器人本体和精密运动控制,实验室机器人对精度和洁净度要求高,但工作空间结构化,反而比通用人形机器人更早落地;第三层是 AI 算力和云,科学模型的训练和推理仍然需要大量 GPU,腾讯云出现在合作方里就是例子。从板块看,这对机器人板块是利好,而且是"结构化场景先落地"的那种更确定的利好;对 AI板块 是 AI for Science 需求继续扩大的又一个信号,和我之前说的"就算企业 AI 转型还没成功,科研仍然在持续消耗 AI 基础算力"是一致的。

不过这仍然是一家未上市公司的融资新闻,文章没有披露收入、客户数量或 Megalaxy 的实际实验吞吐量,"让真实世界实验可编程"目前更多是愿景表述。值得跟踪的是 Poreva Open 的结果:1 万多条序列经过湿实验验证后,有多少设计真正有效、不同模型之间差距多大,这会是检验"AI 设计 + 机器人验证"闭环是否真正跑通的第一组公开数据。
