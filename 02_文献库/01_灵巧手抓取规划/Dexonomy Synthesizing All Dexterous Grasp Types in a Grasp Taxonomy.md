---
title: "Dexonomy: Synthesizing All Dexterous Grasp Types in a Grasp Taxonomy"
year: 2025
doi: 
arxiv: 2504.18829
key: KB-039
venue: arXiv preprint (cs.RO)
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取合成, 抓取分类学, 大规模抓取数据集, 接触感知控制]
pdf: ../../../Dexonomy.pdf
confidence: high
source: pdf
aliases: []
---

# Dexonomy: Synthesizing All Dexterous Grasp Types in a Grasp Taxonomy

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2504.18829（无 DOI）

## 👥 作者与所属院校
- 作者：Jiayi Chen, Yubin Ke, Lin Peng, He Wang（前两位共同一作）
- 机构：北京大学、Galbot、北京通用人工智能研究院（BAAI）

## 📖 研究背景
- 通用灵巧抓取不仅要求抓得住，还要求抓取类型合适；但覆盖 GRASP 分类学的多类型抓取数据极难采集。
- 现有自动抓取合成多为类型无关（type-unaware），只追求稳定，手退化成大号平行夹爪；类型感知方法又常受限于特定物体或轴对齐假设。
- 该文以每种手、每种抓取类型仅一张人工标注模板为起点，用"整体对齐 + 局部细化"两阶段合成任意类型抓取。

## ❓ 需要解决的问题
- 如何为任意抓取类型、任意物体、任意多指手合成接触丰富、无穿透、物理可行的抓取？
- 如何在贴近模板意图的同时保证手-物不穿透并满足 [[力封闭]]，且超参数可跨类型共享？
- 如何用接触感知控制策略在仿真中验证抓取并施加合适接触力？
- 合成的大规模数据能否训练类型条件生成模型，从单视角点云为指定类型生成抓取？

## 📥📤 输入与输出
- 输入：单张人工标注抓取模板（初始手位姿与接触点/法向信息）、物体网格或单视角点云、关节手模型。
- 输出：预抓取、抓取、挤压三段位姿序列，各接触点接触力（经 [[雅可比矩阵]] 转关节力矩），以及 9.5M 抓取数据集与类型条件抓取生成策略。

## ✅ 论文最终达到的效果
- 构建数据集含 10.7k 物体、9.5M 抓取，覆盖 GRASP 分类学 31 种抓取类型（33 类中 2 类被弃用）。
- 优化阶段每次约 1.2 s；以批量可微 [[二次规划]]（Relu-QP）求力，局部细化 200 步、不足 0.1 s。
- 局部细化在 32 线程下可达每秒 200 个以上抓取；仿真验证约 3000 步/抓取，48 线程约 40 个/秒，成为流程瓶颈。
- 真实实验中 Shadow 手仅凭单视角点云、按指定类型抓取新物体，成功率 82.3%。
- 验证后的抓取还可回填为新模板，扩展模板库。

## 🔗 关联
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#抓取合成 #抓取分类学 #大规模数据集 #接触感知控制
