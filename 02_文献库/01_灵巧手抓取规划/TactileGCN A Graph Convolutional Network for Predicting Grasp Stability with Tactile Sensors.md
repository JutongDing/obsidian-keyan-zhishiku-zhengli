---
title: TactileGCN: A Graph Convolutional Network for Predicting Grasp Stability with Tactile Sensors
year: 2019
doi: 
arxiv: 1901.06181
key: KB-151
venue: 待补（arXiv 预印本，正文未印会议/期刊名）
theme: 02_文献库/01_灵巧手抓取规划
tags: [图卷积网络, 触觉传感器, 抓取稳定性预测, 滑移, BioTac]
pdf: ../../../TactileGCN.pdf
confidence: high
source: pdf
aliases: []
---

# TactileGCN: A Graph Convolutional Network for Predicting Grasp Stability with Tactile Sensors

## 📌 年份
2019

## 🔑 论文识别码
arXiv:1901.06181

## 👥 作者与所属院校
- 作者：A. Garcia-Garcia, B.S. Zapata-Impata, S. Orts-Escolano, P. Gil, J. Garcia-Rodriguez 等（5 人）
- 机构：西班牙阿利坎特大学 3D 感知实验室

## 📖 研究背景
- 人类凭触觉在抬手前就能判断抓取是否牢靠，机器人尽早判别可避免抓起后掉落。
- 既有工作把触觉读数压平成特征向量或矩阵式[[触觉图像]]，丢失了传感单元的空间邻接关系。
- [[抓取稳定性预测]]多为 stable/slippery 二分类，需要能保留 taxel 几何布局的表示方法。

## ❓ 需要解决的问题
- 把每个 taxel 建成图节点、按物理邻接连边，图卷积能否比矩阵输入更好地表达接触模式？
- 网络深度、宽度与图连接方式（手工边 vs k-NN）如何影响分类精度？
- 在完全未知物体上，该表示还能保持多少预测精度？

## 📥📤 输入与输出
- 输入：Shadow 手三指 BioTac SP 的 taxel 三维坐标与压力读数（每 taxel 三通道特征）。
- 输出：抓取状态二分类（stable / slippery）及其概率。

## ✅ 论文最终达到的效果
- 构建约 5000 次三指抓取、41 个物体的训练集，另录 1000 次抓取、10 个未知物体作测试集；数据集新增 palm 45° 摆位以扩充视角。
- 验证集精度 92.7%；深度宽度扫描显示 5 层、8-8-16-16-32 结构最优，过深易过拟合。
- 手工指定边的 k=0 连接优于 k-NN 稠密连接，连接度越高精度反而下降，稀疏图更契合 taxel 局部性。
- 未知物体测试精度 0.741–0.774（palm down 0.741、45° 0.774、side 0.751），5 折交叉验证取 10 轮均值。

## 🔗 关联
- [[Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration]]
- [[Multi-Fingered In-Hand Manipulation with Various Object Properties Using Graph Convolutional Networks and Distributed Tactile Sensors]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#图卷积网络 #触觉传感器 #抓取稳定性预测 #滑移 #BioTac
