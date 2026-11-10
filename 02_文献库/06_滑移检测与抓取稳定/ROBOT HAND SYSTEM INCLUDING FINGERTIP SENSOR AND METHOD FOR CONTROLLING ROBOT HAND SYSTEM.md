---
title: ROBOT HAND SYSTEM INCLUDING FINGERTIP SENSOR AND METHOD FOR CONTROLLING ROBOT HAND SYSTEM
year: 2025
doi: 
arxiv: 
key: KB-197
venue: WO 2025/165077 A1
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [专利, 指尖传感器, 锥形接触, 抓取力调节, 机器人手]
pdf: ../../../韩国机械手.pdf
confidence: medium
source: pdf
aliases: [핑거팁 센서를 포함하는 로봇 핸드 시스템 및 로봇 핸드 시스템 제어방법, 韩国机械手]
---

# ROBOT HAND SYSTEM INCLUDING FINGERTIP SENSOR AND METHOD FOR CONTROLLING ROBOT HAND SYSTEM

## 📌 年份
2025（公开日 2025-08-07）

## 🔑 论文识别码
WO 2025/165077 A1（专利公开号；申请号 PCT/KR2025/001359）

## 👥 作者与所属院校
- 作者（发明人）：JUNG Ho Sang, LEE Seung Yeon
- 机构（申请人）：AIDIN ROBOTICS INC.（韩国）

## 📖 研究背景
- 本文为专利公开文本，属 PCT 国际申请公开（WO 2025/165077 A1），非期刊论文。
- 指尖传感器易受装配误差与接触姿态影响，接触判定不准会造成抓取力过大或物体滑脱。
- 该专利先判定锥形接触（cone contact），再把目标手指抓取力调到目标值后执行抓取，兼顾力平衡与力矩上限。

## ❓ 需要解决的问题
- 如何仅凭指尖传感器信号判定手指与物体已形成稳定的锥形接触？
- 多指协同中如何把目标手指（对应拇指）的抓取力调到设定目标力？
- 抓取时如何保证各指对物体的作用力平衡，或使各指力矩之和不超过阈值力矩？

## 📥📤 输入与输出
- 输入：多根手指的指尖传感器信号、手指驱动指令与位置反馈、锥形接触判定结果、目标抓取力。
- 输出：各指驱动指令与抓取模式（力平衡，或力矩之和不超过阈值力矩）、完整抓取动作序列。

## ✅ 论文最终达到的效果
- 主张一种含指尖传感器的机器人手系统及其控制方法（权利要求细节待核对）。
- 控制流程：驱动多指接近物体 → 判定目标手指与物体形成锥形接触 → 调目标指抓取力至目标值 → 执行抓取。
- 抓取模式一：使各指对物体的作用力相互平衡；模式二：使各指施加的力矩之和等于或小于阈值力矩。
- 优先权为 2024-01-29 韩国申请 10-2024-0013196，国际申请日 2025-01-23。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Modulation of grip force with load force during point-to-point arm movements]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#专利 #指尖传感器 #锥形接触 #抓取力调节
