---
title: "GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping"
year: 2020
doi: 
arxiv: 
key: KB-047
venue: IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2020, 11144-11153
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取检测, 数据集, 基准评测, 点云, 抓取位姿]
pdf: ../../../Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf
confidence: high
source: pdf
aliases: [GraspNet-1Billion]
---

# GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

## 📌 年份
2020（CVPR 2020，pp. 11144–11153）

## 🔑 论文识别码
CVPR 2020 会议论文（无数值 DOI；本地编号 KB-047）

## 👥 作者与所属院校
- 作者：Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu
- 机构：上海交通大学

## 📖 研究背景
- 杂乱场景物体抓取是视觉与机器人的基础难题，训练数据不足与评测基准缺失长期制约进展。
- 人工标注[[抓取位姿]]代价高、规模小且稀疏；仿真数据虽可批量生成，但存在视觉域差。
- 矩形框与 6D 位姿两类表示各有指标，方法之间难以统一比较，真机评测成本又过高。

## ❓ 需要解决的问题
- 能否用解析计算替代逐位姿人工标注，获得与真实传感器对齐的稠密抓取真值？
- 能否用同一套指标评测矩形、6D 等不同表示的抓取候选？
- 端到端点云网络能否把逼近方向与操作参数解耦学习，并借亲和场提升鲁棒性？

## 📥📤 输入与输出
- 输入：场景 RGB-D 图像与点云（训练时每场景随机采样 20k 点）、物体 6D 位姿标注。
- 输出：逐点抓取位姿（逼近向量、平面内旋转、抓取宽度与操作参数）、抓取置信度与抓取亲和场。

## ✅ 论文最终达到的效果
- 数据集含 97,280 张 RGB-D 图像、190 个杂乱场景、88 类物体、超 11 亿抓取位姿，规模比此前数据集大约 5 个数量级。
- 采用 RealSense 与 Kinect 双相机采集，物体级标注加解析投影，兼顾稠密标注与真实视觉一致性。
- 在 Seen/Unseen/Novel 三档划分上 AP 分别为 27.56/29.88、26.11/27.84、10.55/11.51（RealSense/Kinect），全面优于 GPD（22.87）与 Liang 等（25.96）。
- 消融：移除亲和场 AP 由 29.88 降至 28.53，分类头换回归降至 23.74，验证两项设计有效。

## 🔗 关联
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#数据集 #抓取检测 #点云 #基准评测
