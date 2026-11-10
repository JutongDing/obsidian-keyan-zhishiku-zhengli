---
title: Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning
year: 2022
doi: 
arxiv: 2206.08686
key: KB-165
venue: NeurIPS 2022 Datasets and Benchmarks Track
theme: 02_文献库/08_学习与强化学习
tags: [强化学习, 双手操作, 基准测试, 手内操作, 灵巧手]
pdf: ../../../human-level bimanual dexterous manipulation with reinforcement learning.pdf
confidence: high
source: pdf
aliases: [Bi-DexHands]
---

# Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning

## 📌 年份
2022

## 🔑 论文识别码
arXiv:2206.08686

## 👥 作者与所属院校
- 作者：Yuanpei Chen, Tianhao Wu, Shengjie Wang, Xidong Feng, Jiechuang Jiang 等
- 机构：北京大学人工智能研究院、北京大学前沿计算研究中心、伦敦大学学院、卡内基梅隆大学、北京通用人工智能研究院

## 📖 研究背景
- 达到人类水平的双手灵巧度仍是公开难题：手指数十自由度耦合，异构"智能体"（关节、手指、手）需协作，策略搜索易陷局部最优。
- 既有[[手内操作]]研究多针对单手、手掌朝上的物体重定向，缺少统一任务集与评测协议，算法间难以横向比较。
- 认知科学的精细动作分测验（FMS）给出婴儿动作能力分级，可作为任务难度标尺。

## ❓ 需要解决的问题
- 能否构建一个覆盖多难度、多物体、双手异构协作的[[强化学习]]基准，统一评测主流算法？
- 单智能体 RL 与多智能体 RL 在需要双手配合的任务上差距有多大？
- 离线 RL、多任务 RL、元 RL 能否实现"一策多技"与少样本泛化？

## 📥📤 输入与输出
- 输入：仿真中双手（两只 Shadow Hand，各 24 关节、20 对拮抗腱）与物体、目标的全状态向量；不使用视觉输入。
- 输出：各手关节的目标位置增量（连续动作），由底层控制器跟踪执行。

## ✅ 论文最终达到的效果
- Bi-DexHands 含 20 个双手任务、6 类技能，目标物体取自 YCB 与 SAPIEN 数据集。
- 单张 RTX 3090、2048 个并行环境下平均达 30,000+ FPS，支撑大规模采样。
- PPO 类 on-policy 算法可掌握约相当于 48 月龄婴儿的简单任务（接飞行物、开瓶）。
- 多智能体 RL 进一步完成抬锅、叠积木等要求双手协同的任务。
- 多任务与少样本设置下现有算法多数失败，说明"一策多技"仍待突破。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Solving Rubik's Cube with a Robot Hand]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#强化学习 #双手操作 #基准测试 #手内操作
