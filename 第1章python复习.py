#------python basic---------
# basic datatypes:
"string" == 'string'
# go next line:
\
# documentation string:
"""This is the documentations string"""
# overloaded to work on strings
'banana' + '_' + 'apple'
4*('appricot' + ' ')
# casting
float(string)
str(float)
eval('string') # eval把string转化成它应有的形式
-------------------------------------------------------------
#------sequence types: share same syntax and functionality---
# 1.tuple: immutable, ordered, mixed types
tu = (23, 'abc', 4.56, (2,3), 'def')
tu[1] >>> 'abc'
tu[-3] >>> 4.56
tu[1:3] >>> ('abc', 4.56) # 1,2
tu[:3] >>> (23, 'abc', 4.56) # 0,1,2
tu[2:] >>> (4.56, (2,3), 'def') # 2,3,4
tu[:] >>> tu # make a copy of entire tuple
tu1 + tu2 >>> (加起来的新tuple)
## 包括冒号前，不包括冒号后
# 2.string: immutable
st = "string" = 'string' = """string"""
's' in str >>> True
str1 + str2 >>> "加起来的新string"
# 3.list: mutable, ordered, mixed types
li = ['abc', 34, 4.34]
li2 = li # refer to the same list
li2 = li[:] # create new independent copy
li1 + li2 >>> [加起来的新list]
# 可以改变:
li[1] = 45
li = ['abc', 45, 4.34]
# list操作
li.append('a') #加到最后
li.insert(2, 'i') # 加到 li[2]
li.sort(reverse=False) #排序，string放最后
#e.g
>>> li = [1,11,3,4,5]
>>> li.append('a')
>>> li.insert(2,'i')
>>> li.sort()
>>> print li
[1, 3, 4, 5, 11, 'a', 'i']
>>> li.sort(reverse=True)#降序
>>> print li
['i', 'a', 11, 5, 4, 3, 1]
>>> li.sort(reverse=False)#升序
>>> li
[1, 3, 4, 5, 11, 'a', 'i']
# list comprehension
[ range(x)  for x in range(4)]
>>> [[], [0], [0, 1], [0, 1, 2]]
[y for x in range(4) for y in range(x)]
>>> [0, 0, 1, 0, 1, 2]
# 1. lists slower but powerful than tuples
# 2. data be accessed but not changed: tuple
# 3. convert between these two:
li = list(tu)
tu = tuple(li)
---------------------------------------------------------
#-----------Dictionaries: a mapping type-----------
# store a mapping between a set of keys and a set of values
    # keys -> immutable
    # values -> any type
# define, modify, view, lookup, delete key-value pairs in the dictionary
d = {'user':'bozo','pswd':1234}
d['user'] = 'clown' # change value for existing key
d['id'] = 25 # add new key-value pair
del d['user'] # remove key-value pair
d.clear() # remove all
d.keys() # list of keys
d.values() # list of values
d.items() # list of pairs as tuples
---------------------------------------------------------
#---------------Control flow----------------
1. if 判断1:
    print
elif 判断2:
    print
else:
    print
2. while 判断：
    print
3. for n in range(2, 10)
    for x in range(2, n)
        if n % x == 0:
        print n, 'equals', x, '*', n//x
        break
    else:
        print n, 'is a prime number'
---------------------------------------------------------
#---------------Function Definitions----------------
1. def <name>(arg1, arg2, ..., argN):
    <statements>
    return <value>
   def times(x,y):
       return x * y # positional arguments
2. def func(a, b, c=10, d=100):
    print a, b, c, d # optional arguments
>>> func(1, 2)
1, 2, 10, 100
>>>func(1, 2, 3, 4)
1, 2, 3, 4
3. gotchas
    arguments to other functions
def square(x):
    return x * x
>>> z = square
>>> z(2)
4
# def map(fun, li)
def map(fun, li)
#arguments: a function and a list
#output: return [fun(x) for x in list]
>>> map(square, [1, 2, 3, 4])
[1, 4, 9, 16]
>>> map(lambda x: x * x, [1, 2, 3, 4])
[1, 4, 9, 16]
# 函数调用字母表示的函数
# 先定义power_generate
def power_generate(n):
    return lambda x: x ** n
# 用字母表示函数
square = power_generate(2)
cube = power_generate(3)
# 应用
map(square, [1, 2, 3, 4])
map(cube, [1, 2, 3, 4])
---------------------------------------------------------
#---------------Python Modules---------------
from numpy import sqrt
import numpy
import numpy as np
from numpy import *
一些numpy的函数
np.sqrt(x)
np.exp(x)
np.array([1.0, 2.0, 3.0])
np.dot(a, b) = np.inner(a, b)
np.outer(a, b)
np,random # random numbers
argparse # command line
sys # I/O
---------------------------------------------------------
#---------------Classes & Objects----------------
1. Object: data structure contains variables+methods
->Encapsulation: public interface and private implelmentation
->Polymorphism: overload operators->have appropriate behavior
->Inheritance: parents->child
2. 
