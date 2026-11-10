---
title: Robust Adaptive Safe Robotic Grasping with Tactile Sensing
year: 2025
doi: 
arxiv: 2411.07833
key: KB-123
venue: arXiv 预印本（cs.RO，v2 2025-11；© 2025 IEEE，会议/期刊待补）
theme: 02_文献库/02_触觉感知与传感
tags: [安全抓取, 控制屏障函数, 触觉传感, 力封闭, 摩擦锥]
pdf: ../../../Robust Adaptive Safe Robotic Grasping with Tactile Sensing.pdf
confidence: high
source: pdf
aliases: []
---

# Robust Adaptive Safe Robotic Grasping with Tactile Sensing

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2411.07833

## 👥 作者与所属院校
- 作者：Yitaek Kim, Jeeseop Kim, Albert H. Li, Aaron D. Ames, Christoffer Sloth
- 机构：南丹麦大学 Maersk Mc-Kinney Moller 研究所、加州理工学院（机械与土木工程系、计算与数学科学系）

## 📖 研究背景
- 力控抓取多只追求"抓得稳"，忽略"抓得安全"：既不希望物体滑落，也不希望施力过大压碎物体。
- 接触动力学、摩擦系数与接触坐标系普遍存在建模误差，普通控制屏障函数（CBF）约束容易被违反。
- 该文以 CBF 把接触力约束与[[力封闭]]约束统一写进安全滤波器，并用力指触觉反馈闭环执行。

## ❓ 需要解决的问题
- 仅凭指尖触觉，能否同时估计接触点、法向力与力矩，替代昂贵的六维力传感？
- 在摩擦系数与接触坐标系存在误差时，哪类安全滤波器仍能把接触力约束在[[摩擦锥]]内、且不过力？
- 提升鲁棒性是否会以过度保守（夹持力偏大）为代价，能否量化？

## 📥📤 输入与输出
- 输入：各指尖触觉的[[接触力估计]]（接触点、法向力、力矩）、期望抓取力、物体质量与摩擦系数估计。
- 输出：前指期望法向力指令；125 Hz 高层安全滤波器输出，1 kHz 底层力跟踪控制器执行。

## ✅ 论文最终达到的效果
- 用 Shadow 手两指抓取 10 g 木块、30 g 塑料圆柱、120 g 轴承座与 15 g 易碎玻璃器皿，均未出现安全违反。
- 标准 CBF 在四类物体上均违反约束（超力后滑落，h1、h3 变负）；RCBF、RaCBF、DOBCBF 保持安全。
- 含扰动观测器的 DOBCBF 保守性最低；相对只用 RCBF 的基线，平均保守性下降 83.5%。
- 触觉接触点估计可支撑按捏合轨迹的力调节，MATLAB 仿真与实机结论一致。
- 局限：摩擦系数仍需迭代调参，接触坐标系被近似为手指坐标系，带来残余不确定性。

## 🔗 关联
- [[LeTac-MPC Learning Model Predictive Control for Tactile-reactive Grasping]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]

## 🏷️ 标签
#安全抓取 #控制屏障函数 #触觉传感 #力封闭 #摩擦锥
