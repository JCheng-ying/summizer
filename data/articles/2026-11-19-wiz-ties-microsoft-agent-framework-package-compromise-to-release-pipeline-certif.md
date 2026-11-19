# Wiz ties Microsoft Agent Framework package compromise to release pipeline certificate
https://siliconangle.com/2026/11/19/wiz-ties-microsoft-agent-framework-package-compromise-to-release-pipeline-certificate/

这篇文章背后的命题是:AI agent 正在变成企业里权限最大的一类软件,而它们的开发工具链本身成了攻击面。agent 框架天然被安装在开发机、CI 构建机和云上的运行环境里,这些地方恰好存着云凭证、部署令牌和模型平台密钥。如果攻击者能在 agent 框架的官方发布渠道里塞进东西,拿到的就不是一台机器,而是一整条通往云资源的钥匙串。

文章指出,Microsoft 用于其 AI agent 工具包 Agent Framework 的官方 Python 包本周被攻破,攻击者通过 Microsoft 自己的发布者账号向 PyPI 发布了 1.26.1 和 1.26.2 两个恶意版本,看上去就是一次例行更新。这个包每月下载量接近 20 万次,两个版本大约一小时内被撤下,但这一小时里安装过的人都面临风险。云安全公司 Wiz 的研究人员发现,攻击者似乎是用了 Microsoft 内部 Engineering System Release Pipeline(公司用来签名和发布软件包的内部服务)的客户端证书和私钥获得了发布权限。该服务的地址过滤拦下了攻击者第一次从 AWS 发起的尝试,但第二次从 Microsoft 自有的地址空间发起时成功了。凭证是怎么泄露的目前不清楚,截至周三 Microsoft 也没有回应 BleepingComputer 的置评请求。

恶意代码的投放方式值得拆开看。文章指出,两个版本都加了一个 .pth 文件,这是 Python 每次启动时都会执行的文件类型,所以哪怕根本没有 import 这个框架,窃取程序也会运行;同时两个版本仍把正版的 agent-framework-core 1.26.0 列为依赖,框架照常工作,恶意代码在后台运行,使用者很难察觉。运行之后它做了几件事:第一是从环境变量和其他正在运行的进程里收集密钥;第二是读取 Azure、npm、Git、Docker、Hugging Face 等服务的凭证文件;第三,据应用安全公司 Endor Labs 的说法,它会为 12 个资源申请 Azure 托管身份令牌,第二个版本还增加了对 GitHub Actions 令牌的请求。数据被压缩、编码后发往攻击者控制的 webhook.site 地址。OpenSourceMalware 的研究人员把它定性为专注于凭证和令牌窃取的工具,而不是远程控制木马,它不会在受感染系统里留下持久化组件。

还有一个细节:攻击者的工具会把进度回报到同一个用来收集赃数据的公开 webhook,Wiz 因此观察到了部分行动过程,工具自称 Cairn,是一个使用 AI 的开源渗透测试框架。受害规模方面,Wiz 的分析认为可能不大,但它只覆盖了攻击者免费 webhook.site 账号保留下来的 50 条请求,其中 17 条只对应 3 次独立的成功窃取,其余来自攻击者自己的机器以及沙箱和安全厂商的扫描。文章也提到这不是今年第一次:5 月 Microsoft 的 durabletask 包因 PyPI 令牌被盗遭劫持,那次攻击被关联到 TeamPCP,也就是攻破 LiteLLM 的同一个团伙,但 Wiz 表示尚未把两起事件联系起来。研究人员建议安装过恶意版本的人一律按凭证泄露处理,从 1.26.0 重建并轮换受影响系统能访问的所有密钥。软件供应链安全公司 Cloudsmith 的安全负责人 James Matchett 补充了一个很现实的盲点:生产环境的依赖清单里可能根本看不到这个框架,而某台构建机可能装过它、在告警到达前就已经销毁了,如果那台构建机有部署令牌,团队就必须查清它装的是哪个版本、令牌能访问什么。

个人看法:这件事和前两天写的 [Microsoft 在 Ignite 2026 上把 Copilot 改造成常驻自主 agent](2026-11-17-at-ignite-2026-microsoft-reinvents-copilot-as-the-autonomous-engine-of-enterpris.md) 以及 [Foundry 的 agent 持续改进闭环](2026-11-17-microsoft-rolls-out-new-first-party-models-and-updates-to-agentic-ai-continuous-.md) 放在一起看会更有意思。那两篇讲的是 agent 拿到自己的身份、记忆和工具,开始长期自主干活;这一篇则说明,agent 的权限越大,构建和发布 agent 的那条流水线就越值钱。我觉得企业 agent 落地目前卡住的瓶颈之一,不是模型能力,而是"敢不敢把权限交出去"——也就是信任和安全。攻击这次用的不是什么高深漏洞,而是三件很朴素的事:第一是发布签名凭证外泄,第二是 Python 启动机制里不需要 import 就会执行的 .pth 文件,第三是短生命周期的 CI 构建机让事后取证几乎无从下手。再加上攻击方自己用的是一个带 AI 的渗透框架,攻防两边都在被 AI 放大。

按照"先找瓶颈再找解决瓶颈的那一层"的思路,这件事对 AI 板块的影响是结构性的,不是利空 agent 本身,而是把一部分价值推向安全层。受益的层次我会这么排:第一层是软件供应链安全,也就是包签名、来源证明、依赖扫描和制品仓库管理,文章里出现的 Wiz、Endor Labs、Cloudsmith 都在这一层,原文没提到的 JFrog、Snyk、Sonatype 也属于这一层;第二层是密钥与非人类身份管理,因为窃取的目标全是令牌和凭证,把长期密钥换成短期、可撤销的身份令牌这件事会更急迫,CyberArk、HashiCorp Vault、Okta 这类公司处在这里;第三层是云和运行时安全,也就是能在构建机、容器里实时发现异常外传的 CrowdStrike、Palo Alto Networks 等;第四层才是 agent 平台本身,谁能把"可审计、可撤销、最小权限"做成默认配置,谁在企业采购里就更占优势,Microsoft 这次反而在这点上失分。另外值得一提的是 Hugging Face 的凭证也在被窃取名单里,说明模型权重和数据集仓库已经被攻击者视为和代码仓库同等价值的目标。

不过目前确认的受害者只有三例,单一事件不会改变任何公司的基本面,我也不会因此对 AI 板块整体变得悲观。值得关注的是 Microsoft 后续会不会公布签名凭证泄露的原因,以及 PyPI、npm 这类公共包仓库会不会加快强制推行可信发布和来源证明;如果类似事件在 agent 框架里继续高频出现,企业安全预算向 AI 供应链安全倾斜就会从一个判断变成一个可以跟踪的订单信号。
