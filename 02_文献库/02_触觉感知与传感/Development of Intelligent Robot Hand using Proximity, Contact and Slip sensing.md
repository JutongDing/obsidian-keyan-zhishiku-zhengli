---
title: Development of Intelligent Robot Hand using Proximity, Contact and Slip sensing
year: 2010
doi: 
arxiv: 
key: KB-001
venue: 2010 IEEE International Conference on Robotics and Automation (ICRA)
theme: 02_文献库/02_触觉感知与传感
tags: [接近觉传感, 触觉传感, 滑移检测, 抓取力控制, 拾放任务]
pdf: ../../../2010ICRA_hasegawa_Development of Intelligent Robot Hand using Proximity, Contact and Slip sensing.pdf
confidence: high
source: pdf
aliases: []
---

# Development of Intelligent Robot Hand using Proximity, Contact and Slip sensing

## 📌 年份
2010

## 🔑 论文识别码
KB-001（本地编号；ICRA 2010 论文，原文未给 DOI）

## 👥 作者与所属院校
- 作者：Hiroaki Hasegawa, Yoshitomo Mizoguchi, Kenjiro Tadakuma, Aiguo Ming, Masatoshi Ishikawa 等（6 人）
- 机构：电气通信大学、Harmonic Drive Systems、大阪大学、东京大学

## 📖 研究背景
- 视觉在非接触相到接触相的边界区被手指遮挡，出现传感信息空档。
- 指尖空间狭小，传感器布线必须最小化，且需 1 ms 级响应以配合 1 kHz 控制回路。
- 已有工作或只做高速接触检测，或只做滑移抑制，缺少视觉—接近—触觉—滑移一体化的[[灵巧手]]。

## ❓ 需要解决的问题
- 如何让压力中心（CoP）触觉与接近传感器在同一指尖表面共面共存，而不牺牲响应速度？
- 手掌接近传感的二维位置输出能否直接吸收初始位姿误差，替代高精度视觉引导？
- 未知重量与摩擦条件下，能否仅靠[[滑移检测]]在线设定目标抓取力？

## 📥📤 输入与输出
- 输入：CoP 触觉传感器的受力中心位置与合力总和、网状接近传感器的照度中心与总和（折算为距离）、指尖光电反射器输出。
- 输出：各关节力矩指令（位置型力控 + 接近/接触时序伺服），以及由滑移判据逐次更新的目标抓取力 f_d。

## ✅ 论文最终达到的效果
- 平台为 Harmonic Drive Systems 三指 8 自由度手，ART-Linux 下实现 1 ms 控制回路。
- 在 CoP 传感器上开 6 mm 通孔嵌入光电反射器，触觉与接近共用同一表面；网状接近传感器仅 6 根线，布线量与感应面积无关。
- 手掌接近传感可覆盖约 ±50 mm 的初始位置误差，接近段锁定在 6 mm 焦距峰值处。
- 目标物 50–200 g 逐级变化时抓取力随重量单调增大，实现[[自适应抓取]]与[[抓取力调节]]。
- 滑移判据同时用于运输段抗干扰与落位触发，贯通 12 步 Pick&Place，无需预设释放位姿。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#接近觉传感 #触觉传感 #滑移检测 #抓取力控制 #拾放任务
