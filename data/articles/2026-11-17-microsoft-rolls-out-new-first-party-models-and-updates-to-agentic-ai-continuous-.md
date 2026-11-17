# Microsoft rolls out new first-party models and updates to agentic AI continuous improvement
https://siliconangle.com/2026/11/17/microsoft-rolls-out-new-first-party-models-and-updates-to-agentic-ai-continuous-improvement/

这篇文章背后的命题是:Microsoft 正在把自己从"OpenAI 模型的分销商"变成一个同时握有自研模型、开源底座改造模型和第三方模型目录的平台,并且把竞争重心放在"agent 上线之后怎么持续变好"这一环。如果这条路走通,企业 AI 的价值会越来越多地沉淀在评估、反馈和再训练的闭环里,而不是某一个单独的模型里。

文章指出,Microsoft 今天对企业 AI 平台 Foundry 做了一轮更新。第一是数据和上下文,Foundry IQ(属于 Microsoft IQ)现在开箱即提供企业知识图谱,把非结构化数据和应用数据整合起来,给 agent 提供上下文。第二是持续改进闭环,Foundry 利用已有的可观测性能力让 agent 在质量、安全、延迟和成本四个维度建立基线;新增的人工标注(预览中)允许业务专家给 agent 的执行轨迹打分和评论,这些反馈再结合针对评估集的优化测试和真实结果对比,进入下一轮改进;Foundry 还可以用组织自己的数据对支持的模型做强化学习,算力由 Foundry 提供。每次改进的结果成为下一个基线。

第三是模型本身。文章指出,决策模型 Decision-1.1 正式可用,它是在 10 月发布的 Microsoft-Decision-1 基础上的新一代,定位是在软件中大规模、低成本地做可靠决策,用于路由、分类、优先级排序、校验和工作流控制,输出带校准的置信度,不确定性高时应用可以选择不采纳。值得注意的是,文章说它换了一个新底座:Google 的 Gemma 4 26B A4,并因此加入了多模态,能分析指令里的图片。此外,Microsoft AI 的自研 MAI 系列加入 Foundry:MAI-Code-2 面向高强度的 agentic 编程,MAI-Code-2-Flash 面向高频日常编程,两者已在 GitHub 正式可用;MAI-Image-2.7 及其 Flash 版本处于预览;MAI-Cyber-2-Flash 是专门的网络安全模型,在 Microsoft 的 agentic 代码安全系统 Codename MDASH 中预览。Foundry 的模型池扩展到前 50 名模型,配有模型路由器和 AI Gateway,整个目录有超过 11000 个模型,来自 OpenAI、Anthropic、Meta、Mistral 和开源社区。

个人看法:这篇最有意思的细节是 Microsoft 的决策模型建在 Google 的开源 Gemma 上。这说明在决策模型这个品类里,底座是谁并不重要,重要的是校准和后训练——这和今天早些时候 [决策模型那篇](2026-11-17-as-decision-model-use-skyrockets-is-customization-the-next-frontier.md) 里"模型容易复制、护城河在数据和持续调优"的判断完全吻合,那篇里 Microsoft 的负责人还强调过不要刷榜,而这次 Foundry 加的人工标注和强化学习闭环正是把"持续调优"产品化。同一天的 [Model ML 融资](2026-11-17-model-ml-raises-250m-to-automate-investment-banking-grunt-work.md) 也在用开源模型压低成本,两条新闻说的是同一个趋势:开源底座 + 专用后训练正在吃掉企业里大量高频、格式固定的调用。另外,Microsoft 一边与 Anthropic 签算力合同(见 [Anthropic 再与 Microsoft 签 43 亿美元算力协议](2026-11-11-anthropic-signs-another-4-3bn-in-compute-agreements-with-microsoft.md)),一边在 Foundry 里上架 Anthropic 和 OpenAI 的模型,同时推自研 MAI 系列,它的定位越来越像一个"模型中立的分销 + 自研补位"的平台。目前来看 agent 的持续改进大概有三种做法:1. 只改提示词和检索上下文,成本最低但上限有限;2. 用人工标注和评估集做离线迭代,这是 Foundry 这次的主线;3. 在组织数据上做强化学习,效果最好但需要算力和高质量反馈。Foundry 把三种都放进了同一个平台。

投资角度,先找瓶颈:企业 agent 落地的瓶颈已经不是"有没有模型可用",一万多个模型足够多了;瓶颈在于第一,agent 拿不到正确的企业上下文;第二,上线后无法衡量和持续改进;第三,推理成本太高。Foundry 这次三个方向各补了一块。受益的层次会是:第一层仍然是算力,强化学习"由 Foundry 运行计算"意味着后训练负载从少数模型实验室下沉到成千上万家企业,这对 Azure 的 GPU 需求、以及 Nvidia 这类供应商是增量,因为每一轮改进闭环都要消耗训练和评估算力;第二层是握有企业数据入口的平台,Microsoft 凭 Office、GitHub、Azure 的客户关系最有条件做"知识图谱 + 反馈闭环",这是这篇最直接的受益方;第三层是 Google,Gemma 被 Microsoft 用作商用决策模型底座,虽然不直接收费,但强化了 Gemma 在开源生态里的地位。相对承压的是单纯卖通用 API 的模型层和小型决策模型创业公司,前者在路由和分类这类调用上被替代,后者要面对云厂商直接把同类产品做进平台。这篇挂 AI 板块;Decision 这类小模型将来可能下沉到端侧,但原文没有涉及端侧部署,我不挂 edge AI 板块。

现在这些更新大部分处于预览阶段,MAI 系列和第三方前沿模型相比到底处在什么水平,文章也没有给出基准数据。值得跟踪的是 Foundry 的强化学习功能何时正式可用、企业是否真的愿意为"持续改进"付费,以及 GitHub 上 MAI-Code-2 能拿到多少原本属于 OpenAI、Anthropic 模型的编程调用份额。
