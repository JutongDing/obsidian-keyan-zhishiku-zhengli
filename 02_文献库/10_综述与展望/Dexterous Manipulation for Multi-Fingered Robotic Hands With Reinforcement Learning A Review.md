---
title: "Dexterous Manipulation for Multi-Fingered Robotic Hands With Reinforcement Learning: A Review"
year: 2022
doi: 10.3389/fnbot.2022.861825
arxiv: 
key: KB-041
venue: Frontiers in Neurorobotics, 16, 861825
theme: 02_文献库/10_综述与展望
tags: [综述, 强化学习, 多指手, 示教学习, 仿真到现实]
pdf: ../../../Dexterous_Manipulation_for_Multi-Fingered_Robotic_.pdf
confidence: high
source: pdf
aliases: [Dexterous_Manipulation_for_Multi-Fingered_Robotic_.pdf]
---

# Dexterous Manipulation for Multi-Fingered Robotic Hands With Reinforcement Learning: A Review

## 📌 年份
2022

## 🔑 论文识别码
DOI: 10.3389/fnbot.2022.861825

## 👥 作者与所属院校
- 作者：Chunmiao Yu, Peng Wang
- 机构：中国科学院自动化研究所、中国科学院大学人工智能学院、中科院脑科学与智能技术卓越创新中心、中科院香港创新研究院人工智能与机器人中心

## 📖 研究背景
- 多指手操作自由度与控制复杂度高，早期基于模型的方法依赖精确的 [[动力学建模]] 与接触模型，难以适应非结构化与非制造场景。
- [[强化学习]] 提供无模型的学习途径，但样本效率低、奖励设计难，仿真策略又存在显著的现实差距。
- 该文系统梳理从无学习模型方法到 RL 及其变体（示教、迁移）的演进，为该方向提供路线图。

## ❓ 需要解决的问题
- 多指手灵巧操作的 RL 方法可如何分类，各自适配哪些任务、观测与动作空间？
- 示范学习与迁移学习如何缓解数据低效与 [[仿真到现实迁移]] 难题？
- 仿真器保真度、多传感器融合、奖励与课程设计的关键瓶颈在哪里？
- 该领域下一步值得投入的方向是什么？

## 📥📤 输入与输出
- 输入：多指手灵巧操作、[[模仿学习]]、sim2real 等相关文献集合。
- 输出：方法分类体系与代表性工作总结、各方法优劣对比、开放挑战与未来方向清单。

## ✅ 论文最终达到的效果
- 将方法归纳为基于模型（无学习）、纯 RL、RL from demonstration、仿真到现实迁移四类，并逐一比较适用范围。
- 指出数据低效是 RL 落地的主要障碍，[[模仿学习]] 与迁移学习是当前最常用的缓解手段。
- 归纳出仿真器精度与速度不足、传感器（视觉+触觉）融合不充分、奖励与课程设计依赖人工等开放问题。
- 提出更先进仿真器、多模态传感融合、提升样本效率与真实环境泛化等未来方向；属定性综述，无统一实验指标。

## 🔗 关联
- [[A comprehensive review of dexterous robotic hands design, implementation, and evaluation]]
- [[A Review of Modeling of Soft-Contact Fingers and Stiffness Control for Dextrous Manipulation in Robotics]]
- [[A Review of Robotic Dexterous Hands]]

## 🏷️ 标签
#综述 #强化学习 #多指手操作 #仿真到现实
