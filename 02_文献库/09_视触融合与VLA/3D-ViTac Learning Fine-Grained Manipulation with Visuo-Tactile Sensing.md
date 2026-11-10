---
title: "3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing"
year: 2024
doi: 
arxiv: 2410.24091
key: KB-005
venue: 8th Conference on Robot Learning (CoRL 2024)
theme: 02_文献库/09_视触融合与VLA
tags: [视触融合, 柔性触觉阵列, 3D表示, 扩散策略, 模仿学习, 双臂操作]
pdf: ../../../3D-ViTac.pdf
confidence: high
source: pdf
aliases: []
---

# 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing

## 📌 年份
2024

## 🔑 论文识别码
arXiv: 2410.24091（CoRL 2024）

## 👥 作者与所属院校
- 作者：Binghao Huang, Yixuan Wang, Xinyi Yang, Yiyue Luo, Yunzhu Li
- 机构：哥伦比亚大学、伊利诺伊大学厄巴纳-香槟分校、华盛顿大学

## 📖 研究背景
- 视觉给全局语义、触觉给局部接触，细粒度操作两者缺一不可。
- 现有光学[[视触觉传感器]]体积大或刚性高，商用触觉件昂贵，低成本阵列又过于稀疏。
- 触觉信号局部、物理，视觉全局、语义，模态差异要求硬件与学习算法协同设计。

## ❓ 需要解决的问题
- 能否做出覆盖大面积、柔性、低成本且单元面积仅 3 mm² 的密集触觉阵列？
- 如何把触觉与视觉统一到同一 3D 表示空间，并保留各自的空间结构？
- 视触融合策略在易碎物抓取、遮挡、手内调整与双臂协作上是否显著优于纯视觉？

## 📥📤 输入与输出
- 输入：多视角 RGB 图像 + 每指 16×16 触觉阵列读数（转为 3D 触觉点云，与相机坐标对齐）；人类[[主从遥操作]]示教轨迹。
- 输出：扩散策略（diffusion policy）生成的双臂动作序列，经[[模仿学习]]训练得到。

## ✅ 论文最终达到的效果
- 统一 3D 视触表示配扩散策略，在四项接触密集任务上全面优于纯视觉与触觉图像基线。
- Hex Key 手内调整成功率 0.95（纯 RGB 0.55），整任务 0.90（0.45）。
- 三明治配餐整任务 0.85（纯 RGB 0.60）；单/多葡萄抓取与鸡蛋等易碎物抓取更稳。
- 触觉 16×16 分辨率略优于 8×8，明显优于 4×4 与二值触觉；连续信号对[[手内操作]]最有效。
- 采集时向操作者回显实时触觉信号，可提升示教数据质量（10 名新手对比，完成任务更快）。

## 🔗 关联
- [[VLA-Touch Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback]]
- [[N0-VTLA Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens]]
- [[OmniVTLA Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing]]

## 🏷️ 标签
#视触融合 #触觉阵列 #3D表示 #扩散策略 #双臂操作
