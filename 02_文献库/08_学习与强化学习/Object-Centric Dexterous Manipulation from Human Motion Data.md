---
title: Object-Centric Dexterous Manipulation from Human Motion Data
year: 2024
doi: 
arxiv: 2411.04005
key: KB-106
venue: arXiv 预印本（arXiv:2411.04005v1）
theme: 02_文献库/08_学习与强化学习
tags: [物体中心操作, 分层策略, 人手动作捕捉, 仿真到现实, 数据增广]
pdf: ../../../Object-Centric Dexterous Manipulation from Human Motion Data.pdf
confidence: high
source: pdf
aliases: []
---

# Object-Centric Dexterous Manipulation from Human Motion Data

## 📌 年份
2024

## 🔑 论文识别码
arXiv: 2411.04005（2024-11-06 v1；无 DOI）

## 👥 作者与所属院校
- 作者：Yuanpei Chen、Chen Wang、Yaodong Yang、C. Karen Liu
- 机构：Stanford University、北京大学

## 📖 研究背景
- 物体中心操作把任务目标写成物体 6-DoF 位姿轨迹，比语言或符号目标更易检验，但双臂双手的高维动作空间让策略学习极难。
- 纯[[强化学习]]方法多只学手指动作，忽略双臂与双手协同；[[模仿学习]]可借人手数据，却受人手机理差异（embodiment gap）阻碍。
- 该文分层处理：高层用人手动作捕捉数据生成类人手腕轨迹，低层在机器人具身上学手指控制。

## ❓ 需要解决的问题
- 仅给定物体目标轨迹，能否生成与之匹配的双腕 6-DoF 参考轨迹？
- 手腕引导能否把高维手指策略的学习难度降到可训练规模，并缓解具身差异？
- 生成模型与控制器能否泛化到未见物体几何与未见目标轨迹？
- 仿真训练的策略能否迁移到真实双臂[[灵巧手]]系统？

## 📥📤 输入与输出
- 输入：物体类别 ID 与期望物体轨迹（预测步长 T=10）；低层观测为物体位姿、机器人本体感觉及高层生成的手腕动作序列。
- 输出：双腕 6-DoF 动作（含 ±4 cm、±0.5 rad 残差修正）与各手指关节动作。

## ✅ 论文最终达到的效果
- 高层用 ARCTIC 数据集 339 条序列、约 210 万步训练 Transformer 生成模型，低层用 PPO；训练时以[[域随机化]]增广物体尺寸、初始位姿与目标路点。
- 10 类家居物体上比 Vanilla RL 平均高 47.3%，比指尖映射等基线高约 50%；数据增广回路再加约 7%（多目标场景 +18%）。
- 真机两台 Shadow Hand + UR10e，完成率比基线高 50% 以上（基线多低于 20%），比采样 MPC 基线平均高 46.3%。
- [[仿真到现实迁移]]用教师-学生蒸馏去掉速度类观测；4 路俯视相机 + FoundationPose 估位姿，15 Hz。

## 🔗 关联
- [[Learning Dexterous In-Hand Manipulation]]
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#物体中心操作 #分层策略 #人手动作捕捉 #仿真到现实
