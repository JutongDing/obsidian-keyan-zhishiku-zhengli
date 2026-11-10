---
title: Self-adaptive control of a two-point contact gripper for the precise handling of compliant objects in industrial robotics
year: 2026
doi: 10.1016/j.cogr.2025.11.001
arxiv: 
key: KB-129
venue: Cognitive Robotics, 6 (2026) 1–19（KeAi/Elsevier，2025-11-22 在线）
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [抓取力调节, 抓取力跟踪, 模糊控制, 强化学习, 柔性物体]
pdf: ../../../Self-adaptive control of a two-point contact gripper.pdf
confidence: high
source: pdf
aliases: []
---

# Self-adaptive control of a two-point contact gripper for the precise handling of compliant objects in industrial robotics

## 📌 年份
2026

## 🔑 论文识别码
DOI: 10.1016/j.cogr.2025.11.001

## 👥 作者与所属院校
- 作者：Sarawit Cheewaratchanon, Jutamanee Auysakul, Paramin Neranon, Arisara Romyen
- 机构：泰国宋卡王子大学（Prince of Songkla University）工程学院机械与机电工程系、经济学院

## 📖 研究背景
- 工业夹爪多针对单一物体定制开环策略，闭环力控研究长期稀缺，难以落地。
- 柔性、可变形物体的接触刚度非线性，经典 PID 在材质变化时力跟踪性能急剧退化。
- 该文模仿人类抓取的力曲线，把 PID、PI-模糊（PI-FLC）与[[强化学习]]并列比较。

## ❓ 需要解决的问题
- 面对刚度差异悬殊的物体，经典 PID 的力跟踪误差与稳定性差距有多大？
- 模糊规则与 RL 能否同时改善[[抓取力跟踪]]精度、稳定性与跨材质泛化？
- 控制器能否在线感知滑移并实时修正夹持力，做到不滑落、不压坏？

## 📥📤 输入与输出
- 输入：指尖 OptoForce OMD-20-SE-40N 三轴力（100 Hz）、位移传感器（175 Hz）、由人类触觉实验得到的参考力曲线。
- 输出：步进电机驱动的位置/夹持力指令，实现[[抓取力调节]]。

## ✅ 论文最终达到的效果
- 五类物体实测：金属 9.82 N/6.26 mm、硅胶 10.59 N、塑料 5.30 N/7.60 mm、泡沫 4.61 N/8.58 mm、海绵 1.40 N/13.29 mm（力/位移）。
- PID 在软材料上 RMSE 最高、方差最大；RL 的 RMSE 明显更低；PI-FLC 全材质 RMSE 最低且最稳定。
- FFT 显示 PID 在 90–100 Hz 仍有高频峰，PI-FLC 能量集中在 30 Hz 以下，力控更平滑。
- t 检验支持三类控制器差异显著；自适应控制器可实现实时[[滑移检测]]与力修正。
- 局限：仅两指二点接触原型、物体种类少，未做工业节拍下的长期可靠性验证。

## 🔗 关联
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]
- [[Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]

## 🏷️ 标签
#抓取力调节 #力跟踪 #模糊控制 #强化学习 #柔性物体
