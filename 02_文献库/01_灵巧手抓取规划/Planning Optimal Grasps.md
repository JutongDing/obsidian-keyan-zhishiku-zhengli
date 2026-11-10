---
title: Planning Optimal Grasps
year: 1992
doi: 
arxiv: 
key: KB-111
venue: IEEE International Conference on Robotics and Automation (ICRA) 1992, pp.2290–2295
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取质量, 抓取规划, 力封闭, 凸包, 度量]
pdf: ../../../Planning Optimal Grasps.pdf
confidence: high
source: pdf
aliases: []
---

# Planning Optimal Grasps

## 📌 年份
1992

## 🔑 论文识别码
无 DOI（ICRA 1992，页码 2290–2295 见页脚；本地编号 KB-111）

## 👥 作者与所属院校
- 作者：Carlo Ferrari、John Canny
- 机构：加州大学伯克利分校电子工程与计算机科学系

## 📖 研究背景
- 选夹爪、定[[抓取位姿]]都需要能量化「这个抓取好不好」，但[[力封闭]]判据只给是/否，缺少连续的质量度量。
- 实际夹爪受执行器电流与力矩限制：总指力决定功耗，最大指力决定峰值负载。
- 该文用广义力空间的不同范数把两种限制统一为两套质量准则，并给出几何解释与规划算法。

## ❓ 需要解决的问题
- 「总指力最小」与「最大指力最小」两种准则如何形式化，才能在任意机构上计算？
- 不同度量（L1、L∞）如何改变准则含义，能否用一个几何对象统一解释？
- 对两爪与三爪夹爪抓平面多边形，能否设计出高效的最优抓取规划算法？

## 📥📤 输入与输出
- 输入：物体多边形几何、夹爪类型与几何、接触点位置、[[摩擦锥]]与接触模型。
- 输出：[[抓取质量]]值 Q（各方向可施加 wrench 的下界）、最优抓取构型及规划结果。

## ✅ 论文最终达到的效果
- 用 L∞ 度量得「最大指力最小」准则，用 L1 度量得「总指力最小」准则，后者对应电机与功放电流最小化。
- Q 被定义为所有 wrench 方向上的最坏情况「wrench/指力」比值；几何上等于包含原点的最大球半径，即凸包最近面到原点的距离。
- 质量只与点和凸包有关，与 wrench 幅值无关，因而可在 wrench 空间用 Minkowski 和与凸包高效计算。
- 两爪抓多边形的规划算法复杂度 O(n)（n 为边数），三爪需处理点-边、边-边等接触组合；两准则的最优抓取可能并不一致。

## 🔗 关联
- [[GraspQP Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping]]
- [[On the Form-Closure Property of Robotic Grasping]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#抓取质量 #抓取规划 #力封闭 #凸包
