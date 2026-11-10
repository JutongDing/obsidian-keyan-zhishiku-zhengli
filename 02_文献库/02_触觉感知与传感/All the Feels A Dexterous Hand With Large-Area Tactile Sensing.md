---
title: "All the Feels: A Dexterous Hand With Large-Area Tactile Sensing"
year: 2023
doi: 10.1109/LRA.2023.3327619
arxiv: 
key: KB-022
venue: IEEE Robotics and Automation Letters
theme: 02_文献库/02_触觉感知与传感
tags: [灵巧手, 大面积触觉, ReSkin, 材料识别, 低成本平台]
pdf: ../../../All the Feels.pdf
confidence: high
source: pdf
aliases: [All the Feels]
---

# All the Feels: A Dexterous Hand With Large-Area Tactile Sensing

## 📌 年份
2023

## 🔑 论文识别码
DOI: 10.1109/LRA.2023.3327619

## 👥 作者与所属院校
- 作者：Raunaq Bhirangi、Abigail DeFranco、Jacob Adkins、Carmel Majidi、Abhinav Gupta 等
- 机构：卡内基梅隆大学（Carnegie Mellon University）、Meta

## 📖 研究背景
- [[灵巧手]]成本高、可靠性差，阻碍其在机器人学习中的大规模部署。
- 缺少可覆盖整手表面的触觉传感方案，使操作技能学习失去低层反馈。
- 深度强化学习与模仿范式需要大量真实接触数据，而现有平台难以支撑长期高频采集。
- 本文切入角度：用低成本 3D 打印结构＋磁弹性 ReSkin 皮肤，做成可整面覆盖的 10 自由度手。

## ❓ 需要解决的问题
- 能否在数千美元级成本内做出可靠、可现场维修、可长期数据采集的灵巧手平台？
- 手掌与指尖全表面覆盖触觉后，触觉信号是否具备足够的材料与纹理判别力？
- 只在手上采集的触觉模型能否泛化到未见物体与杂乱真实场景？
- 大面积触觉相比仅指尖触觉，对分类性能的贡献有多大？

## 📥📤 输入与输出
- 输入：10 个关节位置/电流等本体感知、手掌与指尖 ReSkin 磁信号序列、电机指令（PWM/电流/位置等模式）。
- 输出：关节位置或力矩目标、材料/软硬度/纹理类别标签、抓取成功判定与分拣动作。

## ✅ 论文最终达到的效果
- 三指 10 自由度整机成本约 3500 美元；单个 ReSkin 单元约 20 美元，比 uSkin（约 1000 美元）便宜约 50 倍。
- ReSkin 覆盖手掌全表面与指尖；受芯片短缺限制，指节及指尖侧背面暂无传感。
- 六种同形不同包覆材料分类准确率 71.24%；软硬度＋纹理分层识别同样有效。
- 真实杂乱箱抓取分拣：20 次成功抓取上软硬度与纹理预测准确率均为 65%，模型可跨姿态迁移。
- 样机连续运行 8 个月、累计 400 小时以上无损坏；三次电机故障等均可在 30 分钟内现场修复。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]

## 🏷️ 标签
#灵巧手 #大面积触觉 #磁弹性皮肤 #材料识别
