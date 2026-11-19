# Google gives Gemini the ability to use your Mac for you
https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/

这篇文章背后的命题是:Agent 的竞争正在从"在浏览器里替你办事"延伸到"直接操作你的电脑"。一旦 AI 可以跨本地文件、原生应用和网页完成多步任务,操作系统桌面本身就变成了 Agent 的执行环境,谁能被用户允许接管这块屏幕,谁就掌握了下一层入口。

文章指出,Google 宣布在 macOS 版 Gemini 桌面应用中加入 computer use 能力,AI 可以替用户完成任务、操作 Mac 原生应用,并在后台浏览网页。用户下达指令后,可以在聊天窗口里的实时预览中看到 Agent 的操作过程,同时自己的屏幕和光标仍然空出来继续做别的事;和其他 computer use 产品一样,用户可以暂停、停止,并在动作执行前批准。Google 给出的适用场景偏向重复性的事务:填表、对一批文件反复执行同一操作、按特定规则整理文件夹、从文件或在线仪表盘里的信息生成幻灯片等。功能首先只在美国以英文提供,需要 Mac 版 Gemini 应用和 Google AI Plus、Pro 或 Ultra 订阅,Google 没有说明何时扩展到其他市场或平台。

文章也很直接地认为 Google 在这件事上来得偏晚:OpenAI、Anthropic 和 Meta 已经在各自的桌面应用中提供 Agent 功能有一段时间了。Google 本周才宣布更大范围推出 Gemini 的 Tasks 功能(帮用户登录网站、网购、预约),9 月发布的家庭助理型 Agent "CC" 也才刚开始让早期测试者试用。换句话说,这是 Google 在补齐 Agent 产品矩阵的一块:第一是云端隔离环境里执行的 Task;第二是面向家庭事务、跨邮件日历的 CC;第三才是这次直接落在用户本机上的 computer use。

这篇和昨天 [Gemini Task 模式升级](2026-11-18-google-upgrades-gemini-s-agentic-task-mode-with-new-model-e-commerce-features.md) 那篇可以对照着看。那篇里 Google 强调每个任务跑在 Agent Compute Engine 上专属于该用户的隔离虚拟机里,数据不出 Google 基础设施;而这次的 computer use 则是让 Agent 直接接触用户自己 Mac 上的本地文件和应用,信任边界从 Google 的云延伸到了用户的设备。这恰恰也是今天 [Meta Muse 串话泄露隐私](2026-11-19-meta-s-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report.md) 那篇暴露出来的问题——Agent 能接触的数据越多,一次隔离失误的代价就越大。文章提到的"执行前批准"机制,本质上是用人工确认来换取信任,在产品早期是必要的,但也会限制 Agent 真正无人值守地处理批量任务的效率。

个人看法:目前来看桌面 Agent 有三种实现路径:1. 云端虚拟机,在服务商的隔离环境里开一个浏览器或桌面替用户操作,安全边界清楚但碰不到用户本地文件;2. 本机 computer use,也就是这次 Gemini 的做法,Agent 通过截屏和模拟操作直接驱动用户电脑上的应用,覆盖面最广但权限和隐私风险最高;3. 操作系统原生集成,由 Apple、Microsoft 这样掌握系统层的公司把 Agent 能力做进系统 API,让应用主动暴露可调用的接口而不是靠"看屏幕点按钮"。Google 在 Mac 上只能走第二条路,因为 macOS 的系统层在 Apple 手里,这也说明桌面 Agent 这场竞争里,平台方的位置比模型方更有结构性优势。

投资角度先找瓶颈:这类 Agent 当下卡住的并不是模型能不能理解指令,而是两件事——第一是可靠性,长链路的多步操作中任何一步看错屏幕、点错按钮都会导致任务失败,这和之前那篇 Stroop Test 讨论的长任务目标保持问题是同一个根源;第二是信任与权限,用户和企业愿不愿意把本地文件和账户交给 Agent。受益的层次会是:第一层仍然是推理算力,computer use 每一步都要处理截屏这种多模态输入,单任务的 token 消耗远高于普通对话,订阅门槛(AI Plus/Pro/Ultra)本身就说明这是高成本功能,对 AI板块的算力基础设施(Google TPU、NVIDIA GPU、数据中心)是持续的需求支撑;第二层是 Agent 安全与治理,权限审批、操作审计、隔离执行这些能力会随着 Agent 接触本地数据而变得刚需,这和 [Pretxt 运行时监督层](2026-11-17-with-5m-in-funding-pretxt-launches-runtime-oversight-layer-to-supervise-ai-agent.md) 那篇是同一条线;第三层是 edge AI板块,文章没有说明 Gemini 的 Mac Agent 是在本地还是云端做推理,我推测目前主要仍依赖云端模型,但 Agent 在用户设备上执行动作这一趋势,会逐步推高对端侧算力(Apple M 系列芯片、Qualcomm Snapdragon X 这类 PC 芯片的 NPU)的需求,因为把截屏理解等高频、隐私敏感的步骤放到本地,既省云端成本也降低数据外泄风险。

但这件事目前还早:功能只开放给美国英文付费用户,Google 也没有给出任何使用量或成功率数据,而且和 OpenAI、Anthropic 相比只是追赶。值得关注的是 Google 后续会不会把 computer use 带到 Windows 或者 ChromeOS,以及是否开始在端侧运行部分模型——前者决定它在桌面入口争夺中的覆盖面,后者才是真正能挂上 edge AI板块的信号。
