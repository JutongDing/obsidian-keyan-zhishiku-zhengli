---
title: "OmniVTLA: Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing"
year: 2026
doi: 
arxiv: 2508.08706
key: KB-107
venue: arXiv 预印本（arXiv:2508.08706v3，2026-06 修订）
theme: 02_文献库/09_视触融合与VLA
tags: [VLA, 触觉编码器, 跨模态对齐, 接触密集操作, ObjTac数据集]
pdf: ../../../OmniVTLA.pdf
confidence: high
source: pdf
aliases: []
---

# OmniVTLA: Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing

## 📌 年份
2026（v3 首页标注 2026-06-16；arXiv 首次提交为 2025-08）

## 🔑 论文识别码
arXiv: 2508.08706（v3，2026-06-15；无 DOI）

## 👥 作者与所属院校
- 作者：Zhengxue Cheng、Yiqian Zhang、Anni Tang、Keyu Wang、Wenkang Zhang 等
- 机构：上海交通大学、Paxini Tech

## 📖 研究背景
- [[视觉-语言-动作模型]]（VLA）建立在视觉-语言基座上，但触觉数据难获取，模型基本忽略触觉，在接触密集任务上失败。
- 已有触觉预训练偏重触觉理解任务，未考察交互过程中触觉如何变化，也少在真实操作任务上评估。
- 已有把触觉塞进 VLA 的尝试把触觉当低层信号，未与视觉、语言做语义对齐，[[视触融合]]因此停在浅层。

## ❓ 需要解决的问题
- 触觉信号能否在语义层与视觉、语言对齐，而非仅在特征层拼接？
- 触觉编码器该用单路预训练 ViT，还是「视觉 ViT + 语义对齐 ViT」双路结构，参数匹配下哪个更好？
- 在抓取放置与[[轴孔装配]]上，成功率、完成时间与轨迹平滑度能提升多少？

## 📥📤 输入与输出
- 输入：语言指令、腕部相机 RGB 图像、Paxini Gen2 触觉力场序列（两指夹爪 10 个 token、四指手 25 个 token）。
- 输出：末端位姿增量（xyz + 6D 旋转）、夹爪开度或 16 个关节角的动作序列。

## ✅ 论文最终达到的效果
- 构建 ObjTac：56 个物体、10 个类别、135K 三模态（文本/视觉/触觉）样本，用跨模态对比学习训练语义对齐触觉编码器（SA-ViT）。
- 抓取放置成功率：两指夹爪 96.9%（较基线 +21.9%），四指[[灵巧手]] 100%（+6.2%）。
- 轴孔装配成功率 83.3%（+33.3%），覆盖 0.9/1.2/1.8 mm 三种间隙。
- 借触觉引导缩短完成时间、轨迹更平滑；杂乱堆叠场景无提升（那里靠视觉导航）。
- 平台：UR5 + 两指夹爪（2 个触觉传感器）/ 四指手（11 个触觉传感器），[[主从遥操作]]采集示教。

## 🔗 关联
- [[3D-ViTac Learning Fine-Grained Manipulation with Visuo-Tactile Sensing]]
- [[VLA-Touch Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback]]
- [[N0-VTLA Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens]]

## 🏷️ 标签
#VLA #视触融合 #触觉编码器 #轴孔装配
