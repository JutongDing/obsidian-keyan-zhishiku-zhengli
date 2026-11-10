---
title: "Real-Time Grasping-Force Optimization for Multifingered Manipulation: Theory and Experiments"
year: 2004
doi: 10.1109/TMECH.2004.823879
arxiv: 
key: KB-118
venue: IEEE/ASME Transactions on Mechatronics, vol. 9, no. 1, pp. 65–77
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 线性矩阵不等式, max-det, 三指手实验]
pdf: ../../../Real-time_grasping-force_optimization_for_multifingered_manipulation_theory_and_experiments.pdf
confidence: high
source: pdf
aliases: []
---

# Real-Time Grasping-Force Optimization for Multifingered Manipulation: Theory and Experiments

## 📌 年份
2004

## 🔑 论文识别码
DOI: 10.1109/TMECH.2004.823879

## 👥 作者与所属院校
- 作者：Guanfeng Liu、Zexiang Li
- 机构：香港科技大学（电机与电子工程系）

## 📖 研究背景
- 多指灵巧操作需同时满足[[摩擦锥]]约束与实时性，而摩擦锥本质非线性，接触还在滚动、滑动中时变，问题维度可能极大。
- 已有两条主流路线：BHM 方法把约束嵌入矩阵正定与仿射约束，HTL（Han–Trinkle–Li）方法化为 max–det 型线性矩阵不等式问题。
- 两者的共同短板是递推算法都需要一个可行初值，而可行初值本身在实机上并不易得，这一环节常被忽略。
- 本文切入角度：用 LMI（max–det）算法自动生成初值，再交给梯度递推，从而把[[抓取力优化]]做成可实时运行的完整流程。

## ❓ 需要解决的问题
- 能否把「法向力最小」的指力优化问题在线性矩阵不等式框架下写成可高效求解的 max–det 问题？
- 如何在多指、时变接触下自动生成既满足正定约束又满足仿射约束的初始点，避免人工试凑？
- 自动初值 + 梯度递推后，单次优化的计算量能否降到实机控制周期内？
- 该算法在三指手上配合接触坐标规划，能否完成不落物的物体操作实验？

## 📥📤 输入与输出
- 输入：物体外力旋量、各接触坐标与几何参数、[[抓取矩阵]]映射、摩擦系数与指力权重矩阵。
- 输出：满足摩擦锥约束的最优接触力（含[[内力]]分量）与相应手指速度指令。

## ✅ 论文最终达到的效果
- 给出完整算法链：先用 max–det 求可行初值（Algorithm 1），再以该初值启动内点/梯度迭代求最优指力。
- 用 LAPACK 求特征值与特征向量，初值搜索在 SUN ULTRA60 上约 20 ms，非奇异情形约 10 ms。
- 与已有算法做计算时间对比（论文 Table I），组合方案在同等最优性下更快，且无需外部给定初值。
- 在 HKUST 三指手平台上完成完整操作实验：三指接触坐标收敛到三个对称点（视为最优抓取构型），指力与代价函数收敛曲线平稳。
- 优化后接触力的 z 分量显著下降，因为只在代价函数中计入其贡献，说明该指力分配确实压缩了多余内力。

## 🔗 关联
- [[Recursive Algorithms for Real-Time Grasping Force Optimization]]
- [[Real-Time Force Regulation for Whole-Hand Dexterous Grasping]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#抓取力优化 #线性矩阵不等式 #max-det #摩擦锥 #三指手实验
