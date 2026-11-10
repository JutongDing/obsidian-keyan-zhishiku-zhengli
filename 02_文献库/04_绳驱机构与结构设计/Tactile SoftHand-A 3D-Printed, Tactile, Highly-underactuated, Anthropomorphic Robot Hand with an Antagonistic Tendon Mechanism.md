---
title: "Tactile SoftHand-A: 3D-Printed, Tactile, Highly-underactuated, Anthropomorphic Robot Hand with an Antagonistic Tendon Mechanism"
year: 2025
doi: 
arxiv: 2406.12731
key: KB-152
venue: 待补（SAGE 期刊投稿模板，DOI 为占位 10.1177/ToBeAssigned；arXiv 预印本）
theme: 02_文献库/04_绳驱机构与结构设计
tags: [腱驱动, 欠驱动手, 视触觉传感器, 拮抗肌腱, 3D打印, 遥操作]
pdf: ../../../TactileSoftHandA3DPrinted.pdf
confidence: high
source: pdf
aliases: []
---

# Tactile SoftHand-A: 3D-Printed, Tactile, Highly-underactuated, Anthropomorphic Robot Hand with an Antagonistic Tendon Mechanism

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2406.12731

## 👥 作者与所属院校
- 作者：Haoran Li, Christopher J. Ford, Chenghua Lu, Yijiong Lin, Matteo Bianchi 等（8 人）
- 机构：布里斯托大学/布里斯托机器人实验室、西交利物浦大学、意大利技术研究院（IIT）、比萨大学

## 📖 研究背景
- [[腱驱动]]多指[[欠驱动手]]须在少驱动器下保持拟人灵巧性，被动回弹元件占空间且削弱可控性。
- Pisa/IIT SoftHand 单电机即可自适应抓取，但只靠被动弹性复位，无法主动伸展或做指尖操作。
- 指尖触觉可闭环补偿抓取扰动，但整手触觉集成的装配成本高，需与打印结构一体化。

## ❓ 需要解决的问题
- 增加一根拮抗腱后，两电机的主动/拮抗协调能否实现关节主动屈伸与抓取模式切换？
- 全 3D 打印的视触觉指尖能否做到单件成型、免手工装配并保持足够灵敏度？
- 触觉反馈与拮抗机构耦合后，扰动响应、承载与可操作性能提升多少？

## 📥📤 输入与输出
- 输入：主动/拮抗两电机指令、指尖触觉图像（marker 位移密度图、1-SSIM 形变量）、手势遥操作指令。
- 输出：两电机位置/力指令，进而给出各指关节屈曲伸展、接触定位、滑移判定与抓取补偿动作。

## ✅ 论文最终达到的效果
- 五指全 3D 打印（Stratasys J826 多材料），仅 2 台 HX-35H 电机（11.1 V 下 25 kg·cm），手指 115×20×23 mm。
- 相对被动复位版 BPI SoftHand，闭合时间由 1.4 s 降至 0.5 s，响应与扳手力/力矩约提升 2 倍。
- 单指承载测试加 8 N 砝码仍能保持；多数日常物体 5/5 抓取成功，可切换包络、指尖、捏取三种模式。
- 触觉闭环下可检测[[初始滑移]]并补偿手势；遥操作中按人手手势同步，扰动时避免物体掉落。

## 🔗 关联
- [[An open-source anthropomorphic robot hand system HRI hand]]
- [[Geometric design optimization of an under-actuated tendon-driven robotic gripper]]
- [[A General Contact Force Analysis of an Under-actuated Finger in Robot Hand Grasping]]

## 🏷️ 标签
#腱驱动 #欠驱动手 #视触觉传感器 #拮抗肌腱 #3D打印 #遥操作
