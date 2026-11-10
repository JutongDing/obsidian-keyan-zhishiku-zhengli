---
title: Human-taught sensory-control synergy for universal robotic grasping
year: 2026
doi: 10.1093/nsr/nwaf583
arxiv: 
key: KB-073
venue: National Science Review（13: nwaf583）
theme: 02_文献库/08_学习与强化学习
tags: [触觉手套, 多模态触觉, 语义状态, 模糊控制, 人手技能迁移]
pdf: ../../../Human-taught sensory-control synergy for universal robotic grasping.pdf
confidence: high
source: pdf
aliases: []
---

# Human-taught sensory-control synergy for universal robotic grasping

## 📌 年份
2026（2025-12-22 在线发表）

## 🔑 论文识别码
DOI: 10.1093/nsr/nwaf583

## 👥 作者与所属院校
- 作者：Caise Wei, Zijian Liao, Yichen Qin, Qian Mao, Shiqiang Liu, Rong Zhu 等
- 机构：清华大学精密仪器系、精密测试技术及仪器国家重点实验室

## 📖 研究背景
- 多指[[灵巧手]]的视觉抓取检测依赖 RGB-D 与标注框，感知不到接触细节，易滑落或捏碎物体。
- 遥操作、仿真采数成本高、效率低，难覆盖硅胶玩具、食物等非刚体目标。
- 触觉手套可低成本记录人手抓取，但信号随抓取位姿起伏，难以跨人跨物迁移。
- 该文模仿人类神经认知：先把多模态触觉语义化，再由经验型模糊控制器出动作。

## ❓ 需要解决的问题
- 如何用可穿戴手套同步采集接触、滑移与压力三类信号，并支撑[[滑移检测]]？
- 低层触觉时序如何编码成可解释、可迁移的语义抓取状态？
- 单个被试、20% 数据建成的模型能否泛化到未见物体与未见被试？
- 语义状态到握力动作的映射能否实时闭环并抗动态扰动？

## 📥📤 输入与输出
- 输入：指端双铂热感传感器（界面 IS + 压力 PS）时序、视觉给出的物体位置、任务指令。
- 输出：[[接触状态识别]]得到的语义抓取状态（无接触/轻度不稳/稳定）、握力增减档位与关节动作指令。

## ✅ 论文最终达到的效果
- 传感器 0–30 N 量程、迟滞 2.8%、检测下限 <0.005 N、响应 70 ms，5000 次循环稳定，30–65 ℃ 可用。
- 单被试抓取 23 个物体、仅用 20% 数据建成 SCS，6 个未见物体状态识别 81.7%。
- 机器人抓 29 个示教过物体（每物 10 次）平均成功率 95.2%，24 个未见物体 91.25%。
- 可稳抓生鸡蛋、水球、金属球与装液容器；外部下拉扰动下自主增力不掉落。
- 完成 9 个子任务的手冲咖啡流程，可凭触觉判断不透明容器内的勺粉接触状态。

## 🔗 关联
- [[Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- [[Composing Dextrous Grasping and In-hand Manipulation via Scoring with a Reinforcement Learning Critic]]

## 🏷️ 标签
#触觉手套 #多模态触觉 #语义状态 #模糊控制 #人手技能迁移
