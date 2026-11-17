# Noeri raises $110M to help companies build living AI systems that self-improve over time
https://siliconangle.com/2026/11/16/noeri-raises-110m-to-help-companies-build-living-ai-systems-that-self-improve-over-time/

这篇文章背后的命题是:企业 AI 的未来究竟是"租用一两个最强的通用模型",还是"拥有一套由多个小模型、工具和工作流组成、能自己变好的系统"。如果后者成立,价值会从前沿模型的 API 收入,部分转移到编排层、后训练层和企业自己的数据上。

文章指出,斯坦福的两位知名 AI 研究者 Yejin Choi 和 Carlos Guestrin 创立的 Noeri 带着 1.1 亿美元融资亮相,本轮由 Menlo Ventures 领投,Madrona Ventures、Kindred Ventures、Wing Venture Capital、NEA 参投,Snowflake 和 Cisco Ventures 也参与了。Noeri 的软件会研究企业的数据、工作流和业务流程,然后针对具体任务提出改进建议,比如换一套指令、换一个工具,或者把工作流里某一步用的模型换成另一个;每条建议都附带解释,并且要交给人审核后才生效,文章把这类比为 AI 生成的代码改动走代码审查的流程。它同时支持开源权重模型和闭源模型,客户保留对工作流和所建系统的完全所有权。

文章提出,这家公司建立在两条研究线上。第一是 Guestrin 的自蒸馏(self-distillation)技术,让模型充当自己的老师,把犯过的错误转成训练信号,随时间改进回答;第二是 Choi 在 agentic 编排上的研究,表明由较小的模型去指挥一组 agent 和工具,可以用更低成本超过大得多的前沿模型。公司的起点也很具体:为了帮斯坦福一个微生物与免疫学团队更省钱地使用 OpenAI 的模型,两人做了一个学会调用 OpenAI 旧模型的小模型,微调之后在该团队的项目上表现超过了 GPT-5。文章还交代了创始人背景:Guestrin 参与开发了 XGBoost,联合创立的 GraphLab(后改名 Turi)2016 年被 Apple 收购,之后在 Apple 领导机器学习研究;Choi 曾在 Allen Institute for AI 带常识推理团队,2024 年以杰出科学家身份加入 Nvidia,约一年后离开去了斯坦福。Noeri 意为"复数的智能",两人在博客里的比喻是:很少有公司会把核心业务交给一个同时给所有竞争对手做顾问、可以随时改条款、而且永远无法内化的顾问,而单一的中心化 AI 恰恰就是这种安排。文章也提到同样主张多模型未来的还有 Mira Murati 的 Thinking Machines(去年推出了微调云服务 Tinker)和派工程师驻场帮客户微调的 Applied Compute。

个人看法:这和之前写过的 [Thinking Machines 发布 Inkling 2 Small](2026-11-08-thinking-machines-debuts-inkling-2-small-amid-reported-5b-fundraising-push.md) 以及此前 Import AI 介绍过的 NVIDIA ENPIRE 自我进化机器人是同一条线——把"改进 AI 系统"这件事本身自动化。区别在于层次:ENPIRE 是在训练闭环里自动改代码,Inkling 是让模型学会微调别的模型,而 Noeri 把这件事放到企业工作流层面,而且保留了人工审核这一步,更像是把"self-improvement"包装成企业能接受的变更管理流程。目前来看企业获取 AI 能力大致有三种方式:1.直接调用最强的闭源前沿模型,能力最强但成本高、锁定深;2.自己用开源模型加微调平台(Tinker 这类)去定制,需要较强的工程能力;3.由编排层自动组合多个小模型和工具并持续优化,也就是 Noeri 押注的方向。

先找瓶颈:文章里 Choi 自己点出了企业的两难——要么付不起最强模型的费用,要么接受较差模型的结果。所以瓶颈是推理成本和锁定风险,而不是模型能力本身。受益的层次会是:第一层仍然是算力,但需求结构会变化,小模型持续自蒸馏和反复微调意味着更多分散的训练和推理任务,对 GPU 总量依然是正面,NVIDIA 仍是确定性受益方,而小模型推理也会给推理专用芯片和云上的推理服务带来机会;第二层是数据平台,自我改进的前提是能持续读取企业数据和工作流记录,这也解释了为什么 Snowflake 会出现在投资人名单里,企业数据平台(Snowflake、Databricks)的数据会成为这类系统的燃料;第三层是开源权重模型生态,多模型编排天然偏好便宜、可替换的模型,Meta Llama、Qwen、DeepSeek 这一类会被更多调用;反过来,对按 token 收费的前沿模型 API 是一个温和的定价压力。这篇我挂在 AI 板块。

现在还早:Noeri 刚成立半年,"小模型超过 GPT-5"只是一个研究团队项目上的案例,不是通用结论,文章也没有给出客户名单或收入数字。值得关注的是它说的"包括部分投资人在内的多行业合作伙伴"后续会不会落成具体的公开部署案例,比如在 Snowflake 或 Cisco 的产品里出现集成,那会比融资金额更能说明这条路线是否成立。
