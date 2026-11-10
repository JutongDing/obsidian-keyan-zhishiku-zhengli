---
title: "GraspNet: A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping"
year: 2019
doi: 
arxiv: 1912.13470
key: KB-062
venue: 待补（arXiv 预印本）
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取位姿检测, 数据集与基准, 力封闭, 杂乱场景]
pdf: ../../../GraspNet.pdf
confidence: high
source: pdf
aliases: []
---

# GraspNet: A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping

## 📌 年份
2019

## 🔑 论文识别码
arXiv:1912.13470

## 👥 作者与所属院校
- 作者：Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu
- 机构：上海交通大学

## 📖 研究背景
- 杂乱堆叠场景的 [[抓取位姿]] 检测缺少大规模、稠密标注的数据与统一基准。
- 人工标注规模小且稀疏；纯仿真生成百万级位姿又存在视觉域差，迁移到真机性能下降。
- 抓取表示不统一（矩形框 vs 6D 位姿）导致各方法指标各异、难以横向比较。

## ❓ 需要解决的问题
- 如何在真实传感器采集的场景图像上，稠密标注百万级 6D 抓取位姿而不逐条人工标注？
- 能否用一个解析判据在线评测任意表示形式的抓取，而不预存测试集真值？
- 数据集给出的抓取质量评分，是否与真机抓取成功率一致？

## 📥📤 输入与输出
- 输入：真实场景 RGB-D 图像（Kinect 4 Azure 与 RealSense 435 由机械臂重复轨迹采集）、物体 6D 位姿、物体三维网格。
- 输出：每个场景约 150 万–250 万条 6D 抓取位姿及 [[力封闭]] 评分；另附矩形抓取、实例掩码、包围盒、相机位姿与多视角点云。

## ✅ 论文最终达到的效果
- 覆盖 88 个物体（32 个 YCB + 13 个 DexNet 对抗物体 + 43 个自采）、170 个杂乱场景、每场景 512 帧，共 87,040 张 RGB-D 图像。
- 抓取位姿总数超过 3.7 亿，比此前数据集大三个数量级；正负样本比约 1:2。
- 评测采用 Precision@k（k ≤ 50）、在摩擦系数 μ = 0.1–0.5 上取 AP，NMS 阈值 1 cm / 5°。
- 真机（Flexiv Rizon + RealSense 435）10 个物体各 100 次：高评分抓取平均成功率约 0.96，评分 s = 0.1 时仅 5%–23%。
- 数据集、代码与模型公开。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#抓取位姿检测 #数据集 #基准评测 #力封闭
