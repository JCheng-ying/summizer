# Google releases Gemini 4 Hydrogen, a lower-cost model said to outscore Argon
https://siliconangle.com/2026/11/12/google-releases-gemini-4-hydrogen-a-lower-cost-model-said-to-outscore-argon/

一款更便宜的模型在独立排名上反超自家旗舰,说明的是前沿模型的竞争正在从"谁最聪明"转向"同样聪明谁更便宜、更快",这对推理算力的需求结构会有直接影响。

文章指出,Google 发布 Gemini 4 家族里的低成本模型 Hydrogen,在 Artificial Analysis 智能指数上默认 high 思考档位得分 51,超过旗舰 Argon 的 50;新增的 xhigh 档位可以把分数提到 54。发布方式也不同:Argon 先给 Google 的 Fairwind 计划(一组经过审核的网络安全防御方)用了近两周才开放给付费开发者,Hydrogen 跳过了这一步,今天起所有人都能用,包括免费版 Gemini 应用。与 9 月发布的 Gemini 3.8 Flash 相比,Hydrogen 默认设置下完成任务快 2.5 倍,在 Terminal-Bench 4.1 命令行测试上从 18.2% 提高到 57%。Google 同时在编程工具 Antigravity 里加入 Orchestrator,会在会话中自动在 Hydrogen 和 Gemini 4 Carbon 之间切换,在 Terminal-Bench 4.0 上接近 Carbon 的成功率,但平均少用 24% 的额度。定价方面,Hydrogen 每百万输入/输出 token 为 1.5/7.5 美元,覆盖完整的 100 万 token 上下文;Argon 在 11 月 30 日前为 2/10 美元,之后涨到 4/20 美元。文章还提到,Gemini 4 的三款模型在六周多一点的时间里全部发布。

这里有两个值得拆开的信号:第一是模型路由,Orchestrator 本质上是在一个 agent 会话里动态选择大小模型,把"用多少算力"变成按步骤决定;第二是安全发布流程被简化,低成本模型不再经过安全防御方的预先测试就直接全面开放。

个人看法:这和之前 [Gemini 4 Argon 发布](2026-11-01-google-s-first-gemini-4-model-argon-avoids-hallucinations-and-shines-at-knowledg.md)、[Gemini 4 Carbon 登顶智能指数](2026-11-08-google-gemini-4-carbon-tops-intelligence-index-cybersecurity-benchmarks.md)是连续的三步,Google 的节奏非常快。先找瓶颈:agent 应用的瓶颈正在从模型能力转向单位任务成本和延迟,一个 agent 任务会触发成百上千次推理调用。所以对 AI板块来说,受益的层次会是:第一层是推理算力,而且是更偏向低延迟、高吞吐的推理芯片——Google 自己的 TPU 是最直接的受益者,因为 Hydrogen 跑在自家硬件上;第二层是模型路由和 agent 编排软件,Orchestrator 说明"用对模型"本身就是产品;第三层是 agent 应用层,单位成本下降会直接扩大可用场景。模型越便宜,调用次数增长往往越快,所以总推理算力需求不一定下降。

现在还早,智能指数 1 分之差不代表实际任务表现。值得跟踪的是 Argon 在 11 月 30 日涨价后,开发者流量会不会大规模迁移到 Hydrogen。
