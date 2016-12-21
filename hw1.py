Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3+2
5
>>> 3-2
1
>>> 3*2
6
>>> 3/2
1.5
>>> 4/2
2.0
>>> 3//2
1
>>> 3%2
1
>>> 14%3
2
>>> 1-3+2**3*4
30
>>> abs(-13)
13
>>> min(2,-4.0,6,-12)
-12
>>> min(2,-12.0)
-12.0
>>> 5=4
SyntaxError: can't assign to literal
>>> 5==4
False
>>> 12//5
2
>>> 12/(5==4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    12/(5==4)
ZeroDivisionError: division by zero
>>> (23+19+31)/3
24.333333333333332
>>> abs(54-57)
3
>>> (31%2)==0
False
>>> (1387%19)==0
True
>>> 31%2 == 0
False
>>> x=3.0
>>> type(x)
<class 'float'>
>>> break = 4
SyntaxError: invalid syntax
>>> x=4
>>> X
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    X
NameError: name 'X' is not defined
>>> 500/8
62.5
>>> string3 = '3'
>>> n=3
>>> 'hello'*n
'hellohellohello'
>>> 3 in 31
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    3 in 31
TypeError: argument of type 'int' is not iterable
>>> len(3124)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len(3124)
TypeError: object of type 'int' has no len()
>>> len('3124')
4
>>> s='Apple'
>>> len(s)
5
>>> s[1]
'p'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s[-len(s)]
'A'
>>> s[0]
'A'
>>> myList = [1,3,6]
>>> type(myList)
<class 'list'>
>>> type(myList[1])
<class 'int'>
>>> lst = ['one', 'two', 'four']
>>> lst[2]
'four'
>>> lst[2] = 'three'
>>> lst [2] = three
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    lst [2] = three
NameError: name 'three' is not defined
>>> lst[2]
'three'
>>> lst[3] = 'four'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    lst[3] = 'four'
IndexError: list assignment index out of range
>>> [1,2,3]+[3,4,5]
[1, 2, 3, 3, 4, 5]
>>> x=[1, 2, 3, 3, 4, 5]
>>> x
[1, 2, 3, 3, 4, 5]
>>> x[3]=4
>>> x
[1, 2, 3, 4, 4, 5]
>>> lst = [2,4,6]
>>> lst.append(8)
>>> lst
[2, 4, 6, 8]
>>> len(lst)
4
>>> lst = ['1','b','c','d']
>>> lst
['1', 'b', 'c', 'd']
>>> lst[0]='a'
>>> lst
['a', 'b', 'c', 'd']
>>> lst.pop('c')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    lst.pop('c')
TypeError: 'str' object cannot be interpreted as an integer
>>> lst.pop
<built-in method pop of list object at 0x034037B0>
>>> lst
['a', 'b', 'c', 'd']
>>> lst.pop()
'd'
>>> lst
['a', 'b', 'c']
>>> lst.pop([1])
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    lst.pop([1])
TypeError: 'list' object cannot be interpreted as an integer
>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
>>> s4 = ' '
>>> s1+s4+s2+s4+s3
'ant bat cod'
>>> s1+s4+s2+s4+s2+s3
'ant bat batcod'
>>> s1+s4+s2+s4+s2+s4+s3
'ant bat bat cod'
>>> ((2*s2)+s3+s4)*2
'batbatcod batbatcod '
>>> s1 + ' ' + s2 + ' '+s3
'ant bat cod'
>>> s1 + ' ' + s2 + ' '+s2 + ' ' +s3
'ant bat bat cod'
>>> int(3.4)
3
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
>>> daysPerWeek = 7
>>> hoursPerDay = 24
>>> minutesPerHour = 60
>>> daysPerWeek*hoursPerDay*minutesPerHour
10080
>>> 
>>> 
>>> ((15*6)+(23*7)+(18*8)+(25*9))/(15+23+18+25)
7.654320987654321
>>> 
>>> 
>>> 3**(-6)
0.0013717421124828531
>>> 
>>> 
>>> 
>>> 75//12
6
>>> 75%12
3
>>> 
>>> 
>>> s1 = 'y'
>>> s2 = '$'
>>> s1+(2*s2)+s1
'y$$y'
>>> 
>>> 
>>> s1 = 'y'
>>> s2 = '$'
>>> ((s1*3)+s2)*2
'yyy$yyy$'
>>> 
>>> 
>>> s1 = 'y'
>>> s2 = '$'
>>> (s1+((s2*3)+(s1*2))+s1)
'y$$$yyy'
>>> 
>>> 
>>> s1 = 'y'
>>> s2 = '$'
>>> (s1+(((s2*3)+(s1*2))*2)+s1)
'y$$$yy$$$yyy'
>>> 
>>> 
>>> s1 = 'y'
>>> s2 = '$'
>>> (s1+(s2*3)+(s1*3)+(s2*3)+(s1*2))
'y$$$yyy$$$yy'
>>> 
>>> 
>>> 
>>> (6+(5//2))<10
True
>>> 
>>> 
>>> (6%3)==(14-(8*1.5))
False
>>> 
>>> 
>>> 
>>> 7<6==0+(2>3)
False
>>> 7<6
False
>>> 2>3
False
>>> False + 0
0
>>> False == False
True
>>> 7<6 === 0+(2>3)
SyntaxError: invalid syntax
>>> 7<6 == 0+(2>3)
False
>>> (7<6)==(0+(2>3))
True
>>> 
>>> 
>>> (7<6)==(0+(2>3))
True
>>> 
>>> 
>>> 
>>> (-1<3)==(4<6)
True
>>> 
>>> 
>>> 
>>> s1 = 'silly puddy'
>>> 'x' in s1
False
>>> 
>>> 
>>> s1 = 'silly puddy'
>>> s1[0] == s1[-1]
False
>>> 
>>> 
>>> 
>>> s1 = 'silly puddy'
>>> s1[-2]
'd'
>>> 
>>> 
>>> s1 = 'silly puddy'
>>> s1[6] = 'm'
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    s1[6] = 'm'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> s1 = 'silly puddy'
