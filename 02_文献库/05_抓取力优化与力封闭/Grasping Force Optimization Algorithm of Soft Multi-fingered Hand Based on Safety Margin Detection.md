---
title: Grasping Force Optimization Algorithm of Soft Multi-fingered Hand Based on Safety Margin Detection
year: 2017
doi: 10.13973/j.cnki.robot.2017.0844
arxiv: 
key: KB-068
venue: 机器人（ROBOT）
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 安全裕度, 梯度流, 软手指, 摩擦锥]
pdf: ../../../GraspingForceOptimizationAlgorithmofSoftMulti-fingeredHandBasedonSafetyMarginDetection.pdf
confidence: high
source: pdf
aliases: [基于安全裕度检测的软多指手抓取力优化算法]
---

# Grasping Force Optimization Algorithm of Soft Multi-fingered Hand Based on Safety Margin Detection

## 📌 年份
2017（第 39 卷第 6 期，844–852 页）

## 🔑 论文识别码
DOI: 10.13973/j.cnki.robot.2017.0844

## 👥 作者与所属院校
- 作者：王学林、肖永飞、赵永国、范新建
- 机构：山东省科学院自动化研究所机器人及制造自动化技术重点实验室（齐鲁工业大学）

## 📖 研究背景
- 多指手[[抓取力优化]]的关键是求出既平衡外力、又不让指端滑动的接触力。
- 经典梯度流算法必须先给定满足[[摩擦锥]]约束的合法初值，而现有初值方法无法保证全程不越界。
- 该文定义[[安全裕度]]并迭代生成安全初值，再交给梯度流优化。

## ❓ 需要解决的问题
- 如何用一个 0–100% 的标量直观度量接触点抓取力离摩擦锥边界的距离？
- 逐次提高期望安全裕度的迭代能否自动淘汰不可靠初值？
- 以安全初值作起点，软手指接触力在优化迭代中能否始终不越出摩擦锥？

## 📥📤 输入与输出
- 输入：四个软手指在球面上的接触点位置与法向/切向/扭转基、摩擦系数 μi=0.5 与 μt,i=0.3、重力旋量（球重 5 N）。
- 输出：软手指接触力向量（法向、两切向、扭转分量）的最优值，以及各接触点的安全裕度 ρi。

## ✅ 论文最终达到的效果
- 以半径 50 mm、重 5 N 球体为例，求安全初值迭代 65 次、耗时 0.0336 s。
- 裕度下限取 0 时，迭代到第 94 次后第 4 指 ρ4<0，说明接触会失效、原初值不可靠。
- 期望裕度提高到 20% 后，300 次迭代内四指裕度均大于 0（如 ρ1=0.4957），解全程合法。
- 改用安全初值后法向抓取力整体下降，切向与扭转分量随之自然优化，结果更可靠。

## 🔗 关联
- [[Grasping Force Optimization for Multi-Fingered Robot Hands]]
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#抓取力优化 #安全裕度 #梯度流 #软手指
