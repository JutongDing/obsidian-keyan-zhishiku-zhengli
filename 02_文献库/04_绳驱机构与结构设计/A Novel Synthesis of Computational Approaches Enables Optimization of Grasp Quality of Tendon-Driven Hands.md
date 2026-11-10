---
title: A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands
year: 2012
doi: 10.1109/TRO.2012.2196189
arxiv: 
key: KB-020
venue: IEEE Transactions on Robotics
theme: 02_文献库/04_绳驱机构与结构设计
tags: [腱驱动, 抓取质量, 机构设计优化, 蒙特卡洛]
pdf: ../../../A_Novel_Synthesis_of_Computational_Approaches_Enables_Optimization_of_Grasp_Quality_of_Tendon-Driven_Hands.pdf
confidence: high
source: pdf
aliases: []
---

# A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands

## 📌 年份
2012

## 🔑 论文识别码
DOI: 10.1109/TRO.2012.2196189

## 👥 作者与所属院校
- 作者：Joshua M. Inouye、Jason J. Kutch、Francisco J. Valero-Cuevas
- 机构：南加州大学（University of Southern California）

## 📖 研究背景
- [[腱驱动]]手在灵巧手中具备轻量、低背隙、可远端驱动、力臂与最大腱张力可设计等优势。
- 但腱张力约束、腱摩擦与关节力矩上限使「可行抓取力旋量集合」难以解析求得，设计评价长期靠经验。
- 既有抓取质量指标多为方向相关或需指定力旋量方向集，难以直接用于腱驱动机构的设计优化。
- 本文切入角度：把几何计算、凸包/闵可夫斯基和、蒙特卡洛与回归合成为一条可跑大规模设计空间的流水线。

## ❓ 需要解决的问题
- 如何对任意设计参数的腱驱动手算出完整可行抓取力旋量集合及其[[抓取质量]]？
- 两种腱布置（每自由度对置双腱的 2N 与 N+1 冗余布置）在同样抓取下质量差多少？
- 哪些设计参数（腱最大张力、力臂、关节力矩上限、连杆长度）对质量影响最大？
- 如何把单次评价从数十秒压到可做上千次蒙特卡洛与参数扫描的量级？

## 📥📤 输入与输出
- 输入：手的几何与驱动参数（连杆长度、关节姿态、各腱力臂、腱最大张力、关节力矩容量）、接触位置与静摩擦系数（算例 μs=0.5）、两指/三指抓取构型。
- 输出：可行抓取力旋量凸多面体、方向无关抓取质量（单位 N）、蒙特卡洛质量分布，以及每 1% 参数变化对应的质量变化百分比（归一化回归系数）。

## ✅ 论文最终达到的效果
- 给出完整方法链：腱张力可行域→关节力矩→指尖力→抓取力旋量凸包→最弱方向半径即抓取质量。
- 两指与三指算例中 2N 布置均优于 N+1；三指抓取质量整体高于两指。
- 1000 次蒙特卡洛在最后 20% 迭代中均值与变异系数变化小于 2%，判定收敛；两指 N+1 回归 R²=0.930。
- 网格简化使单次评价由 50 s 降至 1.37 s（约 97%）；可行力集合简化为 12 个顶点再省 46%–77% 时间，质量误差小于 2%。
- 识别出关键薄弱参数为「腱 1 最大张力」：提高 15% 后质量比 N+1 基线高 3.31%–94%；单力臂 ±10% 约带来 10% 质量变化。

## 🔗 关联
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A metric to design spring stiffness of underactuated fingers for stable grasp]]

## 🏷️ 标签
#腱驱动 #抓取质量 #机构设计 #蒙特卡洛
