---
title: Variational Neural Belief Parameterizations for Robust Dexterous Grasping under Multimodal Uncertainty
year: 2026
doi: 
arxiv: 2604.25897
key: KB-159
venue: arXiv 预印本（cs.RO，2026-04-28；会议/期刊待补）
theme: 02_文献库/01_灵巧手抓取规划
tags: [风险敏感抓取, CVaR, 变分推断, 接触不确定性, 力封闭]
pdf: ../../../Variational Neural Belief Parameterizations.pdf
confidence: high
source: pdf
aliases: []
---

# Variational Neural Belief Parameterizations for Robust Dexterous Grasping under Multimodal Uncertainty

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2604.25897（PDF 未印 DOI）

## 👥 作者与所属院校
- 作者：Clinton Enwerem, Shreya Kalyanaraman, John S. Baras, Calin Belta
- 机构：美国马里兰大学帕克分校（电子与计算机工程系、系统研究所）

## 📖 研究背景
- 接触参数、传感噪声与外扰使抓取执行本质随机，稳定与否不能只看名义位形。
- 主流解析与数据驱动方法优化期望抓取质量，忽略尾部失败，遇到不利接触实现即掉物。
- 风险敏感 POMDP 虽能处理尾部风险，但粒子滤波信念不可微，CVaR 估计方差大。
- 该文用可微高斯混合信念替代粒子集，直接对尾部鲁棒性做路径梯度优化。

## ❓ 需要解决的问题
- 如何表示摩擦系数、表面柔顺、接触模式与物体位姿的多模态不确定性信念？
- 能否让 CVaR 代理目标对信念参数可微，从而避开高方差蒙特卡洛估计？
- 与粒子滤波 MPC 相比，规划耗时与鲁棒成功率能否同时改善？
- 信念预测的失败概率是否与实际失败率标定一致？

## 📥📤 输入与输出
- 输入：腕部相机 6D 物体位姿估计、指尖压阻触觉读数、关节本体感知、外力扰动序列。
- 输出：手指关节增量（抓取动作），以及每次决策时的接触几何信念参数与终止判据。

## ✅ 论文最终达到的效果
- 信念用 K=8 高斯混合，配 Gumbel-Softmax 组件选择与位置-尺度重参数化实现可微采样。
- 仿真三种摩擦情形：名义 100%、宽分布 79%、双峰 54% 成功率；鲁棒成功率 79%/67%/38%。
- 同条件下 CEM-MPC 双峰情形仅 42% 成功率、33% 鲁棒成功率，名义工况也略低。
- 约 8.5 s 完成一次规划，比粒子滤波 MPC（约 33–50 s）快约一个数量级。
- 真机 3 物体×4 位姿偏移共 12 次试验两法均 100% 成功，该文步数更少、收敛更快。
- 收敛时[[力封闭]]保持，扳手空间可承受 12 N 侧向剪切，终止质量指标优于基线。

## 🔗 关联
- [[SpringGrasp Synthesizing Compliant, Dexterous Grasps under Shape Uncertainty]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#风险敏感抓取 #CVaR #变分推断 #接触不确定性 #力封闭
