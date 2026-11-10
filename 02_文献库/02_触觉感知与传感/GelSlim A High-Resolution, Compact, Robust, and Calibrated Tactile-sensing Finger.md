---
title: "GelSlim: A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger"
year: 2018
doi: 
arxiv: 
key: KB-055
venue: 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉传感器, 传感手指设计, 触觉传感器标定, 耐久性]
pdf: ../../../GelSlim_A_High-Resolution_Compact_Robust_and_Calibrated_Tactile-sensing_Finger.pdf
confidence: high
source: pdf
aliases: []
---

# GelSlim: A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger

## 📌 年份
2018

## 🔑 论文识别码
KB-055（本地编号；IROS 2018 论文，原文未给 DOI）

## 👥 作者与所属院校
- 作者：Elliott Donlon, Siyuan Dong, Melody Liu, Jianhua Li, Edward Adelson 等（6 人）
- 机构：麻省理工学院（MIT）

## 📖 研究背景
- 触觉硬件最该装在操作链末端，但那里空间最紧、承受的力与磨损最大。
- 已有 [[GelSight]] 类 [[视触觉传感器]] 分辨率高，却体积臃肿、玻璃与软胶脆弱、连续使用后输出漂移。
- 该文切入角度：重排光路（导光板全内反射 + 镜面折叠）把传感器做成细长、带尖端的传感手指，并配套 [[触觉传感器标定]] 流程。

## ❓ 需要解决的问题
- 如何在保持高分辨 [[触觉图像]] 的同时，把手指做薄并把传感垫做大？
- 手指厚度、相机景深与敏感区尺寸三者的几何权衡能否用设计变量参数化？
- 数千次抓取后，亮度、信号强度与照明均匀性是否仍可用，能否被标定补偿？

## 📥📤 输入与输出
- 输入：Raspberry Pi 相机经导光板与反射镜拍摄的凝胶接触图像帧。
- 输出：经透视矫正与亮度/对比度归一化后的触觉图像，用于恢复接触纹理与接触面几何。

## ✅ 论文最终达到的效果
- 传感垫 50 mm × 50 mm，指尖细而带尖，可挤进杂乱场景取物。
- 凝胶改用 XP-565 硅胶 15:1 配比并覆编织织物表皮，显著提升抗磨性。
- 两步标定：出厂用四矩形靶标求一次透视变换；此后每 100 次抓取做在线照明与对比度校正。
- 3000 次以上抓取后死像素少于 0.06%（约 170 个）；信号强度约在 1750 次抓取后明显下降，标定后可部分恢复。
- 传感手指装于 WSG-50 夹爪、ABB 机械臂完成杂乱抓取实验。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]

## 🏷️ 标签
#视触觉传感器 #传感手指 #标定 #耐久性
