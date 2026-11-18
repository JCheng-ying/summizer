# Quantum Physics Can Verify a Person’s Location, NIST Researchers Show
https://thequantuminsider.com/2026/11/18/quantum-physics-can-verify-a-persons-location-nist-researchers-show/

(说明:本文是 NIST 新闻稿经 The Quantum Insider 转载,内容是机构对自家研究的介绍。)

这篇文章背后的命题,是把数字安全从"你知道什么/你持有什么"转移到"你在哪里"。今天所有身份验证——密码、短信验证码、硬件密钥、乃至后量子密码 PQC——本质上都是在验证某个秘密或某个设备,而秘密可以被偷、设备可以被远程劫持,所以攻击者可以坐在地球另一端发起操作。如果物理位置本身能被不可伪造地证明,那么"远程攻击"这个类别在某些高价值场景里就会被直接从协议层面排除。

文章指出,NIST 的 Krister Shalm 和国际合作者在 Nature 上发表了首个完整的量子位置验证(quantum position verification, QPV)实验,并补上了此前同类方案留下的漏洞。实验设置是:在 NIST Boulder 园区里搭了两个相距 195 米的验证站,用电缆和光纤连接,被验证方(prover)声称位于两者之间。流程可以拆成三步。第一步,一个验证站生成一对纠缠光子,自己留一个,把另一个发给被验证方;第二步,两个验证站各发出一串随机数,精确计时让它们同时到达被验证方声称的位置,被验证方必须根据这两串随机数决定如何测量光子的偏振,再把结果回传;第三步,验证站根据往返时间三角定位,同时比对双方光子测量结果的相关性,整个过程在几分钟内重复数百万次。

这里真正起作用的是两条物理约束叠加。第一是光速上限:如果被验证方不在声称的位置,回传必然比预期晚,时间上就露馅。第二是量子不可克隆定理和无漏洞 Bell 检验:冒充者无法复制纠缠态分发给远处的同伙,而测量指令又是随机的、无法提前预测,所以只要相关性强于经典物理允许的上限,就能同时证明"人在那里"和"设备没被动手脚"。文章特别强调,任何实验误差或对量子设备的篡改都会导致 Bell 检验失败——这意味着该方案是"设备无关"的,不需要信任设备厂商,这比单纯依赖时间延迟的经典测距方案要强得多。

但文章也非常坦白:研究合作者 Scott Glancy 表示,真正落地可能还要十年以上,因为前提是存在能在客户和银行之间分发纠缠光子的高保真量子通信网络,而这样的网络目前还在开发中。

个人看法:这篇论文的投资含义,和它描绘的应用场景(银行转账、电网和核电站指令、交易账户)相比要间接得多。按"先找瓶颈"的思路,QPV 本身的协议已经被证明可行,卡住它的不是理论,而是三个具体的工程能力:第一是长距离、高保真的纠缠分发,也就是量子网络/量子中继器;第二是高效率的单光子探测器和纠缠光源;第三是纳秒级的时间同步与低延迟经典链路。195 米的园区实验离城市尺度差了好几个数量级,所以当下真正有业务的仍然是不依赖纠缠分发的那一层。

这和今天同一批读到的几篇形成了一条很清楚的线索:[Chicago 到欧洲 8000 公里的 QKD+PQC 混合网络](2026-11-18-hybrid-qkd-and-pqc-network-connects-chicago-and-europe-across-8-000-km.md)、[Bradesco 和 evolutionQ 的量子通信测试](2026-11-18-bradesco-and-evolutionq-begin-quantum-communication-tests-to-assess-new-data-pro.md),以及昨天的 [NEC 和 IBM 日本的 QKD+PQC 集成演示](2026-11-17-nec-and-ibm-japan-demonstrate-integrated-qkd-and-pqc-communications.md)、[Telia/Nokia/Qmill 的 5G 量子加密](2026-11-17-telia-nokia-and-qmill-demonstrate-quantum-powered-encryption-in-a-5g-network.md),都在说明"量子安全"现阶段的商业化主力是 PQC 软件迁移加点对点 QKD,而 QPV 属于下一代、需要真正纠缠网络的应用。早先 [Toshiba 拿到英国量子网络合同](2026-11-08-toshiba-secures-uk-contract-to-develop-quantum-networking-technologies.md) 和 [量子隐形传态的科普](2026-08-14-what-is-quantum-teleportation-how-quantum-states-transfer-across-distance.md) 讲的也是这层基础设施。

所以对量子计算板块来说,受益的层次会是:第一层是现在就有收入的量子安全软件和 QKD 设备商,比如 Toshiba、ID Quantique(已被 IonQ 收购)以及做密码敏捷性迁移的软件公司,它们卖的是"今天能部署"的东西;第二层是光子器件和探测器供应链——超导纳米线单光子探测器、纠缠光源、低损耗光纤与光开关,这一层同时服务光量子计算和量子网络,无论 QPV 何时落地都会先被拉动;第三层才是量子中继和量子网络运营,这是 QPV 真正依赖的瓶颈,但目前仍主要由 NIST、DOE 国家实验室这类公共资金在推动,离可投资的商业标的还远。这篇论文对板块是一个科学背书,而不是订单信号。

现在还早,QPV 更像是给"为什么要建量子网络"补上了一个新的需求理由——除了 QKD 之外,位置认证也需要纠缠分发。值得关注的是后续有没有城域尺度(几公里到几十公里)的 QPV 演示,或者金融机构、电网运营方在已有 QKD 试点里加入位置验证的测试,那会是这条路线从实验室走向产业的第一个具体信号。
