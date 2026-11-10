---
title: CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors
year: 2019
doi: 10.1109/JSEN.2019.2912968
arxiv: 
key: KB-025
venue: IEEE Sensors Journal
theme: 02_文献库/02_触觉感知与传感
tags: [触觉图像, 卷积神经网络, 迁移学习, 物体识别]
pdf: ../../../CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors.pdf
confidence: high
source: pdf
aliases: []
---

# CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors

## 📌 年份
2019

## 🔑 论文识别码
DOI: 10.1109/JSEN.2019.2912968（本文为预印本，正式版见 IEEE Sensors Journal）

## 👥 作者与所属院校
- 作者：Juan M. Gandarias、Alfonso J. García-Cerezo、Jesús M. Gómez-de-Gabriel
- 机构：马拉加大学（Universidad de Málaga）

## 📖 研究背景
- 高分辨率压阻阵列使压力读数可以直接当作[[触觉图像]]处理，从而借用计算机视觉方法。
- 传统触觉识别多依赖手工特征与浅层分类器（如 SURF-SVM），在类别数增加时性能下滑。
- 深度卷积网络在视觉上成熟，但触觉数据规模小，是否适合从头训练仍存疑。
- 本文切入角度：在同一传感器、同一数据集上系统比较「迁移学习」与「自建轻量 CNN」两类路线。

## ❓ 需要解决的问题
- 用真实 RGB 预训练网络做迁移，与从零训练触觉专用 CNN，哪个更适合触觉物体识别？
- 分类头应重训全连接层，还是换成 SVM，二者精度与耗时差多少？
- 触觉专用网络能否在极小参数量下达到可部署精度与速度？
- 与当时触觉识别最优方法相比，精度提升能否量化？

## 📥📤 输入与输出
- 输入：安装在 AUBO OUR-i5 机械臂末端的触觉传感器采集的单帧压力图（含插入薄膜改善景深），共 22 类物体与人体部位。
- 输出：22 类别的类别标签及置信分布，同时报告 GPU/CPU 上的单帧分类耗时。

## ✅ 论文最终达到的效果
- 共测试 11 种配置：8 种迁移学习（ResNet/VGG16/SqueezeNet × 重训/ SVM/全连接微调）＋3 种自建 TactNet 变体。
- 最佳迁移模型 ResNet-NN 平均识别率 95.36%（25.6M 参数，GPU 3.31 s，CPU 27.0 s）。
- 轻量 TactNet-4 仅 25k 参数即达 93.59%，单帧分类 GPU 0.051 s / CPU 0.094 s。
- TactResNet（790k 参数）93.61%；VGG16-SVM 93.50%；所有方法平均识别率均超过 93%。
- 相对 SURF-SVM 基线最好提升 17.72%（ResNet-NN），最差 CNN 也提升 8.08%。

## 🔗 关联
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#触觉图像 #CNN #迁移学习 #物体识别
