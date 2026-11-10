---
title: "DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation"
year: 2020
doi: 10.1109/LRA.2020.2977257
arxiv: 2005.14679
key: KB-036
venue: IEEE Robotics and Automation Letters (RA-L)
theme: 02_文献库/02_触觉感知与传感
tags: [视触觉传感器, 触觉硬件设计, 手内操作, 低成本制造]
pdf: ../../../DIGIT- A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation

## 📌 年份
2020

## 🔑 论文识别码
DOI: 10.1109/LRA.2020.2977257（arXiv:2005.14679）

## 👥 作者与所属院校
- 作者：Mike Lambeta, Po-Wei Chou, Stephen Tian, Brian Yang, Benjamin Maloon 等（前四位标注为共同一作）
- 机构：Facebook, Menlo Park, CA, USA

## 📖 研究背景
- 通用 [[手内操作]] 仍是未解难题，核心瓶颈是难以精确感知与推理接触力。
- 触觉要在机器人上普及，需同时满足高分辨率、高灵敏、可靠、易用、紧凑、廉价六项，已有传感器难以兼顾。
- 既有视触觉方案（如 [[GelSight]]）分辨率高但体积大、装配繁琐、弹性体寿命短，难以装到多指手上。

## ❓ 需要解决的问题
- 如何把 [[视触觉传感器]] 压缩到约 20 mm 指尖尺度，同时保留高分辨率 [[触觉图像]]？
- 如何让弹性体与整机装配可重复、可批量制造，并把单件成本压到十几美元？
- 多指手仅凭原始触觉图像，能否闭环完成手内滚球这类接触丰富操作？

## 📥📤 输入与输出
- 输入：OVM7692 摄像头采集的 640×480、60 fps 触觉图像帧（含弹性体形变与标记位移）；目标小球 (x, y) 像素位置。
- 输出：MPC 规划出的手指关节位移动作序列（交低层控制器执行），用于推动玻璃球滚向目标点。

## ✅ 论文最终达到的效果
- 整机 20×27×18 mm、重约 20 g，有效敏感区 19×16 mm，可直接装于 Allegro 多指手各指端。
- 批量 1000 件时单件成本约 15 美元（PCB 1.5、电子元件 8、塑料件 2、凝胶 3）。
- 学得结构化动力学模型后单步 MPC 规划约 1.4 s；对照 CDNA 模型需 69 s，无法实时控制。
- 真机玻璃球滚动中位误差随动作步数收敛，手工整定 P 控制器则发散；约 25% 试次小球中途掉落。
- 设计已在 www.digit.ml 开源。

## 🔗 关联
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]

## 🏷️ 标签
#视触觉传感器 #触觉硬件 #手内操作 #低成本
