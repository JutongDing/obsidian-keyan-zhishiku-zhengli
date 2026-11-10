---
title: Learning Stable Robot Grasping with Transformer-based Tactile Control Policies
year: 2024
doi: 
arxiv: 2407.21172
key: KB-087
venue: arXiv preprint（cs.RO, v1）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [抓取稳定, 触觉传感, Transformer, 强化学习, 仿真到现实迁移]
pdf: ../../../Learning Stable Robot Grasping with.pdf
confidence: high
source: pdf
aliases: 
---

# Learning Stable Robot Grasping with Transformer-based Tactile Control Policies

## 📌 年份
2024

## 🔑 论文识别码
arXiv:2407.21172

## 👥 作者与所属院校
- 作者：En Yen Puang、Zechen Li、Chee Meng Chew、Shan Luo、Yan Wu
- 机构：意大利技术研究院/热那亚大学、新加坡国立大学、伦敦国王学院、A*STAR 资讯通信研究院

## 📖 研究背景
- 抓取是否稳定可从触觉推断：夹持点偏离质心时物体会绕接触点转动（pivoting）并[[初始滑移]]。
- 经典 stable grasp 任务只优化重抓位置，且假设物体质心固定、重量不变，脱离真实场景。
- 质心未知且随负载滑动，夹持力过大又会压坏物体，位置与力两个目标天然冲突。

## ❓ 需要解决的问题
- 质心未知且移动时，策略能否同时优化重抓位置与夹持力，而非只顾其一？
- Transformer 是否比堆叠时序的 CNN 更适合触觉序列，能否降低超额夹持力？
- 纯仿真训练的策略能否零样本迁移到真机，适应不同配重？

## 📥📤 输入与输出
- 输入：抬升阶段均匀采样的 11 帧触觉图，每帧为 8×6 剪切力阵列（[[GelSight]] 传感）。
- 输出：二维连续动作——抓取位置偏移量与夹持力，逐步闭环修正。

## ✅ 论文最终达到的效果
- 重构 stable grasp 任务：条形负载质心随倾斜滑动，成功需抬升 ≥17 mm 且倾角 <0.02 rad。
- 用 8 层多头交叉注意力 Transformer 编码触觉序列，SAC 训练（8 并行环境、3 万步）。
- 成功率 0.954–0.992（α 取 10/30/50，Transformer 在 α=10 时为 0.990），平均尝试少于 3 次，超额夹持力低于 0.2。
- 与 CNN 基线相比，Transformer 超额力更低（0.137–0.182 对 0.194–0.281），但尝试次数略多，体现两目标权衡。
- 在 UR5 + Robotiq 两指夹爪 + GelSight 上零样本迁移，5 种配重各 12 次随机试验，含堆叠负载。

## 🔗 关联
- [[Force Estimation and Slip Detection for Grip Control using a Biomimetic Tactile Sensor]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]

## 🏷️ 标签
#抓取稳定 #触觉传感 #强化学习 #仿真到现实迁移
