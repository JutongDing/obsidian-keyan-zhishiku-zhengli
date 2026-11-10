---
title: "Grasp Force Optimization as a Bilinear Matrix Inequality Problem: A Deep Learning Approach"
year: 2025
doi: 10.1007/978-981-96-1158-4_25
arxiv: 
key: KB-058
venue: Lecture Notes in Mechanical Engineering（Springer）
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 双线性矩阵不等式, 深度学习, 力封闭]
pdf: ../../../Grasp Force Optimization as a Bilinear Matrix Inequality Problem_ A Deep Learning Approach.pdf
confidence: high
source: pdf
aliases: [Grasp Force Optimization as a Bilinear Matrix Inequality Problem A Deep Learning Approach]
---

# Grasp Force Optimization as a Bilinear Matrix Inequality Problem: A Deep Learning Approach

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.1007/978-981-96-1158-4_25

## 👥 作者与所属院校
- 作者：Hirakjyoti Basumatary、Daksh Adhar、Riddhiman Shaw、Shyamanta M. Hazarika
- 机构：印度理工学院古瓦哈提分校仿生机器人与人工智能实验室（BRAIL）、英国爱丁堡大学

## 📖 研究背景
- [[抓取力优化]]（GFO）要在力平衡与摩擦约束下求最优接触力，问题非凸，约束中含双线性项。
- 常规解法是通用梯度型非线性优化或半正定规划，计算重且对初值敏感。
- 生物拟态多指手依赖后验协同降维，其约束非光滑但凸，梯度法难以直接套用。
- 本文切入：把多指抓取力分析写成双线性矩阵不等式（BMI）问题，再用神经网络求解以泛化到未见物体。

## ❓ 需要解决的问题
- 抓取力分析与[[力封闭]]条件能否严格表述为线性/双线性矩阵不等式？
- 借神经 ODE 式无约束化训练的网络，解是否满足[[摩擦锥]]、力平衡与关节力矩约束？
- 对训练中未出现过的物体与抓取配置，网络能否直接给出可行且最优的力分配？
- 所得解能否用抓取质量指标定量评价，而不只是可视化演示？

## 📥📤 输入与输出
- 输入：三指接触点位置、手部[[雅可比矩阵]]、期望外力旋量、摩擦与力平衡约束。
- 输出：各指各关节的力矩/接触力分量，即[[接触力分配]]解，以及对应的[[抓取质量]]指标。

## ✅ 论文最终达到的效果
- 用 (1,100,5) 的 tanh 网络，按常微分方程形式在 [0,10] 区间以 0.01 步长训练，1000 次迭代内损失收敛。
- 经典线性规划算例得 x=(0.999, 0.579, −0.228, 0.886)，与基准解一致。
- Barrett 三指手在 PyBullet/GraspIt 中完成满足摩擦锥的抓取，关节力矩约 −34.8 至 −40.8（原文未标单位，低置信待核对）。
- 以最大最小可抵抗旋量 q_lr^w 评价抓取，确认所得解满足力封闭条件。
- 属可行性验证：未与梯度法或半正定规划基线做定量对比，也无实物实验。

## 🔗 关联
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#抓取力优化 #双线性矩阵不等式 #深度学习 #力封闭
