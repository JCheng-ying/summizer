# Firmus looks to raise $3bn in private equity and secure prepayments - report
https://www.datacenterdynamics.com/en/news/firmus-looks-to-raise-3bn-in-private-equity-and-secure-prepayments-report/

这条新闻讲的是一家澳大利亚 neocloud 的融资,但它其实是这一周 neocloud 融资方式变化的第三个样本:当公开资本市场的窗口关上,算力供应商开始把融资压力转给最大的客户。如果这成为常态,AI 基础设施扩张的节奏就不再由 neocloud 自己决定,而是由 Nvidia、OpenAI、Meta 这几家买方愿意预付多少钱决定。

文章援引《澳大利亚金融评论报》(AFR)的报道指出,Firmus 在 IPO 失败之后(公司把原因归结为市场波动)转回私募市场,计划募集 30 亿美元股权,同时争取从最大的几家客户那里拿到预付款,客户名单包括 Nvidia、OpenAI 和 Meta。AFR 引述三位匿名知情人士的说法,预付款最多可以覆盖 Firmus 在建合同的 12.5%。截至 2026 年 9 月,Firmus 有约 916MW 的已签约容量,但实际上线运行的只有 46MW。Firmus 拒绝向 AFR 置评。公司上一轮私募融资是 20 亿美元,投后估值 105 亿美元。

文章把这件事放在更大的背景里:随着私募资本"看似无穷的井"开始干涸,neocloud 越来越依赖预付款。上周 CoreWeave 和 Nebius 都公布了季度财报,CoreWeave CEO Mike Intrator 提到了"资本市场近期的波动",并强调超过 75% 的已承诺资本支出对应投资级和企业客户,其余对应头部 AI 实验室和 AI 原生公司,这些设施可以为相关资本支出提供 70% 到 100% 的融资。Nebius 则更依赖预付款,称本季度签下的合同预付款可以覆盖 100% 的相关资本支出;CFO 的说法是,如果资本市场条件不好,就把更多产能分配给长期合同,如果能以有吸引力的条件融资,就会转向机会性地分配。

把这几家放在一起拆开看,neocloud 现在的融资结构可以分成三层:第一层是股权,Firmus 的 IPO 失败说明公开市场的股权窗口已经收窄,只能回到私募;第二层是以客户合同为抵押的债务,这一层的成本取决于客户信用,所以 CoreWeave 才会反复强调投资级客户占比;第三层是客户预付款,本质上是让客户提前垫付建设资金,对 neocloud 来说成本最低,但前提是客户足够需要这块算力。

个人看法:这篇正好接上之前写的 [CoreWeave 转向客户预付款和短期合同](2026-11-11-coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth.md) 和 [Nebius 400 亿美元资本开支计划](2026-11-12-nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending.md)。用"先找瓶颈"的方法看,Firmus 的瓶颈非常清楚:916MW 签约、46MW 上线,也就是约 95% 的合同容量还停留在纸面上,中间缺的是建设资金。而它能拿到的预付款最多只覆盖 12.5%,远低于 Nebius 声称的 100%,这说明预付款不是所有 neocloud 都能平等拿到的,议价权取决于客户有多需要你那块算力,而一家 IPO 刚失败的澳洲公司显然排不到最前面。

所以我对这篇的判断是分层的:对 AI 板块的算力基础设施这一层(Nvidia GPU、电力和数据中心建设)来说,需求端没有变,Nvidia 自己甚至出现在预付方名单里,说明它愿意掏钱来保证自己的 GPU 能被装进机房;但对 neocloud 这一层来说是利空信号,资金成本在上升、估值在被重新定价,规模小、客户集中度高的公司会先承压。这和之前 [Fermi 失去 TensorWave 租约](2026-11-13-fermi-does-600mw-power-deal-with-hyperscaler-but-tensorwave-lease-is-officially-.md) 的逻辑一致:产业链里谁手里有现金、谁就有议价权。现在还看不出这是短期的资本市场波动还是更长的收缩,值得跟踪的是 Firmus 这一轮最终的估值是否低于 105 亿美元,以及 Nvidia、OpenAI、Meta 有没有真的签下预付款。
