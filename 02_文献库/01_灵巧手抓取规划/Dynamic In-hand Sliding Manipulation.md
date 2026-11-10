---
title: Dynamic In-hand Sliding Manipulation
year: 2015
doi: 
arxiv: 
key: KB-043
venue: 2015 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
theme: 02_文献库/01_灵巧手抓取规划
tags: [动态抓取, 受控滑移, 极限曲面, 重抓取规划]
pdf: ../../../Dynamic In-hand Sliding Manipulation.pdf
confidence: high
source: pdf
aliases: []
---

# Dynamic In-hand Sliding Manipulation

## 📌 年份
2015

## 🔑 论文识别码
KB-043（本地编号；PDF 未印 DOI）

## 👥 作者与所属院校
- 作者：Jian Shi, J. Zachary Woodruff, Kevin M. Lynch
- 机构：美国西北大学神经科学与机器人实验室（NxR）

## 📖 研究背景
- 抓取过程中物体相对手指的滑动普遍存在，可用于装配误差纠正、指步重抓取与松手，但多数研究只把滑移当作需要抑制的扰动。
- 已有重抓取依赖外部接触或准静态指步，缺少通过手部惯性载荷主动规划滑移、一步到达目标抓取位形的方法。
- 该文以软指极限曲面接触模型刻画摩擦，对 n 指抓取建立滑移动力学并规划手部加速度，实现动态 [[手内操作]] 式的重定位。

## ❓ 需要解决的问题
- 给定手/物状态、法向接触力与手加速度，如何求物体相对加速度（正动力学）？
- 给定期望相对加速度，如何反解手加速度与法向力（逆动力学）？
- 如何规划手部运动，使捏抓中的方块滑到目标抓取位形，并用迭代减小误差？
- 规划结果在真实机器人上能复现到什么精度？

## 📥📤 输入与输出
- 输入：n 指抓取的接触几何、各指法向力、软指极限曲面摩擦参数（含最大摩擦与扭转摩擦）、目标相对位形。
- 输出：手（末端）加速度与轨迹、各指法向力序列，以及物体相对手指的滑动轨迹。

## ✅ 论文最终达到的效果
- 建立基于软指极限曲面的 n 指滑移动力学正/逆解，并给出由各指极限曲面合成抓取极限曲面的方法。
- 应用于竖直平面内两指捏抓方块的两个算例，其中一个在真机 ERIN 平台（Barrett WAM + Allegro 手 + BioTac 指尖 + OptiTrack）上验证。
- 滑动阶段约 0.8 s，物体按规划轨迹相对手指滑移并完成重定位。
- 重复实验的重定位误差：x 均值 1.03 cm（s.d. 0.23 cm）、y 1.12 cm（s.d. 0.4 cm）、θ −0.16 rad（s.d. 0.27 rad）；作者归因于机械臂轨迹跟踪误差、摩擦参数与法向力不确定性。

## 🔗 关联
- [[GraspNet A Large-Scale Clustered and Densely Annotated Dataset for Object Grasping]]
- [[CoorGrasp Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- [[A Mathematical Introduction to Robotic Manipulation]]

## 🏷️ 标签
#动态抓取 #受控滑移 #极限曲面 #重抓取
