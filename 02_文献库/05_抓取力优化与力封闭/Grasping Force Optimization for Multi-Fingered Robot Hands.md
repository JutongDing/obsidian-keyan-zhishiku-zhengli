---
title: Grasping Force Optimization for Multi-Fingered Robot Hands
year: 1995
doi: 
arxiv: 
key: KB-066
venue: IEEE International Conference on Robotics and Automation (ICRA)
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 半正定规划, 梯度流, 摩擦锥, 内力]
pdf: ../../../Grasping Force Optimization for Multi-Fingered Robot Hands.pdf
confidence: medium
source: pdf
aliases: []
---

# Grasping Force Optimization for Multi-Fingered Robot Hands

## 📌 年份
1995（ICRA 1995，第 1034–1039 页；OCR 扫描件）

## 🔑 论文识别码
DOI: 无（1995 年会议论文，本地编号 KB-066）

## 👥 作者与所属院校
- 作者：Martin Buss、Hideki Hashimoto、John B. Moore
- 机构：东京大学生产技术研究所、慕尼黑工业大学自动控制系、澳大利亚国立大学系统工程系

## 📖 研究背景
- 多指手抓取要同时平衡外力与[[内力]]，既保证稳定又尽量省力。
- 早期做法把库仑[[摩擦锥]]线性化为多面锥，用单纯形与线性规划求解，摩擦系数被迫取保守值。
- 该文把非线性摩擦约束写成矩阵正定条件，用梯度流求全局收敛解。

## ❓ 需要解决的问题
- 每个接触点的非线性摩擦约束，能否等价表示为含接触旋量强度与摩擦系数的矩阵正定？
- 外力平衡等式能否与摩擦不等式一起化为对该矩阵的仿射线性约束？
- 正定矩阵流形上的梯度流是否全局指数收敛，能否给出递推在线版本？

## 📥📤 输入与输出
- 输入：各接触点位置与法向（接触坐标系）、摩擦系数、被抓物体所受外力和力矩。
- 输出：各接触点的接触力（法向与切向分量），即满足力平衡与摩擦约束的内力分配结果。

## ✅ 论文最终达到的效果
- 构造矩阵 P 含接触旋量与摩擦系数，摩擦约束等价于 P 正定，避免线性化带来的保守性。
- 外力平衡与摩擦约束合并成对 P 的仿射线性约束，问题化为线性约束半正定规划。
- 梯度流在正定矩阵上迭代，理论保证全局指数收敛；给出递推（在线）版本。
- 数值例子表明实现简单、数值性质好并收敛到最优解；步长系数 α 需按经验选取。

## 🔗 关联
- [[Grasping Force Optimization Approaches for Anthropomorphic Hands]]
- [[Grasping Force Optimization Algorithm of Soft Multi-fingered Hand Based on Safety Margin Detection]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#抓取力优化 #半正定规划 #梯度流 #摩擦锥
