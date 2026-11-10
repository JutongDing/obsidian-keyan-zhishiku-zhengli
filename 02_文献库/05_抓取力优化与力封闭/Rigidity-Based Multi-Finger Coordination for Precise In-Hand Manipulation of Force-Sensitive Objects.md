---
title: Rigidity-Based Multi-Finger Coordination for Precise In-Hand Manipulation of Force-Sensitive Objects
year: 2026
doi: 10.1109/LRA.2026.3666396
arxiv: 
key: KB-122
venue: IEEE Robotics and Automation Letters, vol. 11, no. 4, pp. 4401–4408
theme: 02_文献库/05_抓取力优化与力封闭
tags: [图刚性, 力封闭, 力位映射, 易损物体]
pdf: ../../../Rigidity-Based Multi-Finger Coordination for Precise In-Hand Manipulation of Force-Sensitive Objects.pdf
confidence: high
source: pdf
aliases: []
---

# Rigidity-Based Multi-Finger Coordination for Precise In-Hand Manipulation of Force-Sensitive Objects

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1109/LRA.2026.3666396

## 👥 作者与所属院校
- 作者：Xinan Rong、Changhuang Wan、Aochen He、Xiaolong Li、Gangshan Jing
- 机构：重庆大学自动化学院、香港城市大学机械工程系

## 📖 研究背景
- 多指[[手内操作]]精度受限于多指协调的复杂度与感知能力不足，易损物体的力规划尤其难做。
- 与带夹爪末端的多机械臂不同，多指手只有指尖点接触、不能施加拉力，协调力规划的自由度更紧。
- 多数商用[[灵巧手]]缺少标定过的力矩传感器，触觉传感器又贵、难集成、噪声大、有延时。
- 本文切入角度：不靠触觉与力矩控制，在图刚性（graph rigidity）与[[力封闭]]约束下规划接触力，再经力位映射转成关节轨迹。

## ❓ 需要解决的问题
- 能否把多指接触点之间的距离不变性写成刚性矩阵约束，让指尖在运动中保持相对构型不散架？
- 在内力被「反向使用」（需保留而非抑制）的点接触场景下，接触力如何分解为操作力与刚性内力？
- 规划出的力轨迹如何映射为关节位置指令，使无力矩控制的商用灵巧手也能执行？
- 在质量、摩擦已知但存在参数不确定性时，该框架能否安全操作生鸡蛋、软毛线一类物体？

## 📥📤 输入与输出
- 输入：物体期望 6-DoF 轨迹、指尖接触位置与法向、摩擦系数与法向力上下界、物体质量与柔顺增益、视觉（AprilTag）位姿反馈。
- 输出：各指接触力（操作力 + 刚性内力 + 法向预压）及对应关节角轨迹，逐周期滚动执行。

## ✅ 论文最终达到的效果
- 提出双层框架：上层刚性力规划器（约束含摩擦锥、法向上限与刚性条件），下层力位转换器把力映射为虚拟目标点并解[[逆运动学]]。
- 用指尖间距总相对偏差 TRD 作指标，四指围成方框沿方形轨迹运动时偏差极小，毛线保持绷紧不被拉长。
- 空塑料杯（3 g）与注水杯（53 g）均稳定跟踪，未出现变形或滑移；基线因抓取不稳使杯体变形。
- 生鸡蛋在空中书写字母「RAL」，最大路径点误差仅 0.3 mm，相邻路径点执行时间 2.79–6.89 s。
- 重力方向改变（竖直姿态）下操作杯与鸡蛋，平均误差 0.4 mm，单路径点耗时 3.12–5.67 s；对质量与摩擦不确定性亦做了鲁棒性测试。

## 🔗 关联
- [[Real-Time Force Regulation for Whole-Hand Dexterous Grasping]]
- [[Real-Time Grasping-Force Optimization for Multifingered Manipulation Theory and Experiments]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#力封闭 #图刚性 #手内操作 #力位映射 #易损物体抓取
