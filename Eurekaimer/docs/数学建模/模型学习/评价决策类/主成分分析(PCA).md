# 主成分分析(PCA)

## 基本概念

问题提出：简化变量

目标：用较少的新变量代替原来较多的旧变量，并且**尽可能多的保留原本变量所反映的信息**？

REMARK： 数学上的求极大无关组？

### 数据降维

去除噪声和不重要的特征，可以接受一定量的信息损失 

+ 换特征
+ 减少特征

几何意义是旋转坐标系，正比例函数改为坐标轴，那样就可以使用一个变量控制

### 分析原理

对于大多数情况，各个变量基本服从于正态分布（中心极限定理？），所以变量为2的数据散点分布大致为一个椭圆，可以在多元统计中找到。

代数意义：找到一个低阶的投影矩阵，代替原本的信息矩阵。


## 建立模型

### 标准化处理


### 计算协方差矩阵


### 计算特征值和特征向量


### 计算贡献率以及累计贡献率


### 写出主成分


### 根据系数分析主成分代表的意义


### 做后续分析


感觉上可以作为一个思想进行应用 对于大数据类均可以使用

解释主成分才是比较困难的，需要能够较好地解释那些主成分（带有一些模糊性）

优势是维数降低了，除非能够大大地降低维数，否则不应该采用。

































