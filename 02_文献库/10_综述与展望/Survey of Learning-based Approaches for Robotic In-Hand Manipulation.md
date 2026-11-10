---
title: Survey of Learning-based Approaches for Robotic In-Hand Manipulation
year: 2024
doi: 
arxiv: 2401.07915
key: KB-139
venue: arXiv 预印本（v2 2024-10-24，待补）
theme: 02_文献库/10_综述与展望
tags: [综述, 手内操作, 强化学习, 模仿学习, 模型学习]
pdf: ../../../Survey of Learning-based Approaches for Robotic.pdf
confidence: high
source: pdf
aliases: []
---

# Survey of Learning-based Approaches for Robotic In-Hand Manipulation

## 📌 年份
2024（v1 2024-01，v2 2024-10-24）

## 🔑 论文识别码
arXiv: 2401.07915（无 DOI）

## 👥 作者与所属院校
- 作者：Abraham Itzhak Weinberg, Alon Shirizly, Osher Azulay, Avishai Sintov
- 机构：AI-Weinberg AI Experts、以色列理工学院机械工程系、特拉维夫大学机械工程学院

## 📖 研究背景
- [[手内操作]]长期被视为机器人难题：早期按预设轨迹执行，随后转向解析运动学与接触建模。
- 解析方法难以应对复杂环境与不确定性，研究重心因此转向从真实或仿真数据中学习。
- 近五年相关论文数量快速上升，但缺少横跨手型、接触模式与算法族系的系统梳理。

## ❓ 需要解决的问题
- 学习类手内操作方法应怎样分类，才能同时覆盖手型、任务与算法三个层面？
- 灵巧手（高自由度、连续接触）与非灵巧手路线在技术积累与产出上差距多大？
- 模型学习、[[强化学习]]、[[模仿学习]]三类子领域的适用条件与主要瓶颈分别是什么？
- 仿真平台与数据集能否支撑可复现的横向比较？

## 📥📤 输入与输出
- 输入：近年手内操作研究文献（算法、任务、平台、数据集、应用场景）。
- 输出：分类体系与路线图——灵巧/非灵巧手 × 连续/非连续接触 × 模型学习/RL/IL，并给出开放问题清单。

## ✅ 论文最终达到的效果
- 作者称这是首篇专门针对「学习类手内操作」的综述，按三维度归并文献并给出对照表。
- 结论：灵巧手路线在算法数量与论文产出上更活跃，连续接触类方法技术储备更丰富。
- 梳理模型学习（状态表征与动力学监督学习）、RL（奖励驱动自学习）、IL（示教模仿）三条主线。
- 指出瓶颈：RL 泛化与多任务弱、模型法受动态环境复杂度限制、IL 依赖大量高质量示教。
- 展望方向：手型无关的少样本/零样本泛化、假肢手复杂任务、轻量多模态融合、人机协作中持续学习。

## 🔗 关联
- [[Dexterous Manipulation for Multi-Fingered Robotic Hands With Reinforcement Learning A Review]]
- [[An overview of learning-based dexterous grasping recent advances and future directions]]
- [[Interactive imitation learning for dexterous robotic manipulation challenges and perspectives—a survey]]

## 🏷️ 标签
#综述 #手内操作 #强化学习 #模仿学习 #灵巧手
