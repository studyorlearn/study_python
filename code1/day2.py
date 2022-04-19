#input() function
""" present=input("1+1等于几呢")
print(present,type(present))#获取的为str类型
a=int(input('first number'))
b=int(input('second number'))
print(a+b) """

#运算符号  加减乘除+-*/ 整除// 取余数% 幂运算**
from cv2 import dft


print(1/2)
print(11//2)
print(11%3)
print(3*4)
print(3**4)
print(9//-4)#负数向下取整
print(9%-4)
print(-9%4)#被除数-除数×商 

#赋值运算符
q=w=e=20#链式赋值 三个变量指向一个地址
print(id(q))
q=400
print(id(q))
print(id(w))
q+=30#q=q+30#-=  *=  /=  //=
q,w,e=20,30,40
q,w=w,q#交换变量值

#比较运算符 > < >= <= 
print(q>w)#return bool 
print(q<=w,w<=q,q==w,q!=w)
q,w=10,10#同一值 若内存中已存在 不会再占用新的内存
c=q is w#判断qw的id是否一样
print(c)
list1=[1,2,3]
list2=[1,2,3]
print(list1==list2)
print(list1 is not list2)#true

print('----------------bool---------------')
#布尔运算符 and or not in  not in 
print(not 1)
print(ord('k'))

#位运算符 & | <<  >> 移位 溢出补0
print(4&8)
print(4|8)
print(128<<2)#左移两位

#运算符优先级 1** 2* / //  3+-算术运算 4 << >> 5& 6 | 位运算
# 7比较运算 >< >= <= == != 布尔运算8 and 9 or 赋值运算10 =
