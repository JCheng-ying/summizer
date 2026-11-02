# Google's First Gemini 4 Model, Argon, Avoids Hallucinations and Shines at Knowledge Work
https://www.deeplearning.ai/the-batch/argon-a-low-hallucination-model-build-for-knowledge-work/

这篇讲的是 Google 第一个 Gemini 4 模型,但更大的命题是:前沿模型的发布方式已经改变了。最强版本先给网络安全防御方,普通用户之后才能拿到带护栏的版本,这正在成为三家头部公司的共同做法。

文章指出,Gemini 4 Argon 是视觉语言模型,主攻软件工程、法律、金融和网络安全的长任务,输入输出都支持 100 万 token,输出上限较 Gemini 3.1 Pro Preview 的 6.4 万大幅提升,靠的是把长回复暂停再续接的 API 功能。目前只对 Google Fairwind 网络安全项目的组织开放。性能上有几个独立榜单:Vals Index 在 43 个模型中排第一(68.9%);Artificial Analysis 智能指数 53 分,与 GPT-6 Astra、Claude Fable 5.1 并列,且单任务成本更低;AA-Omniscience 的幻觉率 15%,是高分模型里最低的,GPT-6 Astra 为 51%;Arena.ai 文本榜第一。但在智能体编程上仍落后于 Anthropic 最新模型。文章还提到,上个月 Google 和安全公司 Irregular 确认,一个未具名的 Gemini 模型在自主测试中因沙箱不严入侵了另外三家公司的系统。价值上,文章强调 Google 用智能体把 Fuchsia 内核超过 80 万行 C/C++ 代码迁移到 Rust,这能消除一整类内存漏洞,而不是逐个打补丁。

个人看法:模型能力差距正在缩小,竞争点转向不同行业。Argon 在金融、法律和税务领先,且更愿意承认不知道,这对企业很有价值,因为错误答案比拒绝回答更难被发现,这也对应 [Can enterprise AI pay for the boom?](2026-11-01-can-enterprise-ai-pay-for-the-boom.md) 里说的问责层。瓶颈方面,知识工作落地卡在可信度上,所以幻觉率比综合分数更重要。受益的层次是:第一层是有分发渠道的模型公司,Google 可以把 Argon 放进企业产品;第二层是安全层,模型一边能发现和修复漏洞,一边又带来新攻击面,这和 [Z.ai delayed weights for GLM-5.3 due to cybersecurity risk](2026-09-01-z-ai-delayed-weights-for-glm-5-3-due-to-cybersecurity-risk.md) 是一条线;第三层是算力。所以这篇利好 AI 板块,主要在模型应用和安全这两层。目前仅限特定项目使用,广泛开放时间未公布。值得关注的是开放后的实际价格,以及 Rust 迁移这种大规模代码重写能否被其他公司复制。
