---
title: Robust Model-Based In-Hand Manipulation with Integrated Real-Time Motion-Contact Planning and Tracking
year: 2023
doi: 
arxiv: 2309.01813
key: KB-125
venue: arXiv 预印本（cs.RO；会议/期刊待补）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [手内操作, 接触隐式MPC, 触觉反馈, 力位混合控制, 分层控制]
pdf: ../../../Robust Model-Based In-Hand Manipulation with Integrated Real-Time.pdf
confidence: high
source: pdf
aliases: []
---

# Robust Model-Based In-Hand Manipulation with Integrated Real-Time Motion-Contact Planning and Tracking

## 📌 年份
2023

## 🔑 论文识别码
arXiv:2309.01813

## 👥 作者与所属院校
- 作者：Yongpeng Jiang
- 机构：清华大学信息科学技术国家研究中心（Research Center for Information Science and Technology, Tsinghua University）

## 📖 研究背景
- 学习型[[手内操作]]性能亮眼，但数据需求大、训练周期长，泛化到新任务代价高。
- 模型法无需训练，却受限于在线规划效率与建模误差处理，实机应用受限。
- 该文用"接触隐式 MPC 规划 + 触觉反馈跟踪"的分层结构，兼顾实时规划与误差补偿。

## ❓ 需要解决的问题
- 能否在 10 Hz 内实时生成含接触建立/断开的手指运动与接触力联合参考，而不预设接触序列？
- 触觉反馈能否补偿高层规划中"力在距离外"（force-at-a-distance）一类建模误差？
- 换任务（开门、转卡、滑板、开盒）时是否无需重新建模或示教？

## 📥📤 输入与输出
- 输入：期望物体运动、手抓取位姿、手与物体模型、指尖 Tac3D 视触觉的接触法向与力（30 Hz）、本体感知。
- 输出：各指关节位置指令与期望接触力；高层接触隐式 MPC 10 Hz，底层[[力位混合控制]]（MPC-based HFMC）30 Hz。

## ✅ 论文最终达到的效果
- MuJoCo 球体旋转任务成功率 100/100，平均任务误差 0.024 rad；开环仅 14/100，MJPC-CEM 83/100。
- 高层 9.88 Hz、底层 30.0 Hz 稳定运行；6 项挑战任务全部完成（抓取、开门、转卡、滑板、开盒等）。
- 开门任务中可承受人手扰动，门柄仍转到目标 180°；相对无接触跟踪基线收敛更快、姿态误差更小。
- 力跟踪在计划力高频变化时有可见延迟，源于触觉采样率与舵机特性未精确建模。
- 平台：LEAP 手装于 UR5 法兰，四个指尖换装 Tac3D 触觉传感器。

## 🔗 关联
- [[Non-Parametric Self-Identification and Model Predictive Control of Dexterous In-Hand Manipulation]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]
- [[Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control]]

## 🏷️ 标签
#手内操作 #接触隐式MPC #触觉反馈 #力位混合控制 #分层控制
