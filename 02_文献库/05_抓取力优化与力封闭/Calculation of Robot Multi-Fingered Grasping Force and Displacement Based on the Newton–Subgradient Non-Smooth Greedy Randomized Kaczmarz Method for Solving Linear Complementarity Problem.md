---
title: Calculation of Robot Multi-Fingered Grasping Force and Displacement Based on the Newton–Subgradient Non-Smooth Greedy Randomized Kaczmarz Method for Solving Linear Complementarity Problem
year: 2025
doi: 10.3390/s25072309
arxiv: 
key: KB-027
venue: Sensors (MDPI), 2025, 25: 2309
theme: 02_文献库/05_抓取力优化与力封闭
tags: [线性互补问题, 抓取力计算, 非光滑方程, Kaczmarz, 多指抓取]
pdf: ../../../Calculation of Robot Multi-Fingered Grasping Force and Displacement Based on the Newton–Subgradient Non-Smooth Greedy Randomized Kaczmarz Method for Solving Linear Complementarity Problem.pdf
confidence: high
source: pdf
aliases: []
---

# Calculation of Robot Multi-Fingered Grasping Force and Displacement Based on the Newton–Subgradient Non-Smooth Greedy Randomized Kaczmarz Method for Solving Linear Complementarity Problem

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.3390/s25072309

## 👥 作者与所属院校
- 作者：Zhiwei Ai, Chenliang Li（通讯）等
- 机构：桂林电子科技大学数学与计算科学学院、桂林航天工业学院人工智能学院、广西应用数学中心（GUET）

## 📖 研究背景
- 多指 [[灵巧手]] 的稳定抓取与滑移损伤分析，都要先算出各指抓取力与指端位移。
- 把 [[摩擦锥]] 线性化后，该问题可写成系数矩阵为鞍点结构的 [[线性互补问题]]（LCP）。
- 数值计算领域的 LCP 解法不适用于这种鞍点结构，Pivot 法又只能处理特定抓取构型。

## ❓ 需要解决的问题
- 如何把鞍点结构 LCP 转成可迭代的非光滑方程组，并给出收敛性保证？
- 能否不依赖枢轴旋转、也不解大型线性方程组，就同时得到抓取力与滑移位移？
- 方法对二维多指、三维三指/五指、不同多面体近似面数是否都成立？

## 📥📤 输入与输出
- 输入：接触点坐标、手指柔性系数、外部力旋量与力矩、摩擦锥多面体近似面数、初始零向量。
- 输出：各指抓取力、指端滑移位移、物体位移；收敛判据为残差 RES<10⁻⁵ 或迭代 20000 次。

## ✅ 论文最终达到的效果
- 提出牛顿–次梯度非光滑贪心随机 Kaczmarz 方法（NSNGRK），把 LCP 经 merit function 化为非光滑方程组，用次梯度构造广义 [[雅可比矩阵]]，收敛性有证明。
- 5 个数值算例覆盖二维六指、三维三指棱柱、1×1×1 立方体三指两种构型与五指立方体。
- 与 Pivot 法可解算例的结果一致到 10⁻⁶ 量级；算例 4、5 中 Pivot 法失效，NSNGRK 仍给出解。
- 多面体近似面数由 4、6、8 增至 16 时仍稳定收敛，对摩擦锥离散精度不敏感。
- 仅数值实验，尚无实物抓取验证（原文自述）。

## 🔗 关联
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]
- [[A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation]]

## 🏷️ 标签
#抓取力计算 #线性互补问题 #非光滑优化 #多指抓取
