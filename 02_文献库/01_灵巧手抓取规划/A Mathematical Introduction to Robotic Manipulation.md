---
title: A Mathematical Introduction to Robotic Manipulation
year: 1994
doi: 
arxiv: 
key: KB-009
venue: CRC Press（专著/研究生教材）
theme: 02_文献库/01_灵巧手抓取规划
tags: [旋量理论, 李群, 多指手运动学, 力封闭, 非完整系统]
pdf: ../../../A Mathematical Introduction to Robotic Manipulation.pdf
confidence: high
source: pdf
aliases: [MLS94]
---

# A Mathematical Introduction to Robotic Manipulation

## 📌 年份
1994

## 🔑 论文识别码
KB-009（本地编号；CRC Press 专著，ISBN 9780849379819，原文未给 DOI）

## 👥 作者与所属院校
- 作者：Richard M. Murray, Zexiang Li, S. Shankar Sastry
- 机构：加州理工学院、香港科技大学、加州大学伯克利分校

## 📖 研究背景
- 多指手操作缺少统一数学语言：位形、速度、力与接触约束需在同一几何框架下表述。
- 该书以旋量（screw）与李群/李代数统一刚体运动、运动学、动力学与抓取静力学。
- 是[[力封闭]]、[[抓取矩阵]]与[[腱驱动]]手指分析的经典教科书来源，被后续灵巧手文献反复引用。

## ❓ 需要解决的问题
- 如何用指数坐标与旋量统一描述刚体变换、正运动学与速度/力对偶关系？
- 多指抓取的静力平衡、力封闭条件与抓取约束如何形式化并给出构造性判据？
- 含约束的动力学、冗余与非可操作抓取、弹性腱驱动如何建模与控制？

## 📥📤 输入与输出
- 输入：连杆几何与关节变量、接触模型参数、目标物体位姿与期望接触力。
- 输出：正/[[逆运动学]]映射、[[雅可比矩阵]]、抓取矩阵与力封闭判据、手部动力学方程与分层控制律。

## ✅ 论文最终达到的效果
- 全书 8 章（PDF 共 474 页）：刚体运动、操作臂运动学、动力学与控制、多指手运动学、手动力学与控制、非完整系统及其规划。
- 第 5 章给出抓取静力学、抓取映射、力封闭的构造性条件与所需最少接触点数界，并讨论[[抓取规划]]。
- 第 6 章给出含约束 Lagrange 方程、[[内力]]分解、腱驱动（弹性/非弹性）静力学与分层控制结构。
- 第 5、6 章还覆盖滚动接触运动学与冗余/非可操作抓取，是[[接触力分配]]推导的通用底座。
- 第 7–8 章用 Frobenius 定理与 Lie 括号讨论非完整可控性与运动规划，附习题与书目。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#旋量理论 #李群 #多指手运动学 #力封闭 #非完整系统
