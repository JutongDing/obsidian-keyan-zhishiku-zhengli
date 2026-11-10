---
title: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity
year: 2026
doi: 10.1126/scirobotics.ady2869
arxiv: 
key: KB-161
venue: Science Robotics（vol. 11, eady2869, 2026）
theme: 02_文献库/09_视触融合与VLA
tags: [视触融合, 自监督预训练, 多任务策略, 在线模仿学习, 灵巧手]
pdf: ../../../Visual-tactile pretraining and online multitask learningfor humanlike manipulation dexterity.pdf
confidence: high
source: pdf
aliases: []
---

# Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1126/scirobotics.ady2869

## 👥 作者与所属院校
- 作者：Qi Ye, Qingtao Liu, Siyun Wang, Jiaying Chen, Yu Cui 等（前两位同等贡献）
- 机构：浙江大学控制科学与工程学院、杭州电子科技大学自动化学院

## 📖 研究背景
- 拟人五指手要像人一样灵巧，需在高维动作空间里协调多指并判断接触时机。
- [[手内操作]]面临高维观测、频繁遮挡与复杂手-物接触动力学，单靠视觉难以消解。
- 依赖示教的[[模仿学习]]需为每个状态采集精确机器人数据，难以规模化。
- 该文模仿人类"观察+练习"：先用人类演示做视触表征预训练，再在线学统一多任务策略。

## ❓ 需要解决的问题
- 仅靠人类视频与触觉手套的二值接触事件，能否学到可迁移的[[视触融合]]表征？
- 只有单目图像与稀疏二值触觉的低成本系统，成功率能到多高？
- 统一多任务策略能否泛化到未见但手-物协调模式相似的新任务？
- 预训练表征相比纯视觉训练，在样本效率与成功率上提升多少？

## 📥📤 输入与输出
- 输入：单目 RGB 图像、二值触觉接触事件、本体感知与任务标识（task ID）。
- 输出：Shadow 手多指关节动作，由统一多任务策略给出。

## ✅ 论文最终达到的效果
- 两阶段框架：MAE 式掩码重建学跨模态整合 token，再用强化学习加在线模仿学统一策略。
- 五个复杂任务、25 个物体上平均成功率 85%。
- 额外泛化到三个未见任务，其手-物协调模式与训练任务共享。
- 只用单目相机与低成本二值触觉事件，不需高分辨率视触觉传感器。
- 在三种不同原理与分辨率的触觉传感器上做了迁移验证。

## 🔗 关联
- [[3D-ViTac Learning Fine-Grained Manipulation with Visuo-Tactile Sensing]]
- [[N0-VTLA Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens]]
- [[OmniVTLA Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing]]

## 🏷️ 标签
#视触融合 #自监督预训练 #多任务策略 #在线模仿学习 #灵巧手
