---
title: Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands
year: 2022
doi: 10.1109/LRA.2022.3187497
arxiv: 
key: KB-110
venue: IEEE Robotics and Automation Letters, 7(4), 8566-8573, Oct. 2022
theme: 02_文献库/07_装配与操作任务
tags: [轴孔装配, 双臂协同, 灵巧手, 手内操作, 力位混合控制]
pdf: ../../../Peg-in-Hole Assembly With Dual-Arm Robotand Dexterous Robot Hands.pdf
confidence: high
source: pdf
aliases: [Peg-in-Hole Assembly With Dual-Arm Robotand Dexterous Robot Hands]
---

# Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands

## 📌 年份
2022

## 🔑 论文识别码
DOI: 10.1109/LRA.2022.3187497

## 👥 作者与所属院校
- 作者：Dong-Hyuk Lee, Myoung-Su Choi, Hyeonjun Park, Ga-Ram Jang, Jae-Han Park 等
- 机构：韩国生产技术研究院（KITECH）机器人研发部、科学技术联合大学院（UST）、ROBROS 公司

## 📖 研究背景
- 传统[[轴孔装配]]研究多把工件固定在机械臂上或用简单夹爪，规避了手的不确定性，适用面窄。
- [[灵巧手]]通用性强但不为特定任务优化，用其完成装配全流程的研究极少，臂–手协同未被充分研究。
- 人手装配靠指尖力觉与微小试探动作完成，机器实现需要柔顺行为与力控策略支撑。

## ❓ 需要解决的问题
- 灵巧手如何在未知工件形状下"盲抓"并保持力与力矩平衡？
- 如何通过[[手内操作]]旋转工件对准钥匙孔方向而不失稳？
- 接近–搜索–对准–插入四阶段能否由统一的扰动模式（perturbation pattern）组合实现？

## 📥📤 输入与输出
- 输入：各指关节角与力矩（推算指尖力）、双臂末端位姿、工件与孔位姿、用户设定的合力 fgrasp 与扰动旋量。
- 输出：各指尖期望力、手指关节力矩、双臂末端位置/力控指令、装配阶段切换。

## ✅ 论文最终达到的效果
- 以 50 自由度人形上半身（双臂+腕+灵巧手）完成钥匙孔形工件的全流程装配演示。
- 100 次重复实验：总成功率 87%，总平均装配时间 13.86 s。
- 四阶段完整场景（Case 1）平均 19.42 s；跳过搜索与对准的 Case 4 仅 3.37 s。
- Case 2（接近–搜索–插入）最常出现（41 次成功），Case 3 最罕见（5 次）。
- 采用前馈任务空间力控 + 低增益位置调节实现柔顺插入；阶段切换仍由人工判据触发，全自主切换列为后续工作。

## 🔗 关联
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]
- [[Active Touch Sensing for Robust Hole Detection in Assembly Tasks]]
- [[Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand]]

## 🏷️ 标签
#轴孔装配 #双臂协同 #灵巧手 #手内操作 #力位混合控制
