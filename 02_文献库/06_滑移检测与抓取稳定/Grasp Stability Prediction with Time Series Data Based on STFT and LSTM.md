---
title: Grasp Stability Prediction with Time Series Data Based on STFT and LSTM
year: 2023
doi: 10.1109/ICARM58088.2023.10218771
arxiv: 
key: KB-061
venue: 2023 8th International Conference on Advanced Robotics and Mechatronics (ICARM), Sanya, China
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [抓取稳定性预测, 滑移检测, STFT, LSTM, 力传感器]
pdf: ../../../Grasp stability prediction with time series data based on STFT and LSTM.pdf
confidence: high
source: pdf
aliases: []
---

# Grasp Stability Prediction with Time Series Data Based on STFT and LSTM

## 📌 年份
2023

## 🔑 论文识别码
DOI: 10.1109/ICARM58088.2023.10218771

## 👥 作者与所属院校
- 作者：Tao Wang、Frank Kirchner
- 机构：深圳 Dorabot 公司、德国不来梅大学数学与计算机科学学院、德国人工智能研究中心机器人创新中心（DFKI RIC）

## 📖 研究背景
- 物流等场景要求机器人搬运多样物品，抓取后需实时判断是否稳定并及时调节抓力。
- [[滑移检测]]多在滑移已发生后才识别；预测比事后检测更有价值，可提前规划安全抬升。
- 视触觉方案要等较大力变化才判稳，响应慢；力传感器精度高、频率高，更适合做早期[[初始滑移]]预警。
- 本文切入：把力/压力时序经短时傅里叶变换（STFT）转入时频域，再交给 LSTM 做稳定性分类。

## ❓ 需要解决的问题
- 仅用力/压力时序，能否在宏观滑动前预测抓取失稳？
- 时域数据叠加 STFT 频谱特征，是否稳定优于纯 LSTM 或其他浅层分类器？
- 用公开力数据集训练、再换压力通道与三指[[灵巧手]]实测，能否保持精度？
- 预测延迟能否满足闭环抓取控制（约 16 Hz）？

## 📥📤 输入与输出
- 输入：力/压力时序（采集 16.7 Hz，每批 160 步；STFT 窗长 20 步、矩形窗、10 个频带）。
- 输出：稳定/失稳（滑移）二分类标签，以及提前于掉落的预测时刻。

## ✅ 论文最终达到的效果
- 公开数据集含 2,550 组、每组 400 步，覆盖 10 个物体；滑移信号频率 2–8 Hz。
- 基线：朴素贝叶斯 68.81%、KNN 79.70%、SVM 84.67%、LSTM 84.60%。
- 四种融合结构中 (Data+STFT)&LSTM 成功率 80.09%，提前预警率 67.50%；纯 LSTM 为 75.27%/84.63%。
- DoraHand 三指手实测：LSTM 89.38%，(Data+STFT)&LSTM 87.24%，均可用于在线预测。
- 16 路传感器单次推理约 4 ms，整手约 16 Hz（64 ms）；方向泛化测试准确率 66.9%–87.4%。

## 🔗 关联
- [[A Robotic Grasping State Perception Framework With Multi-Phase Tactile Information and Ensemble Learning]]
- [[Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand]]
- [[An Adaptive Grasping Force Tracking Strategy for Nonlinear and Time-Varying Object Behaviors]]

## 🏷️ 标签
#抓取稳定性预测 #滑移检测 #STFT #LSTM #力传感器
