---
title: Reinforcement Learning Grasping With Force Feedback From Modeling of Compliant Fingers
year: 2025
doi: 10.1109/TMECH.2024.3450269
arxiv: 
key: KB-120
venue: IEEE/ASME Transactions on Mechatronics, vol. 30, no. 3, pp. 2222–2233
theme: 02_文献库/08_学习与强化学习
tags: [力反馈, 柔顺夹爪, caging 抓取, 仿真到现实]
pdf: ../../../Reinforcement Learning Grasping with Force Feedback from Modeling of Compliant Fingers.pdf
confidence: high
source: pdf
aliases: []
---

# Reinforcement Learning Grasping With Force Feedback From Modeling of Compliant Fingers

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.1109/TMECH.2024.3450269

## 👥 作者与所属院校
- 作者：Luke Beddow、Helge Wurdemann、Dimitrios Kanoulas
- 机构：伦敦大学学院（University College London）

## 📖 研究背景
- 现有[[强化学习]]抓取多由相机数据定抓取位置、再执行硬编码闭合动作，很少把力反馈纳入策略观测。
- 杂货物体重量、纹理、表面不规则差异大，易被夹伤，恰是最需要限制并监测接触力的场景。
- 柔顺指多用硅胶等非线性超弹材料、依赖摩擦抓取，精确的接触力仿真代价高，拖慢数据驱动训练。
- 本文切入角度：先用物理模型刻画柔顺指弯曲，使仿真跑得快，再把指力与掌力作为观测喂给策略。

## ❓ 需要解决的问题
- 柔顺指的弯曲与受力能否用可解析/可快速计算的模型描述，从而把仿真速度提升到可训练的量级？
- 在含力反馈的观测下，策略能否同时学会抓稳与限力，而不是靠固定闭合行程碰运气？
- 仿真训练的力反馈策略迁移到实物后，成功率与[[仿真到现实迁移]]差距有多大？
- 手指刚度改变时模型与力反馈带来的增益是否依然成立？

## 📥📤 输入与输出
- 输入：腕部相机视角与本体状态、由应变片测得并经模型换算的指力/掌力读数，用于闭环观测。
- 输出：三指与可动掌心的关节动作指令，构成 caging 式包络抓取。

## ✅ 论文最终达到的效果
- 设计 3 自由度 caging 夹爪：三根柔顺指加一个可动掌心，可把物体「罩」在笼内，指尖内置应变片测力。
- 柔顺指弯曲模型使仿真达到 16.8× 实时，足以支撑 PPO 策略训练。
- 训练物体上实物成功率 98.0%，平均 sim2real 差距 3.1%。
- 42 个未见杂货物体上成功率 95.0%，其中 80.1% 的抓取还能承受额外 5 N 竖直扰动。
- 抓取过程平均指力 1.36 N、掌力 3.02 N，除香蕉轻微压伤外未造成可见损伤；刚性替代物与真实杂货的成功率仅差 1.4%，说明性能对重量与摩擦不敏感。

## 🔗 关联
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Human-taught sensory-control synergy for universal robotic grasping]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#强化学习 #力反馈 #柔顺夹爪 #仿真到现实迁移 #杂货抓取
