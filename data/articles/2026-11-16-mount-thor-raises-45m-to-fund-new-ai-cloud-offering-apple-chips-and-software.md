# Mount Thor raises $45m to fund new AI cloud offering Apple chips and software
https://www.datacenterdynamics.com/en/news/mount-thor-raises-45m-to-fund-new-ai-cloud-offering-apple-chips-and-software/

这笔融资规模不大,但它测试的是一个有意思的假设:AI 推理和 Agent 工作负载,是否一定要跑在英伟达 GPU 上?如果答案是否定的,那么"推理算力"这一层就可能被消费级芯片架构切走一部分。

文章指出,新成立的 AI 云服务商 Mount Thor 累计融资 4,500 万美元,包括 CRV 和 Conviction 联合领投的 A 轮,以及此前由 Chad Byers 和 Offline Ventures 联合领投的种子轮;来自 Cognition、Meta、OpenAI、Together AI、Vercel 等公司的个人天使也参与了。公司还筹集了非稀释性资金用于购买硬件,股权融资主要用于扩充团队和购买算力。它的产品是把 Apple 硬件和 macOS 放进数据中心,提供裸金属 Apple 机器和虚拟机,面向研究实验室、应用 AI 公司和企业。CEO Peter Voell 的论点有两层:第一,macOS 几十年在无障碍和人机交互上的积累,让它成为"Agent 工作、人类监督 Agent"的最佳环境;第二,M5 Ultra 这类 Apple 芯片正在成为更省电、更省成本的生产级推理平台。文章也提到不确定性:公司称不到六个月就部署了第一个数据中心,但没有披露地点、规模,也没说是否为独立设施。此外,AWS、Scaleway、Oracle Cloud 已有 Mac 实例,MacStadium 等少数第三方也专做 Apple 硬件托管;Apple 自己据报道在研发对外销售的 AI 服务器,并在 2025 年 2 月宣布了德州服务器工厂。

需要说明的是,"Apple 芯片更省电、更省钱"是公司 CEO 和投资方的说法,原文没有给出任何对比数据,应当按未经独立验证处理。

个人看法:我觉得这件事真正的逻辑在第一层而不是第二层。用 Apple 芯片跑大规模推理和 H100/B200 集群去比吞吐,很难占到便宜;但"让 Agent 操作一台真实的 Mac"是一个 GPU 云给不了的东西——computer use 类的 Agent 需要的是完整的操作系统、图形界面和应用生态,而不只是矩阵乘法。这和之前写过的 Agent 需要 Planner、Memory 等"Transformer 外面的管理层"是一条线:Agent 越成熟,它需要的运行环境就越像一台完整的电脑,而不是一块 GPU。

目前来看给 Agent 提供运行环境有三种方式:1. 云端 Linux 沙盒(Daytona、E2B 这一类),便宜、可规模化,但很多桌面应用跑不了;2. Windows 或 macOS 虚拟机,兼容性好但授权和硬件约束多,Mac 尤其如此,因为 macOS 只能合法运行在 Apple 硬件上;3. 直接在用户本地设备上跑,也就是 edge AI 的路径。Mount Thor 押的是第二种里最难规模化的那一块。

按先找瓶颈的思路,这里的瓶颈是"能合法、大规模运行 macOS 的数据中心容量",解决它的只能是 Apple 硬件本身。所以受益的层次会是:第一层是 Apple 自己,无论 Mount Thor 成败,它买的都是 Apple 的机器,而且这也给 Apple 自研 AI 服务器提供了一个外部需求验证——这对 edge AI 板块是一个侧面信号,因为同一套为终端设计的低功耗芯片被拿去做云端推理;第二层是 AI 板块里的 Agent 平台层,如果"给 Agent 一台 Mac"成为标准做法,Cognition 这类 Agent 公司会是主要客户;第三层才是 Mount Thor 这类托管商,它的护城河很薄,AWS 已经有 Mac 实例,Apple 如果自己下场,它会首当其冲。现在只能观望,值得跟踪的是 Mount Thor 是否会披露第一个数据中心的规模和客户,以及 Apple 对外销售 AI 服务器的计划是否落地。
