# Token sticker shock pushes enterprises from frontier labs toward open-weight AI factories
https://siliconangle.com/2026/11/17/gpus-alone-won-t-carry-enterprise-ai-pilots-production-dellatsc26/

先说明利益相关:这是 theCUBE 在 SC26 上的访谈,文末披露这一段由 Dell 赞助,受访者是 Dell AI 解决方案高级总监 Brad Maltz,所以文中的成本数字和合作伙伴数量都是厂商自述,未经独立验证,而且"企业转向开源权重模型自建"这个结论本身就符合 Dell 卖 AI 工厂的利益。

这篇文章背后的命题是:企业 AI 从试点走向生产时,决定成败的变量正在从"能不能买到 GPU"变成"token 账单、数据主权和模型选择"。如果企业因为 token 成本和数据合规转向自建、跑开源权重模型,那么 AI 的价值分配会从前沿实验室的 API 收入,部分转移到企业本地部署的硬件和集成层。

文章指出,很多企业仍停留在试点阶段,编程助手往往是最容易的切入点,员工已经用过 Anthropic 和 OpenAI 的工具,希望把这些经验用到业务场景上,但试点一旦扩大,账单就来了。Maltz 说,在前沿实验室和超大规模云厂商上的 token 支出比预期高,"我们没想到每人每月要花 1 万到 2 万美元"。文章认为成本只是触发因素之一,数据主权、知识产权泄露、安全和治理都必须在上线前解决,这推动许多企业转向可以微调并在本地运行的开源权重模型,包括 Nvidia 的 Nemotron 这类美国选项。Maltz 的判断是前沿实验室和开源权重模型都会长期存在,问题在于开源权重模型是否有足够的多样性覆盖企业用例。为此 Dell 推出了 AI Ecosystem Program 来验证 AI 工厂上的软件伙伴,据称还有约 60 家伙伴已申请或在评估中,每增加一家可以多解决 10 到 30 个客户问题;主权部署通常意味着断网的本地系统,把模型放在企业已经掌控的 GPU 和数据旁边。

个人看法:这是今天 Dell 在 SC26 上的第三篇访谈,和 [液冷软件定义存储](2026-11-17-dell-bets-liquid-cooled-software-defined-storage-can-keep-ai-factories-fed.md)、[agent 数据网关](2026-11-17-dell-puts-a-single-gateway-between-enterprise-ai-agents-and-the-data-they-crave.md) 一起看,Dell 在讲同一个故事:企业要把 AI 搬回自己机房。这篇的新信息只有一个,但很重要——"每人每月 1 万到 2 万美元"的 token 支出。如果这个数字有代表性,它和 [Ramp 数据显示 AI 支出停滞](2026-11-08-ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo.md) 可以互相解释:企业不是不想用,而是用量一上来就被账单吓住了。同时它也和 [Anthropic 招股书里的规模不经济](2026-11-01-the-hidden-threat-in-anthropic-s-prospectus-diseconomies-of-scale.md) 呼应,前沿实验室的高定价对客户来说就是迁移动机。

先找瓶颈。企业 AI 生产化卡在两个地方:第一是单位 token 成本,第二是数据不能出门。解决这两个瓶颈的路线目前有三种:1. 继续用前沿 API,等模型降价,[GPT-6.2 Astra](2026-11-17-openai-rolls-out-gpt-6-2-astra-for-professional-work-and-gpt-6-2-sol-for-everyda.md) 这类降本模型就是在走这条路;2. 本地部署开源权重模型,也就是这篇文章说的路线;3. 混合模式,敏感数据和高频任务放本地,复杂推理调前沿 API。我倾向于认为第三种会是大多数企业的最终形态,这也是 Maltz 自己说"两者都会长期存在"的意思。

对 AI板块 的影响,受益的层次会是:第一层仍然是 GPU,不管企业用前沿 API 还是本地开源模型,推理都要跑在英伟达的卡上,而且英伟达通过 Nemotron 同时站在了开源权重这一侧,这和 [英伟达开源战略不变](2026-11-17-nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huang-s-exit.md) 是一致的;第二层是企业级整机和私有化交付,Dell、HPE、Supermicro 和 Lenovo 都在这一层竞争,本地化趋势是它们相对超大规模云厂商的增量;第三层是开源模型生态和微调、推理优化工具链,包括 Meta、Mistral 这类开源权重提供方和 Hugging Face 这样的平台。利空的一面是前沿实验室的企业 API 收入可能面临价格压力。edge AI板块 我不单独挂,因为原文说的"本地部署"是企业机房而不是终端设备。

这类赞助访谈的结论天然偏向卖硬件的一方,现在还很难判断企业回流本地有多大规模。值得跟踪的是前沿实验室下一轮企业定价会不会大幅下调,以及 Dell 财报里企业(而非 neocloud)AI 服务器收入的增速,这两个信号会说明 token 账单到底是在推动迁移,还是只是在倒逼降价。
