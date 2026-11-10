---
title: Learned Slip-Detection-Severity Framework using Tactile Deformation Field Feedback for Robotic Manipulation
year: 2024
doi: 
arxiv: 2411.07442
key: KB-082
venue: arXiv preprint（cs.RO, v1）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, 初始滑移, 触觉传感, GelSight, 形变矢量场]
pdf: ../../../Learned Slip-Detection-Severity Framework using Tactile Deformation Field Feedback for Robotic Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# Learned Slip-Detection-Severity Framework using Tactile Deformation Field Feedback for Robotic Manipulation

## 📌 年份
2024

## 🔑 论文识别码
arXiv:2411.07442

## 👥 作者与所属院校
- 作者：Neel Jawale、Navneet Kaur、Amy Santoso、Xiaohai Hu、Xu Chen 等
- 机构：华盛顿大学（University of Washington）机械工程系 MACS 实验室，美国

## 📖 研究背景
- 传统[[滑移检测]]把滑移当二值事件，忽略滑得多快、多严重，控制策略因此不够精细。
- 视觉相机易被手指遮挡，[[视触觉传感器]]能直接观测接触面形变，适合实时闭环。
- 已有方法多依赖已知物体或力控，缺乏对未知形状、纹理、质量的通用性。

## ❓ 需要解决的问题
- 如何从[[GelSight]] Mini 的形变矢量场中提取能刻画滑移非线性动力学的特征？
- 滑移严重程度（物体相对传感器表面的滑移速度）能否由触觉特征直接回归？
- 仅凭滑移检测 + 严重度反馈，不借助显式力控与物体先验，能否完成竖直滑动任务？

## 📥📤 输入与输出
- 输入：GelSight Mini 标记点位移矢量场序列，提取速度、散度、旋度、归一化接触面积及其时间导数。
- 输出：滑移发生概率（分类）与滑移速度估计（cm/s），据此调节 Robotiq 夹爪开口位置。

## ✅ 论文最终达到的效果
- 构建约 66,000 个数据点的数据集；滑移检测用随机森林/梯度提升，严重度用 LSTM 与 MLP 回归。
- 滑移检测平均准确率 92%（五折交叉验证 99.1%）；未见物体上剪刀、掸子 >99%，海绵跌至 43.7%。
- 严重度估计：合并全部特征后 LSTM 在已知物体上 MAE 0.26 cm/s、RMSE 0.77 cm/s、R² 0.75；未见物体平均 MAE 0.6 cm/s。
- 真值由 ArUco 标记 + 指数加权滤波给出，速度剖面覆盖 0.8–6.7 cm/s，每档重复 5 次。
- 在 UR5e + Robotiq Hand-E（位置控制指）上做竖直滑移实验，沿 10 条轨迹验证闭环。
- 无需显式力控、无需物体尺寸/几何/纹理先验，靠滑移严重度反馈即可减少过度补偿。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#滑移检测 #触觉传感 #视触觉 #抓取稳定
