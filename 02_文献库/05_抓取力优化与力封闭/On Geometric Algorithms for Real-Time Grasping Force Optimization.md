---
title: On Geometric Algorithms for Real-Time Grasping Force Optimization
year: 2004
doi: 10.1109/TCST.2004.833630
arxiv: 
key: KB-108
venue: IEEE Transactions on Control Systems Technology, Vol.12, No.6, pp.843–857
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 摩擦锥, 黎曼流形, 收敛性分析, 实时计算]
pdf: ../../../On Geometric Algorithms for Real-Time Grasping.pdf
confidence: high
source: pdf
aliases: []
---

# On Geometric Algorithms for Real-Time Grasping Force Optimization

## 📌 年份
2004

## 🔑 论文识别码
DOI: 10.1109/TCST.2004.833630

## 👥 作者与所属院校
- 作者：Guanfeng Liu、Jijie Xu、Zexiang Li
- 机构：香港科技大学电子与电机工程系

## 📖 研究背景
- 多指手[[抓取力优化]]要在[[摩擦锥]]约束下最小化目标函数，约束与目标都非线性，接触构型还随时间变化，必须实时求解。
- 把摩擦锥线性化的做法解偏保守；半正定规划/内点法精度高，但此前多维求解，实时性不足。
- Buss 等发现摩擦锥约束等价于某些对称矩阵正定，问题可化为黎曼流形上的凸优化；Helmke 等再降维，衍生出五种候选算法。

## ❓ 需要解决的问题
- 两种梯度算法、两种 Newton 算法与一种内点算法，能否放进统一的几何框架推导并给出步长选取规则？
- 哪些算法具二次收敛？其连续版本是否指数收敛？
- 摩擦锥的不同矩阵表示（BHM/HHM）与处理器、容差差异，对实时计算时间影响多大？
- 优化出的指力能否驱动物体轨迹跟踪控制器并在真手上闭环？

## 📥📤 输入与输出
- 输入：接触坐标与法向、摩擦系数与接触类型（软指/硬指）、[[抓取矩阵]]、物体期望运动与外力、初始指力。
- 输出：使目标函数最小的各指接触力（按[[接触力分配]]），以及指端速度/位置指令。

## ✅ 论文最终达到的效果
- 在统一框架下给出五种算法与各自步长规则；证明部分算法二次收敛、连续版本指数收敛。
- HHM 表示使算法 1–4 的计算时间降到 BHM 表示的约 1/5，内点法约 1/2。
- 实时性最好的是 Dikin 型欧氏梯度算法（算法 1）与内点法（算法 5）；收敛速度以算法 2、4、5 最快。
- 仿真中五种算法收敛到同一最优解与同一组指力；HKUST 三指手实验用[[指尖力传感器]]闭环，验证物体轨迹跟踪。

## 🔗 关联
- [[Grasping Force Optimization for Multi-Fingered Robot Hands]]
- [[Grasping Force Optimization Approaches for Anthropomorphic Hands]]
- [[On the Closure Properties of Robotic Grasping]]

## 🏷️ 标签
#抓取力优化 #摩擦锥 #收敛性分析 #实时计算
