---
title: Humanoid Five-Digit Robotic Grasping via Multi-Agent Reinforcement Learning With Potential-Guided Optimization and Weight Scheduling
year: 2026
doi: 10.1109/TASE.2026.3672621
arxiv: 
key: KB-074
venue: IEEE Transactions on Automation Science and Engineering（Vol.23）
theme: 02_文献库/08_学习与强化学习
tags: [多智能体强化学习, 示教学习, 运动基元, 五指手, 仿真到现实迁移]
pdf: ../../../Humanoid Five-Digit Robotic Grasping via Multi-Agent Reinforcement Learning With Potential-Guided Optimization and Weight Scheduling.pdf
confidence: high
source: pdf
aliases: []
---

# Humanoid Five-Digit Robotic Grasping via Multi-Agent Reinforcement Learning With Potential-Guided Optimization and Weight Scheduling

## 📌 年份
2026（T-ASE 第 23 卷；2026-03-10 在线）

## 🔑 论文识别码
DOI: 10.1109/TASE.2026.3672621

## 👥 作者与所属院校
- 作者：Jiashuai Wang, Ke Li, Xiaoyu Wang, Guanglin Li, Zong-Ming Li 等
- 机构：山东大学控制科学与工程学院智能医学工程中心、中科院深圳先进技术研究院、亚利桑那大学、山东大学齐鲁医院

## 📖 研究背景
- 示教学习（[[模仿学习]]）对每类物体单独训练轨迹，跨物体泛化差，难适应未知物体。
- 单智能体[[强化学习]]用一个策略生成五指动作，难刻画拇指与手指的异步异构关节运动。
- DDPG 类方法探索效率低、收敛慢；MADDPG 缺少面向抓取的分层奖励与势场引导。
- 该文用 DM-KMP 压缩示教轨迹，并用 PWS-MADDPG 把拇指与四指建模为独立智能体。

## ❓ 需要解决的问题
- 少量示教能否覆盖 11 类物体的抓取轨迹生成？
- 多智能体分解能否改善异构关节协调与训练收敛速度？
- 势场引导与权重调度奖励能否稳定训练并提升成功率？
- 仿真策略能否迁移真机，并按外加载荷实时调节[[抓取力调节]]？

## 📥📤 输入与输出
- 输入：关节角与接触力、物体位姿、示教关节角阈值、各智能体局部状态。
- 输出：各指关节角增量（位置控制）与期望接触力（力控制），即五指动作序列。

## ✅ 论文最终达到的效果
- 11 类物体抓取成功率 85.48%，较 DDPG 提升 40.31%，较 MADDPG 提升 20.05%。
- 2000 回合训练约 12 h 收敛，单步动作推理 <20 ms，满足实时控制。
- Gazebo（ODE）训练后迁至真机五指手，任务流程一致，测试物体均可稳定抓取，体现[[仿真到现实迁移]]能力。
- 五只六维力传感器圆柱杯（340 g）逐级加 50 g 砝码至 490 g：拇指握力 6.04→6.55 N，负载力 1.34→1.58 N。
- 补充验证可抓不同载荷的变形纸杯，载荷变化时各指同步增力。

## 🔗 关联
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#多智能体强化学习 #示教学习 #运动基元 #五指手 #仿真到现实迁移
