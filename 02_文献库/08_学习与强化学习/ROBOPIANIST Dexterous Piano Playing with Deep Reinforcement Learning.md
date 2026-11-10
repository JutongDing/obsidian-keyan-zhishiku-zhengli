---
title: "ROBOPIANIST: Dexterous Piano Playing with Deep Reinforcement Learning"
year: 2023
doi: 
arxiv: 2304.04150
key: KB-115
venue: 7th Conference on Robot Learning (CoRL 2023)
theme: 02_文献库/08_学习与强化学习
tags: [钢琴演奏, 高维控制, 双臂灵巧操作, 基准环境]
pdf: ../../../ROBOPIANIST.pdf
confidence: high
source: pdf
aliases: [ROBO PIANIST]
---

# ROBOPIANIST: Dexterous Piano Playing with Deep Reinforcement Learning

## 📌 年份
2023

## 🔑 论文识别码
arXiv: 2304.04150

## 👥 作者与所属院校
- 作者：Kevin Zakka、Philipp Wu、Laura Smith、Nimrod Gileadi、Taylor Howell 等
- 机构：加州大学伯克利分校、Google DeepMind、斯坦福大学

## 📖 研究背景
- 复现人手灵巧性是机器人学长期难题，高维控制至今仍是重大挑战，机械设计与控制理论两条路线都投入了大量研究。
- [[强化学习]]近年进展显著，但主流任务多以单一目标状态或终止条件定义，解空间有限，常出现只为达标却不自然的动作。
- 钢琴演奏同时要求空间与时间精度、双手协调与乐句规划，可作为灵巧性的极端测试场景。
- 本文切入角度：把两只人形[[灵巧手]]放在仿真钢琴前，以 MIDI 乐谱为任务，用同一套流程覆盖 150 首难度递进的曲目。

## ❓ 需要解决的问题
- 学习型策略能否在 44 维位置控制空间里完成双手钢琴演奏，并显著优于采样式规划器？
- 单曲专家策略与多曲联合策略的性能如何权衡，多曲训练能否带来对未见曲目的零样本泛化？
- 动作空间约束、控制步长、网络规模等设计选择对最终 F1 分数各贡献多少？
- 如何给出可解释、可跨曲目比较的演奏质量指标？

## 📥📤 输入与输出
- 输入：仿真中双手关节角与关节速度等本体感知状态，附加延音踏板标量；任务侧为 MIDI 音符事件序列。
- 输出：44 维关节位置控制量（左右各一只 22 自由度 Shadow hand），由策略逐步给出以按下正确琴键。

## ✅ 论文最终达到的效果
- 构建 ROBOPIANIST-REPERTOIRE-150：150 首、24 位西方作曲家的标注 MIDI 曲目，覆盖巴洛克、古典与浪漫时期。
- 每曲训练 5M 采样；在 12 首评测集 ETUDE-12 上平均 F1 为 0.79，明显高于采样式 MPC 基线的 0.43。
- 定性上出现跨键盘远距离换位、和弦三音齐按、快速颤音等类人技巧。
- 多曲联合训练暴露任务干扰：训练曲目从 1 首增至 16 首时，训练曲 F1 由约 0.7 降至接近 0。
- 开源环境、任务基准与可解释评测指标，并列出后继开放问题（如利用人类先验加速学习）。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#强化学习 #高维控制 #双臂操作 #钢琴演奏 #基准环境
