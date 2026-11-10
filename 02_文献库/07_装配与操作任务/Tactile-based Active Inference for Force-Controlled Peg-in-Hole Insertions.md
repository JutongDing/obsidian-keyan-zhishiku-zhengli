---
title: Tactile-based Active Inference for Force-Controlled Peg-in-Hole Insertions
year: 2023
doi: 
arxiv: 2309.15681
key: KB-150
venue: 待补（arXiv 预印本，正文未印会议/期刊名）
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 视触觉传感器, 主动推理, 力控制, 强化学习]
pdf: ../../../Tactile-based Active Inference for Force-Controlled Peg-in-Hole Insertions.pdf
confidence: high
source: pdf
aliases: []
---

# Tactile-based Active Inference for Force-Controlled Peg-in-Hole Insertions

## 📌 年份
2023

## 🔑 论文识别码
arXiv:2309.15681

## 👥 作者与所属院校
- 作者：Tatsuya Kamijo, Ixchel G. Ramirez-Alpizar, Enrique Coronado, Gentiane Venture 等（4 人）
- 机构：东京大学、产业技术综合研究所（AIST）、CNRS-AIST 联合机器人实验室（JRL）

## 📖 研究背景
- [[轴孔装配]]中夹爪遮挡视线、初始抓取位姿不确定，纯视觉力控策略常被迫假设 peg 刚性固定在末端。
- [[视触觉传感器]]能提供夹持面内的接触形状，但用它学触觉策略训练代价大、跨物体泛化差。
- 主动推理（active inference）把感知与动作统一为最小化自由能，适合小样本的位姿对齐。

## ❓ 需要解决的问题
- peg 在夹爪内滑动倾斜后，能否仅凭触觉图像推断 peg 相对末端的倾角？
- 不依赖大规模数据训练，触觉对齐策略能否与力控插入策略解耦协同？
- 在 0.08 mm 级间隙下，成功率能否显著超过无触觉基线？

## 📥📤 输入与输出
- 输入：双 GelSight Mini 触觉图像、peg 接触区形状、末端力/位置反馈与相对倾角观测量。
- 输出：对齐策略的末端姿态修正角、插入策略的末端位移与接触力指令。

## ✅ 论文最终达到的效果
- 双策略架构：插入侧用 PID 位置-力混合控制加 [[强化学习]]，对齐侧用主动推理按触觉预测误差更新倾角。
- 自数据增广：仅用一张直握触觉图旋转生成 1000 帧训练集，免去大规模触觉数据采集。
- 0.08 mm 间隙立方 peg 成功率 90%，无触觉基线仅 5%；0.3 mm 间隙滑轮任务 93%（37/40）。
- 五种不同 peg 上验证对齐策略可迁移；基线强插虽能到 70%，但会压坏触觉胶体。

## 🔗 关联
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]
- [[Active Touch Sensing for Robust Hole Detection in Assembly Tasks]]
- [[Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand]]

## 🏷️ 标签
#轴孔装配 #视触觉传感器 #主动推理 #力控制 #强化学习
