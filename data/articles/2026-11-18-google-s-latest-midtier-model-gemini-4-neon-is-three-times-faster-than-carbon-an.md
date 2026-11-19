# Google’s latest midtier model Gemini 4 Neon is three times faster than Carbon and wins on some metrics
https://siliconangle.com/2026/11/18/googles-latest-midtier-model-gemini-4-neon-is-three-times-faster-than-carbon-and-wins-on-some-metrics/

当一家公司的中端模型在部分测试上超过自家旗舰、速度快三倍、成本低六成,真正被改写的是"旗舰"这个概念本身:前沿模型的竞争正在从单一的能力排名,变成在能力、速度、价格三个维度上同时比较的产品矩阵,而企业客户的采购决策会越来越像在买云服务的实例规格,而不是在挑"最聪明的那个"。

文章指出,Google 在一个月前发布旗舰 Gemini 4 Carbon、随后推出低成本的 Gemini 4 Hydrogen 之后,今天发布了定位介于两者之间的 Gemini 4 Neon,用于复杂编程、多步 agent 工作流和分析推理。按 Google 自己公布的基准,Neon 在部分任务上超过了 Carbon,完成大多数任务的速度约为 Carbon 的三倍、成本低约 60%;Google 还称 Neon 在知识工作、推理、自动化、多模态理解、网络安全、科学和数学等测试上超过了同为中端定位的 Claude Opus 5.5 和 GPT-6.2 Sol。这些是厂商自测数据。独立评测机构 Artificial Analysis 给出的智能指数是 61,排第三,仅次于 Anthropic 的 Claude Fable 5.2(65)和 OpenAI 的 GPT-6.2 Astra(62);Artificial Analysis 还提到这是 Google DeepMind 七周内发布的第四个模型,智能分数比 Carbon 略高,单任务成本低约 17%。

价格是这篇文章里更值得拆开的部分。文章指出,Neon 定价为每百万输入 token 3 美元、缓存输入 0.15 美元、输出 15 美元,正好夹在 GPT-6.2 Sol(2 美元/0.10 美元/10 美元)和 Claude Opus 5.5(4 美元/0.20 美元/20 美元)之间。文章认为,既然中端模型的性能已经如此接近,成本效率就成了企业客户越来越看重的因素,Neon 在部分负载上的小幅领先,未必足以让很多机构愿意多付钱。需要说明的是,原文在这一段写的是 Neon 领先"GPT-6.2 Sol 和 Claude Fable 5.2",和前文对比对象 Claude Opus 5.5 不一致,Fable 5.2 在独立指数上其实排在 Neon 之前,这里应以前文为准。Neon 今天起向 Google AI Pro 和 Ultra 订阅用户开放,开发者可以通过付费 API、Antigravity 平台等渠道使用。

把这几组数字放在一起,能看出三件事:第一,"三倍速度、低 60% 成本"是和自家旗舰比,不是和竞品比,对外定价上 Neon 并没有打价格战,而是选在中间;第二,独立指数上前三名之间只差 1 到 4 分,头部模型在能力上已经进入"贴身肉搏";第三,七周四个模型的节奏说明 Google 在用发布频率而不是单个模型去抢位置。

个人看法:这是 Gemini 4 家族的第四步,接在 [Argon](2026-11-01-google-s-first-gemini-4-model-argon-avoids-hallucinations-and-shines-at-knowledg.md)、[Carbon 登顶智能指数](2026-11-08-google-gemini-4-carbon-tops-intelligence-index-cybersecurity-benchmarks.md)、[Hydrogen](2026-11-12-google-releases-gemini-4-hydrogen-a-lower-cost-model-said-to-outscore-argon.md) 之后;而在 Hydrogen 那篇里我写过,agent 应用的瓶颈正在从模型能力转向单位任务成本和延迟,Neon 基本就是这个判断的又一次印证。同时它的对手也很清楚,昨天的 [GPT-6.2 Astra / Sol 发布](2026-11-17-openai-rolls-out-gpt-6-2-astra-for-professional-work-and-gpt-6-2-sol-for-everyda.md) 同样是"旗舰 + 日常款"的双档结构,三家都在把产品线切成不同的价格档。

先找瓶颈:模型层能力差距在收窄,真正卡住企业大规模部署的是"每完成一个任务要花多少钱、等多久"。那谁在解决这个瓶颈?受益的层次会是:第一层是推理算力,而且是能把单 token 成本压下去的那部分——Google 能在三倍速度下把成本压低 60%,很大程度依赖自家 TPU 的推理效率,这和之前 [TPU 8 系列](2026-11-09-google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-m.md) 的布局是一条线,Nvidia、Broadcom(为 Google 设计 TPU 的合作方)这一层仍是确定性受益方;第二层是模型路由和 agent 编排,当三四个档位的模型能力接近、价格不同,"在每一步选用哪个模型"本身就是省钱的手段,Antigravity 里的 Orchestrator 就是这个逻辑;第三层才是模型厂商自己,中端价格带的价格竞争会压缩它们的毛利,这一点对正在 IPO 的 Anthropic 尤其需要观察。这些主要挂在 AI板块。如果中端模型持续变快变便宜,agent 在终端设备和本地场景的可用性也会提高,但这篇没有涉及端侧部署,暂时不挂 edge AI板块。

现在还早,厂商自测和独立指数之间本来就有差距,1 到 4 分的指数差距也未必对应实际业务表现。值得关注的是接下来几周 OpenRouter 这类平台上的实际调用量份额,以及 Anthropic 和 OpenAI 会不会针对中端档位下调价格——如果出现降价,说明价格战真正开始了。
