---
title: "An open-source anthropomorphic robot hand system: HRI hand"
year: 2020
doi: 10.1016/j.ohx.2020.e00100
arxiv: 
key: KB-070
venue: HardwareX
theme: 02_文献库/04_绳驱机构与结构设计
tags: [拟人手, 欠驱动, 四杆机构, 开源硬件, 模块化手指]
pdf: ../../../HRI hand.pdf
confidence: high
source: pdf
aliases: [HRI hand, Human-Robot Interaction LAB hand]
---

# An open-source anthropomorphic robot hand system: HRI hand

## 📌 年份
2020（HardwareX 第 7 卷，e00100）

## 🔑 论文识别码
DOI: 10.1016/j.ohx.2020.e00100（种子所记 10.17605/OSF.IO/SFPB2 为硬件项目 DOI）

## 👥 作者与所属院校
- 作者：Hyeonjun Park、Donghan Kim（通讯）
- 机构：韩国庆熙大学电子工程系

## 📖 研究背景
- 协作机器人需要能操作工具的多指末端，商用手爪价格高、结构与固件封闭。
- 高自由度拟人手要配大量驱动器与复杂机构，成本与维护门槛居高不下。
- 该文给出全开源、可 3D 打印的欠驱动拟人手 HRI hand，整机约 500 美元。

## ❓ 需要解决的问题
- 6 个直线舵机能否驱动 5 指多关节结构，并保留接近人手的预成形（pre-shaping）运动？
- 双四杆机构的[[欠驱动手]]指模块，指尖轨迹能否覆盖抓取所需工作空间？
- 模块化手指能否按需组合成二指、三指或四指末端并接入 ROS？

## 📥📤 输入与输出
- 输入：上位机经 HC-06 蓝牙下发的电机 ID（1–6）与 PWM 指令（500–1000）。
- 输出：6 个 PQ12 直线舵机的推杆位移，经双四杆机构映射为 DIP/PIP/MCP 关节角（拇指为 IP/MCP/CMC）。

## ✅ 论文最终达到的效果
- 整手 5 指、6 个驱动器、重 0.57 kg、尺寸 84×61×235.5 mm，轻于 Shadow 手（4.3 kg）。
- 成本约 500 美元（纯 3D 打印）或 400 美元（SUS304 加工），MIT 许可开放 CAD、固件与 ROS 包。
- 功率抓取（方、长方、圆柱、球，14–1011 g）与精度抓取（长方、三指）实验均通过。
- 提供 URDF、rviz 节点与关节角速度测试，可改装为二/三/四指末端。

## 🔗 关联
- [[A Novel Synthesis of Computational Approaches Enables Optimization of Grasp Quality of Tendon-Driven Hands]]
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]

## 🏷️ 标签
#拟人手 #欠驱动 #四杆机构 #开源硬件
