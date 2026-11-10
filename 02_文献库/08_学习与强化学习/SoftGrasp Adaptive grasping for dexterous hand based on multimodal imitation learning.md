---
title: "SoftGrasp: Adaptive grasping for dexterous hand based on multimodal imitation learning"
year: 2025
doi: 10.1016/j.birob.2025.100217
arxiv: 
key: KB-135
venue: Biomimetic Intelligence and Robotics, vol. 5, 100217
theme: 02_文献库/08_学习与强化学习
tags: [模仿学习, 多模态融合, 灵巧手抓取, 关节力矩, 示教数据采集]
pdf: ../../../SoftGrasp.pdf
confidence: high
source: pdf
aliases: []
---

# SoftGrasp: Adaptive grasping for dexterous hand based on multimodal imitation learning

## 📌 年份
2025（2024-11-25 投稿，2025-01-17 录用，2025-01-28 在线）

## 🔑 论文识别码
DOI: 10.1016/j.birob.2025.100217

## 👥 作者与所属院校
- 作者：Yihong Li, Ce Guo, Junkai Ren, Bailiang Chen, Chuang Cheng 等
- 机构：国防科技大学智能科学学院

## 📖 研究背景
- 抓取可变形物体时，形状与尺寸随手接触动态变化，固定力控要么压坏要么滑落。
- 人类靠视觉、本体感觉与触觉协同调节指力，机器人却缺少同等的多模态示教数据。
- 现有方法或依赖昂贵触觉传感器，或只处理刚性物体，跨尺寸、形状、硬度的自适应能力不足。

## ❓ 需要解决的问题
- 如何搭建带力反馈的沉浸式示教平台，同步采集视觉图像、指关节角与[[关节力矩控制]]信号？
- 多头注意力怎样对齐并融合视觉、角度、力矩三种异构且采样率不同的模态？
- 角度-力矩联合损失的行为克隆，能否学到「先轻触、再夹紧」的多阶段力曲线？
- 对训练中未见的尺寸、形状、硬度组合，成功率能否保持？

## 📥📤 输入与输出
- 输入：UR3 机械臂末端五指灵巧手（6 个控制自由度）、RealSense D435i 视觉图像、数据手套映射的期望关节角、实测关节角与关节力矩。
- 输出：下一时刻各指期望关节角，经关节力矩闭环驱动指尖力，实现自适应多阶段抓取。

## ✅ 论文最终达到的效果
- 真实场景 12 类物体各 10 次抓取，平均成功率 98%，覆盖软塑、可变形与刚性物体。
- 对比基线：ACT 91%、Timesformer 79%、直接拼接特征仅 13%。
- 模态消融：三模态全用 98%，仅视觉 46%，视觉+力矩 43%，仅力矩 0%。
- 损失权重 λ=0.1 最优；λ=0 时成功率降至 68.3%，λ=0.5 时仅 38.8%。
- 力矩分布比 Timesformer 更集中，说明学到的是力控制而非仅位置复现；代码已开源。

## 🔗 关联
- [[Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations]]
- [[Interactive imitation learning for dexterous robotic manipulation challenges and perspectives—a survey]]
- [[Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids]]

## 🏷️ 标签
#模仿学习 #多模态融合 #灵巧手抓取 #关节力矩 #示教采集
