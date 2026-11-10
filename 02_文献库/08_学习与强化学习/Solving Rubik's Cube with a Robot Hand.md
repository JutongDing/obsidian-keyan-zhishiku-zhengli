---
title: Solving Rubik's Cube with a Robot Hand
year: 2019
doi: 
arxiv: 1910.07113
key: KB-136
venue: arXiv 预印本（2019-10-17）
theme: 02_文献库/08_学习与强化学习
tags: [仿真到现实迁移, 自动域随机化, 手内操作, 元学习, Shadow 灵巧手]
pdf: ../../../Solving Rubik's Cube with a Robot Hand.pdf
confidence: high
source: pdf
aliases: []
---

# Solving Rubik's Cube with a Robot Hand

## 📌 年份
2019（预印本标注 2019-10-17）

## 🔑 论文识别码
arXiv: 1910.07113（无 DOI）

## 👥 作者与所属院校
- 作者：OpenAI（Ilge Akkaya, Marcin Andrychowicz, Maciej Chociej, Mateusz Litwin 等，按字母序署名）
- 机构：OpenAI

## 📖 研究背景
- 只用仿真数据让真机完成极高复杂度操作，长期受「现实差距」制约。
- 魔方任务同时压测两件事：多指[[手内操作]]的接触控制，与立方体位置、朝向、面角的在线状态估计。
- 该文用自动域随机化（ADR）让随机化分布随训练自适应扩张，替代手工设定参数区间。

## ❓ 需要解决的问题
- 随机化范围如何自动扩张，使策略始终在训练分布边缘被挑战而不崩？
- 在 ADR 分布上训练的 LSTM 策略，是否会在测试时涌现元学习（在线快速适应）？
- 视觉状态估计器能否完全用仿真渲染图训练，再迁移到三路真实相机？
- 腱驱灵巧手硬件（线缆磨损、关节耦合）如何改造以支撑长期 RL 训练？

## 📥📤 输入与输出
- 输入：手指关节角与指尖位置（PhaseSpace 动捕）、三路 RGB 相机图像、魔方面角（视觉估计或 Giiker 智能魔方内置传感）。
- 输出：关节位置动作序列，涵盖翻转、面旋转等复合技能，直至魔方复原。

## ✅ 论文最终达到的效果
- Shadow 灵巧手 + 定制笼式平台；策略与视觉估计器全部在仿真训练，零真实数据。
- 积木重定向任务：ADR(XXL) 平均成功 32.0±6.4 次，基线仅 18.8±5.4 次。
- 魔方任务（Giiker+视觉）：ADR(XXL) 平均 26.8/50 次成功，每次翻转约 6.55 s、面旋转约 11.79 s。
- 仅靠视觉估计面角时降至 12.8/50，说明状态估计精度是主要瓶颈。
- LSTM 细胞状态可视化显示 4 组神经元对应「翻回掌心」等高层技能，佐证涌现的隐式元学习。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#仿真到现实迁移 #域随机化 #手内操作 #元学习 #LSTM策略
