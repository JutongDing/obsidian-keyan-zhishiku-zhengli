---
title: In-Hand Manipulation with Enforced Grasp Stability for Contact-Rich Tasks
year: 2025
doi: 
arxiv: 
key: KB-167
venue: IEEE ICRA 2025 Workshop on Contact-Rich Manipulation (CRM)
theme: 02_文献库/08_学习与强化学习
tags: [强化学习, 手内操作, 力封闭, 抓取稳定性预测, 指尖力/力矩传感]
pdf: ../../../n-Hand Manipulation with Enforced Grasp.pdf
confidence: high
source: pdf
aliases: [OpenReview YK2YeuL2rU]
---

# In-Hand Manipulation with Enforced Grasp Stability for Contact-Rich Tasks

## 📌 年份
2025

## 🔑 论文识别码
KB-167（本地编号；ICRA 2025 CRM Workshop，OpenReview id: YK2YeuL2rU）

## 👥 作者与所属院校
- 作者：Yifei Chen, Shihan Lu, Haoxuan Zhang, Kevin M. Lynch
- 机构：美国西北大学（Northwestern University）

## 📖 研究背景
- 近年[[手内操作]]的重定向演示多依赖手掌支撑或指尖托举，并非真正稳定抓取，掉物仍常见。
- 现有无模型[[强化学习]]多以视觉、[[触觉图像]]或关节力矩为观测，很少直接用指尖六维力/力矩。
- 人类靠指尖丰富力觉维持稳定握持，这条仿生线索在手指步态控制中尚未被系统利用。

## ❓ 需要解决的问题
- 把指尖力/力矩纳入观测空间，能否在动态接触中提升[[抓取稳定性预测]]与保持能力？
- 以抓取力旋量矩阵加 SVD 构造的[[力封闭]]奖励，能否让策略兼顾稳定性与旋转量，而非"空中打转"刷分？
- 力/力矩观测与力封闭奖励各自贡献多少，初值扰动下是否仍有效？

## 📥📤 输入与输出
- 输入：Allegro Hand V4 的 16 个关节角、物体（方块）位姿、指尖 6D 力/力矩，观测堆叠 5 帧。
- 输出：16 维目标关节角序列，经关节空间 PID 跟踪；策略用 SAC 训练。

## ✅ 论文最终达到的效果
- 加力封闭奖励后，约 0.5M 步即突破 600 分，收敛约 850 分；基线策略全程不足 100 分。
- 无扰动评测：力封闭策略回合时长显著延长，有效旋转略降，因基线靠空中旋转虚增转角。
- ±10 mm、±5° 初值扰动下，仍比无力封闭策略转得更多、掉物更少。
- 2M 环境步约需 8 小时（RTX 3060 笔记本，12 个并行环境），每策略评测 50 回合、单回合上限 10 s。
- 作者明确声明为初步结果，鲁棒性与泛化仍需更多随机化与外力扰动实验。

## 🔗 关联
- [[Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations]]
- [[Progressive Transfer Learning for Dexterous In-Hand Manipulation with Multi-Fingered Anthropomorphic Hand]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#强化学习 #手内操作 #力封闭 #抓取稳定性
