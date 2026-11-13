# ASIC ambition
https://www.datacenterdynamics.com/en/analysis/asic-custom-silicon-amazon-arm-meta/

这篇文章讨论的是 AI 芯片市场正在发生的一次结构性分化：当 AI 负载从训练转向推理，"通用 GPU 打天下"的格局会不会被大量为特定负载定制的芯片切开。如果这件事成立，算力这一层的确定性受益方就不再只有 Nvidia 一家，而是会扩展到所有能帮别人"造自己芯片"的环节。

文章开头引用了 Google AI 与基础设施副总裁 Amin Vahdat 在 2025 年 10 月 a16z Runtime 活动上的判断：某些计算在 TPU 上运行的每瓦效率是 CPU 的 10 到 100 倍，而像 agentic 负载这样的场景还会受益于更专门的架构。文章指出，不到一年这个判断就有了印证：2026 年 6 月到 8 月之间，OpenAI 发布了与 Broadcom 合作开发的"Jalapeño"智能处理器；Anthropic 确认正在组建自研芯片团队；有报道称 Google 在开发一款能更高效运行 Gemini 的新芯片；芯片初创公司 Etched 和 Olix 分别融资 7 亿美元和 3 亿美元，估值分别达到 210 亿美元和 33 亿美元。Futurum Group 旗下芯片测试机构 Signal65 的负责人 Ryan Shrout 的解释很直接：设计芯片的资本门槛一直很高，但现在这个领域"钱太多了"，几乎所有有好想法的人都会去追。

文章用 Amazon 作为超大规模云自研芯片的样本。2026 年 7 月 Amazon 披露其定制芯片业务年化收入超过 250 亿美元，这条线起源于 2015 年收购 Annapurna Labs，现在包括用于训练和推理的 Trainium、用于通用云计算和 agentic AI 的 Graviton，两者都基于 Nitro 系统做安全和网络。Andy Jassy 在 4 月说过，AWS 两个最大的客户问能不能买下今年所有可用的 Graviton 实例容量。Amazon 工程总监 Mark Carroll 给出的理由可以拆成几层：第一是成本，去掉不需要的功能后跨代实现约 40% 的性价比优势；第二是能效，相比上一代每瓦 token 输出提升到五倍；第三是上市速度和灵活性，可以针对客户在内存接口、内存使用和加速器互联上做优化；第四是全栈控制，从芯片、板卡、机箱、系统、固件驱动到上层软件都自己做，每一层的反馈都能回流到芯片设计。他还提到 Amazon 会和 Anthropic 等客户沟通其发展方向，针对性地设计芯片。

但文章同样花了很大篇幅讲门槛。第一是钱，引用英国政府科学技术委员会 2025 年报告，设计一颗先进芯片约需 5000 万到 1 亿美元，制造约 1 亿美元，建一座晶圆厂约 200 亿美元。第二是产能，TSMC 占全球先进制程产能约 92%，虽然在美国、德国、日本和台湾投入数千亿美元扩产，但大部分新产能要到这个十年末才能释放；Shrout 的说法是，造 1000 颗原型还可以想办法，但如果初创公司要量产 300 万颗，根本没有闲置的晶圆投片，Nvidia 和 AMD 也不会让出产能。第三是内存，全球内存短缺推高了价格，SK Hynix 和 Samsung 都警告紧张会持续到 2027 年以后；文章提到 Olix 声称用 SRAM 加光子架构绕开 HBM，从而避开这条供应链约束。第四是节奏，Nvidia 和 AMD 已经是一年一代，而 Vahdat 说即使最好的团队把专用架构从概念推到量产也要两年半。Shrout 最后的判断是，现在是"狂野西部"，没人真正知道 agentic AI 的推理和计算需求会是什么样，CPU 的复兴就是三年前没人预料到的例子；定制芯片会有一席之地，但通用计算不会从数据中心消失，Nvidia 不必太担心。（原文结尾处被截断，以上是能读到的全部内容。）

个人看法：这篇和之前写过的 [Google 扩展 TPU 家族推出 8tx 和 8i](2026-11-09-google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-m.md)、[英国推理芯片公司 Fractile 融资 7.2 亿美元](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md) 和 [Cerebras 因芯片收入和微软合作大涨](2026-11-12-surging-ai-chip-revenue-and-microsoft-deal-boost-cerebras-systems-stock-by-17.md) 是同一条线索：推理侧的定制芯片已经从概念进入资本密集阶段。按"先找瓶颈再找解决瓶颈的那一层"来看，这篇文章其实把瓶颈说得很清楚——不是芯片设计能力，而是先进制程产能、HBM 内存和时间。所以目前来看定制芯片有三种玩法：1. 超大规模云全栈自研（Amazon、Google），它们有自己的负载和客户来摊薄成本，是最稳的；2. 模型公司借助设计服务商定制（OpenAI 与 Broadcom、Anthropic 自建团队），本质是用芯片去压低自己的推理成本；3. 独立初创公司（Etched、Olix、Fractile），估值很高，但最容易卡在量产产能上。

受益的层次会是：第一层是先进制程代工，TSMC 无论谁的芯片胜出都要来这里投片，而且产能本身就是瓶颈，这是最确定的；第二层是定制芯片设计服务和互联，Broadcom、Marvell 这类替客户做 ASIC 的公司是"卖铲子"的位置，比押注某个具体芯片更稳；第三层是内存，SK Hynix、Samsung、Micron 在短缺持续的情况下仍然有定价权，而绕开 HBM 的架构（比如 Olix 的 SRAM 加光子）如果走通，会对这一层形成边际冲击，也和之前 [Staera 的芯粒光互联](2026-11-10-staera-launches-with-4-6m-to-develop-an-optical-interconnect-for-chiplets.md) 有一点呼应；第四层是能效带来的电力侧影响，每瓦 token 提升五倍意味着同样电力能支撑更多推理，这对能源板块不是利空，而是让数据中心电力约束下的有效算力继续扩张。这些都挂在 AI板块的基础设施层上。对 Nvidia 本身，我同意文章的判断，短期不会被替代，但长期推理侧的份额被切走一部分是大概率事件。

现在还看不出哪条定制路线会胜出，但值得关注的是 Etched、Olix 这类高估值初创公司能不能拿到真正的量产投片，以及 Amazon 定制芯片的年化收入下一次披露时增速如何——这比任何一款新芯片的发布会更能说明定制芯片是不是真的在吃掉 GPU 的份额。
