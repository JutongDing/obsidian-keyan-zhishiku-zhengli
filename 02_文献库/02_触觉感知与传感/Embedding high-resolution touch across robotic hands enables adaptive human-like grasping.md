---
title: Embedding high-resolution touch across robotic hands enables adaptive human-like grasping
year: 2025
doi: 10.1038/s42256-025-01053-3
arxiv: 
key: KB-044
venue: Nature Machine Intelligence
theme: 02_文献库/02_触觉感知与传感
tags: [全手触觉覆盖, 高分辨率触觉, 仿生手, 类人抓取]
pdf: ../../../Embedding high-resolution touch across .pdf
confidence: high
source: pdf
aliases: [F-TAC Hand]
---

# Embedding high-resolution touch across robotic hands enables adaptive human-like grasping

## 📌 年份
2025

## 🔑 论文识别码
DOI: 10.1038/s42256-025-01053-3

## 👥 作者与所属院校
- 作者：Zihang Zhao, Wanlin Li, Yuyang Li, Tengyu Liu, Boren Li 等（前四位共同一作）
- 机构：北京大学人工智能研究院、北京通用人工智能研究院（BIGAI）、PKU–武汉人工智能研究院、北京大学工学院、伦敦玛丽女王大学工程与材料科学学院

## 📖 研究背景
- 灵巧手运动学与机电设计已接近人手，但触觉反馈不足，使其在动态真实环境中仍难与人类相比。
- 高分辨率 [[触觉传感器]] 多集中在指尖小块区域，难以覆盖整手曲面，且嵌入后常牺牲关节运动范围。
- 该文提出 F-TAC Hand，以 0.1 mm 分辨率触觉覆盖手表面 70%，并配套生成式类人手构型算法与抓取策略。

## ❓ 需要解决的问题
- 如何在大面积手表面嵌入高分辨率触觉，同时保持完整运动范围与可制造性？
- 如何利用高维全手触觉生成类人抓取构型，并在动态扰动下保持稳定？
- 有触觉与无触觉方案在复杂操作任务上的差异是否统计显著？
- 方法能否泛化到不同拓扑的手（两指、三指、四指、拟人五指）？

## 📥📤 输入与输出
- 输入：全手高分辨率触觉点阵（接触位置与压力分布）、关节本体感知、物体与任务信息、单视角或已知物体位姿。
- 输出：类人抓取手构型（生成式算法给出关节角）、抓取与操作动作序列、多物体搬运的两阶段策略。

## ✅ 论文最终达到的效果
- 触觉空间分辨率 0.1 mm，覆盖手表面 70% 面积，同时保留完整运动范围。
- 600 次真实世界试验表明，触觉版在复杂操作任务上显著优于无触觉方案（P < 0.0001）。
- 生成式算法仅需单样本即可合成类人手构型，并泛化到 EZGripper、Barrett、Allegro、Shadow 等不同手型。
- 部分手指被禁用时仍能稳定抓取，表现出类似人类的代偿能力。
- 完成多物体连续搬运与动态扰动下的 [[自适应抓取]]，验证全手触觉对智能行为的支撑作用。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#全手触觉 #高分辨率触觉 #仿生手 #类人抓取
