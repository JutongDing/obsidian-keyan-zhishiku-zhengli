---
title: Grip Stabilization through Independent Finger Tactile Feedback Control
year: 2020
doi: 10.3390/s20061748
arxiv: 1910.07113
key: KB-069
venue: Sensors
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移预测, 触觉反馈, 模块化控制, 随机森林, BioTac]
pdf: ../../../Grip Stabilization through Independent.pdf
confidence: high
source: pdf
aliases: [Grip Stabilization through Independent]
---

# Grip Stabilization through Independent Finger Tactile Feedback Control

## 📌 年份
2020（Sensors 第 20 卷第 6 期，1748）

## 🔑 论文识别码
DOI: 10.3390/s20061748

## 👥 作者与所属院校
- 作者：Filipe Veiga、Benoni Edin、Jan Peters（通讯）
- 机构：MIT CSAIL、于默奥大学综合医学生物学系、达姆施塔特工业大学、马普智能系统研究所

## 📖 研究背景
- [[手内操作]]长期被当作整体规划问题，需精确的手-物运动学、[[动力学建模]]与接触状态模型。
- 数据驱动方法需要大量样本、只适用相近场景，或依赖协同等低维表示，泛化受限。
- 该文提出仿生模块化方案：每根手指各自用触觉抑制局部滑移，不做中央协调。

## ❓ 需要解决的问题
- 各指完全独立、无中央通信时，多指手能否自发形成稳定抓取？
- 用随机森林从 BioTac 信号提前预测滑移，精度是否足以支撑力调节？
- 独立控制器能否抵抗外力扰动，并在四指与五指两种手型上通用？

## 📥📤 输入与输出
- 输入：每指 BioTac/BioTac SP 的 44 或 49 维触觉信号及一阶差分 Δx，历史窗 τH=1。
- 输出：滑移/接触/未接触三分类标签（提前 10 步、约 100 ms），折成手指任务空间速度指令以增减法向力。

## ✅ 论文最终达到的效果
- [[滑移检测]]改为滑移预测：分类器在滑移发生前 100 ms 给出标签，15 分钟内即可采完训练数据。
- 在 Allegro 四指手与 Wessling 五指手上验证，抓取构型覆盖 2–5 指。
- 12 种物体各 10 次稳定试验：卡片、橙方块、JELL-O 盒、Cheez-It 盒达 90–100%，香蕉 50%、苹果 60%。
- 外力反复扰动后能自行恢复抓取；[[主从遥操作]]实验显示可作分层控制的底层模块。

## 🔗 关联
- [[Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization]]
- [[Force Estimation and Slip Detection for Grip Control using a Biomimetic Tactile Sensor]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#滑移预测 #触觉反馈 #模块化控制 #随机森林
