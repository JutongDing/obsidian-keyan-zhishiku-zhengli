---
title: Learning Haptic-based Object Pose Estimation for In-hand Manipulation Control with Underactuated Robotic Hands
year: 2022
doi: 
arxiv: 2207.02843
key: KB-085
venue: arXiv preprint（cs.RO, v2）；正文自称 letter，疑为 IEEE RA-L 版本（卷期待核对）
theme: 02_文献库/02_触觉感知与传感
tags: [触觉传感, 位姿估计, 欠驱动手, 手内操作, 模型预测控制]
pdf: ../../../Learning Haptic-based Object Pose Estimation.pdf
confidence: high
source: pdf
aliases: 
---

# Learning Haptic-based Object Pose Estimation for In-hand Manipulation Control with Underactuated Robotic Hands

## 📌 年份
2022

## 🔑 论文识别码
arXiv:2207.02843

## 👥 作者与所属院校
- 作者：Osher Azulay、Inbar Ben-David、Avishai Sintov
- 机构：特拉维夫大学（Tel-Aviv University）机械工程系，以色列

## 📖 研究背景
- [[欠驱动手]]柔性自适应，但关节刚度、摩擦、制造误差难建模，解析模型往往不可得。
- 抓取物体位姿多靠视觉，在柜内、遮挡、狭窄空间里视线被挡，视觉直接失效。
- 低成本硬件与数据驱动模型为替代视觉提供机会，但需要筛选出真正有信息量的触觉/本体特征。

## ❓ 需要解决的问题
- 不用视觉，仅凭本体感知（关节角、执行器负载）与低成本触觉，能否估计抓取物体位姿？
- 哪些特征组合贡献最大，GP、全连接网络、LSTM 三类回归器谁更准？
- 基于该位姿估计的 MPC 能否把物体操作到目标位姿，包括柜内[[轴孔装配]]场景？

## 📥📤 输入与输出
- 输入：关节角、执行器负载、3D 打印指尖内 FSR（低成本[[指尖力传感器]]）电压（含接触位置信息）、抓取初始位姿（部分实验提供）。
- 输出：物体在平面位姿 SE(2) 的位置与朝向；MPC 输出下一时刻手的动作序列。

## ✅ 论文最终达到的效果
- 设计 FlX 指尖：整体一次 3D 打印，靠柔性关节与软垫凸起压迫 FSR，成本低且随接触位置改变输出。
- 建立触觉特征状态表示，比较 GP、FC-NN 与 LSTM；全特征下 LSTM 位置 RMSE 3.1 mm、朝向 3.0°，GP 为 4.1 mm/4.9°。
- 数据采集约 10 Hz，训练约 12 小时；验证圆柱（15 mm）、椭圆、方形、月牙等截面物体。
- 提出 MPC-Critic，用学习到的观测模型与 critic 估计预测误差；仅靠触觉即可把物体移到目标位姿。
- 在封闭柜内完成插孔演示，成功率略低于视觉版 MPC-Vis 与视觉伺服，但验证了无视线操作可行。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[Finger contact sensing and the application in dexterous hand manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#触觉传感 #位姿估计 #欠驱动手 #手内操作
