---
title: Real-Time Force Regulation for Whole-Hand Dexterous Grasping
year: 2026
doi: 
arxiv: 2609.30082
key: KB-117
venue: arXiv 预印本（会议/期刊待补）
theme: 02_文献库/05_抓取力优化与力封闭
tags: [全手接触, 实时力调节, 二次规划, 重抓取]
pdf: ../../../Real-Time Force Regulation for Whole-Hand Dexterous Grasping.pdf
confidence: high
source: pdf
aliases: []
---

# Real-Time Force Regulation for Whole-Hand Dexterous Grasping

## 📌 年份
2026

## 🔑 论文识别码
arXiv: 2609.30082

## 👥 作者与所属院校
- 作者：Sang Min Kim、Alexander Alexiev、Tzu-Yuan Lin、Sangbae Kim、Young Min Kim 等
- 机构：首尔国立大学、麻省理工学院、延世大学

## 📖 研究背景
- 稳健的[[灵巧手]]抓取不只靠生成抓取位姿，还要在接触不断变化时维持物理稳定。
- 规划位姿难以精确复现：位置误差、控制误差、闭合过程推挤与后续扰动，使接触位置、法向甚至数量持续变化，预计算的力分配迅速失效。
- 现有反应式抓取控制器多只考虑指尖接触，因为触觉阵列常装在那里；全手未instrumented表面（指侧、指背、掌心）覆盖困难。
- 本文切入角度：用被跟踪的物体模型加本体感知几何地估计全手接触，绕开触觉覆盖问题。

## ❓ 需要解决的问题
- 不依赖接触处触觉传感，能否从物体位姿与关节角实时估计全手接触位置与法向？
- 接触集合动态增删时，如何在摩擦约束、执行器限幅与「驱动一致性」约束下反复重算期望接触力？
- 全手接触相比仅指尖接触带来多少成功率增益，执行一致性约束是否必要？
- 该力调节器与反应式接近控制能否串成从接近、抓取、受扰保持到掉落重抓的完整闭环？

## 📥📤 输入与输出
- 输入：被跟踪物体的 6-DoF 位姿（30 Hz，Gaussian 渲染替代 FoundationPose 渲染器）、各关节角、手部连杆网格与物体网格/SDF。
- 输出：全手各接触点的期望接触力，经[[接触力分配]]转为关节力矩指令（QP 求解）。

## ✅ 论文最终达到的效果
- 仿真：79 个 YCB 物体上 790 个 power grasp 做六方向负载测试；全手力调节在各接触数分箱均优于前馈与仅指尖阻抗两类基线。
- 位置偏置 30°、5 mm、接触阈值 1 cm 时成功率 93%；阈值过小（0.5 cm）或过大（2 cm）均变差。
- 接触点数与成功率正相关，约三分之一抓取含 5 个以上接触；加入执行一致性约束后接触力更接近期望、质心净力近零。
- 接触采样数 K=5 时成功率最高（93.2%），计算频率随 K 由 227 Hz 降到 66 Hz，仍满足实时。
- 实物 27 自由度平台（7 自由度 Flexiv Rizon 4 臂 + 20 自由度 Robotis 5F 手）约 200 s 内施加 78 次人为扰动，丢物 8 次，其中 6 次自动回到接近并重抓；全程不使用触觉传感器。

## 🔗 关联
- [[Real-Time Grasping-Force Optimization for Multifingered Manipulation Theory and Experiments]]
- [[Rigidity-Based Multi-Finger Coordination for Precise In-Hand Manipulation of Force-Sensitive Objects]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#接触力分配 #二次规划 #全手接触 #实时力调节 #重抓取
