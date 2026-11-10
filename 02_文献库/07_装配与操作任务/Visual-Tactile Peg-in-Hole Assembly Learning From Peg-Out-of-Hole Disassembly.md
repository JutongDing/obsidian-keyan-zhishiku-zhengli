---
title: Visual-Tactile Peg-in-Hole Assembly Learning From Peg-Out-of-Hole Disassembly
year: 2026
doi: 10.1109/LRA.2026.3679227
arxiv: 
key: KB-160
venue: IEEE Robotics and Automation Letters（RA-L, vol. 11, no. 6, 2026）
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 视触融合, 强化学习, 示教数据复用, 逆任务]
pdf: ../../../Visual-Tactile Peg-in-Hole Assembly Learningfrom Peg-out-of-Hole Disassembly.pdf
confidence: high
source: pdf
aliases: []
---

# Visual-Tactile Peg-in-Hole Assembly Learning From Peg-Out-of-Hole Disassembly

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1109/LRA.2026.3679227

## 👥 作者与所属院校
- 作者：Yongqiang Zhao, Xuyang Zhang, Zhuo Chen, Matteo Leonetti, Emmanouil Spyrakos-Papastavridis 等
- 机构：英国伦敦国王学院（King's College London，待核对）

## 📖 研究背景
- [[轴孔装配]]是机器人装配的基础难题，要求精确对位与柔顺力控，长期依赖人工示教。
- [[强化学习]]从零探索代价高，监督学习依赖高质量示教且对未见间隙/物体泛化差。
- 插入的逆任务——拔出（PooH）只需克服摩擦、无需精确对位，数据采集容易得多。
- 该文把拔出策略的轨迹时间反演并随机化动作，作为插入任务的专家数据。

## ❓ 需要解决的问题
- 拔出轨迹反向复用，能否等价为插入任务的高质量专家示教？
- 视觉与触觉在插入中各自承担什么角色，去掉任一模态会损失多少？
- 在多种销孔几何与亚毫米间隙下，成功率与接触力能否同时改善？
- 对未见物体与未见销孔形状的泛化能力如何？

## 📥📤 输入与输出
- 输入：机器人运动学、腕部视觉图像、触觉流（tactile flow）。
- 输出：末端位姿增量动作；拔出与插入共享同一 POMDP 观测空间与动作空间。

## ✅ 论文最终达到的效果
- 视触双模态策略的接触力比单模态版本低 6.4%。
- 已知物体平均成功率 87.5%，未见物体 77.1%。
- 比从零训练插入策略的直接强化学习高 18.1 个百分点。
- 六种销孔对（红立方、红圆柱、红六边形、白立方、红 D 形、红不等边三角），含 1.0 mm 间隙。
- 消融证实视觉负责远距接近，触觉补偿销孔对位偏差，二者互补。

## 🔗 关联
- [[Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands]]
- [[Haptic-Based and SE(3)-Aware Object Insertion Using Compliant Hands]]
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]

## 🏷️ 标签
#轴孔装配 #视触融合 #强化学习 #示教数据复用 #逆任务
