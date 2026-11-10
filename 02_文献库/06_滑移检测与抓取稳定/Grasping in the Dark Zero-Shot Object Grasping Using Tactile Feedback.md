---
title: Grasping in the Dark: Zero-Shot Object Grasping Using Tactile Feedback
year: 2021
doi: arXiv:2011.00712
arxiv: 2011.00712
key: KB-067
venue: arXiv 预印本（cs.RO，2021-09-16 v2；正式发表信息待核对）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [零样本抓取, 滑移检测, 触觉反馈, Shadow手, BioTac]
pdf: ../../../Grasping in the Dark.pdf
confidence: medium
source: pdf
aliases: [Grasping in the Dark]
---

# Grasping in the Dark: Zero-Shot Object Grasping Using Tactile Feedback

## 📌 年份
2021（arXiv v2，2021-09-16）

## 🔑 论文识别码
arXiv: 2011.00712（种子所记 DOI 10.1038/s41598-018-38277-w 与本文不符，低置信，待核对）

## 👥 作者与所属院校
- 作者：Kanishka Ganguly、Behzad Sadrfaridpour、Pavan Mantripragada、Nitin J. Sanket 等
- 机构：马里兰大学帕克分校（UMIACS / 计算机科学系）、美国陆军研究实验室（待核对）

## 📖 研究背景
- 家庭机器人要抓从未见过的物体，多数末端设计依赖物体模型或外部视觉估计形状与尺寸。
- 人类闭着眼睛也能抓，靠的是皮肤触觉对滑落的快速反应。
- 该文只用触觉与关节角，实现零样本（zero-shot）物体抓取。

## ❓ 需要解决的问题
- 无形状、尺寸、质量先验时，能否仅凭触觉判断物体正在滑落、滑得多快？
- 如何把滑移速度转成手指与手臂的运动指令，做到即滑即补？
- 对透明物体（相机与激光雷达难以稳定感知）能否同样抓稳？

## 📥📤 输入与输出
- 输入：Shadow 手五指 BioTac SP 触觉读数、近节 FSR 接触信号、手指关节角与 UR-10 末端位姿。
- 输出：J1/J2/J3 关节增量与手臂抬升速度（滑得越快增量越大），以及抓取终止判据。

## ✅ 论文最终达到的效果
- [[滑移检测]]用 100 ms 非重叠窗口内触觉信号的回归斜率变化，比较相邻窗判断滑移快慢。
- 10 类物体总体成功率 73.5%：瓶子与电子盒 85%、透明酒杯 80%、番茄与 Jell-O 盒 70%、足球 60%。
- 成功判据为抓牢后悬持 10 s；撤掉两指接触后仍能维持抓取，说明控制器可在线适应接触数。
- 与视觉方法（87.8%）、强化学习方法（98.0%）相比精度相当，但可抓透明酒杯。

## 🔗 关联
- [[Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization]]
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#零样本抓取 #滑移检测 #触觉反馈 #Shadow手
