---
title: "LeTac-MPC: Learning Model Predictive Control for Tactile-reactive Grasping"
year: 2024
doi: 
arxiv: 2403.04934
key: KB-081
venue: arXiv preprint（cs.RO, v2）
theme: 02_文献库/02_触觉感知与传感
tags: [触觉传感, GelSight, 模型预测控制, 抓取力调节, 可变形物体]
pdf: ../../../LeTac-MPC.pdf
confidence: high
source: pdf
aliases: []
---

# LeTac-MPC: Learning Model Predictive Control for Tactile-reactive Grasping

## 📌 年份
2024

## 🔑 论文识别码
arXiv:2403.04934

## 👥 作者与所属院校
- 作者：Zhengtong Xu、Yu She
- 机构：普渡大学（Purdue University）机械工程系，美国

## 📖 研究背景
- 抓取是被动响应任务：人靠指尖触觉估计物体状态并实时调节手指，机器人却常开环夹紧。
- 物体刚度、质量分布、形状差异大，固定夹持力要么夹不稳，要么压坏草莓、鸡蛋等软物。
- 纯模型法（PD、MPC）依赖高质量触觉反馈，泛化性受限；[[GelSight]]可提供高分辨[[触觉图像]]。

## ❓ 需要解决的问题
- 能否从触觉图像端到端学出收敛、稳定的夹持控制器，而不是靠人工设计反馈律？
- 如何自动化采集覆盖不同物理属性物体的触觉-夹持数据，摆脱人工示教？
- 在动态抖动与突发碰撞下，学习型控制器能否优于 PD、模型 MPC 与开环？

## 📥📤 输入与输出
- 输入：GelSight 触觉图像序列、夹爪宽度与速度、历史动作；经 CNN 提特征后送入可微分 MPC 层。
- 输出：夹爪加速度/宽度指令，闭环频率 25 Hz（底层 WSG 50-110 位置跟踪最高 30 Hz）。

## ✅ 论文最终达到的效果
- 提出 LeTac-MPC：神经网络嵌入 + 可微分模型预测控制层，实现 25 Hz 收敛的[[抓取力调节]]。
- 设计全自动数据采集流水线（主从双臂、4.5 mm/s 相对运动、0.9 mm 宽度步进），并公开数据集与代码。
- 可稳定抓取番茄、鸡蛋等易滑物；夹爪宽度在 ±0.05 mm 内即可收敛。
- 障碍碰撞任务 10/10 成功，开环仅 3/10；动态抖动 8/10，PD/MPC 为 10/10，但其初始夹持力过大、易损伤软物。
- 局限：极软物体（剥壳水煮蛋、肉类）触觉特征不足，宽度持续减小直至压坏。

## 🔗 关联
- [[FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#触觉传感 #视触觉 #模型预测控制 #抓取力调节
