---
title: "Contact-Implicit Model Predictive Control for Dexterous In-hand Manipulation: A Long-Horizon and Robust Approach"
year: 2024
doi: 
arxiv: 2402.18897
key: KB-032
venue: 待补（arXiv 预印本）
theme: 02_文献库/01_灵巧手抓取规划
tags: [接触隐式MPC, 手内操作, DDP, 触觉反馈, 阻抗控制]
pdf: ../../../Contact-Implicit Model Predictive Control for Dexterous In-hand Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# Contact-Implicit Model Predictive Control for Dexterous In-hand Manipulation: A Long-Horizon and Robust Approach

## 📌 年份
2024

## 🔑 论文识别码
arXiv:2402.18897（v3, 2024-11）

## 👥 作者与所属院校
- 作者：Yongpeng Jiang, Mingrui Yu, Xinghao Zhu, Masayoshi Tomizuka, Xiang Li（通讯）
- 机构：清华大学自动化系与北京信息科学与技术国家研究中心、加州大学伯克利分校机械工程系

## 📖 研究背景
- 接触高度刚硬且拓扑可变，使实时接触检测与推断困难，基于模型的方法性能被拖累。
- 接触显式方法依赖预定义接触序列或单独规划环节，扰动下序列会变成误导信息。
- 接触隐式方法靠光滑化回避 LCP 求解，但带来「远距离受力」伪影，模式稍有偏差即失败。

## ❓ 需要解决的问题
- 能否不预设接触序列、不做离线规划，在线生成长时程的手内接触动作？
- 高层接触隐式 [[抓取规划]] 与低层执行如何分层，才能既长时程又抗扰？
- 对建模误差、外力扰动与传感噪声，闭环能否稳定恢复接触？

## 📥📤 输入与输出
- 输入：期望物体运动（位姿序列）、当前手–物状态、触觉测得的接触力。
- 输出：20 Hz 的关节参考位置与接触力参考；100 Hz 的 [[关节力矩控制]]/阻抗指令。

## ✅ 论文最终达到的效果
- 提出分层结构：高层接触隐式 MPC 用 DDP 在光滑准静态模型上求解，低层接触控制器以触觉反馈修正轨迹，末端为关节级 [[阻抗控制]]。
- 无需预训练即可泛化到不同物体：球（半径 6 cm）以 0.29 rad/s、立方体（边长 7 cm）以 0.4 rad/s 旋转。
- 四指 Allegro 手（16 个驱动关节）在仿真中跑 RotZ（nq=17）与 Free（nq=23）两套系统，长时程旋转球超过 270°。
- 参考生成 20 Hz、接触控制器 100 Hz，满足实时；Free 系统下可从高斯扰动与噪声中恢复。
- 消融显示无接触控制器时，外力扰动下因接触丢失与误接触直接失败。

## 🔗 关联
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#接触隐式MPC #手内操作 #DDP #触觉反馈 #阻抗控制
