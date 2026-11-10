---
title: Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration
year: 2021
doi: 10.3389/frobt.2021.703869
arxiv: 
key: KB-060
venue: "Frontiers in Robotics and AI, 8:703869"
theme: 02_文献库/01_灵巧手抓取规划
tags: [抓取稳定性预测, 触觉探索, 贝叶斯优化, 深度视觉, 未知物体]
pdf: ../../../Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration.pdf
confidence: high
source: pdf
aliases: []
---

# Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration

## 📌 年份
2021

## 🔑 论文识别码
DOI: 10.3389/frobt.2021.703869

## 👥 作者与所属院校
- 作者：Muhammad Sami Siddiqui、Claudio Coppola、Gokhan Solak、Lorenzo Jamone
- 机构：伦敦玛丽女王大学电子工程与计算机科学学院先进机器人中心（ARQ）

## 📖 研究背景
- 非结构化环境中的自主抓取需要判断未知物体能否被稳定抓起，视觉点云常有遮挡与建模误差。
- 即使有先验模型，实时局部探索仍是弥补建模误差的必要手段。
- 触觉探索可按抓取度量在线搜索更好的抓取，但要在有限观测次数内收敛。
- 本文切入：深度视觉给位姿、触觉探索给接触信息，用贝叶斯优化选择下一探索点，无任何物体先验。

## ❓ 需要解决的问题
- 在完全无先验时，能否用 RGB-D 位姿加触觉探索在线预测抓取稳定性，达到[[抓取稳定性预测]]可用精度？
- 标准贝叶斯优化（BO）与无迹贝叶斯优化（UBO）相比均匀网格搜索，收敛更快吗？
- 把传感噪声与执行误差纳入优化后，UBO 能否找到更安全的抓取？
- 探索得到的[[抓取质量]]度量峰值能否对应真实抬升稳定性？

## 📥📤 输入与输出
- 输入：Kinect RGB-D 点云与物体 6D 位姿、Allegro 指尖的 Optoforce [[指尖力传感器]]三维力、候选[[抓取位姿]]及其[[力封闭]]度量。
- 输出：下一探索点（手部位姿）、最优抓取位姿，以及稳定/部分稳定/失败的稳定性预测。

## ✅ 论文最终达到的效果
- 平台为 UR5 + Allegro 手 + 三指 Optoforce 力传感器，测试 3 个复杂形状物体（C 形管接头、芥末瓶、蓝色物体）。
- 每个物体 5 组实验、每组 20 次迭代（另有 50 观测点设置），比较 UNI/BO/UBO 三种探索。
- 抬升成功率：瓶 80/80/100%，管接头 60/100/100%，蓝色物体 66/60/80%。
- UBO 稳定性得分 96/90/80，BO 为 80/83.5/50，均匀搜索为 70/60/53。
- 所有实验均无物体从空中掉落；UBO 在少量观测内即收敛到度量峰值。

## 🔗 关联
- [[Grasp Prediction based on Local Finger Motion Dynamics]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#抓取稳定性预测 #触觉探索 #贝叶斯优化 #深度视觉 #未知物体
