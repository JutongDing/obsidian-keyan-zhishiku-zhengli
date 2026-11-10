---
title: "SCT-CNN: A Spatio-Channel-Temporal Attention CNN for Grasp Stability Prediction"
year: 2021
doi: 10.1109/ICRA48506.2021.9561397
arxiv: 
key: KB-127
venue: 2021 IEEE International Conference on Robotics and Automation (ICRA)
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取稳定性预测, 触觉传感, 注意力机制, CNN, uSkin]
pdf: ../../../SCT-CNN_A_Spatio-Channel-Temporal_Attention_CNN_for_Grasp_Stability_Prediction.pdf
confidence: high
source: pdf
aliases: []
---

# SCT-CNN: A Spatio-Channel-Temporal Attention CNN for Grasp Stability Prediction

## 📌 年份
2021

## 🔑 论文识别码
DOI: 10.1109/ICRA48506.2021.9561397

## 👥 作者与所属院校
- 作者：Gang Yan, Alexander Schmitz, Satoshi Funabashi, Sophon Somlor, Tito Pradhono Tomo 等
- 机构：早稻田大学（Waseda University）现代机械工程系、理工学研究所

## 📖 研究背景
- 传统[[抓取规划]]主要依赖视觉，但抓取是否稳定还取决于接触处的力与形变，纯视觉难以判断。
- 既有触觉方法对触觉矩阵的所有空间区域与序列的所有时间步一视同仁，冗余信息干扰特征学习。
- 该文首次把空间-通道与时间注意力共同引入纯触觉[[抓取稳定性预测]]。

## ❓ 需要解决的问题
- 只用抓取过程中的触觉序列、不用视觉，能否预测提起后的成败（稳定/掉落）？
- 空间-通道注意力与时间注意力各自带来多少精度增益，能否叠加？
- 与 CNN-LSTM、Conv3D、ConvLSTM、Deep Forest 等模型相比是否更优？

## 📥📤 输入与输出
- 输入：两片 6×4 三轴 uSkin 分布式触觉阵列读数（含接触前数据），100 Hz 采样、取 125 步序列（0–6.25 s）。
- 输出：未来提起结果的二分类（稳定/掉落）。

## ✅ 论文最终达到的效果
- 52 种日常物体、50 种抓取，共 13,000 条序列（按试次 3:1:1 划分），SCT-CNN 准确率 81.38%。
- 相比 Deep Forest 74.21%、ConvLSTM 75.58%、Conv3D 76.23%、CNN-LSTM 79.76%，最高提升 7.17%。
- 仅用时间注意力（80.69%）或仅用空间-通道注意力（80.57%）均有效，二者同用最佳。
- 可变形卷积（−1.46%）与非局部模块（−3.31%）反而掉点；再叠加 LSTM 也未提升。
- 作者认为该注意力结构可迁移到[[滑移检测]]、硬度感知等触觉学习任务。

## 🔗 关联
- [[Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration]]
- [[Grasp Prediction based on Local Finger Motion Dynamics]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#抓取稳定性预测 #触觉传感 #注意力机制 #CNN #uSkin
