---
title: Hybrid Closed-Loop Control of Robotic Hand Regrasping
year: 1998
doi: 
arxiv: 
key: KB-075
venue: Proceedings of the 1998 IEEE International Conference on Robotics and Automation（ICRA）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [混合系统, 混合自动机, 变结构阻抗控制, 重抓取, 抓取力优化]
pdf: ../../../Hybrid Closed-Loop Control of Robotic Hand Regrasping .pdf
confidence: high
source: pdf
aliases: []
---

# Hybrid Closed-Loop Control of Robotic Hand Regrasping

## 📌 年份
1998（ICRA 1998，Leuven，pp.3026–3031）

## 🔑 论文识别码
KB-075（本地编号，原文无 DOI）

## 👥 作者与所属院校
- 作者：Thomas Schlegl, Martin Buss
- 机构：慕尼黑工业大学自动控制工程研究所（TU München）

## 📖 研究背景
- 多指手抓取在接触开/合之间切换，本质是离散-连续混合动力学，单一连续控制器难以描述。
- 重抓取（手指抬起→移到新接触点→再接触）会改变抓取拓扑，须在线重构参考轨迹。
- 物体几何建模误差会造成离散抓取状态错误，可能瞬间失去[[力封闭]]并滑落。
- 该文用混合自动机生成分阶段参考，配变结构[[阻抗控制]]构成混合闭环。

## ❓ 需要解决的问题
- 如何统一建模离散抓取状态与连续关节/接触动力学？
- 减力、移动、增力、回稳四阶段的混合参考如何自动生成与切换？
- 离散状态错误如何检测与补偿，避免抓取失稳？
- 补偿后能否在重抓取全程维持力封闭？

## 📥📤 输入与输出
- 输入：指端接触传感器信号、关节角与角速度、物体位姿误差、离散状态指令。
- 输出：各指关节力矩、接触力旋量（经[[抓取力优化]]求解）、离散状态切换与参考修正量。

## ✅ 论文最终达到的效果
- 4 指平面手、1 kg 立方体（带未建模台阶）、Kp=120I₈、Kd=60I₈ 的动力学仿真验证。
- 无补偿时离散误差由 [0 0 0 −1]ᵀ 恶化到 [0 −1 0 −1]ᵀ，掉指后失去力封闭并滑落。
- 预滤波补偿（外推重抓指轨迹、线性修正期望接触点）显著降低物体位置误差，全程保持力封闭。
- 参考自适应（停在 MOVE 态直至接触传感器确认再接触）误差下降幅度相近，同样全程力封闭。
- 仅数值仿真验证，未上实物手；作者将形式化行为分析与混合补偿器综合列为后续工作。

## 🔗 关联
- [[Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]
- [[Adaptive Grasping by Multi Fingered Hand with Tactile Sensor based on Robust Force and Position Control]]

## 🏷️ 标签
#混合系统 #混合自动机 #变结构阻抗控制 #重抓取 #抓取力优化
