---
title: Local connection reinforcement learning method for efficient robotic peg-in-hole assembly
year: 2024
doi: 10.1016/j.engappai.2024.108520
arxiv: 
key: KB-094
venue: Engineering Applications of Artificial Intelligence, 133 (2024) 108520
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 强化学习, DDPG, 柔顺控制, Shapley值, 数据效率]
pdf: ../../../Local connection reinforcement learning method for efficient robotic peg-in-hole assembly.pdf
confidence: high
source: pdf
aliases: [LCRL]
---

# Local connection reinforcement learning method for efficient robotic peg-in-hole assembly

## 📌 年份
2024

## 🔑 论文识别码
DOI: 10.1016/j.engappai.2024.108520

## 👥 作者与所属院校
- 作者：Yuhang Gai, Jiwen Zhang, Dan Wu, Ken Chen
- 机构：清华大学机械工程系摩擦学国家重点实验室

## 📖 研究背景
- [[轴孔装配]]的接触动力学强非线性且随插入过程变化，恒参数[[柔顺控制]]只能应付弱非线性工况。
- 自适应柔顺控制（变柔心、变参数）依赖人工设计规则；[[强化学习]]可替代经验设计，但训练极慢。
- 症结在于常规 RL 是"全连接"的：每个动作分量都吃全部状态分量，状态-动作空间被无谓放大。

## ❓ 需要解决的问题
- 如何量化某个动作分量对某个状态分量的真实影响，而非靠先验假设？
- 能否据此构造"局部连接"策略网络，剔除无关状态输入而不损失最优性？
- 在 DDPG 上落地后，收敛所需回合数与最终奖励能改善多少？
- 与[[力位混合控制]]式的比例柔顺控制器结合，能否在真机上完成方轴方孔插入？

## 📥📤 输入与输出
- 输入：机器人笛卡尔位姿与六维力/力矩传感器读数（力 Fx–Fz、力矩 Mx–Mz）。
- 输出：柔顺控制器 6 个参数修正量 Δx、Δy、Δz、Δα、Δβ、Δγ，合成位姿修正指令 a ∈ R6。

## ✅ 论文最终达到的效果
- 提出连续空间序列化 Shapley 值 CS3 与连接图，定量给出动作-状态依赖关系（如 a1 影响 s1、s2）。
- 相同平均奖励所需回合数仅为传统全局连接 DDPG 的 49%。
- 末回合最终奖励比传统方法高 35%，训练更稳、装配过程更平稳。
- 仿真与真机均验证：方轴 9.9 mm 对 10 mm 孔、插入深度 30 mm、倒角 0.5 mm、ABS 材料。
- 随机初始位姿 ±0.4 mm / ±1°，控制步 250 步内完成插入。

## 🔗 关联
- [[End-to-end deep reinforcement learning and control with multimodal perception for planetary robotic dual peg-in-hole assembly]]
- [[Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand]]
- [[Active Touch Sensing for Robust Hole Detection in Assembly Tasks]]

## 🏷️ 标签
#轴孔装配 #强化学习 #DDPG #柔顺控制 #数据效率
