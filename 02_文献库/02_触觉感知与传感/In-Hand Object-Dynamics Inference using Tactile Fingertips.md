---
title: In-Hand Object-Dynamics Inference using Tactile Fingertips
year: 2021
doi: 
arxiv: 2003.13165
key: KB-076
venue: arXiv 预印本（v2，2021-01-19；正式发表信息待补）
theme: 02_文献库/02_触觉感知与传感
tags: [触觉力估计, 摩擦估计, 惯性参数辨识, 因子图, 手内操作]
pdf: ../../../In-Hand Object-Dynamics Inference using Tactile Fingertips.pdf
confidence: high
source: pdf
aliases: []
---

# In-Hand Object-Dynamics Inference using Tactile Fingertips

## 📌 年份
2021（arXiv v2；初版 2020-03）

## 🔑 论文识别码
arXiv: 2003.13165（原文未见 DOI 与期刊卷期，待核对）

## 👥 作者与所属院校
- 作者：Balakumar Sundaralingam, Tucker Hermans
- 机构：犹他大学机器人中心与计算学院、NVIDIA

## 📖 研究背景
- 物体摩擦与惯性参数此前多在实验室用外部精密传感（腕部六维力/力矩）离线辨识。
- 腕部力传感器用于[[灵巧手]]估计物体惯性有三难：需现场标定、手自重与噪声耦合、关节状态缺失。
- 指端触觉力只测局部接触、量级小且随接触变化，能否支撑"野外"估计存疑。
- 该文只用多指 BioTac 的[[指尖力传感器]]读数，配合因子图做摩擦与惯性联合推断。

## ❓ 需要解决的问题
- 仅凭指端触觉力能否估计抓取中的摩擦系数？
- 如何主动激励物体，使质量、质心与惯性张量可观？
- 接触建立/断开与传感噪声下，如何保证参数物理一致（惯性矩阵正定）？
- 手内估计能否与腕部力传感器基线相当？

## 📥📤 输入与输出
- 输入：多指 BioTac 法向/切向力及不确定性、关节角、物体位姿（视觉或放宽刚体约束跟踪）。
- 输出：摩擦系数 μ、质量、质心与惯性张量共 10 个惯性参数。

## ✅ 论文最终达到的效果
- 平台：Allegro 手 + BioTac 指尖 + KUKA 臂，因子图（GTSAM）实现，不依赖力矩传感。
- 摩擦系数与真值的中位误差 0.0056；BioTac[[接触力估计]]幅度中位精度 0.03 N。
- 加物理一致性约束后，惯性参数在 7 类物体上接近真值；常速假设基线出现负质量等失败。
- 手内估计在 box_2 上优于腕部力传感器（Wrist-FT），归因于接触点分布与质心位置。
- 通过主动接触至[[滑移检测]]触发来估摩擦；断触时力读数归零，结构化因子图可自然处理多次断触。

## 🔗 关联
- [[Finger contact sensing and the application in dexterous hand manipulation]]
- [[Development of Intelligent Robot Hand using Proximity, Contact and Slip sensing]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#触觉力估计 #摩擦估计 #惯性参数辨识 #因子图 #手内操作
