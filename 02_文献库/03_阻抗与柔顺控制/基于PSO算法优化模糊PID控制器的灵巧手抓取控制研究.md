---
title: 基于PSO算法优化模糊PID控制器的灵巧手抓取控制研究
year: 2024
doi: 10.19950/j.cnki.CN61-1121/TH.2024.02.013
arxiv: 
key: KB-175
venue: "工业仪表与自动化装置, 2024(2): 75-79"
theme: 02_文献库/03_阻抗与柔顺控制
tags: [灵巧手, 模糊控制, PID, 粒子群算法, 抓取力控制]
pdf: ../../../基于PSO算法优化模糊PID控制器的灵巧手抓取控制研究_李锦洋.pdf
confidence: high
source: pdf
aliases: [Research on grasp control of smart hand optimization using fuzzy PID controller based on PSO algorithm]
---

# 基于PSO算法优化模糊PID控制器的灵巧手抓取控制研究

## 📌 年份
2024

## 🔑 论文识别码
DOI: 10.19950/j.cnki.CN61-1121/TH.2024.02.013

## 👥 作者与所属院校
- 作者：李锦洋, 关翔予, 孔晓光, 许舜
- 机构：沈阳化工大学、小米科技（南京）有限公司

## 📖 研究背景
- 五指[[灵巧手]]是仿生机器人主执行机构，但抓取过程中内部作用复杂、速度慢、效率低。
- 常规 PID 参数固定，难以兼顾关节角大偏差时的快速性与到位后的抖动抑制。
- 该文以角度闭环模糊自适应 PID 为基础，用粒子群算法整定控制器参数，并在 ADAMS-Simulink 联合仿真中验证。

## ❓ 需要解决的问题
- 关节角度偏差与 PID 三个参数之间的模糊规则如何制定，能否在线实时自整定？
- 粒子群算法给出的参数初值能否减少关节抖动并缩短调节时间？
- 指尖接触力能否被压到更小量级，既不压坏物体又不致滑落？
- 刚体接触仿真能否替代实物，反映抓取全过程的力位响应？

## 📥📤 输入与输出
- 输入：各关节期望角与实际角、角度偏差及其变化率；ADAMS 中手—物刚体接触模型参数；控制器参数初值。
- 输出：各关节驱动力矩、关节角跟踪曲线、指尖接触力曲线、整定后的 kp/ki/kd。

## ✅ 论文最终达到的效果
- 建立 ADAMS 与 Simulink 联合仿真模型，含手—目标物体刚体接触（刚度 1.0E+06 N/m、最大阻尼 1.0E+04 N·s/m）。
- 关节角跟踪：常规控制约 1 s 后稳定，PSO 优化模糊算法 0.9 s 达到稳定。
- 指尖接触力：PID 在 0.1 N 峰值后稳定于 0.04 N、物体 1.2 s 稳定；PSO 优化模糊算法在 0.01 N 峰值后稳定于 0.003 N、物体 1 s 稳定。
- 结论：接触力更小、调节更快、手部抖动更少，物体姿态更稳定，抓取效率提升。

## 🔗 关联
- [[多指灵巧手动力学建模与柔顺控制技术研究]]
- [[Force position control with bounded actions on a dexterous robotic hand with two-degree-of-freedom fingers]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]

## 🏷️ 标签
#模糊控制 #PID #粒子群算法 #抓取力控制 #联合仿真
