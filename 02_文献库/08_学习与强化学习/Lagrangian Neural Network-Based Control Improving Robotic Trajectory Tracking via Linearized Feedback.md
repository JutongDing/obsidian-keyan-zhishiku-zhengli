---
title: "Lagrangian Neural Network-Based Control: Improving Robotic Trajectory Tracking via Linearized Feedback"
year: 2026
doi: 10.1109/LRA.2026.3653326
arxiv: 
key: KB-002
venue: IEEE Robotics and Automation Letters (RA-L), Vol. 11, No. 3
theme: 02_文献库/08_学习与强化学习
tags: [拉格朗日神经网络, 计算力矩控制, 反馈线性化, 动力学建模, 数据效率]
pdf: ../../../2026_Lagrangian_Neural_Network-Based_Control_Improving_Robot.pdf
confidence: high
source: pdf
aliases: []
---

# Lagrangian Neural Network-Based Control: Improving Robotic Trajectory Tracking via Linearized Feedback

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1109/LRA.2026.3653326

## 👥 作者与所属院校
- 作者：Manuel Weiss, Alexander Pawluchin, Jan-Hendrik Ewering, Thomas Seel, Ivo Boblan
- 机构：柏林应用科学与技术大学（Compliant Robotics Lab）、莱布尼茨汉诺威大学机电系统研究所

## 📖 研究背景
- 计算力矩控制（CTC）靠模型抵消惯性、科氏/离心与重力项，模型失配会直接劣化跟踪与调节。
- [[强化学习]]常需千万级交互，实机数据采集代价高；PINN/LNN 以力学先验提升数据效率。
- 以往 LNN 控制器置于反馈线性化框架之外（如前馈），未参与塑造闭环误差动态。

## ❓ 需要解决的问题
- 能否把 LNN 逆动力学模型嵌入 CTC 内环，使闭环误差动态仍为解耦线性形式？
- 在仅 10–100 s 训练数据下，模型能否外推到分布外（OOD）关节状态？
- 相比模型 CTC、PINN-CTC、DNN-CTC、LNN 前馈与 PID，跟踪精度与数据效率是否占优？

## 📥📤 输入与输出
- 输入：4 自由度机械臂的关节角 q、速度 q̇、加速度 q̈ 与参考轨迹；数据按 500 Hz 采样，来自 MuJoCo 仿真与实机 PD 跟踪。
- 输出：关节力矩 τ（LNN 逆动力学 + 反馈线性化），等价于对下层的位置/力矩指令。

## ✅ 论文最终达到的效果
- 在 Agility Robotics Digit 的 4 自由度臂上验证，跟踪精度较基于模型的基线最高提升 30%。
- 相同训练数据下关节空间 RMSE 最低；100 s 实机或 1000 s 仿真数据即可满足重力补偿。
- Apple M1 Pro CPU 上单次推理约 0.2 ms（375,324 FLOPs，500 Hz 下 187.7 MFLOP/s）。
- 参数扰动（连杆 ±10%、质量 ±15%、惯量 ±25%、质心 ±15 mm、摩擦 ±50%）下 95 分位 RMSE 仍 < 3.253°。
- 加装 3.5 kg 负载（约等于臂质量 3.6 kg）后微调即可恢复标称跟踪；仿真中扩展到 UR5 与 KUKA iiwa 14。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#拉格朗日神经网络 #计算力矩控制 #反馈线性化 #动力学建模 #数据效率
