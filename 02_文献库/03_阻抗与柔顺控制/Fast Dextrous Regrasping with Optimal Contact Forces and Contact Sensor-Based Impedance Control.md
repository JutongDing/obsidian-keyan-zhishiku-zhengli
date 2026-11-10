---
title: Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control
year: 2001
doi: 
arxiv: 
key: KB-048
venue: Proceedings of the 2001 IEEE International Conference on Robotics & Automation (ICRA), Seoul, 103-108
theme: 02_文献库/03_阻抗与柔顺控制
tags: [抓取力优化, 阻抗控制, 重抓, 力传感器, 多指手]
pdf: ../../../Fast dextrous re-grasping with optimal contact forces and contact sensor-based impedance control.pdf
confidence: high
source: pdf
aliases: []
---

# Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control

## 📌 年份
2001（ICRA 2001，Seoul，5 月 21–26 日）

## 🔑 论文识别码
ICRA 2001 会议论文（无数值 DOI；本地编号 KB-048）

## 👥 作者与所属院校
- 作者：Thomas Schlegl, Martin Buss, Toru Omata, Gunther Schmidt
- 机构：慕尼黑工业大学自动控制工程研究所、柏林工业大学控制系统教研室、东京工业大学精密机械系统系

## 📖 研究背景
- 多指手重抓（regrasping）任务执行慢，瓶颈在抓取力规划的计算量，而非机械速度。
- 操作中物体位姿变化、手指数变化使[[抓取矩阵]]时变，接触力必须在线重算。
- 规划须同时满足外力平衡与接触点单边摩擦约束，而该问题无闭式解。

## ❓ 需要解决的问题
- 能否用 6 维指尖力传感器在线辨识抓取矩阵与未知外力，使[[抓取力优化]]的【待建名词：半定规划】可实时求解？
- 优化得到的接触力如何经指尖[[阻抗控制]]施加，并同时跟踪期望指尖位置？
- 重抓速度与抗扰能力能否同时提升，而不牺牲抓取稳定？

## 📥📤 输入与输出
- 输入：各指尖 6 维力/力矩传感器数据、当前指尖位置、期望指尖位置、物体外力估计。
- 输出：最优接触力（含[[内力]]与[[接触力分配]]）、指尖阻抗控制指令、关节位置/力指令。

## ✅ 论文最终达到的效果
- 实时抓取力优化单次求解约 4 ms，可随抓取结构变化在线更新。
- 借助传感器信息补偿外部扰动力，实验中承受接近 8 倍常规幅值的扰动仍保持稳定。
- 在 TIT 三指手上完成灯泡对孔并旋入灯座的连续重抓，扰动下指尖位移约 1.5 cm 后恢复。
- 结论为重抓与操作速度提升、鲁棒性增强（以定性对比为主）。

## 🔗 关联
- [[多指灵巧手动力学建模与柔顺控制技术研究]]
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]

## 🏷️ 标签
#抓取力优化 #阻抗控制 #重抓 #多指手
