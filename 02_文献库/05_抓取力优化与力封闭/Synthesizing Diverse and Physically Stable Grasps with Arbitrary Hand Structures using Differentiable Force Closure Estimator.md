---
title: Synthesizing Diverse and Physically Stable Grasps with Arbitrary Hand Structures using Differentiable Force Closure Estimator
year: 2021
doi: 
arxiv: 2104.09194
key: KB-140
venue: IEEE Robotics and Automation Letters (RA-L)
theme: 02_文献库/05_抓取力优化与力封闭
tags: [力封闭, 抓取合成, 可微优化, 能量模型]
pdf: ../../../Synthesizing Diverse and Physically Stable Grasps with Arbitrary Hand Structures using Differentiable Force Closure Estimator.pdf
confidence: high
source: pdf
aliases: []
---

# Synthesizing Diverse and Physically Stable Grasps with Arbitrary Hand Structures using Differentiable Force Closure Estimator

## 📌 年份
2021

## 🔑 论文识别码
arXiv:2104.09194（RA-L 2021 预印本，DOI 见期刊页）

## 👥 作者与所属院校
- 作者：Tengyu Liu, Zeyu Liu, Ziyuan Jiao, Yixin Zhu, Song-Chun Zhu 等
- 机构：加州大学洛杉矶分校 VCLA、北京通用人工智能研究院（BIGAI）、北京大学、清华大学

## 📖 研究背景
- 抓取合成长期分两派：解析法依赖特定手型与物体假设，适用面窄；数据驱动法则受限于示教数据。
- 人手抓取数据训练出的模型难迁移到三指夹爪等异构末端，泛化能力差。
- [[力封闭]] 是公认的 [[抓取质量]] 指标，但需解接触力优化，计算昂贵，极少被直接当作优化目标。
- 该文把力封闭误差写成可微能量项，毫秒级求值并可反传梯度，据此做抓取合成。

## ❓ 需要解决的问题
- 能否构造毫秒级、可微的力封闭估计，使力封闭误差直接作为损失函数？
- 不使用任何训练数据，能否对任意手结构合成物理稳定且多样的抓取？
- 合成抓取在物理仿真中是否真稳定，接触点是否贴合、无穿透？
- 力封闭分数能否与真实抓取质量一致，并达到或超过解析与数据驱动基线？

## 📥📤 输入与输出
- 输入：物体形状（DeepSDF 隐式 SDF）、手模型与关节参数（MANO 参数或可微正运动学）、接触点候选集合。
- 输出：手部 [[抓取位姿]] 与接触点集合、力封闭误差值（能量）、优化后的接触力与稳定性评分。

## ✅ 论文最终达到的效果
- 力封闭单次判定达毫秒级；合成单步约 224.4 ms，其中 200 ms 以上用于 SDF 二阶梯度。
- 仿真成功率 85.00%（σ<0.0005），持平数据驱动 Visuo-Haptic 的 85.00%，高于 Unions of Balls 的 72.53%。
- 371 个合成抓取的能量景观与 Feix 分类大体对应，并给出分类体系之外的新抓取类型。
- 无需改动即可用于三指 Robotiq 夹爪与去掉拇指的 MANO 手，验证结构无关性。
- 局限：凹形物体易被单指满足力封闭，且依赖完美的形状先验。

## 🔗 关联
- [[Grasping Force Optimization for Multi-Fingered Robot Hands]]
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#力封闭 #抓取合成 #可微优化 #能量模型
