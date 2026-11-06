# lambda：一行小函数

def sqaure(x):
    return x**2

x= lambda x: x**2
print(x(5))

#map 和 filter 都是高阶函数：它们接收函数作为参数。
#map：对每个元素做转换
numbers = [1, 2, 3, 4, 5]
x=list(map(lambda x:x**2,numbers))
print(x)

y=list(filter(lambda x:x%2==0, numbers))
print(y)

z=list(map(lambda x:x**2, list(filter(lambda x:x%2==0, range(1,11)))))
print(z)

def buy_milktea(*args):
    print(type(args))  # 打印类型看看
    print(args)        # 打印内容看看

buy_milktea("珍珠", "椰果", "布丁")


#练习 1：通用计时装饰器
#写一个 @timer 装饰器，打印函数名和耗时。

import time
def timer(greet):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=greet(*args,**kwargs)
        end=time.time()
        print(f"{greet.__name__}耗时{end-start}")
        return result
    return wrapper



@timer
def tim():
    print('hello world')

tim()

#练习 2：带参数的重试装饰器
#写一个 @retry，失败时自动重试。

def retry(max_retries=3):
    def decorator(func):
      def wrapper(*args,**kwargs):
          for i in range(1, max_retries + 1):
            try:
              return func(*args,**kwargs)
            except Exception as e:
              print(f"尝试 {i} 失败: {e}")
              if i==max_retries:
                print("已达到最大重试次数，操作失败。")
                raise e
      return  wrapper
    return decorator

@retry()
def tim():
    print('hello world')

tim()

#练习 1｜lambda + map/filter 组合
#给定 orders = [("苹果", 3, 12.5), ("香蕉", 1, 4.0), ("牛奶", 2, 8.9), ("面包", 5, 6.0)]
#用 一行 代码完成：筛选出单价（第三个字段）大于 7 的商品，并转换成 ["苹果", "牛奶"] 这样的名字列表。

orders = [("苹果", 3, 12.5), ("香蕉", 1, 4.0), ("牛奶", 2, 8.9), ("面包", 5, 6.0)]


result=list(map(lambda x:x[0], filter(lambda x:x[2]>7, orders)))
print(result)  # 输出: ['苹果', '牛奶']