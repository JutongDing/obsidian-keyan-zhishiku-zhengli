---
title: A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning
year: 2022
doi: 10.1109/LRA.2022.3151260
arxiv: 
key: KB-011
venue: IEEE Robotics and Automation Letters, 7(3)
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [触觉感知, 抓取稳定性预测, 滑移检测, 集成学习, 深度学习]
pdf: ../../../A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning.pdf
confidence: high
source: pdf
aliases: []
---

# A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning

## 📌 年份
2022（RA-L 第 7 卷第 3 期，2022-02-14 在线）

## 🔑 论文识别码
DOI: 10.1109/LRA.2022.3151260

## 👥 作者与所属院校
- 作者：Gang Yan, Alexander Schmitz, Satoshi Funabashi, Sophon Somlor, Tito Pradhono Tomo 等
- 机构：早稻田大学（Waseda University）

## 📖 研究背景
- 基于触觉传感器的抓取感知已广泛用于机器人操作，提升前预测[[抓取稳定性预测]]、提升后判定[[滑移检测]]是两个被反复研究的任务。
- 以往工作各自为其中一个任务设计新网络，未利用"抓取—提升"两个动作阶段互相连通、前一阶段信息可迁移到后一阶段的事实。
- 单一网络假设空间有限，而触觉数据量小、模型多借自图像领域，易过拟合。
- 缺乏把两个阶段统一建模、并用集成手段稳定提升精度的框架。

## ❓ 需要解决的问题
- 能否用一个多阶段、多输出框架同时输出提升前的稳定性与提升后的滑移概率？
- 集成不同网络架构能否比任何单一架构更可靠，注意力加权集成是否优于线性加权与投票？
- 在未见物体上的实时推理是否仍保持精度，且延迟可接受？

## 📥📤 输入与输出
- 输入：三轴触觉传感器阵列的时序测量，窗口取 [T−0.5 s, T+0.5 s]（含 50 个时间步），覆盖抓取相与提升相。
- 输出：抓取相稳定性判据与提升相滑移发生判据的双路二分类概率。

## ✅ 论文最终达到的效果
- 在 6 种主流网络（CNN、LSTM、CNN-LSTM、TCN 等）、两个数据集共 3000 次以上抓取、80 余个物体上验证。
- 多阶段模型全面优于单阶段：抓取+提升相精度最高比单相提升 3.83 个百分点（TCN，Normal 数据集）。
- 集成优于单模型：自注意力集成在 Fβ 分数上最多领先基学习器 9.66；第二数据集达 90.88%（1050 次抓取）。
- 真实机器人未见物体实验：最佳配置 87.14%，比仅用抓取相提升 5.72%。
- 单模型推理约 0.03 s，集成后约 0.20 s，作者认为可接受；精度仍低于 90%，归因于传感器维修后量程变化与数据量不足。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]
- [[Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand]]

## 🏷️ 标签
#触觉感知 #抓取稳定性预测 #滑移检测 #集成学习 #深度学习
