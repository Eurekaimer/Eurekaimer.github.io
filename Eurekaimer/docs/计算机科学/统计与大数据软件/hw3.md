# hw3

## Problem 1 汽车

### 编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。

这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：

car = make_car('subaru', 'outback', color='blue', tow_package=True)

打印返回的字典，确认正确地处理了所有的信息。


```python
def make_car(manufacturer, model, **other_info):
    """创建包含汽车信息的字典"""
    car_dict = {
        'manufacturer': manufacturer,
        'model': model
    }
    car_dict.update(other_info)  # 添加额外的关键字参数
    return car_dict

# 调用函数并打印结果
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
```

    {'manufacturer': 'subaru', 'model': 'outback', 'color': 'blue', 'tow_package': True}
    

## Problem 2 餐馆

### 创建一个名为Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和cuisine_type。


```python
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
```

### 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。


```python
    def describe_restaurant(self):
        print(f"restaurant_name ：{self.restaurant_name}，cuisine_type：{self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业")
```

### 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


```python
restaurant = Restaurant ("二食堂", "预制菜")
# 打印两个属性
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# 调用两个方法
describe_restaurant(restaurant)
open_restaurant(restaurant)

```

    二食堂
    预制菜
    restaurant_name ：二食堂，cuisine_type：预制菜
    二食堂 正在营业
    

## Problem 3 三家餐馆

### 根据你为完成练习2而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。


```python
# 创建三个实例
restaurant1 = Restaurant("一食堂", "预制菜" )
restaurant2 = Restaurant("二食堂", "预制菜" )
restaurant3 = Restaurant("三食堂", "预制菜" )

# 调用方法
describe_restaurant(restaurant1)
describe_restaurant(restaurant2)
describe_restaurant(restaurant3)
```

    restaurant_name ：一食堂，cuisine_type：预制菜
    restaurant_name ：二食堂，cuisine_type：预制菜
    restaurant_name ：三食堂，cuisine_type：预制菜
    

## Problem 4 用户

### 创建一个名为User 的类，其中包含属性first_name 和last_name，还有用户简介通常会存储的其他几个属性。


```python
class User():
    def __init__(self, first_name, last_name, **other_info):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info     
```

### 在类User 中定义一个名为describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。


```python
    def describe_user(self):
        """打印用户信息摘要"""
        print("用户信息摘要：")
        print(f"first name：{self.first_name}，last name：{self.last_name}")
        for key, value in self.other_info.items():
            print(f"{key}：{value}")
    
    def greet_user(self):
        """向用户发出个性化问候"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"你好(Hello)，{full_name}！欢迎访问！")
```

### 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。


```python
# 创建不同用户实例
user_1 = User("黄", "刚", age = 19, city = "天津") # 中文实例
user_2 = User("Emma", "Wilson", job = "Designer", hobby = "Reading") # 英文实例
user_3 = User("朱", "Peter", language = "Jupyter", work = "Notebook") # 中英混杂实例
 
# 调用方法
describe_user(user_1)
greet_user(user_1)

# 换行隔开
print("\n") 

describe_user(user_2)
greet_user(user_2)

# 换行隔开
print("\n") 

describe_user(user_3)
greet_user(user_3)
```

    用户信息摘要：
    first name：黄，last name：刚
    age：19
    city：天津
    你好(Hello)，黄 刚！欢迎访问！
    
    
    用户信息摘要：
    first name：Emma，last name：Wilson
    job：Designer
    hobby：Reading
    你好(Hello)，Emma Wilson！欢迎访问！
    
    
    用户信息摘要：
    first name：朱，last name：Peter
    language：Jupyter
    work：Notebook
    你好(Hello)，朱 Peter！欢迎访问！
    

## Problem 5 就餐人数

### 在为完成练习2而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。


```python
# 练习2的程序
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

# 实例
restaurant = Restaurant("包子铺", "包子", 10)
print(f"来了{restaurant.number_served}人")

# 修改 再次打印
restaurant.number_served = 100
print(f"来了{restaurant.number_served}人")
```

    来了10人
    来了100人
    

### 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。


```python
    # 添加一个名为set_number_served()的方法，它让你能够设置就餐人数
    def set_number_served(self, num):
        self.number_served = num
        
# 调用这个方法并向它传递一个值，然后再次打印这个值。
set_number_served(restaurant, 200)
print(f"来了，{restaurant.number_served}人")
```

    来了，200人
    

### 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。


```python
    # 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增
    def increment_number_served(self, increment_number):
        self.number_served += increment_number

# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数
increment_number_served(restaurant, 900)
print(f"现在来了，{restaurant.number_served}人")
```

    现在来了，1100人
    

## Problem 6 尝试登录次数

### 在为完成 练习4 而编写的 User 类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts()的方法，它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts()的方法，它将属性login_attempts 的值重置为0。


```python
# 练习4编写的 User 类
class User():
    def __init__(self, first_name, last_name, login_attempts = 0, **other_info):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.other_info = other_info  
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
```

### 根据User 类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，并再次打印属性login_attempts 的值，确认它被重置为0。


```python
user_4 = User("Huang", "gang", age = 19, city = "TJ")

# 多次调用
for i in range(0,5):
    user_4.increment_login_attempts()
    print(f"尝试登陆次数，{user_4.login_attempts}")

# 重置登录次数
user_4.reset_login_attempts()
print(f"重置后登陆次数，{user_4.login_attempts}")
```

    尝试登陆次数，1
    尝试登陆次数，2
    尝试登陆次数，3
    尝试登陆次数，4
    尝试登陆次数，5
    重置后登陆次数，0
    


```python

```
