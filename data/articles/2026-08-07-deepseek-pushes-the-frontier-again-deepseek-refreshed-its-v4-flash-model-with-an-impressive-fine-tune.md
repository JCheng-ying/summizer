# DeepSeek Pushes the Frontier Again: DeepSeek refreshed its V4 Flash model with an impressive fine-tune
https://www.deeplearning.ai/the-batch/deepseek-pushes-the-frontier-again-deepseek-refreshed-its-v4-flash-model-with-an-impressive-fine-tune/

这篇文章讨论的是大模型竞争里一个越来越清晰的趋势:决定胜负的不再只是"谁的旗舰模型最聪明",而是"谁能用更小的模型、更低的成本,做到接近旗舰的智能水平"。

文章指出,DeepSeek 发布了 DeepSeek-V4-Flash-0731,是 V4 系列里"轻量版"Flash 模型的正式版(取代 4 月的预览版)。有意思的是,架构和参数量完全没变(混合专家架构,总参数 2840 亿,每个 token 激活 130 亿),仅仅是重新做了一轮微调,就让这个"小模型"在独立测试里反超了自家参数量更大的旗舰 DeepSeek-V4-Pro。具体训练方法上,文章描述了一个两阶段流程:先针对数学、编程、Agent 任务等不同领域,分别训练出专精的"专家模型"(监督微调 + 强化学习),再用一种叫"on-policy distillation"的方法把十几个专家模型合并回一个模型——合并后的模型自己生成答案,再被训练朝着对应领域专家会给出的答案方向修正。性能上,DeepSeek-V4-Flash-0731 在 Artificial Analysis 的智能指数上拿到 50 分,和 GPT-5.6 Luna 只差一分,和 Gemini 3.6 Flash 打平,同时处在"智能-成本帕累托前沿"上(意味着没有任何被评测的模型能同时比它更聪明、单任务成本还更低)。价格上,每百万输入/缓存/输出 token 分别是 0.14/0.0028/0.28 美元,权重在 MIT 协议下可免费商用。

文章特别指出这次发布赶上了一个"降价扎堆"的月份:DeepSeek 发布前一天,OpenAI 把 GPT-5.6 Luna 价格砍了 80%,GPT-5.6 Terra 砍了 20%,理由是效率提升(包括用 GPT-5.6 Sol 优化了自家的生产推理代码);再往前一周,谷歌推出了主打速度和成本而非能力上限的 Gemini 3.6 Flash 和 Gemini 3.5 Flash-Lite,任务耗时缩短了大约一半;同一周,Thinking Machines(此前在 Import AI 那篇联署"踩刹车"声明的文章里已经在我们图谱出现过)也发布了小模型 Inkling Small,参数量不到旗舰 Inkling 的三分之一,智能指数却只差 1 分。

个人看法:这篇文章和 DeepSeek 这次更新最值得记的一点,其实不是"DeepSeek 又变强了"这个表面结论,而是文章里"我们在想"部分点出的市场结构变化——不是所有客户都需要"最大、能力上限最高"的模型,真正规模化的场景(分诊 bug 报告、核对发票、客服问答)要的是"足够聪明、够便宜、够快"的模型,这类需求现在有 Gemini Flash、Claude Sonnet、GPT-5.6 Luna、DeepSeek-V4-Flash 一大批同台竞争的选项。这意味着**AI 板块**里"小模型/推理成本优化"这条线,正在从旗舰模型的技术溢出品,变成一个独立的、竞争烈度不低于旗舰模型的战场——对最终用户是好事(成本持续下降),但对模型厂商而言,意味着"轻量级模型"这个产品线本身的护城河,可能比想象中要浅,因为几乎所有头部厂商都在同一时间段做同样的事,差异化窗口期很短。

个人看法:另一个值得关注的细节是,DeepSeek 强调 3-bit 量化版本能在 110GB 内存的机器上跑起来,这意味着对数据不能出内网的企业客户,DeepSeek-V4-Flash 是少数能绕开 API、直接本地部署又不掉太多智能水平的选项——这对**edge AI 板块**和企业私有化部署这条线也是一个值得关注的信号,如果这类"高智能、可本地部署、开源可商用"的模型继续增多,会在一定程度上分流原本只能靠云端 API 触达的客户群体,值得持续跟踪云厂商和开源模型厂商之间这条边界会不会进一步松动。
