# Nvidia says its open-source AI strategy remains intact after Jensen Huang’s exit
https://techcrunch.com/2026/11/17/nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huangs-exit/

这篇文章是英伟达黄仁勋离职后第一次财报电话会上的一个侧面,它回答的问题是:当一家公司的某个战略高度依附于创始人个人时,创始人离开后这个战略会不会跟着变。对英伟达来说,开源模型战略不是一个边缘项目,它是"让全世界的每个国家、公司、行业都自己训练模型"这一叙事的核心,而这个叙事本身就是 GPU 需求的放大器。

文章指出,临时 CEO、同时也是 CFO 的 Colette Kress 在开场发言中确认,英伟达会继续致力于"培育活跃的开放模型生态,让每个国家、公司和行业都能构建自己的智能"。她给出的支撑数据是:OpenRouter 上的每周 token 量同比增长 35 倍,过去三个月增长 3.5 倍;英伟达自己的 Nemotron 开放权重模型系列(面向长时间运行的 agent 系统和推理负载,是黄仁勋在内部推动的)现在是 OpenRouter 上"使用最广的美国开放模型"。关于 9 月宣布以 129 亿美元收购的 Hugging Face——这是英伟达史上第二大收购,平台服务超过 1.18 亿开发者和 20 万家公司——Kress 表示双方会一起扩展平台,文章称到目前为止收购没有变化,但分析师问答环节并没有直接讨论这笔交易。文章也提到,Hugging Face CEO 曾把黄仁勋的离开称为"悲伤的一天",并表示会"比以往更努力地为开源 AI 而战"。

个人看法:这篇要和今天的 [董事会不打算让黄仁勋复职](2026-11-17-nvidia-says-it-doesn-t-plan-to-reappoint-jensen-huang-as-ceo.md) 放在一起看。董事会在人事上和黄仁勋切割得很干净,但在战略上 Kress 选择在开场发言里主动重申开源路线,我的理解是管理层想传递一个信号:人走了,但"卖铲子同时补贴挖矿的人"这套飞轮不变。英伟达做开源模型和收购 Hugging Face 的逻辑本质上是需求侧的:开放模型越多、越多主体想要自己的模型,训练和推理需求就越分散、越庞大,而这些需求最终都落回 GPU 上。

先找瓶颈。英伟达现在的瓶颈不在供给侧,也不在需求侧的总量,而在"信任"这一层——[SEC 调查](2026-11-17-sec-reportedly-investigating-nvidia-amid-huang-exit.md) 和出口管制合规问题都还没有落地。在这种情况下,Hugging Face 这笔 129 亿美元的交易反而是一个值得盯的变量:它没有在问答环节被讨论,说明分析师的注意力都在治理问题上,但它本身也可能面临反垄断审查,而在公司被多个部门调查的时候,大额收购的审批环境不会变得更宽松。我在 [9 月那篇 Import AI](2026-09-01-import-ai-471-why-hugging-face-worries-me-space-mining-five-eyes-on-ai.md) 的讨论里已经提到过 Hugging Face 作为开源基础设施的特殊地位,被单一硬件厂商收购本身就会引起开发者社区的担心。

对 AI板块 的影响:第一层仍然是算力,OpenRouter token 量同比 35 倍这个数字(虽然来自英伟达自己的引用,不是独立统计)说明推理需求在开放模型这一侧增长很快,这对 GPU 和推理云都是直接利好,不管英伟达 CEO 是谁;第二层是推理路由和推理服务平台,OpenRouter 这类聚合层和 Together AI、Fireworks 这类开放模型推理云会受益于开放模型使用量的扩散;第三层才是英伟达自身的"生态控制",Nemotron 加 Hugging Face 让它在模型分发层也有了位置,但这一层的风险正是治理和审批。现在只能观望,值得跟踪的信号是 Hugging Face 交易的监管审批进度,以及永久 CEO 人选是否继续公开支持开源路线。
