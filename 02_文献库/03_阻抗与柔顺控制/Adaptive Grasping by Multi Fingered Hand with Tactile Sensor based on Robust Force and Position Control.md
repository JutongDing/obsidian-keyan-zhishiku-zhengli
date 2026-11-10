---
title: Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control
year: 2008
doi: 
arxiv: 
key: KB-185
venue: 2008 IEEE International Conference on Robotics and Automation (ICRA)（投稿评审版，据 PDF 元数据）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [鲁棒力位控制, 扰动观测器, 滑移检测, 触觉传感, 多指手]
pdf: ../../../日本三指夹爪_基于鲁棒力位控制的触觉传感器多指灵巧手自适应抓取.pdf
confidence: high
source: pdf
aliases: [Adaptive Grasping by Multi Fingered Hand with Tactile Sensor]
---

# Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control

## 📌 年份
2008

## 🔑 论文识别码
KB-185（本地编号，PDF 无 DOI，首页为评审版）

## 👥 作者与所属院校
- 作者：Taro Takahashi, Toshimitsu Tsuboi, Takeo Kishida, Yasunori Kawanami, Satoru Shimizu 等
- 机构：Sony Corporation, Intelligent System Research Laboratory（Information Technologies Laboratories）

## 📖 研究背景
- 服务机器人需抓取质量、刚度与摩擦均未知的物体，视觉几何误差与物性缺失使力控参数难以事先设定。
- 传统[[力位混合控制]]依赖任务空间分解，碰撞瞬间易产生冲击，模式切换不平滑。
- 指尖触觉可感知[[初始滑移]]，为在线决定抓取力提供直接依据。

## ❓ 需要解决的问题
- 位置控制与力控制能否随外力大小平滑、快速切换？
- 齿轮摩擦与重力等扰动下，力控精度如何保证？
- 物性与表面位置未知时，如何确定刚好防滑的抓取力？

## 📥📤 输入与输出
- 输入：关节角与角速度、外力/接触力、指尖触觉图像（3×3 mm 传感面，38.8 Hz）。
- 输出：关节力矩/电流指令、位置或力模式指令、各指期望抓取力（实验中约 1.0 N）。

## ✅ 论文最终达到的效果
- 以扰动观测器估计重力与齿轮摩擦，构成鲁棒加速度控制器，并在其上搭建力控制器。
- 实现位置、力、力约束位置三种模式，按外力大小平滑切换；控制周期 0.25 ms。
- 12 自由度三指手（每指 4 关节）对豆腐、玻璃等未知物性物体实现平稳碰撞与稳定抓取。
- 以触觉图像中接触点（COP）位移经 3×3 高斯加权构成滑移量，在线完成[[抓取力调节]]，兼顾起始与静止阶段。
- 同一组参数可抓取不同尺寸物体，无需已知表面位置、质量与刚度。

## 🔗 关联
- [[Force position control with bounded actions on a dexterous robotic hand with two-degree-of-freedom fingers]]
- [[多指灵巧手动力学建模与柔顺控制技术研究]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]

## 🏷️ 标签
#鲁棒力位控制 #扰动观测器 #滑移检测 #触觉传感 #多指手
