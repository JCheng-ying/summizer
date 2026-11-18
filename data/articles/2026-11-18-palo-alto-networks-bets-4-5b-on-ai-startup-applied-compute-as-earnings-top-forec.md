# Palo Alto Networks bets $4.5B on AI startup Applied Compute as earnings top forecasts
https://siliconangle.com/2026/11/18/palo-alto-networks-bets-4-5b-on-ai-startup-applied-compute-as-earnings-top-forecasts/

这篇文章背后的命题是:企业 AI 的终局会不会是"开源权重模型 + 自有数据 + 自己部署",如果是,那么谁来负责这些模型的训练、推理和安全。一家网络安全公司花 45 亿美元买一家模型后训练和推理平台,说明安全厂商判断,模型本身正在变成企业的一类新资产,而这类资产需要被保护。

文章指出,Palo Alto Networks 宣布以全股票方式、估值 45 亿美元收购 AI 模型训练与推理初创公司 Applied Compute,交易需监管批准,预计在 Palo Alto 的第三财季完成;完成后 Applied Compute 联合创始人兼 CEO Yash Patil 将出任 Palo Alto 联席首席 AI 官,研究团队也一起并入。Applied Compute 由前 OpenAI 研究员 Patil、Rhythm Garg 和 Linden Li 于 2025 年创立,提供开源权重模型的后训练和推理平台,包括自动扩缩容的推理引擎和名为 Shift-1 的模型路由器。本月早些时候它刚以 32.5 亿美元估值完成 3.5 亿美元融资,由 Elad Gil 领投,Nvidia、Shopify Ventures 和 HubSpot Ventures 参投,当时公司称年化经常性收入已超过 1 亿美元,知名客户包括 Microsoft 和 DoorDash,累计融资超过 5 亿美元。也就是说,Palo Alto 的收购价比几周前的融资估值溢价约四成。

Palo Alto 对这笔交易的表述是:企业 AI 会是混合式的,大量企业运行用自己数据调过的开源权重模型,而目前没有大型供应商能安全地交付这类模型;收购后企业可以在公有云或主权环境里训练和部署带安全能力的开源权重模型。CEO Nikesh Arora 的说法是,每家企业都会混用开源和闭源模型,每个模型都需要被保护。

同一天公布的第一财季(截至 10 月 31 日)业绩也明显好于预期:调整后每股收益 1.05 美元(去年同期 0.93 美元),收入 34.4 亿美元、同比增长 39%,分析师预期为 0.97 美元和 33.1 亿美元;下一代安全业务 ARR 增长 66% 至 97.3 亿美元,剩余履约义务增长 35% 至 210 亿美元;受 4.57 亿美元税收收益帮助,GAAP 净利润 4.82 亿美元。CFO Dipak Golechha 表示考虑到当前威胁环境和需求,公司"大幅上调"全年指引:全年收入预期从 141 亿到 142 亿美元上调至 145.2 亿到 145.7 亿美元,调整后每股收益 4.26 到 4.30 美元,高于 FactSet 统计的 4.18 美元。盘后股价涨超 8%,此前常规交易时段已涨近 10%。

个人看法:这篇和昨天写过的 [token 账单推动企业转向开源权重 AI 工厂](2026-11-17-token-sticker-shock-pushes-enterprises-from-frontier-labs-toward-open-weight-ai-.md) 是同一个判断,只是换了一个买单方。那篇里我说企业 AI 生产化卡在两个瓶颈:第一是单位 token 成本,第二是数据不能出门,并且倾向于认为"敏感数据和高频任务放本地、复杂推理调前沿 API"的混合模式会是多数企业的最终形态。Palo Alto 这笔收购的逻辑几乎就是这句话——Arora 说的"每家企业都会混用开源和闭源模型"。不同的是,Dell 想卖的是硬件,Palo Alto 想卖的是在这条链上加一层安全。[Noeri 融资那篇](2026-11-16-noeri-raises-110m-to-help-companies-build-living-ai-systems-that-self-improve-ov.md) 当时也提到 Applied Compute 是主张"多模型未来"的公司之一,现在这条路线拿到了一个大型安全厂商的价格确认。

我觉得这里还有一个更具体的瓶颈:安全行业过去保护的是网络、终端和身份,但 [Palo Alto 自己的报告显示企业难以追踪和保护 AI Agent](2026-11-16-palo-alto-networks-report-finds-organizations-struggle-to-track-and-secure-ai-ag.md),而模型被微调之后,训练数据泄露、权重被篡改、推理被投毒这些风险都发生在模型层,传统安全产品看不到。买一个后训练和推理平台,等于直接站到模型的生产线上,而不是在外围加一道防火墙。这和 [Corma 融资训练网络安全专用基础模型](2026-11-16-corma-raises-125m-to-train-cybersecurity-optimized-foundation-models.md) 的方向不同:Corma 是用模型做安全,Palo Alto 这次更像是给模型做安全。

对 AI板块 的影响,受益的层次会是:第一层仍然是 GPU,后训练和推理都要跑在 GPU 上,Nvidia 同时还是 Applied Compute 的投资方,这类退出对英伟达的 [初创投资组合](2026-11-17-nvidia-s-startup-stakes-ballooned-to-65b-but-huang-s-exit-puts-future-deals-in-d.md) 是正面的;第二层是开源权重模型的后训练、推理和路由工具链,这一层原本都是初创公司,现在开始被安全和基础设施大厂溢价收购,同类公司(包括 Thinking Machines 的微调服务)的估值参照会被抬高;第三层是安全厂商本身,Palo Alto、CrowdStrike、Zscaler 这一层的 AI 叙事从"用 AI 做安全"扩展到"为 AI 做安全",ARR 增速 66% 说明需求端至少目前是真实的。利空的一面是,如果"开源权重 + 自建"真的成为主流,前沿实验室的企业 API 收入会面临持续的价格压力。

这笔交易还要等监管批准,而且是全股票交易,Palo Alto 的股价本身就是对价的一部分。值得跟踪的是交易完成后 Palo Alto 是否把 Applied Compute 的平台打包进现有安全订阅,以及 Microsoft、DoorDash 这类客户会不会因为供应商变成安全厂商而继续留下,这会说明"模型安全"能否成为一个独立的收费层。
