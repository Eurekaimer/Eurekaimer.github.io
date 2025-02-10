# Topsis法

Topsis法（Technique for Order Perference by Similarity to Ideal Solution）

## 基本概念

对比层次分析法: 层次分析法的缺点在于决策层不能太多，而且构造判断矩阵相对主观，所以我们对它进行改进得到Topsis法。

国内也称为**优劣解距离法**：也就是**利用与理想解的距离**进行判断选择

模型原理：一种理想目标相似性顺序选优技术，在多目标决策分析中是一种有效的方法

### 评分算法

构造一个评分$\frac{x-min}{max-min}$ 进行归一化 前提是存在最小值和最大值 否则可以考虑使用样本的数据。

### 数据分类

+ 越大越好的指标是极大型指标
+ 否则是极小型指标

统一指标的类型 **指标正向化**（转化为极大型）

### 矩阵处理

+ 原始矩阵
+ 正向矩阵
+ 标准矩阵

## 模型建立

### 原始矩阵正向化

+ 极大型指标
+ 极小型指标
	+ $\dot{x}=max-x$
+ 中间型指标
	+ $M=max\left\{ \lvert x_{i}-x_{best} \rvert \right\},\dot{x_{i}}=1- \frac{\lvert x_{i}-x_{best} \rvert}{M}$
+ 区间型指标
	+ 最优区间为$\left[ a,b \right]$
	+ $M=max\left\{ a-min\left\{ x_{i} \right\},max\left\{ x_{i}\right\}-b \right\}$



### 正向矩阵标准化

若将正向化矩阵记为$X_{n\times m}$,有n个要评价的对象，m个评价指标，将标准化矩阵记为$Z,z_{ij}=\frac{x_{ij}}{\sqrt{ \sum\limits_{i=1}^{n}x_{ij}^{2} }}$

$\frac{x-min}{max-min}=\frac{x-min}{max-x+x-min}$ 也就是与最小值的距离除以与最大值的距离和最小值的距离

### 计算得分并归一化

$Z^{+}=\left( Z_{1}^{+},Z_{2}^{+},\dots,Z_{m}^{+} \right),Z_{1}^{+}=max\left( z_{11},z_{21},\dots,z_{n_{1}} \right)$

$Z^{-}=\left( Z_{1}^{-},Z_{2}^{-},\dots,Z_{m}^{-} \right),Z_{1}^{-}=min\left( z_{11},z_{21},\dots,z_{n_{1}} \right)$

$D_{i}^{+}=\sqrt{ \sum\limits_{j=1}^{m}\left( Z_{j}^{+}-z_{ij} \right)^{2} }$  $D_{i}^{-}=\sqrt{ \sum\limits_{j=1}^{m}\left( Z_{j}^{-}-z_{ij} \right)^{2} }$

$$
S_{i}=\frac{D_{i}^{-}}{D_{i}^{{-}}+D_{i}^{+}}
$$


或者计算百分制得分



## 总结

这个算法与层次分析法有很大的相似处 并且都主要使用了矩阵计算和矩阵的处理。

但是可以对指标较大的数据进行处理弥补了不分层次分析法的不足。



这里有一个拓展部分 [[基于熵权法对Topsis模型的修正]]






