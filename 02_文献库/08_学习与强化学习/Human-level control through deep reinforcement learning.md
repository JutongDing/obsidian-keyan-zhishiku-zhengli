---
title: Human-level control through deep reinforcement learning
year: 2015
doi: 10.1038/nature14236
arxiv: 
key: KB-095
venue: Nature
theme: 02_文献库/08_学习与强化学习
tags: [强化学习, DQN, 经验回放, 目标网络, 深度Q学习]
pdf: ../../../MNIH_2015_Nature_Human-level Control through Deep Reinforcement Learning.pdf
confidence: high
source: pdf
aliases: [DQN, Nature 2015 Mnih]
---

# Human-level control through deep reinforcement learning

## 📌 年份
2015

## 🔑 论文识别码
DOI: 10.1038/nature14236

## 👥 作者与所属院校
- 作者：Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness 等
- 机构：Google DeepMind（伦敦）

## 📖 研究背景
- [[强化学习]]理论上可逼近最优控制，但真实场景的高维感知输入要求智能体自行学出有效表征。
- 用非线性函数逼近器（神经网络）表示动作价值函数时，样本相关性与目标漂移会导致训练不稳甚至发散。
- 该文提出深度 Q 网络（DQN），把卷积网络与 Q-learning 稳定地结合起来，直接从像素学策略。

## ❓ 需要解决的问题
- 如何打断连续观测之间的时间相关性，使 SGD 假设成立？
- 如何避免"追着自己跑"的目标漂移造成 Q 值振荡发散？
- 同一套网络结构、超参数能否跨多款差异极大的游戏通用，而不逐游戏调参？
- 学到的内部表征是否真的对应游戏状态语义？

## 📥📤 输入与输出
- 输入：最近 4 帧 84×84 灰度游戏画面堆叠（原始 210×160 RGB 帧按 6 帧取 1、10 Hz 决策）。
- 输出：18 个合法按键动作对应的动作价值 Q(s,a)，取最大者执行（ε-greedy，ε 从 1.0 退火至 0.1）。

## ✅ 论文最终达到的效果
- 在 49 款 Atari 2600 游戏上，DQN 在 29 款达到人类测试者 75% 以上得分，多数游戏远超此前最好方法。
- 统一网络架构与超参数（同一套卷积栈 + 全连接），逐游戏仅换输入维度与动作数。
- 训练规模：5000 万帧（约 38 天游戏时长），经验回放缓存 100 万帧，目标网络定期克隆。
- 消融显示经验回放与独立目标网络二者缺一即性能明显下降。
- 末隐层表征的 t-SNE 嵌入与人类玩家的状态聚类重叠，说明网络学到了可迁移的状态语义。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#强化学习 #DQN #经验回放 #目标网络 #深度Q学习
