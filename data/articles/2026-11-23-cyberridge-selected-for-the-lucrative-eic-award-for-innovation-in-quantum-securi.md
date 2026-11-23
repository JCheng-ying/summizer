# CyberRidge Selected for The Lucrative EIC Award For Innovation In Quantum Security
https://thequantuminsider.com/2026/11/23/cyberridge-european-innovation-council-co-funding/

需要先说明,这篇是 CyberRidge 自己的新闻稿,产品原理和效果描述都来自公司,未经独立验证。但它提出的问题值得单独拿出来看:量子安全这条线索里,大家一直在讨论"怎么让数据更难被解密",而这家公司认为真正没被解决的是另一半——数据在被截获的那一刻就已经输了。

文章指出,欧洲创新理事会(EIC)在这一轮从 1211 家申请者中选出 71 家给予联合资助,CyberRidge 是其中之一。它针对的是"先截获、后解密"(Harvest Now, Decrypt Later)威胁:攻击者今天在光纤上窃听并大规模存储加密流量,等量子计算机成熟后再解密。文章认为,TLS、IPsec、MACsec、后量子密码(PQC)甚至量子密钥分发(QKD)都只是让数据更难解密,但它们产生的信号仍然可以被录下来。CyberRidge 的产品 Carmel 采用所谓"光子层安全":第一,把信号分散到数百个波长上;第二,把信号埋在光学噪声之下;第三,用持续变化且从不存储的光子密钥保护信号。公司称窃听者在光纤上拿不到可用信号,只有授权接收端能还原数据,而且由于保护基于物理而不是数学复杂度,算力进步(包括量子和 AI)不会削弱它。部署上,它替换现有光传输设备里的线路卡,不需要改网络架构。EIC 资金将用于在欧洲与电信运营商、国防机构和关键基础设施客户推进部署;公司此前累计融资 2600 万美元,投资方包括 AWZ、Elron Ventures、Arkin Capital、RedSeed VC 和欧盟 Horizon-EIC 项目。

个人看法:最近量子安全相关的文章已经形成一条很清楚的线:[NEC 和 IBM 日本的 QKD+PQC 集成演示](2026-11-17-nec-and-ibm-japan-demonstrate-integrated-qkd-and-pqc-communications.md)、[芝加哥到欧洲 8000 公里的混合网络](2026-11-18-hybrid-qkd-and-pqc-network-connects-chicago-and-europe-across-8-000-km.md)、[SK Broadband 在韩新海缆上测试量子安全](2026-11-19-sk-broadband-to-test-quantum-security-on-korea-singapore-subsea-cable.md)。目前来看保护传输数据有三种思路:1. 数学层,PQC 换算法,成本最低、最容易大规模铺开;2. 密钥层,QKD 用量子物理分发密钥,安全性更强但距离和成本受限;3. 物理信号层,也就是 CyberRidge 这种让信号本身不可截获的路线。第三种的说法最激进,但"基于物理所以不受算力影响"这类表述需要独立的密码学评估来证实,在没有第三方测试之前我会保持怀疑。

先找瓶颈:量子安全市场今天的瓶颈不是技术选择,而是部署动力——量子计算机还没真正能破解 RSA,大部分企业没有紧迫感去升级。HNDL 叙事的价值就在于把"未来的威胁"折算成"今天的损失",对需要保密十年以上数据的电信、国防和关键基础设施客户最有说服力,EIC 资助的方向也正对着这几类客户。和今天 [海上算力那篇](2026-11-23-the-coming-wave-is-compute-at-sea-ready-to-sink-or-swim.md) 里专家担心离岸光缆被窃听是同一个问题,光纤物理窃听正在从理论风险变成被反复点名的现实风险。

对量子计算板块来说,这类公司属于"量子威胁的受益者"而不是量子计算本身:受益层次是,第一层是已经在推 PQC 迁移的网络和安全设备商,比如 Cisco、Nokia、Ciena 这些光传输和路由厂商,任何光层方案最终都要嵌进它们的设备里;第二层是 QKD 和量子安全专业厂商,IonQ(收购了 ID Quantique)、Toshiba,以及 [准备收购 QuintessenceLabs 的 SEALSQ](2026-11-18-sealsq-signs-letter-of-intent-to-acquire-quintessencelabs.md);第三层才是 CyberRidge 这种早期私营公司。2600 万美元的累计融资说明它还很早,值得跟踪的是它能不能拿到一家欧洲大型电信运营商的商用部署,而不只是试点。
