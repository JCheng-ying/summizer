# Satya Nadella predicts AI agents will reshuffle the economics of the web
https://techcrunch.com/2026/11/18/satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web/

这篇文章背后的命题是:互联网的变现逻辑一直建立在"人眼"上——流量、曝光、广告位,如果越来越多的浏览、比价和下单由 AI Agent 代劳,那么谁付钱给谁、按什么计费,整套分配规则都要重写。这不是某一家公司的产品问题,而是互联网商业模式的一次换代,规模上可以类比当年从门户网站到搜索引擎的迁移。

文章指出,Microsoft CEO Satya Nadella 在纽约时报 Dealbook 峰会上提出,Agent 网络的兴起会改变哪些公司为流量和交易向别人付费,他拿从 Yahoo 这样的门户到 Google 这样的搜索引擎的转变做类比。他的原话大意是:现在为"人类网络"设计商业模式的聚合者会被"重新洗牌";如果过去是靠眼球卖广告,现在可能要下沉到按点击付费(CPC),甚至更偏交易型的收费;"如果你不接受 Agent,别人会接受"。讨论随后转到 Amazon 屏蔽 AI Agent 访问其零售网站、不让 Agent 浏览商品目录和代用户下单这件事上。Nadella 的看法是,试图保护既有商业模式的公司可能会输给更愿意拥抱 Agent 的对手,比如 Amazon 如果继续屏蔽,Shopify 这样的购物平台可能选择放行并因此获得优势。他还说其他品类也在发生同样的事,"如果你爱上了某种商业模式,就得开始手忙脚乱地调整"。

需要说明的是,这是一段峰会发言,不是数据或新闻事件,Shopify 那一段是 Nadella 举的假设性例子,文章没有说 Shopify 已经做了什么。Microsoft 本身也有立场:它卖 Copilot 和 Agent 平台,Agent 网络越开放,对它越有利。

个人看法:这和之前写过的 [ChatGPT Wallet 让 Agent 代用户下单](2026-11-13-chatgpt-s-new-wallet-lets-ai-agents-shop-and-check-out-for-you.md) 是同一个问题的两面。那篇里我提到 Agent 电商有两个瓶颈:第一是"谁对这笔钱负责"的信任和支付问题,第二是"商家愿不愿意让第三方 Agent 站在自己和顾客之间"的渠道问题,当时文中就提到 Amazon 在屏蔽外部 Agent、引导用户使用 Alexa。Nadella 这次讲的正是第二个瓶颈,而且他给出的判断很直接:渠道封锁守不住,因为总有竞争者愿意放行。我觉得这个判断方向上成立,但节奏上未必那么快——Amazon 的护城河是物流、Prime 会员和商品丰富度,而不是网页本身,Agent 绕开 Amazon 之后能不能找到同等质量的履约,是另一个问题。另外 [银行表示用 AI Agent 的客户被盗刷要自己负责](2026-11-18-more-banks-say-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacke.md) 那篇说明,第一个瓶颈(责任归属)也远没解决。

如果按 Nadella 的框架看,目前对 Agent 网络的应对大概有三种:1. 封锁,像 Amazon 这样保护自有入口,用自家 Agent(Alexa)替代第三方;2. 开放并改收费方式,从按曝光收广告费转向按交易或按点击收费,也就是 Nadella 说的"下沉到 CPC 或交易型";3. 自己成为 Agent 入口,也就是 Microsoft、OpenAI、Google、Meta 正在争的位置。

对 AI板块 的影响,先找瓶颈:Agent 网络当下卡住的不是模型能力,而是商家接入和交易结算。受益的层次会是:第一层是 Agent 入口方,Microsoft、OpenAI、Alphabet、Meta,谁拿到用户的"代理权",谁就拿到新的流量分配权;第二层是支付和结算层,Visa、Mastercard、Stripe、Adyen 这类公司不用押注哪家 Agent 胜出,只要交易发生就要过它们的网络;第三层是愿意开放接入的电商平台,Shopify 这类给中小商家提供基础设施的公司,有可能因为 Agent 流量获得相对增量;第四层仍然是算力,Agent 代替人去逐页浏览和比价,单次购物背后的推理调用量会远高于一次搜索。利空的一面是依赖展示广告和"人类流量"的聚合者,它们面临的是计费方式的重定价。

现在还只是 CEO 在峰会上的判断,没有数据支撑,看不出迁移的真实速度。值得跟踪的是 Amazon 会不会松动对外部 Agent 的屏蔽,以及有没有大型电商平台公开宣布对第三方 Agent 开放结账接口,这会是"重新洗牌"是否真正开始的第一个信号。
