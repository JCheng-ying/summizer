# Isomorphic Labs raises $5B as it looks to take drug candidates to clinical trials
https://techcrunch.com/2026/11/17/isomorphic-labs-raises-5b-as-it-looks-to-take-drug-candidates-to-clinical-trials/

这篇文章背后的命题是:AI for Science 是否能从"发论文、拿诺奖"走到"产出能进临床的药物"。在企业 AI 落地还在被质疑的阶段,一家 AI 药物发现公司半年内连续拿到 21 亿美元和 50 亿美元两轮融资,说明资本愿意为"AI 改变科研生产方式"这个故事支付极高的溢价——但这个故事真正的检验点是临床试验,而不是融资额。

文章指出,Isomorphic Labs 2021 年从 Google DeepMind 拆分出来,本轮 50 亿美元 C 轮由 Greenoaks 和 Sequoia Capital 联合领投,Andreessen Horowitz 作为新投资方加入,所有老股东都跟投,包括 Alphabet 旗下的 GV 和 CapitalG、Thrive Capital、MGX、Temasek 以及英国 Sovereign AI Fund。距离上一轮 5 月份的 21 亿美元 B 轮只隔了半年。公司没有披露估值,文章引用 Bloomberg 此前的报道称其寻求的估值是 500 亿美元。

在技术和业务上,文章提到 Isomorphic 的药物设计引擎建立在 DeepMind 的 AlphaFold 之上,由一组覆盖不同化学领域的模拟 AI 模型组成,公司称在肿瘤和免疫领域取得了"积极的临床前结果",并已与 Eli Lilly、Novartis、Johnson & Johnson 达成合作。新资金将用于继续开发引擎、拓展更多药物类型,并推动候选药物进入临床。文章还提到,这是 Demis Hassabis 卸任 DeepMind 负责人、转任 DeepMind 董事长并专注药物发现后的第一轮融资。

这里需要区分两件事:AlphaFold 解决的是"给定氨基酸序列,预测蛋白质三维结构",而药物设计还需要第二步——找到能和这个结构结合、又有成药性的分子,再经过第三步的动物实验和第四步的人体临床。AI 目前对前两步的加速是确定的,但药物研发最贵、最耗时、失败率最高的是临床阶段,AI 能把这一段压缩多少,目前还没有公开数据。

个人看法:这和风格参考里那篇 CIGaRS 的判断是一致的——即使企业端 AI 的生产力提升还没被证实,科研场景对算力的需求是独立且持续的。之前 [Import AI 475 里讨论的 AI 科学家和生物方向](2026-10-14-import-ai-475-swarm-scaling-google-deepmind-watermarks-biology-and-the-ai-scienc.md) 是研究层面的信号,这次 Isomorphic 的融资则是资本层面的确认。Hassabis 亲自离开 DeepMind 去做药,也说明 Alphabet 内部把 AI 药物发现看作和大模型同级别的方向。

按"先找瓶颈"的思路,AI 药物发现的瓶颈分三层:第一是数据,高质量的蛋白-配体结合实验数据远少于互联网文本;第二是算力,大规模分子模拟和生成模型训练需要大量 GPU;第三是临床验证,这是资金和时间的绝对大头。50 亿美元融资主要就是为了解决第三层。所以受益的层次会是:第一层是 AI 基础设施,Isomorphic 依托 Alphabet 生态,TPU 和 Google Cloud 大概率是主要算力来源,NVIDIA 在其他 AI 制药公司中同样受益;第二层是生成实验数据的实验室自动化和 CRO,比如 Thermo Fisher、Danaher 这类仪器厂商,以及承接临床的 IQVIA 等 CRO;第三层是合作药企,Eli Lilly、Novartis、J&J 获得的是低成本的候选药物管线期权。板块上,这篇利好 AI板块,而且是"AI for Science"这条支线——它不依赖企业办公场景的 AI 落地,而是靠科研和制药这种高价值、长周期的需求拉动算力。实验室自动化理论上也会利好机器人板块,但原文没有涉及,这里不硬挂。

500 亿美元估值下,市场已经在为"AI 设计的药成功上市"提前定价,而第一批候选药物连临床都还没进。现在还是观望阶段,值得跟踪的是 Isomorphic 第一个候选药物的 IND 申报时间和适应症,这会是 AI 制药从"概念"走向"管线"的第一个硬信号。
