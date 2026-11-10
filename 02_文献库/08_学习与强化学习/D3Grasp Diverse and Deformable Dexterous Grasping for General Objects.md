---
title: "D3Grasp: Diverse and Deformable Dexterous Grasping for General Objects"
year: 2025
doi: 
arxiv: 2509.19892
key: KB-035
venue: 待补（arXiv 预印本）
theme: 02_文献库/08_学习与强化学习
tags: [视觉触觉融合, 非对称强化学习, 可变形物体, 课程学习, 灵巧抓取]
pdf: ../../../D3Grasp.pdf
confidence: high
source: pdf
aliases: []
---

# D3Grasp: Diverse and Deformable Dexterous Grasping for General Objects

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2509.19892

## 👥 作者与所属院校
- 作者：Keyu Wang, Bingcong Lu, Zhengxue Cheng（通讯）, Hengdi Zhang, Li Song
- 机构：上海交通大学、Paxini Tech

## 📖 研究背景
- [[灵巧手]] 已有 16 自由度以上硬件，但多模态感知整合与数据高效策略学习仍是落地瓶颈。
- 单模态各有短板：视觉怕透明与遮挡，触觉缺全局信息，本体感觉几乎不含环境信息。
- 直接把视觉与触觉特征拼接会抬高观测维度、拖慢策略收敛，且固定融合权重无法适应不同操作阶段。
- 因此需要一种 [[视触融合]] 表示，配合数据高效的 [[强化学习]]，在仿真中直接学出可迁移的抓取策略。

## ❓ 需要解决的问题
- 如何构建统一的视觉–触觉表示，让策略按阶段自适应地依赖不同模态？
- 在无人工示教、无复杂物体建模的前提下，如何提升样本效率与 sim-to-real 泛化？
- 对可变形、易压坏物体，如何兼顾抓取多样性与稳定性，避免穿透与不可行姿态？

## 📥📤 输入与输出
- 输入：腕部视觉、手上 11 路触觉传感器的三维力、手指关节状态与本体感觉；训练时另有特权信息（物体应变场、手–物距离等）。
- 输出：Dexhand13 的关节动作与 6D 根位姿（真机映射为 UR5 末端运动）。

## ✅ 论文最终达到的效果
- Paxini Dexhand13：四指 16 自由度，配 11 个触觉传感器，加 UR5 共 22 自由度；IsaacSim 中训练，PPO + 非对称 actor–critic。
- 三项指标：抓取成功率、抬升 0.1 m 成功率、抬升后六向 2.5 N 外力 2 s 干扰通过率。
- 仿真中多样物体抬升/抗扰 84.2%/82.7%，可变形物体 84.4%/82.2%，均高于 DexGraspNet、DexDiffuser、ISAGrasp 等方法。
- 真机 50 个物体：抓取成功率平均 95.1%、抬升 91.0%、抗扰 90.5%；基线 D(R,O) 抬升 89.0%。
- 200 步推理时延 0.36 s，快于 D(R,O) 的 0.65 s。

## 🔗 关联
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Learning Dexterous In-Hand Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#视觉触觉融合 #非对称强化学习 #可变形物体 #课程学习 #灵巧抓取
