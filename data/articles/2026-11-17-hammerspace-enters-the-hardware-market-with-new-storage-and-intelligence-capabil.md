# Hammerspace enters the hardware market with new storage and intelligence capabilities
https://siliconangle.com/2026/11/17/hammerspace-enters-the-hardware-market-with-new-storage-and-intelligence-capabilities/

这篇讲的是一家数据编排软件公司开始卖硬件,背后的更大命题是:AI 基础设施的瓶颈正在从"GPU 够不够"慢慢转向"数据能不能足够快、足够干净地喂给 GPU"。如果存储和数据治理变成 AI 训练和推理里的约束,那么原本被视为配角的存储层,就会像网络和电源一样,变成 AI 资本开支里单独值得看的一块。

文章指出,Hammerspace 原本做的是软件:用全局命名空间把分散在不同存储系统、数据中心和云上的文件统一起来,应用不用做大规模数据迁移就能找到并访问数据;今年 3 月它还推出了自动把企业数据送到 GPU 的 AI 数据平台,底层基于对 Linux 做增强的并行 NFS,不需要专有客户端。这次推出的 Hammerspace Data System 把数据发现、管理、编排和存储打包成一个产品,客户可以买整套配置好的系统,也可以继续只用软件。新东西拆开来看有三块:第一是 Open Flash Platform,一种以 DPU(数据处理单元)而不是传统存储服务器为核心的高密度闪存系统,把处理、网络和固态硬盘集成在紧凑硬件里,目标是降低功耗、散热和机柜空间,公司称每个机架单元吞吐达到 350GB/s,但更广泛的性能测试还在进行;第二是原有的 Tier 0,把 GPU 服务器本地的 NVMe 盘聚合成共享资源,用来存推理的 KV cache,让应用复用已经算过的上下文,不用反复重算;第三是数据智能模块,能编目分布式文件、索引元数据、扫描内容识别个人信息和受监管数据,用自然语言检索,再转成自动化策略,比如阻止含个人信息的文件进入训练管线。商业模式上,软件仍按管理的数据量计费,硬件单独报价、没有公开价目表,公司说不打算赚硬件差价,零部件经由供应商和分销伙伴流转。Hyperion Research 的分析师认为这不只是捆绑销售,但也提醒更有说服力的是真实用户负载下的性能、能效比和性价比对比。文章最后提到,Hammerspace 2025 年 4 月融资 1 亿美元,客户包括 Meta 和美国国防部。

个人看法:350GB/s 每机架单元是公司自己给的数字,而且测试还没做完,只能按未经验证处理;"软件公司做硬件"历史上成功率也不高。但我觉得这条新闻值得记的点在 Tier 0 和 KV cache。agent 和长上下文推理越来越多,KV cache 的体量会远超 GPU 显存本身能装下的范围,于是推理系统开始出现一个新的分层:HBM → 本地 NVMe → 共享闪存 → 对象存储,越往下越便宜也越慢。谁能把这条分层管好,谁就在解决"推理时上下文放在哪"这个具体瓶颈。这和今天同一批的 [Nvidia 在 SC26 强调"循环速度"而不是单次算力](2026-11-17-nvidia-at-sc26-agents-are-the-new-scientists-and-they-need-a-lab.md) 是同一个逻辑:当一次任务变成一个不断重复的循环,数据搬运、调度和网络的延迟就直接决定了 GPU 的利用率。

所以对 AI 板块,受益的层次会是:第一层是 NAND 闪存和企业级 SSD,KV cache 外溢到存储层意味着推理集群的闪存用量上升,三星、SK Hynix、美光、铠侠这些是最直接的供给侧;第二层是 DPU 和智能网卡,Hammerspace 的闪存方案恰好以 DPU 为核心,Nvidia BlueField、Marvell、AMD Pensando 这一类会受益;第三层才是存储和数据软件本身,Hammerspace 之外 VAST Data、Pure Storage、NetApp、WEKA 都在争这个位置,竞争很激烈,谁能赢还看不清。另外"降低功耗和散热"这一条对能源板块只能算很边际的联系,这里不硬挂。现在还在观望阶段,值得跟踪的是 Hammerspace 能不能拿出真实客户负载下 KV cache 复用带来的推理成本数据,以及大型 GPU 云是否开始把共享 KV cache 存储作为标配。
