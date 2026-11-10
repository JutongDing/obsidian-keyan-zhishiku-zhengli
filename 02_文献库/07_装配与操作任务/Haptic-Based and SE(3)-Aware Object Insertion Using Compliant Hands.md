---
title: Haptic-Based and SE(3)-Aware Object Insertion Using Compliant Hands
year: 2023
doi: 10.1109/LRA.2022.3224670
arxiv: 
key: KB-071
venue: IEEE Robotics and Automation Letters
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 触觉一瞥, 力/力矩传感, 残差强化学习, 欠驱动柔顺手]
pdf: ../../../Haptic-Based_and_SE3-Aware_Object_Insertion_Using_Compliant_Hands.pdf
confidence: high
source: pdf
aliases: [Haptic-Based and SE3-Aware Object Insertion Using Compliant Hands]
---

# Haptic-Based and SE(3)-Aware Object Insertion Using Compliant Hands

## 📌 年份
2023（RA-L 第 8 卷第 1 期，208–215；2022 年 11 月在线）

## 🔑 论文识别码
DOI: 10.1109/LRA.2022.3224670

## 👥 作者与所属院校
- 作者：Osher Azulay、Maxim Monastirsky、Avishai Sintov（通讯）
- 机构：特拉维夫大学机械工程学院

## 📖 研究背景
- [[轴孔装配]]多在刚性手上研究，初始抓取误差与感知误差导致的间隙难以克服。
- 欠驱动柔顺手可被动适应环境，但会带来更大的物体位姿不确定性，接触力本身又添扰动。
- 该文仿人类“触觉一瞥”（haptic glance）：接触时主动激励手指，用力/力矩信息反推物体状态。

## ❓ 需要解决的问题
- 接触时对指尖施加扰动，能否比竖直按压或摆臂更准地定位接触、判断是否已插入？
- 仅用 F/T 与关节信息，能否估计并纠正物体相对孔的全部 SE(3) 位姿偏差（含滚转、俯仰）？
- 残差[[强化学习]]加课程学习能否在真机上高效学会精密插入，并泛化到未训练物体？

## 📥📤 输入与输出
- 输入：Robotiq FT-300 六维力/力矩（100 Hz）、指尖扰动序列、物体与孔的标称位姿。
- 输出：平面位移 Δx、Δy 与偏航 Δθ 动作，对滚转/俯仰倾角的隐式纠正，以及插入成功判定与所需触觉一瞥次数。

## ✅ 论文最终达到的效果
- 三种触觉一瞥原语中，指尖扰动定位误差最小、成功率最高，单次扰动约 4 s，被选为后续方案。
- 插入分类器用 1600 条训练样本，训练/测试物体准确率 97% 与 96%。
- 训练 320 回合（约 7 h 真机学习）后残差 RL + 课程学习在训练物体上成功率最高、所需触觉一瞥最少。
- 5 个未训练物体（含线轴、星形与花形棱柱）在 1.5 mm 间隙下可插入；初始误差 ±15 mm、±12° 及额外 ±10° 倾角均可纠正。

## 🔗 关联
- [[Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands]]
- [[Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand]]
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]

## 🏷️ 标签
#轴孔装配 #触觉一瞥 #力/力矩传感 #残差强化学习
