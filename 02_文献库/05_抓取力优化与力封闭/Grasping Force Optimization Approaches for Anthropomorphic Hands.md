---
title: Grasping Force Optimization Approaches for Anthropomorphic Hands
year: 2018
doi: 10.1115/1.4038684
arxiv: 
key: KB-065
venue: Journal of Mechanisms and Robotics
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 拟人手, 摩擦锥, 线性矩阵不等式, 软手指接触]
pdf: ../../../Grasping Force Optimization Approaches for Anthropomorphic Hands.pdf
confidence: high
source: pdf
aliases: []
---

# Grasping Force Optimization Approaches for Anthropomorphic Hands

## 📌 年份
2018（JMR 第 10 卷第 1 期，011004）

## 🔑 论文识别码
DOI: 10.1115/1.4038684

## 👥 作者与所属院校
- 作者：Aimee Cloutier、James Yang
- 机构：德州理工大学机械工程系 Human-Centric Design Research Lab

## 📖 研究背景
- 拟人手的抓取力难定：力小则滑落，力大则压坏脆弱物体，需要自动求解。
- 既有[[抓取力优化]]研究的手型、物体与接触模型各不相同，结果难以横向比较。
- 该文在同一套手模型上系统比较线性规划、非线性规划与 LMI 三种解法。

## ❓ 需要解决的问题
- 三种方法在最优接触力精度与计算耗时上如何取舍？
- 软手指（SF）与硬手指（HF）接触模型对最优力差别有多大？
- 外力取 18 个方向、摩擦锥用 4/10/20 段线性化时结论是否稳定？
- 接触点位置出现变异时，最优解是否仍然可用？

## 📥📤 输入与输出
- 输入：手的关节角与连杆参数、预设接触点位置与法向、物体质量与摩擦系数（0.6–2）、18 个方向的外力。
- 输出：各指节接触力的法向、切向与扭转分量最优值，以及单次求解耗时。

## ✅ 论文最终达到的效果
- 非线性与 LMI 精度最好且结果几乎一致；线性法结果随摩擦锥段数由 4 增至 20 逼近它们。
- 指尖抓取仅两接触点时，非线性与 LMI 力值完全相同（如法向 0.841 N），线性法偏差最大。
- 耗时：指尖抓取的 4 段线性法 0.0091 s、非线性 0.026 s；整手圆柱抓取 LMI 10.7 s、线性 20 段 3.52 s，均偏慢。
- SF 接触比 HF 更费时（圆柱抓取 4.63 s 对 10.7 s）；HF 下线性与非线性力幅差 4–5 N，三角抓取相对差均在 15% 以内。

## 🔗 关联
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#抓取力优化 #拟人手 #摩擦锥 #线性矩阵不等式
