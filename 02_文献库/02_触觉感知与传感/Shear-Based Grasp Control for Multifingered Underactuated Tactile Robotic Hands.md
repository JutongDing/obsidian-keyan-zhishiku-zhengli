---
title: Shear-Based Grasp Control for Multifingered Underactuated Tactile Robotic Hands
year: 2025
doi: 10.1109/TRO.2025.3563046
arxiv: 
key: KB-130
venue: IEEE Transactions on Robotics, vol. 41, 2025, pp. 3113–3128
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉传感器, 剪切力, 欠驱动手, 抓取力调节, SoftHand]
pdf: ../../../Shear-Based_Grasp_Control_for_Multifingered_Underactuated_Tactile_Robotic_Hands.pdf
confidence: high
source: pdf
aliases: []
---

# Shear-Based Grasp Control for Multifingered Underactuated Tactile Robotic Hands

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.1109/TRO.2025.3563046

## 👥 作者与所属院校
- 作者：Christopher J. Ford, Haoran Li, Manuel G. Catalano, Matteo Bianchi, Efi Psomopoulou 等
- 机构：布里斯托大学（University of Bristol）工程数学系与布里斯托机器人实验室、意大利技术研究院（IIT）、比萨大学

## 📖 研究背景
- [[欠驱动手]]的接触点与驱动器解耦，夹持力无法由电机电流准确反推，也缺乏本体感知。
- 柔性欠驱动手抓取易碎物时，必须知道接触点的法向力与切向剪切力，才能既不滑落也不压坏。
- 该文把微型化 TacTip（microTac）装到 Pisa/IIT SoftHand 五个指尖，用剪切反馈做反射式闭环。

## ❓ 需要解决的问题
- 指尖尺寸的[[视触觉传感器]]能否给出足够精度的接触位姿与三维力？
- 五个传感器的位姿/力模型能否用一次迁移学习统一，而非逐传感器单独训练？
- 仅凭剪切变化率，能否在扰动下维持稳定抓取并避免压碎？

## 📥📤 输入与输出
- 输入：五路 microTac[[触觉图像]]，异步并行推理出的接触位姿、法向力与剪切力。
- 输出：SoftHand 腱驱动机构的驱动指令，实现[[抓取力调节]]。

## ✅ 论文最终达到的效果
- 平均控制采样率 60 Hz；标准迁移学习使预测精度较单传感器模型提升 70% 以上，MAE 最低。
- 静态倒米实验（100/200/300 g）：阶跃扰动平均收敛 0.32 s，稳态误差 0.0023 N/s，五次试验均未滑落或压碎。
- 控制阈值：跟踪误差带 ±0.05 N/s、目标阈值 0.25 N/s、夹持力上限 9 N（纸杯压溃基线）。
- 倾斜倒出（质心动态变化）与触觉驱动主从任务均完成：人推被持物体，触觉力被转成 UR5 速度指令。
- 结论：快速反射式触觉控制可让欠驱动手在易碎物操作上接近人类灵巧度。

## 🔗 关联
- [[Learning Haptic-based Object Pose Estimation for In-hand Manipulation Control with Underactuated Robotic Hands]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]

## 🏷️ 标签
#视触觉传感器 #剪切力 #欠驱动手 #抓取力调节 #SoftHand
