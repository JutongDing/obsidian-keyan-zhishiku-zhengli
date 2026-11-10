---
title: "Construction of a Multiple-DOF Under-actuated Gripper with Force-Sensing via Deep Learning"
year: 2024
doi: 
arxiv: 
key: KB-031
venue: Robotics: Science and Systems (RSS) 2024, Delft
theme: 02_文献库/04_绳驱机构与结构设计
tags: [欠驱动夹爪, 连杆机构, 力反馈控制, LSTM, 抓取模式切换]
pdf: ../../../Construction of a Multiple-DOF Under-actuated.pdf
confidence: high
source: pdf
aliases: []
---

# Construction of a Multiple-DOF Under-actuated Gripper with Force-Sensing via Deep Learning

## 📌 年份
2024

## 🔑 论文识别码
KB-031（本地编号；RSS 2024 论文，无 DOI）

## 👥 作者与所属院校
- 作者：Jihao Li, Keqi Zhu, Guodong Lu, I-Ming Chen, Huixu Dong（通讯）
- 机构：浙江大学 Grasp Lab 与机器人研究所、南洋理工大学机器人研究中心

## 📖 研究背景
- 现有 [[欠驱动手]] 普遍存在负载小、抓取力小、力感知不足、稳定性弱、成本高的问题。
- 多数产品只能单一抓取模式，可抓物体的尺寸范围受限，两指节手指也难以构成 [[形封闭]]。
- 间接力感知多依赖软体或连续体结构的变形模型，刚性欠驱动夹爪上难以照搬。

## ❓ 需要解决的问题
- 能否用单驱动器同时实现平行抓取与包络抓取的自动切换，扩大尺寸适应范围？
- 不加装力传感器，如何从电机电流估计指端接触力并做闭环 [[抓取力调节]]？
- 该机构在负载、抓取力、力感知精度与稳定性上能否超过商用 Robotiq85？

## 📥📤 输入与输出
- 输入：单电机驱动电流与编码器角度、五连杆机构的关节角、目标抓取力设定值。
- 输出：抓取模式判定（平行/包络）、指节接触力估计值与电机力控指令。

## ✅ 论文最终达到的效果
- 机构为五连杆叠双四杆的两指三关节（6 自由度）夹爪，靠 screw-nut 副传动，单电机驱动。
- 建立运动学与功率传递模型，可算指节位置与接触力；提出 MS-LSTM 分类器做 [[接触力估计]]，无需力传感器。
- 力感知误差小于 3%，而 Robotiq85 依赖电流估计的误差约 10%。
- 平行抓取时径向负载 150 N（约 15 kg）、轴向 180 N（约 18 kg）；最大径向抓取力设定 250 N，实验中记录到约 350 N 峰值。
- 法向最大抓取力超过 105 N，径向与轴向分别约为 Robotiq85 的 7 倍与 5 倍。
- 能抓工具、眼镜等不规则物体；薄片类（桌上的纸）仍会失败。

## 🔗 关联
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]

## 🏷️ 标签
#欠驱动夹爪 #连杆机构 #力反馈控制 #LSTM #抓取模式切换
