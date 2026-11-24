# Walmart teams up with Meta to bring Black Friday deals to AI agent Muse
https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/

这条新闻背后的命题是:当购物入口开始从网页和 App 迁移到 AI agent,零售商面临一个选择题——把第三方 agent 挡在门外以保住自己的流量和数据,还是主动开放接口、让自己成为所有 agent 都能调用的"货架"。沃尔玛和亚马逊恰好选了相反的两条路,这会决定未来 agent 商业的流量分配方式。

文章指出,沃尔玛与 Meta 合作,让顾客可以通过 Meta 的 AI agent Muse 购买沃尔玛的黑色星期五折扣商品。流程是用户在 Muse 应用里登录沃尔玛账户,然后让 Muse 去找商品、比价、追踪折扣;Muse 把请求发给沃尔玛,由沃尔玛返回相关商品并帮助组建购物车。文章特别对比了两家零售巨头的态度:亚马逊已经采取措施阻止第三方 AI agent 替顾客下单,而沃尔玛在主动拥抱这件事。

在隐私上,文章提到沃尔玛称 Muse 拿不到顾客的沃尔玛购物历史和其他个人信息;用户可以设置消费上限、要求下单前审批、复查 agent 下的订单,也可以随时删除 agent 的配置。整个体验由沃尔玛 10 月上线的 Agent Gateway 支撑,这是一套让外部 AI 助手直接接入沃尔玛在线商店的系统,沃尔玛计划把它开放给更多开发者和 AI 平台,也就是说 Muse 未来只会是能在沃尔玛购物的若干个 agent 之一。文章还提到 Instacart 也已经和 Muse 合作,沃尔玛自己的购物助手 Sparky 也在增加功能,比如把手写购物清单转成购物车、用照片和语音找商品、在门店地图上标出货架位置,以及让货架价签亮起来的"Flash Price Tag"按钮。

个人看法:把这篇和 [ChatGPT 钱包让 agent 代为结账](2026-11-13-chatgpt-s-new-wallet-lets-ai-agents-shop-and-check-out-for-you.md)、[Gemini 加入电商功能](2026-11-18-google-upgrades-gemini-s-agentic-task-mode-with-new-model-e-commerce-features.md)、[Nadella 说 agent 会重塑网络经济](2026-11-18-satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web.md) 放在一起,目前 agent 商业大致有三种模式:1. 平台自建支付和结账(OpenAI 钱包),agent 方掌握交易;2. 零售商开放网关(沃尔玛 Agent Gateway),零售商掌握商品、库存和交易,agent 只是一个前端;3. 零售商封闭(亚马逊),坚持流量和数据留在自己的生态里。沃尔玛的做法本质上是在用"接口标准"换"渠道数量",它不在乎是谁的 agent,只要最后在沃尔玛下单。

先找瓶颈:agent 购物今天卡住的不是技术能不能下单,而是信任——用户敢不敢让 agent 花钱。同一天的 [ShellBench 那篇](2026-11-24-even-the-best-ai-agents-struggle-with-everyday-life.md) 里,agent 有 40.3% 的情况建议了重复或错误的发票付款,Muse Wonder 系列在不同 harness 下的成功率只有四五成,再加上 [Muse 混淆对话暴露隐私的报道](2026-11-19-meta-s-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report.md) 和 [银行表示用 agent 的客户被盗要自己负责](2026-11-18-more-banks-say-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacke.md),这些都说明"消费上限、下单前审批、订单复查"这些护栏才是让交易真正发生的前提。所以沃尔玛把这些控制权放在自己一侧,是很务实的设计。

投资角度落在 AI板块:第一层是推理算力,每一次比价、搜索和建购物车都是多轮工具调用,黑五这种高峰会直接体现成推理负载;第二层是 agent 和商户之间的"接入层",包括零售商网关、支付和身份验证、反欺诈,这一层解决的正是信任瓶颈,比单纯做 agent 前端更有确定性;第三层才是 Muse 这类前端 agent,它们要靠接入的商户数量和可靠性竞争,目前看可靠性还没过关。对亚马逊来说,封闭策略短期保护了广告和数据,但如果 agent 购物真的成为主流入口,这个选择的代价会逐渐显现。现在还早,值得关注的是黑五之后沃尔玛会不会披露通过 Agent Gateway 成交的订单量,以及 Agent Gateway 下一批接入的是哪些 AI 平台。
