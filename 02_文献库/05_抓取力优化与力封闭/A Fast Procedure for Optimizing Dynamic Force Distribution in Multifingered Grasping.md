---
title: A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping
year: 2006
doi: 10.1109/TSMCB.2006.879015
arxiv: 
key: KB-019
venue: IEEE Transactions on Systems, Man, and Cybernetics—Part B: Cybernetics
theme: 02_文献库/05_抓取力优化与力封闭
tags: [动态力分配, 线性规划, 多指抓取, 实时计算]
pdf: ../../../A_Fast_Procedure_for_Optimizing_Dynamic_Force_Distribution_in_Multifingered_Grasping.pdf
confidence: high
source: pdf
aliases: []
---

# A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping

## 📌 年份
2006

## 🔑 论文识别码
DOI: 10.1109/TSMCB.2006.879015

## 👥 作者与所属院校
- 作者：Yu Zheng、Wen-Han Qian
- 机构：上海交通大学（待核对）

## 📖 研究背景
- 多指手动态操作时必须实时求出接触力，以平衡随运动不断变化的外部力旋量（external wrench）。
- 已有动态力分配（dynamic force distribution, DFD）算法分两类：一类坚持最优性但计算量大，一类牺牲最优性换速度。
- 两阶段（离线＋在线）思路的难点在于：外力连续变化导致最优接触力也在变，难以真正减少在线计算量。
- 本文切入角度：抓取构型固定时，线性规划的可行域多面体不随外力改变，只有最优顶点在移动。

## ❓ 需要解决的问题
- 能否在不损失最优性的前提下，把 DFD 降到实时可用的计算量级？
- 如何把「法向力分量之和最小」这一准则严格转成可快速求解的线性规划？
- 外力方向连续变化时最优解是否只在相邻顶点间跳转，从而可用邻接搜索替代全局求解？
- 离线阶段需要预计算哪些量（顶点集合、顶点邻接关系），才能保证在线搜索不丢最优性？

## 📥📤 输入与输出
- 输入：抓取构型（各接触点位置、单位内法线、摩擦系数、各指力上界）与在线测得的动态外部力旋量 w_ext(t)。
- 输出：使法向力分量之和最小的各指[[接触力分配]]结果，接触约束按[[摩擦锥]]线性化为多面锥处理。

## ✅ 论文最终达到的效果
- 目标函数化为动态外力旋量与某向量的内积，约束为一组线性不等式并定义多面体，最优解必在「解顶点」取得。
- 离线算出全部顶点及邻接表；在线只从上一时刻顶点沿邻接爬升，实测 CPU 时间约为单纯形法的 1/1000。
- 茶壶算例：四指抓取可行域 861 个顶点，五指 1618 个顶点；单顶点至多 13 条邻接，多数仅 6 条。
- 外力周期 5 s、采样间隔 5 ms（每周期 1000 点）时，在线计算远低于采样间隔，可满足实时控制。
- 离线计算不含外力，故外力可实时由传感器获取，也适用于非完整（nonholonomic）情形。

## 🔗 关联
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation]]
- [[Calculation of Robot Multi-Fingered Grasping Force and Displacement Based on the Newton–Subgradient Non-Smooth Greedy Randomized Kaczmarz Method for Solving Linear Complementarity Problem]]

## 🏷️ 标签
#抓取力优化 #接触力分配 #线性规划 #多指抓取
