---
title: Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing
year: 2024
doi: 10.1109/TNNLS.2023.3270579
arxiv: 
key: KB-091
venue: IEEE Transactions on Neural Networks and Learning Systems, vol. 35, no. 10
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [滑移检测, GelStereo, 视触觉, ConvLSTM, 滑移反馈控制, 拧瓶盖]
pdf: ../../../Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing.pdf
confidence: high
source: pdf
aliases: []
---

# Learning-Based Slip Detection for Dexterous Manipulation Using GelStereo Sensing

## 📌 年份
2024（TNNLS 第 35 卷第 10 期，2023-05-24 在线发表）

## 🔑 论文识别码
DOI: 10.1109/TNNLS.2023.3270579

## 👥 作者与所属院校
- 作者：Shaowei Cui, Shuo Wang, Rui Wang, Shaolin Zhang, Chaofan Zhang
- 机构：中国科学院自动化研究所多模态人工智能系统全国重点实验室、中国科学院大学人工智能学院

## 📖 研究背景
- [[滑移检测]]是抓取失败的直接前兆，也是[[灵巧手]]操作闭环里最稀缺的反馈信号。
- 阈值法与模型法依赖接触模型假设，换物体、换接触条件即失效。
- GelStereo（GS）[[视触觉传感器]]输出 2-D 位移场与 3-D 点云，比单张[[触觉图像]]多出几何维度，正好可补上这一缺口。

## ❓ 需要解决的问题
- 把 2-D 位移场序列与 3-D 接触点云同时送入网络，是否比只用图像更准？
- 位置嵌入（PE）模块带来的精度增益来自接触位置变化还是别的因素？
- 双分支各自贡献多少？去掉 3-D 分支性能掉多少？
- 检测结果如何接入实时回路，驱动夹持力自适应而不顶坏易碎物？
- 换机器人平台、换任务（抓取/拧盖）是否仍成立？

## 📥📤 输入与输出
- 输入：GS 传感器 20 Hz 输出的接触面 2-D 位移场序列与 3-D 点云。
- 输出：滑移/非滑移标签及滑移时刻，经安全策略生成器转为夹爪目标力增量（力指令 100 Hz、末端位姿指令 20 Hz）。

## ✅ 论文最终达到的效果
- PE-ConvLSTM 在完全未见测试集上达 95.79% 检测准确率，高于现有视触觉模型法与学习法。
- 消融：加 PE 模块提升 1.22%；去掉 3-D 分支时本方法仅掉 0.24%，而仅 2-D 版本掉 3.4%。
- 判定滑移的最优时间窗为 200 ms，滑移触发力阈值 δf = 1 N。
- 真实平台完成鸡蛋抓取、瓶盖拧紧/拧松：随滑移发生逐步加力，稳定后保持，拧紧至 56 N 上限停止。
- 在多种机器人/夹爪配置上复现，验证控制框架的通用性。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[FingerVision Tactile Sensor Design and Slip Detection Using Convolutional LSTM Network]]

## 🏷️ 标签
#滑移检测 #GelStereo #视触觉 #ConvLSTM #滑移反馈控制
