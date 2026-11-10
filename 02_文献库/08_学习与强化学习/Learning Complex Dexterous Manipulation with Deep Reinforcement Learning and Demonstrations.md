---
title: Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
year: 2018
doi: 
arxiv: 1709.10087
key: KB-083
venue: arXiv preprint（cs.LG, v2）；后发表于 CoRL 2018（卷期待核对）
theme: 02_文献库/08_学习与强化学习
tags: [强化学习, 模仿学习, 手内操作, 灵巧手, 示教增广]
pdf: ../../../Learning Complex Dexterous Manipulation with.pdf
confidence: high
source: pdf
aliases: []
---

# Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

## 📌 年份
2018

## 🔑 论文识别码
arXiv:1709.10087

## 👥 作者与所属院校
- 作者：Aravind Rajeswaran、Vikash Kumar、Abhishek Gupta、Giulia Vezzani、John Schulman 等
- 机构：华盛顿大学、OpenAI、加州大学伯克利分校、意大利技术研究院（IIT）

## 📖 研究背景
- 多指[[灵巧手]]自由度高、接触模式多变，如何控制仍是难题；此前 DRL 多停在低维机械臂任务。
- 无模型[[强化学习]]样本效率低，真机部署代价高；已有 benchmark 又过于简化，难反映手的复杂度。
- 该文尝试把少量人类示教接入策略梯度，兼顾接触丰富任务与可接受的样本量。

## ❓ 需要解决的问题
- 无模型 DRL 能否从零扩展到 24 自由度手的复杂操作，而非只做抓取或转笔？
- 少量 VR 示教能把样本复杂度降到什么量级，是否相当于数小时真机经验？
- 示教学到的策略是否更自然、更抗扰动，能否胜过仅靠奖励塑形与 DDPGfD？

## 📥📤 输入与输出
- 输入：关节角与角速度、物体位姿、指尖位置等本体状态（仿真中不引入触觉）。
- 输出：24 个关节的目标位置增量，由底层 PD 跟踪；任务含物体重定位、[[手内操作]]转笔、开门、锤击。

## ✅ 论文最终达到的效果
- 在 MuJoCo 中用 ADROIT 24 自由度手从零学会四类任务，证明 DRL 可扩展到高维手。
- 提出示教增广策略梯度 DAPG：以自然策略梯度为基座，用示教轨迹引导探索并加正则。
- 示教把样本量压到相当于数小时真机经验；DAPG 明显优于 DDPG、DDPGfD 与仅奖励塑形的 RL。
- 示教策略动作更接近人类、冗余动作更少，且在物体尺寸与动力学扰动下更鲁棒。
- 局限：全部在仿真中评估，尚未验证真机迁移，也未使用触觉。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#强化学习 #模仿学习 #手内操作 #灵巧手
