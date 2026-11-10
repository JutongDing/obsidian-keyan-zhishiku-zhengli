---
title: "An overview of learning-based dexterous grasping: recent advances and future directions"
year: 2025
doi: 10.1007/s10462-025-11262-2
arxiv: 
key: KB-024
venue: Artificial Intelligence Review
theme: 02_文献库/10_综述与展望
tags: [综述, 学习式抓取, 抓取生成, 抓取执行]
pdf: ../../../An overview of learning-based dexterous grasping.pdf
confidence: high
source: pdf
aliases: []
---

# An overview of learning-based dexterous grasping: recent advances and future directions

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.1007/s10462-025-11262-2

## 👥 作者与所属院校
- 作者：Xu Song、Yongyao Li、Yunfan Zhang、Yufei Liu、Lei Jiang
- 机构：人形机器人（上海）创新中心、中国北方车辆研究所、上海理工大学

## 📖 研究背景
- 具身智能与人形机器人推动[[灵巧手]]抓取成为机器人学与人工智能的研究热点。
- 与 7 自由度平行夹爪不同，五指手通常超 20 自由度，更贴近人手的结构与运动。
- 学习式方法进展分散在生成、规划、控制多个子方向，研究者难以快速把握全貌。
- 本文切入角度：以「抓取生成（Grasp Generation, GG）」与「抓取执行（Grasp Execution, GE）」两条主线组织近年文献。

## ❓ 需要解决的问题
- 学习式方法如何统一刻画[[抓取位姿]]生成与后续执行两阶段的分工与耦合？
- 现有基准数据集与评价指标能否公平比较不同方法的成功率与[[抓取质量]]？
- 仿真训练的[[强化学习]]、[[模仿学习]]策略在真实五指手上失败的主要成因是什么？
- 从实验室走向工业制造、家庭服务、医疗康复，还缺哪些关键能力？

## 📥📤 输入与输出
- 输入：综述的对象是文献、数据集（如 DexYCB、GRAB、ContactPose、ARCTIC 等）与评测协议。
- 输出：GG/GE 二维分类框架、方法对比表、基准与指标梳理，以及未来研究方向的判断。

## ✅ 论文最终达到的效果
- 建立「生成—执行」两视角综述框架：GG 负责为目标物体生成合适的抓取位姿，GE 通过运动规划与运动控制落实该位姿。
- 系统梳理近期基准数据集与评价指标，并据此对代表性方法做横向对比分析。
- 指出面向[[手内操作]]、接触丰富任务时，[[仿真到现实迁移]]仍是主要瓶颈。
- 归纳出需重点攻克的若干方向，覆盖工业制造、家庭服务、医疗康复等落地场景。
- 该综述不产生新实验数据，结论以趋势判断与分类对照为主。

## 🔗 关联
- [[A Review of Modeling of Soft-Contact Fingers and Stiffness Control for Dextrous Manipulation in Robotics]]
- [[A Review of Robotic Dexterous Hands]]
- [[A comprehensive review of dexterous robotic hands design, implementation, and evaluation]]

## 🏷️ 标签
#综述 #学习式抓取 #抓取生成 #抓取执行
