# Google Gemini 4 Carbon Tops Intelligence Index, Cybersecurity Benchmarks
https://www.deeplearning.ai/the-batch/gemini-leads-the-pack-again/

这篇文章真正值得看的不是"谁又拿了第一",而是前沿模型竞争的维度正在变化:当几家头部模型在分数和每 token 价格上越来越接近,决定成本的就变成了"完成同一件任务要花多少 token",也就是 token 效率。

文章指出,Google 发布的 Gemini 4 Carbon 在 Artificial Analysis 新版 Intelligence Index v5.0 上排名第一(59 分),小幅领先 Claude Opus 5.5 和 GPT-6 Astra;在 Vals AI 的 Vals Index v2.2 上排第二,仅次于开到最高推理档的 Claude Sonnet 5.5;在 Arena.ai 文本榜上以 1,528 Elo 排第一。它是一个多模态模型,输入支持文本、图像、语音和视频(最长 100 万 token),输出为文本,可调节推理强度。Google 称 Carbon 建立在 Gemini 4 Argon 之上,Argon 是一个用推理、解题和定理证明数据做强化学习训练的混合专家模型。和 Argon 一样,Carbon 先只开放给 Google 挑选的一小批网络安全公司,在三个网络安全基准(CWE-bench 71.0%、ExploitGym 54.8%、SEC-bench Pro 88.2%)上领先所有模型,不过这些分数是 Google 自报的。参数量、架构、训练数据和正式开放日期都没有公布。

文章认为几个细节值得注意。第一,在编程智能体指数上 Carbon 仍排第二,落后于 Claude Opus 5.5,但每个任务更便宜、更快。第二,Intelligence Index 刚刚改版,换了更难的测试,并把权重均分给知识工作、编程、科学和常识四类,新旧版本分数不能直接比较;改版后最强的开源权重模型 Kimi 3.1 Pro 与 Claude Opus 5.5 的差距从 3 分拉大到 12 分。第三,也是文章最核心的判断:优惠期结束后 Carbon 每 token 价格将和 Claude Opus 5.5 完全一样,但在该指数上完成任务少用 29% 的输出 token,每任务成本低 23%。当分数和单价趋同,token 效率就成了新的竞争点。另外,Carbon 距离 Argon 全面开放只隔了大约两周,而 Carbon 比 Argon 在该指数上高出 9 分。

个人看法:这和之前写过的 [Gemini 4 Argon](2026-11-01-google-s-first-gemini-4-model-argon-avoids-hallucinations-and-shines-at-knowledg.md) 是一条线,Google 在用"高频发布 + 安全行业先行"的节奏追赶。我更关心的是 token 效率这件事对产业链意味着什么。目前模型层的瓶颈已经不是"能不能做出来",而是价格战下的毛利,这一点和今天 [Ramp 数据显示 AI 支出停滞](2026-11-08-ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo.md) 是同一个问题:用量在涨,但每单位能力越来越便宜。从"先找瓶颈"的角度看,受益的层次会是:第一层仍然是算力基础设施,Google 自研 TPU 加上自有云,使它在 token 效率上的优势可以直接转成成本优势,这是其他只能租算力的模型公司做不到的;第二层是网络安全这个具体场景,前沿模型先给安全公司用,意味着 AI 在攻防两端都会加速,安全厂商既是客户也是被改写的对象;第三层才是模型公司本身,在分数趋同的情况下,单纯的模型能力很难再支撑溢价。所以这条新闻我会挂在 AI 板块上,但更偏利好"有自有算力的全栈公司",而不是泛泛的模型层。还要注意新版指数刚改版就出新模型,榜单本身的可比性在下降,自报的安全分数也需要第三方复核,现在只能把它当成方向性信号。值得跟踪的是 Carbon 正式开放后的实际定价和 Claude、GPT 的回应。
