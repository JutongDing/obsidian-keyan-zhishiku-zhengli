---
title: Learning to Detect Slip with Barometric Tactile Sensors and a Temporal Convolutional Neural Network
year: 2022
doi: 10.1109/ICRA46639.2022.9811592
arxiv: 2202.09549
key: KB-092
venue: 2022 IEEE International Conference on Robotics and Automation (ICRA), pp. 570–576
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, 气压触觉, TakkTile, 时间卷积网络, 抓取稳定]
pdf: ../../../Learning_to_Detect_Slip_with_Barometric_Tactile_Sensors_and_a_Temporal_Convolutional_Neural_Network.pdf
confidence: high
source: pdf
aliases: [arXiv:2202.09549（预印本已合并至本条）, 与 KB-090 为同一工作的 arXiv 版]
---

# Learning to Detect Slip with Barometric Tactile Sensors and a Temporal Convolutional Neural Network

## 📌 年份
2022（ICRA 2022，5 月 23–27 日，费城）

## 🔑 论文识别码
DOI: 10.1109/ICRA46639.2022.9811592（预印本 arXiv:2202.09549）

## 👥 作者与所属院校
- 作者：Abhinav Grover, Philippe Nadeau, Christopher Grebe, Jonathan Kelly
- 机构：多伦多大学航空航天研究所（UTIAS）

## 📖 研究背景
- 说明：同一工作存在 arXiv 预印本（arXiv:2202.09549v2）与 ICRA 2022 正式版两个 PDF，本笔记以正式版为准（预印本笔记已合并至此）。
- 抓取中物体相对指尖的滑移比任何外感都更早可测，但触觉传感器在工业场景仍难普及。
- 成本与耐用性是主因：光学[[视触觉传感器]]精度高却脆弱，[[GelSight]] 类方案尤甚。
- 该文以廉价耐用的气压计阵列 TakkTile 采集压力流，把[[滑移检测]]建模为时序二分类问题。

## ❓ 需要解决的问题
- 6 通道/指的低维气压信号能否支撑可靠的滑移判别？
- TCN 的膨胀卷积结构是否比频率域 CNN、经典阈值法更能抓住滑移前兆？
- 检测器对滑移速度、方向、表面曲率与滑移类型的敏感度分布如何？
- 在真实抓握任务中面对未训练物体能否直接泛化？

## 📥📤 输入与输出
- 输入：三指 TakkTile 的 MEMS 气压计读数，100 Hz，滑动窗口 Tk 帧的压力值栈。
- 输出：逐步的 slipping / stable 标签与对应时间戳，用于触发[[抓取力调节]]。

## ✅ 论文最终达到的效果
- 数据集 143,584 个样本点，含球/柱/平面三类曲率、多档速度与方向的滑移。
- TCN 四项指标均达 91.4% 左右（准确率 91.3%），优于对比的频率域 CNN 与阈值法。
- 敲击实验 6 类物体平均 87.5%，表面平滑者最好，可变形泡沫套最差（80%）。
- 提升实验平均 72.5%：塑料盒 100%、金属罐 95%，泡沫套与塑料球仅 35%。
- 对滑移速度与方向鲁棒，对滑移类型与曲率敏感；平台为 UR10 + Robotiq 三指夹爪。

## 🔗 关联
- [[Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy]]
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Force Estimation and Slip Detection for Grip Control using a Biomimetic Tactile Sensor]]

## 🏷️ 标签
#滑移检测 #气压触觉 #TakkTile #时间卷积网络 #抓取稳定
