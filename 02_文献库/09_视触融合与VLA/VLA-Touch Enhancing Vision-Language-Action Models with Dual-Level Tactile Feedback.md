---
title: "VLA-Touch: Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback"
year: 2025
doi: 
arxiv: 2507.17294
key: KB-158
venue: arXiv（cs.RO 预印本，v2）
theme: 02_文献库/09_视触融合与VLA
tags: [视触融合, 视觉-语言-动作模型, 触觉感知, 扩散策略, 接触密集操作]
pdf: ../../../VLA-Touch.pdf
confidence: high
source: pdf
aliases: [VLA-Touch]
---

# VLA-Touch: Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback

## 📌 年份
2025

## 🔑 论文识别码
arXiv:2507.17294

## 👥 作者与所属院校
- 作者：Jianxin Bi, Kevin Yuchen Ma, Ce Hao, Mike Zheng Shou, Harold Soh 等
- 机构：新加坡国立大学计算机系、Smart Systems Institute

## 📖 研究背景
- 主流[[视觉-语言-动作模型]]只吃视觉-语言-动作数据，没有触觉通道，接触密集任务受限。
- 视觉难以判断软硬、粗糙度与接触事件；补触觉又缺大规模多模态数据集。
- 该文不微调基座 VLA，在任务规划与动作控制两层外挂触觉，走[[视触融合]]路线。

## ❓ 需要解决的问题
- 不改基座模型，能否把触觉转成语义文本送入高层规划，让模型据此决策？
- 触觉能否作为条件精修 VLA 输出的动作块，提升接触精度与力控制？
- 规划层与控制层触觉各自贡献多少，去掉其一会退化多少？

## 📥📤 输入与输出
- 输入：RGB 图像、[[GelSight]][[触觉图像]]（10 Hz）、语言指令；基座为 RDT 策略。
- 输出：扩散/插值控制器精修后的动作块（8 Hz 执行）、抓取与放置决策、接触力调节量。

## ✅ 论文最终达到的效果
- 相对 RDT 基座，任务成功率提升 42%（叠杯）、140%（擦洗）、67%（削皮）。
- 相对 LSTM 残差控制器提升 67%、100%、42%，说明多峰动作分布建模更关键。
- 去掉规划层触觉，成功率降 44%/58%/14%；去掉控制层触觉降 33%/58%/43%。
- 仅把触觉写成语言描述，GPT-4o 力判断由 50% 升至 90%，硬度判断由 60% 升至 75%。
- 具体计数：擦洗完整完成 12/20、削皮 10/20、叠杯放置 10/20。

## 🔗 关联
- [[3D-ViTac Learning Fine-Grained Manipulation with Visuo-Tactile Sensing]]
- [[N0-VTLA Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens]]
- [[OmniVTLA Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing]]

## 🏷️ 标签
#视触融合 #视觉-语言-动作模型 #触觉感知 #扩散策略
