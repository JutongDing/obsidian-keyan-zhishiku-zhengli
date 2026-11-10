---
title: "Grasp to Act: Dexterous Grasping for Tool Use in Dynamic Settings"
year: 2026
doi: 
arxiv: 2602.20466
key: KB-164
venue: arXiv 预印本（cs.RO，2026-02-24；会议/期刊待补）
theme: 02_文献库/08_学习与强化学习
tags: [工具使用, 动态抓取, 抓取优化, 强化学习, 零样本sim2real]
pdf: ../../../grasp_to_act_dexterous_grasping_for_tool_use_in_dynamic_setting.pdf
confidence: high
source: pdf
aliases: []
---

# Grasp to Act: Dexterous Grasping for Tool Use in Dynamic Settings

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2602.20466（PDF 未印 DOI）

## 👥 作者与所属院校
- 作者：Harsh Gupta, Mohammad Amin Mirzaee, Wenzhen Yuan
- 机构：美国伊利诺伊大学厄巴纳-香槟分校（UIUC）

## 📖 研究背景
- 现有灵巧抓取多按静态几何稳定性优化，一旦出现冲击、扭矩或持续阻力便失效。
- 锤击、锯切、搅拌等工具使用正是这类动态载荷场景，对抓取稳定性要求远高于静态抓取。
- 低自由度夹爪接触点少，难以抵抗大力矩；[[灵巧手]]可形成包络抓取分散载荷。
- 该文把物理抓取优化与[[强化学习]]在线抓取自适应结合，兼顾初始位形与全程稳定。

## ❓ 需要解决的问题
- 如何在抓取采样与评分阶段就把任务动态载荷纳入，而不仅看几何稳定？
- 在线自适应能否只做小幅关节修正就抑制手内滑移，不必重规划？
- 纯仿真训练的策略能否零样本迁移到真实工具任务？
- 换工具尺寸、质量与形状后，抓取还能否保持稳定？

## 📥📤 输入与输出
- 输入：RGB-D 观测、人类演示轨迹（提供动态条件与初始抓取位置）、物体轨迹、任务力条件。
- 输出：腕部位姿与手指关节位置残差修正（在线自适应策略输出的动作）。

## ✅ 论文最终达到的效果
- 五个工具任务（锤击、锯切、切割、搅拌、舀取）零样本[[仿真到现实迁移]]，任务完成率优于基线。
- 仿真中五任务抓取成功率均 100%，手内平移滑移降至 0.69–0.94 cm。
- 旋转滑移显著下降，如锤击 1.35°，而 RL 基线为 4.07°。
- 三种锤子变体仅训练其一，仍达 100% 成功且滑移很小。
- 去掉在线自适应的消融在锯切任务成功率降到 92.3%，旋转滑移升至 11.43°。

## 🔗 关联
- [[FunGrasp Functional Grasping for Diverse Dexterous Hands]]
- [[Just Add Force for Contact-Rich Robot Policies]]
- [[Closing the Reality Gap Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

## 🏷️ 标签
#工具使用 #动态抓取 #抓取优化 #强化学习 #零样本sim2real
