---
title: A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand
year: 2024
doi: 
arxiv: 2409.12339
key: KB-008
venue: arXiv preprint（cs.RO；会议信息待补）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [抓取控制, 阻抗控制, 多接触包覆抓取, 外力旋量估计, 神经网络]
pdf: ../../../A Learning-based Controller for Multi-Contact Grasps.pdf
confidence: high
source: pdf
aliases: []
---

# A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand

## 📌 年份
2024

## 🔑 论文识别码
arXiv: 2409.12339

## 👥 作者与所属院校
- 作者：Dominik Winkelbauer, Rudolph Triebel, Berthold Bäuml
- 机构：德国宇航中心（DLR）机器人与机电研究所、慕尼黑工业大学 aidx-lab、卡尔斯鲁厄理工学院（KIT）

## 📖 研究背景
- 现有抓取控制器多只支持指尖抓取，或需要显式配置[[内力]]，难以直接用在包覆抓取上。
- 真实抓取常为多指节多点接触，甚至与手掌基座接触，或处于奇异位形。
- 该文只用关节力矩测量与粗略 3D 模型，估计外力旋量并预测抗扰所需力矩。

## ❓ 需要解决的问题
- 任意抓取类型（含多接触包覆抓取与奇异位形）能否由统一的弹性模型解析求解？
- 解析解的实时性不足时，能否用学习网络逼近并保持同等控制效果？
- 外力旋量存在歧义时，如何避免网络「幻觉」出不存在的力而导致误动作？

## 📥📤 输入与输出
- 输入：各关节力矩测量 τm、关节角 qm、粗糙 3D 模型（可由单张深度图重建）。
- 输出：期望关节角 qd（送入关节级[[阻抗控制]]器），间接给出抵消外力所需的[[关节力矩控制]]指令。

## ✅ 论文最终达到的效果
- 施加最大 10 N 的外力旋量时，83.1% 的测试抓取保持稳定。
- 相较两个基线，效率更高且诱发的物体非自愿位移更小。
- 在真实 DLR-Hand II（12 个驱动关节，关节内置力矩传感）上循环时间达 6 ms。
- 采用「最小旋量」损失训练外力估计网络，缓解歧义场景下的错误估计。
- 训练数据由控制器解析式自动生成，全监督、无需人工标注；优于仅在无外力假设下学习的基线。

## 🔗 关联
- [[多指灵巧手动力学建模与柔顺控制技术研究]]
- [[Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control]]
- [[Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control]]

## 🏷️ 标签
#抓取控制 #阻抗控制 #多接触包覆抓取 #外力估计 #神经网络
