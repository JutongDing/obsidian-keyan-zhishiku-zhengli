---
title: Design, Fabrication, and Characterization of a Novel Optical Six-Axis Distributed Force and Displacement Tactile Sensor for Dexterous Robotic Manipulation
year: 2023
doi: 10.3390/s23249640
arxiv: 
key: KB-037
venue: Sensors (MDPI), 23(24), 9640
theme: 02_文献库/02_触觉感知与传感
tags: [六轴触觉传感器, 分布式触觉阵列, 光学传感, 指尖力/位移估计]
pdf: ../../../Design, Fabrication, and Characterization of a Novel Optical Six-Axis Distributed Force and Displacement Tactile Sensor for Dexterous Robotic Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# Design, Fabrication, and Characterization of a Novel Optical Six-Axis Distributed Force and Displacement Tactile Sensor for Dexterous Robotic Manipulation

## 📌 年份
2023

## 🔑 论文识别码
DOI: 10.3390/s23249640

## 👥 作者与所属院校
- 作者：Olivia Leslie, David Córdova Bulens, Stephen J. Redmond
- 机构：爱尔兰都柏林大学（UCD）电子与电气工程学院

## 📖 研究背景
- 稳定抓取与 [[手内操作]] 依赖接触界面处的实时多轴分布式触觉信息，单点力传感难以刻画接触状态。
- 现有六轴力/力矩传感器多为刚性整体结构、厚度大，难以直接贴装到 [[灵巧手]] 指尖；[[GelSight]]、[[DIGIT]] 等视触觉方案擅长二维形变成像，但缺少分布式多轴力与位移的联合估计。
- 该文沿用 LiVec 光强/光角度传感原理，把十个可变形传感单元排成指尖阵列，以低成本工艺换取分布式六轴感知。

## ❓ 需要解决的问题
- 如何在接近人类拇指尺寸、厚度极小的指尖内集成十个传感单元并保持可装配性？
- 如何从各单元的光强与入射角变化中解算局部 XYZ 三轴力与三轴位移？
- 如何由分布式单元阵列反算全局 XYZ 力与三轴力矩，且精度足以支撑抓取闭环？
- 传感器能否不改动商用夹爪结构即完成实时力/力矩测量演示？

## 📥📤 输入与输出
- 输入：各传感单元中 LED 与光电探测器测得的光强及入射角信号（对应弹性单元的三维变形）。
- 输出：十个位置的局部 XYZ 力与位移估计，以及全局 XYZ 力与力矩 Tx、Ty、Tz。

## ✅ 论文最终达到的效果
- 局部力精度 X 20.89 mN、Y 19.19 mN、Z 43.22 mN，量程约 XY ±1.5 N、Z 0 至 −2 N。
- 局部位移精度 X 56.70 µm、Y 50.18 µm、Z 13.83 µm，量程 XY ±2 mm、Z 0 至 −1.5 mm（压缩）。
- 全局力矩精度 Tx 1.90 N·mm、Ty 1.54 N·mm、Tz 1.26 N·mm，并用独立测量验证全局力/力矩估计。
- 尺寸与人拇指相当、厚度小，可直接加装于现有机器人手指；在 OnRobot RG2 夹爪上演示了抓取过程中实时变化的全局力与力矩。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#六轴触觉传感器 #光学触觉 #分布式阵列 #指尖传感
