# China's LineShine retains supercomputing crown as both Top500 and Green500 lists remain largely unchanged
https://www.datacenterdynamics.com/en/news/chinas-lineshine-retains-supercomputing-crown-as-both-top500-and-green500-lists-remain-largely-unchanged/

Top500 榜单本身是一个偏学术的排名,但这一期透露的信号值得放在出口管制的语境下看:一台完全由中国自研芯片和网络设备组成的系统,已经连续两期排在第一;而同时,全球新上榜系统数量跌到了历史最低。前者说明管制没有阻止中国在传统 HPC 上做到顶尖,后者说明全球算力投资的重心正在从公共超算转向私有的 AI 集群。

文章指出,2026 年 11 月这一期 Top500 前十名没有任何变化,新上榜系统只有 27 台,是"有记录以来最低,而且低得多"。排名最高的新系统是韩国 KITSI 超算中心的 Hangang,排在第 12 位,使用 Nvidia Grace CPU 和 GH200 超级芯片(文章给出的数字是 342.6 exaflops,这与第 12 名的位置明显不符,很可能是单位或精度口径问题,这里不作采信)。Top500 官方解释称,新系统少并不代表性能停止提升,而是增长主要来自榜单头部系统的扩容和升级,而不是整机替换。

位居榜首的是深圳国家超算中心的 LineShine,HPL 性能 2.198 exaflops,在 2026 年 6 月从美国的 El Capitan 手中拿走第一。文章指出,它采用中国设计的芯片和网络设备,包括基于 Armv9 指令集、主频 1.55GHz 的 304 核 LX2 处理器,这款处理器看起来是与国家超算中心和华为联合设计的,共 40960 颗芯片、92 个机柜、13,789,440 个核心。前十名里美国有四台(El Capitan、Frontier、Aurora 和微软的 Eagle),此外还有德国 JUPITER Booster、意大利 Eni 的 HPC7 和 HPC6、日本富岳和瑞士 Alps。Green500 前十同样不变,但几乎被欧洲系统包揽,法国和德国各三台,英国和波兰各一台。

个人看法:这篇要分两层读。第一层是中国的路线。LineShine 的 2.2 exaflops 是 FP64 的 HPL 成绩,靠的是 1300 多万个 Arm CPU 核心堆出来的规模,而不是 GPU 加速器——这说明在双精度科学计算上,中国可以绕开 Nvidia 的 GPU 生态,用自研 CPU 加自研互联做到世界第一。但这和 AI 训练是两回事,AI 训练依赖低精度矩阵算力和 HBM 带宽,这正是 [禁运芯片仍出现在中国最强模型背后](2026-11-13-export-banned-nvidia-chips-are-behind-china-s-most-powerful-ai-models-uh-oh-jens.md) 那篇揭示的缺口,也是 [Nvidia 这几周的出口管制风波](2026-11-17-jensen-huang-plots-return-as-nvidia-ceo-as-doubt-raised-on-whether-alice-huang-w.md) 的核心。所以真正的瓶颈仍然在 AI 加速器和先进制程,而不在 HPC 系统集成能力。

第二层是榜单停滞本身。新系统数量创新低,我理解为公共科研超算正在被私有 AI 集群"挤出"——xAI、Meta、微软、OpenAI 们的十万卡集群大多不提交 Top500,资本和 GPU 都流向了那里。这和 [Nvidia 刚发布面向科学计算的 Rubin HPC GPU](2026-11-16-nvidia-unveils-rubin-hpc-gpu-for-agentic-ai-powered-science-and-engineering-work.md)、[DOE 征集低温与量子超算测试平台意见](2026-11-17-doe-seeks-input-on-cryogenic-and-quantum-supercomputing-testbeds.md) 放在一起看就很清楚:国家实验室的下一代系统会是 AI 加 HPC 加量子的混合架构,下一轮榜单更新大概率要等这批系统交付。

对板块来说,AI板块的确定性受益方仍然是算力基础设施,但要分清两件事:一是 Nvidia、AMD 这类加速器厂商,以及 HPE(El Capitan、Frontier、Aurora 的系统集成商)这类整机方,会在下一代国家级系统招标里受益;二是 Green500 被欧洲包揽,说明能效正在成为采购指标,AI 的约束正在从芯片转向电力和散热,液冷和电源管理这一层(Vertiv、Schneider)仍然是能源板块里和算力挂钩最紧的部分。量子计算板块这次挂得比较弱,只是通过 DOE 的混合超算路线间接相关,暂时不单独看。现在还早,值得关注的是明年 6 月那一期榜单:如果美国新一代系统没有夺回第一,出口管制的有效性讨论会再被拿出来。
