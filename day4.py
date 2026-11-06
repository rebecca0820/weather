#列表推导式（List Comprehension
# squares = [i * i for i in range(1, 11)]
# 只要偶数的平方
#even_squares = [i * i for i in range(1, 11) if i % 2 == 0]
#print(even_squares)  # [4, 16, 36, 64, 100]

# 字典：创建 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#square_dict = {i: i*i for i in range(1, 6)}

# 过滤：只要分数>=80的学生
#scores = {"Alice": 75, "Bob": 90, "Charlie": 85, "David": 60}
#passed = {name: score for name, score in scores.items() if score >= 80}
#print(passed)  # {'Bob': 90, 'Charlie': 85}


#元组和列表很像，但创建后不能修改（不可变）。用 () 表示
# 函数返回多个值，其实就是返回元组
#def get_min_max(numbers):
    #return min(numbers), max(numbers)

#lowest, highest = get_min_max([3, 1, 7, 2, 9])
##print(lowest, highest)  # 1 9

#集合（Set）
#集合的特点是：不重复、无序。用 {} 表示
# 创建集合
#fruits = {"苹果", "香蕉", "苹果", "橘子"}
#print(fruits)  # {'苹果', '香蕉', '橘子'}  ← 重复的"苹果"自动去掉了

# 去重（非常实用！）
#numbers = [1, 2, 2, 3, 3, 3, 4]
#unique = list(set(numbers))
#print(unique)  # [1, 2, 3, 4]

# 集合运算
#a = {1, 2, 3, 4, 5}
#b = {4, 5, 6, 7, 8}

#print(a & b)   # 交集：{4, 5}
#print(a | b)   # 并集：{1, 2, 3, 4, 5, 6, 7, 8}
#print(a - b)   # 差集：{1, 2, 3}

# 判断元素是否在集合中（比列表快得多）
# 创建集合
#fruits = {"苹果", "香蕉", "苹果", "橘子"}
#print(fruits)  # {'苹果', '香蕉', '橘子'}  ← 重复的"苹果"自动去掉了

# 去重（非常实用！）
#numbers = [1, 2, 2, 3, 3, 3, 4]
#unique = list(set(numbers))
#print(unique)  # [1, 2, 3, 4]

# 集合运算
#a = {1, 2, 3, 4, 5}
#b = {4, 5, 6, 7, 8}

#print(a & b)   # 交集：{4, 5}
#print(a | b)   # 并集：{1, 2, 3, 4, 5, 6, 7, 8}
#print(a - b)   # 差集：{1, 2, 3}

# 判断元素是否在集合中（比列表快得多）
# 创建集合
#fruits = {"苹果", "香蕉", "苹果", "橘子"}
#print(fruits)  # {'苹果', '香蕉', '橘子'}  ← 重复的"苹果"自动去掉了

# 去重（非常实用！）
#numbers = [1, 2, 2, 3, 3, 3, 4]
#unique = list(set(numbers))
#print(unique)  # [1, 2, 3, 4]

# 集合运算
#a = {1, 2, 3, 4, 5}
#b = {4, 5, 6, 7, 8}

#print(a & b)   # 交集：{4, 5}
#print(a | b)   # 并集：{1, 2, 3, 4, 5, 6, 7, 8}
#print(a - b)   # 差集：{1, 2, 3}

# 判断元素是否在集合中（比列表快得多）
#print("苹果" in fruits)  # True


# 用一行代码生成：['1的平方是1', '2的平方是4', '3的平方是9', ..., '10的平方是100']
square=[ i * i for i in range(1,11)]
print(square)


#练习2：字典统计
#写一个函数，接收一个字符串，统计每个字符出现的次数，返回字典：

def count_chars(text):
    dic={}
    for i in text:
      dic[i]=dic.get(i,0)+1
    return dic



print(count_chars("hello") )
 # 返回 {'h': 1, 'e': 1, 'l': 2, 'o': 1}

#练习3：字典过滤
#给定一个商品字典，用字典推导式筛选价格大于50的商品：

products = {"苹果": 10, "牛排": 80, "牛奶": 15, "龙虾": 120, "面包": 8}

products_enpensive={fruits: price for fruits, price in products.items() if price>=50 }
print(products_enpensive)
# 结果应该是 {"牛排": 80, "龙虾": 120}


#练习4：集合去重+排序
#给定一个有重复数字的列表，去重后按从小到大排序输出：

nums = [5, 3, 8, 3, 1, 5, 9, 1, 7]
# 结果应该是 [1, 3, 5, 7, 8, 9]

print(list(sorted(set(nums))))


#练习5：综合题
#给定一段英文文本，找出出现次数最多的单词（忽略大小写）：

text = "Python is great and Python is fun and Python is easy"
list= text.split()
print(list)

def count_max(text):
  dic={}
  for i in text:
    dic[i]=dic.get(i,0)+1
 
  max_count=max(dic.values())
  max_word={word for word,count in dic.items() if count==max_count}
  return max_word,max_count

print(count_max(list))
# 结果应该是 "python"（出现了3次）

# collection.counter
from collections import Counter

word=text.split()
word_count=Counter(word)
print(word_count)
print(word_count.most_common(2))

















