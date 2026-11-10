---
title: "UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy"
year: 2023
doi: 
arxiv: 2303.00938
key: KB-156
venue: CVPR 2023（IEEE/CVF 计算机视觉与模式识别会议；PDF 为 arXiv v2，2023-03）
theme: 02_文献库/08_学习与强化学习
tags: [灵巧抓取, 抓取位姿生成, 强化学习, 教师学生蒸馏, 点云]
pdf: ../../../UniDexGrasp.pdf
confidence: high
source: pdf
aliases: []
---

# UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy

## 📌 年份
2023

## 🔑 论文识别码
arXiv:2303.00938（PDF 未印 DOI）

## 👥 作者与所属院校
- 作者：Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Shan 等（共 13 人，前四位同等贡献）
- 机构：北京大学（前沿计算研究中心、信息科学技术学院）、北京通用人工智能研究院、斯坦福大学、清华大学

## 📖 研究背景
- 平行夹爪抓取在未知物体上成功率已很高，但抓取方式单一，难以支撑功能性操作。
- [[灵巧手]]动作空间维度高，直接从视觉输入学抓取策略样本效率低、跨类别泛化差。
- 已有 CVAE 联合建模旋转、平移与关节角易模式坍缩，生成不了多样抓取。
- 该文沿用夹爪的成功范式，把任务拆为"抓取位姿生成"与"目标条件执行"两阶段。

## ❓ 需要解决的问题
- 如何在 SO(3) 旋转与欧氏平移/关节角构成的乘积空间上，训练不坍缩的条件生成模型？
- 只用真实可得的点云输入的学生策略，能否保住特权教师策略的成功率？
- 在未见物体实例与未见类别上，成功率相对训练集下降多少？
- 生成的目标位姿作为条件，策略能否按指定方式完成抓取而非随便抓住？

## 📥📤 输入与输出
- 输入：桌面场景下物体单视角点云（学生策略）；教师策略另用物体位姿、接触等特权状态。
- 输出：[[抓取位姿]]（手根旋转、平移、关节角）；执行阶段输出手部关节目标动作序列。

## ✅ 论文最终达到的效果
- 自建数据集含 133 个类别、3251 个训练实例，覆盖数千物体实例的桌面抓取任务。
- 状态策略平均成功率 74%（训练集）/69%（测试集），基线 PPO 14%、DAPG 13%、ILAD 25%。
- 视觉策略平均成功率超过 60%，蒸馏到学生策略后仅下降约 6%–7%。
- 生成模型把旋转（GraspIPDF）与平移+关节角（GraspGlow）解耦，配合测试时适配产出可行位姿。
- 消融显示状态规范化、物体课程学习、教师学生蒸馏三项技术各自贡献显著。

## 🔗 关联
- [[Cross-Embodiment Dexterous Grasping with Reinforcement Learning]]
- [[Robust Dexterous Grasping of General Objects]]
- [[FunGrasp Functional Grasping for Diverse Dexterous Hands]]

## 🏷️ 标签
#灵巧抓取 #抓取位姿生成 #强化学习 #教师学生蒸馏 #点云
