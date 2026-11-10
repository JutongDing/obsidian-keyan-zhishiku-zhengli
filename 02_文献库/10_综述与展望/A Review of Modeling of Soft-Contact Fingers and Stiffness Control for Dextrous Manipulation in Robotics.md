---
title: A Review of Modeling of Soft-Contact Fingers and Stiffness Control for Dextrous Manipulation in Robotics
year: 2001
doi: 
arxiv: 
key: KB-017
venue: Proceedings of the 2001 IEEE International Conference on Robotics & Automation (ICRA), Seoul
theme: 02_文献库/10_综述与展望
tags: [综述, 软指接触, 接触力学, 刚度控制, 抓取刚度]
pdf: ../../../A review of modeling of soft-contact fingers and stiffness control for dextrous manipulation in robotics.pdf
confidence: high
source: pdf
aliases: []
---

# A Review of Modeling of Soft-Contact Fingers and Stiffness Control for Dextrous Manipulation in Robotics

## 📌 年份
2001

## 🔑 论文识别码
无 DOI（本地编号 KB-017；ICRA 2001，Seoul，2001-05-21/26）

## 👥 作者与所属院校
- 作者：Yanmei Li, Imin Kao
- 机构：纽约州立大学石溪分校机械工程系

## 📖 研究背景
- [[灵巧手]]操作横跨运动学、滚动与滑动、接触力学、抓取规划与优化、动力学与控制，结论高度依赖接触模型选择。
- 文献普遍假设点接触或软接触；软接触更贴近真实，却因建模复杂而长期少用。
- 软指接触可传递绕公共法向的纯扭矩，直接改变运动学、动力学与稳定抓取所需的手指数。
- Hertz 接触模型基于线性弹性假设，需推广后才能描述软指的实际行为。

## ❓ 需要解决的问题
- 软指接触如何在力与力矩两个层面建模，兼顾物理真实与可计算性？
- 含扭矩时[[摩擦锥]]如何推广为摩擦极限曲面，以刻画切向力与扭矩的耦合？
- 传统同余变换在存在外载荷时是否仍成立，关节刚度到笛卡尔刚度的映射应如何修正？
- 保守刚度控制应满足什么判据？

## 📥📤 输入与输出
- 输入：接触力学、抓取刚度与刚度控制方向的既有文献及人手抓取刚度实验数据。
- 输出：接触类型分类、软接触与摩擦极限曲面模型、保守同余变换（CCT）及其刚度判据。

## ✅ 论文最终达到的效果
- 厘清三类接触：无摩擦点接触（仅法向力）、有摩擦点接触即硬指（锥内传力）、软指面接触（可传扭矩）。
- 给出最少手指数结论：实现特定属性抓取需 7 个无摩擦点接触、4 个硬指或 3 个软指。
- 把 Hertz 模型由线性弹性推广到软接触，用椭球摩擦极限曲面替代锥形近似描述扭矩—切向力耦合。
- 指出 Salisbury（1980）常规同余变换仅在外力为零时成立；提出 CCT，说明任意保守系统在非零外载下 6×6 刚度矩阵非对称，并给出 R3×3 与 6×6 的保守刚度判据。
- 综述抓取刚度建模与实验（含人手抓取实验分解为对称/反对称分量），为后续[[阻抗控制]]与柔顺控制提供理论基础。

## 🔗 关联
- [[A comprehensive review of dexterous robotic hands design, implementation, and evaluation]]
- [[A Review of Robotic Dexterous Hands]]
- [[A review of adaptive intelligence in tactile sensing robotic hands for human centered dexterous control]]

## 🏷️ 标签
#综述 #软指接触 #接触力学 #刚度控制 #抓取刚度
