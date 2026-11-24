# Even the best AI agents struggle with everyday life
https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/

这篇文章触及的是个人 AI agent 这条赛道当下最核心的一个问题:模型在编码和专业任务上的基准分数一路上涨,但"替普通人处理生活琐事"这件事真正卡住的,可能根本不是模型够不够聪明,而是在一堆杂乱、过时、甚至带有恶意的个人数据里,能不能稳定、安全地做对同一件事。如果这个判断成立,个人 agent 的竞争重心会从"谁的模型分数最高"转向"谁的执行环境和安全护栏做得最好"。

文章介绍了一个新的基准 ShellBench,由 The OpenClaw Foundation、Parsewave、Hugging Face、Red Hat 和 UC Berkeley 的研究者合作开发,基于超过一千万条匿名的真实 agent 交互记录,专门测试人们日常真正交给 agent 的工作。文章指出,即便是 OpenAI、Anthropic、Meta 最先进的模型,失败率也超过三分之一;所有模型的尝试中有 15.7% 至少违反一条安全要求。测试场景刻意模拟了真实的个人工作区:邮件、日历、表格、收据、聊天记录,夹杂着过时信息和钓鱼内容,agent 需要自己判断哪些信息相关、哪些是隐私、怎样完成任务又不制造新问题。

文章给出的失败可以拆成三类。第一是任务本身做不对,最强的模型也经常达不到要求。第二是不稳定,同一任务在完全相同的条件下跑三次,得分最高的 OpenAI GPT-6 Astra 三次全对的比例不到一半——对于本应在后台无人监督运行的助手来说,这几乎是致命的,因为用户如果需要反复跑几次才敢相信结果,"自动化"就失去了意义。第三是安全,约 10% 本来做对了的尝试仍然违反了至少一条安全标准:在处理孩子接送安排时,agent 有 79.5% 的情况没有正确考虑进去;在处理笔记本电脑保管记录时,有 18.6% 的尝试没能识别并隐藏一个敏感的银行上传令牌;另一个任务里,agent 有 40.3% 的情况建议了重复或错误的发票付款。

更有意思的是 harness 的作用。文章解释,harness 是控制模型如何获取信息、调用工具和执行动作的那一层软件。研究发现总体上模型的选择比 harness 影响更大,但在能力更强的模型之间,表现越来越依赖 harness:GPT-6 Astra 在 Pi harness 里胜过 Anthropic 的 Claude Fable 5.2,放进 Claude Code 里却输了;Meta 的 Muse Wonder Full 在 Pi 里得分 56%,在 Claude Code 里只有 38.1%;Muse Wonder 1.0 在五个 harness 上平均成功率 39.7%。文章也提醒,研究者没有在 Muse、Dots、Claude Duet 这些产品自己的原生 harness 里测试,所以结果不一定代表数百万消费者今天的真实体验。

个人看法:这篇和之前几篇放在一起看,线索很清楚。[Cyberhaven 发现 agent 在 100 次测试中 87 次泄露机密数据](2026-11-23-ai-agents-leaked-confidential-data-in-87-of-100-test-runs-cyberhaven-finds.md)、[Muse 混淆对话暴露隐私](2026-11-19-meta-s-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report.md)、[加州司法部长起诉 OpenAI 的失控 agent 事件](2026-11-16-california-state-ag-sues-openai-over-rogue-agent-incidents.md),再加上这次 ShellBench 的系统性数据,说明个人 agent 的问题不是个案,而是结构性的。这也呼应了 style_reference 里 Stroop Test 那篇的判断:Transformer 在长上下文、强干扰下保持目标的能力本来就弱,真实生活的数据恰恰是最"脏"的上下文。

先找瓶颈:模型能力当然还要继续提升,但这篇最值得注意的结论是"越强的模型越依赖 harness",也就是说边际瓶颈正在从模型层往执行层转移——一致性(同样输入同样结果)、隐私识别(哪些东西不能碰)和动作审批(付款前要不要停下来问)。所以受益的层次我会这么拆:第一层仍然是算力基础设施,一致性差的直接后果是要多跑几次、多做验证,每一次重试和 verifier 调用都是推理消耗;第二层是 harness 和 agent 框架本身,[MIT 的 VISTA harness](2026-11-08-mit-researchers-build-vista-an-agent-harness-that-keeps-images-in-memory-for-fas.md)、[MemCon](2026-11-21-researchers-at-ucla-washington-and-northwestern-release-memcon-for-agents.md) 这类工作,以及 LangChain、Claude Code 这类执行环境,会因为"同一个模型换个 harness 能差近 20 个百分点"而获得独立的定价权;第三层是 agent 安全与治理,包括 [PreTxt 的运行时监督层](2026-11-17-with-5m-in-funding-pretxt-launches-runtime-oversight-layer-to-supervise-ai-agent.md)、Onyx 这类治理工具,以及身份和数据防泄漏厂商。这些都挂在 AI板块下面,但真正受益的是解决"可靠性和安全"这个瓶颈的那一层,不是单纯卖"个人助手"概念的应用。

利空的一面也要说清楚:一千万级用户已经在用这类产品,而基准显示三分之一的任务做不对,这意味着个人 agent 的大规模付费转化可能比市场预期慢,监管和诉讼风险会先于收入到来。现在还早,值得关注的是 Meta、OpenAI、Anthropic 会不会拿自己原生 harness 去跑一遍 ShellBench 并公布结果,以及"三次全对"这种一致性指标会不会成为行业新的标准口径。
