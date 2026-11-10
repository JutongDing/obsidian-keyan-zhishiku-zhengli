---
title: Characterization, Analytical Planning, and Hybrid Force Control for the Inspire RH56DFX Hand
year: 2026
doi: 
arxiv: 2603.08988
key: KB-166
venue: arXiv 预印本（cs.RO）
theme: 02_文献库/01_灵巧手抓取规划
tags: [灵巧手, 硬件标定, 抓取规划, 力位混合控制, 轴孔装配]
pdf: ../../../inspire_RH56DFX.pdf
confidence: high
source: pdf
aliases: [Inspire RH56DFX 标定与力控]
---

# Characterization, Analytical Planning, and Hybrid Force Control for the Inspire RH56DFX Hand

## 📌 年份
2026（arXiv:2603.08988v1，2026-03-09）

## 🔑 论文识别码
arXiv:2603.08988

## 👥 作者与所属院校
- 作者：Xuan Tan, William Xie, Nikolaus Correll
- 机构：美国科罗拉多大学博尔德分校（University of Colorado Boulder）

## 📖 研究背景
- 商用[[灵巧手]]价格与可及性优于研究平台，但只暴露未标定的本体信号（力读数 0–1000、无量纲），难以作为科研仪器使用。
- Inspire RH56DFX 有六个驱动自由度，高速接触时力超调最高达 +1618%，经典方法难以直接套用。
- 其欠驱动耦合连杆把运动约束在圆弧上，对跖抓取需随物体宽度（110/55/0 mm）做最多 49° 的平移-旋转修正。

## ❓ 需要解决的问题
- 能否把原始力读数标定为牛顿量级，并定量给出延迟与超调？
- 耦合连杆下，"物体宽度→[[抓取位姿]]"的解析映射能否建模并经 sim2real 验证？
- 混合速度-力闭环控制器能否在[[轴孔装配]]与多样物体抓取上超过仅用手腕力反馈的基线？

## 📥📤 输入与输出
- 输入：手指力原始读数（0–1000）、关节角、物体宽度或点云；可外接检测器与视觉-语言模型估计宽度与目标力。
- 输出：带旋转-平移修正的抓取位姿、各指目标力与速度指令、逐指力与[[力封闭]]诊断量。

## ✅ 论文最终达到的效果
- 力标定 R² > 0.98，端到端延迟 66 ms，并量化了 +1618% 的力超调。
- MuJoCo 模型经 sim2real 验证，可做解析式宽度→抓取规划。
- 轴孔装配成功率 65%，手腕力反馈基线仅 10%。
- 15 类物体共 300 次抓取成功率 87%，优于免规划抓取与学习型抓取。
- 方法模块化、可解释，代码与模型开源。

## 🔗 关联
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]
- [[Force Feedback Control For Dexterous Robotic Hands Using Conditional Postural Synergies]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#灵巧手 #硬件标定 #抓取规划 #力位混合控制
