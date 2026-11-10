---
title: A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure
year: 2024
doi: 10.1109/IAECST64597.2024.11117905
arxiv: 
key: KB-012
venue: 2024 6th International Academic Exchange Conference on Science and Technology Innovation (IAECST)
theme: 02_文献库/01_灵巧手抓取规划
tags: [欠驱动手, 抓取策略, 几何建模, 运动学, 力位控制]
pdf: ../../../A Simplified Grasping Strategy for Under-Driven Dexterous Hand Based on Geometric Structure.pdf
confidence: high
source: pdf
aliases: []
---

# A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure

## 📌 年份
2024

## 🔑 论文识别码
DOI: 10.1109/IAECST64597.2024.11117905

## 👥 作者与所属院校
- 作者：Yuanchen Tang, Liang He
- 机构：西北工业大学软件学院

## 📖 研究背景
- [[欠驱动手]]执行器少，控制简化、重量轻、能效与成本占优，是[[灵巧手]]的重要分支。
- 传统抓取策略要先建立手指驱动动力学（电机输入电流与指尖输出力的关系），再求物体力平衡方程与稳定指标，建模代价高。
- 物体几何属性可直接给出稳定接触点，从而绕开精确动力学；视觉也易于提取这类几何特征。
- 现有工作缺少按几何类别（圆柱、长方体、球）分别给出可执行抓取流程的系统化做法。

## ❓ 需要解决的问题
- 只建运动学、不建驱动动力学，能否仍生成稳定抓取策略？
- 对圆柱、长方体、球三类几何体，如何由几何约束解出接触点与各关节目标角？
- 拇指以多大的接触力、在什么时刻停止加力，才算完成闭合？

## 📥📤 输入与输出
- 输入：目标物体几何参数（半径 R、边长 m/n 等）、抓取类别、手部改进 D-H 参数。
- 输出：四指位置控制的关节目标角、拇指欠驱动连杆位移 d(t) 的五次多项式轨迹，以及基于堵转电流与指腹力阈值的闭合判据。

## ✅ 论文最终达到的效果
- 给出拇指与四指两组改进 D-H 参数表，建立拇指→其余四指的坐标系映射。
- 分别推导圆柱、长方体、球的接触点与关节角解析条件；以长方体为例给出 m<4.1 cm、n<3.1 cm 的可抓域。
- 控制分工：拇指 π1 全驱动先转至 90°，π2、π3 为欠驱动关节由连杆 d 连续伸长实现力闭合；四指做位置控制。
- 停止条件两条：堵转电流超过额定值 3 倍；拇指触觉传感器力达阈值。
- 用五次多项式插值保证首末速度与加速度为零，轨迹平滑；相较既有方法省去复杂[[动力学建模]]，但文中未给出实机抓取成功率等定量实验。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#欠驱动手 #抓取策略 #几何建模 #运动学 #力位控制
