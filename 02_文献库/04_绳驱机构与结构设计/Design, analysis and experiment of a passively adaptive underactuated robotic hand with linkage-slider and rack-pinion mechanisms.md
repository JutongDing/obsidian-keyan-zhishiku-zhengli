---
title: Design, analysis and experiment of a passively adaptive underactuated robotic hand with linkage-slider and rack-pinion mechanisms
year: 2021
doi: 10.1016/j.mechmachtheory.2020.104092
arxiv: 
key: KB-038
venue: Mechanism and Machine Theory, 155, 104092
theme: 02_文献库/04_绳驱机构与结构设计
tags: [欠驱动手, 连杆滑块机构, 齿轮齿条传动, 静力学建模]
pdf: ../../../Design, analysis and experiment of a passively adaptive underactuated robotic hand with linkage-slider and rack-pinion mechanisms.pdf
confidence: high
source: pdf
aliases: []
---

# Design, analysis and experiment of a passively adaptive underactuated robotic hand with linkage-slider and rack-pinion mechanisms

## 📌 年份
2021

## 🔑 论文识别码
DOI: 10.1016/j.mechmachtheory.2020.104092

## 👥 作者与所属院校
- 作者：Daoming Wang, Yan Xiong, Bin Zi, Sen Qian, Zhengyu Wang 等
- 机构：合肥工业大学机械工程学院、美国马里兰大学巴尔的摩郡分校机械工程系

## 📖 研究背景
- 全驱动 [[灵巧手]] 关节自由度多，但驱动器数量带来重量与控制复杂度急剧上升，成本高、维护难。
- [[欠驱动手]] 用少量驱动器换取多自由度，却普遍存在指尖抓取力弱、强力抓取与 [[自适应抓取]] 难以兼顾的矛盾。
- 该文以连杆-滑块与齿轮齿条复合传动构建五指欠驱动手，试图用简单机构同时获得强指尖力与包络自适应能力。

## ❓ 需要解决的问题
- 仅用 6 个直流伺服电机如何驱动五指手，并实现指尖、包络、侧接触三类抓取模式？
- 连杆-滑块与齿轮齿条耦合下，三指节的运动耦合比是否接近人手？
- 指节接触力如何随接触位置与弯曲角变化，静力学模型能否准确预测？
- 低成本样机能否稳定抓取不同形状与尺寸的物体？

## 📥📤 输入与输出
- 输入：6 个电机的输出力矩与转角、目标抓取模式、被抓物体的几何位形。
- 输出：各指节关节角轨迹、指尖与各指节接触力、抓取位姿及手指工作空间。

## ✅ 论文最终达到的效果
- 样机尺寸与人手相当，由 6 个 DC 伺服电机驱动五指，可完成指尖抓取、掌部包络抓取与侧接触抓取。
- 指尖抓取实验：输入力矩 2400 N·mm 时，接触力理论值 17.3 N、实测稳定值约 18.7 N。
- 自适应抓取实验：近节/中节/远节理论接触力 3.5/0/9.1 N，实测 2.9/0/9.0 N，静力学模型得到验证。
- 运动学仿真显示三指节运动耦合比与人类手在整个抓取过程中基本一致，工作空间计算验证了可达性。
- 完成方块等物体的多模式抓取实验，说明机构兼具较强指尖力与被动适应能力。

## 🔗 关联
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]

## 🏷️ 标签
#欠驱动手 #连杆滑块 #齿轮齿条 #静力学 #机构设计
