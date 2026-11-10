---
title: Quadratic Programming for Multirobot and Task-Space Force Control
year: 2019
doi: 10.1109/TRO.2018.2876782
arxiv: 
key: KB-114
venue: IEEE Transactions on Robotics, Vol.35, No.1（2019-02）
theme: 02_文献库/03_阻抗与柔顺控制
tags: [二次规划, 多机器人, 任务空间控制, 力跟踪, 全身操作]
pdf: ../../../Quadratic Programming for Multirobot and Task-Space Force Control(1).pdf
confidence: high
source: pdf
aliases: []
---

# Quadratic Programming for Multirobot and Task-Space Force Control

## 📌 年份
2019（2018-11 在线发表，2019-02 正刊）

## 🔑 论文识别码
DOI: 10.1109/TRO.2018.2876782

## 👥 作者与所属院校
- 作者：Karim Bouyarmane、Kevin Chappellet、Joris Vaillant、Abderrahmane Kheddar
- 机构：法国洛林大学 CNRS/Inria Nancy-Grand Est（LORIA）、CNRS-AIST 联合机器人实验室（筑波）

## 📖 研究背景
- 任务空间多目标控制普遍写成[[二次规划]]（QP），按权重、严格优先级或混合优先级组织多个任务，每拍在线求解。
- 机器人要与固体、铰接机构、被动或浮动基物体交互时，任务描述与接触力一致性很难写。
- 该文把交互对象与机器人一并建模为「机器人簇」，塞进单个集中式 QP，并补上接触感知与力控闭环。

## ❓ 需要解决的问题
- 任意被动、半被动或全驱动实体及其交互约束，能否统一进一个 QP 并算出物理一致的接触力？
- QP 控制器如何从「只跟踪运动」扩展到可靠闭环跟踪期望接触力？
- 在真实人形、机械臂与多指灵巧手上，控制频率与力跟踪表现是否达标？

## 📥📤 输入与输出
- 输入：各机器人簇的动力学模型、任务约束（关节/速度/力矩/非滑移）、期望任务加速度与期望接触力（力/力矩传感器或观测器）。
- 输出：关节加速度、接触力系数 λ 与[[关节力矩控制]]指令，经位置控制接口下发。

## ✅ 论文最终达到的效果
- 在 HRP-4 人形、ROMEO 机械臂与 Shadow 多指手上验证，控制频率分别取 100 Hz 与 200 Hz。
- 力跟踪用对角增益 KI 把力误差转成速度，再经 20 Hz 三阶 Butterworth 低通，作为 QP 的末端任务闭环。
- 完成全身操作、灵巧手点击笔、机器人-机器人共操作门、抽屉、箱体乃至弹簧笔等铰接机构。
- 多机器人 QP 与[[柔顺控制]]结合，使任务描述简化到交互层；框架与实现开源，硬约束冲突时退化为加权折中。

## 🔗 关联
- [[Fast Dextrous Regrasping with Optimal Contact Forces and Contact Sensor-Based Impedance Control]]
- [[Non-Parametric Self-Identification and Model Predictive Control of Dexterous In-Hand Manipulation]]
- [[A Learning-based Controller for Multi-Contact Grasps on Unknown Objects with a Dexterous Hand]]

## 🏷️ 标签
#二次规划 #任务空间控制 #力跟踪 #全身操作
