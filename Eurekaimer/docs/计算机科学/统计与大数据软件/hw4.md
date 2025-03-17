# hw4


## Problem 1 冰淇淋小店


### 冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类


让它继承你为完成第三次作业练习2 或练习5 而编写的Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。


### 添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。


### 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，并调用这个方法。


```python
# hw3中练习2的类：
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"restaurant_name ：{self.restaurant_name}，cuisine_type：{self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业")
        
# 编写新的名为IceCreamStand的类
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        # 继承父类
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def show_flavors(self):
        print(f"各种品味的冰淇淋：")
        for flavor in self.flavors:
            print(f"+ {flavor}")

# 创建实例并调用方法

bingqiling = IceCreamStand("bingqilingdian", "IceCream", ["草莓味冰淇淋", "香草味冰淇淋", "巧克力味冰淇淋"])
bingqiling.show_flavors()
```

    各种品味的冰淇淋：
    + 草莓味冰淇淋
    + 香草味冰淇淋
    + 巧克力味冰淇淋
    

## Problem 2 管理员


### 管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成第三次作业中练习4 或练习6 而编写的User 类。


### 添加一个名为privileges 的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。


### 编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。


```python
# hw3中练习4的类：
class User():
    def __init__(self, first_name, last_name, **other_info):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info    
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
    
# 编写新的Admin类
class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        # 继承父类
        super().__init__(first_name, last_name)
        self.privileges = privileges
    def show_privileges(self):
        print(f"{self.first_name} {self.last_name}，你拥有管理员权限如下")
        for privilege in self.privileges:
            print(f"+ {privilege}")
        
# 创建实例并调用方法
administer = Admin("zg", "Huang", ["can add post", "can delete post", "can ban user"])
administer.show_privileges()
```

    zg Huang，你拥有管理员权限如下
    + can add post
    + can delete post
    + can ban user
    

## Problem 3 权限


### 编写一个名为Privileges 的类，它只有一个属性——privileges，其中存储了练习2所说的字符串列表。


### 将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges 实例用作其属性。


### 创建一个Admin 实例，并使用方法show_privileges()来显示其权限。


```python
# 原本的User类
class User():
    def __init__(self, first_name, last_name, **other_info):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info    
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
        
class Privileges():
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges
    # 移动方法
    def show_privileges(self):
        print(f"你拥有管理员权限如下")
        for privilege in self.privileges:
            print(f"+ {privilege}")
        
# 新的Admin类
class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        # 继承父类
        super().__init__(first_name, last_name)
        # 使用Privileges类的实例作为属性
        self.privileges = Privileges(privileges)
        
administer_test = Admin("zg", "Huang", ["can add post", "can delete post", "can ban user"])
administer_test.privileges.show_privileges()
```

    你拥有管理员权限如下
    + can add post
    + can delete post
    + can ban user
    

## Problem 4 


### 编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语。


### 并将一条访问记录添加到文件 guest_book.txt 中，确保这个文件中的每条记录都独占一行. 


```python
filename = "guest_book.txt"
with open(filename, 'a') as file:
    """指定附加模式a"""
    while True:
        # 提示用户输入其名字
        name = input("请输入你的名字（输入 'quit' 退出）：")
        # 避免大小写混淆
        if name.lower() == "quit":
            break
        # 打印问候语
        print(f"你好，{name}！欢迎访问！")
        # 将用户名字添加到文件中，并添加换行符
        file.write(name + '\n')
```

    请输入你的名字（输入 'quit' 退出）：Huang
    你好，Huang！欢迎访问！
    请输入你的名字（输入 'quit' 退出）：黄
    你好，黄！欢迎访问！
    请输入你的名字（输入 'quit' 退出）：quit
    

## Problem 5 


### 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。


### 再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It’s _____.”。


```python
import json

# 提示用户输入他喜欢的数字
favorite_number = input("请输入你喜欢的数字: ")

filename = "favorite_number.json"

try:
    # 将数字转换为整数
    number = int(favorite_number)
    # 以写入模式打开文件
    with open(filename, 'w') as file:
        # 使用 json.dump() 将这个数字存储到文件中
        json.dump(number, file)
except ValueError:
    print("你输入的不是有效的数字，请输入一个整数。")
```

    请输入你喜欢的数字: 114514
    


```python
import json
filename = "favorite_number.json"

try:
    # 以读取模式打开文件
    with open(filename, 'r') as file:
        # 使用 json.load() 从文件中读取数字
        favorite_number = json.load(file)
    # 打印消息
    print(f"I know your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    print("未找到存储数字的文件，请先运行存储数字的程序。")
```

    I know your favorite number! It's 114514.
    

## Problem 6 


### 将练习 5中的两个程序合而为一。


如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。

> 这里保存了两次运行的结果


```python
import json

# 定义存储数字的文件名
filename = 'favorite_number_test.json'

try:
    # 尝试打开文件并读取用户喜欢的数字
    with open(filename, 'r') as f:
        content = f.read()
        if content:
            # 文件内容不为空，尝试解析 JSON
            favorite_number = json.loads(content)
            print(f"I know your favorite number! It’s {favorite_number}.")
        else:
            # 文件内容为空，提示用户输入喜欢的数字
            while True:
                try:
                    favorite_num = input("文件内容为空，请输入你喜欢的数字: ")
                    # 尝试将输入转换为整数
                    favorite_number = int(favorite_num)
                    try:
                        # 尝试将用户输入的数字写入文件
                        with open(filename, 'w') as file:
                            json.dump(favorite_number, file)
                        # Feedback
                        print(f"已成功将你喜欢的数字 {favorite_number} 保存到 {filename} 文件中。")
                        break
                    except Exception as e:
                        print(f"保存数字到文件时出现错误: {e}")
                except ValueError:
                    print("你输入的不是一个有效的整数，请重新输入。")
except FileNotFoundError:
    print(f"文件 {filename} 未找到，将为你创建并请输入你喜欢的数字。")
    while True:
        try:
            favorite_num = input("请输入你喜欢的数字: ")
            favorite_number = int(favorite_num)
            try:
                with open(filename, 'w') as file:
                    json.dump(favorite_number, file)
                print(f"已成功将你喜欢的数字 {favorite_number} 保存到 {filename} 文件中。")
                break
            except Exception as e:
                print(f"保存数字到文件时出现错误: {e}")
        except ValueError:
            print("你输入的不是一个有效的整数，请重新输入。")
```

    文件 favorite_number_test.json 未找到，将为你创建并请输入你喜欢的数字。
    请输入你喜欢的数字: 1919810
    已成功将你喜欢的数字 1919810 保存到 favorite_number_test.json 文件中。
    


```python
import json

# 定义存储数字的文件名
filename = 'favorite_number_test.json'

try:
    # 尝试打开文件并读取用户喜欢的数字
    with open(filename, 'r') as f:
        content = f.read()
        if content:
            # 文件内容不为空，尝试解析 JSON
            favorite_number = json.loads(content)
            print(f"I know your favorite number! It’s {favorite_number}.")
        else:
            # 文件内容为空，提示用户输入喜欢的数字
            while True:
                try:
                    favorite_num = input("文件内容为空，请输入你喜欢的数字: ")
                    # 尝试将输入转换为整数
                    favorite_number = int(favorite_num)
                    try:
                        # 尝试将用户输入的数字写入文件
                        with open(filename, 'w') as file:
                            json.dump(favorite_number, file)
                        # Feedback
                        print(f"已成功将你喜欢的数字 {favorite_number} 保存到 {filename} 文件中。")
                        break
                    except Exception as e:
                        print(f"保存数字到文件时出现错误: {e}")
                except ValueError:
                    print("你输入的不是一个有效的整数，请重新输入。")
except FileNotFoundError:
    print(f"文件 {filename} 未找到，将为你创建并请输入你喜欢的数字。")
    while True:
        try:
            favorite_num = input("请输入你喜欢的数字: ")
            favorite_number = int(favorite_num)
            try:
                with open(filename, 'w') as file:
                    json.dump(favorite_number, file)
                print(f"已成功将你喜欢的数字 {favorite_number} 保存到 {filename} 文件中。")
                break
            except Exception as e:
                print(f"保存数字到文件时出现错误: {e}")
        except ValueError:
            print("你输入的不是一个有效的整数，请重新输入。")
```

    I know your favorite number! It’s 1919810.
    


```python

```
