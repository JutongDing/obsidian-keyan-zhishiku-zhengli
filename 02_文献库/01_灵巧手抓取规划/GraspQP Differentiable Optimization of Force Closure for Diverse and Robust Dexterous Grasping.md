---
title: "GraspQP: Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping"
year: 2025
doi: 
arxiv: 2508.15002
key: KB-063
venue: arXiv 预印本（cs.RO）
theme: 02_文献库/01_灵巧手抓取规划
tags: [力封闭, 可微优化, 抓取数据集, 抓取多样性, MALA]
pdf: ../../../GraspQP.pdf
confidence: high
source: pdf
aliases: [GraspQP]
---

# GraspQP: Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2508.15002（预印本，无 DOI）

## 👥 作者与所属院校
- 作者：René Zurbrügg、Andrei Cramariuc、Marco Hutter
- 机构：苏黎世联邦理工学院（ETH Zürich）及 ETH AI Center

## 📖 研究背景
- 训练抓取预测模型、操作策略与任务规划都依赖大规模、高质量的[[抓取位姿]]数据。
- 采样法与简化力闭合分析效率低、且易收敛到单一的 power grasp，抓取类型与手型多样性不足。
- 近期梯度法用可微但松弛的[[抓取质量]]指标，常忽略摩擦力等物理要素，牺牲真实性与多样性。
- 本文切入：把[[力封闭]]写成隐式[[二次规划]]约束下的可微能量项，并用改进采样器 MALA* 抑制模式坍塌。

## ❓ 需要解决的问题
- 如何在保持严格力闭合物理含义的同时，得到对抓取姿态完全可微的能量函数？
- 优化过程如何避免所有样本塌缩到同一类抓取，从而提升关节熵与唯一抓取率？
- 同一套方法能否覆盖 Shadow、Allegro、Ability 等不同[[灵巧手]]以及 pinch、precision 等抓取类型？
- 相比 DexGraspNet、GenDexGrasp、TDG 等基线，多样性与稳定性提升多少、代价多大？

## 📥📤 输入与输出
- 输入：物体网格/点云（DexGraspNet 5,700 个物体）、手模型与抓取类型、初始粗略抓取候选。
- 输出：多组满足力闭合的抓取姿态（腕部位姿 + 关节角），以及大规模抓取数据集标注。

## ✅ 论文最终达到的效果
- 5 N 扰动、50 物体测试集、12 接触点设置下总体唯一抓取率 52%，优于 GenDexGrasp 与 TDG 的 45%、DexGraspNet 的 40%。
- 分手上：Allegro 76%、Shadow 63%、Robotiq 3F 57%、Ability 35%；4 接触点设置总体 45%。
- MALA* 相对 MALA 提升唯一抓取率 +7.0%（GenDexGrasp 式能量）与 +5.0%（TDG 式能量）。
- 消融：去掉动态重置降 4.8%，去掉温度缩放降 4.5%，改无约束形式降约 10%。
- 发布含 5 种夹爪、3 类抓取类型的数据集；Robotiq 2F140 原始成功率仍 >80%；单次抓取 3.4 s（Shadow 24 自由度，基线 1.15 s），定位离线数据生成。

## 🔗 关联
- [[Dexonomy Synthesizing All Dexterous Grasp Types in a Grasp Taxonomy]]
- [[GraspNet-1Billion A Large-Scale Benchmark for General Object Grasping]]
- [[D(R, O) Grasp A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping]]

## 🏷️ 标签
#力封闭 #可微优化 #抓取数据集 #抓取多样性 #二次规划
