---
title: FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network
year: 2018
doi: 
arxiv: 1810.02653
key: KB-050
venue: arXiv preprint (cs.RO)
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉, 滑移检测, 卷积LSTM, 传感器设计, 形变场]
pdf: ../../../FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network.pdf
confidence: high
source: pdf
aliases: []
---

# FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network

## 📌 年份
2018（arXiv 1810.02653v1，2018-10-05）

## 🔑 论文识别码
arXiv:1810.02653

## 👥 作者与所属院校
- 作者：Yazhan Zhang, Zicheng Kan, Yu Alexander Tse, Yang Yang, Michael Yu Wang
- 机构：香港科技大学（待核对）

## 📖 研究背景
- 触觉对稳定抓取至关重要，缺少触觉反馈时人难以维持稳定抓握。
- 光学式[[视触觉传感器]]把接触变形转成图像，可在大工作面上获得高分辨、高灵敏信号。
- 既有滑移判别多依赖手工特征，随物体与接触条件变化而失稳，难以覆盖大量目标物体。

## ❓ 需要解决的问题
- 如何做出结构紧凑、易制造、分辨率高的指形光学触觉传感器？
- 标记点阵列的位移场能否作为统一的接触表征，兼容不同物体？
- 卷积 LSTM 能否从形变时序中直接学出滑移/非滑移判别，并达到高准确率？

## 📥📤 输入与输出
- 输入：指内鱼眼相机拍摄的软皮肤标记点阵列图像序列，经跟踪得到[[触觉图像]]形变场。
- 输出：滑移/非滑移二分类结果（[[滑移检测]]），以及用于力估计的形变场。

## ✅ 论文最终达到的效果
- 传感器由软皮肤、嵌入式标记阵列、刚性框架与鱼眼摄像头组成，体积紧凑、易于制作。
- 数据采集借用人手感：手抓 12 种日常物体与传感器皮肤交互，由人判定并标注滑移标签。
- 卷积 LSTM 滑移分类框架在测试集上达到 97.62% 准确率。
- 作者预期该判别可用于[[抓取力调节]]与更主动的接触探索，提升抓取稳定性。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#视触觉 #滑移检测 #卷积LSTM #传感器设计
