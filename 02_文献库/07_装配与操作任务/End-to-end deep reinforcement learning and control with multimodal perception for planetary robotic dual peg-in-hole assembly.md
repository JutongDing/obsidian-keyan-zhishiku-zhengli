---
title: End-to-end deep reinforcement learning and control with multimodal perception for planetary robotic dual peg-in-hole assembly
year: 2024
doi: 10.1016/j.asr.2024.08.028
arxiv: 
key: KB-046
venue: Advances in Space Research, 74(11), 5860-5873
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 强化学习, 多模态感知, 行星建造, DDPG]
pdf: ../../../End-to-end Deep Reinforcement Learning and Control with Multimodal Perception for Planetary Robotic Dual Peg-in-Hole Assembly.pdf
confidence: high
source: pdf
aliases: []
---

# End-to-end deep reinforcement learning and control with multimodal perception for planetary robotic dual peg-in-hole assembly

## 📌 年份
2024（ASR 第 74 卷，5860–5873）

## 🔑 论文识别码
DOI: 10.1016/j.asr.2024.08.028

## 👥 作者与所属院校
- 作者：Boxin Li, Zhaokui Wang
- 机构：清华大学航天航空学院

## 📖 研究背景
- 行星基地建造（NASA MMPACT、中国载人探月）要求机器人自主装配，对少人工干预的控制方法提出需求。
- 行星环境非结构化，构件几何与[[接触状态识别]]先验未知，地面工业[[轴孔装配]]的固定接触模型难以直接迁移。
- 双轴孔装配接触交互复杂、通用性强，被选为方法验证对象。

## ❓ 需要解决的问题
- 能否由 RGB-D 观测端到端输出连续动作（[[强化学习]]策略），跳过人工接触建模与状态分类？
- 如何设计分阶段奖励，兼顾自由空间趋近的稠密引导与接触后插入的稀疏成功判定？
- 仿真训练的策略能否经[[仿真到现实迁移]]部署到地面真机，并借真机图像持续进化？

## 📥📤 输入与输出
- 输入：RGB-D 图像（RealSense D435i）、末端位姿、力反馈、视觉虚拟目标点与插入深度。
- 输出：末端 6 维连续动作（Vision-DDPG 策略），完成双轴对孔与插入。

## ✅ 论文最终达到的效果
- 约 2.2k 轨迹样本后分阶段奖励收敛：0–800 回合奖励趋近 1（逼近虚拟目标点），800–2200 回合稳定在 2（完成装配）。
- CoppeliaSim 训练的策略经 ROS 接口部署到 UR3 真机，完成地面双轴孔装配。
- 用真机采集的 RGB-D 图像回流仿真做融合训练，形成数据持续累积的策略进化链路。
- 结论为可行性与有效性验证，未给出量化成功率。

## 🔗 关联
- [[Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands]]
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]
- [[Active Touch Sensing for Robust Hole Detection in Assembly Tasks]]

## 🏷️ 标签
#轴孔装配 #强化学习 #多模态感知 #行星建造
