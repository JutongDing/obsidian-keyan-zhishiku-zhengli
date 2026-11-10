---
title: "Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic"
year: 2025
doi: 
arxiv: 2505.13253
key: KB-030
venue: ICRA 2025（据项目页 icra25；arXiv 2505.13253）
theme: 02_文献库/08_学习与强化学习
tags: [抓取选择, 价值函数, 手内操作, 强化学习, DLR Hand II]
pdf: ../../../Composing Dextrous Grasping and In-hand Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2505.13253

## 👥 作者与所属院校
- 作者：Lennart Röstel, Dominik Winkelbauer, Johannes Pitz, Leon Sievers, Berthold Bäuml
- 机构：慕尼黑工业大学 Learning AI for Dextrous Robots Lab、德国宇航中心（DLR）机器人与机电研究所

## 📖 研究背景
- 抓取与 [[手内操作]] 长期被分开研究：抓取只看静态 [[抓取质量]]，手内操作只追求把物体转到目标姿态。
- [[强化学习]] 能练出重定向策略，但真机常需人工把物体摆到合适的初始抓取状态，落地困难。
- 现有可操作性指标依赖手–物 [[雅可比矩阵]]，与策略实际能达成的成功率并不一致。

## ❓ 需要解决的问题
- 如何判断一个抓取是否「有利于后续手内重定向」，而不只看静态稳定性？
- 能否不再训练新网络，直接复用已有策略的价值函数做抓取打分？
- 打分选出的抓取能否在真机上组成「抓取→重定向」全流程并提升成功率？

## 📥📤 输入与输出
- 输入：物体的形状编码与目标姿态、候选初始手位姿与指关节角、可达的末态手位姿集合。
- 输出：候选组合的 critic 打分；据此选出初始抓取、末态手位姿与指关节构型，并驱动 [[抓取规划]] 与后续策略。

## ✅ 论文最终达到的效果
- critic 打分与仿真成功率正相关，Pearson 系数 0.82（N≈60 万次试验）。
- 选择最高分抓取使成功率相对「全部候选平均」提升 9.4%，物体掉落率由 3.8% 降到 2.5%，到目标时间由 4.2 s 降到 3.6 s。
- 再允许手基座绕竖轴转动 π/2 以内，提升达 17.6%，掉落率 1.9%，时间 2.7 s；最低分抓取则下降 14.6%。
- 打分本身很便宜：T4 GPU 上批量评估 18000 个组合约 0.1 s。
- 真机 Agile Justin + DLR Hand II，两款物体各测 24 个目标朝向，22 与 23 次成功，合计 93.7%。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]

## 🏷️ 标签
#抓取选择 #价值函数 #手内操作 #强化学习 #DLR手
