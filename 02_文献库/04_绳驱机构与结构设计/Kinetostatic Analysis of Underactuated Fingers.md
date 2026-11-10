---
title: Kinetostatic Analysis of Underactuated Fingers
year: 2004
doi: 10.1109/TRA.2004.824641
arxiv: 
key: KB-080
venue: IEEE Transactions on Robotics and Automation
theme: 02_文献库/04_绳驱机构与结构设计
tags: [欠驱动手指, 静力学, 抓取稳定性, 机构设计, 力封闭]
pdf: ../../../Kinetostatic_analysis_of_underactuated_fingers.pdf
confidence: high
source: pdf
aliases: []
---

# Kinetostatic Analysis of Underactuated Fingers

## 📌 年份
2004

## 🔑 论文识别码
DOI: 10.1109/TRA.2004.824641

## 👥 作者与所属院校
- 作者：Lionel Birglen、Clément M. Gosselin
- 机构：拉瓦尔大学（Laval University）机械工程系，加拿大魁北克

## 📖 研究背景
- [[欠驱动手]]靠弹簧、机械限位等被动元件实现形状自适应，用少量驱动器换来自[[自适应抓取]]能力。
- 但这类手指的接触力分布被机构部分"写死"，样机多凭直觉与仿真设计，行为缺乏通用认识。
- 纯理论抓取研究与功能样机之间存在鸿沟，欠驱动情形尤其缺少可比较的分析工具。

## ❓ 需要解决的问题
- 任意 n 指节欠驱动手指的驱动力矩与各指节接触力之间，是否存在统一的解析关系？
- 在哪些接触构型下某些指节力会消失，甚至出现把物体"挤出"的不稳定现象？
- 如何用可计算的指标横向比较连杆、腱绳滑轮、齿轮等不同传动方案？

## 📥📤 输入与输出
- 输入：手指几何参数（连杆长度、关节角限位、弹簧刚度）、传动方式、驱动器力矩、接触指节数与接触点位置。
- 输出：各指节接触力分量、力为零的条件、稳定抓取构型集合（stability loci）及三个力能力指标。

## ✅ 论文最终达到的效果
- 为[[欠驱动手指静力学]]（kinetostatics）建立通用框架：引入[[雅可比矩阵]] J 与传动矩阵 T（transmission matrix），接触力可直接由驱动力矩与两矩阵的乘积解出（式 22）。
- 给出"挤出（ejection）"判据：驱动器持续闭合反把物体推离手掌，破坏抓取。
- 以典型参数计算，三指节稳定抓取仅占接触构型空间约 14%；放宽关节角限位后升至约 32%。
- 用三个指标比较四连杆、腱绳滑轮等方案；理论上指节越多越好，工程上以 3–4 指节为宜；摩擦与弹性等非数学因素仍可能否掉[[腱驱动]]方案。

## 🔗 关联
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]
- [[A metric to design spring stiffness of underactuated fingers for stable grasp]]
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]

## 🏷️ 标签
#欠驱动手指 #静力学 #抓取稳定性 #机构设计
