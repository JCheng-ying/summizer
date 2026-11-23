# CrowdStrike to buy Zscaler in record-setting $43.9B cybersecurity deal
https://siliconangle.com/2026/11/23/crowdstrike-to-buy-zscaler-in-record-setting-43-9b-cybersecurity-deal/

这笔交易背后的命题是:在 AI agent 开始以机器速度发起和承受攻击的阶段,网络安全行业的核心资产正在从"单个最好的产品"变成"最完整的遥测数据 + 一个统一的控制平面"。如果这个判断成立,安全行业会像云计算一样走向少数几家平台型公司,而数据量本身就是护城河,因为它直接决定了安全 AI 模型的训练质量。

文章指出,CrowdStrike 宣布以约 439 亿美元全股票方式收购同为网络安全软件公司的 Zscaler,对价为每股 260.4 美元,较上周五(CrowdStrike 收购意向公开当天)收盘价溢价 34%,是有记录以来规模最大的网络安全收购,而且大幅领先。两家公司同时公布了季度业绩,都全面超出预期:CrowdStrike 调整后净利润 3.549 亿美元、营收 15.8 亿美元,并上调全年指引;Zscaler 调整后利润 2.084 亿美元、营收 9.493 亿美元。

文章把两家公司的产品拆成两层:第一层是 CrowdStrike 的 Falcon 平台,用轻量的"传感器"程序保护员工设备、云实例等终端资产;第二层是 Zscaler 的 Zero Trust Exchange,保护连接这些资产之间的网络连接,定位是 VPN 的替代品——它加密员工设备与业务应用之间的流量,需要时管理员可以解密检查威胁,并对敏感系统要求更严格的身份验证。两家在部分领域有重叠:都提供防御提示词注入等威胁的 AI 应用保护工具,也在安全浏览器上竞争。文章特别提到,Zscaler 有自动对应用发起模拟攻击以寻找弱点的工具,CrowdStrike 今年早些时候推出了 SafeMind,一组定制 AI 模型和相关资产,既能发现软件漏洞,也能自动生成检测规则和工作流。CrowdStrike 表示会用 Zscaler 收集的网络遥测数据扩充 SafeMind 的训练数据集,文章提到 Zscaler 在 2024 年披露其平台每天拦截超过 90 亿次威胁。

商业层面,文章指出 CrowdStrike 会把 Zscaler 的软件纳入 Flex(一份合同购买多种安全工具的模式),约 8,000 家 Zscaler 客户还没有使用 CrowdStrike 的产品。CrowdStrike 预计交易在其 2028 财年下半年完成,交割后对每股自由现金流"显著且立即增厚",并预计 18 到 24 个月内实现每年 5 亿美元的成本协同(主要来自数据中心、供应商和运营),30 个月内为年化收入贡献 10 亿美元的增量。CEO George Kurtz 的说法是要打造"网络安全的操作系统",一个部署 AI、控制 AI、让任何 agent 应用安全运行的统一控制平面。

个人看法:我认为这笔交易里最被低估的一句是"用 Zscaler 的网络遥测训练 SafeMind"。先找瓶颈:AI 驱动的攻击已经让漏洞从发现到被利用的时间压缩到极短,[Google 的 AI 框架把补丁直接变成漏洞利用](2026-11-16-google-says-an-ai-framework-turned-security-patches-into-exploits-with-no-human-.md)、[GPT-6 Astra 安全调优版本关闭 Linux 根权限漏洞](2026-11-13-openai-s-security-tuned-version-of-gpt-6-astra-closed-root-level-linux-holes-for.md) 这几篇都在说明攻防两端都在用模型。在这种环境里,防守方的瓶颈不是规则写得好不好,而是有没有足够完整的数据让模型看到攻击的全貌——终端只看到一半,网络只看到另一半。CrowdStrike 花 439 亿美元买的,本质上是另一半的训练数据和数据入口。这和 [Corma 融资训练安全专用基础模型那篇](2026-11-16-corma-raises-125m-to-train-cybersecurity-optimized-foundation-models.md) 是同一条路线的两种打法:初创公司从模型切入,巨头从数据切入。

对 AI板块 的受益层次:第一层是拥有最大遥测数据和统一控制平面的平台型安全公司,合并后的 CrowdStrike 和正在 [押注 Applied Compute 的 Palo Alto Networks](2026-11-18-palo-alto-networks-bets-4-5b-on-ai-startup-applied-compute-as-earnings-top-forec.md) 是这一层的两极;第二层是支撑这些"安全 AI"模型训练和实时推理的算力和数据中心,文章里 5 亿美元成本协同主要来自数据中心整合,说明两家公司的推理和数据处理负载本身已经很大,合并后还会继续扩张;第三层是被挤压的一层,独立的 SASE 厂商和单点产品公司会面对捆绑销售的压力。也要看到风险:全股票交易、交割要等到 2027 年下半年以后,两套产品的真正整合还没开始,而 CrowdStrike 在 2024 年的 Falcon 更新事故也说明,控制平面越集中,单点故障的代价越大。现在还早,值得跟踪的是 SafeMind 在接入网络遥测之后,检测效果是否能拿出可以对外验证的数据。
