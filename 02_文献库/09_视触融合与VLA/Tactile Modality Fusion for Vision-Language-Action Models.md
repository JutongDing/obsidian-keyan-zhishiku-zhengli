---
title: Tactile Modality Fusion for Vision-Language-Action Models
year: 2026
doi: 
arxiv: 2603.14604
key: KB-145
venue: arXiv preprint（会议论文格式，发表信息待核对）
theme: 02_文献库/09_视触融合与VLA
tags: [视觉-语言-动作模型, 视触融合, 触觉反馈, 轴孔装配]
pdf: ../../../Tactile Modality Fusion for Vision-Language-Action Models.pdf
confidence: high
source: pdf
aliases: []
---

# Tactile Modality Fusion for Vision-Language-Action Models

## 📌 年份
2026

## 🔑 论文识别码
arXiv:2603.14604（无 DOI）

## 👥 作者与所属院校
- 作者：Charlotte Morissette, Amin Abyaneh, Wei-Di Chang, Anas Houssaini, David Meger 等
- 机构：麦吉尔大学、Mila 魁北克人工智能研究所、英伟达

## 📖 研究背景
- [[视觉-语言-动作模型]]（VLA）具备语义泛化能力，但几乎只依赖视觉，接触丰富任务中遮挡与毫米级调整使其失效。
- 触觉能提供接触力、表面摩擦、柔顺与剪切信息，是视觉在接触阶段的关键补充。
- 既有触觉 VLA 多靠 token 拼接或大规模多模态预训练，序列变长、算力开销大且易随上下文增长退化。
- 该文提出 TacFiLM：在后训练微调阶段用特征级线性调制（FiLM）以触觉表征条件化中间视觉特征。

## ❓ 需要解决的问题
- 不做大规模多模态预训练，能否在已预训练 VLA 上轻量注入触觉信号？
- 特征级 FiLM 条件化相比 token 拼接、交叉注意力，在成功率、直插率与力稳定性上是否更优？
- 不同预训练触觉编码器（T3、Sparsh 变体）对下游策略性能影响多大？
- 在小间隙插入、线缆插接与抽屉拉开等分布外任务上能否保持低接触力与短耗时？

## 📥📤 输入与输出
- 输入：腕部相机图像、间隔 5 帧的两帧触觉图像、语言指令、本体状态。
- 输出：OpenVLA-OFT 动作头的末端动作增量；按分布内 30 次、分布外 15 次 rollout 评测。

## ✅ 论文最终达到的效果
- 3 mm 圆销插入：成功率 100%、直插率 36.67%、峰值力 7.64 N、耗时 52.03 s。
- 同任务基线 OpenVLA-OFT 为 86.67%/3.33%/14.94 N/92.24 s，token 拼接为 96.67%/16.67%/9.19 N/75.11 s。
- 2 mm 小间隙与 HDMI 插线任务上成功率与直插率仍最高，峰值力与耗时最低；拼接法在 2 mm 时力显著升高。
- 遮挡测试（亮度降 80%、帧率减半）下仍保持 100% 成功率，纯视觉基线降至 73.33%。
- 触觉编码器评测中 Sparsh-DINO 最优（平均分类 97.72%、力回归 RMSE 36.09），被选为触觉骨干。

## 🔗 关联
- [[VLA-Touch Enhancing Vision-Language-Action Models with Dual-Level Tactile Feedback]]
- [[3D-ViTac Learning Fine-Grained Manipulation with Visuo-Tactile Sensing]]
- [[N0-VTLA Scaling Vision–Tactile–Language–Action Model with Latent Tactile Tokens]]

## 🏷️ 标签
#视觉-语言-动作模型 #视触融合 #触觉反馈 #轴孔装配
