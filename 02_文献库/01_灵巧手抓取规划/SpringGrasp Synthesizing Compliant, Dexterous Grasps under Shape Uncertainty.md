---
title: "SpringGrasp: Synthesizing Compliant, Dexterous Grasps under Shape Uncertainty"
year: 2024
doi: 
arxiv: 2404.13532
key: KB-138
venue: arXiv 预印本（待补）
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取规划, 形状不确定性, 柔顺抓取, 阻抗控制, 可微指标]
pdf: ../../../SpringGrasp-Compliant-Dexterous-Grasps-under-Shape-Uncertainty-2024.pdf
confidence: high
source: pdf
aliases: []
---

# SpringGrasp: Synthesizing Compliant, Dexterous Grasps under Shape Uncertainty

## 📌 年份
2024（arXiv 首版 2024-04-21）

## 🔑 论文识别码
arXiv: 2404.13532（无 DOI）

## 👥 作者与所属院校
- 作者：Sirui Chen, Jeannette Bohg, C. Karen Liu
- 机构：斯坦福大学计算机科学系

## 📖 研究背景
- 多指[[灵巧手]]在任意物体上生成稳定抓取，是高级操作的前提能力。
- 既有可微[[抓取质量]]指标多假设物体几何精确已知，而真实观测含噪且只有部分视角。
- 该文把柔顺抓取建模为指尖到物体的虚拟弹簧，用整段接触过程的动态行为来评价抓取优劣。

## ❓ 需要解决的问题
- 只有含噪、不完整的点云时，如何优化[[抓取位姿]]而不是从固定候选中挑选？
- 能否把「预抓取—接触—稳定」全过程的动态写成可解析、可微的指标，供梯度优化？
- 每指[[阻抗控制]]增益能否与手部位姿联合优化，而不靠人工整定？
- 相对基于[[力封闭]]的规划器，形状不确定条件下成功率能高多少？

## 📥📤 输入与输出
- 输入：单/双视角 RGB-D 重建的含噪部分物体表面、Allegro 手运动学模型。
- 输出：优化后的预抓取手部位姿，以及每指笛卡尔阻抗增益（刚度、阻尼），交由阻抗控制器执行。

## ✅ 论文最终达到的效果
- 提出 SpringGrasp planner 与可微的 SpringGrasp metric，用虚拟弹簧动能与平衡位形评价抓取。
- 真机 14 件日常物体：双视角成功率 89%，单视角仍有 84%。
- 相比基于力封闭的规划器，成功率至少高 18%。
- 无需精确物体模型或触觉探测重规划，即可在形状不确定下稳定抓取。
- 平衡位形由 Kabsch 算法解析求解，指标可端到端反传到位姿与增益。

## 🔗 关联
- [[GraspQP Differentiable Optimization of Force Closure for Diverse and Robust Dexterous Grasping]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[On the Form-Closure Property of Robotic Grasping]]

## 🏷️ 标签
#抓取规划 #形状不确定性 #柔顺抓取 #阻抗控制 #可微指标
