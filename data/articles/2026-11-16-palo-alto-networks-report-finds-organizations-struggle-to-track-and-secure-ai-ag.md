# Palo Alto Networks report finds organizations struggle to track and secure AI agents in the cloud
https://siliconangle.com/2026/11/16/palo-alto-networks-report-finds-organizations-struggle-to-track-and-secure-ai-agents-in-the-cloud/

需要先说明:这是网络安全厂商 Palo Alto Networks 自己发布的调查报告,厂商有很直接的利益(结论天然指向"需要买更多统一的安全平台"),下面引用的比例都是问卷自报数据,未经独立验证。

这份报告背后的命题是:AI Agent 已经几乎普及到软件开发流水线里,但企业的安全和问责体系还停留在"每个操作背后都是一个人"的时代。当改代码、改配置、动生产环境的主体有一大部分变成了 Agent,出了事连"是谁干的"都说不清,这才是 Agent 规模化部署真正的摩擦点。

文章指出,报告基于 10 个国家 2800 名安全从业者的调查。第一是普及程度:99% 的受访者说在开发流水线里用 Agent 做自主或半自主操作,73% 允许 Agent 修改代码、流水线配置甚至生产环境,44% 的组织让 Agent 做安全测试。第二是变更量上升而检查跟不上:82% 说 AI 驱动的开发增加了进入云端的基础设施更新量,但在报告衡量的 8 项部署前安全检查里,组织平均执行不到 3 项;42% 用 AI 生成基础设施即代码模板,只有 34% 会在上线前扫描。结果是 90 天内平均 19% 的高危和严重应用安全问题进入了生产环境,修复上线平均要 18.4 天,最常见的阻碍是"业务要求快速发布"(39%)。第三是问责:五分之二的组织无法还原 Agent 做了什么,金融业这一比例是 46%;53% 的 Agent 活动记录在开发者本人的身份或个人访问令牌下,出事后得先分辨哪些是人做的、哪些是 Agent 做的。第四是处置速度:60% 的组织撤销非人类身份的权限仍需人工介入,轮换泄露的凭证、API key 平均要 2.5 天。

文章还提到,报告里的问卷把"前沿 AI 自主发现并利用漏洞"称为 "Mythos-grade" 威胁,指的是 Anthropic 的 Claude Mythos 模型;Palo Alto Networks 是 Anthropic Project Glasswing 的首批合作方之一,今年 4 月提前拿到了 Claude Mythos Preview 的使用权。98% 的受访者担心这类威胁,公用事业行业中有 79% 认为它在未来 12 到 18 个月会对关键基础设施构成重大或严重威胁,电信业是 48%。报告的论点是:面对机器速度的攻击者,18.4 天的修复周期意味着漏洞被发现后有 17 天以上的暴露窗口;只有 19% 的组织在代码、云、身份和运行时之间有统一的遥测和工作流。建议是给每个 Agent 独立身份和明确负责人、最小权限,并在建好回滚机制之后再自动化修复重复出现的问题。

个人看法:这份报告和三天前写的 [Onyx Security 给 Glean 加 Agent 治理](2026-11-13-exclusive-onyx-security-brings-ai-agent-governance-to-glean-s-enterprise-ai-plat.md)讲的是同一个瓶颈,只是这次给了一组量化数字——"53% 的 Agent 用开发者身份在操作"基本就是那篇里说的 Agent 没有"户口"的问题。同时它也和 [OpenAI 的安全版 GPT-6 Astra 修 Linux 漏洞](2026-11-13-openai-s-security-tuned-version-of-gpt-6-astra-closed-root-level-linux-holes-for.md)、[Anthropic 发布 Mythos 5.2](2026-11-09-anthropic-launches-fable-5-2-and-mythos-5-2-with-science-coding-upgrades.md)形成了一个对照:攻防两端都在用前沿模型提速,但企业内部修复和撤权的流程还是人工节奏。按"先找瓶颈"的思路,AI 板块里 Agent 落地现在卡住的不是模型能力,而是"可追溯、可撤权、可审计"这一层。受益的层次会是:第一层是身份与权限管理,也就是给非人类身份发证、轮换和自动撤销的那一层,Okta、CyberArk(已被 Palo Alto 收购)、Microsoft Entra 这一类;第二层是把代码、云、运行时遥测打通的云安全平台,Palo Alto 自己、CrowdStrike、Wiz 都在争这块,也是这份报告最想推销的部分;第三层是 Onyx 这样专门做 Agent 治理的创业公司。需要打个折扣的是,报告由卖方发布,"只有 19% 有统一遥测"这种数字天然有利于其平台叙事。

另外一个值得留意的细节是公用事业行业对前沿模型攻击的担忧最高(79%)。在 AI 数据中心大量接入电网的背景下,电网本身的网络安全会不会成为新的监管门槛,目前只是猜测,这里不挂能源板块。

现在还早,这类调查每年都会说"差距很大"。值得关注的具体信号是:会不会有大型云厂商或代码托管平台把"Agent 独立身份"做成默认设置,或者监管机构(尤其是金融业)开始要求可还原的 Agent 操作日志——那会是这个瓶颈从"厂商营销话题"变成真实采购需求的分界点。
