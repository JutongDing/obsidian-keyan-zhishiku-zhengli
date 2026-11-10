---
title: Learning Reactive Dexterous Grasping via Hierarchical Task-Space RL Planning and Joint-Space QP Control
year: 2026
doi: 
arxiv: 2605.03363
key: KB-086
venue: arXiv preprint（cs.RO, v1）
theme: 02_文献库/01_灵巧手抓取规划
tags: [反应式抓取, 强化学习, 二次规划, 仿真到现实迁移, 灵巧手]
pdf: ../../../Learning Reactive Dexterous Grasping via Hierarchical Task-Space RL Planning and Joint-Space QP Control.pdf
confidence: high
source: pdf
aliases: []
---

# Learning Reactive Dexterous Grasping via Hierarchical Task-Space RL Planning and Joint-Space QP Control

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2605.03363

## 👥 作者与所属院校
- 作者：Ho Jae Lee、Yonghyeon Lee、Alexander Alexiev、Tzu-Yuan Lin、Se Hwan Jeon 等
- 机构：麻省理工学院（MIT）机械工程系，美国

## 📖 研究背景
- 多指反应式抓取是接触丰富的混合动力学问题，接触模式突变、摩擦复杂，比平行夹爪难得多。
- 接触隐式 MPC 需精确物体几何与可靠接触状态估计，且常依赖准静态假设，难应对动态抓取。
- 单一大策略同时承担任务推理、高维关节协调与安全约束，负担过重，策略难引导、难保证安全，亟需新的[[抓取规划]]范式。

## ❓ 需要解决的问题
- 能否把高层"往哪抓"的空间意图与低层"关节怎么动"的执行显式解耦？
- 在严格满足运动学极限与避碰约束的前提下，策略能否零样本迁移到真机？
- 安全裕度与动态障碍能否由操作者在线调整，而无需重新训练策略？

## 📥📤 输入与输出
- 输入：机器人本体状态、目标物体位置与粗包围盒尺寸（不含精确三维网格与接触状态）。
- 输出：100 Hz 手掌位姿速度指令（arm agent）与指尖线速度指令（hand agent），经 500 Hz[[二次规划]]解算为关节速度。

## ✅ 论文最终达到的效果
- 提出多智能体[[强化学习]]规划 + GPU 并行 QP 的分层框架：高层 100 Hz，低层 500 Hz，约束由 QP 硬性保证。
- 在 7 自由度臂 + 20 自由度五指手上验证，仿真随机种子平均成功率 81.4%，位置误差 4.2 cm、姿态误差 15.9°。
- 测试集 26 个物体中成功抓取并抬起 22 个；不同长宽比物体自动选出偏心抓、包络抓等策略。
- 纯仿真训练的策略零样本迁移真机，可在外部扰动后在线重规划并恢复抓取。
- 结构解耦带来"零样本可操纵性"：不改策略即可调整安全裕度、绕开新出现的障碍。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[Contact-Implicit Model Predictive Control for Dexterous In-hand Manipulation A Long-Horizon and Robust Approach]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#反应式抓取 #强化学习 #二次规划 #仿真到现实迁移
