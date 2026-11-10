---
title: Recursive Algorithms for Real-Time Grasping Force Optimization
year: 1997
doi: 
arxiv: 
key: KB-119
venue: Proceedings of the 1997 IEEE International Conference on Robotics and Automation (ICRA), Albuquerque
theme: 02_文献库/05_抓取力优化与力封闭
tags: [半定规划, Dikin 算法, 递归优化, 摩擦锥]
pdf: ../../../Recursive Algorithms for Real-Time Grasping Force Optimization.pdf
confidence: high
source: pdf
aliases: []
---

# Recursive Algorithms for Real-Time Grasping Force Optimization

## 📌 年份
1997

## 🔑 论文识别码
KB-119（本地编号；原文无 DOI 与 arXiv 号）

## 👥 作者与所属院校
- 作者：Martin Buss、Leonid Faybusovich、John B. Moore
- 机构：慕尼黑工业大学、美国圣母大学、澳大利亚国立大学

## 📖 研究背景
- 灵巧手抓取时外力必须由接触力平衡，冗余自由度使问题变成在非线性摩擦稳定约束下最小化抓取代价。
- 早期做法把[[摩擦锥]]线性化后用单纯形法求解，但线性化会把可行域放大，算出的力可能不满足真实摩擦约束。
- 启发式与非线性规划方法则存在局部极小与抓取力跳变问题；且当时多数方法只能离线运行。
- 本文切入角度：沿用内点法思路，把[[抓取力优化]]重写为带仿射约束的半定规划（semidefinite program）。

## ❓ 需要解决的问题
- 非线性摩擦力上限约束能否等价写成矩阵正定的线性约束，从而进入半定规划框架？
- 在严格凸、含障碍项的代价函数族下，哪种递推格式能保证收敛到唯一最优解且数值稳定？
- 如何避免梯度法对步长的敏感，构造自洽（self-concordant）障碍与 Dikin 型递推？
- 单次迭代的计算量能否支撑实时（毫秒级）在线指力计算？

## 📥📤 输入与输出
- 输入：外力旋量、接触几何与[[抓取矩阵]]、摩擦系数、代价权重矩阵，以及满足约束的初始正定矩阵。
- 输出：各指最优接触力（对应正定矩阵的分解结果）及其随时间的递推更新序列。

## ✅ 论文最终达到的效果
- 证明摩擦锥约束等价于某对称矩阵正定，外力补偿也是该矩阵上的线性约束，故原问题化为仿射约束半定规划。
- 给出三类梯度流（标准黎曼度量、逆障碍幂度量）及两种递推实现（欧氏梯度与 Dikin 型），均证明指数收敛到唯一解。
- 四指矩形物体算例（点接触带摩擦，μ=0.4）：三种度量分别用 46、27、40 个积分步收敛。
- 同一算例在 SUN SPARCstation 20 上以 MATLAB 运行，耗时分别约 9 s、38 s、60 s，说明度量选择对数值性质影响显著。
- 递推版在 MC 68040（25 MHz）上单次优化计算约 5 ms，具备在线实时能力；三指时系统矩阵维度为 78（原文参数符号抽取不清，低置信，待核对）。

## 🔗 关联
- [[Real-Time Grasping-Force Optimization for Multifingered Manipulation Theory and Experiments]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]

## 🏷️ 标签
#抓取力优化 #半定规划 #内点法 #摩擦锥 #实时计算
