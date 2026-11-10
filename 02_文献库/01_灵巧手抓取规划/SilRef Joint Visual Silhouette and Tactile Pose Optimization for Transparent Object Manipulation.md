---
title: "SilRef: Joint Visual Silhouette and Tactile Pose Optimization for Transparent Object Manipulation"
year: 2026
doi: 10.1109/LRA.2026.3653340
arxiv: 
key: KB-003
venue: IEEE Robotics and Automation Letters (RA-L), Vol. 11, No. 3
theme: 02_文献库/01_灵巧手抓取规划
tags: [透明物体, 位姿细化, 轮廓对齐, 触觉接触点, 视触融合]
pdf: ../../../2026_SilRef_Joint_Visual_Silhouette_and_Tactile_Pose_Optimiz.pdf
confidence: high
source: pdf
aliases: []
---

# SilRef: Joint Visual Silhouette and Tactile Pose Optimization for Transparent Object Manipulation

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1109/LRA.2026.3653340

## 👥 作者与所属院校
- 作者：Jean-Baptiste Weibel, Clemence Dubois, Negar Layegh Khavidaki, Saifeddine Aloui, Mathieu Grossard 等（7 人）
- 机构：维也纳工业大学（TU Wien）自动化与控制研究所、维也纳自然资源与生命科学大学（BOKU）、巴黎-萨克雷大学 CEA LIST

## 📖 研究背景
- 实验室自动化需操作中小型透明容器，而透明件外观随背景变化、深度传感器测量严重失准。
- 深度法位姿细化与 render-and-compare 依赖深度图或真实感渲染，在透明物体上双双失效。
- 该文改用轮廓（silhouette）配几何线索（触觉接触点或支撑面）做梯度下降位姿优化。

## ❓ 需要解决的问题
- 只用物体轮廓与 3D 模型渲染，能否在无深度、无真实感渲染时把 6D 位姿约束住？
- 抓取中的触觉接触点能否作为几何线索，消除透明件位姿的旋转歧义？
- 在 Keypose 与新采集的 Tracebot In-Gripper 数据集上能否超过 ICP 与 Megapose6D？

## 📥📤 输入与输出
- 输入：单目 RGB 图像、物体 3D 模型、初始位姿假设；in-gripper 场景另含触觉传感器给出的接触点（或支撑面信息）。
- 输出：细化后的 6D [[抓取位姿]]，以 ADD-S 评价，供后续[[抓取规划]]使用。

## ✅ 论文最终达到的效果
- ADD-S@0.01 m 相对 Megapose6D 与 ICP 提升 2.8 倍（Keypose）与 2.7 倍（Tracebot In-Gripper）。
- 多数实验（54%）的 ADD-S 小于 1 cm；相较基线有明显更大的收敛域。
- 消融显示只用轮廓或只用接触点都不足以稳定约束，二者结合才使大部分预测低于 1 cm。
- 背景由均匀换成带纹理时平均 ADD-S 由 0.031 m 变为 0.028 m，对背景变化不敏感。
- 新数据集含 7 类透明物体、608 张抓取图像及对应触觉输出，用于[[视触融合]]位姿细化评测。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#透明物体 #位姿细化 #轮廓对齐 #触觉接触点 #视触融合
