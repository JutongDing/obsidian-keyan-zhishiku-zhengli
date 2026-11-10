---
title: "Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning"
year: 2026
doi: 
arxiv: 2603.26660
key: KB-126
venue: arXiv 预印本（cs.RO，v2 2026-03）
theme: 02_文献库/04_绳驱机构与结构设计
tags: [开源灵巧手, 腱驱动, 并联腕, 外展内收, 遥操作]
pdf: ../../../Ruka-v2.pdf
confidence: high
source: pdf
aliases: []
---

# Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2603.26660

## 👥 作者与所属院校
- 作者：Xinqi (Lucas) Liu, Ruoxi Hu, Alejandro Ojeda Olarte, Zhuoran Chen, Kenny Ma 等
- 机构：纽约大学（New York University）、上海纽约大学（NYU Shanghai）

## 📖 研究背景
- 硬件是达成人类级灵巧度的瓶颈：[[灵巧手]]直驱方案体积大、重，微型直驱手易过热或价格高。
- 上一代 Ruka 为全开源[[腱驱动]]人形手，11 个自由度（每指 2、拇指 3），成本低于 1300 美元，但缺腕部运动与手指外展/内收。
- 该文补上解耦的 2 自由度并联腕与手指外展，面向遥操作与策略学习。

## ❓ 需要解决的问题
- 并联腕能否独立、平滑地实现屈伸与桡/尺偏，并在柜内等受限空间完成操作？
- 外展/内收自由度是否解锁细薄物体抓取、手内旋转与书写等动作？
- 开源硬件配合数据驱动腱控制，能否形成可复现的机器人学习平台？

## 📥📤 输入与输出
- 输入：[[主从遥操作]]或示教指令、腱长测量与电机指令、手指外展与腕部目标。
- 输出：各关节/腱长控制量；并输出 13 项灵巧任务的遥操作数据与 3 项任务的自主策略。

## ✅ 论文最终达到的效果
- 与 Ruka 的遥操作用户研究对比：完成任务时间减少 51.3%，成功率提升 21.2%。
- 支持双臂与单臂遥操作共 13 项灵巧任务，并在 3 项任务上完成自主策略学习。
- 2 自由度并联腕提供平滑独立的屈伸与桡/尺偏，可在柜内等局促空间操作。
- 外展使细薄物体抓取、[[手内操作]]式旋转与书写成为可能。
- 全部 3D 打印文件、装配说明、控制软件与视频开源（ruka-hand-v2.github.io）。

## 🔗 关联
- [[An open-source anthropomorphic robot hand system HRI hand]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]

## 🏷️ 标签
#开源灵巧手 #腱驱动 #并联腕 #外展内收 #遥操作
