---
title: Robust Dexterous Grasping of General Objects
year: 2025
doi: 
arxiv: 2504.05287
key: KB-124
venue: arXiv 预印本（cs.RO，v3 2025-08；会议/期刊待补）
theme: 02_文献库/08_学习与强化学习
tags: [灵巧抓取, 强化学习, 教师学生蒸馏, 单视角点云, 鲁棒性]
pdf: ../../../Robust Dexterous Grasping of General Objects.pdf
confidence: high
source: pdf
aliases: []
---

# Robust Dexterous Grasping of General Objects

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2504.05287

## 👥 作者与所属院校
- 作者：Hui Zhang, Zijian Wu, Linyi Huang, Sammy Christen, Jie Song 等
- 机构：苏黎世联邦理工学院（ETH Zurich）、香港科技大学（广州）、香港科技大学

## 📖 研究背景
- [[灵巧手]]抓取研究多依赖预先扫描的物体、人类到机器人的示教迁移，或执行预测出的静态抓取位姿。
- 上述做法难以部署到新物体；静态位姿执行缺乏在线调整能力，遇到碰撞或扰动即失效。
- 该文用"以手为中心"的局部形状表征加特权教师策略蒸馏，学习零样本动态抓取。

## ❓ 需要解决的问题
- 仅凭单视角点云，策略能否泛化到从未见过的物体？
- 在外部碰撞、观测噪声、执行器误差下，能否实时补偿并保持抓取？
- 只编码接触区域附近的局部形状，是否比重建全局几何更抗形状变化与感知不确定？

## 📥📤 输入与输出
- 输入：单视角物体点云、含噪关节状态与手部本体感知（学生策略不使用触觉，教师策略用全观测点云与接触/冲量）。
- 输出：腕部 6 维运动与 Allegro 手 16 维关节目标；高层 5 Hz，底层 PD 100 Hz。

## ✅ 论文最终达到的效果
- 仿真 247,786 个物体成功率 97.0%；真实世界 512 个物体成功率 94.6%（UR5 + Allegro 手）。
- 细小物体受手尺寸限制（直径 < 1.5 cm）仍达 0.949；仅用单视角深度即可工作。
- 混合课程（先[[模仿学习]]蒸馏教师、后[[强化学习]]探索）显著提升抗扰性；去掉 IL 损失成功率仅略降。
- 训练中加入观测噪声与动力学[[域随机化]]，可在意外碰撞、粗糙观测与持续外力下维持抓取。
- 定位为鲁棒低层抓取控制器，为下游操作任务提供基础。

## 🔗 关联
- [[FunGrasp Functional Grasping for Diverse Dexterous Hands]]
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#灵巧抓取 #强化学习 #教师学生蒸馏 #单视角点云 #鲁棒性
