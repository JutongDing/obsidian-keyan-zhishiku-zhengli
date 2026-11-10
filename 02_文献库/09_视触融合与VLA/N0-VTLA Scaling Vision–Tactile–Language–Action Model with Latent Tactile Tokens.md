---
title: "N0-VTLA: Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens"
year: 2026
doi: 
arxiv: 2607.23782
key: KB-103
venue: arXiv 技术报告（cs.RO，2026-07-26）
theme: 02_文献库/09_视触融合与VLA
tags: [视触融合, 视觉-语言-动作模型, 潜在触觉token, 离线强化学习, 接触密集操作]
pdf: ../../../N0-VTLA.pdf
confidence: high
source: pdf
aliases: [N0-VTLA, VTLA]
---

# N0-VTLA: Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2607.23782

## 👥 作者与所属院校
- 作者：NeoteAI Team 与 Fudan TEAI Team（团队署名，未列个人作者）
- 机构：NeoteAI、复旦大学 TEAI 团队

## 📖 研究背景
- [[视觉-语言-动作模型]]已具备跨任务、跨本体的通用性，但触觉长期缺席，接触密集操作仍是短板。
- 已有触觉扩展只在任务级数据（多为数十小时、少数技能）上训练，缺乏规模化触觉预训练。
- 两种常见接法各有缺陷：把触觉 token 拼进视觉-语言前缀，稀疏触觉被密集视觉淹没；或把当前触觉注入动作去噪，而触觉记录的是已发生的接触，难以预告下一步。

## ❓ 需要解决的问题
- 能否把触觉当作「预测目标」而非「观测上下文」，让策略预判自己动作将造成的接触变化？
- 潜在触觉 token 是否真编码接触状态，而非退化为外观线索？
- 能否仅用已部署的轨迹做离线策略改进，而不重新采集示教？

## 📥📤 输入与输出
- 输入：3 路 RGB、语言指令、机器人状态，以及双指[[视触觉传感器]]的接触差分[[触觉图像]]（30 fps，224×224）。
- 输出：50 步动作块（32 维规范动作容器），由 flow-matching 动作专家在潜在触觉 token 条件下生成。

## ✅ 论文最终达到的效果
- 20 任务仿真套件平均成功率 63.8%，最强基线 44.0%；NeoReal 9 个真机任务全部取胜。
- 潜在 token 对未来触觉的 top-1 检索准确率 92.3%，随机水平仅 3.2%，说明编码的是接触而非外观。
- 配 ALTER 离线改进后，3 个长程真机任务成功率达 75–95%。
- 预训练语料 NeoData 覆盖 ARX X5、UR5e、Flexiv、Franka、Piper 机械臂与 TacUMI 手持夹爪，触觉以图像流而非低维力信号记录。

## 🔗 关联
- [[VLA-Touch Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback]]
- [[3D-ViTac Learning Fine-Grained Manipulation with Visuo-Tactile Sensing]]
- [[OmniVTLA Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing]]

## 🏷️ 标签
#视触融合 #视觉-语言-动作模型 #潜在触觉token #离线强化学习 #接触密集操作
