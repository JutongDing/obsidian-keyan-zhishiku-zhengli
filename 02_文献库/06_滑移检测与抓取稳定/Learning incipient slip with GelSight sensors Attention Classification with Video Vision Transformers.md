---
title: "Learning incipient slip with GelSight sensors: Attention Classification with Video Vision Transformers"
year: 2024
doi: 10.1109/IROS58592.2024.10801324
arxiv: 2103.13460
key: KB-088
venue: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2024
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [初始滑移, 滑移检测, GelSight, 视频视觉Transformer, 触觉传感]
pdf: ../../../Learning incipient slip with GelSight sensors.pdf
confidence: high
source: pdf
aliases: 
---

# Learning incipient slip with GelSight sensors: Attention Classification with Video Vision Transformers

## 📌 年份
2024

## 🔑 论文识别码
DOI: 10.1109/IROS58592.2024.10801324

## 👥 作者与所属院校
- 作者：Amit Parag、Edward H. Adelson、Ekrem Misimi
- 机构：挪威 SINTEF Ocean、美国麻省理工学院（MIT）

## 📖 研究背景
- [[初始滑移]]（incipient slip）是物体将滑未滑的临界阶段，此时补救最省力，错过就只能掉落。
- 滑移本质是动态过程，单帧触觉图纹理变化微弱，靠静态特征难以及时判定。
- 标注滑移时刻昂贵，样本量小，需要能吃小数据的时序模型。

## ❓ 需要解决的问题
- 视频 Transformer 能否在滑移真正发生之前若干帧预测其起始，而不只是事后识别？
- 需要多长的历史帧窗口才能保持精度，能否压缩到 2–5 帧以适配实时控制？
- 对训练中未出现的物体，模型能否零样本泛化？

## 📥📤 输入与输出
- 输入：双[[GelSight]]以 25 帧/秒采集的触觉视频，取滑移前连续 5 帧（另做 4/3/2 帧消融）。
- 输出：滑移起始的二分类概率，作为预防性加力或收紧夹爪的触发信号。

## ✅ 论文最终达到的效果
- 用 Video Vision Transformer（ViViT）直接映射原始触觉帧到滑移起始标签，利用自注意力建模时空相关。
- 通过抓取、抬升、抖动与扭转 30 件日用品诱发滑移，构建训练集；数据增强含翻转、通道交换与加噪。
- 5、4、3、2 帧消融均保持稳定精度，说明短窗口即可工作。
- 在 10 个未见物体上零样本平均预测准确率达 99%。
- 最多可提前至滑移前第 5 帧预警，为"更牢固地闭合夹爪"等预防动作留出时间。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#初始滑移 #滑移检测 #视触觉 #视频理解
