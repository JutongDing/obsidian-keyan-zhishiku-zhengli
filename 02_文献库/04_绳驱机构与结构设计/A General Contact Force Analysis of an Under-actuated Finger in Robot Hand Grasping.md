---
title: A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping
year: 2016
doi: 10.5772/62131
arxiv: 
key: KB-006
venue: International Journal of Advanced Robotic Systems, Vol. 13
theme: 02_文献库/04_绳驱机构与结构设计
tags: [欠驱动手指, 接触力分配, 静力学分析, 整指抓取, 虚拟样机]
pdf: ../../../A General Contact Force Analysis.pdf
confidence: high
source: pdf
aliases: []
---

# A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping

## 📌 年份
2016

## 🔑 论文识别码
DOI: 10.5772/62131

## 👥 作者与所属院校
- 作者：Xuan Vinh Ha, Cheolkeun Ha, Dang Khoa Nguyen
- 机构：韩国蔚山大学机械工程学院

## 📖 研究背景
- [[欠驱动手]]用少于自由度的驱动器配弹簧与机械限位，可被动适应不规则物体，无需复杂控制与传感。
- 但接触力分布决定抓取是否成立，欠驱动指在整指接触（full-phalanx）下的力分布长期缺少通用解析方法。
- 已有工作多针对特定机构（LARM Hand、BarrettHand 等），缺少 n 自由度的一般推导。

## ❓ 需要解决的问题
- 能否给出 n 自由度欠驱动指在全部指节接触时的[[接触力分配]]解析式？
- 当接触指节数少于 n 时方程如何退化，是否仍能唯一求解？
- ADAMS 虚拟样机的接触力与实测值是否吻合，能否替代 build-and-test？

## 📥📤 输入与输出
- 输入：指节几何与质量参数、弹簧刚度与机械限位、驱动器输入力矩（如 T1 = 1.5 N·m）。
- 输出：各指节接触力 F1、F2、F3 的幅值与分布，即[[欠驱动手指静力学]]的解。

## ✅ 论文最终达到的效果
- 建立了输入力矩→各指节接触力的映射，覆盖 full-phalanx 与少于 n 指节两类抓取情形。
- ADAMS 三自由度指模型算得 F1 = 10.1289 N、F2 = 5.7138 N、F3 = 7.8316 N，实测为 10.0779、5.6525、7.7661 N。
- 增大输入时远端指节力 F1 由 14.3496 升至 27.0532 N、F3 由 8.1763 升至 17.3404 N，与实测基本一致。
- 在给定参数与关节限位下，稳定的三指节抓取只占全部接触位形空间的约 32%。
- 虚拟样机显著缩短设计迭代，避免反复制造实物原型。

## 🔗 关联
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]
- [[A metric to design spring stiffness of underactuated fingers for stable grasp]]

## 🏷️ 标签
#欠驱动手指 #接触力分配 #静力学 #整指抓取 #虚拟样机
