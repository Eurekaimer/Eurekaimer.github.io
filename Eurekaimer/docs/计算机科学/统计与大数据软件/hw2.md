# hw2

## Problem 1 熟食店

### 创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；


```python
sandwich_orders = ["chicken sandwich", "vegetable sandwich", "beef sandwich", "salmon sandwich", "tuna sandwich"]
```

### 再创建一个名为finished_sandwiches 的空列表。


```python
finished_sandwiches = [ ]
```

### 遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich，并将其移到列表finished_sandwiches。


```python
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)
```

    I made your chicken sandwich
    I made your vegetable sandwich
    I made your beef sandwich
    I made your salmon sandwich
    I made your tuna sandwich


### 所有三明治都制作好后，打印一条消息，将这些三明治列出来。


```python
print(finished_sandwiches)
```

    ['chicken sandwich', 'vegetable sandwich', 'beef sandwich', 'salmon sandwich', 'tuna sandwich']


## Problem 2 五香烟熏牛肉（pastrami）卖完了

### 与1相似，创建列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。


```python
sandwich_orders = ["chicken sandwich", "pastrami", "vegetable sandwich", "pastrami", "beef sandwich", "salmon sandwich", "pastrami", "tuna sandwich"]
```

### 在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了;


```python
print("熟食店的五香烟熏牛肉卖完了")
```

    熟食店的五香烟熏牛肉卖完了


### 再使用一个while 循环将列表sandwich_orders 中的'pastrami'都删除。


```python
print("熟食店的五香烟熏牛肉卖完了")
sandwich_orders = ["chicken sandwich", "pastrami", "vegetable sandwich", "pastrami", "beef sandwich", "salmon sandwich", "pastrami", "tuna sandwich"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
```

    熟食店的五香烟熏牛肉卖完了


### 确认最终的列表finished_sandwiches 中不包含'pastrami'。


```python
finished_sandwiches = [ ]
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
```

    ['chicken sandwich', 'vegetable sandwich', 'beef sandwich', 'salmon sandwich', 'tuna sandwich']


## Problem 3 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地

### 使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。


```python
# 存储调查结果的字典
survey_results = {}

while True:
    # 获取用户姓名
    name = input("请输入你的姓名（输入 'quit' 退出调查）：")
    # 不区分大小写以免多次输入
    if name.lower() == "quit":
        break
    # 提示用户输入梦想的度假胜地
    destination = input("If you could visit one place in the world, where would you go? ")
    # 将用户的调查结果存入字典
    survey_results[name] = destination

# 打印调查结果
print("\n--- survey results ---")
for name, destination in survey_results.items():
    print(f"{name} 梦想的度假胜地是 {destination}")
```

    请输入你的姓名（输入 'quit' 退出调查）： quit


​    
​    --- 调查结果 ---


## Problem 4 大饼卷一切：编写一个函数，它接受顾客要在大饼中添加的一系列食材

### 这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的大饼卷一切进行概述。调用这个函数三次，每次都提供不同数量的实参。


```python
def all_ingredients(*ingredients):
    # 形参名*ingredients中的星号让Python创建一个名为ingredients的空元组，并将收到的所有值都封装到这个元组中。
    # 对顾客点的大饼卷一切进行概述
    print("该顾客点的大饼卷一切包含以下食材：")
    for ingredient in ingredients:
        print(f"+ {ingredient}")
    # 换行隔开
    print()

# 调用三次
# 两个实参
all_ingredients("生菜", "火腿")
# 三个实参
all_ingredients("生菜", "鸡蛋", "火腿")
# 四个实参
all_ingredients("生菜", "鸡蛋", "火腿", "番茄酱")
```

    该顾客点的大饼卷一切包含以下食材：
    + 生菜
    + 火腿
    
    该顾客点的大饼卷一切包含以下食材：
    + 生菜
    + 鸡蛋
    + 火腿
    
    该顾客点的大饼卷一切包含以下食材：
    + 生菜
    + 鸡蛋
    + 火腿
    + 番茄酱


​    

## Problem 5 同学：编写一个函数，将班级同学的信息存储在一个字典中。

### 这个函数总是接受姓名和学号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，以及两个名称—值对。这个函数必须能够像下面这样进行调用：car = classmate('Li', 'Lei', gender='male', age=18)打印返回的字典，确认正确地处理了所有的信息。


```python
def classmate(name, number, **others_info):
# 形参**others_info中的两个星号让Python创建一个名为others_info的空字典，并将收到的所有名称—值对都封装到这个字典中
    # 建立空字典
    allinfo = {}
    # 必要元素
    allinfo["name"] = name
    allinfo["number"] = number
    # 将任意数量关键字参数添加到字典中
    for key, value in others_info.items():
        allinfo[key] = value
    return allinfo

# 调用函数
car = classmate("Li Lei", "2313915x", gender = "male", age = 18)

# 打印返回的字典
print(car)
```

    {'name': 'Li Lei', 'number': '2313915x', 'gender': 'male', 'age': 18}

