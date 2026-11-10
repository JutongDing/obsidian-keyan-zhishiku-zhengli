---
title: Maintaining stable grasps during highly dynamic robot trajectories
year: 2020
doi: 10.1109/IROS45743.2020.9341575
arxiv: 
key: KB-096
venue: 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9199–9204
theme: 02_文献库/01_灵巧手抓取规划
tags: [动态抓取, 摩擦锥, 抓取稳定性预测, 轨迹优化, 惯性力]
pdf: ../../../Maintaining stable grasps during highly dynamic robot trajectories.pdf
confidence: high
source: pdf
aliases: []
---

# Maintaining stable grasps during highly dynamic robot trajectories

## 📌 年份
2020（IROS 2020，10 月 25–29 日，拉斯维加斯/线上）

## 🔑 论文识别码
DOI: 10.1109/IROS45743.2020.9341575

## 👥 作者与所属院校
- 作者：Giandomenico Martucci, Joao Bimbo, Domenico Prattichizzo, Monica Malvezzi
- 机构：意大利技术研究院（IIT）ADVR、锡耶纳大学、比萨大学

## 📖 研究背景
- 高速搬运能提产能，但大加速度带来的惯性力会让被夹物体滑出[[摩擦锥]]。
- 传统[[抓取规划]]与稳定性判据多基于准静态平衡，动态轨迹下不再成立。
- 该文沿轨迹逐点算物体所受空间力旋量，判断其是否越出"抓取空间力空间"多面体，再只改姿态把力拉回来。

## ❓ 需要解决的问题
- 如何从关节轨迹（位置/速度/加速度）经逆动力学得到物体上的惯性力与力矩？
- 抓取可行域（GSFS 多面体）与瞬时力旋量如何比较，距离如何度量？
- 在保持总时长的前提下，仅调整物体朝向能否消除滑移？
- 抓取式与非抓取式两类任务上策略是否一致？

## 📥📤 输入与输出
- 输入：机械臂关节轨迹 θ、θ̇、θ̈（MoveIt 规划）、物体质量与惯量、接触摩擦系数估计。
- 输出：每个 via-point 的位姿（姿态四元数）修正量与"该轨迹是否可完成"的判定。

## ✅ 论文最终达到的效果
- 平台为 Franka Emika Panda 七自由度机械臂 + 夹爪，物体为 5×5×5 cm、37 g 的 3D 打印立方体。
- 非抓取式运输：t=1.05 s 时切向力 fx=−0.105 N 超过摩擦可承受上限 |fx|≤0.096 N，物体滑落。
- 按 μ=0.35 重算后判定滑移点；优化轨迹仅需绕轴倾斜约 8° 即可把力旋量拉回 GSFS 内。
- 两任务（抓取式摆动、非抓取式快移）均在总时长不变的前提下完成，验证"改姿态不改时间"的策略。
- 局限：GSFS 视为轨迹中不变，未计入接触点与法向力变化引起的多面体形变。

## 🔗 关联
- [[Dynamic In-hand Sliding Manipulation]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#动态抓取 #摩擦锥 #抓取稳定性预测 #轨迹优化
