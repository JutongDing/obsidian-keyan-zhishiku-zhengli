---
title: "On the Form-Closure Property of Robotic Grasping"
year: 1994
doi: 
arxiv: 
key: KB-105
venue: Preprints of the 4th IFAC Symposium on Robot Control (SYROCO '94), Capri, Italy
theme: 02_文献库/01_灵巧手抓取规划
tags: [形封闭, 部分形封闭, 线性规划, 凸多面锥, 抓取分析]
pdf: ../../../ON THE FORM-CLOSURE PROPERTY OF ROBOTIC.pdf
confidence: high
source: pdf
aliases: []
---

# On the Form-Closure Property of Robotic Grasping

## 📌 年份
1994

## 🔑 论文识别码
KB-105（本地编号，原文无 DOI/arXiv）

## 👥 作者与所属院校
- 作者：A. Bicchi
- 机构：比萨大学 Centro "E. Piaggio"（Università di Pisa）

## 📖 研究背景
- [[形封闭]]是纯几何性质：仅靠单侧、无摩擦接触约束阻止物体运动，与手或夹具的运动学、接触力大小无关。
- 既有工作多研究抓取综合（给定物体摆放接触点），而分析问题（给定接触点判断还剩哪些自由度）研究较少。
- 该文系统研究部分形封闭（partial form-closure），给出自由运动锥的几何刻画与构造算法。

## ❓ 需要解决的问题
- 给定接触集合，如何判定哪些运动被约束、哪些仍自由？
- 部分形封闭最少需要几个接触点？与 Reuleaux–Somov 条件如何对应？
- 自由运动锥能否用有限个基向量正张成，以便直接用于规划？

## 📥📤 输入与输出
- 输入：物体表面 n 个接触点的位置与法向（构成[[抓取矩阵]]与约束矩阵）。
- 输出：形封闭的布尔判定、自由运动锥的凸基、被约束运动子空间的维数。

## ✅ 论文最终达到的效果
- 形封闭判定等价于线性规划 max fᵀx s.t. NᵀGᵀx ≤ 0 无可行解，可直接用单纯形法检验。
- 证明形封闭至少需 d+1 个接触（平面 4、空间 7），部分形封闭对 m 维子空间需 m+1 个。
- 自由运动子集是凸多面锥，其最大嵌入子空间为 NᵀGᵀ 的零空间，从而与可接近性/可分离性概念接轨。
- 给出算法 1：将约束零空间按 d−1 个一组求交、剔除不可行向量，得到自由运动锥的凸基。
- 明确局限：结论只到一阶（忽略滚动），有限曲率手指的高阶效应未涉及。

## 🔗 关联
- [[A Mathematical Introduction to Robotic Manipulation]]
- [[Dexonomy Synthesizing All Dexterous Grasp Types in a Grasp Taxonomy]]
- [[A Simplified Grasping Strategy for Under-driven Dexterous Hand Based on Geometric Structure]]

## 🏷️ 标签
#形封闭 #部分形封闭 #线性规划 #凸多面锥 #抓取分析
