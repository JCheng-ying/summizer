# British inference chip developer Fractile raises $720M in funding
https://siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/

这篇文章讨论的是 AI 推理阶段一个越来越清晰的物理瓶颈：模型不是算不动，而是数据搬不动。当 agent 需要长链条、多步骤地调用大模型时，限制速度和能耗的往往是计算单元和内存之间来回搬运数据的那段距离。谁能把这段距离缩短，谁就有机会在推理芯片这一层分走 GPU 的一部分蛋糕。

文章指出，英国 AI 推理芯片初创公司 Fractile 完成了 7.2 亿美元 C 轮融资，由 Thrive Capital、Founders Fund、Lightspeed 和 Redpoint 领投，跟投方约十几家，包括英国 Sovereign AI Fund、British Business Bank 以及 Alphabet 旗下的 CapitalG，公司估值达到 70 亿美元。Fractile 由 AI 研究员 Walter Goodwin 在 2022 年创立。公司声称其芯片性能可达现有芯片的 100 倍，能耗降低 90%，不过这些都是公司自己的预期，芯片要到明年才开始出货。

技术原理上，文章解释得比较清楚：大语言模型生成回答要经过很多步，每完成一步就把结果写到片外的 HBM，再读回来作为下一步的输入，这种反复往返拖慢了推理。解决这个瓶颈目前有三种思路：第一是 Cerebras 的晶圆级芯片，用大容量片上 SRAM 缓存（WSE-3T 可以存 44GB）减少数据移动，SRAM 每个单元六个晶体管，速度快但贵、容量有限；第二是 Fractile 的做法，把标准 DRAM 直接堆叠在芯片逻辑电路的正上方，缩短数据传输距离、降低搬运能耗；第三是 Samsung 8 月发布的 zHBM，同样可以堆叠在 AI 加速器上，用细铜线连接，Samsung 称它比未来的 HBM5 快 8 倍。Fractile 预计其芯片能让 LLM 每秒处理数千个 token，并计划以机架级系统、配合自研编译器等软件一起交付。TechCrunch 同日的报道补充，英国政府称这轮融资是为了让英国"在支撑未来经济的硬件上拥有更大份额"，并把 Fractile 与 Axelera、Etched、OLIX 并列为融资最多的专用 AI 芯片初创公司之一；公司此前经历过一次技术路线转向，才确定了 DRAM 堆叠方案。

个人看法：这篇可以和之前的 [Staera 为 chiplet 开发光互联](2026-11-10-staera-launches-with-4-6m-to-develop-an-optical-interconnect-for-chiplets.md)、[Google 扩展 TPU 家族](2026-11-09-google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-m.md) 放在一起看：推理阶段的竞争正在从"谁的算力峰值高"转向"谁的数据搬运代价低"。用"先找瓶颈"的方法看，瓶颈在内存带宽和数据移动能耗，而不在计算单元本身。所以真正受益的层次会是：第一层是先进封装和 3D 堆叠能力，不管是 Fractile 的 DRAM 堆叠还是 Samsung 的 zHBM，都需要混合键合、TSV 这类工艺，TSMC 的先进封装产线以及 Besi、Applied Materials 这类键合设备厂商都是受益方；第二层是存储厂商，DRAM 从"插在旁边"变成"堆在上面"，Samsung、SK hynix、Micron 的产品形态会随之改变；第三层才是推理芯片初创公司本身，它们的风险最高，因为性能数据尚未经过独立验证，而且需要在 Nvidia 的软件生态面前证明编译器足够好用。

这对 AI 板块是利好，因为它说明资本仍在大规模押注推理效率；如果 90% 的能耗降低能部分兑现，对能源约束也有边际缓解，但目前还停留在公司预期层面，不足以构成能源板块的信号。值得关注的是 Fractile 明年首批芯片和系统出货后，有没有第三方基准测试或公开客户名单。
