---
title: TacDexGrasp: Compliant and Robust Dexterous Grasping with Tactile Feedback
year: 2026
doi: 
arxiv: 2603.07040
key: KB-141
venue: arXiv preprint (cs.RO)（正式发表信息待核对）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [触觉反馈, 二阶锥规划, 抓取稳定, 柔顺抓取]
pdf: ../../../TacDexGrasp.pdf
confidence: high
source: pdf
aliases: []
---

# TacDexGrasp: Compliant and Robust Dexterous Grasping with Tactile Feedback

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2603.07040（无 DOI）

## 👥 作者与所属院校
- 作者：Yubin Ke, Jiayi Chen, Hang Lv, Xiao Zhou, He Wang（通讯）等
- 机构：北京大学、Galbot、北京智源人工智能研究院

## 📖 研究背景
- 多指手力控维度高：既要分配各接触力抵消重力，又要在抓取点远离质心时抑制重力矩引起的转动滑移。
- 已有柔顺抓取工作多面向平行夹爪或欠驱动手，自由度低，偏置抓取时易转动滑移、峰值力偏大。
- 该文用触觉反馈加二阶锥规划（SOCP），直接约束各指切向与法向力之比，不显式建模力矩、不做 [[滑移检测]]。

## ❓ 需要解决的问题
- 多接触力分配能否在力矩建模之外同时抑制平动与转动滑移？
- 转动滑移是否必然在某接触点诱发平动滑移，从而切向/法向力比可作早期稳定指标？
- SOCP 能否在约 10 ms 内求解并稳定跟踪到 16 自由度全驱动手？
- 对未知质量、未知摩擦与易损形变物，成功率与峰值接触力能否优于既有基线？

## 📥📤 输入与输出
- 输入：4 个 Tac3D [[视触觉传感器]] 测得的三维接触力、Leap 手 16 个关节状态、在线估计的物体质量与摩擦系数。
- 输出：各指目标法向与切向力（受 [[摩擦锥]] 约束的 SOCP 最优解），再经 PID 转成关节指令。

## ✅ 论文最终达到的效果
- 12 类物体真机实验平均成功率 83%，平均最大接触力 1.59 N，较最优基线低约 38%。
- 形变物 1.24 N/75%、细长物 1.96 N/80%；基线 BODex 为 2.20 N/35%、2.83 N/20%。
- SOCP 单次求解约 10 ms；质量估计比值接近 1，杯内加米与快速抖动下仍保持稳定。
- 消融去掉 PID 跟踪或 SOCP 模块后成功率下降、峰值力上升；受 Leap 出力与 30 Hz 触觉刷新率限制。

## 🔗 关联
- [[Reactive Slip Control in Multifingered Grasping Hybrid Tactile Sensing and Internal-Force Optimization]]
- [[Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#触觉反馈 #二阶锥规划 #抓取稳定 #柔顺抓取
