---
title: "GelSphere: An Omnidirectional Rolling Vision-Based Tactile Sensor for Online 3D Reconstruction and Normal Force Estimation"
year: 2026
doi: 
arxiv: 2603.14104
key: KB-056
venue: arXiv 预印本（cs.RO）
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉, 球面滚动, 三维重建, 法向力估计, 无线传感]
pdf: ../../../GelSphere_An Omnidirectional Rolling Vision-Based Tactile Sensor for Online 3D Reconstruction and Normal Force Estimation.pdf
confidence: high
source: pdf
aliases: [GelSphere]
---

# GelSphere: An Omnidirectional Rolling Vision-Based Tactile Sensor for Online 3D Reconstruction and Normal Force Estimation

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2603.14104（预印本，无 DOI）

## 👥 作者与所属院校
- 作者：Seoyeon Lee、Mohammad Amin Mirzaee、Wenzhen Yuan（前两位共同一作）
- 机构：伊利诺伊大学香槟分校（UIUC）

## 📖 研究背景
- 工业检修与制造、皮肤科定量评估都需要对大面积或曲面做连续形貌扫描，结构光与激光轮廓仪受视场、体积与环境光限制。
- [[GelSight]] 类[[视触觉传感器]]只能局部感知，且滑移会磨损凝胶；圆柱滚动式设计仅能沿单一方向滚动，多带线缆。
- 现有方案靠反复抬离-再接触扩展覆盖，难以连续成像。
- 本文切入：把感测凝胶做成球面，用钢珠轴承层实现任意方向滚动，并把相机、LED 与电池全部封进球内。

## ❓ 需要解决的问题
- 球面滚动时如何保持内部相机视野稳定，并让触觉凝胶在任意方向自由滚动？
- 滚动拼接（触觉 SLAM）后的几何精度如何：平面距离漂移与法向角漂移分别是多少？
- 能否直接从原始[[触觉图像]]估计法向接触力，跨不同曲率表面精度如何？
- 亮面与哑光两种凝胶涂层对重建与测力精度的影响差异有多大？

## 📥📤 输入与输出
- 输入：单帧 240×240 RGB 触觉图像、滚动轨迹与帧间位姿、法向压痕。
- 输出：局部表面法向图与三维网格、在线拼接的大面积重建表面、法向力估计值（1–15 N）。

## ✅ 论文最终达到的效果
- 感测凝胶直径 65.3 mm，内置 4.5 mm 钢珠轴承层；整机约 100×100×90 mm，XIAO ESP32-S3 摄像头经 Wi-Fi 推流。
- 单帧六边形压头法向估计平均点积 0.965（亮面）/0.939（哑光），SSIM 0.950/0.930。
- 连续扫描 75×32.5 mm² 区域：距离漂移 MAE 1.07 mm / 1.25 mm，角度漂移 MAE 1.3° / 2.7°。
- 1–15 N、8 种曲率（1–64 cm）压头约 750 组数据训练 4 层 CNN，法向力 MAE 0.44 N（亮面）/0.93 N（哑光）。
- 局限：快速扫描会降低重建质量，钢珠可能卡入壳体与凝胶之间；提高分辨率会增加推流延迟。

## 🔗 关联
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#视触觉 #球面滚动 #三维重建 #法向力估计 #无线传感
