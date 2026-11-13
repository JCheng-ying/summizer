# ChatGPT’s new Wallet lets AI agents shop and check out for you
https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/

这篇文章背后的命题是:AI Agent 什么时候才能从"帮你找答案"变成"替你花钱"。如果 Agent 能够被授权直接完成交易,那么消费级 AI 的商业模式就不再只是订阅费,而是开始切入电商和支付这条链上的佣金与流量分配——这是一个比聊天大得多的市场,但也是一个信任门槛和渠道阻力都高得多的市场。

文章指出,OpenAI 推出了 ChatGPT Wallet,让它的 Agent(OpenAI 把它们叫做 dots)帮用户决定买什么,并代为完成结账。首批只开放给少量美国 ChatGPT Pro 订阅用户,要求年满 18 岁、持有美国发行的 Visa、Mastercard 或 American Express 卡。流程上有三层设计:第一是用户可控,结账前用户可以核对商品、总价和要用的卡,再通过 Face ID 或指纹这类安全验证批准,系统会留下交易记录;第二是支付令牌化,Wallet 用一个替代卡号的支付令牌去扣款,所以真实卡信息既不会交给 Agent,也不会交给商家,商家只拿到履约需要的收货地址和联系方式;第三是保留传统卡组织的保障,用户依然能拿信用卡积分,也能对交易发起争议。文章还提到,OpenAI 计划之后让用户设定消费上限、按品类或时间段预先授权,让 Agent 在这些边界内更自主地下单,同时发布了一份 Commerce Partner Playbook,指导零售商如何支持 Agent 购物。

但文章也点出了两个现实阻力。第一是需求端的证据还不强:DoorDash 和 Uber 披露的 Agent 下单量都很低,反而是 Meta 的 Muse(用户已超过 1000 万)里 AI 辅助购物成了热门功能。第二是供给端的封锁:部分零售商在阻止 AI Agent 访问网站,最大的就是 Amazon,它希望用户转去用自家的 Alexa。

个人看法:我觉得 Agent 电商当下真正的瓶颈不在模型能力,而在两件事:一是"谁对这笔钱负责"的信任与合规问题,二是"商家愿不愿意让第三方 Agent 站在自己和顾客之间"的渠道问题。OpenAI 这次的设计基本都是在解决第一个瓶颈——生物识别确认、令牌化、保留卡组织的争议机制,本质上是把现有支付体系的风控层原封不动地借过来,而不是自己重建一套。从这个角度看,真正解决瓶颈的那一层其实是 Visa、Mastercard、American Express 这些卡组织和它们的令牌化服务,以及 Stripe、Adyen 这类支付处理商:无论最后是 ChatGPT、Meta Muse 还是 Alexa 赢下 Agent 购物入口,交易都要从它们的网络上走一遍,这是一个不用押注具体 Agent 平台的位置。第二个瓶颈则更难,Amazon 屏蔽外部 Agent、引导用户使用 Alexa 的做法说明,大平台不会轻易把用户关系让给 OpenAI,Agent 电商很可能会分裂成"各家平台自己的 Agent"格局,这对 OpenAI 的商业化是一个实在的限制。

这和之前写过的 [Meta 推出 Muse Ember 支撑低成本 AI Agent](2026-11-09-meta-introduces-muse-ember-to-power-cost-efficient-ai-agents.md) 可以放在一起看:两家都在把 Agent 往消费交易里推,而 Meta 的优势是本身就有社交电商的流量。对 AI 板块来说,这件事利好的逻辑是给消费级 AI 找到了订阅之外的变现路径,如果 Agent 购物规模化,推理调用量也会随之上升,间接利好算力层;但 [OpenAI 季度收入首次突破 100 亿美元](2026-11-11-openai-s-quarterly-revenue-reportedly-crosses-10b-for-the-first-time.md) 的增长目前主要还不来自这类场景。现在只开放给少量 Pro 用户,还远看不出效果,值得关注的是 OpenAI 什么时候开放消费上限式的预授权,以及有没有大型零售商在 Playbook 发布之后公开接入。
