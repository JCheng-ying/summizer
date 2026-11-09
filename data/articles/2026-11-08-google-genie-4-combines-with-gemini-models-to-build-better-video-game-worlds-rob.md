# Google Genie 4 Combines With Gemini Models to Build Better Video Game Worlds, Robotics Training
https://www.deeplearning.ai/the-batch/world-models-become-robot-playgrounds/

这篇文章讨论的是机器人训练里一个越来越热的方向:用世界模型生成无限的虚拟练习场,让机器人在里面学。如果这条路走通,机器人数据瓶颈会从"真机采集"转移到"模拟器的物理真实度"上。

文章指出,Google 于 10 月 27 日发布 Genie 4,以研究预览形式开放给少量测试者。Genie 4 生成可交互的世界,用户可以用键盘鼠标在其中移动,并在中途用文字修改场景;新版本还能为生成的世界实时配音。核心变化是 Gemini 模型参与了"导演"工作:第一,Gemini 3.8 Flash 把用户目标拆成步骤,并逐帧检查每一步是否完成,用户插入修改时会调整计划;第二,视频生成模型 Gemini Omni 帮助渲染更真实的画面;第三,在机器人演示中,推理模型 Gemini 4 Argon 把任务拆成文本步骤交给 Genie 4,渲染出 Apptronik 的 Apollo 人形机器人和人下跳棋的模拟,但 Google 没有说明闭环里有没有机器人控制系统。

文章对结果相当保守。Google 只给了精选演示,没有定量评估。模拟最长可以跑两分钟,约是 Genie 3 的两倍,但 DeepMind 工程师承认跑满两分钟并不保证全程一致。演示里甚至有物理错误:一个大理石半身像砸在西瓜上,本应翻倒却稳稳落回底座。文章还梳理了竞争格局:Runway 的 GWM Worlds 2 同样实时生成视频,World Labs 的 Marble 和腾讯开源的 HY-World 2.0 则生成持久的 3D 场景;AMD 9 月同意以约 82 亿美元收购 World Labs,Rivian 收购了世界模型初创公司 Third Dimension,亚马逊据报在洽谈收购 Decart。文章认为 Google 目前最有说服力的证据其实来自另一条路线:Gemini 4 Argon 根据照片和视频编写 MuJoCo 物理仿真,单张桌面照片生成 4,500 多个练习片段,用它们微调机器人控制模型后,真实世界成功率从 56% 提升到 75%。Google 把这种结合代码推理和像素生成的方法称为混合世界模型。文章最后提了一个尖锐的问题:Gemini 导演会检查每一步是否成功,这可能让生成的世界不自觉地向预期结果漂移,那么在 Genie 4 里计划能失败吗?

个人看法:这个问题问得非常到位,和之前写的 RoboReward 那篇的逻辑完全一致:机器人学习真正需要的是失败样本,而通用生成模型天生偏向"成功长什么样"。一个会把半身像"摆正"的模拟器,对机器人训练反而有害。所以目前来看世界模型做机器人训练有三种方式:1. 纯像素生成(Genie、Runway),画面真实但因果不可靠;2. 物理引擎 + AI 自动建场景(Argon 写 MuJoCo),因果可靠但场景受限,这是目前唯一有真机提升数据的;3. 持久 3D 场景(World Labs、腾讯),介于两者之间。今天的 [Physicl 融资](2026-11-08-physicl-raises-10m-to-make-the-digital-world-real-enough-for-robots.md) 也是在押第 2、3 种。先找瓶颈:机器人板块当下卡在高质量、物理正确、包含失败的数据。受益的层次会是:第一层是算力,世界模型渲染和大规模仿真都极度吃 GPU,NVIDIA(包括 Isaac Sim / Cosmos 这条线)和 Google TPU 是确定性受益方;第二层是能保证物理正确性的仿真工具链,物理引擎和合成数据公司;第三层是人形机器人整机厂,Apptronik 出现在演示里说明它和 Google 的合作在继续。这条新闻我会挂在机器人板块和 AI 板块,但对机器人板块的利好要打折扣,因为目前没有任何定量证据表明 Genie 4 能提升真机表现。也可以对照 [Import AI 479 里对 Genie 4 的讨论](2026-11-05-import-ai-479-spacewar-low-latency-tasks-versus-llms-genie-4.md)。值得跟踪的是 Google 的技术报告,看它有没有真机迁移的数字。
