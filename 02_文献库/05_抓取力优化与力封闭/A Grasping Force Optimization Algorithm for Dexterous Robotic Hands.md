---
title: A Grasping Force Optimization Algorithm for Dexterous Robotic Hands
year: 2012
doi: 
arxiv: 
key: KB-007
venue: 2012 IEEE International Conference on Robotics and Automation (ICRA), Saint Paul, MN, USA
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 力封闭, 凸优化, 双臂操作, 实时性]
pdf: ../../../A Grasping Force Optimization Algorithm for Dexterous Robotic Hands.pdf
confidence: high
source: pdf
aliases: []
---

# A Grasping Force Optimization Algorithm for Dexterous Robotic Hands

## 📌 年份
2012

## 🔑 论文识别码
KB-007（本地编号，原文无 DOI/arXiv）；ICRA 2012, pp. 4170-4175

## 👥 作者与所属院校
- 作者：Vincenzo Lippiello, Bruno Siciliano, Luigi Villani
- 机构：那不勒斯费德里科二世大学（PRISMA Lab，据作者团队常规署名，待核对）

## 📖 研究背景
- 多指手控制需在线求解[[抓取力优化]]问题，保证[[力封闭]]与可行性，同时抵御外部扰动。
- 约束与目标均非线性、变量规模大，且抓取构型与负载旋量随时间变化。
- 已有方法用 LMI 或线性化[[摩擦锥]]处理，但引入关节力矩上限后复杂度随关节数超二次增长；双臂系统更甚。

## ❓ 需要解决的问题
- 含关节力矩约束的抓取力优化能否写成凸优化并在线求解？
- 能否依据上一采样时刻的力矩裕度动态裁剪有效力矩约束，以降低计算量？
- 双臂情形用单臂次优分解，能否在不破坏可行性的前提下换取实时性？

## 📥📤 输入与输出
- 输入：[[抓取矩阵]]、接触点位置与法向、摩擦系数、关节力矩上下限、目标负载旋量、手部雅可比。
- 输出：各接触点接触力与[[内力]]、关节力矩、有效约束集合与单步计算时间。

## ✅ 论文最终达到的效果
- 以紧凑摩擦锥表示 + 凸优化 + 障碍函数，统一处理摩擦锥与关节力矩上下限约束。
- 力矩约束动态激活（阈值 στ）：平均计算时间较全约束下降 30%（στ=0）至 90%（στ=0.8）。
- 全约束基准为 23 ms（Intel Pentium IV 2.8 GHz）；στ=0.5 满足 10 ms 实时要求，στ=0.8 满足 2 ms 理想要求。
- 加入力矩约束后接触旋量范数更小、负载在手指间更均衡，关节力矩全程不越限（负值区消除）。
- 双臂场景（两只 DEXMART 手倒水，旋转 135°）验证：单臂分解+加权伪逆进一步降计算量，但解为次优。

## 🔗 关联
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]
- [[A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation]]
- [[Calculation of Robot Multi-Fingered Grasping Force and Displacement Based on the Newton–Subgradient Non-Smooth Greedy Randomized Kaczmarz Method for Solving Linear Complementarity Problem]]

## 🏷️ 标签
#抓取力优化 #力封闭 #凸优化 #双臂协同 #实时控制
