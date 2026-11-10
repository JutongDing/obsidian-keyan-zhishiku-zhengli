---
title: "TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses"
year: 2025
doi: 
arxiv: 2509.25746
key: KB-144
venue: arXiv preprint (cs.RO)（正文自称 letter，发表信息待核对）
theme: 02_文献库/08_学习与强化学习
tags: [抓取位姿细化, 触觉反馈, 仿真到现实迁移, 灵巧手]
pdf: ../../../TacRefineNet.pdf
confidence: high
source: pdf
aliases: []
---

# TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2509.25746（无 DOI）

## 👥 作者与所属院校
- 作者：Shuaijun Wang, Haoran Zhou, Diyun Xiang, Yangwei You
- 机构：小米机器人（Xiaomi Robotics）

## 📖 研究背景
- 传统抓取流水线与 VLA 方法在长程任务中，抓取执行阶段的位姿误差会累积，影响最终成功率。
- 视觉在接触后易被遮挡、难分辨毫米级偏差，而人手主要靠指尖触觉完成最后的位姿微调。
- 该文聚焦“最后一公里”，只用多指指尖触觉，把已知物体从任意手中位姿调整到任意目标位姿。

## ❓ 需要解决的问题
- 仅有指尖触觉与本体感觉，能否估计末端 6 自由度位姿修正量并迭代收敛？
- 如何把用户示教的目标触觉图像作为一次性的目标条件，支持任意初始/目标位姿组合？
- 物理触觉仿真能否生成足够保真的数据，使仿真预训练加少量真机数据优于纯仿真？
- 多指触觉与本体感觉怎样融合，才能在任意手中位姿下都保持毫米级精度？

## 📥📤 输入与输出
- 输入：各指尖 11×9 taxel 触觉图像（间距约 1.1 mm）、目标触觉图像、当前关节角与腕部位姿。
- 输出：腕部 6 自由度位姿增量，手重新张开—移动—再抓，形成迭代 [[抓取位姿]] 细化闭环。

## ✅ 论文最终达到的效果
- 策略 B 在 10 步调整内位置误差由 8.9 mm 降到 1.1 mm，姿态误差 0.044 rad 降到 0.016 rad。
- 三组初始/目标组合成功率分别由 80%、40%、100% 提升到 100%、100%、100%。
- 16 组任意手中位姿组合各重复 5 次，均达毫米级，姿态误差稳定低于 0.1 rad。
- 仿真预训练加少量真机数据明显优于纯仿真训练；触觉传感器由弹性接触点在 MuJoCo 中建模。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#抓取位姿细化 #触觉反馈 #仿真到现实迁移 #灵巧手
