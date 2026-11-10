---
title: "3D tactile servo control: a peg-in-hole strategy for hole with dynamic random motion"
year: 2026
doi: 10.1108/IR-11-2024-0510
arxiv: 
key: KB-004
venue: "Industrial Robot: the international journal of robotics research and application, Vol. 53, No. 1"
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 触觉伺服, 动态孔, 孔搜索, 空间装配]
pdf: ../../../3D tactile servo controla peg-in-hole strategy.pdf
confidence: high
source: pdf
aliases: []
---

# 3D tactile servo control: a peg-in-hole strategy for hole with dynamic random motion

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1108/IR-11-2024-0510

## 👥 作者与所属院校
- 作者：Haoxun Lin, Yu Xie, Haibo Zhang, Minghang Liu, Yiwei Chen 等（7 人）
- 机构：厦门大学萨本栋微米纳米科学技术研究院、北京控制工程研究所、中石化石油化工科学研究院

## 📖 研究背景
- 空间装配中微重力使目标件随机漂移，静止孔位假设下的传统[[轴孔装配]]策略直接失效。
- 在轨装配风险高，需先建地面可动孔平台，验证动态装配这一步的可行性。
- 该文用夹持 peg 的指内触觉（卷曲量 curl 与压力中心 CoP）构造三维[[触觉伺服]]。

## ❓ 需要解决的问题
- 仅凭指内触觉信息，能否实时跟踪孔平台的随机运动而不依赖外部视觉？
- 动态孔搜索如何设计接触探索与搜索轨迹，才能兼顾成功率与耗时？
- 相对基线，成功率与任务耗时能否同时改善，插入碰撞力是否下降？

## 📥📤 输入与输出
- 输入：指内触觉传感器的 curl 与压力中心（CoP）信号、机器人关节位姿与速度。
- 输出：末端速度/位置修正量（触觉伺服）、指数增长正弦搜索轨迹与插入动作序列。

## ✅ 论文最终达到的效果
- 30 次试验成功率 90%，基线为 73.33%；任务耗时下降 26.5%。
- 触觉伺服控制器实现对孔平台随机运动的快速、稳定跟踪。
- 主动接触探索 + 指数增长正弦轨迹提升了动态孔搜索的成功率与效率。
- 插入过程中 peg 与孔的碰撞力和碰撞频次均下降，属于[[接触状态识别]]驱动的柔顺插入。
- 文中含消融实验；后续拟把孔平台运动由平面扩展到三维空间。

## 🔗 关联
- [[Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands]]
- [[Active Touch Sensing for Robust Hole Detection in Assembly Tasks]]
- [[Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand]]

## 🏷️ 标签
#轴孔装配 #触觉伺服 #动态孔 #孔搜索 #空间装配
