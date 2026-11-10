---
title: Force Feedback Control For Dexterous Robotic Hands Using Conditional Postural Synergies
year: 2023
doi: 
arxiv: 2303.06170
key: KB-052
venue: arXiv preprint (cs.RO)
theme: 02_文献库/01_灵巧手抓取规划
tags: [力反馈控制, 姿态协同, cVAE, 抓取力调节, 灵巧手]
pdf: ../../../Force_Feedback_Control_For_Dexterous_Robotic_Hands_Using_Conditional_Postural_Synergies.pdf
confidence: high
source: pdf
aliases: []
---

# Force Feedback Control For Dexterous Robotic Hands Using Conditional Postural Synergies

## 📌 年份
2023（arXiv 2303.06170v1，2023-03-10）

## 🔑 论文识别码
arXiv:2303.06170

## 👥 作者与所属院校
- 作者：Dimitrios Dimou, José Santos-Victor, Plinio Moreno
- 机构：葡萄牙里斯本大学高等技术学院系统与机器人研究所（ISR/IST）

## 📖 研究背景
- 非结构化环境中的灵巧操作依赖指尖触觉反馈，开环位置控制提重物会因滑移失败。
- 既有触觉力控制器多为每指独立闭环，难以推广到不同拟人[[抓取位姿]]与抓取类型。
- 姿态协同可把高维手部关节压缩到低维空间，但缺少与力反馈的闭环结合。

## ❓ 需要解决的问题
- 能否只用一个低维变量（抓取尺寸，即拇指—食指指尖距离）同时驱动整只手的关节？
- 条件变分自编码器（cVAE）能否按抓取类型生成姿态，实现「换标签即换抓法」？
- 力反馈能否应对物体重量变化，并支持放置与人对交接？

## 📥📤 输入与输出
- 输入：各指尖 FTS-3 三维力（50 Hz）、抓取类型标签、手部世界位姿。
- 输出：期望法向力与尺寸误差 → 抓取尺寸增量 → cVAE 姿态采样器输出的全手关节角。

## ✅ 论文最终达到的效果
- 硬件为 Seed Robotics RH8D 五指[[灵巧手]]，每指尖配 FTS-3 三维力传感器。
- 法向力按 μf_n ≥ f_t 与切向力成比例设定，形成防滑的[[安全裕度]]。
- 支持 3 种精确抓取，5 组递进实验：提放瓶子、旋转 90° 后放置、旋转后交人、泡沫砖 180° 交接、杯中投币增重。
- 能在重量在线变化时调整抓取构型，完成放置与人手交接；局限为无视觉、传感器噪声与遮挡。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[GraspNet-1Billion A Large-Scale Benchmark for General Object Grasping]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#力反馈控制 #姿态协同 #cVAE #抓取力调节
