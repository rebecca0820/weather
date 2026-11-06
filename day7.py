

from pyclbr import Class


class Student:
   count=0    # 类的属性
   def __init__(self,name,score):
      self.name=name
      self.score=score
      Student.count+=1   # 对象的属性，要用类名来访问
      print(f"已创建第{Student.count}个学生对象")



   def pass_or_fail(self):
       if self.score>60 :
            print("pass")
       else :
              
            print("fail")    

s1 = Student("Alice", 85)
s2 = Student("Bob", 42)
s3 = Student("Cindy", 60)


print(f"总共创建了 {Student.count} 个学生")
s3.pass_or_fail()


class GraduateStudent(Student):
    def __init__(self, name, score, advisor):
        super().__init__(name, score)  # 调用父类的构造函数
        self.advisor = advisor     #加上自己的属性

    def research(self):
        print(f"{self.name} is doing research under {self.advisor}")


class ExchangeStudent(Student):
        
    def pass_or_fail(self):
           print(f"交换生考核标准不同")
           if self.score>=70 :
                print("pass")
           else :
                  
                print("fail") 