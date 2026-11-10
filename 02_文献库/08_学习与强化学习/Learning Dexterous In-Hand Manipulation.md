---
title: Learning Dexterous In-Hand Manipulation
year: 2019
doi: 
arxiv: 1808.00177
key: KB-084
venue: arXiv（cs.LG 预印本，v5）
theme: 02_文献库/08_学习与强化学习
tags: [强化学习, 手内操作, 仿真到现实迁移, 域随机化, 灵巧手]
pdf: ../../../Learning Dexterous In-Hand Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# Learning Dexterous In-Hand Manipulation

## 📌 年份
2019（arXiv v5；初版 2018）

## 🔑 论文识别码
arXiv:1808.00177

## 👥 作者与所属院校
- 作者：OpenAI；Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafał Józefowicz, Bob McGrew 等
- 机构：OpenAI

## 📖 研究背景
- 五指[[灵巧手]]控制难度大：Shadow 手 24 个自由度、20 对拮抗[[腱驱动]]，商用多年仍未普及。
- 真机采样成本高，纯仿真策略又受"现实差距"限制，常无法迁移。
- 该文用大规模分布式[[强化学习]]加[[域随机化]]，从零学视觉[[手内操作]]，不用人类示教。

## ❓ 需要解决的问题
- 仅靠仿真参数与外观随机化，24 自由度手的重定向策略能否零样本迁移到真机？
- 策略网络的记忆（LSTM）与视觉[[抓取位姿]]估计对迁移是否必要，能否用消融验证？
- 不给示教与先验奖励，手指步态、多指协调等人类行为能否自发涌现？

## 📥📤 输入与输出
- 输入：关节角与 5 个指尖笛卡尔位置（PhaseSpace 动捕，<20 μm）、3 路 RGB 的物体位姿、目标姿态。
- 输出：20 个执行器的相对位置增量；策略以约 12 Hz 输出，底层位置控制约 1 kHz。

## ✅ 论文最终达到的效果
- 方块（状态输入）连续重定向：仿真均值 43.4±13.8 次，真机 18.8±17.1 次（上限 50 次）。
- 视觉版本：仿真 30.0±10.3 次，真机 15.2±14.3 次；八棱柱真机仅 7.8±7.8 次。
- 采样用 384 台 16 核机器并行；策略训练用 8 块 V100 与 6144 个 CPU 核。
- 视觉网络只用约 100 万条合成状态、200×200 三路图像训练，无需真实图像。
- 涌现行为：指尖捏、三指捏、五指精确抓、手指步态与受控利用重力，且偏好用小指。

## 🔗 关联
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]

## 🏷️ 标签
#强化学习 #手内操作 #仿真到现实迁移 #域随机化
