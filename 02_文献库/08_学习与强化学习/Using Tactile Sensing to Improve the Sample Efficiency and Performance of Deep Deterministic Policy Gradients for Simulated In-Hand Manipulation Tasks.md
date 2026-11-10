---
title: Using Tactile Sensing to Improve the Sample Efficiency and Performance of Deep Deterministic Policy Gradients for Simulated In-Hand Manipulation Tasks
year: 2021
doi: 10.3389/frobt.2021.538773
arxiv: 
key: KB-157
venue: Frontiers in Robotics and AI（2021, vol. 8, art. 538773）
theme: 02_文献库/08_学习与强化学习
tags: [触觉传感, 强化学习, 手内操作, 样本效率, Shadow手]
pdf: ../../../Using Tactile Sensing to Improve the Sample Efficiency and Performance of Deep Deterministic Policy Gradients for Simulated In-Hand Manipulation Tasks.pdf
confidence: high
source: pdf
aliases: []
---

# Using Tactile Sensing to Improve the Sample Efficiency and Performance of Deep Deterministic Policy Gradients for Simulated In-Hand Manipulation Tasks

## 📌 年份
2021

## 🔑 论文识别码
DOI: 10.3389/frobt.2021.538773

## 👥 作者与所属院校
- 作者：Andrew Melnik, Luca Lach, Matthias Plappert, Timo Korthals, Robert Haschke 等
- 机构：德国比勒费尔德大学 CITEC、PAL Robotics（西班牙巴塞罗那）、OpenAI（美国旧金山）

## 📖 研究背景
- [[强化学习]]在[[手内操作]]上已见成效，但需海量交互样本，仿真与真机均难承受。
- 人类可仅凭触觉完成手内操作，而主流仿真基准只提供关节角与物体位姿。
- 该文给 OpenAI Gym 的 Shadow 手环境加装接触阵列，系统评估触觉对学习的影响。

## ❓ 需要解决的问题
- 加入触觉观测后，达到同等回报所需交互样本能减少几倍？
- 触觉带来的是收敛更快，还是最终性能也更高？
- 传感器测量精度（连续真值/含噪连续/布尔）与空间分辨率各起多大作用？
- 收益能否在方块、蛋、笔等多个手内操作任务上稳定复现？

## 📥📤 输入与输出
- 输入：Shadow 手关节角与速度、物体位姿与速度、各触觉单元的接触法向力（或布尔接触标志）。
- 输出：手部 20 维关节位置增量动作，训练时用 HER 做目标重标记。

## ✅ 论文最终达到的效果
- 触觉使训练样本效率最高提升三倍以上，即用不到三分之一样本达到同等性能。
- 加入触觉后最终性能最多提升 46%。
- 空间分辨率实验比较 927、92、16 个合并传感区域三种配置，收益随分辨率下降而衰减。
- 布尔化或含噪的触觉读数仍保留大部分收益，低成本二值接触信号已可用。
- 作者把触觉扩展开源为 Gym Shadow 手的新环境，便于后续复现与横向比较。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#触觉传感 #强化学习 #手内操作 #样本效率 #Shadow手
