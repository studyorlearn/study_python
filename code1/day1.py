#  \转义字符
print("hello world")
print("hello\nworld")
print("hello\tworld")
print("helloooo\tworld")
print("hello\rworld")
print("hello\bworld")#back a letter
print("http:\\\www.baidu.com")
#原字符 不希望转义字符\起作用  结尾不能是\ 
print(r'hello\world')
print(r'hello\world\2')

# 字符编码
print(chr(0b100111001011000))
print(ord('乘'))

#python 中标识符 字母、数字、下划线 保留字 区分大小写
import keyword
print(keyword.kwlist)

#变量
t='hello world'
print(t)
print(id(t))
print(type(t))
t='你好世界'#多次赋值指向一个新的内存空间
print(t)
print(id(t))
print(type(t))

#数据类型 int float bool str 
print('十进制',112)
print('八进制',0o117)
print('二进制',0b1010)
print('十六进制',0xff)
a=1.1
b=2.2
print(a+b)
c=True
print(c)
str1='''ni
hao
'''
print(str1)
s=20.0
print(s,type(s))

#类型转换 +  str() int() float()
print('you are '+str(250))
print(int('128'))#带小数的字符串不可以使用 不是数字串不可以

#注释 #单行  '''多行注释'''
 