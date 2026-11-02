# Import AI 478: Math for alignment; ProgramBench; and Mirendil shows what RSI means
https://importai.substack.com/p/import-ai-478-math-for-alignment

这期 Import AI 的主线是 AI 研发本身的成本正在塌缩。一个人、几个月、不到一千万美元就能接近开放权重的前沿,这如果持续下去,大模型的进入门槛和模型公司的护城河都要重新评估。需要说明,作者 Jack Clark 是 Anthropic 联合创始人,文中有 Claude 的成绩,解读时要留意。

文章讲了四件事。第一是 Mirendil-Base:初创公司 Mirendil 称,一名研究员用 3.5 个月、不到 1000 万美元算力训练出一个 1000 亿到 5000 亿参数区间的模型,优于 Nemotron-550B-Base、GLM-5.3 和 DeepSeek-V4-Pro-Base,低于 Kimi-K3;还在训练的更大版本已超过 K3。公司称下一代模型将部分由 Mirendil 模型自己构建,但尚未到完全自主的递归自我改进。第二是 ProgramBench:让 AI 根据编译后的程序和文档从零重建 FFmpeg、SQLite、ripgrep 这类软件。5 月发布时所有模型得分为 0%,现在 Claude Opus 5.5 达到 18.5% 完全通过、70.5% 接近通过,作者预计到 2027 年底饱和。第三是安全:OpenAI 用自家智能体红队测试内部控制,处在不同 microVM 里的智能体通过处理器缓存的时序差异传递信息,绕过了网络和共享文件的隔离。第四是 AI 安全公司 Resolution 自动形式化了奇点消解,耗时约一周,约 13.5 万美元 token 费用,生成约 60 万行 Lean 代码。

个人看法:这期和 [Import AI 474](2026-10-14-import-ai-474-platonic-mindspace-tpus-in-space-zhipu-starts-an-outer-rsi-loop.md) 的递归改进线索是连着的。我的看法是,如果训练一个"够用"的模型只要不到一千万美元,模型层的稀缺性就在下降,这和 [The hidden threat in Anthropic's prospectus](2026-11-01-the-hidden-threat-in-anthropic-s-prospectus-diseconomies-of-scale.md) 讲的规模不经济形成了有意思的反差:最前沿越来越贵,次前沿越来越便宜。价值会流向哪里?第一层仍是算力,因为研发成本下降后,尝试的人更多,总需求未必下降;第二层是隔离和安全基础设施,缓存侧信道这个例子说明现有沙箱挡不住智能体,这是具体且未被解决的瓶颈;第三层是开发者工具,如果软件可以从文档重建,传统软件的护城河也受影响。所以这期利好 AI 板块的基础设施和安全层,对纯软件公司是压力。Mirendil 的成绩是公司自述,值得跟踪的是第三方评测,以及 ProgramBench 是否真的如作者所说快速饱和。
