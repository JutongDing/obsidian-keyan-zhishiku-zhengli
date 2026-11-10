---
title: Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy
year: 2024
doi: 
arxiv: 2303.00935
key: KB-089
venue: arXiv preprint (arXiv:2303.00935v4)
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, 视触觉, GelSight, 接触力场, 熵, 抓取力调节]
pdf: ../../../Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy.pdf
confidence: high
source: pdf
aliases: []
---

# Learning to Detect Slip through Tactile Estimation of the Contact Force Field and its Entropy

## 📌 年份
2024（arXiv v4，2024-04-28 更新）

## 🔑 论文识别码
arXiv: 2303.00935（无 DOI）

## 👥 作者与所属院校
- 作者：Xiaohai Hu, Aparajit Venkatesh, Yusen Wan, Guiliang Zheng, Neel Jawale 等
- 机构：华盛顿大学机械工程系、Amazon（Paul Birkmeyer）；UW+Amazon Science Hub 资助

## 📖 研究背景
- 抓取与操作中[[滑移检测]]是防止掉落的底线能力，人类靠皮肤感受器无视觉地调节握力。
- 既有方案多依赖视觉外感或固定力阈值，面对未知物体与未知接触条件时泛化差。
- 该文用[[GelSight]] Mini 光学触觉传感器，把标记点位移场重建成接触力场，以力场不均匀性的熵作为物理可解释特征。

## ❓ 需要解决的问题
- 滑移瞬间触觉读数的空间不均匀性能否量化成可分特征？
- 熵 E 与熵变化率 δE/δt 是否优于平均位移速度分量 Vx、Vy？
- 在随机划分与跨物体划分两种协议下，DT/RF/SVM/KNN 谁更稳、是否仍实时？
- 检测到[[初始滑移]]后能否在线闭环加力，完成真实书架取物任务？

## 📥📤 输入与输出
- 输入：双指[[触觉图像]]序列（标记点位移场），经传感器力场重建得到分布接触力。
- 输出：静态/滑移二分类标签（逐帧实时输出），以及触发后夹爪开合增量，即[[抓取力调节]]量。

## ✅ 论文最终达到的效果
- 10 种常见物体约 14,000 个样本，五折交叉验证下 KNN 四特征平均准确率 95.61%（F1 95.40）。
- 用 E 与 δE/δt 替代 Vx、Vy 后，DT/RF/SVM/KNN 准确率分别提升 11.7%、6.7%、4.9%、11.2%。
- 未见物体测试：浣熊玩具 93.73%、隐形眼镜液 86.66%、书 71.69%（跨物体泛化明显衰减）。
- 单帧推理 0.29–0.94 ms（DT 最快、KNN 0.94 ms），可嵌入实时回路。
- UR5e + Robotiq 平行夹爪完成"从书架抽书"：滑移前逐步加力，全程未掉落。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand]]
- [[FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network]]

## 🏷️ 标签
#滑移检测 #视触觉 #GelSight #接触力场 #熵 #抓取力调节
