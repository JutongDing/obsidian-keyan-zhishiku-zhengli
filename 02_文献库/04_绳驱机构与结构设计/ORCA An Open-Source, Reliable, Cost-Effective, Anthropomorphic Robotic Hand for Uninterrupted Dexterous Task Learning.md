---
title: "ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning"
year: 2025
doi: 
arxiv: 2504.04259
key: KB-168
venue: arXiv 预印本（cs.RO，v2）
theme: 02_文献库/04_绳驱机构与结构设计
tags: [灵巧手, 腱驱动, 开源硬件, 触觉传感, 仿真到现实迁移]
pdf: ../../../orca.pdf
confidence: high
source: pdf
aliases: [ORCA hand, orca]
---

# ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2504.04259

## 👥 作者与所属院校
- 作者：Clemens C. Christoph, Maximilian Eberlein, Filippos Katsimalis, Arturo Roberti, Aristotelis Sympetheros 等
- 机构：苏黎世联邦理工学院软体机器人实验室（ETH Zurich, Soft Robotics Lab）

## 📖 研究背景
- 通用机器人需要类人灵巧度；类人形制还可直接复用人类手-物交互的大规模数据集。
- 瓶颈不只在软件：接近人手的商用手价格高昂、体积大、依赖企业级维护，阻碍社区复现与长期实验。
- 该文追问"能否一天内就开始用可靠灵巧手做研究"，走低成本开源硬件路线。

## ❓ 需要解决的问题
- 17 自由度[[腱驱动]]结构能否由个人在 8 小时内装好、物料成本低于 2000 瑞士法郎？
- 崩开式关节、自标定与张紧机构能否同时降低复杂度并提升精度、可靠性与鲁棒性？
- 集成触觉与自标定能否支撑[[主从遥操作]]、[[模仿学习]]与零样本[[仿真到现实迁移]]？

## 📥📤 输入与输出
- 输入：遥操作关节指令、人类示范轨迹、仿真中 4096 个并行手模型的状态；指尖二值触觉与电机电流。
- 输出：各关节电机位置指令（含自标定得到的关节映射与张紧补偿）。

## ✅ 论文最终达到的效果
- 17 自由度，装配少于 8 小时，物料成本低于 2000 CHF，设计与代码全部开源。
- 四指握持载荷 10.5 kg（103 N），仅用食指 2 kg（19.6 N）。
- 连续运行超过 10,000 个作业循环（约 20 小时）无硬件失效。
- IsaacGym 中 4096 手并行、A2C 加[[域随机化]]，约 1 小时训练即可真机重定向网球。
- 自标定使关节误差小，仿真策略可零样本部署；触觉目前仅按绝对阈值作二值接触判断。

## 🔗 关联
- [[Ruka-v2 Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning]]
- [[An open-source anthropomorphic robot hand system HRI hand]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]

## 🏷️ 标签
#灵巧手 #腱驱动 #开源硬件 #触觉传感
