---
title: Force/position control with bounded actions on a dexterous robotic hand with two-degree-of-freedom fingers
year: 2022
doi: 10.1016/j.bbe.2021.12.006
arxiv: 
key: KB-053
venue: "Biocybernetics and Biomedical Engineering, 42(1): 233-246"
theme: 02_文献库/03_阻抗与柔顺控制
tags: [力位混合控制, 饱和函数, 假肢手, 有界输入]
pdf: ../../../Forceposition control with bounded actions.pdf
confidence: high
source: pdf
aliases: [Force/position control with bounded actions]
---

# Force/position control with bounded actions on a dexterous robotic hand with two-degree-of-freedom fingers

## 📌 年份
2022

## 🔑 论文识别码
DOI: 10.1016/j.bbe.2021.12.006

## 👥 作者与所属院校
- 作者：Lina N. Rojas-García、César A. Chávez-Olivares、Isela Bonilla-Gutiérrez、Marco O. Mendoza-Gutiérrez、Fernando Ramírez-Cardona
- 机构：墨西哥圣路易斯波托西自治大学理学院、阿瓜斯卡连特斯自治大学机器人工程系、Viretrade S.A. de C.V.

## 📖 研究背景
- 假肢手设计研究多关注执行器数量、重量与尺寸，低成本方案被视为普及关键。
- 现有力控制器常忽略执行器力矩饱和上限，并假设被抓物体刚性不变形，接触时易失稳。
- [[阻抗控制]]等间接力调节方案需在位置与力之间折中，但缺少输入有界的保证。
- 本文切入：用广义饱和函数（GSF）把[[力位混合控制]]的指令约束在执行器力矩范围内，并加入重力补偿。

## ❓ 需要解决的问题
- 10 自由度手（每指 2 个主动关节）在单关节力矩上限 0.325 N·m 下能否并行跟踪位置与法向力？
- 经 GSF 限幅后的闭环能否给出避免执行器饱和的可检验充分条件？
- 抓取刚度 1000 N/m 的柔性球体时，位置误差与力误差如何折中？
- 用 SolidWorks 建模加 Simscape Multibody 仿真标定手部[[动力学建模]]，能否替代实物整手实验？

## 📥📤 输入与输出
- 输入：各指关节角与角速度、期望指尖位置、期望法向接触力（仿真取 1 N）、重力补偿项。
- 输出：各关节力矩指令；力、位置、阻尼通道分别经 LGSF/GSF 限幅，边界为 M_F、M_P、M_D。

## ✅ 论文最终达到的效果
- 完成一只 10 自由度[[灵巧手]]设计：拇指 2 自由度、四指各 2 自由度，ABS 3D 打印，最大电机力矩 0.325 N·m。
- Simulink 中实时运行，采样周期 2.5 ms（1900 MHz 工控机）。
- 仿真：五指抓取 1000 N/m 泡沫球，各指施加 1 N 法向力并保持期望位姿，验证力位并行调节。
- 实物：仅用 3D 打印食指复现同一柔顺抓取任务，验证控制器可落地（未做整手实验）。
- 给出以 T_i ≥ B_g/B_J 形式表达的避免饱和充分条件，并说明该条件非必要。

## 🔗 关联
- [[多指灵巧手动力学建模与柔顺控制技术研究]]
- [[Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]

## 🏷️ 标签
#力位混合控制 #饱和函数 #假肢手 #有界输入 #重力补偿
