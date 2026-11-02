# Google’s first data center satellite is online and writing poetry
https://techcrunch.com/2026/10/30/googles-first-data-center-satellite-is-online-and-writing-poetry/

这篇的意义在于太空数据中心从 PPT 变成了在轨硬件。虽然规模极小,但它开始产生真实的工程数据,这比任何估算都更重要。

文章指出,Google Suncatcher 的原型卫星本月随 SpaceX 猎鹰 9 号发射,经过约三周调试后已经上线,搭载四颗 TPU,发电能力最高 1 千瓦。由于功耗限制,同一时间只能运行一颗 TPU,而且每次只能开约 20 分钟。卫星预装 Google DeepMind 的 Gemma 4,工程师发送的第一个提示是写一首关于太空的俳句。后续测试将考察芯片在热应力和太空辐射下的表现。辐射会造成"比特翻转",地面测试显示对推理影响较小,对训练影响更大。如果成功,2027 年会再发射两颗卫星,提高发电能力并验证星间光链路。文章指出,Suncatcher 的特点是卫星紧密编队、以高速链路支持相干分布式计算,而 SpaceX 的方案中卫星相距较远,Starcloud 和 Cowboy Space 则在单颗卫星上做推理。Alphabet 持有 SpaceX 的大量股份,两家的方案都依赖 Starship 完全快速复用;Suncatcher 研究者估算,SpaceX 需要飞 1800 次 Starship 才能实现类似之前火箭的成本下降。文章最后提到,这个项目能否持续,取决于 Alphabet 如何应对眼下 AI 带来的压力。

个人看法:这正好验证了 之前写 SpaceX 太空数据中心那篇里我说的:太空数据中心的限制不在 GPU,而在能源和散热。1 千瓦带不动四颗 TPU,只能轮流开 20 分钟,这就是最直观的证据。和 [Import AI 474](2026-10-14-import-ai-474-platonic-mindspace-tpus-in-space-zhipu-starts-an-outer-rsi-loop.md) 里的 TPU 上太空是同一条线。受益层次仍是之前的框架:第一层是发射,Starship 是最大瓶颈,1800 次这个数字说明降本还要很久;第二层是太阳能阵列和航天电源;第三层是散热和热控;第四层是星间光通信;第五层是抗辐射算力。这篇对太空经济板块是实质性利好,但主要是技术验证,对 AI 板块和 edge AI 板块也有一点利好,因为在轨推理本质上是一种极端的边缘计算。但还是很早,Alphabet 现金流转负后,这类登月项目的预算也值得留意。值得跟踪的是辐射测试的结果,以及 2027 年两颗卫星能否如期发射。
