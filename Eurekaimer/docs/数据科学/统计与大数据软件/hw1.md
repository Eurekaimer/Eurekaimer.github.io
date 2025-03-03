---
comments: true
tags:
    - Python
---
# hw1


## Problem 1 安装anaconda


已安装


## Problem 2 把今天上课讲的变量类型在jupyter上进行练习。


### 字符串

#### 表示方法


```python
"A string" 
# or 'A string' 
```




    'A string'



#### 函数


```python
string_test='nankai university'
print(string_test.title())
print(string_test.upper())
print(string_test.lower())
```

    Nankai University
    NANKAI UNIVERSITY
    nankai university
    

#### 特殊字符


```python
print("Math:\n\tAnalysis\n\tAlgebra\n\tGeometry")
```

    Math:
    	Analysis
    	Algebra
    	Geometry
    


```python
print(r"Math:\n\tAnalysis\n\tAlgebra\n\tGeometry")
```

    Math:\n\tAnalysis\n\tAlgebra\n\tGeometry
    

#### 输出


```python
message_test = "I have finished my homework"
print(message_test)
```

    I have finished my homework
    

#### 合并字符串


```python
test_subject = "I"
test_verb = "Love"
test_object = "Mathematical Statistics"
sentence = test_subject + " " + test_verb + " " + test_object
print(sentence)
```

    I Love Mathematical Statistics
    


```python
print(test_object[0])
print(test_object[0:4])
print(test_object[::3])
```

    M
    Math
    Mhac asc
    

### 整型和浮点型


```python
print(5+3)
print(5/3)
print(5//3)
print(5**3)
print(3*0.2)
print(5*0.3)
```

    8
    1.6666666666666667
    1
    125
    0.6000000000000001
    1.5
    

### 布尔值


```python
a = True
b = False
print("a", a, "b", b)
```

    a True b False
    

### 列表

#### 初始化和输出


```python
Travel = ["Tokyo", "New York", "Takayama", "Luo Yang", "Xi An"]
print(Travel)
print(Travel[2])
print(Travel[-2])
print(Travel[1:3])

```

    ['Tokyo', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    Takayama
    Luo Yang
    ['New York', 'Takayama']
    

#### 修改、添加和删除元素


```python
Travel[0] = "Beijing"
print(Travel)
Travel.append("Tianjin")
print(Travel)
Travel.insert(2, "Tianjin")
print(Travel)
del Travel[2]
print(Travel)
Travel.pop()
print(Travel)
Travel.remove("Xi An")
print(Travel)
last_word = Travel.pop()
print("The last word is " + last_word)
```

    ['Beijing', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    ['Beijing', 'New York', 'Takayama', 'Luo Yang', 'Xi An', 'Tianjin']
    ['Beijing', 'New York', 'Tianjin', 'Takayama', 'Luo Yang', 'Xi An', 'Tianjin']
    ['Beijing', 'New York', 'Takayama', 'Luo Yang', 'Xi An', 'Tianjin']
    ['Beijing', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    ['Beijing', 'New York', 'Takayama', 'Luo Yang']
    The last word is Luo Yang
    

#### 排序


```python
Travel.sort()
print(Travel)
Travel.sort(reverse = True)
print(Travel)
print(sorted(Travel))
```

    ['Beijing', 'New York', 'Takayama']
    ['Takayama', 'New York', 'Beijing']
    ['Beijing', 'New York', 'Takayama']
    


```python
Travel.reverse()
print(Travel)
print(len(Travel))
additional_list = ["Tianjin", "Hong Kong"]
print(Travel + additional_list)
```

    ['Beijing', 'New York', 'Takayama']
    3
    ['Beijing', 'New York', 'Takayama', 'Tianjin', 'Hong Kong']
    

### 元组


```python
tuple = (1919, 1895)
print(tuple)
tuple = (1895, 1919) 
print(tuple)
```

    (1919, 1895)
    (1895, 1919)
    


```python
demo = (250, [1, 2], 100)
demo[1].append(3)
print(demo)
```

    (250, [1, 2, 3], 100)
    


```python
a = [1, 2, 3]
b = 4, 5, 6
a1, a2, a3 = a
print(a1, a2, a3)
a1, a2, a3 = b
print(a1, a2, a3)
a1, a2, a3 = a2, a3, a1
print(a1, a2, a3)
```

    1 2 3
    4 5 6
    5 6 4
    

## Problem 3 放眼世界：想出至少5 个你渴望去旅游的地方。

Data = Tokyo, New York, Takayama, Luo Yang, Xi An

#### 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。


```python
Travel=["Tokyo", "New York", "Takayama", "Luo Yang", "Xi An"]
```

#### 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python 列表。


```python
print(Travel)
```

    ['Tokyo', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    

#### 用sorted()按字母顺序打印这个列表，同时不要修改它。


```python
print(sorted(Travel))
```

    ['Luo Yang', 'New York', 'Takayama', 'Tokyo', 'Xi An']
    

#### 再次打印该列表，核实排列顺序未变。


```python
print(Travel)
```

    ['Tokyo', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    

#### 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。


```python
print(sorted(Travel, reverse = True))
```

    ['Xi An', 'Tokyo', 'Takayama', 'New York', 'Luo Yang']
    

#### 再次打印该列表，核实排列顺序未变。


```python
print(Travel)
```

    ['Tokyo', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    

#### 使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。


```python
Travel.reverse()
print(Travel)
```

    ['Xi An', 'Luo Yang', 'Takayama', 'New York', 'Tokyo']
    

#### 使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。


```python
Travel.reverse()
print(Travel)
```

    ['Tokyo', 'New York', 'Takayama', 'Luo Yang', 'Xi An']
    

#### 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。


```python
Travel.sort()
print(Travel)
```

    ['Luo Yang', 'New York', 'Takayama', 'Tokyo', 'Xi An']
    

#### 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。


```python
Travel.sort(reverse = True)
print(Travel)
```

    ['Xi An', 'Tokyo', 'Takayama', 'New York', 'Luo Yang']
    
