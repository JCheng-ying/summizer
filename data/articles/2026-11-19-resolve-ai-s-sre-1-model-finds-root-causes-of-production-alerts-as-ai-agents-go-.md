# Resolve AI’s SRE-1 model finds root causes of production alerts as AI agents go on call
https://siliconangle.com/2026/11/19/resolve-ais-sre-1-model-finds-root-causes-of-production-alerts-as-ai-agents-go-on-call/

(说明:本文内容基于 Resolve AI 的产品发布,模型指标、客户效果数据均来自公司及其客户自述,未经独立验证。)

这篇文章背后的命题是:AI 已经大幅改变了软件怎么写,但几乎还没碰过软件怎么运行。如果 Agent 能在生产环境的告警链路上替代工程师值班,那么 AI 在软件工程里的渗透就从"写代码"延伸到了"运维",而运维的数据是私有的,这意味着垂直领域的专用模型有了一条通用大模型难以复制的护城河。

文章指出,Resolve AI 发布了 SRE-1,一个专门训练来定位生产告警根因的模型,同时推出 Primary On-call 服务,让它的 AI agent 排在人类工程师前面值班。公司的论点是,生产环境没有类似公开代码那样的训练语料,每家公司的事故数据都是私有的。SRE-1 是一个基于开放权重的 270 亿参数模型,由 16 名研究人员训练,最终一轮训练用时 7.4 天、最多 512 块 GPU,只用了强化学习;在相同事故上训练前后对比,单次调查的通过率从 6.9% 提升到 38.8%。训练使用的是 Snowflake 的 Cortex Training,一个定制开放权重模型的无服务器服务,Resolve AI 是它的第一个设计合作伙伴。

文章还给出了几组测试数据:在 49 个困难的真实生产案例上(每个跑五次),五次 SRE-1 调查的集成结果与测试中最强的前沿模型持平,成本更低;在 178 次生产告警调查上,完整系统解决的事故数约为通用编程 Agent 的两倍。Primary On-call 会跨遥测、基础设施、代码和运维知识调查每一条告警,根据结果关闭告警、在团队策略允许时直接缓解问题,或升级给人类,处理后还会对照生产基线持续监控直到恢复稳定;对还不放心的团队,提供只记录判断不执行的影子模式。公司称最多 80% 的告警可以不经升级处理,客户报告平均修复时间改善十倍、根因准确率最高 95%。Salesforce 是早期用户,其 CRM Analytics 团队在头几周的暗发布测试中,超过 70% 的告警被 Agent 关闭。Resolve AI 累计融资超过 1.9 亿美元,4 月由 DST Global 和 Salesforce Ventures 领投 4000 万美元 A 轮扩展,估值 15 亿美元,客户包括 Coinbase、DoorDash、Figma、MSCI、Nasdaq、SAP、Zscaler。

个人看法:这篇和今天 [Elastic 财报超预期却下跌](2026-11-19-despite-posting-a-solid-earnings-beat-elastic-sees-its-stock-slide-on-rough-guid.md) 正好构成一组对照。Elastic 卖的是可观测性和安全工具,AlertZero 也在讲安全 Agent;Resolve AI 做的是坐在这些工具上面、直接替代值班工程师的那一层。市场担心"AI 挑战软件商业模式",某种程度上担心的就是这种情况:价值从工具层向 Agent 层迁移。但我觉得也要看到反面,Resolve AI 的 Agent 需要跨遥测、日志、代码读取数据,可观测性平台反而是它的数据来源,两者短期更像上下游而不是替代。

技术上值得注意的是它的路线:不是直接调用最强的通用模型,而是用 270 亿参数的开放权重模型加私有事故数据做强化学习,再用五次集成去追平前沿模型。这和 [Meta 推出 Muse Ember 主打低成本 Agent](2026-11-09-meta-introduces-muse-ember-to-power-cost-efficient-ai-agents.md) 是同一个方向——Agent 在生产环境里要跑得起,成本比单次最强能力更重要。不过 38.8% 的单次通过率也说明,单次调查仍然大部分失败,所以才需要集成和影子模式兜底。

投资角度先找瓶颈:运维 Agent 的瓶颈有两个,第一是数据,事故数据私有、没有公开语料;第二是信任,让 Agent 直接改生产环境的风险很高。解决第一个瓶颈的是能把企业私有数据变成训练和推理燃料的层次,所以受益的层次会是:第一层仍然是 GPU 算力,512 块 GPU 训 7.4 天的规模虽然不大,但每个垂直领域都这样做一遍,加上每条告警的多轮调查推理,累积起来是持续的需求;第二层是企业数据平台和模型定制服务,Snowflake 的 Cortex Training 在这里不只是卖存储,而是在卖"在数据旁边训练模型"的能力,这是数据平台在 AI 周期里找到新收入的一个具体例子;第三层是 Agent 安全与治理,和 [Pretxt 运行时监督层](2026-11-17-with-5m-in-funding-pretxt-launches-runtime-oversight-layer-to-supervise-ai-agent.md) 那篇一样,让 Agent 坐在关键路径上需要审批、审计、回滚能力。这些都落在 AI板块,而且更偏基础设施和数据层,而不是通用应用层。

现在 Primary On-call 刚全面上线,数据全部来自公司自述。值得跟踪的是 Salesforce 的暗发布能否转为正式部署,以及 Snowflake 是否在财报里提到 Cortex Training 的客户数量——这会说明"在私有数据上训练垂直模型"是不是一个能规模化的模式。
