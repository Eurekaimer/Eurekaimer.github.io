# hw6

## Problem 1

如果有dataframe df = pd.DataFrame( {'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]} ), 那么对于列X的每一个值，计算相对于离其最近的(前面的？)0的相对位置（如果前面没有0，则计算从头开始的位置），这样就会得到[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]，我们可以把它作为df的新的列'Y'.  

问题：让用户输入任意一列整数，构造新的dataframe，以此列整数为列X，并按照上述方法计算新的列Y。


```python
# 使用pandas 定义一个函数处理这个过程
import pandas as pd

def calculate(input_list):
    df = pd.DataFrame({'X': input_list})
    y = []
    last_zero = -1
    for i, value in enumerate(df['X']):
        # 找出0的位置并更新
        # 判断0
        if value == 0:
            last_zero = i
            y.append(0)
        else:
            # 没有零那么就是后面的坐标加1
            if last_zero == -1:
                y.append(i + 1)
            else:
                y.append(i - last_zero)
    df['Y'] = y
    return df


input_str = input("请输入一列整数，用空格隔开: ")
# 去除末尾空格以免错误输入报错
input_str = input_str.strip()
input_list = [int(x) for x in input_str.split(' ')]
result_df = calculate(input_list)
print(result_df)
    
```

    请输入一列整数，用空格隔开: 2 0 2 2 2 0 2 2 2 2 2 2 2 0
        X  Y
    0   2  1
    1   0  0
    2   2  1
    3   2  2
    4   2  3
    5   0  0
    6   2  1
    7   2  2
    8   2  3
    9   2  4
    10  2  5
    11  2  6
    12  2  7
    13  0  0


## Problem 2

滑动平均：给定dataframe包含两列，一列为group，一列为value，

例如 df = pd.DataFrame({'group': list('aabbabbbabab'), 'value': [1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8]})

请根据group的进行滑动平均，自己定义窗口尺寸，如遇到nan请忽略（注意不是作为0处理，是忽略）。例如上边的例子结果应为（窗口长度为3）：

0     1.000000

1     1.500000

2     3.000000

3     3.000000

4     1.666667

5     3.000000

6     3.000000

7     2.000000

8     3.666667

9     2.000000

10    4.500000

11    4.000000


```python
import pandas as pd
import numpy as np

# 让用户输入 group 数据
group_input = input("请输入 group 数据不用任何符号分隔（例如：aabbabbbabab）：")
# 直接将字符串转换为列表
group_data = list(group_input)

# 让用户输入 value 数据
value_input = input("请输入 value 数据，用逗号分隔，若为缺失值请输入np.nan（例如：1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8）：")
value_data = [np.nan if val.strip() == 'np.nan' else float(val) for val in value_input.split(',')]

# 创建示例 DataFrame
df = pd.DataFrame({'group': group_data, 'value': value_data})

window_size = 3

# 按组进行滚动平均计算，忽略 NaN
result = df.groupby('group')['value'].rolling(
    window=window_size, min_periods=1).mean()

# 重置索引并按原始顺序排序
result = result.reset_index(0, drop=True).sort_index()

print(result)
```

    请输入 group 数据不用任何符号分隔（例如：aabbabbbabab）：aabbabbbabab
    请输入 value 数据，用逗号分隔，若为缺失值请输入np.nan（例如：1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8）：1, 2, 3, np.nan, 2, 3, np.nan, 1, 7, 3, np.nan, 8
    0     1.000000
    1     1.500000
    2     3.000000
    3     3.000000
    4     1.666667
    5     3.000000
    6     3.000000
    7     2.000000
    8     3.666667
    9     2.000000
    10    4.500000
    11    4.000000
    Name: value, dtype: float64

##  Problem 3

扫雷游戏。创建一个dataframe来模拟扫雷游戏：

(1) 创建一个扫雷游戏，即创建一个dataframe，包含两列X和Y

例如5 * 4的扫雷游戏，这个dataframe分别记录5 * 4个格子的坐标，这个dataframe为两列，20行，它的一部分如下：

\  x  y

0  0  0

1  0  1

2  0  2



```python
import pandas as pd
import numpy as np

# 创建DataFrame
# 定义行列长度
rows = 5
cols = 4
# 也可以自定义
# rows = int(input("请输入扫雷游戏的行数: "))
# cols = int(input("请输入扫雷游戏的列数: "))
# 用坐标表示
coordinates = [(x, y) for x in range(rows) for y in range(cols)]
df = pd.DataFrame(coordinates, columns=['x', 'y'])    
```

（2）增加一列，此列为格子是否为雷，如果是的话值为1，否则为0. （使用随机函数，每个位置为雷的概率为0.4）


```python
probability = 0.4
# 增加一列记为nina
df['nina'] = np.random.choice([1, 0], size=len(df), p=[probability, 1 - probability])
```

（3）再增加一列adjacent，此列记录当前格子相邻的格子的雷的数目，如果当前格子为雷，则值为NaN。


```python
# 定义一下函数
def count_adjacent_nina(row):
    if row['nina'] == 1:
        return np.nan
    x, y = row['x'], row['y']
    adjacent_count = 0
    # 数3 x 3范围内的雷
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            # 确认坐标
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols:
                # 二维坐标到一维索引
                adjacent_index = new_x * cols + new_y
                adjacent_count += df.loc[adjacent_index, 'nina']
    return adjacent_count


df['adjacent'] = df.apply(count_adjacent_nina, axis=1)

```

（4）创建一个新的5行4列的dataframe，其中值为(3)中计算得到的雷的数目。


```python
# 创建新的df
new_df = df['adjacent'].values.reshape(rows, cols)
new_df = pd.DataFrame(new_df)

print("原始的DataFrame:")
print(df)
print("\n新的DataFrame:")
print(new_df)
```

    原始的DataFrame:
        x  y  nina  adjacent
    0   0  0     0       3.0
    1   0  1     1       NaN
    2   0  2     0       3.0
    3   0  3     0       1.0
    4   1  0     1       NaN
    5   1  1     1       NaN
    6   1  2     0       4.0
    7   1  3     1       NaN
    8   2  0     0       4.0
    9   2  1     1       NaN
    10  2  2     0       5.0
    11  2  3     0       2.0
    12  3  0     0       2.0
    13  3  1     1       NaN
    14  3  2     1       NaN
    15  3  3     0       1.0
    16  4  0     0       1.0
    17  4  1     0       2.0
    18  4  2     0       2.0
    19  4  3     0       1.0
    
    新的DataFrame:
         0    1    2    3
    0  3.0  NaN  3.0  1.0
    1  NaN  NaN  4.0  NaN
    2  4.0  NaN  5.0  2.0
    3  2.0  NaN  NaN  1.0
    4  1.0  2.0  2.0  1.0



