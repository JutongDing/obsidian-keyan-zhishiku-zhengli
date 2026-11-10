---
title: Just Add Force for Contact-Rich Robot Policies
year: 2024
doi: 
arxiv: 2410.13124
key: KB-079
venue: arXiv 预印本（2024-10-17，正式发表信息待补）
theme: 02_文献库/08_学习与强化学习
tags: [扩散策略, 力反馈, 易碎物体抓取, 电流测力, 数据集]
pdf: ../../../Just Add Force for Contact-Rich Robot Policies.pdf
confidence: high
source: pdf
aliases: []
---

# Just Add Force for Contact-Rich Robot Policies

## 📌 年份
2024（arXiv v1，2024-10-17）

## 🔑 论文识别码
arXiv: 2410.13124（原文无 DOI，正式发表信息待核对）

## 👥 作者与所属院校
- 作者：William Xie, Stefan Caldararu, Nikolaus Correll
- 机构：科罗拉多大学博尔德分校

## 📖 研究背景
- 机器人基础模型的数据多为图像、语言、末端位姿与二值夹爪开合，缺夹持力信息。
- 二值开合无法胜任软质果蔬、纸容器、干粮等易碎易变形物体的细粒度[[抓取力调节]]。
- 专用力/触觉传感器成本高且需改硬件，难以并入大规模数据集。
- 该文用电机电流估计夹持力，采集带力轨迹并蒸馏为扩散策略。

## ❓ 需要解决的问题
- 无需额外硬件的电流式力估计能否支撑易碎物体抓取？
- 带力（forceful）与仅位置两种扩散策略在易碎物体上差距多大？
- 130 条轨迹、30 个物体的小数据能否泛化到未见物体？
- 带力策略能否在保持成功率的同时降低推理时延？

## 📥📤 输入与输出
- 输入：腕部 RGB-D 图像、任务指令、末端位姿、连续夹爪位置与电流做的[[接触力估计]]。
- 输出：连续夹爪位置与施加夹持力动作序列（每次抓取 15 步 rollout）。

## ✅ 论文最终达到的效果
- 数据集：130 条成功抓取轨迹、30 个物体（1–500 g），5 Hz 采集，RLDS 格式公开。
- 平台：UR5 + MAGPIE 夹爪 + D405/D435 相机；靠电流估力，无需额外力传感器。
- 易碎物体 10 物×10 次：带力策略成功率 82%（示教过 85%、未见 80%），仅位置策略 54%（45%、60%）。
- 每次抓取 15 步 @4 Hz 即 3.75 s，较 LLM 法 14.11 s 快 3.76 倍。
- 带力策略从 0.15 N 起增力，仅位置策略恒加 2 N，后者失败多为压溃变形。
- 局限：仅在静止抓取段评估，未做运动中自适应抓取；数据规模小。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#扩散策略 #力反馈 #易碎物体抓取 #电流测力 #数据集
