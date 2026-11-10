---
title: Active Touch Sensing for Robust Hole Detection in Assembly Tasks
year: 2025
doi: 10.3390/s25154567
arxiv: 
key: KB-021
venue: Sensors (MDPI)
theme: 02_文献库/07_装配与操作任务
tags: [主动触觉, 孔定位, 概率搜索, 插孔装配]
pdf: ../../../Active Touch Sensing for Robust Hole Detection in Assembly Tasks.pdf
confidence: high
source: pdf
aliases: []
---

# Active Touch Sensing for Robust Hole Detection in Assembly Tasks

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.3390/s25154567

## 👥 作者与所属院校
- 作者：Bojan Nemec、Mihael Simonič、Aleš Ude
- 机构：Jožef Stefan Institute（人形与认知机器人实验室，斯洛文尼亚）

## 📖 研究背景
- 双目/结构光相机在遮挡、弱光、相机位姿不佳时失效，手眼标定误差对小间隙装配尤其致命。
- 力与触觉信号远不如视觉丰富，仅靠稀疏接触点做[[轴孔装配]]中的孔口定位缺少系统方法。
- 常见螺旋搜索、启发式搜索需人工整定参数，且不利用目标物体的先验几何。
- 本文切入角度：以先验 3D 地图为假设空间，用稀疏触觉点击做主动假设检验，并给出确定性/概率两版算法。

## ❓ 需要解决的问题
- 仅用触点是否接触这类二值稀疏反馈，如何把孔口中心定位到足以插入的精度？
- 面向多层平行表面（不同高度）的常见装配件，如何同时搜索位置与高度？
- 传感器噪声与 3D 地图误差下，如何避免定位失败并保持收敛？
- 与随机搜索、螺旋搜索相比，收敛速度与成功率能否量化占优？

## 📥📤 输入与输出
- 输入：目标物体的先验 3D 地图（含高度离散化 δh）、末端触觉接触信号与接触区域、当前末端位姿、插入容差 ε。
- 输出：孔口中心位姿假设集与下一次探测命令位置，直至[[接触状态识别]]判定进入目标区域并完成插入的终止信号。

## ✅ 论文最终达到的效果
- 100 次音频插头试验：随机搜索基线平均 37.37 次尝试、71.0 s；确定性算法 5.83 次、11.1 s，成功率 100%。
- 加入高度估计后 6.37 次、12.1 s，仍 100%；有噪声时确定性版降至 85%，概率版恢复 100%（6.76 次、12.8 s）。
- Task Board 探针：4.07 次、8.7 s、100%；顶部带孔圆锥：3.78 次（标准差 0.84）、7.9 s、100%。
- 组合式（螺旋＋地图配准）搜索：20 次试验全部成功，平均 7.8 s，对参数不敏感。
- 反直觉结论：几何越复杂收敛越快，因为接触签名更丰富、错误假设被更快剔除；算法满足搜索区域单调收缩的收敛性证明。

## 🔗 关联
- [[Peg-in-Hole Assembly With Dual-Arm Robot and Dexterous Robot Hands]]
- [[3D tactile servo control a peg-in-hole strategy for hole with dynamic random motion]]
- [[Comparative Peg-in-Hole Testing of a Force-Based Manipulation Controlled Robotic Hand]]

## 🏷️ 标签
#主动触觉 #轴孔装配 #概率搜索 #触觉定位
