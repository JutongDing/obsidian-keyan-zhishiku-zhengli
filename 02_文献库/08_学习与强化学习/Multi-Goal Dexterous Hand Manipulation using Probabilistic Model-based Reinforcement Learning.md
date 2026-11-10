---
title: "Multi-Goal Dexterous Hand Manipulation using Probabilistic Model-based Reinforcement Learning"
year: 2025
doi: 
arxiv: 2504.21585
key: KB-099
venue: arXiv 预印本（cs.RO，首页未标注会议/期刊，待补）
theme: 02_文献库/08_学习与强化学习
tags: [强化学习, 基于模型的强化学习, 模型预测控制, 多目标, 灵巧手]
pdf: ../../../Multi-Goal Dexterous Hand Manipulation using.pdf
confidence: high
source: pdf
aliases: [GC-PMPC]
---

# Multi-Goal Dexterous Hand Manipulation using Probabilistic Model-based Reinforcement Learning

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2504.21585

## 👥 作者与所属院校
- 作者：Yingzhuo Jiang, Wenjun Huang, Rongdun Lin, Chenyang Miao, Tianfu Sun 等
- 机构：中国科学院大学、中国科学院深圳先进技术研究院

## 📖 研究背景
- 传统控制难建手-物动力学模型，[[强化学习]]成为替代路线，但多目标任务奖励稀疏、值函数学习需上万小时级交互。
- 基于模型的强化学习（MBRL）用学到的动力学模型提高样本效率，可高维灵巧手动力学难以准确刻画。
- 真实[[灵巧手]]控制频率低，MPC 在线求解负担重，需异步策略才能落地。

## ❓ 需要解决的问题
- 概率神经网络集成能否比原 DPETS 更稳定地描述多指手高维动力学？
- 异步 MPC 能否在约 3 Hz 的真实控制频率下完成在线规划？
- 单一策略能否按不同目标位姿（骰子不同面朝上）切换而不遗忘旧目标？

## 📥📤 输入与输出
- 输入：12 个主动关节角、5 个指尖触觉法向力、骰子三维位置与四元数位姿（单目相机检测）。
- 输出：12 维关节角动作序列，驱动 60 mm 立方骰子达到目标朝向。

## ✅ 论文最终达到的效果
- 4 个 Shadow Hand 仿真任务、每个 20 个随机目标，成功率全面超过 DPETS、TD7 等基线。
- Hand Reach 200 回合（400 s）掌握；Egg 位置+姿态任务 100 回合（30 min）达 80%，其余基线几乎不学习；纯姿态任务 1 h 约 70%，基线仅 20%。
- 真机 DexHand 021（12 主动 + 7 被动自由度、5 个触觉传感器）三个目标各约 28 min，共约 80 min 学会，控制频率 3 Hz。
- 学新目标时旧目标测试奖励不下降，体现多目标兼容。

## 🔗 关联
- [[Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing]]
- [[Learning Dexterous In-Hand Manipulation]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#强化学习 #基于模型的强化学习 #模型预测控制 #多目标 #灵巧手
