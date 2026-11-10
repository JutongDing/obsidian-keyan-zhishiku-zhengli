---
title: High Speed and High Sensitivity Slip Sensor for Dexterous Grasping
year: 2012
doi: 10.20965/jrm.2012.p0298
arxiv: 
key: KB-072
venue: Journal of Robotics and Mechatronics（Vol.24 No.2）
theme: 02_文献库/02_触觉感知与传感
tags: [滑移传感, 压敏导电橡胶, 小波变换, 抓取力控制, 灵巧手]
pdf: ../../../High Speed and High Sensitivity Slip Sensor for Dexterous Grasping.pdf
confidence: high
source: pdf
aliases: []
---

# High Speed and High Sensitivity Slip Sensor for Dexterous Grasping

## 📌 年份
2012（JRM 第 24 卷第 2 期；2011-11-09 录用）

## 🔑 论文识别码
DOI: 10.20965/jrm.2012.p0298

## 👥 作者与所属院校
- 作者：Seiichi Teshigawara, Takahiro Tsutsumi, Yosuke Suzuki, Makoto Shimojo
- 机构：日本电气通信大学机械工程与智能系统系、横河 DCS 硬件开发部

## 📖 研究背景
- 家庭与护理机器人须按物体形状、质量、摩擦系数调节握力，多指[[灵巧手]]离不开触觉[[滑移检测]]闭环。
- 既有 PVDF、CoP 方案结构厚（覆盖层约 3 mm）、布线与信号处理复杂，难以分离手部振动与真实滑移。
- 压敏导电橡胶薄而廉价，但电阻变化同时受法向力影响，单靠幅值无法判滑移。
- 该文从频域切入：滑移前数 kHz 以上高频分量可作为判据。

## ❓ 需要解决的问题
- 压敏导电橡胶的剪切变形是否产生可区别于法向力变化的高频电阻变化？
- 握力增减与[[初始滑移]]能否在同一通道上分离？
- 传感器能否做得薄、小、少线并装入机器人指端？
- 检出滑移后能否闭环[[抓取力调节]]，逼近最小握力又不掉物？

## 📥📤 输入与输出
- 输入：指端电极间电压（压敏导电橡胶电阻变化），10–50 kHz 采样。
- 输出：滑移/静止判别（离散小波系数阈值）、握力增减指令与指关节动作。

## ✅ 论文最终达到的效果
- 传感器厚 0.5 mm、最小 2 mm×2 mm、仅 2 根引线、响应约 1 ms。
- 小波系数峰值（×10⁻⁶）：滑移 700（圆柱）/1100（方柱），握力变化 25，静止 4，可区分。
- 滑移位移前 3–11 ms 报警：0.272 s vs 0.283 s、0.922 s vs 0.925 s。
- 指端安装后以杯内加颗粒三档质量验证，握力收敛至接近最小握力（定性结论）。

## 🔗 关联
- [[Development of Intelligent Robot Hand using Proximity, Contact and Slip sensing]]
- [[Finger contact sensing and the application in dexterous hand manipulation]]
- [[All the Feels A Dexterous Hand With Large-Area Tactile Sensing]]

## 🏷️ 标签
#滑移传感 #压敏导电橡胶 #小波变换 #抓取力控制 #灵巧手
