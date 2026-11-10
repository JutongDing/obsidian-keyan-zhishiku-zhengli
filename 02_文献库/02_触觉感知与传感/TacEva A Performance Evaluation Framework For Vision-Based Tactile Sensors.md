---
title: "TacEva: A Performance Evaluation Framework For Vision-Based Tactile Sensors"
year: 2025
doi: 
arxiv: 2509.19037
key: KB-142
venue: arXiv preprint (cs.RO)（期刊/会议信息待核对）
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉传感器, 性能评测, 标定, 空间分辨率]
pdf: ../../../TacEva-A Performance Evaluation Framework For Vision-Based Tactile Sensors.pdf
confidence: high
source: pdf
aliases: []
---

# TacEva: A Performance Evaluation Framework For Vision-Based Tactile Sensors

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2509.19037（无 DOI）

## 👥 作者与所属院校
- 作者：Qingzheng Cong, Steven Oh, Wen Fan, Shan Luo, Kaspar Althoefer 等
- 机构：帝国理工学院生物工程系、伦敦玛丽女王大学先进机器人中心、伦敦国王学院

## 📖 研究背景
- [[视触觉传感器]] 空间分辨率高、制造成本低，被广泛用于机器人任务，但传感机理、结构尺寸差异造成性能差异显著。
- 缺少统一度量，使任务前的传感器选型与后续参数微调都缺乏依据。
- 现有工作多为定性罗列，缺少可重复、跨传感器可比的定量评测流程。
- 该文提出 TacEva：内在指标、标准性能、鲁棒性三层框架，并为每个指标设计结构化实验流水线。

## ❓ 需要解决的问题
- 如何定义覆盖典型应用场景的量化指标，并保证不同传感机理之间可比、可重复？
- 力与位置回归精度、空间分辨率、机械灵敏度、鲁棒性如何在同一机器人平台上统一测量？
- 四种代表性传感器（ViTacTip、MagicTac、GelSight Mini、GelSightWM）各自优劣如何排序？
- 性能差异能否追溯到弹性体材料、厚度、标记设计等结构因素并指导设计优化？

## 📥📤 输入与输出
- 输入：传感器在不同压深、位移、接触位置下的 [[触觉图像]] 与原始读数、机器人末端位姿与力真值、3D 打印线/点光栅板。
- 输出：MAE、R²、sMAPE，空间分辨率曲线、机械灵敏度与一致性、鲁棒性量化指标与选型建议。

## ✅ 论文最终达到的效果
- 四款传感器实测：视场 1257/304/266/266 mm²、厚度 50/15/4.25/4.25 mm、帧率 30/60/25/25 Hz。
- 力回归 ViTacTip 绝对误差最低（Fz MAE 0.0164、R² 0.978），但量程仅 0.7 N，致 sMAPE 偏高。
- 容差收紧到 0.05 mm 时空间分辨率：ViTacTip 降至 80.6%，GelSight 系列 99.0%、MagicTac 98.3%。
- 结论性规律：软厚穹顶凝胶易贴合但会平滑局部细节；薄而平整的中等模量弹性体在柔顺与保真间更优。

## 🔗 关联
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#视触觉传感器 #性能评测 #标定 #空间分辨率
