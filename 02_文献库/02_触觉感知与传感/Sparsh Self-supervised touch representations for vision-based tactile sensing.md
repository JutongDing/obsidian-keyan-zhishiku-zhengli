---
title: "Sparsh: Self-supervised touch representations for vision-based tactile sensing"
year: 2024
doi: 
arxiv: 2410.24090
key: KB-137
venue: arXiv 预印本（待补）
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉传感器, 自监督学习, 触觉表征, 基准测试, 跨传感器迁移]
pdf: ../../../Sparsh.pdf
confidence: high
source: pdf
aliases: []
---

# Sparsh: Self-supervised touch representations for vision-based tactile sensing

## 📌 年份
2024（arXiv 首版 2024-10-31）

## 🔑 论文识别码
arXiv: 2410.24090（无 DOI）

## 👥 作者与所属院校
- 作者：Carolina Higuera, Akash Sharma, Chaithanya Krishna Bodduluri, Taosha Fan, Patrick Lancaster 等
- 机构：Meta FAIR、华盛顿大学、卡内基梅隆大学

## 📖 研究背景
- [[视触觉传感器]]（GelSight、DIGIT 等）已成机器人操作的重要模态，但每换传感器或任务就得重训专用模型。
- 触觉真值标签（接触力、滑移）采集昂贵，且各传感器光照、标记点形式差异导致表征无法复用。
- 该文把计算机视觉成熟的自监督学习搬到触觉，追求一套跨传感器、跨任务的通用表征。

## ❓ 需要解决的问题
- 能否用无标签触觉图像预训练出通用表征，替代任务与传感器专用的手工设计模型？
- 掩码重建与像素/潜空间自蒸馏（MAE、IJEPA、DINO、VJEPA）哪种预训练目标更有效？
- 在仅 33%–50% 标注预算下，通用表征能否超过端到端专用训练？
- 表征能否零样本或少样本迁移到形态完全不同的新传感器？

## 📥📤 输入与输出
- 输入：DIGIT、GelSight 2017、GelSight Mini 三种传感器共约 661k 张[[触觉图像]]，其中 70%（462.7k）用于自监督预训练。
- 输出：通用触觉特征向量，接轻量任务解码器后输出力、滑移、位姿、抓取稳定性、织物类别等。

## ✅ 论文最终达到的效果
- 提出 Sparsh 模型族与 TacBench 六任务基准（T1 力估计至 T6 迷宫珠）。
- 在 33%–50% 标注数据下，比任务/传感器专用端到端模型平均提升 95.1%。
- 抓取稳定性分类：Sparsh(VJEPA) 仅用 33% 数据，在 DIGIT 上约 80% 准确率。
- 跨传感器迁移：GelSight 上训练的织物分类器在 DIGIT 上 10-shot 达 61.8%，端到端仅 10.9%。
- Sparsh(DINO) 整体比 Sparsh(IJEPA) 高 5.6%；解码器微调收益有限，冻结特征已足够强。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[Embedding high-resolution touch across robotic hands enables adaptive human-like grasping]]

## 🏷️ 标签
#视触觉传感器 #自监督学习 #触觉表征 #TacBench #跨传感器迁移
