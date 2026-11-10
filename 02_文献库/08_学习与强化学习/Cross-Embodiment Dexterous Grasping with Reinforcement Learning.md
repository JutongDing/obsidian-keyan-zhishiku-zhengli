---
title: Cross-Embodiment Dexterous Grasping with Reinforcement Learning
year: 2025
doi: 
arxiv: 2309.06440
key: KB-026
venue: ICLR 2025
theme: 02_文献库/08_学习与强化学习
tags: [跨实体学习, 强化学习, 特征抓取, 重定向]
pdf: ../../../CROSS-EMBODIMENT DEXTEROUS GRASPING.pdf
confidence: high
source: pdf
aliases: [CrossDex]
---

# Cross-Embodiment Dexterous Grasping with Reinforcement Learning

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2309.06440（ICLR 2025 会议论文，无 DOI）

## 👥 作者与所属院校
- 作者：Haoqi Yuan、Bohan Zhou、Yuhui Fu、Zongqing Lu
- 机构：北京大学计算机学院、北京智源人工智能研究院

## 📖 研究背景
- 已有[[灵巧手]]抓取策略多针对单一手型（如 ShadowHand）训练，换手即需重采数据或重调仿真与超参。
- 跨实体学习希望复用不同机器人共享的结构特征，从而泛化到新本体。
- 人手可通过[[主从遥操作]]「操控」各种灵巧手，提示存在与本体无关的统一动作接口。
- 本文切入角度：用人手特征抓取（eigengrasp）作统一动作空间，把重定向映射放到策略之外。

## ❓ 需要解决的问题
- 如何定义跨不同自由度、不同指数的统一动作空间与统一观测空间？
- 重定向计算在 RL 训练中极慢，如何保证 8192 并行环境下的训练吞吐？
- 单一[[强化学习]]策略能否在多个手型上同时达到可用成功率？
- 对训练中完全未见过的手型，能否零样本抓取，微调后收益多大？

## 📥📤 输入与输出
- 输入：视觉观测（物体与手的关系）、统一本体感知（仅指尖与手掌位置）、手臂关节状态。
- 输出：k 维特征抓取动作系数 w 与手臂动作，经重定向网络映射为各手的关节位置目标，由 PD 控制器跟踪执行。

## ✅ 论文最终达到的效果
- 单一视觉策略在 4 种训练手（ShadowHand、Allegro、Ability、Schunk）上 YCB 抓取成功率 0.800，状态版 0.885。
- 零样本迁移到 2 种未见手（LEAP 16 自由度四指、Inspire 12 自由度五指）：视觉 0.352、状态 0.391，显著优于多任务基线（0.145/0.046）。
- 45 个 YCB 物体中，有 42 个在四种训练手上成功率超过 60%。
- 仅用其他四手数据训练，三指 D'Claw 夹爪仍达 0.853；单机成功率最高为 Schunk 0.911。
- 训练用 8192 个并行环境；特征抓取与重定向网络由 GRAB 数据集 1.6M 帧人手姿态获得。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#跨实体 #强化学习 #特征抓取 #重定向
