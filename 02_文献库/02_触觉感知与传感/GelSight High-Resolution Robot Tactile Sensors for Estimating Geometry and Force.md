---
title: "GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force"
year: 2017
doi: 10.3390/s17122762
arxiv: 1708.00922
key: KB-121
venue: Sensors, vol. 17, no. 12, art. 2762
theme: 02_文献库/02_触觉感知与传感
tags: [GelSight, 视触觉, 几何测量, 力估计]
pdf: ../../../Resolution_Robot_Tactile_Sensors_for_Estimating_Geometry_and_Force.pdf
confidence: high
source: pdf
aliases: [GelSight review]
---

# GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

## 📌 年份
2017

## 🔑 论文识别码
DOI: 10.3390/s17122762（arXiv: 1708.00922）

## 👥 作者与所属院校
- 作者：Wenzhen Yuan、Siyuan Dong、Edward H. Adelson
- 机构：麻省理工学院计算机科学与人工智能实验室（CSAIL）

## 📖 研究背景
- 机器人触觉长期以测接触与接触力分布为主，商用阵列空间分辨率约 5 mm，仅够做接触检测与夹持力控制。
- 人类虽不能精确测力，却能从触觉读出形状、纹理、材料、质量、柔顺性、粗糙度与热导率，当前机器人远未用足这些信息。
- 本文认为「柔软接触面 + 高分辨率几何测量」应是合格触觉传感器的核心，而非只堆压力点位。
- 本文切入角度：综述[[GelSight]]这一基于视觉的光学[[视触觉传感器]]，从原理、光路、算法到不同版本硬件。

## ❓ 需要解决的问题
- 如何用摄像头透过弹性体拍摄接触面形变，把亚毫米级三维几何还原出来？
- 从形变场能否同时反解法向力、切向力与力矩，并给出可靠的测力量程与精度？
- 光照、标记点图案、弹性体厚度与硬度如何设计，才能兼顾分辨率、体积与帧率？
- 这类传感器怎样做[[触觉传感器标定]]，并装到机器人指尖上长期可用？

## 📥📤 输入与输出
- 输入：斜射多色 LED 照明下的弹性体表面接触图像序列，含表面涂层与标记点图案。
- 输出：接触面高分辨率三维几何（[[触觉图像]]）、法向/切向力与力矩估计、滑移与初始滑移状态。

## ✅ 论文最终达到的效果
- 原理：弹性体受压形变改变反照率与法向，由彩色图像梯度积分出表面法向，再重建深度。
- 分辨率：面向分辨率优化的版本可达 1–2 µm；装于指尖的紧凑版通常为 30–100 µm，远超人类皮肤。
- 指尖版用 30 Hz、640×480 的 USB 相机，视场 18 mm × 14 mm，空间分辨率约 20–30 µm，标记点平均间隔 1.1 mm。
- 力测量：标定装置最小可分辨法向力为 0.05 N；用神经网络从图像回归法向力、切向力与方向，R² 高于 0.9。
- 除几何与力之外还能指示滑移与初始滑移，并已用于材料识别、手内定位等任务。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#GelSight #视触觉传感器 #触觉图像 #力估计 #传感器设计
