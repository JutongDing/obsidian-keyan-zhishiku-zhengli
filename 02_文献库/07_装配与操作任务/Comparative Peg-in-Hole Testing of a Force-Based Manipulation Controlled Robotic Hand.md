---
title: "Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand"
year: 2018
doi: 10.1109/TRO.2018.2791591
arxiv: 
key: KB-029
venue: IEEE Transactions on Robotics, 34(2): 542–549
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 性能基准, 力控操作, 非参数统计, 多指手]
pdf: ../../../Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand.pdf
confidence: high
source: pdf
aliases: []
---

# Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand

## 📌 年份
2018

## 🔑 论文识别码
DOI: 10.1109/TRO.2018.2791591

## 👥 作者与所属院校
- 作者：Karl Van Wyk, Mark Culleton, Joe Falco, Kevin Kelly
- 机构：美国国家标准与技术研究院（NIST）、爱尔兰都柏林圣三一学院

## 📖 研究背景
- 力控操作正成为装配精细操作的主要手段，但领域缺少可复现、可统计比较的性能基准。
- 已有插入基准的共性缺陷：试件设计随意、只看完成时间、依赖昂贵力测量或定制件、统计方法不全。
- 力控 [[柔顺控制]] 方案要在装配中立足，必须与成熟夹爪方案在同条件下正面对比。
- [[轴孔装配]] 占工业装配操作 35% 以上，是合适的测试载体。

## ❓ 需要解决的问题
- 能否用 3D 打印件做出低成本、可复制的插孔测试方法与配套指标？
- 三指 [[灵巧手]] 的指尖力控能否与「刚性夹爪 + 柔顺臂」方案同台比较？
- 在两组位置误差下，两系统的完成时间与成功率差异是否统计显著？

## 📥📤 输入与输出
- 输入：随机生成的孔位误差（σ1 与 σ2=2 mm）、三指 [[指尖力传感器]] 测得的法向/摩擦三维力、塞杆位姿。
- 输出：完成时间 CT、成功率 PS（95% 置信），以及自相关、KS、Levene、t 检验、KC 检验结论。

## ✅ 论文最终达到的效果
- 建成 NIST 可复制测试：孔间距 35 cm、无量纲间隙 c=(D−d)/D=0.02、60 次插入、3D 打印试件。
- 统计流程把连续量（CT）与离散量（PS）分开：r1 查样本独立性，KS 比分布，Brown–Forsythe 比方差，KC 比序数成功率。
- 系统 1（力控手 + 刚性臂）：σ1 下 CT 11.70 s、PS 85.4%；σ2 下 18.31 s、87.6%。
- 系统 2 准随机搜索：σ1 下 3.11 s、95.2%；σ2 下 8.2 s、95.2%，快于手系统。
- 手系统对位置误差最不敏感：均值仅膨胀 1.6 倍，螺旋搜索的臂系统膨胀 4.6 倍。
- 系统 1 在 σ1 下 60 次中失败 4 次、σ2 下失败 3 次，系统 2 无失败；按 KC 检验需至少 5 次失败才具显著差异。
- 人手 DFA 参考 CT 为 2.5 s；结论为手系统已达夹爪系统的可竞争水平。

## 🔗 关联
- [[Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands]]
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]
- [[Active Touch Sensing for Robust Hole Detection in Assembly Tasks]]

## 🏷️ 标签
#轴孔装配 #性能基准 #力控操作 #非参数统计 #多指手
