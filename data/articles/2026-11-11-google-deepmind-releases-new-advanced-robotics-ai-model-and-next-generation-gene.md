# Google DeepMind releases new advanced robotics AI model and next-generation gene prediction model
https://siliconangle.com/2026/11/11/google-deepmind-releases-new-advanced-robotics-ai-model-and-next-generation-gene-prediction-model/

这篇文章里最值得关注的信号是：机器人基础模型正在从"实验室 demo"走进"工厂概念验证并给出成功率"的阶段。如果前沿大模型的推理能力可以较快地迁移到机器人的动作模型上，那么人形机器人落地的瓶颈就会从"模型够不够聪明"转向"硬件能不能便宜可靠地量产"。

文章指出，Google DeepMind 发布了 Gemini Robotics 2.5，这是其迄今能力最强的视觉-语言-动作（VLA）模型，用来给机器人提供 "AI 大脑"。DeepMind 表示，借助 9 月底推出的前沿大模型 Gemini 4 Argon 的能力，Robotics 2.5 能更广、更快地学习新技能并应用到真实场景中，已在 200 多种不同任务上测试。改进集中在三个方面：第一是灵巧度，机器人能用日常工具处理易碎、柔性物体；第二是可靠性，在 Mercedes-Benz 的真实场景概念验证中，打包汽车零部件的成功率达到 96%；第三是安全性，改进了物理层面的可操控性，并新增了一个测试越狱的基准。评测中，Robotics 2.5 按任务不同成功率在 30% 到 100% 之间，完成速度比上一版快 20% 到 30%。模型可以适配多种机器人，包括 Apptronik 的 Apollo 2 人形机器人和使用两指平行夹爪的 Franka Duo 平台。Apptronik CEO Jeff Cardenas 说，Apollo 2 配合 Gemini Robotics，在几周的后训练里模型表现显著提升，迁移到 Mercedes-Benz 产线时几乎没有性能下降。Gemini Robotics 2.5 今天开始通过 DeepMind 的机器人合作伙伴推出，包括 Agile Robots、Apptronik 和 Boston Dynamics。同一天 DeepMind 还发布了 AlphaGenome 2，可以预测 DNA 序列变异如何影响具体细胞类型和状态的基因活性，新增了 DNA 甲基化预测，并能在不重新训练的情况下适配新的单细胞数据，但它只用于指导研究，并未获批用于临床或诊断。

个人看法：这篇可以直接接上之前的 [Video Friday 里第一次见到 Gemini Robotics](2026-07-31-video-friday-meet-google-deepminds-gemini-robotics-2.md)、[Google 的机器人模型长出了腿](2026-08-14-googles-robotics-model-has-legs.md)，以及 [Gemini 4 Argon 的发布](2026-11-01-google-s-first-gemini-4-model-argon-avoids-hallucinations-and-shines-at-knowledg.md)。这次的逻辑和 style_reference 里讲 Transfer Learning 的那一篇完全一致：先用通用大模型学到世界知识和推理，再用少量后训练迁移到具体机器人和具体产线，Apptronik 说"几周后训练"就是这种范式的直接证据。但"30% 到 100%"这个区间也提醒我们，96% 是在一个具体的打包任务上，不同任务之间差距仍然非常大——这正是之前那篇讲的 Novelty Detection 问题：模型在见过的任务上很稳，在开放环境里还远没有达到工业级可靠性。

用"先找瓶颈"的方法看，机器人落地目前卡在三处：第一是泛化，也就是任务间的成功率差距；第二是数据与后训练成本；第三是硬件的成本和可靠性。Gemini Robotics 解决的是第一和第二个。所以受益的层次会是：第一层是拥有前沿大模型、能把推理能力迁移到 VLA 的公司，Alphabet 是最直接的；第二层是接入这套模型的硬件整机厂，Apptronik、Boston Dynamics、Agile Robots 等合作方可以少花自己的模型研发投入，更快进入工厂场景，汽车制造是第一个落地点；第三层是机器人上游的执行器、减速器、灵巧手和力觉传感器供应链，因为当"大脑"不再是瓶颈，硬件就成了新的瓶颈。同时训练和推理这些 VLA 模型仍然需要大量 GPU/TPU 算力。

这利好机器人板块，有具体客户场景和成功率数据支撑；也利好 AI 板块，因为它展示了前沿大模型向物理世界溢出的商业路径。但目前还是概念验证，不是规模部署。值得关注的是 Mercedes-Benz 是否会把这个 96% 的打包任务推进到正式产线采购，以及其他车厂会不会跟进。
