---
title: Geometric design optimization of an under-actuated tendon-driven robotic gripper
year: 2018
doi: 10.1016/j.rcim.2017.09.012
arxiv: 
key: KB-057
venue: Robotics and Computer-Integrated Manufacturing, 50 (2018) 80-89
theme: 02_文献库/04_绳驱机构与结构设计
tags: [欠驱动, 腱驱动, 机构设计优化, 遗传算法, 抓取稳定性]
pdf: ../../../Geometric design optimization of an under-actuated tendon-driven robotic gripper.pdf
confidence: high
source: pdf
aliases: []
---

# Geometric design optimization of an under-actuated tendon-driven robotic gripper

## 📌 年份
2018

## 🔑 论文识别码
DOI: 10.1016/j.rcim.2017.09.012

## 👥 作者与所属院校
- 作者：Huixu Dong, Ehsan Asadi, Chen Qiu, Jiansheng Dai, I-Ming Chen
- 机构：南洋理工大学 机器人研究中心、伦敦国王学院 机器人研究中心

## 📖 研究背景
- 通用抓取要求夹爪在非结构化环境中稳定作业，但高成本高复杂度设计难以产品化。
- 双指单驱动[[欠驱动手]]配[[腱驱动]]传动（TDM）结构简单、成本低，是工业主流方案。
- 欠驱动手指各关节被同一主动腱耦合，接触力比例运行中不可调；设计不当会顶飞工件或出现回弹（roll-back）。

## ❓ 需要解决的问题
- 如何建立主动力到各接触力的解析映射，使 22 个几何设计变量与抓取稳定性可量化关联？
- 6 个滑轮、12 个路由变量决定的腱绳路径如何影响传动效率与阻力？
- 在几何约束下，遗传算法能否求出稳定抓取的尺寸最优解并经受实物验证？

## 📥📤 输入与输出
- 输入：三节指骨长/宽、三关节卷筒半径、掌宽、6 个滑轮的路由位置与包角、摩擦与主动力 Fa。
- 输出：22 维最优几何参数、传动比与传动效率、抓取稳定性判据与适应度值。

## ✅ 论文最终达到的效果
- 建立 22 变量优化模型（3 指骨长、3 指骨宽、3 关节卷筒半径、掌宽、12 路由变量），3 个目标函数合成 2 个适应度模型。
- 遗传算法 100 代收敛，取 72 次优化均值：L1=54.8、L2=33.8、L3=25.2 mm，2r1=15.7、2r2=7.7、2r3=16.4 mm。
- 最优适应度为 1.57083，多次运行均值同值（收敛稳定）。
- 样机可稳定抓取 102 mm 杯子至 8 mm 笔的尺寸跨度。
- 方法对常规欠驱动腱驱动夹爪具有通用性。

## 🔗 关联
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]
- [[A metric to design spring stiffness of underactuated fingers for stable grasp]]

## 🏷️ 标签
#欠驱动 #腱驱动 #结构优化 #遗传算法 #抓取稳定性
