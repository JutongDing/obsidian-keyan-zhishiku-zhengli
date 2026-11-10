---
title: Slip Detection with Combined Tactile and Visual Information
year: 2018
doi: 
arxiv: 1802.10153
key: KB-134
venue: arXiv 预印本（待补）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, GelSight, 视触融合, CNN-RNN, 抓取稳定性]
pdf: ../../../Slip Detection with Combined Tactile and Visual Information.pdf
confidence: high
source: pdf
aliases: []
---

# Slip Detection with Combined Tactile and Visual Information

## 📌 年份
2018（arXiv 首版 2018-02-27）

## 🔑 论文识别码
arXiv: 1802.10153（无 DOI）

## 👥 作者与所属院校
- 作者：Jianhua Li, Siyuan Dong, Edward Adelson
- 机构：MIT CSAIL（计算机科学与人工智能实验室）

## 📖 研究背景
- 滑移是抓取失效的直接前兆，接触状态反馈对[[抓取力调节]]与策略选择不可或缺。
- 仅靠触觉时，物体刚接触、表面纹理贫乏或几乎未受力，信号弱到难以判别。
- 该文把[[GelSight]]触觉图像与夹爪外置相机图像并联，用深度网络做端到端的抓取稳定性判别。

## ❓ 需要解决的问题
- 触觉与视觉两路图像序列能否互补，覆盖从「几乎无接触」到「明显滑移」的全区间？
- 不预设物体质量、摩擦、几何等物理参数，能否直接判定一次抓取是否稳定？
- 8 帧图像序列配合 CNN 提特征、RNN 比时序，是否足以刻画滑移动态？
- 训练用日常物体上学到的判别，能否泛化到完全未见过的物体？

## 📥📤 输入与输出
- 输入：UR5 机械臂 + WSG-50 两指夹爪，一指换装 GelSight（640×480，0.024 mm/pixel），夹爪顶部外置 USB 相机；两路各取 8 帧图像序列。
- 输出：该次抓取的二分类标签（发生滑移 / 未发生滑移，等价于抓取稳定与否）。

## ✅ 论文最终达到的效果
- 训练集覆盖 84 件日常物体、1102 次抓取-抬升；测试集为 10 件未见物体、152 次抓取。
- 检测准确率最高达 88.03%，明显高于作者前作基于标记位移阈值的 71%。
- 无需物体几何与质量先验，可直接服务自动力控、抓取策略选择与精细操作。
- 作者指出数据量仍是主要瓶颈，扩大数据集后精度有望继续提升。

## 🔗 关联
- [[Slip Detection and Stable Grasping With Multi-Fingered Robotic Hand Using Deep Learning Approach]]
- [[Learning to Detect Slip with Barometric Tactile Sensors and a Temporal Convolutional Neural Network]]
- [[Learning incipient slip with GelSight sensors Attention Classification with Video Vision Transformers]]

## 🏷️ 标签
#滑移检测 #GelSight #视触融合 #CNN-RNN #抓取稳定性
