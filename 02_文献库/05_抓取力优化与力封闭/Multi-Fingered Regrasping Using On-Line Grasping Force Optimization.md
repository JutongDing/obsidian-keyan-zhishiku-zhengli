---
title: "Multi-Fingered Regrasping Using On-Line Grasping Force Optimization"
year: 1997
doi: 
arxiv: 
key: KB-102
venue: 1997 IEEE International Conference on Robotics and Automation (ICRA), Albuquerque, pp. 998–1003
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 重抓取, 梯度流, 半定规划, 阻抗控制]
pdf: ../../../Multi-fingered regrasping using on-line grasping force optimization.pdf
confidence: high
source: pdf
aliases: []
---

# Multi-Fingered Regrasping Using On-Line Grasping Force Optimization

## 📌 年份
1997

## 🔑 论文识别码
KB-102（本地编号，原文无 DOI/arXiv）

## 👥 作者与所属院校
- 作者：Martin Buss, Thomas Schlegl
- 机构：慕尼黑工业大学自动控制工程研究所（Institute of Automatic Control Engineering, TU München）

## 📖 研究背景
- 早期[[抓取力优化]]多用启发式或非线性规划，只能离线算，满足不了实时控制。
- 该文把问题写成半定规划，在正定矩阵流形上构造线性约束梯度流，用带线搜索的递推式实时求解。
- 进一步把算法推广到重抓取（regrasping）：一指抬起、换接触点再落下，并要求力过渡连续。【待建名词：重抓取】

## ❓ 需要解决的问题
- 递推梯度流能否在毫秒级给出满足[[力封闭]]与[[摩擦锥]]约束的接触力？
- 抬起某指时，如何让该指法向力平滑趋零而不破坏其余手指的平衡？
- 重抓取过程中关节力矩与迭代次数是否保持连续、可预测？

## 📥📤 输入与输出
- 输入：期望外力旋量、接触几何（[[抓取矩阵]]）、摩擦系数、各指权重矩阵。
- 输出：各指接触力旋量与对应的期望关节力矩，以及被弱化手指的法向力轨迹。

## ✅ 论文最终达到的效果
- 递推算法约 10 步即收敛到可用次优解；MC 68040（25 MHz）上单次优化约 5 ms。
- 步长初值 a0 = 2、缩减因子 0.8–0.9 时收敛良好。
- 给出两种弱化手指方式：调权重（wp→∞、wi→0）或加线性约束让法向力按 b(t) 变化；两者结合过渡最平滑。
- 四指抓取仿真：第 4 指接触力在 0.5–1.5 s 降为零、2–3 s 恢复，力矩与迭代曲线连续无跳变。
- 与[[阻抗控制]]结合后，可用刚度/阻尼增益同时规定物体的笛卡尔行为。

## 🔗 关联
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]
- [[Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control]]
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]

## 🏷️ 标签
#抓取力优化 #重抓取 #梯度流 #半定规划 #阻抗控制
