---
title: Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand
year: 2018
doi: 10.1109/aim.2018.8452704
arxiv: 
key: KB-042
venue: 2018 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM), pp. 21–27
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移方向检测, 抓取力调节, 触觉阵列, 人机协作]
pdf: ../../../Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand.pdf
confidence: high
source: pdf
aliases: []
---

# Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand

## 📌 年份
2018

## 🔑 论文识别码
DOI: 10.1109/aim.2018.8452704

## 👥 作者与所属院校
- 作者：Moaed A. Abd, Iker J. Gonzalez, Thomas C. Colestock, Benjamin A. Kent, Erik D. Engeberg
- 机构：美国佛罗里达大西洋大学海洋与机械工程系/计算机与电气工程系、阿克伦大学机械工程系

## 📖 研究背景
- 假肢使用者缺乏抓取力反馈，物体常因无触觉信息而被掉落或捏碎；人机/机机协作同样需要触觉沟通。
- 既有 [[滑移检测]] 多依赖振动频谱判断"是否滑移"，只能触发统一反射，无法区分滑移方向，难以做情境相关响应。
- 该文用 BioTac SP 的 24 电极阻抗序列训练神经网络，实时判别滑移方向，并据此调节抓取协同。

## ❓ 需要解决的问题
- 24 电极阻抗信号能否实时区分滑移方向（东/南/西/北）与接触/未接触状态？
- 在不同滑移速度与摩擦系数（玻璃、涂油玻璃）下，离线分类器是否鲁棒？
- 在线分类精度能否满足实时控制，并支撑抓取力增/减的协同反射？
- 方向感知能否让人-机器人与机器人-机器人之间的物体交接更高效？

## 📥📤 输入与输出
- 输入：Shadow 手食指 BioTac SP 的 24 个电极阻抗时间序列（滑移起始前后）及末端运动。
- 输出：滑移方向类别（东/南/西/北 + Touch/No Touch），经协同控制映射为抓取力增大或松开指令。

## ✅ 论文最终达到的效果
- 离线 ANN 分类总体准确率 91.40%；在线测试四个滑移方向均接近 100%（电极更多、特征更丰富）。
- 检测到沿重力方向下滑时，手自动增大抓取力防止掉落；检测到向上滑移时，主动松手把物体交给同伴。
- 在机器人-机器人、人-机器人两类协作场景中均完成物体交接演示，验证了可行性。
- 结果说明带方向信息的 [[抓取力调节]] 可提供情境相关反射，提高协作任务效率。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]

## 🏷️ 标签
#滑移检测 #滑移方向 #抓取力调节 #人机协作
