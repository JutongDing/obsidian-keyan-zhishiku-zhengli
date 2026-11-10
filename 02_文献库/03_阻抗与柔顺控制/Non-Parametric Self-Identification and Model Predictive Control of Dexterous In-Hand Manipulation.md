---
title: "Non-Parametric Self-Identification and Model Predictive Control of Dexterous In-Hand Manipulation"
year: 2023
doi: 
arxiv: 2307.10033
key: KB-104
venue: arXiv 预印本（cs.RO，首页未标注会议/期刊，待补）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [手内操作, 高斯过程回归, 模型预测控制, 欠驱动手, 自辨识]
pdf: ../../../Non-Parametric Self-Identification and Model Predictive Control of.pdf
confidence: high
source: pdf
aliases: []
---

# Non-Parametric Self-Identification and Model Predictive Control of Dexterous In-Hand Manipulation

## 📌 年份
2023

## 🔑 论文识别码
arXiv:2307.10033

## 👥 作者与所属院校
- 作者：Podshara Chanrungmaneekul, Kejia Ren, Joshua T. Grace, Aaron M. Dollar, Kaiyu Hang 等
- 机构：莱斯大学（Rice University）、耶鲁大学（Yale University）

## 📖 研究背景
- [[手内操作]]的手-物模型涉及几何、动力学与时变接触，精确建模困难，且叠加物理与感知不确定性。
- 主流数据驱动方法依赖大量离线数据，样本代价高，换物体或换抓取还要重训。
- 该文放弃精确建模，用少量探索动作在线自辨识局部模型，再嵌入 MPC 闭环控制。

## ❓ 需要解决的问题
- 无关节编码器、仅单目相机时，能否用十几条数据辨识出手-物映射？
- 模型何时失效，能否按误差自动触发补采数据？
- 换物体后能否迁移已学模型，减少新物体的探索次数？

## 📥📤 输入与输出
- 输入：物体上标记点的三维位置（AprilTag，1024×512，30 fps）、欠驱动手的驱动指令。
- 输出：驱动器指令序列，以及预测的物体标记点运动轨迹。

## ✅ 论文最终达到的效果
- 用高斯过程回归学 Γ 与逆模型 Γ⁻¹，初始探索 20 次后性能收敛，平均操作误差 < 0.8 mm。
- 一般只需不到 30 个数据点，单个任务 15 点即可完成（误差阈值 γ = 2 mm 触发更新，到位容差 α = 1 mm）。
- MPC 优化尺度 σ < 0.02 时更新请求过多；适度增大后平均自适应动作降到 5 次以下。
- 模型迁移：源物体 25 次探索所得模型直接用于新物体，总探索次数从 25 降到 12，误差无显著上升。
- 硬件为无编码器 Yale Model O [[欠驱动手]]加单目相机，验证了毫米级精度。

## 🔗 关联
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]
- [[Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control]]
- [[Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control]]

## 🏷️ 标签
#手内操作 #高斯过程回归 #模型预测控制 #欠驱动手 #自辨识
