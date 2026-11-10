---
title: A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation
year: 2026
doi: 10.1016/j.apm.2026.117151
arxiv: 
key: KB-014
venue: "Applied Mathematical Modelling, 161: 117151（卷期标注 2027，2026-06-24 在线）"
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 摩擦锥, 算子分裂, 实时控制, 凸优化]
pdf: ../../../A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1016/j.apm.2026.117151
（期刊卷期页标为 Applied Mathematical Modelling 161 (2027) 117151，DOI 与在线日期为 2026 年）

## 👥 作者与所属院校
- 作者：Gaston Haidak, Yekini Shehu, Jianlong Kou
- 机构：浙江师范大学（物理与电子信息工程学院、数学科学学院）

## 📖 研究背景
- 精密装配、仓储物流、果蔬采摘都要求毫秒级重算指尖力，既不能滑移也不能压坏工件。
- [[抓取力优化]]（GFO）是这些场景的共同数学内核：在[[摩擦锥]]与力平衡约束下求最小范数接触力。
- 早期把摩擦锥线性化为线性规划，牺牲可行性保证；半定规划、内点法精度高但单次迭代昂贵、难以热启动，成为实时性瓶颈。
- 已有算子分裂工作未把该问题当作圆锥规划处理，也未给出完整的收敛与主动集识别分析。

## ❓ 需要解决的问题
- 能否把 GFO 写成保留圆形摩擦锥几何的凸二次圆锥规划，并给出可在线求解的一阶算法？
- 自适应步长与反射惯性项能否在保持理论保证的同时把单次求解压到亚毫秒？
- 主动接触约束能否在有限次迭代内被识别，从而转为自由子空间上的线性迭代？
- 传感器噪声下如何在线自适应而不破坏收敛？

## 📥📤 输入与输出
- 输入：接触点位置与法向、摩擦系数、时变外部力旋量（重力、插入阻力、装配力矩）、上一步解（热启动）。
- 输出：满足力平衡与摩擦锥约束的各指接触力（含切向分量）及平衡乘子。

## ✅ 论文最终达到的效果
- 建立凸二次圆锥规划（CQCCP）形式，证明全局收敛、自然残差 O(1/k) 速率、主动集有限步识别，识别后局部 R 线性收敛。
- 工业装配算例（12 自由度 Inspire RH56DFX 五指、0.48 kg 铝圆柱、μ=0.45）：N=4000 时热启动 0.32 ms，比 SeDuMi 快约 9 倍、比 MOSEK 快约 11 倍、比 OSQP 快约 20%。
- 单次迭代耗时随规模线性增长（40 μs→320 μs，N 由 2000 增至 16000），支撑最高 1 kHz 控制回路。
- 热启动使迭代次数减少 25%–40%；软三指采摘算例（0.18 kg 苹果、μ=0.65、压伤阈值 8 N）同样亚毫秒求解。
- 给出噪声下的随机扩展并分析其收敛性；回代残差均低于 1e-4 容差。

## 🔗 关联
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]
- [[Calculation of Robot Multi-Fingered Grasping Force and Displacement Based on the Newton–Subgradient Non-Smooth Greedy Randomized Kaczmarz Method for Solving Linear Complementarity Problem]]

## 🏷️ 标签
#抓取力优化 #摩擦锥 #算子分裂 #实时控制 #凸优化
