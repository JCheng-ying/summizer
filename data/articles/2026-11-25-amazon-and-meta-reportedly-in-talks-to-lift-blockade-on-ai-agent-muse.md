# Amazon and Meta reportedly in talks to lift blockade on AI agent Muse
https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/

昨天写 [沃尔玛与 Meta 合作把黑五折扣接入 Muse](2026-11-24-walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse.md) 时,我把亚马逊归为 agent 商业里"零售商封闭"那一类。仅仅一天之后,就有报道说亚马逊可能在松动。这件事背后的命题是:当最大的电商平台也开始和第三方 agent 谈接入条件,争论的焦点就从"要不要让 agent 进来"变成了"agent 进来之后,搜索排序和广告收入归谁"。

文章援引 Fortune 的报道称,亚马逊和 Meta 已经就允许 Muse 直接接入亚马逊商店进行了多轮谈判。这和两个月前形成反差,当时 Muse 用户在亚马逊结账时只会收到报错。文章指出,谈判还卡在两个问题上:第一是搜索结果如何呈现,第二是广告如何处理。亚马逊最大的顾虑之一是 Muse 这类第三方购物 agent 会如何影响它的广告业务;CEO Andy Jassy 在 10 月还说过,通过外部购物 agent 下单的顾客很少。文章还提到另外两层考虑:亚马逊可能一直在等 Muse 更成熟,因为如果 Muse 下错单或者出了问题,最后要面对不满的顾客和卖家的是亚马逊;高管们也担心第三方购物 agent 会削弱亚马逊和消费者之间的直接关系。据报道,任何协议都需要两家 CEO 亲自批准。Meta 和亚马逊均未回应置评请求。

个人看法:这篇和昨天沃尔玛那篇放在一起看,能更清楚地看到 agent 商业的瓶颈在哪。技术上让 agent 下单早就不是问题,真正卡住的是利益分配——亚马逊的广告业务建立在"用户在亚马逊页面上浏览、点击赞助商品"之上,一旦由 agent 代替用户搜索和比价,赞助位就失去了眼球,所以"搜索结果怎么呈现、广告怎么处理"正是这场谈判的核心,也呼应了 [Nadella 说 agent 会重塑网络经济](2026-11-18-satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web.md) 的判断。另一层瓶颈是可靠性和责任,亚马逊担心"下错单的锅"最终落在自己身上,这和之前写过的 [Muse 混淆对话、暴露隐私的报道](2026-11-19-meta-s-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report.md)、[银行说用 agent 被盗要客户自担](2026-11-18-more-banks-say-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacke.md) 是同一个问题。

所以如果谈成,我判断合作形式更可能接近沃尔玛 Agent Gateway 那种"零售商控制商品、排序和交易,agent 只是前端"的模式,亚马逊会想办法把广告位以某种形式嵌进 agent 返回的结果里。投资角度落在 AI板块:第一层仍是推理算力,Meta 自己的 Muse 和背后的数据中心负载会随着可购物商户增加而增长;第二层是接入层,零售商网关、身份与支付授权、反欺诈和订单纠纷处理,这一层直接解决信任和责任瓶颈;第三层是"agent 时代的广告"这个新问题,谁能设计出在 agent 结果里仍然可计量、可竞价的广告形式,谁就能保住电商广告的利润池,这对亚马逊和 Meta 都是核心利益。

目前只是匿名消息源的报道,双方都没有确认,也需要两位 CEO 亲自拍板,很可能谈不成或者拖很久。值得跟踪的是,如果真的达成协议,公开出来的条款里广告和排序是怎么处理的,这会成为后面其他 agent(ChatGPT、Gemini)和亚马逊谈判时的模板。
