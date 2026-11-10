---
title: "CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty"
year: 2024
doi: 
arxiv: 2412.16490
key: KB-033
venue: 待补（arXiv 预印本）
theme: 02_文献库/01_灵巧手抓取规划
tags: [灵巧手抓取, 触觉反馈控制, 接触力分配, MPC]
pdf: ../../../CoorGrasp.pdf
confidence: high
source: pdf
aliases: []
---

# CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty

## 📌 年份
2024

## 🔑 论文识别码
arXiv:2412.16490

## 👥 作者与所属院校
- 作者：Mingrui Yu, Yongpeng Jiang, Yongyi Jia, Xiang Li（通讯）
- 机构：清华大学自动化系、北京信息科学与技术国家研究中心

## 📖 研究背景
- 灵巧抓取研究大多集中在 [[抓取位姿]] 生成，而「把规划好的抓取真正执行出来」被忽视。
- 在形状不确定、位置不确定与生成误差下，开环执行会出现多接触不协调，造成物体 [[手内操作]] 位移甚至抓取失败。
- 现有触觉反馈方法把接近与抓取分成两段：先位置控制找接触、再力控制加力，切段处容易失配。

## ❓ 需要解决的问题
- 能否在接近与抓取两个阶段同时维持多指接触力均衡，而不是分包处理？
- 手臂运动能否用来补偿物体位置误差，减少纯手指调节带来的扰动？
- 加力过程中如何做到各接触 [[接触力分配]] 均衡，避免单侧过载推动物体？

## 📥📤 输入与输出
- 输入：已规划的抓取位姿、指尖 [[视触觉传感器]] 估计的接触位置与接触力、物体位姿观测（含不确定度）。
- 输出：10 Hz 的关节动作指令与各接触期望力；解析模型把接触力映射到关节运动，交给低层高频执行。

## ✅ 论文最终达到的效果
- 仿真覆盖 15k 次抓取、478 个物体、Shadow / Allegro / LEAP 三种手。
- 真机 UR5 + LEAP Hand、8 种物体：抬升前物体位置误差 3.1±2.4 mm，开环为 8.5±4.6 mm；归一化力旋量 0.40，开环 0.57。
- 力不平衡的基线即使成功率不低，物体位移仍可能大于开环执行。
- MPC 单次求解约 30 ms（i9-13900K），满足 10 Hz 闭环。
- 方法对抓取类型与接触构型无限制，可直接接在现有抓取生成方法之后。

## 🔗 关联
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[A Mathematical Introduction to Robotic Manipulation]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#灵巧手抓取 #触觉反馈 #接触协调 #MPC
