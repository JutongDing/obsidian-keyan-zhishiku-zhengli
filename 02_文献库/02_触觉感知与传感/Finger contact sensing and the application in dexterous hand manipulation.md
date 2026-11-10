---
title: Finger contact sensing and the application in dexterous hand manipulation
year: 2015
doi: 10.1007/s10514-015-9425-4
arxiv: 
key: KB-049
venue: Autonomous Robots, 39(1), 25-41
theme: 02_文献库/02_触觉感知与传感
tags: [触觉传感, 接触力估计, 指尖, 力/力矩传感器, 曲面跟踪]
pdf: ../../../Finger contact sensing and the application in dexterous hand manipulation(1).pdf
confidence: high
source: pdf
aliases: []
---

# Finger contact sensing and the application in dexterous hand manipulation

## 📌 年份
2015（Auton Robot 第 39 卷，25–41）

## 🔑 论文识别码
DOI: 10.1007/s10514-015-9425-4

## 👥 作者与所属院校
- 作者：Hongbin Liu, Kien Cuong Nguyen, Véronique Perdereau, Joao Bimbo, Junghwan Back 等
- 机构：King's College London、UPMC Sorbonne Universités（待核对）

## 📖 研究背景
- 精细[[手内操作]]需要实时知道接触点位置、法向与切向力、局部力矩，而非仅一个合力。
- 单点力/力矩传感器加可变形橡胶蒙皮成本低，但由 6 维力反解接触状态是病态问题。
- 既有方法多局限于小接触半径、低摩擦或静态条件，难以覆盖指尖整个表面。
- 接触信息最终要服务于[[触觉伺服]]与探索，例如沿未知曲面跟踪时的法向力保持。

## ❓ 需要解决的问题
- 如何结合橡胶蒙皮弹性模型，由 6 轴力/力矩反解接触位置与接触力分量？
- 在摩擦系数 μ≤1、接触半径从小到大的范围内，精度与实时性如何保证？
- 辨识出的接触信息能否直接支撑曲面跟踪与灵巧手操作？

## 📥📤 输入与输出
- 输入：指尖 6 轴力/力矩信号（分辨率 1/160 N、1/32 Nmm）、2 mm 厚橡胶蒙皮的几何与弹性参数。
- 输出：接触点位置（指尖表面坐标）、法向力与摩擦力的大小和方向、接触处局部力矩。

## ✅ 论文最终达到的效果
- 传感算法运行频率 158–242 Hz，满足实时操作需求。
- 接触位置最大误差小于 0.55 mm；μ≤1 条件下辨识稳健、精度较高。
- 指尖采用 a=9.5 mm、b=17 mm、c=10.5 mm 的曲面外形，覆盖整个指尖表面而非单点。
- 以曲面跟踪/探索实验验证接触信息的可用性，说明可服务于精细操作。

## 🔗 关联
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#触觉传感 #接触力估计 #指尖 #力/力矩传感器
