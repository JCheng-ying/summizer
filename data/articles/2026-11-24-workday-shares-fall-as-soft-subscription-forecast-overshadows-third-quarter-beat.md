# Workday shares fall as soft subscription forecast overshadows third-quarter beat
https://siliconangle.com/2026/11/24/workday-shares-fall-as-soft-subscription-forecast-overshadows-third-quarter-beat/

这篇财报新闻背后更大的命题是:企业软件公司把 AI agent 讲成新的增长引擎,但资本市场看的是订阅收入增速有没有因此重新加速。如果 AI 产品的新增合同额在快速增长、整体订阅增速却在放缓,那就说明 agent 目前更多是在"守住存量客户",还没有变成足以抵消传统 SaaS 增长放缓的新收入曲线——这是整个应用层 AI 叙事当下最需要回答的问题。

文章指出,Workday 截至 10 月 31 日的第三财季调整后每股收益 2.82 美元,同比增长 22%,收入 27.05 亿美元,同比增长 11.2%,均高于分析师预期的 2.75 美元和 26.9 亿美元。订阅收入同比增长 12.8% 至 25.32 亿美元;未经调整的净利润为 2.37 亿美元,低于去年同期的 2.52 亿美元,其中包含 5100 万美元重组费用,对应公司 9 月底宣布的约 2.5% 裁员,主要集中在产品和技术团队。订阅收入总积压增长 6.1% 至 275.48 亿美元,其中 12 个月内的部分增长 12.3% 至 92.16 亿美元;自由现金流 6.91 亿美元,高于去年的 5.5 亿美元,季度内还花了 7.5 亿美元回购约 380 万股。

问题出在指引上。文章指出,Workday 预计第四财季订阅收入 26 亿美元,增长 10%,略低于分析师预期的 26.1 亿美元,而且相比第三季度的 12.8% 明显降速;尽管全年订阅收入指引上调到 99.58 亿美元(增长 13%,高于 8 月给出的 99.4 亿到 99.5 亿美元),全年调整后营业利润率也上调到 31.5%,高于分析师预期的 31.1%,股价盘后仍然下跌超过 7%。

AI 方面,文章提到了几件事。第一,Workday 在 10 月的 Rising 大会上把 Sana 作为平台的新首页体验,Sana 基于公司去年以约 11 亿美元收购的 Sana Labs 的技术,是一个把任务、决策、会议和 agent 活动整合在一起的 AI 界面;同时发布了在后台处理日常 HR、财务和 IT 流程的 Autopilot Agents。第二,Workday 宣布收购 agent 身份平台 ConductorOne(即 C1.ai),交易已于周一完成。第三,与 Anthropic 的合作将把 Claude 与 Sana AI agents 以及 Workday 的 HR 和财务数据结合起来。联合创始人兼 CEO Aneel Bhusri(今年 2 月在 Carl Eschenbach 卸任后回归)表示,第三季度 AI 产品带来了近 1.5 亿美元的新增 ACV,是一年前的三倍多,接下来的重点是让更多客户真正把 agent 跑在生产环境里;购买了至少一款 AI 产品的核心客户环比增长近 25%,超过 2200 家。CTO Gabe Monroy 此前在采访中的说法是,企业 agent 需要 Workday 这类系统的确定性规则来配合 AI 的概率性推理,客户不必为此切换入口,继续用 Gemini 等系统也可以。

个人看法:我觉得这份财报可以从三个数字的对比来看。第一是 AI 新增 ACV 近 1.5 亿美元、同比三倍;第二是季度订阅收入约 25 亿美元、增速从 12.8% 降到指引的 10%;第三是总积压只增长 6.1%,明显慢于 12 个月积压的 12.3%,说明长期合同的新增在放缓。把这三个放在一起,AI 产品确实在增长,但体量相对整体收入还很小,而且很可能有一部分是存量客户在续约时加购,而不是带来新的长期合同——这和我之前写的 [Ramp data shows AI spending stalling just as Anthropic nears its IPO](2026-11-08-ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo.md) 里企业 AI 支出放缓的担忧是一致的,也和今天的 [Anthropic shares fall below IPO price, a worrying sign for AI startups](2026-11-24-anthropic-shares-fall-below-ipo-price-a-worrying-sign-for-ai-startups.md) 放在同一个情绪背景下:市场开始要求 AI 叙事兑现成增速,而不只是新产品发布。

还有一个值得注意的结构性变化:Monroy 说客户不必登录 Workday,而是在 Gemini 等入口里调用它。这意味着 SaaS 公司的定位正在从"用户每天打开的界面"退到"agent 背后的确定性数据和规则层"。按"先找瓶颈"的思路,企业 agent 真正卡住的是两件事:一是 agent 能否安全地访问 HR、财务这类敏感数据,二是 agent 的动作能否被审计和授权——Workday 收购 ConductorOne 做 agent 身份,恰好就是在解决第一件事,这和今天另一篇 [Anthropic’s Siren tests whether Claude models will break out of an insecure sandbox](2026-11-24-anthropic-s-siren-tests-whether-claude-models-will-break-out-of-an-insecure-sand.md) 讲的 agent 越权问题是同一条线。

落到 AI 板块,受益的层次会是:第一层仍然是模型和推理算力,Workday 与 Anthropic 合作、同时兼容 Gemini 入口,说明不管哪个前端胜出,调用都会流向前沿模型和背后的 GPU/数据中心;第二层是 agent 身份、权限和治理,包括 Okta、CyberArk 以及被 Workday 收购的 ConductorOne 这类方向,因为数据越敏感,这一层越不可替代;第三层才是 Workday、Salesforce、ServiceNow 这些应用层 SaaS,它们手里有确定性数据,但面临的是被 agent 入口"降级为后端"的风险,定价能否从按席位转向按 agent 用量,是决定它们能否享受 AI 红利的关键。对应用层来说,这份财报偏中性略空:AI 在帮它们守住客户,但还没帮它们重新加速。

现在还早,1.5 亿美元的 AI ACV 还撑不起整体增速。值得跟踪的是下一两个季度 AI 新增 ACV 能否继续以三倍速度增长,以及 Workday 是否开始披露按 agent 计费的收入——如果订阅增速在 10% 附近企稳回升,才说明 agent 真正变成了新的收入曲线。
