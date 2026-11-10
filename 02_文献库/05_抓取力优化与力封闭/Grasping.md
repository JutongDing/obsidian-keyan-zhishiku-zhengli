---
title: Grasping
year: 2016
doi: 
arxiv: 
key: KB-163
venue: Springer Handbook of Robotics（第 2 版第 38 章，待核对）
theme: 02_文献库/05_抓取力优化与力封闭
tags: [抓取模型, 形封闭, 力封闭, 约束分析, 综述章节]
pdf: ../../../grasp Handbook of Robotics.pdf
confidence: medium
source: pdf
aliases: [Springer Handbook of Robotics 第38章 Grasping]
---

# Grasping

## 📌 年份
2016（低置信，待核对：PDF 首页未印出版年，据章节编号与页码推断为第 2 版）

## 🔑 论文识别码
DOI: KB-163（本地编号；PDF 未印 DOI，Springer 章节 DOI 低置信，待核对）

## 👥 作者与所属院校
- 作者：Domenico Prattichizzo, Jeffrey C. Trinkle
- 机构：意大利锡耶纳大学、美国伦斯勒理工学院（据作者长期单位，待核对）

## 📖 研究背景
- 抓取分析需要把接触行为模型与刚体运动学、动力学模型耦合起来统一描述。
- 接触模型的核心是选取各接触点实际传递的力与力矩分量，其余由此派生。
- 完整模型的数学性质自然导出五类基本抓取型，为抓取与操作规划提供物理直觉。
- 本章系统整理抓取建模、柔顺抓取、约束分析（形封闭与力封闭）及封闭质量度量。

## ❓ 需要解决的问题
- 无摩擦点、点接触带摩擦、软指接触、完整约束等模型如何改变可控旋量空间？
- [[形封闭]]与[[力封闭]]的判定条件差在哪里，所需最少接触数为何不同？
- 超静定（hyperstatic）抓取该如何定义可比较的封闭质量度量？
- 刚性假设在何处失效，柔顺接触与关节驱动约束该如何纳入分析？

## 📥📤 输入与输出
- 输入：手-物几何、各接触位置与法向、摩擦系数、关节与驱动约束。
- 输出：[[抓取矩阵]]、可控旋量与力旋量空间、封闭判定结论与质量度量数值。

## ✅ 论文最终达到的效果
- 给出五类抓取分类及各自可控自由度；力封闭依赖摩擦，故比形封闭所需接触更少。
- 平面多边形示例中四个接触即可形封闭；球体、超静定与对偶示例给出闭式判定。
- 以示例对比 LP1 与 Ferrari–Canny 等封闭度量随接触数增加的变化趋势。
- 指出 LP1 度量不随接触增加单调上升，Ferrari–Canny 单调但并非严格单调。
- 指出接触滑动下的稳定性分析仍是开放问题，抓取力分配问题本章未展开。

## 🔗 关联
- [[On the Closure Properties of Robotic Grasping]]
- [[Grasping Force Optimization for Multi-Fingered Robot Hands]]
- [[A Fast Procedure for Optimizing Dynamic Force Distribution in Multifingered Grasping]]

## 🏷️ 标签
#抓取模型 #形封闭 #力封闭 #约束分析 #综述章节
