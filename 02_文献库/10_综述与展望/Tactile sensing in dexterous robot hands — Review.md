---
title: Tactile sensing in dexterous robot hands — Review
year: 2015
doi: 10.1016/j.robot.2015.07.015
arxiv: 
key: KB-148
venue: Robotics and Autonomous Systems, Vol. 74, pp. 195–220
theme: 02_文献库/10_综述与展望
tags: [触觉传感, 灵巧手, 综述, 抓取稳定性, 触觉伺服]
pdf: ../../../Tactile sensing in dexterous robot hands — Review.pdf
confidence: high
source: pdf
aliases: []
---

# Tactile sensing in dexterous robot hands — Review

## 📌 年份
2015

## 🔑 论文识别码
DOI: 10.1016/j.robot.2015.07.015

## 👥 作者与所属院校
- 作者：Zhanat Kappassov, Juan-Antonio Corrales, Véronique Perdereau 等（3 人）
- 机构：巴黎第六大学智能系统与机器人研究所（ISIR）、法国克莱蒙费朗机械工程高等学院（IFMA）

## 📖 研究背景
- [[灵巧手]]自主操作（即[[手内操作]]）是工业与服务机器人的关键技能，依赖指尖接触处的力与表面属性信息。
- 已有触觉综述多只讲传感器硬件，缺少对"算法 + 触觉反馈控制"这一层的系统梳理。
- 制造需求从大批量两指夹爪转向小批量多品种，要求手具备更高适应性与操作能力。

## ❓ 需要解决的问题
- 已集成进机器人手的触觉传感器在换能原理上有哪几类，各自适配什么任务？
- 现有算法如何把触觉信号用于抓取稳定性估计、物体识别、[[触觉伺服]]与力控制？
- 压力分布、振动、温度等不同触觉数据在抓取与识别中的能力边界在哪里？

## 📥📤 输入与输出
- 输入：指尖触觉阵列的压力/振动/温度读数、传感单元在指面的空间布置、手部关节与接触状态。
- 输出：抓取稳定性判别、物体类别、触觉伺服修正量与期望抓取力。

## ✅ 论文最终达到的效果
- 按换能类型分类评述了 28 种集成于机器人手的触觉传感器，覆盖电阻、电容、光学、压电、磁性与气压式。
- 归纳触觉数据的四类应用：抓取稳定性估计、触觉物体识别、触觉伺服与力/位置控制。
- 以 Table 8 逐类对比各触觉数据在抓取稳定与物体识别中的优缺点（+/− 标注）。
- 指出趋势：由单一法向力测量转向多模态、可穿戴化，以及算法与硬件的协同设计。

## 🔗 关联
- [[A review of adaptive intelligence in tactile sensing robotic hands for human centered dexterous control]]
- [[A Review of Robotic Dexterous Hands]]
- [[A Review of Modeling of Soft-Contact Fingers and Stiffness Control for Dextrous Manipulation in Robotics]]

## 🏷️ 标签
#触觉传感 #灵巧手 #综述 #抓取稳定性 #触觉伺服
