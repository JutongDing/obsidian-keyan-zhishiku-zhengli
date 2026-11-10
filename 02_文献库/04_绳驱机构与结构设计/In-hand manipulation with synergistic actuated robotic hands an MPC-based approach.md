---
title: "In-hand manipulation with synergistic actuated robotic hands: an MPC-based approach"
year: 2023
doi: 10.1109/HUMANOIDS57100.2023.10374563
arxiv: 
key: KB-077
venue: 2023 IEEE-RAS 22nd International Conference on Humanoid Robots（Humanoids）
theme: 02_文献库/04_绳驱机构与结构设计
tags: [协同, 欠驱动, 模型预测控制, 手内操作, 仿真分析]
pdf: ../../../In-hand manipulation with synergistic actuated robotic hands.pdf
confidence: high
source: pdf
aliases: [In-hand manipulation with synergistic actuated robotic hands]
---

# In-hand manipulation with synergistic actuated robotic hands: an MPC-based approach

## 📌 年份
2023（Humanoids 2023）

## 🔑 论文识别码
DOI: 10.1109/HUMANOIDS57100.2023.10374563

## 👥 作者与所属院校
- 作者：Martin Rohrmüller, Philipp Beckerle, Knut Graichen, Monica Malvezzi, Maria Pozzi
- 机构：埃尔朗根-纽伦堡大学、锡耶纳大学、意大利技术研究院（IIT）

## 📖 研究背景
- [[手内操作]]需精确协调多自由度，全驱动手方案较多，欠驱动与协同驱动研究偏少。
- 协同（synergy）把关节运动耦合、降维，用少量输入完成类人抓取与调姿。
- 既有工作多把协同当运动学后处理，未纳入带接触力约束的预测控制回路。
- 该文把协同以两种方式嵌入 MPC，并比较计算量与跟踪精度。

## ❓ 需要解决的问题
- 协同写成关节等式约束，还是重分配输入写入系统函数，哪个更省算力？
- 驱动维度 nu 如何影响指尖跟踪误差与单步迭代时间？
- 协同耦合如何限制手的工作空间与可完成的手内操作？
- 仿真结论能否用于按任务需求选择[[欠驱动手]]的自由度？

## 📥📤 输入与输出
- 输入：指尖/接触点期望轨迹、物体位姿与外力旋量、协同矩阵 S、关节状态与接触力约束。
- 输出：协同输入速度 z（或期望关节速度）、关节力矩与接触力。

## ✅ 论文最终达到的效果
- MATLAB MPC Toolbox + SynGrasp，20 关节拟人手与夹爪，Δt=0.01 s，预测域 3Δt，kp=100、kd=20、qp=5000。
- nu=1 时指间距离恒存固定偏差；nu=15 可达 0.01 m 目标，误差随 nu 增大收敛。
- 协同写入系统函数较写入关节约束，平均迭代时间降 17.9%（夹爪）/9.0%（手）。
- 协同约束加在期望关节量上仅降 3.1%/2.6%；两种写法的轨迹精度无明显差异。
- 仅仿真，未上实物；作者拟在真实全驱动（[[腱驱动]]/软件协同）与欠驱动手上验证。

## 🔗 关联
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A metric to design spring stiffness of underactuated fingers for stable grasp]]

## 🏷️ 标签
#协同 #欠驱动 #模型预测控制 #手内操作 #仿真分析
