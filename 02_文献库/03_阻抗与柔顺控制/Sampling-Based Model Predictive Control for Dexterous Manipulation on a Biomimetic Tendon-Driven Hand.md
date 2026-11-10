---
title: Sampling-Based Model Predictive Control for Dexterous Manipulation on a Biomimetic Tendon-Driven Hand
year: 2025
doi: 
arxiv: 2411.06183
key: KB-128
venue: arXiv 预印本（cs.RO，v3 2025-08；会议/期刊待补）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [采样MPC, 视觉语言模型, 仿生灵巧手, 腱驱动, 手内操作]
pdf: ../../../Sampling-Based Model Predictive Control for Dexterous.pdf
confidence: high
source: pdf
aliases: []
---

# Sampling-Based Model Predictive Control for Dexterous Manipulation on a Biomimetic Tendon-Driven Hand

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2411.06183

## 👥 作者与所属院校
- 作者：Adrian Hess, Alexander M. Kübler, Benedek Forrai, Mehmet Dogar, Robert K. Katzschmann
- 机构：苏黎世联邦理工学院（ETH Zurich）、英国利兹大学（University of Leeds）

## 📖 研究背景
- 仿生柔性[[灵巧手]]（[[腱驱动]]滚动接触关节）自由度高、接触复杂、状态估计不确定，控制难度远高于刚性夹爪。
- 采样型模型预测控制（MPC）以物理仿真器为动力学模型，无需长训练，但代价函数仍需人工反复调参。
- 该文把视觉语言模型（GPT-4o）接入 MuJoCo MPC，据视频反馈自动改写代价权重。

## ❓ 需要解决的问题
- 采样 MPC 能否在存在状态不确定性的实体柔性手上稳定运行，而非只在仿真中奏效？
- VLM 能否替代人工试错，从任务描述与行为视频中自动设计代价项与权重？
- 自动调参的效果能否超过穷举搜索，且耗时更短？

## 📥📤 输入与输出
- 输入：任务的自然语言描述、手部行为视频（10 s）、腱长测量与扩展卡尔曼滤波估计的关节角、MuJoCo 中 Faive 手模型。
- 输出：采样 MPC 最优控制序列，经几何模型换算为 11 自由度手的腱长目标。

## ✅ 论文最终达到的效果
- 每次 VLM 迭代约 2 min；4 轮进化（8 min）即完成调参，而穷举搜索需 121 组权重 × 10 min（20+ 小时）。
- 球体滚动：绕 ±x、±y、z 各向角速度 0.96–1.01 rad/s，球始终未掉落。
- 抛翻：VLM 版翻转高度 14.0 cm、91 次/分（穷举版 9.6 cm、48 次/分），但掉落更频繁（33 次/分）。
- 仿真与实体 Faive 手（11 DoF）上均演示滚动、抛翻与接球，属该手首次实机[[手内操作]]。
- 仍是可行性验证：掉落率偏高、未做定量成功率统计，且依赖仿真模型精度。

## 🔗 关联
- [[Non-Parametric Self-Identification and Model Predictive Control of Dexterous In-Hand Manipulation]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]
- [[Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control]]

## 🏷️ 标签
#采样MPC #视觉语言模型 #仿生灵巧手 #腱驱动 #手内操作
