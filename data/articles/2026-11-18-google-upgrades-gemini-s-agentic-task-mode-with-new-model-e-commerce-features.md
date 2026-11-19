# Google upgrades Gemini’s agentic Task mode with new model, e-commerce features
https://siliconangle.com/2026/11/18/google-upgrades-geminis-agentic-task-mode-with-new-model-e-commerce-features/

这篇文章背后的命题是:当 Agent 真正开始替用户执行多步任务、甚至花钱的时候,竞争的焦点会从"谁的模型最聪明"转向"谁能用最低的成本、在最可信的环境里把任务做完"。Google 这次的动作恰好同时押注了三件事——更便宜更快的模型、支付与电商的标准接口、以及把 Agent 关在用户专属的隔离环境里——然后直接把价格降到零。

文章指出,Gemini 应用现在分成两个模式:Chat 负责快速、相对简单的回答;Task 负责预约、比价这类复杂的多步任务,这次更新的重点就是 Task。Google 把 Task 切换到了最新的 Gemini 4 Hydrogen,它的能力略弱于最强的 Gemini 4 Carbon,但成本效率高得多,Google 称部分任务的处理速度是上一代入门级模型的 2.8 倍。文章提到,Hydrogen 缩短等待时间的一个办法是把通常串行执行的步骤并行化;用户可以在每一步之后给模型反馈,模型在执行网上购物这类敏感操作前也会主动征求用户指令。

支付和电商这一层,文章指出 Task 目前用 Google Wallet 处理交易,Google 正在和 American Express、Mastercard、Visa 合作接入支付令牌化——用一个占位的令牌代替真实卡号交给商家,降低数据泄露风险;同时还计划支持 Universal Commerce Protocol(UCP),让 Agent 更容易和网店交互、减少出错。安全和隐私这一层,Task 可以利用 Gmail 等 Google 服务里的数据做决策(比如参考过往购买记录给购物建议),而这些数据不必离开 Google 的基础设施;按 Gemini 应用负责人 Josh Woodward 的说法,每个任务都运行在 Google Cloud 的 Agent Compute Engine 上一台专属于该用户、不与其他用户共享的硬件隔离虚拟机里,并定期接受红队测试。最后,Google 把 Task 在美国、日本、韩国、加拿大、澳大利亚和印度免费开放,文章认为这可能迫使对类似功能收费的 Anthropic 和 OpenAI 重新考虑定价。

这篇和几篇旧文能串成一条线。[Gemini 4 Hydrogen 发布](2026-11-12-google-releases-gemini-4-hydrogen-a-lower-cost-model-said-to-outscore-argon.md) 那篇讲的是低成本模型本身,这篇说明了它最先被用在哪里——高频、长链路、需要反复调用模型的 Agent 任务,正是推理成本最敏感的场景。支付令牌化的思路和 [ChatGPT Wallet](2026-11-13-chatgpt-s-new-wallet-lets-ai-agents-shop-and-check-out-for-you.md) 几乎一样,都是不让 Agent 和商家接触真实卡号;而今天 [多家银行宣布客户使用 AI Agent 后果自负](2026-11-18-more-banks-say-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacke.md) 那篇则说明,走卡组织令牌化这条受控通道,恰好是绕开银行责任条款阻力的路径。

个人看法:消费级 Agent 的竞争目前来看有三个维度:1. 单位任务成本,谁能把一次多步任务的推理成本压到足够低,谁就能免费送;2. 交易通道,谁能接上卡组织令牌和商家协议,谁的 Agent 才能真正完成"买"这个动作;3. 数据和信任,谁本来就握有用户的邮件、日历、购买记录,并能证明数据不出自己的基础设施。Google 在三个维度上同时有存量优势,所以它敢把 Task 免费——这本质上是用搜索和云的现金流补贴 Agent 入口,和 [Nadella 判断 Agent 会重排互联网变现逻辑](2026-11-18-satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web.md) 那篇是同一场入口争夺。

先找瓶颈:Agent 购物现在卡在两处,一是长链路任务的推理成本,二是交易的授权与责任。按这个逻辑,受益的层次会是:第一层是推理算力,免费策略意味着调用量会被放大,而 Google 用的是自研 TPU,这一层的受益更多落在 Alphabet 自己和它的芯片设计/代工伙伴(Broadcom、TSMC)上,而不是通用 GPU;第二层是支付令牌化网络,Visa、Mastercard、American Express 在 OpenAI 和 Google 两边都被选中,成为"不管谁的 Agent 胜出都要经过的收费站";第三层是隔离执行环境,也就是给每个 Agent 任务分配独立虚拟机的云基础设施,这会推高单用户的计算和内存占用。这条我挂 AI 板块:对拥有入口和自研芯片的平台型公司偏利好,对靠消费订阅收费的独立模型公司则是价格压力。

现在还早,Agent 下单的真实需求此前在 DoorDash、Uber 的数据里都还很弱。值得关注的是 Task 免费之后 Google 会不会披露任务量或交易量,以及 Anthropic、OpenAI 有没有跟进降价——那会是消费级 Agent 进入价格战的信号。
