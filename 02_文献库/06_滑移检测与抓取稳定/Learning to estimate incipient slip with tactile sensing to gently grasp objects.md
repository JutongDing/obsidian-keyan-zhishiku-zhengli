---
title: Learning to estimate incipient slip with tactile sensing to gently grasp objects
year: 2024
doi: 10.1109/ICRA57147.2024.10611517
arxiv: 
key: KB-093
venue: 2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [初始滑移, 安全裕度, 抓取力调节, 触觉传感, 视触觉, CNN]
pdf: ../../../Learning_to_estimate_incipient_slip_with_tactile_sensing_to_gently_grasp_objects.pdf
confidence: high
source: pdf
aliases: []
---

# Learning to estimate incipient slip with tactile sensing to gently grasp objects

## 📌 年份
2024（ICRA 2024，5 月 13–17 日，横滨）

## 🔑 论文识别码
DOI: 10.1109/ICRA57147.2024.10611517

## 👥 作者与所属院校
- 作者：Dirk-Jan Boonstra, Laurence Willemet, Jelle Luijlx, Michaël Wiertlewski
- 机构：代尔夫特理工大学认知机器人系、麻省理工学院 CSAIL

## 📖 研究背景
- 轻柔抓取要在"够摩擦"与"别压坏"之间取平衡，难点是摩擦系数逐物体、逐次抓取都在变。
- 现有触觉方案多在检测到真实滑移后才反应，此时物体已位移，脆弱物体可能已损。
- 该文把抓取[[安全裕度]]（frictional safety margin Γ）作为回归目标，用 CNN 从触觉图像直接估计"离滑移还有多远"。

## ❓ 需要解决的问题
- 能否从单帧触觉图像回归出连续的 Γ，而不是只给二分类滑移标签？
- 估计精度在平面/曲面、高摩擦/低摩擦条件下是否一致？
- 用估计的 Γ 做比例闭环控力，能否稳定维持 20%、40%、60% 的目标裕度？
- 换成当天重新标定的传感器与环境湿度条件，模型是否仍可用？

## 📥📤 输入与输出
- 输入：双指彩色软指尖（减色混色原理）的触觉图像左右拼接帧，50 Hz 刷新。
- 输出：0–100% 的[[安全裕度]]估计值 Γ，经比例控制器转成夹爪目标夹持力（0.25–3.2 N 区间）。

## ✅ 论文最终达到的效果
- ShuffleNetV2 主干 + 全连接回归头，Γ 估计平均准确率 98.2%，验证集在另一天采集。
- 触觉图像 50 Hz 刷新，满足实时控力；抓取力大小对估计误差无显著影响。
- 用 20/40/60% 三档目标抓草莓（20 g）、橘子（90 g）、香蕉（180 g），夹持力随目标显著上升（p<0.001）。
- 目标裕度越高全滑移次数越少，60% 档草莓零次完全滑移；≤40% 档夹持力低于力封闭抓取所需。
- 缓慢加米（载荷渐增）实验中，控制器按目标持续上调夹持力，验证动态载荷适应。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]
- [[Finger contact sensing and the application in dexterous hand manipulation]]

## 🏷️ 标签
#初始滑移 #安全裕度 #抓取力调节 #触觉传感 #CNN
