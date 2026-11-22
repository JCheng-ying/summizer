# Researchers at UCLA, Washington, and Northwestern Release MEMCON for Agents
https://www.deeplearning.ai/the-batch/adaptive-memory-management/

这篇研究讨论的是 Agent 长期执行任务时绕不开的一个问题:记忆不是存得越多越好,而是要知道什么时候该查、查什么、什么时候该忘。如果记忆管理本身可以从经验中学出来,而不是靠开发者手工调参数,那么 Agent 在长任务里的稳定性和 token 成本都会改善。

文章指出,很多 Agent 把过去的经验以文本形式存在外部记忆库里,但检索几条、什么时候删除这类设置通常是开发者手工定的。UCLA、华盛顿大学和西北大学的研究者提出 MEMCON(Memory as a Controlled Process),包在现有记忆后端外面,调用原有的存、取、删函数,并从经验中学习怎么用。它的核心洞察有三点:第一,任务早期记忆库里成功案例少,按相似度检索反而可能误导,不如检索"同类型任务是怎么处理的";第二,后期换个说法重新查询可能找到新东西;第三,记忆库变大后要删,因为记忆在争夺有限的检索位置。具体做法是一个小控制器维护一张"情境 × 记忆操作"的分数表,每次要取记忆前先提取一个紧凑的状态(目标类型、是否在重复动作、记忆库大致规模、是否有相似任务的成功记录),从搜索、改写查询再搜、调取相似任务的成功轨迹、合并重复、删除、跳过检索等操作里选分数最高的,同时适当探索少用的操作;任务结束后按结果和步数打分,越靠近结尾的决策调整幅度越大。实验用了 GPT-4.1-mini、Claude Sonnet-4、DeepSeek-V3.2 三个模型和六个基准:在 ALFWorld 上 MEMCON 成功率 67.9%,高于最强基线 G-Memory 的 59.7%,每个任务输入 token 从 45,000 降到 39,000,节省 13%;在 GAIA 上准确率 22.4%,略高于 G-Memory 的 21.2%。

这和 [MIT researchers build VISTA, an agent harness that keeps images in memory](2026-11-08-mit-researchers-build-vista-an-agent-harness-that-keeps-images-in-memory-for-fas.md) 是同一个方向——都是在模型外面加一层记忆管理,而不是重新训练模型。

个人看法:这和我之前写的 Stroop Test 那篇逻辑是连着的:Transformer 本身没有人类式的执行控制,所以行业在模型外面补 Memory、Planner、Supervisor 这些管理层。MEMCON 的有意思之处在于它用的是一个非常轻量的类似多臂老虎机/强化学习的分数表,而不是再训练一个大模型,这意味着成本很低、可以直接套在现有框架上。从数据看,ALFWorld 上提升明显,GAIA 上提升很小,说明在需要多步交互的环境里记忆管理更有价值,在单问题检索任务里作用有限。对 AI 板块来说,这类研究利好的是 Agent 基础设施层:第一层是 Memory OS 和 Agent 框架公司(Mem0、Letta、Zep、LangChain/LangGraph 等),它们可以把这种自适应策略产品化;第二层是推理算力,token 节省 13% 看起来是降低需求,但历史上效率提升往往带来更多 Agent 部署,总量反而上升。这是学术研究,还没有产品化,只能算一个方向性信号,值得关注的是主流 Agent 框架会不会把"学出来的记忆策略"作为标准功能加进去。
