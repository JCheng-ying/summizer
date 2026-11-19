# Microsoft CEO Satya Nadella explains why he asked 60K employees to quit
https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/

这篇文章背后的命题是:AI 对劳动力的冲击,第一波可能不是"AI 直接替代某个岗位",而是"岗位的工作方式被改写,一部分人不愿意或来不及跟上"。如果连 Microsoft 这样手握 Copilot、Azure 和 OpenAI 关系的公司,都要靠给 6 万人发自愿离职补偿来完成内部转型,那么企业 AI 落地真正的瓶颈就不只是模型能力,而是组织重构的速度和成本。

文章指出,Nadella 在 DealBook 峰会上解释了 10 月向 6 万名员工提供买断(buyout)、鼓励自愿离职而不是再做一次大规模裁员的原因。他的说法是,这不是用 AI 取代员工,尤其不是取代软件工程师,而是把 Microsoft 重组成一家"每个人都用 AI 干活、工作重心变成管理 AI"的公司;买断是为了"让每个人都觉得自己在做选择时有主动权"。他用软件工程举例,行业认知从"AI 永远写不了软件",到"AI 什么软件都能写,还要工程师干什么",再到现在重新发现软件工程不但没死,反而会繁荣,只是团队的组织方式和工程师的工作内容有了一个"新的运行点"。文章提到他举的例子是 Microsoft 365 里的 AI Agent 产品 Cowork,团队只有 11 名开发者,他们"搭建一座造产品的软件工厂,而不是直接造产品"。Nadella 认为未来所有岗位的员工都会变成 Agent 的管理者,但 Microsoft 是一家 51 年的老公司,不是 AI 原生的,所以问题是"在职者能多快改造工作本身、工作流程和工作产出,以及与之配套的薪酬",而这"会比所有人预期的时间更长"。文章还引用他上周在 The Pragmatic Engineer 播客里的话:围绕奇点、AI 会拿走所有工作的说法,让人们产生了失去掌控命运的焦虑,因此必须真正去做结构调整、给人安排位置、给人机会。TechCrunch 的概括是,买断本身就是给员工的信息:要么跟上新的 AI-first 方案,要么去别处开始新生活。

需要说明的是,这是 CEO 在峰会和播客上的解释,文章没有给出接受买断的实际人数、成本或者对利润率的影响,"11 人团队做出 Cowork"也只是 Nadella 的举例,没有可独立核对的产出数据。Microsoft 本身也是 Agent 工具的卖方,"每个人都会变成 Agent 管理者"这个叙事和它的商业利益是一致的。

个人看法:这篇和今天同样来自 DealBook 峰会的 [Nadella 谈 Agent 重塑互联网经济](2026-11-18-satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web.md) 是一对:那篇讲的是 Agent 改写外部的商业模式,这篇讲的是 Agent 改写内部的组织结构。再往前看,[Ignite 2026 上 Copilot 被重塑为企业自主引擎](2026-11-17-at-ignite-2026-microsoft-reinvents-copilot-as-the-autonomous-engine-of-enterpris.md) 是 Microsoft 对客户的说法,而这次买断是它在自己身上做的同一件事——某种意义上,Microsoft 在拿自己当第一个大客户做样板。我之前在风格参考里写过一个担心:多家公司的报告都说 AI 在企业里替代人类生产还有很大不足,企业部署的动力不够,会冲击 AI 板块信心。Nadella 这次的说法其实部分承认了这一点——"比任何人预期的都要久",说明瓶颈不在模型,而在组织。

目前来看,企业用 AI 做组织转型大概有三种方式:1. 直接裁员,先压成本再说,短期利润率好看但留下的人焦虑更重;2. 自愿买断,也就是 Microsoft 这次的做法,成本更高,但把选择权交给员工,减少转型阻力;3. 不动编制、靠培训和工具渗透慢慢改,风险最低但速度最慢。Microsoft 选第二种,说明它判断阻力主要来自"人愿不愿意改变工作方式",而不是"有没有工具"。

按"先找瓶颈再找解决瓶颈的那一层"来看,这篇文章里的瓶颈是工作流改造:把原来由人直接产出的东西,改成由人指挥 Agent 产出。对 AI板块,受益的层次会是:第一层是 Agent 平台和开发工具,也就是 Microsoft 自己的 Copilot/GitHub 体系、以及 Anthropic、OpenAI 这些模型供应方——如果"11 人软件工厂"成为常态,单个工程师背后的模型调用量会远高于今天,这和之前 [Anthropic 与 Microsoft 再签 43 亿美元算力协议](2026-11-11-anthropic-signs-another-4-3bn-in-compute-agreements-with-microsoft.md) 的需求逻辑是一致的;第二层是 Agent 治理和监督层,员工变成"Agent 管理者",就需要权限控制、运行时监督和审计,这正是前几天写过的 PreTxt、Onyx 这类公司在做的事;第三层仍然是算力基础设施,人少了,但推理调用多了,资本开支从工资表转移到 GPU 和数据中心。需要警惕的是,"人员换算力"这个逻辑在财务上能不能成立,要看 Microsoft 后续财报里人员费用下降和 AI 资本开支上升的相对速度。

现在还只是 CEO 的解释,看不出买断的实际效果。值得跟踪的是 Microsoft 下一季财报里有没有披露接受买断的人数和一次性成本,以及其他大型软件公司会不会跟进类似的"自愿离职 + AI-first 重组"方案——如果跟进的公司多了,说明这是行业层面的组织转型,而不只是 Microsoft 自己的选择。
