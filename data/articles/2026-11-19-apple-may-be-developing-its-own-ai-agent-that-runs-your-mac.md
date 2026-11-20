# Apple may be developing its own AI agent that runs your Mac
https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/

这篇文章背后的命题是:桌面 Agent 的竞争里,掌握操作系统的平台方开始同时扮演两个角色——一边自己下场做 Agent,一边收紧第三方 Agent 对系统的控制权。如果这两件事同时成立,Mac 上的 Agent 入口就不再是一个开放的模型竞赛,而是一个由平台方定规则的市场。

文章指出,消息最早来自 Bloomberg,线索是 Apple 新发布的一则招聘:招一位高级工程经理,负责打造一个"能使用电脑的 AI agent"。招聘描述里的设想是,这个 Agent 像一个能干的人一样使用电脑,浏览网页、跨应用工作、执行命令、编写和调试代码、调用服务,并在每一步选择合适的工具;它要能在应用、浏览器、命令行、代码和 API 之间流畅切换,完成多步任务,而且"私密地"完成。文章提到,Anthropic、OpenAI 已经推出这类服务,Meta 最近也发布了 Muse agent 系列,Apple 在 John Ternus 时代想扩展 AI 产品线,跟进是合理的。

更值得注意的是另一半信息。文章指出,Bloomberg 同时报道,即将推出的 macOS 27.3 会弹出警告,劝阻用户给第三方 Agent 授予完全访问权限;Apple 10 月已向开发者发通知,称会引入额外控制,确保真正想给某个应用这种"非同寻常级别访问权"的用户,只能通过非常明确的操作才能授权。不过 Bloomberg 也说,Apple 虽然考虑最早在明年年底推出这项服务,自研 Agent 的进展仍处于早期阶段。

这正好接上今天 [Google 给 Gemini 加上 Mac computer use](2026-11-19-google-gives-gemini-the-ability-to-use-your-mac-for-you.md) 那篇。那篇里我把桌面 Agent 分成三条路径:云端虚拟机、本机 computer use、操作系统原生集成,并且判断 Google 在 Mac 上只能走第二条路,因为系统层在 Apple 手里。这篇几乎是同一天给了答案:Apple 打算走第三条路,同时让第二条路变得更难走。

个人看法:Apple 收紧第三方权限,有两种解读。第一种是安全,这和今天 [Meta Muse 串话泄露隐私](2026-11-19-meta-s-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report.md) 以及 [Microsoft Agent Framework 包被植入恶意代码](2026-11-19-wiz-ties-microsoft-agent-framework-package-compromise-to-release-pipeline-certif.md) 那两篇是同一个背景——Agent 权限越大,一次失误的代价越大,平台方加一道明确授权是说得通的。第二种是竞争,自己的 Agent 还在早期,先抬高第三方的使用摩擦,等于给自家产品留出时间窗口,这和当年 App Store 规则、Safari 默认浏览器之争的逻辑很像。我倾向于两者都有,而且后者如果过度,未来可能引来反垄断关注,但现在只是一则招聘和一个警告弹窗,下结论太早。

投资角度先找瓶颈:桌面 Agent 当下的瓶颈不是"能不能做",而是可靠性和授权——用户愿不愿意把本地文件、账户交给它。Apple 招聘描述里反复强调"私密地"完成,说明它想用隐私作为差异化,而隐私在 Apple 的体系里通常意味着尽量在设备端处理。所以受益的层次会是:第一层是 edge AI板块,如果 Apple 的 Agent 像它的其他 AI 功能一样尽量端侧运行,截屏理解、跨应用操作规划这些高频步骤会持续推高对 Apple M 系列芯片神经引擎、以及更大设备端内存的需求(Micron 这类 DRAM 厂商是间接受益者);第二层是 AI板块里的平台方,掌握系统 API 的 Apple、Microsoft 在 Agent 入口上有结构性优势,而依赖"看屏幕点按钮"的第三方 Agent(包括 Google、OpenAI、Anthropic 的桌面应用)在 Mac 上的使用摩擦会上升;第三层仍然是云端推理算力,即使 Apple 主打端侧,复杂多步任务大概率还是要回到云端模型,这部分需求不会消失。

不过目前这只是一则招聘加上一份 Bloomberg 报道,Apple 没有回应,上线时间最早也在明年年底。值得跟踪的信号是 macOS 27.3 的授权警告具体有多严格、会不会延伸到 iOS,以及 Apple 是否开放一套让应用主动暴露能力给 Agent 调用的系统接口——后者才是"操作系统原生集成"这条路线真正落地的标志。
