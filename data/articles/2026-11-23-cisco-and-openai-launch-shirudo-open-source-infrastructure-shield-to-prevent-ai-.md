# Cisco and OpenAI launch Shirudo open-source infrastructure shield to prevent AI-driven cyberattacks
https://siliconangle.com/2026/11/23/cisco-and-openai-launch-shirudo-an-open-source-infrastructure-shield-to-protect-against-ai-driven-cyberattacks/

这篇文章讨论的是一个越来越清晰的范式转移:当 AI 让漏洞"还没公开就已经被利用",传统"发现漏洞 → 写补丁 → 全网打补丁"这条以周甚至月为单位的防御链条就彻底失效了。如果这个前提成立,基础设施安全就必须从"事后修补"变成"运行时自我防御",而且防御本身也只能由 AI agent 以机器速度来执行。

文章指出,OpenAI 和 Cisco 宣布了一个开源的 Secure Infrastructure Project,目标是让所有 AI 计算基础设施在设计上就是安全的,能抵御极快的 AI 驱动攻击;第一个项目是 Shirudo(日语"盾"),用于在补丁就位之前自动保护基础设施免受关键漏洞攻击。文章引用 Cisco 安全 CTO Thomas Graf 的说法:行业一直把安全当成事后附加的东西,因为过去的基础设施是为人类速度的工作流设计的;现在一个广泛使用的软件出现重大漏洞,修复并确保所有系统打上补丁往往要几周甚至几个月,而"平均利用时间已经变成负数",也就是越来越多的漏洞在公开之前就被利用,随着开放权重模型的网络安全能力提升,这会成为常态。

文章提出两家公司的思路可以拆成三层:第一是基础设施要默认加固、不可变、并且可以从之前的"良好状态"重建,出了问题可以快速回滚;第二是以可信平台模块(TPM)为基础,并用强化学习安全地测试自己的防御,以应对未知攻击路径;第三是在运行时保护工作负载,这就是 Shirudo 的定位。Shirudo 是开源运行时安全项目 Tetragon 的演进,基于 Linux 内核技术 eBPF——文章的解释是,eBPF 允许经过验证的小程序在内核里运行,观察应用行为并修改其行为,而不需要改源代码或重启,就像 JavaScript 让浏览器无需重启即可编程。Graf 表示选择 eBPF 是因为没有真正的替代方案,面向人的安全控制台和策略语言对 AI agent 来说太慢。通过可编程的内核接口,agent 可以采集细粒度遥测、先以监控模式评估缓解措施,再在毫秒级部署经过加密签名的"盾牌",在不中断线上业务的情况下实时拦截利用未知漏洞的攻击。

OpenAI 的角色是验证这套方法。文章指出,OpenAI 已经把 Shirudo 部署在由其 Codex 编程 agent 驱动的 agent 控制平面里:拿到新漏洞的细节后,Codex 用 Shirudo 自主构建漏洞复现程序,设计缓解策略,验证缓解代码,再把签名后的盾牌部署到所有受影响节点。两家公司最近用 OpenJDK 中一个名为 Java4Shell 的新严重漏洞做了测试,Shirudo 迅速生成 Java 字节码,直接注入正在运行的 Elasticsearch agent,拦截了本会导致系统被攻破的恶意 Base64 覆写。

个人看法:这篇和最近几篇安全文章连起来看,逻辑链条非常完整。[Google 的 AI 框架无人参与地把补丁变成漏洞利用](2026-11-16-google-says-an-ai-framework-turned-security-patches-into-exploits-with-no-human-.md) 说明进攻端已经自动化;[GPT-6 Astra 安全调优版关闭 Linux 根权限漏洞](2026-11-13-openai-s-security-tuned-version-of-gpt-6-astra-closed-root-level-linux-holes-for.md) 说明防守端开始用模型找漏洞;[Satya Nadella 谈关键基础设施](2026-11-18-amidst-fears-of-ai-cyberattacks-satya-nadella-says-lots-of-critical-infrastructu.md) 和 [一连串宕机那篇](2026-11-18-recent-spate-of-outages-attributed-to-technical-issues-amid-accelerated-ai-bug-d.md) 则暴露出真正的瓶颈——不是找不到漏洞,而是补丁部署太慢、而且仓促打补丁本身会造成宕机。Shirudo 恰好卡在这个瓶颈上:它不替代补丁,而是在"发现"和"修好"之间插入一个毫秒级、可回滚的临时防线。这和同一天 [CrowdStrike 收购 Zscaler 那篇](2026-11-23-crowdstrike-to-buy-zscaler-in-record-setting-43-9b-cybersecurity-deal.md) 是两条不同的路线:CrowdStrike 走的是封闭的统一平台,Cisco 和 OpenAI 走的是开源内核层。

对 AI板块 的受益层次:第一层是掌握运行时和网络层的基础设施厂商,Cisco 早年收购了 Tetragon 背后的 Isovalent,这次等于把开源项目变成自己 AI 基础设施安全叙事的核心,和 [Cisco 上调 AI 基础设施收入预期那篇](2026-11-12-cisco-beats-expectations-lifts-guidance-and-forecasts-ai-infrastructure-revenue-.md) 能对上;第二层是模型公司,Codex 在这里从"写代码的工具"变成"持续运行的安全运维 agent",这是一种全天候、按事件触发的推理负载,对 OpenAI 的企业收入是新的入口;第三层是硬件信任根,TPM 和机密计算相关的芯片与模组会因为"可信、可重建的基础设施"这个要求获得更多需求。但也要看到,文章本身带有明显的发起方叙事色彩,Java4Shell 的测试结果也只是两家公司自己披露的,未经独立验证;而且让 agent 直接往生产系统内核里注入代码,本身就是一个新的攻击面。现在只能观望,值得跟踪的是有没有 Cisco 和 OpenAI 之外的大型云厂商或内核社区真正参与进来——开源安全项目的价值取决于它能不能成为事实标准。
