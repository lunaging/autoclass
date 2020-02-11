
#数值
wideth = 12

#String
x = 'abc'

print(2+2)

#可以使用f + {} 引入变量打印；
print(f'c:\\some\\name\\{x}')

print('c:\\some\\name\\{y}\\{x}'.format(y=x,x=124))

#Lists
list1 = [1,2,3,56,78,90]
list1[1]
list1[1:3]
list1[-3:-1] #倒数第4个到倒数第2个
list1.pop()
list1.remove(56)
list1.count() #?
list1.popleft() #从头部开始弹出
list1.sort()

#Sets集合 无排序



#元组tuples 不可修改

#列表Lists 可修改


#词典-关系数据
d={'a':1, 'apple':2}
print(d['a'])

#if条件判断
# x = input("您好，请输入一个偶数:" %d)
# if x % 2 == 0:
#     print("输入正确，是偶数")
# elif x % 2 != 0:
#     print("输入不正确，不是偶数")
# else:
#     print("不符合要求")

