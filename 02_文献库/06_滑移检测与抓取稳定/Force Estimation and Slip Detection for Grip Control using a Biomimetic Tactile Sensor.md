---
title: Force Estimation and Slip Detection for Grip Control using a Biomimetic Tactile Sensor
year: 2015
doi: 10.1109/HUMANOIDS.2015.7363558
arxiv: 
key: KB-051
venue: IEEE-RAS 15th International Conference on Humanoid Robots (Humanoids 2015)
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, 抓取力控制, 仿生触觉, 力估计, BioTac]
pdf: ../../../Force Estimation and Slip Detection for Grip Control.pdf
confidence: high
source: pdf
aliases: [Force estimation and slip detection/classification for grip control using a biomimetic tactile sensor]
---

# Force Estimation and Slip Detection for Grip Control using a Biomimetic Tactile Sensor

## 📌 年份
2015（Humanoids 2015，韩国首尔）

## 🔑 论文识别码
DOI: 10.1109/HUMANOIDS.2015.7363558

## 👥 作者与所属院校
- 作者：Zhe Su, Karol Hausman, Yevgen Chebotar, Artem Molchanov, Gerald E. Loeb 等
- 机构：University of Southern California、Max Planck Institute for Intelligent Systems（待核对）

## 📖 研究背景
- 服务机器人要在家庭环境抓取未知物体，视觉给出位姿后仍难以保证可靠抓取。
- 触觉能监测手—物交互，尤其对易碎物体，而这些交互难以从外部观察或建模。
- 仿生触觉传感器 BioTac 提供类人丰富信号，但需把原始电极信号映射为力与操作事件。

## ❓ 需要解决的问题
- 如何由 BioTac 电极阵列信号估计三个方向的指尖力与切向力？
- 能否在宏观滑移发生前检出[[初始滑移]]，并区分线性滑移与旋转滑移？
- 力估计与滑移判别的结果能否闭环驱动[[抓取力调节]]，既不捏碎也不掉落？

## 📥📤 输入与输出
- 输入：BioTac 19 路电极阻抗时序（取 100 帧窗口，1900 维输入）、力导数值；物体 IMU 仅用于评测真值。
- 输出：三向[[接触力估计]]、滑移类别（无滑移/线性/旋转）、抓取力指令。

## ✅ 论文最终达到的效果
- 指尖力估计对比了解析模型、LWPR 与 1–3 层神经网络三类回归器，覆盖三维受力方向。
- 滑移分类成功率超过 80%（每物体 80 次以上抓取，训练/测试 8:2 划分）。
- 判别可在 IMU 察觉物体运动之前给出正确类别，为机器人争取响应时间。
- Barrett 手爪配合力控制器完成 100–1500 g 塑料罐与 10–500 g 塑料杯的抓放，中途加配重也能稳住。

## 🔗 关联
- [[Modulation of grip force with load force during point-to-point arm movements]]
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#滑移检测 #抓取力控制 #仿生触觉 #力估计
