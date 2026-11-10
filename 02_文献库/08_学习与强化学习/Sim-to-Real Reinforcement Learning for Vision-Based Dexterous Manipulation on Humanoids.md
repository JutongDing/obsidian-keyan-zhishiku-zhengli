---
title: Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids
year: 2025
doi: 
arxiv: 2502.20396
key: KB-131
venue: arXiv 预印本（待补）
theme: 02_文献库/08_学习与强化学习
tags: [仿真到现实迁移, 人形机器人, 灵巧操作, 扩散策略, 自动域随机化, 蒸馏]
pdf: ../../../Sim-to-Real Reinforcement Learning.pdf
confidence: high
source: pdf
aliases: []
---

# Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids

## 📌 年份
2025

## 🔑 论文识别码
arXiv: 2502.20396（无 DOI）

## 👥 作者与所属院校
- 作者：Toru Lin, Kartik Sachdev, Linxi "Jim" Fan, Jitendra Malik, Yuke Zhu
- 机构：UC Berkeley、NVIDIA、UT Austin

## 📖 研究背景
- 人形[[灵巧手]]的接触丰富操作自由度多、时序长，[[强化学习]]在真实世界几乎无法直接训练。
- 仿真训练再迁移长期受三类误差夹击：物理建模偏差、视觉感知差距、稀疏奖励下的探索困难。
- 该文以 Fourier GR-1 人形本体加两款多指手为平台，把一套可复用的 sim-to-real 流程逐项拆开验证。

## ❓ 需要解决的问题
- 能否用自动化的 real-to-sim 调参模块替代人工试凑，稳定提高迁移成功率？
- 抓取、抬起、双臂交接这类长时序接触任务，如何写出可复用而不逐任务手调的奖励？
- 稀疏奖励下如何提升样本效率，同时不牺牲最终迁移性能？
- 视觉侧的渲染与现实差距，能否靠稀疏加稠密的混合物体表示来弥合？

## 📥📤 输入与输出
- 输入：第三人称与自我中心两路 RGB-D 图像、双臂与双手关节角/角速度等本体状态、任务指令。
- 输出：双臂 7 DoF 与双手 6 DoF 的绝对期望关节位置（由扩散策略给出），部署时以 5 Hz 下发。

## ✅ 论文最终达到的效果
- 四项技术：自动 real-to-sim 调参、通用奖励设计、分治蒸馏、稀疏+稠密混合物体表示。
- 真实世界成功率：抓取-伸取 62.3%、抬箱 80%、双臂交接 52.5%。
- 有人类姿态初始化时抓取/抬起/交接为 80%/90%/30%；无初始化时交接为 0%。
- 单项随机化中仅质量扰动迁移最好（90.0%），形状 63.3%、尺寸 40.0%、全随机 23.3%。
- 策略可零样本泛化到未见物体，并适配 Fourier 与 Inspire 两种不同多指手，抗外力扰动。

## 🔗 关联
- [[Solving Rubik's Cube with a Robot Hand]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Learning Dexterous In-Hand Manipulation]]

## 🏷️ 标签
#仿真到现实迁移 #人形机器人 #灵巧操作 #扩散策略 #域随机化
