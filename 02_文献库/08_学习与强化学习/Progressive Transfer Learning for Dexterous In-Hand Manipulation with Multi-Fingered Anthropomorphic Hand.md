---
title: Progressive Transfer Learning for Dexterous In-Hand Manipulation with Multi-Fingered Anthropomorphic Hand
year: 2023
doi: 
arxiv: 2304.09526
key: KB-112
venue: IEEE Transactions on Neural Networks and Learning Systems（2023，early access）
theme: 02_文献库/08_学习与强化学习
tags: [迁移学习, 手内操作, 渐进神经网络, 强化学习, 样本选择]
pdf: ../../../Progressive Transfer Learning for Dexterous.pdf
confidence: high
source: pdf
aliases: []
---

# Progressive Transfer Learning for Dexterous In-Hand Manipulation with Multi-Fingered Anthropomorphic Hand

## 📌 年份
2023

## 🔑 论文识别码
arXiv: 2304.09526（DOI 待补；本地编号 KB-112）

## 👥 作者与所属院校
- 作者：Yongkang Luo、Wanyi Li、Peng Wang、Haonan Duan、Wei Wei 等
- 机构：中国科学院自动化研究所多模态人工智能系统全国重点实验室、中国科学院大学人工智能学院

## 📖 研究背景
- 多指拟人手的[[手内操作]]状态 36 维、动作 24 维，接触模式丰富，深度[[强化学习]]的样本复杂度很高。
- 场景略变（如球或立方体尺寸改一点）就要重采数据、反复微调，与人手快速迁移技能的能力差距明显。
- 该文提出渐进迁移学习（PTL）：复用源任务轨迹与已训好的[[动力学建模]]模型，只对目标任务做少量在线尝试。

## ❓ 需要解决的问题
- 如何从源任务海量轨迹中挑出对目标任务最有用的样本（按动力学性质、奖励与轨迹分数）？
- 渐进神经网络能否只加新列就迁移动力学模型，同时不遗忘源任务知识？
- 目标任务少量尝试能达到多高成功率，训练时间与数据量能省多少？

## 📥📤 输入与输出
- 输入：源任务轨迹（状态 36 维、动作 24 维、控制频率 10 Hz）、源任务训练好的动力学模型、目标场景少量随机探索数据。
- 输出：目标场景的动力学模型与策略动作（24 维关节目标），供[[欠驱动手]]式拟人手执行。

## ✅ 论文最终达到的效果
- Baoding Balls 同尺寸变化任务：奖励阈值成功率 99.2%、分数阈值 92.8%，从头训练仅 76.7% / 3.0%。
- 训练 4.7 h 对从头 31 h；摘要称训练时间成本最多减少 95%，数据量约 19 万对 91 万条。
- 大小球混合任务 94.6% / 65.8%（微调 88.6% / 64.8%）；Cube Reorientation 迁移后 97.25% / 73.5%。
- 与 PNN、PNN-V1、微调、从头训练对比，结果取 5 个随机种子平均；仿真环境为 MuJoCo 类 24 自由度拟人手。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Multi-Goal Dexterous Hand Manipulation using Probabilistic Model-based Reinforcement Learning]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#迁移学习 #手内操作 #渐进神经网络 #样本选择
