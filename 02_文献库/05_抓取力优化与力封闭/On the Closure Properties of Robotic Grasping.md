---
title: On the Closure Properties of Robotic Grasping
year: 1995
doi: 
arxiv: 
key: KB-109
venue: The International Journal of Robotics Research（1994 录用，1995 刊出；卷期待核对）
theme: 02_文献库/05_抓取力优化与力封闭
tags: [形封闭, 力封闭, 部分封闭, 李雅普诺夫方法, 抓取分析]
pdf: ../../../On the Closure Properties.pdf
confidence: high
source: pdf
aliases: []
---

# On the Closure Properties of Robotic Grasping

## 📌 年份
1995（稿件 1993-11 投稿、1994-07 录用；卷期页码待核对）

## 🔑 论文识别码
无 DOI（本地编号 KB-109；原稿页脚注明投 IJRR）

## 👥 作者与所属院校
- 作者：Antonio Bicchi
- 机构：意大利比萨大学「E. Piaggio」研究中心

## 📖 研究背景
- [[形封闭]]与[[力封闭]]是抓取分析的两块基石：前者只依赖单边、无摩擦的几何约束，后者关乎具体装置能否经接触施加任意力。
- 形封闭检验已有成熟算法；力封闭检验要么近似，要么计算昂贵——已有做法需解 12 个带单边约束的非线性规划。
- 该文重新梳理定义，引入部分封闭概念，并把力封闭判别转化为动力系统平衡点问题。

## ❓ 需要解决的问题
- 形封闭与力封闭应怎样定义，才互不重叠又便于分析与实现？
- 只约束部分自由度的「部分形封闭」抓取，能否给出可计算的几何描述算法？
- 力封闭判别能否化为某个常微分方程平衡点的稳定性问题，从而避免逐个求解非线性规划？

## 📥📤 输入与输出
- 输入：接触点位置与法向构成的单边约束集合、摩擦系数、物体几何与抓取构型。
- 输出：形封闭/部分形封闭/力封闭的判定结果、部分形封闭的几何描述，以及动力系统平衡点是否存在。

## ✅ 论文最终达到的效果
- 证明力封闭分析与某个常微分方程的平衡点研究等价，可用李雅普诺夫直接法判别，算法具二次收敛速度。
- 传统方法要解 12 个非线性优化问题，新算法只需积分相应动力系统，效率显著提高。
- 给出部分形封闭的可综合几何描述算法；复述经典结论：平面形封闭至少 4 个接触点、空间至少 7 个。
- 作者自述结果仍限于特定接触模型（点接触、无摩擦或库仑摩擦），综合与更一般模型的分析留作开放问题。

## 🔗 关联
- [[On Geometric Algorithms for Real-Time Grasping Force Optimization]]
- [[Grasping Force Optimization for Multi-Fingered Robot Hands]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#形封闭 #力封闭 #部分封闭 #抓取分析
