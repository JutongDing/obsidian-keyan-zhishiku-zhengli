---
title: "Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey"
year: 2025
doi: 10.3389/frobt.2025.1682437
arxiv: 
key: KB-078
venue: Frontiers in Robotics and AI（12:1682437）
theme: 02_文献库/10_综述与展望
tags: [交互式模仿学习, 综述, 灵巧操作, 人类反馈, 策略表示]
pdf: ../../../Interactive imitation learning for dexterous robotic manipulation.pdf
confidence: high
source: pdf
aliases: [Interactive imitation learning for dexterous robotic manipulation]
---

# Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey

## 📌 年份
2025（Frontiers in Robotics and AI，2025-12-19 发表）

## 🔑 论文识别码
DOI: 10.3389/frobt.2025.1682437

## 👥 作者与所属院校
- 作者：Edgar Welte, Rania Rayyes
- 机构：卡尔斯鲁厄理工学院（KIT）物料搬运与物流研究所人工智能与机器人组

## 📖 研究背景
- [[灵巧手]]动作空间高维、接触动力学复杂，数据需求随维度近似指数增长，样本效率成关键。
- 纯[[强化学习]]样本效率低，纯[[模仿学习]]受协变量偏移与分布漂移困扰。
- 交互式模仿学习（IIL）允许人在训练中介入纠错，已在部分任务见效，但[[手内操作]]等灵巧任务研究稀少。
- 该综述系统梳理 IIL 的反馈类型、策略表示与真实部署条件，并指出研究空白。

## ❓ 需要解决的问题
- IIL 的反馈类型（评估式、纠正式、干预式）如何分类、比较与组合？
- 策略表示（参数化、扩散策略、层次式）如何影响样本效率与训练稳定性？
- 高维手部动作空间中 IIL 的具体研究缺口在哪？
- 人形手真实部署还需哪些硬件、安全与数据条件？

## 📥📤 输入与输出
- 输入：IL/RL/IIL 的文献语料（方法、反馈类型、策略表示、任务与平台）。
- 输出：方法分类框架与对比结论、研究缺口与未来方向（含 FIER/PIER 等模块设计）。

## ✅ 论文最终达到的效果
- 定性结论：IIL 用于灵巧操作的具体研究仍明显不足，是待填补的空白。
- 归纳协变量偏移缓解路径：人类纠错数据 + 优先经验回放，并比较监督式与 RL 混合范式。
- 提出 FIER（前瞻交互经验回放：验证—标注—重标注）与 PIER（优先交互经验回放）模块。
- 建议用结构化手部/接触状态反馈与层次策略推进真实人形手部署，并指出[[主从遥操作]]采数的作用。
- 全文为综述，无自采实验数据与量化指标，结论以定性归纳为主。

## 🔗 关联
- [[Dexterous Manipulation for Multi-Fingered Robotic Hands With Reinforcement Learning A Review]]
- [[An overview of learning-based dexterous grasping recent advances and future directions]]
- [[A Review of Modeling of Soft-Contact Fingers and Stiffness Control for Dextrous Manipulation in Robotics]]

## 🏷️ 标签
#交互式模仿学习 #综述 #灵巧操作 #人类反馈 #策略表示
