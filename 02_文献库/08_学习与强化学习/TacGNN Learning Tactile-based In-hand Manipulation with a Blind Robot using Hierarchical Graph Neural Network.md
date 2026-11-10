---
title: "TacGNN: Learning Tactile-based In-hand Manipulation with a Blind Robot using Hierarchical Graph Neural Network"
year: 2023
doi: 
arxiv: 2304.00736
key: KB-143
venue: IEEE Robotics and Automation Letters (RA-L)
theme: 02_文献库/08_学习与强化学习
tags: [手内操作, 图神经网络, 强化学习, 仿真到现实迁移]
pdf: ../../../TacGNN.pdf
confidence: high
source: pdf
aliases: []
---

# TacGNN: Learning Tactile-based In-hand Manipulation with a Blind Robot using Hierarchical Graph Neural Network

## 📌 年份
2023

## 🔑 论文识别码
arXiv:2304.00736（RA-L 2023 预印本，DOI 见期刊页）

## 👥 作者与所属院校
- 作者：Linhan Yang, Bidan Huang, Qingbiao Li, Ya-Yen Tsai, Wang Wei Lee 等
- 机构：香港大学、腾讯 Robotics X、剑桥大学、帝国理工学院、南方科技大学

## 📖 研究背景
- 盲操作（仅触觉加本体感觉）是灵巧手走向实用化的关键，但触觉阵列信号高维、随接触稀疏激活，难以建立解析模型。
- CNN 需把触觉读数重排成固定矩阵，破坏 taxel 间空间关系；GCN 使用固定图，无法适应接触区域变化。
- 该文构建随接触状态动态重建的触觉图 TacGNN 提取物体状态，再用 PPO 学习 [[手内操作]] 策略。

## ❓ 需要解决的问题
- 如何构造动态增删节点与连边的触觉图，并兼容不同传感器布置？
- 触觉图是否比 MLP、CNN、GCN 更准地预测手中双球的位置与姿态？
- 仅用触觉与本体感觉的 PPO 策略能否完成 180° 保龄球（Baoding ball）相对转动任务？
- 仿真策略经 [[域随机化]] 能否零样本迁移真机，并泛化到未见的难度等级？

## 📥📤 输入与输出
- 输入：Allegro 手 653 维 taxel 法向力读数（指尖 12×6、指节 6×6、掌心 113 个单元）、16 个关节角。
- 输出：物体状态（双球位置与姿态）预测，以及 16 维关节目标动作。

## ✅ 论文最终达到的效果
- 双球位置预测 RMSE 0.096 cm，优于 MLP 0.250、GCN 0.152；CNN 测试误差达 27.76 cm。
- 成功率：易 94.71%、中 88.57%、难 79.78%；中等难度较次优 GCN 的 64.51% 提升明显。
- 策略仅在仿真训练，真机不再微调即可完成 180° 相对转动，验证 [[仿真到现实迁移]]。
- 消融显示 32 通道足够，16 通道时 RMSE 升至 0.251 cm。

## 🔗 关联
- [[Multi-Fingered In-Hand Manipulation with Various Object Properties Using Graph Convolutional Networks and Distributed Tactile Sensors]]
- [[Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#手内操作 #图神经网络 #强化学习 #仿真到现实迁移
