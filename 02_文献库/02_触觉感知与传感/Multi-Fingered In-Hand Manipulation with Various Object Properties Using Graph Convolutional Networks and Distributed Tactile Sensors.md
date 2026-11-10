---
title: "Multi-Fingered In-Hand Manipulation with Various Object Properties Using Graph Convolutional Networks and Distributed Tactile Sensors"
year: 2022
doi: 
arxiv: 2205.04169
key: KB-098
venue: arXiv 预印本（cs.RO，首页未标注会议/期刊，待补）
theme: 02_文献库/02_触觉感知与传感
tags: [手内操作, 图卷积网络, 三轴触觉, 物体属性, 灵巧手]
pdf: ../../../Multi-Fingered In-Hand Manipulation with Various Object Properties Using Graph Convolutional Networks and Distributed Tactile Sensors.pdf
confidence: high
source: pdf
aliases: []
---

# Multi-Fingered In-Hand Manipulation with Various Object Properties Using Graph Convolutional Networks and Distributed Tactile Sensors

## 📌 年份
2022

## 🔑 论文识别码
arXiv:2205.04169

## 👥 作者与所属院校
- 作者：Satoshi Funabashi, Tomoki Isobe, Fei Hongyi, Atsumu Hiramoto, Alexander Schmitz 等
- 机构：早稻田大学（Waseda University）

## 📖 研究背景
- 多指[[灵巧手]]上的触觉传感器尺寸、形状各异，而卷积网络要求矩形输入，必须人为映射排布。
- 这种映射会在曲面上打乱相邻关系，拇指实际更靠近其他手指，固定手指顺序并不反映真实构型。
- 该文改用图卷积网络（GCN），按手部几何邻接建图，并为每个物体附加属性标签来调节动作。【待建名词：图卷积网络】

## ❓ 需要解决的问题
- 不规则分布的三轴触觉阵列能否不经矩形化预处理，直接作为控制输入？
- 单个网络能否兼顾软硬、轻重、滑涩各类物体，既不捏碎也不掉落？
- 属性标签是否真的改变抓取力，使软物在操作中不被压扁？

## 📥📤 输入与输出
- 输入：Allegro 手四指 24 个 uSkin 三轴传感器加手掌，共 1152 维触觉；16 维关节角；物体属性标签。
- 输出：下一时刻各指关节角指令，同步屈伸完成[[手内操作]]。

## ✅ 论文最终达到的效果
- 8 种未训练物体（轻约 40 g、重约 100 g）总成功率 73.75%（59/80）（正文写 73.85%，与表 II 不一致，待核对）。
- 标签正确时软塑料圆柱截面保持圆形，标签错误时被压成椭圆，证明标签可调节抓取力。
- 实验者猛拉被抓物体、彻底改变抓取状态后，手仍能恢复并到达目标[[抓取位姿]]。
- PCA 显示 GCN 各节点聚类与手指构型对应，网络学到测地特征。
- 局限：初始抓取位置须在小范围内，指节间隙偶会卡住物体。

## 🔗 关联
- [[CNN-based Methods for Object Recognition with High-Resolution Tactile Sensors]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]

## 🏷️ 标签
#手内操作 #图卷积网络 #三轴触觉 #物体属性 #灵巧手
