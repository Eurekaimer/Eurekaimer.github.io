# 层次分析法(AHP)
The analytic hierarchy process(AHP)

## 基本概念

层次分析法（AHP）：首先将问题变得条理化、层次化，构造出一个有层次的结构模型
+ 最高层（目标层） 预定目标或理想结果
+ 中间层（准则层） 目标所设计的中间环节
+ 最底层（方案层） 实现目标的措施和决策方案

基本步骤：
+ 建立层次结构模型
+ 构造出判断矩阵
+ 一致性检验
+ 求权重后评分

**给出评价指标--分配权重--得出分数--根据分数进行判断**

得到指标的方式-知网或其他论文网站（in Google）


## 模型建立

### 构造判断矩阵

+ 对指标的重要程度进行比较 构造**判断矩阵**$a_{ij}$的意义是第$i$个指标相对于第$j$个指标的重要程度
+ 主要是判断矩阵
	+ 正互反矩阵（满足对称位置互为倒数）
	+ 一致性 $a_{ki}=a_{kj}\cdot a_{ji}$
	+ 行列倍数关系
		+ 证明思路：归纳法即可 利用一致性 并且可以推出2阶情形


REMARK： 指标过多时不容易证明
+ 一致矩阵的秩一定是1
+ 对称位置的值应该互为倒数


### 一致性检验

1. 计算一致性指标CI $CI= \frac{\lambda_{max}-n}{n-1}$ 
2. 查找平均随机一致性指标RI
3. 计算一致性比例CR


### 求权重

+ 算术平均法
+ 几何平均法
+ 特征值法


## 基本的分析步骤

1. 建立层次结构图 加入**该图片** SmartArt
2. 构造判断矩阵（找到参量） 主观评价
3. 计算权重并进行一致性检验
	1. 算术平均法
	2. 几何平均法
	3. 特征值法
最好三种都进行，以提高模型的稳健性
+ 计算一致性指标CI
+ 查找对应的平均随机一致性指标RI
+ 计算一致性比例CR CR=CI/RI
	+ 若CR<0.1 则认为判断矩阵的一致性可以接受 否则需要修正

如何修正 往一致矩阵上调整


缺点：决策性不能太多 一致性会受到影响
平均随机一致性指标表格中n最多到15

+ 目标层
+ 准则层
+ 方案层

