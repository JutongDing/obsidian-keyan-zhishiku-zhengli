---
title: Slip Detection and Stable Grasping With Multi-Fingered Robotic Hand Using Deep Learning Approach
year: 2025
doi: 10.1049/csy2.70036
arxiv: 
key: KB-133
venue: IET Cyber-Systems and Robotics
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, CNN-LSTM, 多指手, 抓取力补偿, 触觉传感]
pdf: ../../../Slip Detection and Stable Grasping With Multi‐Fingered.pdf
confidence: high
source: pdf
aliases: []
---

# Slip Detection and Stable Grasping With Multi-Fingered Robotic Hand Using Deep Learning Approach

## 📌 年份
2025（2025-07-07 投稿，2025-10-23 录用）

## 🔑 论文识别码
DOI: 10.1049/csy2.70036

## 👥 作者与所属院校
- 作者：Haoliang Xu, Syed Muhammad Nashit Arshad, Shichi Peng, Han Xu, Hang Yin 等
- 机构：深圳技术大学灵巧机器人实验室（Dexterous Robotics Lab）

## 📖 研究背景
- 多指[[灵巧手]]在动态环境中作业，[[滑移检测]]与抓取稳定直接决定实时性能与成功率。
- 阈值法与纯 PID 方案难以捕捉细微滑移，物体往往在掉落后才被察觉。
- 深度学习可同时利用触觉阵列的空间分布与时间演化，但受样本量与单指覆盖限制。

## ❓ 需要解决的问题
- 每指 16 个压阻 taxel、连续 100 帧的[[触觉图像]]序列，能否用 CNN-LSTM 同时刻画滑移的空间与时间特征？
- 数据增强能否从有限的真实抓取数据扩出可训练、可泛化的数据集？
- 检测粒度能否下沉到单根手指，做到哪指滑就补哪指的定向[[抓取力调节]]？
- 相比纯 CNN、纯 LSTM 与传统 PID，闭环抓取成功率能提升多少？

## 📥📤 输入与输出
- 输入：五指手各指尖压阻阵列的触觉图像序列（连续 100 帧切窗），手本体控制频率 67 Hz。
- 输出：每指三分类（滑移/无滑移/无接触），触发滑移后按指生成抓取力补偿增量。

## ✅ 论文最终达到的效果
- CNN-LSTM（40 帧输入）平均检测准确率 91.39%，高于纯 CNN 89.16%、LSTM 85.59%。
- 精确率 92.61%、召回率 88.41%、F1 分数 89.26%。
- 100 次真实抓取成功 82 次（82%），对比 CNN 70%、LSTM 72%、PID 仅 54%。
- 单指级力补偿避免了对易碎、易变形物体的整体过度加压。
- 局限：小型不规则物体（如眼镜盒）接触稀疏，易被误判为[[初始滑移]]。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing]]
- [[FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network]]

## 🏷️ 标签
#滑移检测 #CNN-LSTM #多指手 #抓取力补偿 #压阻触觉
