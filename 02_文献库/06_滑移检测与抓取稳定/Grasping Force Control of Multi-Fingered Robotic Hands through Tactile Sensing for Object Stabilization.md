---
title: Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization
year: 2020
doi: 10.3390/s20041050
arxiv: 1810.02653
key: KB-064
venue: Sensors
theme: 02_文献库/06_滑移检测与抓取稳定
tags: [触觉传感, 抓取力控制, 滑移检测, 材料识别, Shadow手]
pdf: ../../../Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization.pdf
confidence: high
source: pdf
aliases: []
---

# Grasping Force Control of Multi-Fingered Robotic Hands through Tactile Sensing for Object Stabilization

## 📌 年份
2020（Sensors 第 20 卷第 4 期，1050）

## 🔑 论文识别码
DOI: 10.3390/s20041050

## 👥 作者与所属院校
- 作者：Zhen Deng、Yannick Jonetzko、Liwei Zhang（通讯）、Jianwei Zhang
- 机构：福州大学机械工程及自动化学院、汉堡大学信息学系 TAMS

## 📖 研究背景
- 抓取未知物体时，环境扰动会把原本稳定的抓取推入失稳，需在线维持接触。
- 人类靠触觉在毫秒级调整握力，机器人多指手借触觉做[[抓取力调节]]仍少有完整方案。
- 该文把材料识别、[[滑移检测]]与[[接触力估计]]合成一个触觉闭环框架。

## ❓ 需要解决的问题
- 仅凭指尖触觉时序，能否同时判别接触事件（未接触/接触/滑移）与物体材料？
- 未做力标定时，BioTac 电极阵列能否给出接触力与接触点位置？
- 检出滑移后，如何调整三指接触构型让物体重新稳定而不必知道其质量？

## 📥📤 输入与输出
- 输入：Shadow 五指手三指（拇指、食指、中指）指尖 BioTac 的 19 电极阻抗、压力与温度读数，100 Hz 采样。
- 输出：接触事件与四类材料标签、接触法向力与接触点 x/y 位置、各指关节力矩指令（底层力矩控制器）。

## ✅ 论文最终达到的效果
- 滑移检测测试准确率约 98%，窗口 48、采样 33.3 Hz 时最高 99.0%。
- 材料四分类（纸/泡沫/塑料/金属）准确率约 95%，最优 97.2%；塑料与纸易混。
- 为兼顾实时性取窗口 32、33.3 Hz；检测与估计模块在 2.5 GHz Intel i5 上运行。
- 八种物体各 10 次真机抓取，成功率 95%（76/80），失败集中在金属杯 3 次、薯片罐 1 次。

## 🔗 关联
- [[Slip Detection for Grasp Stabilization With a Multifingered Tactile Robot Hand]]
- [[Force Estimation and Slip Detection for Grip Control using a Biomimetic Tactile Sensor]]
- [[Direction of Slip Detection for Adaptive Grasp Force Control with a Dexterous Robotic Hand]]

## 🏷️ 标签
#触觉传感 #抓取力控制 #滑移检测 #材料识别 #Shadow手
