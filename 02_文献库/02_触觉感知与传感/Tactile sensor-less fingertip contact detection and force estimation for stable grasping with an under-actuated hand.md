---
title: Tactile sensor-less fingertip contact detection and force estimation for stable grasping with an under-actuated hand
year: 2024
doi: 10.1186/s40648-024-00273-3
arxiv: 
key: KB-149
venue: ROBOMECH Journal, Vol. 11, Article 5
theme: 02_文献库/02_触觉感知与传感
tags: [无外置传感器, 接触检测, 指尖力估计, 欠驱动手, DBSCAN]
pdf: ../../../Tactile sensor-less fingertip contact detection and force estimation for stable grasping with an under-actuated hand.pdf
confidence: high
source: pdf
aliases: []
---

# Tactile sensor-less fingertip contact detection and force estimation for stable grasping with an under-actuated hand

## 📌 年份
2024

## 🔑 论文识别码
DOI: 10.1186/s40648-024-00273-3

## 👥 作者与所属院校
- 作者：Ha Thang Long Doan, Hikaru Arita, Kenji Tahara 等（3 人）
- 机构：九州大学工学研究院

## 📖 研究背景
- 连杆式[[欠驱动手]]带自锁机构，成本低、出力大，但运动学与动力学强非线性，精细抓取难建模。
- 外置[[指尖力传感器]]会抬高成本、增加走线与装配难度，量产场景倾向不加。
- 只靠机器人模型反解接触力误差大，只靠纯数据驱动又缺物理约束，二者单独都不够。

## ❓ 需要解决的问题
- 仅用编码器、丝杠位置与指节 load cell 等内置信号，能否实时判定指尖与物体的接触时刻？
- 同一套内置信号能否在接触后实时估计指尖力，精度足以支撑力闭环？
- 把接触检测与力估计接进抓取控制器后，能否在三指手上维持物体力/力矩平衡？

## 📥📤 输入与输出
- 输入：丝杠位置编码器、手指转角编码器、指节内置 load cell 读数等手内传感器时序数据。
- 输出：各指接触标志 Contact₁,₂,₃、指尖力估计值、指尖力 PID 指令与指旋转角指令。

## ✅ 论文最终达到的效果
- 接触检测用 DBSCAN 对预先采集的非接触数据聚类、离线调参，在线判定偏离即判为接触。
- 力估计用加权平均把模型中难建模部分替换为数据驱动项，降低模型假设与传感器噪声影响。
- 三指 Jinki Hand 上完成接近—闭合—平衡—保持全流程，指尖力估计值跟踪到期望值。
- 抓稳后施加 10–15 N 水平外扰，手指自动调整力与角度，物体不脱落，扰动撤除后回到原位。

## 🔗 关联
- [[Finger contact sensing and the application in dexterous hand manipulation]]
- [[In-Hand Object-Dynamics Inference using Tactile Fingertips]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#无外置传感器 #接触检测 #指尖力估计 #欠驱动手 #抓取控制
