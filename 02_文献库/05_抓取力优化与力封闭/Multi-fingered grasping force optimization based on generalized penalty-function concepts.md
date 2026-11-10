---
title: "Multi-fingered grasping force optimization based on generalized penalty-function concepts"
year: 2021
doi: 10.1016/j.robot.2020.103672
arxiv: 
key: KB-100
venue: Robotics and Autonomous Systems, 135 (2021) 103672
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取力优化, 摩擦锥, 二阶锥规划, 惩罚函数, 抓取力分配]
pdf: ../../../Multi-fingered grasping force optimization based on generalized penalty-function concepts.pdf
confidence: high
source: pdf
aliases: []
---

# Multi-fingered grasping force optimization based on generalized penalty-function concepts

## 📌 年份
2021

## 🔑 论文识别码
DOI: 10.1016/j.robot.2020.103672

## 👥 作者与所属院校
- 作者：Zhong Chen, Qisen Wu, Cao Hong, Xianmin Zhang
- 机构：华南理工大学机械与汽车工程学院、广东省精密装备与制造技术重点实验室

## 📖 研究背景
- 多指手[[抓取力优化]]要在[[摩擦锥]]约束下求满足平衡的接触力，问题本质是二阶锥规划（SOCP）。
- 主流做法把 SOCP 转成半定规划（SDP）求解，需构造大量线性矩阵不等式，计算复杂度高、迭代多。【待建名词：二阶锥规划】
- 该文用障碍函数吸收不等式约束，引入惩罚因子构造增广目标，绕开 LMI 直接做牛顿迭代。

## ❓ 需要解决的问题
- 不引入 LMI 能否处理摩擦锥约束，并把单次求解时间压到亚毫秒级？
- 惩罚因子取何值时抓取既远离摩擦锥边界（稳）又不使关节力矩超限？
- 接触位置与摩擦系数波动时，抓取成功概率有多高？

## 📥📤 输入与输出
- 输入：三指手接触点位置与单位法向、目标物体重力旋量、关节力矩上限、摩擦系数。
- 输出：各指三维接触力，即满足[[力封闭]]的[[接触力分配]]方案及对应关节力矩。

## ✅ 论文最终达到的效果
- 单次求解 0.357 ms，SDP 为 0.724 ms；收敛迭代 7 次 vs 12 次；浮点运算约 11 kflops vs 23 kflops；LMI 数 0 vs 23。
- 1000 次蒙特卡洛：惩罚因子 rk ≤ 5 时抓取成功率 >90%，rk ∈ [0.5, 3] 时提升到 95% 以上。
- 3 s 轨迹仿真中三指关节力矩残差与摩擦残差全程非负，未出现滑移。
- 惩罚因子小则摩擦[[安全裕度]]大、抗滑强；因子大则力矩小但易滑，可按任务取舍。

## 🔗 关联
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]
- [[A forward-reflected-backward method with adaptive stepsize for real-time grasping force optimization in multi-fingered robotic manipulation]]
- [[A Grasping Force Optimization Algorithm for Dexterous Robotic Hands]]

## 🏷️ 标签
#抓取力优化 #摩擦锥 #二阶锥规划 #惩罚函数 #抓取力分配
