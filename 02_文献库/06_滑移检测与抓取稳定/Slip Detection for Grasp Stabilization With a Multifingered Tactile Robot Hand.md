---
title: Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand
year: 2021
doi: 10.1109/TRO.2020.3031245
arxiv: 1810.02653
key: KB-132
venue: IEEE Transactions on Robotics
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, 触觉传感, SVM, 多指手, 抓取稳定]
pdf: ../../../Slip Detection and Stable Grasping With Multi-Fingered Robotic Hand Using Deep Learning Approach.pdf
confidence: high
source: pdf
aliases: [Slip Detection and Stable Grasping With Multi-Fingered Robotic Hand Using Deep Learning Approach]
---

# Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand

## 📌 年份
2021（TRO 第 37 卷第 2 期）

## 🔑 论文识别码
DOI: 10.1109/TRO.2020.3031245

## 👥 作者与所属院校
- 作者：Jasper Wollaston James, Nathan F. Lepora
- 机构：University of Bristol、Bristol Robotics Laboratory（UWE Bristol）

## 📖 研究背景
- 人类抓取靠触觉[[滑移检测]]避免掉落，机器人多指手需要把单点结论扩展到多传感器。
- 既有方法分模型驱动（梁束模型、[[摩擦锥]]）与无模型（随机森林、深度学习），孰优未定。
- 该文用低成本三指 T-MO 手（TacTip 光学[[视触觉传感器]] + Model O 手）做可解释检测。

## ❓ 需要解决的问题
- TacTip 的 30 个标记针速度特征能否从单指可靠扩展到三指整手？
- 与固定阈值、逻辑回归相比，线性/非线性 SVM 是否在少样本与下采样下更稳？
- 检测到[[初始滑移]]后，用几帧、几指触发响应才能在误报与掉落间折中？
- 无视觉、无质量先验时，能否靠触觉一次成功抓取？

## 📥📤 输入与输出
- 输入：三指 TacTip 的 30 个 pin 像素坐标，按 60 Hz 差分得到 pin 速度（60 维时序）。
- 输出：滑移/静止二分类标签与 F1；触发后各指闭合增量，即[[抓取力调节]]量。

## ✅ 论文最终达到的效果
- SVM 峰值 F1 0.972、全测试平均 0.960，优于逻辑回归 0.957，且数据下采样 70% 仍稳定。
- 重抓 11 种物体（含 6 种新物体）：2Fr2Sen 策略成功率 74%，1Fr2Sen 为 73%。
- 罐内加米致失稳的场景重复 5 次，物体均未掉落；50–500 g 七档质量首次抓取全部成功。
- 过抓量：100–300 g 平均偏紧 39%，更重时达 105%；可变形玩具猫为 34% 与 74%。
- 停止滑落位移 21 mm、29 mm（相机 60 fps，逊于 TacTip 的 16 mm）。

## 🔗 关联
- [[Modulation of grip force with load force during point-to-point arm movements]]
- [[ROBOT HAND SYSTEM INCLUDING FINGERTIP SENSOR AND METHOD FOR CONTROLLING ROBOT HAND SYSTEM]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#滑移检测 #触觉传感 #SVM #多指手
