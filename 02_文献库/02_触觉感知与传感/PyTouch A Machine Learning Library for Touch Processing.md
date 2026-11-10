---
title: "PyTouch: A Machine Learning Library for Touch Processing"
year: 2021
doi: 
arxiv: 2105.12791
key: KB-113
venue: IEEE International Conference on Robotics and Automation (ICRA) 2021（待核对）
theme: 02_文献库/02_触觉感知与传感
tags: [触觉处理库, 触觉检测, 滑移检测, 迁移学习, 开源软件]
pdf: ../../../PyTouch A Machine Learning Library for Touch Processing.pdf
confidence: high
source: pdf
aliases: []
---

# PyTouch: A Machine Learning Library for Touch Processing

## 📌 年份
2021

## 🔑 论文识别码
arXiv: 2105.12791（无 DOI；本地编号 KB-113）

## 👥 作者与所属院校
- 作者：Mike Lambeta、Huazhe Xu、Jingwei Xu、Po-Wei Chou、Shaoxiong Wang 等
- 机构：Facebook AI Research（Menlo Park）、加州大学伯克利分校、上海交通大学

## 📖 研究背景
- 新型触觉传感器越来越丰富，却缺少统一的触觉处理软件，各团队各自重复写预处理、训练与推理代码。
- 视觉领域有 PyTorch、CAFFE、OpenCV 降低门槛，触觉缺少对应的基础设施与统一接口。
- 该文开源 PyTouch，把触觉检测、[[滑移检测]]、物体位姿估计、接触区域估计封装为可复用模块与预训练模型。

## ❓ 需要解决的问题
- 如何用统一接口屏蔽不同视触觉传感器的差异（DIGIT、OmniTact、GelSight）？
- 单传感器模型与多传感器联合训练模型，精度差多少；数据量增加时如何变化？
- 换用新传感器时，仅用少量数据微调能否接近全量训练精度？

## 📥📤 输入与输出
- 输入：原始[[触觉图像]]帧（归一化后下采样到 64×64，可选用 12 帧或 128 帧序列）。
- 输出：接触/非接触与滑移/非滑移二分类、物体位姿、接触区域估计等高层信号。

## ✅ 论文最终达到的效果
- 触觉检测（5 折交叉验证）：联合模型 96.2%（[[DIGIT]]）、99.5%（OmniTact）、98.3%（[[GelSight]]），优于各单传感器模型。
- 滑移检测：ResNet-18 在按序列划分时 97.9%、按物体划分时 96.3%；3D 卷积仅 91.7% / 81.2%，作者归因于滑移速度方差大。
- 迁移到新传感器时只要 10%–50% 数据微调，验证精度可维持约 90%。
- 采用 Hydra 配置、模型下载即用的「触觉处理即服务」设计，代码开源（facebookresearch/pytouch）。

## 🔗 关联
- [[DIGIT A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation]]
- [[GelSlim A High-Resolution, Compact, Robust, and Calibrated Tactile-sensing Finger]]
- [[Learning to Detect Slip with Barometric Tactile Sensors and a Temporal Convolutional Neural Network]]

## 🏷️ 标签
#触觉处理库 #触觉检测 #滑移检测 #迁移学习
