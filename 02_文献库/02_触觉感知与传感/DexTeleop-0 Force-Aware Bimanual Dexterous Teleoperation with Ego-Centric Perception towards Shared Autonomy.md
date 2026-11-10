---
title: "DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy"
year: 2026
doi: 
arxiv: 2606.23431
key: KB-162
venue: arXiv 预印本（cs.RO，2026-06-22；会议/期刊待补）
theme: 02_文献库/02_触觉感知与传感
tags: [主从遥操作, 触觉反馈, 双臂灵巧操作, 共享自治, 力柔顺]
pdf: ../../../dexteleop.pdf
confidence: high
source: pdf
aliases: []
---

# DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2606.23431（PDF 未印 DOI）

## 👥 作者与所属院校
- 作者：Haichao Liu, Yuyao Jiang, Hyunsun Park, Yuanjiang Xue, Ziwei Wang
- 机构：新加坡南洋理工大学、OOJU（美国）

## 📖 研究背景
- 精细双臂灵巧操作仍是机器人基础难题，接触丰富任务尤其依赖高质量反馈回路。
- 传统[[主从遥操作]]存在人-机具身差距，运动学映射不准，易产生破坏性接触力。
- 纯视觉跟踪管线缺触觉与力反馈，高精度操作的数据采集效率极低。
- 该文在遥操作管线上叠加触觉驱动的实时力平衡残差优化，实现共享自治。

## ❓ 需要解决的问题
- 如何把粗粒度的人体跟踪意图转成精确且力柔顺的机器人指令？
- 只用触觉接触点估计与指尖力廓线，能否在线估计并补偿具身差距？
- 力平衡残差优化能否在双臂手 56 个自由度上实时收敛？
- 相比位置绑定与关节级分散控制基线，接触力与分阶段成功率改善多少？

## 📥📤 输入与输出
- 输入：VR 头显的第一视角手部跟踪、指尖触觉力与接触点估计、关节角。
- 输出：双臂手 56 个自由度的关节角增量，按操作空间[[雅可比矩阵]]转成局部修正。

## ✅ 论文最终达到的效果
- 齿轮啮合任务二级装配成功率 57.14%，位置基线 11.43%、PD 控制 37.14%。
- 插销任务一级捕获成功率 97.14%，二级插入完成率 60.00%。
- 食物分拣任务四阶段末端成功率 74.29%，平均接触力 4.94±1.80 N，为各法最低。
- 长时序试管操作二级 100.00%、三级 77.14%，位置基线三级仅 34.29%。
- 搅拌任务无残差方案接触力 15.56±6.59 N，该文 7.93±2.67 N，约为前者一半。

## 🔗 关联
- [[Finger contact sensing and the application in dexterous hand manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]

## 🏷️ 标签
#主从遥操作 #触觉反馈 #双臂灵巧操作 #共享自治 #力柔顺
