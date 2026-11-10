---
title: A metric to design spring stiffness of underactuated fingers for stable grasp
year: 2018
doi: 10.1016/j.robot.2018.01.001
arxiv: 
key: KB-015
venue: "Robotics and Autonomous Systems, 102: 1–12"
theme: 02_文献库/04_绳驱机构与结构设计
tags: [欠驱动手指, 弹簧刚度, 抓取稳定域, 静力学, 机构设计]
pdf: ../../../A metric to design spring stiffness of underactuated fingers for stable.pdf
confidence: high
source: pdf
aliases: []
---

# A metric to design spring stiffness of underactuated fingers for stable grasp

## 📌 年份
2018

## 🔑 论文识别码
DOI: 10.1016/j.robot.2018.01.001

## 👥 作者与所属院校
- 作者：Jing Cui, Shaobo Yan, Jian Hu, ZhongYi Chu
- 机构：北京工业大学机械工程与应用电子技术学院、北京航空航天大学仪器科学与光电工程学院

## 📖 研究背景
- 在轨服务（空间站装配、卫星维修、加注）依赖机械臂末端执行器，其对不规则目标的适应能力决定任务等级。
- [[欠驱动手]]以被动弹簧替代部分执行器，靠机构自身柔顺包络物体，代价是抓取稳定性对弹簧刚度高度敏感。
- 刚度过小则稳定域收缩、抓取易失稳；刚度过大则退化为全驱动，适应性变差，缺乏定量设计依据。
- 既有设计多凭经验试凑弹簧参数，未给出刚度与稳定域之间的解析边界。

## ❓ 需要解决的问题
- 弹簧刚度 K 与稳定抓取域之间是否存在可解析表达的定量关系？
- 不同抓取拓扑（3 点、4 点、5 点接触）之间，稳定域如何随 K 变化并发生分岔？
- 给定输入力矩与物体半径，如何反解出最优刚度区间？

## 📥📤 输入与输出
- 输入：手指几何参数（近/远指节 L1、L2、掌宽 L0、初始角 γ0）、主动力矩 Ta、摩擦系数 μ、物体半径 r_obj、弹簧刚度 K。
- 输出：抓取状态平面（接触位置 e/L2 — 关节角 θ2）上的稳定域面积 S，以及使 S 最大的刚度取值区间。

## ✅ 论文最终达到的效果
- 提出以稳定域面积 S 为度量的刚度设计指标：平衡曲线与接触轨迹围成的闭区域，面积可由解析积分式算出。
- 给出刚度"分界线"（delimiter）与不同抓取拓扑之间的分岔点，把"太软—适中—太硬"三段区分开。
- Ta=1 N·m 时最优区间：4 点抓取 K≈2.5–3，3 点抓取 K≈1–1.25，5 点抓取 K≈0.81–1.09。
- Ta=1.5 N·m 时最优区间整体上移：4 点抓取 K≈3.5–4.5，3 点抓取 K≈3–3.5。
- 2 点抓取被判定为临界稳定而不讨论；以圆形参考物体与设计算例验证该指标可直接用于选型。

## 🔗 关联
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]

## 🏷️ 标签
#欠驱动手指 #弹簧刚度 #抓取稳定域 #静力学 #机构设计
