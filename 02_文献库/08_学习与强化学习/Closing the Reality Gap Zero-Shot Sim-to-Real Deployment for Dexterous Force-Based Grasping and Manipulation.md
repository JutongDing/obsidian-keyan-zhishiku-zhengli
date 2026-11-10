---
title: "Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation"
year: 2026
doi: 
arxiv: 2601.02778
key: KB-028
venue: 待补（arXiv 预印本，ByteDance Seed）
theme: 02_文献库/08_学习与强化学习
tags: [仿真到现实, 触觉仿真, 力控抓取, 手内旋转, PPO]
pdf: ../../../Closing the Reality Gap.pdf
confidence: high
source: pdf
aliases: []
---

# Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2601.02778

## 👥 作者与所属院校
- 作者：Haoyu Dong, Zhibin Li, Zhe Zhao, Zhengmao He, Yang Li 等（完整作者表见文末 Contributions）
- 机构：字节跳动 Seed（ByteDance Seed）

## 📖 研究背景
- 多指 [[灵巧手]] 具备接近人的操作潜力，但接触物理复杂、执行器不理想，训练出的策略难以直接上真机。
- 腿足机器人已靠 [[域随机化]]、执行器建模与 [[仿真到现实迁移]] 打通 sim-to-real，操作领域仍缺可复现的配方。
- 现有方法常把接触简化为刚体、忽略齿隙与力矩–转速饱和，触觉信号也难以高频率生成。

## ❓ 需要解决的问题
- 如何在仿真中以可接受算力生成高频高分辨的稠密触觉信号，供 [[强化学习]] 训练直接使用？
- 没有关节力矩传感器时，能否用电机电流标定出可信的力矩观测？
- 传感与执行两侧都建模后，策略能否零样本完成力控抓取与手内重定向？

## 📥📤 输入与输出
- 输入：12 自由度五指手关节位置、电流换算的关节力矩、虚拟触觉单元的接触力与接触中心、物体 6D 姿态、目标抓取力指令。
- 输出：12 维目标关节位置（交电机级 PD 执行），体现为抓取力大小与 [[手内操作]] 的旋转动作。

## ✅ 论文最终达到的效果
- 纯仿真训练的 PPO（非对称 actor–critic）策略零样本部署到 xHand，真机无微调。
- 指端触觉仿真用并行正运动学算虚拟触觉单元到物体的距离，省去稠密碰撞计算。
- 力指令 0–2 区间内接触力与关节力矩近似线性跟随，实现 [[抓取力跟踪]]。
- 手内旋转真机消融（各 10 次）：完整观测平均连续成功 25.1 次、单次 3.36 s、失效前 84.3 s；去掉触觉感知仅 1.1 次；用四元数替 6D 旋转表示降到 2.9 次。
- 力奖励与力矩奖励缺一不可：只用 RForce 接触力偏小，只用 Rtorque 力矩传不到指尖。

## 🔗 关联
- [[D3Grasp Diverse and Deformable Dexterous Grasping for General Objects]]
- [[Learning Dexterous In-Hand Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#仿真到现实 #触觉仿真 #力控抓取 #手内旋转 #PPO
