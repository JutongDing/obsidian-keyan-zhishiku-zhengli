---
title: "Reactive Slip Control in Multifingered Grasping: Hybrid Tactile Sensing and Internal-Force Optimization"
year: 2026
doi: 
arxiv: 2602.16127
key: KB-116
venue: arXiv 预印本（会议/期刊待补）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [反应式滑移控制, 混合触觉, 内力优化, 多指抓取]
pdf: ../../../Reactive Slip Control in Multifingered Grasping.pdf
confidence: high
source: pdf
aliases: [RSC]
---

# Reactive Slip Control in Multifingered Grasping: Hybrid Tactile Sensing and Internal-Force Optimization

## 📌 年份
2026

## 🔑 论文识别码
arXiv: 2602.16127

## 👥 作者与所属院校
- 作者：Théo Ayral、Saifeddine Aloui、Mathieu Grossard
- 机构：格勒诺布尔-阿尔卑斯大学 CEA-Leti、巴黎-萨克雷大学 CEA-List（法国）

## 📖 研究背景
- 多指抓取需在重力、惯性负载与突发扰动下检测并抑制手内滑移，对易碎、易变形物体尤忌接触力过大。
- 平行夹爪常用的「整手同步加力」策略移植到多指手，会引入不希望的物体运动，破坏抓取稳定。
- 依赖显式摩擦模型与外力估计的方法，在真实场景中摩擦系数、物体属性、扰动幅度往往不可得。
- 本文切入角度：把滑移抑制降为与任务层解耦的低层反射环，只在抓取零空间内调节[[内力]]，不动操作力。

## ❓ 需要解决的问题
- 能否不估计摩擦系数、不直接测接触力，仅靠触觉反馈维持接触稳定与摩擦裕度？
- 压电（PzE）快滑移线索与压阻阵列（PzR）接触定位如何组合，在线构建以接触为中心的抓取表示？
- 从[[滑移检测]]到内力更新的闭环能否进入 50 ms 量级，与人类反射基线可比？
- 非对称多指构型下，内力剖面如何在抓取零空间内协调分配？

## 📥📤 输入与输出
- 输入：混合触觉垫信号（PzE 高频动力学、PzR 空间定位）、关节角与本体感知，无需先验物体模型与力矩传感器。
- 输出：[[抓取矩阵]]零空间内的内力剖面更新量与实际期望接触力，用于中止手内滑移并保留物体级力旋量。

## ✅ 论文最终达到的效果
- 受控试验中滑移起始检出延迟 20.4 ± 6 ms（主要来自窗口化与证据累积），几何与控制管线约 10 ms。
- 理论抓取响应延迟约 30 ms；抓取模型更新 <5 ms，内力选择约 4 ms，支持亚 50 ms 触觉驱动响应。
- 实物因分块数据传输，端到端延迟被抬到 100–400 ms，仅能对每次滑移施加单步大内力，无法渐进调节。
- 四指模块化[[腱驱动]]夹具（每指三节、可自转，指尖力达 20 N）上验证对称与非对称三指平面抓取；10 N 外拉力下约 130 ms 触发、物体位移 19 mm 后止滑。
- 全程无显式摩擦模型、无直接力传感，仅凭触觉推断抓取几何。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Grip Stabilization through Independent Finger Tactile Feedback Control]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#滑移检测 #内力调节 #混合触觉 #多指抓取 #低层反射控制
