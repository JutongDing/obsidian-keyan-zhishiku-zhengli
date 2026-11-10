---
title: Grasp Prediction based on Local Finger Motion Dynamics
year: 2025
doi: 
arxiv: 2506.10818
key: KB-059
venue: arXiv 预印本（cs.HC）
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取预测, 手指运动学, LSTM, 交互延迟, 到达-抓取]
pdf: ../../../Grasp Prediction based on Local Finger Motion Dynamics.pdf
confidence: high
source: pdf
aliases: [Grasp Prediction based on Local Finger Motion Dynamics]
---

# Grasp Prediction based on Local Finger Motion Dynamics

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2506.10818（预印本，无 DOI）

## 👥 作者与所属院校
- 作者：Dimitar Valkov、Pascal Kockwelp、Florian Daiber、Antonio Krüger
- 机构：萨尔大学与德国人工智能研究中心（DFKI）、明斯特大学

## 📖 研究背景
- 基于手与手势的自然交互受跟踪延迟与精度不足困扰，选择错误与操作不精确直接降低体验。
- 到达-抓取（reach-to-grasp, R2G）过程中手指逐渐成形，其形态与物体尺寸、形状及使用意图相关。
- 已有工作多用整手轨迹预测目标，很少利用这种局部手指动力学信息。
- 本文切入：只用手指运动特征训练 LSTM，实时预测目标物体、抓取时刻与剩余距离，为[[抓取规划]]与界面提前调度提供依据。

## ❓ 需要解决的问题
- 仅凭局部手指运动学，能否在手掌到达目标之前判别被抓物体？
- 距抓取的时间与到目标距离能预测到多准，提前量是否足以抵消点对点延迟？
- 对训练中未出现的用户，预测精度下降多少？
- 物体尺寸、形状与身份的可分性分别受什么限制？

## 📥📤 输入与输出
- 输入：手部标记点轨迹派生的 31 维特征（手速 VH、手指多边形 FP、掌心多边形 PP），25 帧滑窗序列。
- 输出：到目标物体的距离与距抓取剩余时间（回归）；物体尺寸、形状、身份类别（分类）。

## ✅ 论文最终达到的效果
- 采集 16 名被试、768 条序列（每人 48 条），覆盖真实物体与合成物体。
- 抓取时刻预测精度优于 21 ms，已接近数据集同步精度（约 25 ms）。
- 距离预测 MAE：已知用户小于 1 cm，未知用户小于 3 cm。
- 目标尺寸判别准确率优于 97%；抓取前 350 ms 最差情形仍不低于 85%。
- 有效提前量 280–400 ms；对真实物体判别良好，但合成物体形状判别仅约 30%，抓取类型是关键限制。

## 🔗 关联
- [[Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration]]
- [[A Mathematical Introduction to Robotic Manipulation]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#抓取预测 #手指运动学 #LSTM #交互延迟 #到达-抓取
