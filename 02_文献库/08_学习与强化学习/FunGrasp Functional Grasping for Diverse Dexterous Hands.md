---
title: "FunGrasp: Functional Grasping for Diverse Dexterous Hands"
year: 2024
doi: 
arxiv: 2411.16755
key: KB-054
venue: arXiv 预印本（cs.RO）
theme: 02_文献库/08_学习与强化学习
tags: [功能性抓取, 重定向, 强化学习, 仿真到现实迁移, 跨手型]
pdf: ../../../FunGrasp.pdf
confidence: high
source: pdf
aliases: [FunGrasp]
---

# FunGrasp: Functional Grasping for Diverse Dexterous Hands

## 📌 年份
2024

## 🔑 论文识别码
arXiv:2411.16755（预印本，无 DOI）

## 👥 作者与所属院校
- 作者：Linyi Huang、Hui Zhang、Zijian Wu、Sammy Christen、Jie Song 等
- 机构：ETH Zürich、苏黎世大学（待核对具体院系）

## 📖 研究背景
- 人类按任务选择抓法：握剪刀的指孔以裁剪、握刀柄以便安全递出；机器人缺少这种任务相关的功能抓取。
- 现有[[灵巧手]]抓取研究偏重 power grasp，忽略任务与物体特定的功能性[[抓取位姿]]。
- 人手抓取数据丰富，但跨手型（自由度、指数不同）重定向困难；手指电机功率与精度受限，仿真到真机差距大。
- 本文切入：单张人手抓取 RGBD 图像 → 估计手姿态 → 人到手（H2R）重定向 → 仿真中用[[强化学习]]训练动态抓取策略。

## ❓ 需要解决的问题
- 单张 RGBD 人手抓取图像能否给出可直接用于机器人重定向的手部姿态与物体位姿？
- 同一功能抓取如何映射到自由度、指数各异的多种灵巧手上而不破坏接触与人类姿态相似性？
- 在关节力矩受限、接触模型不精确时，策略能否稳定完成动态抓取并零样本迁移真机？
- 重定向模块、特权信息与特权学习、系统辨识与重力补偿各自贡献多大？

## 📥📤 输入与输出
- 输入：单张人手抓取 RGBD 图像（含物体 6D 位姿与速度）、机器人本体状态（关节角、腕部位姿）、特权信息（接触力、物体速度）。
- 输出：各手关节目标动作序列（PD 跟踪、含重力补偿力矩），完成抬升高度 >0.1 m 的功能抓取。

## ✅ 论文最终达到的效果
- 真机 Allegro 上对训练集外物体（25% DexYCB 测试划分）一次性迁移，平均成功率 74%。
- 仿真跨手型一致达 75% 以上：Allegro 85%、Faive 81%、Shadow 75%。
- 消融：用 DexGraspNet 初始化替代重定向降至 65%，角度重置 62%；去特权信息 61%，去特权学习 40%。
- 逐步加入系统辨识与重力补偿后，真机成功率由 38% 升到 59%、75%。
- 可抓取可变形环状玩偶等物理特性与训练集差异很大的物体，验证泛化性。

## 🔗 关联
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]
- [[Dexonomy Synthesizing All Dexterous Grasp Types in a Grasp Taxonomy]]
- [[Learning Dexterous In-Hand Manipulation]]

## 🏷️ 标签
#功能性抓取 #重定向 #强化学习 #仿真到现实迁移 #跨手型
