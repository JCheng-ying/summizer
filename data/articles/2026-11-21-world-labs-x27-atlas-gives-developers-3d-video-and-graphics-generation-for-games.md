# World Labs' Atlas Gives Developers 3D Video and Graphics Generation for Games, Robotics, More
https://www.deeplearning.ai/the-batch/amds-world-model-arrives/

这篇文章讲的是世界模型从"演示视频"走向"可以买、可以导出的开发者工具"。如果世界模型能稳定地产出可用于游戏引擎和仿真器的 3D 资产,那么机器人训练里最贵的一环——构建大量多样化的仿真环境——成本会显著下降;同时这件事还发生在 AMD 刚完成收购 World Labs 之后,牵涉到芯片厂商向模型和软件层延伸的战略。

文章指出,World Labs 11 月 12 日向所有人开放了最新世界模型 Atlas,提供自助 API,可以把文字提示变成 3D 场景和可控相机路径的视频并导出。配套的网页工具有 Viewfinder(用一张或多张照片构建场景,最多 64 张)、Chisel(从参考图或文字构建场景),以及重新打光的 Relight 和把高斯泼溅(Gaussian splats)转成网格的 Splats to Mesh。技术上,Atlas 是一个从零预训练的多模态自回归扩散 Transformer,能处理文本、图像、视频和 3D 数据,并把每张图像和深度图绑定到具体相机位姿,所以可以从不同视角一致地渲染同一场景。定价是 720p 首帧 0.04 美元、之后每帧 0.008 美元,转成精细 splats 5 美元。开发者可以串联 API:估计相机位姿和深度、渲染新视角或视频、转成 splats、再转成带纹理的多边形网格或给游戏引擎和仿真器用的简化碰撞体。性能方面,Atlas 在 Rapidata 公开榜上 19 个视频和世界模型中遵循相机运动指令排名第一,人类评审在 76.7% 的对比中更偏好它;World Labs 自测在七个数据集上 3D 重建误差比第二名 Pi3X 平均低约 12%,但没有发布模型卡或论文,外部也还没有复现。背景方面,9 月 AMD 同意以约 82 亿美元全股票收购 World Labs,11 月 16 日完成,联合创始人李飞飞出任 AMD 首席科学家和执行副总裁,但 AMD 的公告都没有提到 Atlas 或 World Labs 产品的未来。文章还注意到,Atlas 9 月发布时重点讲为机器人构建仿真训练环境,这次正式上线则以网页工具和 3D 管线为主,开发者文档里已经不提机器人。

和 [Can agentic robotics solve robotics data scaling problem](2026-11-09-can-agentic-robotics-solve-robotics-data-scaling-problem.md) 讨论的机器人数据瓶颈联系起来看,仿真环境的生成成本正是数据瓶颈的一部分。

个人看法:我觉得这篇文章最关键的一句是"它有价目表和导出按钮"。Google DeepMind 的 Genie 4、Runway 的 GWM Worlds 2 都是流式输出像素的交互视频,好看但没法直接用;Atlas 输出的是 splats 和网格,可以进 Blender、游戏引擎和仿真器,这就和 NVIDIA Isaac Sim 这类机器人仿真工作流接得上了。机器人训练的瓶颈之一是仿真环境的多样性:人工搭一个逼真的厨房或仓库场景要很多工时,而 sim-to-real 的效果很大程度取决于环境够不够多样。如果用几张照片就能重建一个带碰撞体的场景,这一层的成本会大幅下降。所以对机器人板块的利好机制是"降低仿真数据的生产成本",而不是直接卖机器人;不过 World Labs 在文档里淡化机器人用途,说明短期商业重心可能在游戏和 3D 内容。对 AI 板块来说,更值得思考的是 AMD 的意图:收购一家世界模型公司,说明 AMD 想在软件和模型层建立自己的生态,来弥补和 Nvidia 在 CUDA、Omniverse、Cosmos 上的差距。受益的层次会是:第一层是 AMD 本身,如果 Atlas 被优化到 MI 系列 GPU 上运行,就是一个能拉动 GPU 需求的应用入口;第二层是仿真和 3D 引擎生态(Unity、Epic、Autodesk 等);第三层是依赖大规模仿真训练的机器人基础模型公司。不过 AMD 的公告完全没提 Atlas,产品方向还不清楚,目前只能观望,值得关注的是 AMD 会不会把 Atlas 整合进自己的机器人或 ROCm 软件栈。
