---
title: An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors
year: 2025
doi: 
arxiv: 2412.02335
key: KB-023
venue: IEEE Transactions on Automation Science and Engineering（早期访问，卷期待补）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [抓取力跟踪, 广义刚度估计, LSTM, PI控制]
pdf: ../../../An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors.pdf
confidence: high
source: pdf
aliases: []
---

# An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2412.02335（DOI 尚缺）

## 👥 作者与所属院校
- 作者：Ziyang Cheng、Xiangyu Tian、Ruomin Sui、Tiemin Li、Yao Jiang
- 机构：清华大学（未央书院、机械工程系）

## 📖 研究背景
- 现有研究多集中于[[滑移检测]]与抓取力规划，却忽略了「实际力如何跟踪目标力」这一执行环节。
- 力跟踪控制器的最优增益强烈依赖物体刚度，而多数自适应算法以刚度估计为前提。
- 真实物体常表现黏滞、塑性、变刚度等非线性时变行为，传统刚度定义与估计方法失效。
- 本文切入角度：把刚度推广为「广义刚度」，用 LSTM 在线估计并据此整定 PI 参数。

## ❓ 需要解决的问题
- 对黏弹、塑性、变刚度等非理想物体，如何给出可在线使用的刚度定义？
- 慢速加载时零力漂移与恒力漂移会让最小二乘斜率失真，如何抑制？
- 如何在保证渐近精度的同时显著缩短初始探测（probing）时间？
- 估计器能否泛化到训练分布之外的新物体？

## 📥📤 输入与输出
- 输入：指端位移 x(t) 与实测抓取力 F(t) 的时间序列（刚度估计频率 100 Hz）。
- 输出：广义刚度估计值 k̂，以及据此在线整定的 PI 增益与期望抓取力指令，实现[[抓取力跟踪]]。

## ✅ 论文最终达到的效果
- 全部测试物体平均渐近误差 0.16 N，约为 MiFREN 基线 0.49 N 的三分之一。
- 平均探测时间仅 3.34 s，不到 MiFREN 的 38.65 s 的十一分之一。
- 纸杯加配重：渐近误差 0.21 N 对 0.49 N，探测时间 3.60 s 对 38.65 s。
- 黏土塑性阶段（0–8 s）滑动 RMSE 小于 0.5 N，MiFREN 接近 4 N。
- 网络为 5 层 LSTM、隐层 512；覆盖弹性、黏弹、塑性、变刚度共十余种日常物体。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]
- [[Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand]]

## 🏷️ 标签
#抓取力跟踪 #广义刚度 #LSTM #力控制
