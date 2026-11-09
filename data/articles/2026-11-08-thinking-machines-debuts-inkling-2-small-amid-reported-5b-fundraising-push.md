# Thinking Machines debuts Inkling 2 Small amid reported $5B fundraising push
https://siliconangle.com/2026/11/06/thinking-machines-debuts-inkling-2-small-amid-reported-5b-fundraising-push/

这篇文章的核心命题是"让 AI 去做 AI 研究":Thinking Machines 发布的新模型专门用自动化 AI 训练任务来训练,也就是让模型学会微调别的模型、优化内核。这是之前多篇 Import AI 讨论过的递归自我改进(RSI)在产品层面的一个具体形态。

文章指出,由前 OpenAI CTO Mira Murati 去年创立的 Thinking Machines Labs 发布了 Inkling 2 Small;据 Business Insider,公司正在进行由 Accel 领投的 50 亿美元融资,估值预计 400 亿美元。模型在 GB300 NVL72 机架集群上训练,每台机架包含 72 块 Blackwell Ultra GPU,预训练用了 68 小时,之后是九天的强化学习。训练数据包括数十万个长周期编程挑战,其中有一批复杂的"自动研究"任务,要求模型对神经网络做后训练、优化 LLM 内核等。测试中,它被要求微调开源模型 Qwen3.5-4B 以提升天气预测等预测能力,4.5 小时内把预测得分翻倍。它在三个知识工作基准上超过 Spark Open、Kimi K3 等开源模型,在多个金融任务数据集上也得分更高。模型总参数 5,940 亿,其中视觉编码器 2.92 亿,每次推理激活约 170 亿参数,可以调节计算投入。视觉编码器让它能"看"自己生成的页面,比如做电商网站时检查商品页是否正确渲染。模型已在 Thinking Machines 的 Tinker 云服务上线,权重将在下周以开源许可发布。

个人看法:这和之前写过的 [Import AI 478 里 RSI 的讨论](2026-11-01-import-ai-478-math-for-alignment-programbench-and-mirendil-shows-what-rsi-means.md) 以及 NVIDIA ENPIRE 自我进化机器人是同一个方向:把"改进模型"这件事本身自动化。今天 [Anthropic 招股书](2026-11-08-anthropic-s-s-1-outlines-company-s-strong-financials-methods-potential-risks-aft.md) 也披露 Claude 写了公司代码库 90% 以上的贡献,说明这件事已经在发生。先找瓶颈:AI 研究的瓶颈之一是顶尖研究员的时间,如果模型能自动完成微调和内核优化,迭代速度就不再受人数限制,而是受算力限制。受益的层次会是:第一层是算力,自动化研究意味着更多实验、更多训练跑次,GB300 NVL72 这种机架级系统是直接受益,NVIDIA 仍然是确定性受益方;第二层是后训练和微调平台,Tinker 这类服务正是在卖"让客户自己定制模型"的能力;第三层是开源模型生态,一个 5,940 亿参数的开源模型会继续压低闭源模型的定价,这和今天 [Ramp 数据](2026-11-08-ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo.md) 显示的价格战形成呼应。我会把它挂在 AI 板块。需要注意的是基准结果都是公司自报,而且对比的主要是开源模型,值得跟踪的是下周权重开源后社区的独立测试。
