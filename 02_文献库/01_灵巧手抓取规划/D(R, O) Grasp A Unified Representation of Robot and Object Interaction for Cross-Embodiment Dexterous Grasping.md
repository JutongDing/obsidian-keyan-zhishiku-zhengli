---
title: "D(R, O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping"
year: 2024
doi: 
arxiv: 
key: KB-034
venue: 待补（arXiv 预印本）
theme: 02_文献库/01_灵巧手抓取规划
tags: [跨本体抓取, 距离矩阵表示, 点云, 对比预训练, 灵巧抓取]
pdf: ../../../D(R,O)Grasp.pdf
confidence: medium
source: pdf
aliases: []
---

# D(R, O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping

## 📌 年份
2024

## 🔑 论文识别码
待补（低置信，待核对）：种子给出的 arXiv:2204.13998 实为正文参考文献，本文自身的 arXiv 号未在抽取文本中出现。

## 👥 作者与所属院校
- 作者：Zhenyu Wei, Zhixuan Xu, Jingxiang Guo, Yiwen Hou, Chongkai Gao 等
- 机构：新加坡国立大学计算机系、上海交通大学电子信息与电气工程学院与致远学院

## 📖 研究背景
- 机器人中心表示（如直接回归关节角）推理快，但样本效率低、换手即失效。
- 物体中心表示（接触点、接触图）泛化好，却常只建模指尖、需要完整物体几何。
- 手工设计 [[抓取质量]] 指标再逐例优化，速度慢，难以覆盖高自由度多指手的构型空间。
- 缺少一种同时编码「手在本抓取位姿下的构型」与「物体几何」的统一表示。

## ❓ 需要解决的问题
- 能否用一张手–物点对距离矩阵 D(R,O) 同时表达手结构与物体几何，实现跨本体 [[抓取规划]]？
- 如何预训练出对初始手构型不敏感的编码器，使同一模型适配 Barrett、Allegro、Shadow 等手？
- 在部分点云、未见物体与真机条件下，成功率、多样性与推理速度能否同时占优？

## 📥📤 输入与输出
- 输入：张开的手点云、物体点云（可为部分观测）、手描述（本体几何）。
- 输出：D(R,O) 距离矩阵，及其最小二乘反解出的手腕位姿与各指关节角（一组 [[抓取位姿]]）。

## ✅ 论文最终达到的效果
- 提出交互中心表示与构型不变的对比预训练，跨手迁移无需逐手重训。
- 仿真三种手（Barrett、Allegro、ShadowHand）成功率 87.30%/92.30%/83.00%，均值 87.53%；对比 GenDexGrasp 均值 57.40%。
- 抓取多样性 0.513/0.397/0.441 rad；单次推理 0.49/0.47/0.98 s，均不足 1 秒。
- 真机 LeapHand 对 10 个未见物体平均成功率 89%。
- 训练数据为 CMapDataset 子集，评测在 Isaac Gym 中进行。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#跨本体抓取 #距离矩阵表示 #点云 #对比预训练 #灵巧抓取
