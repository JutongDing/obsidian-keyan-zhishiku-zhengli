---
title: Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing
year: 2023
doi: 
arxiv: 2304.05141
key: KB-040
venue: arXiv preprint (cs.RO)
theme: 02_文献库/08_学习与强化学习
tags: [手内操作, 触觉反馈, 深度强化学习, 仿真到现实迁移]
pdf: ../../../Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing.pdf
confidence: high
source: pdf
aliases: []
---

# Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing

## 📌 年份
2023

## 🔑 论文识别码
arXiv:2304.05141（无 DOI）

## 👥 作者与所属院校
- 作者：Wenbin Hu, Bidan Huang, Wang Wei Lee, Sicheng Yang, Yu Zheng 等
- 机构：英国爱丁堡大学信息学院、腾讯 Robotics X（深圳）、伦敦大学学院计算机科学系

## 📖 研究背景
- 细长圆柱（如长棍）的连续 [[手内操作]] 需三指协同滚动与滑移，接触区窄、对误差与不确定性极敏感。
- [[视触觉传感器]] 如 [[GelSight]]、[[DIGIT]] 需相机与标定、体积大；指尖分布式 [[触觉传感器]] 阵列更易集成，但原始高维读数难以直接进策略。
- 该文用触觉阵列估计的接触中心位置作为低维反馈，端到端训练 [[强化学习]] 策略，并借助标定与 [[域随机化]] 完成 [[仿真到现实迁移]]。

## ❓ 需要解决的问题
- 如何从三指高维触觉阵列中稳健估计长棍与指尖的接触中心位置？
- 仅以关节位置 + 接触中心为观测，能否学到跟踪直线、圆、8 字、螺旋等连续轨迹的策略？
- 仿真策略经模型标定与域随机化后，能否直接部署到真机而不掉棍？
- 接触中心位置反馈相比原始触觉或其他感知基线是否更有效？

## 📥📤 输入与输出
- 输入：TRX 三指手 8 个关节位置、三指触觉阵列读数（二值化接触 + 接触中心位置估计）、长棍目标位姿轨迹。
- 输出：8 个关节目标位置指令；高层策略 50 Hz，低层关节位置控制器 1 kHz。

## ✅ 论文最终达到的效果
- 仿真轨迹跟踪：直线端点误差 0.83 cm、朝向误差 1.80°；圆 0.97 cm/1.92°；8 字 1.16 cm/2.36°；螺旋最难，2.32 cm/5.90°。
- 未见过的目标角速度与半径（0.5π–1.5π rad/s、半径 1–3 cm）上性能与训练设定相当。
- 策略成功迁移到真机，实现长棍连续姿态跟踪；消融表明基于接触中心位置的触觉反馈优于其他感知基线。
- 传感器漂移通过每次试验前的空载均值标定（s(t)=max(s*(t)−s0,0)）补偿，保证接触判定可靠。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#手内操作 #触觉反馈 #深度强化学习 #仿真到现实
