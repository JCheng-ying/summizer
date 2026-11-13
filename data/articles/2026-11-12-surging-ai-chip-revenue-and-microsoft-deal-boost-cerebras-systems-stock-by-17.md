# Surging AI chip revenue and Microsoft deal boost Cerebras Systems stock by 17%
https://siliconangle.com/2026/11/12/surging-ai-chip-revenue-and-microsoft-deal-boost-cerebras-systems-stock-by-17/

Cerebras 的这份财报回答的是一个越来越现实的问题:当 Nvidia GPU 交期长、价格高、而且公司本身陷入管理层动荡时,非 GPU 架构的 AI 芯片能不能真正接住溢出的需求。

文章指出,Cerebras 三季度核心调整后营收 2.309 亿美元,同比增长 70%,高于预期的 2.147 亿美元;调整后每股亏损 0.67 美元,但由于会计处理(扣除转手收入、给大客户的认股权证按非现金方式冲减收入)不能和指引直接对比。调整后经营利润率 -14%,明显好于三个月前 -24% 的指引。公司宣布了新客户微软,此前已与 AWS 和 Oracle 签约;CEO Andrew Feldman 说微软协议一个月前签署,预计 2027 财年一季度开始贡献收入。未完成订单从 8 月的 250 亿美元增至 260 亿美元,但其中很大一部分来自与 OpenAI 的协议。四季度指引营收 3.1–3.3 亿美元、核心毛利率 47%–49%,均高于市场预期,Feldman 还称到 2027 财年末收入将翻三倍。股价盘后上涨近 18%。

文章同时提醒了两个风险:第一,积压订单增量很小,市场担心这些新客户的单子规模都偏小;第二,公司正在评估融资方式来消化积压订单,而在 AI 基建资金越来越紧的环境下,融资并不容易。Feldman 自己把机会讲得很直白:GPU 交期长、成本高,正好给硬件销售创造了机会。

个人看法:先找瓶颈——当前推理端的瓶颈是 GPU 的交付周期和成本,而 Cerebras 这类晶圆级芯片在低延迟推理上有结构性优势,这是它能拿到微软、AWS、Oracle 的原因。之前写过 [Fractile 融资 7.2 亿美元做推理芯片](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md)、[Google 扩展 TPU 家族](2026-11-09-google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-m.md),再加上同一天 [Luminal 用编译器打 CUDA 护城河](2026-11-12-with-23m-in-funding-luminal-is-the-latest-startup-to-put-nvidia-s-cuda-moat-in-i.md),能看到"去 Nvidia 依赖"正在硬件和软件两个方向同时推进。对 AI板块来说,受益的层次会是:第一层是有现成客户的替代推理芯片(Cerebras、Google TPU、AWS Trainium);第二层是让模型能跨硬件运行的编译器和推理云;第三层是给这些芯片供货的先进制程和封装产能——替代芯片越多,台积电的确定性反而越高。但要注意,Cerebras 对 OpenAI 一个客户的集中度很高,这一点和 [Nvidia 管理层动荡](2026-11-12-nvidia-ceo-jensen-huang-resigns-following-affairs-scandal.md)带来的"客户集中度风险重估"是同一个问题。

现在还早。值得跟踪的是 2027 年一季度微软那部分收入的实际规模,以及 Cerebras 最终选择什么样的融资方式。
