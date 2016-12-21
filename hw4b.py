Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> movie_tix(1, 2)
0
>>> movie_tix(12,3)
33
>>> movie_tix(13,4)
56
>>> movie_tix(60,5)
70
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> movie_tix(1,2)
0
>>> movie_tix(12,3)
33
>>> movie_tix(13,4)
56
>>> movie_tix(60,5)
50
>>> t = [ [3,5,7], [0,2,1], [3,8,3] ]
m = [ [3,5,7,9], [0,2,1,6], [3,8,3,1] ]

# print each row of 2-D list
for lst in t:
    print( lst )

print()
print( 't[0][2]: {0}'.format( t[0][2] ) )
print( 't[-1][-2]: {0}'.format( t[-1][-2] ) )
print()
print( 't[0][2] old: {0}'.format( t[0][2] ) )
t[0][2] = t[0][2] + 3
print( 't[0][2] new: {0}'.format( t[0][2] ) )
print()
SyntaxError: multiple statements found while compiling a single statement
>>> t = [ [3,5,7], [0,2,1], [3,8,3] ]
m = [ [3,5,7,9], [0,2,1,6], [3,8,3,1] ]

# print each row of 2-D list
for lst in t:
    print( lst )

print()
print( 't[0][2]: {0}'.format( t[0][2] ) )
print( 't[-1][-2]: {0}'.format( t[-1][-2] ) )
print()
print( 't[0][2] old: {0}'.format( t[0][2] ) )
t[0][2] = t[0][2] + 3
print( 't[0][2] new: {0}'.format( t[0][2] ) )
print()
SyntaxError: multiple statements found while compiling a single statement
>>> t = [ [3,5,7], [0,2,1], [3,8,3] ]
>>> m = [ [3,5,7,9], [0,2,1,6], [3,8,3,1] ]
>>> t
[[3, 5, 7], [0, 2, 1], [3, 8, 3]]
>>> m
[[3, 5, 7, 9], [0, 2, 1, 6], [3, 8, 3, 1]]
>>> for lst in t:
    print( lst )

    
[3, 5, 7]
[0, 2, 1]
[3, 8, 3]
>>> print( 't[0][2]: {0}'.format( t[0][2] ) )
t[0][2]: 7
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace ( m )
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    trace ( m )
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 34, in trace
    print([row][entry])
IndexError: list index out of range
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    trace(m)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 32, in trace
    for j in range( len(i)):
TypeError: object of type 'int' has no len()
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
[8, -2, 5]
[-20, -3, 11]
[0, -16, 9]
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    trace(m)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 32, in trace
    for entry in range( len(row)):
TypeError: object of type 'int' has no len()
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    trace(m)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 32, in trace
    for entry in row:
TypeError: 'int' object is not iterable
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
0
1
2
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    trace(m)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 32, in trace
    for col in row:
TypeError: 'int' object is not iterable
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
[8, -2, 5] 8
[8, -2, 5] -2
[8, -2, 5] 5
[-20, -3, 11] -20
[-20, -3, 11] -3
[-20, -3, 11] 11
[0, -16, 9] 0
[0, -16, 9] -16
[0, -16, 9] 9
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
[8, -2, 5] 8
[8, -2, 5] -2
[8, -2, 5] 5
[-20, -3, 11] -20
[-20, -3, 11] -3
[-20, -3, 11] 11
[0, -16, 9] 0
[0, -16, 9] -16
[0, -16, 9] 9
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    trace(m)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 33, in trace
    if matrix[row] == row[col]:
TypeError: list indices must be integers or slices, not list
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> m = [ [8, -2, 5], [-20, -3, 11], [0, -16, 9] ]
>>> trace(m)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    trace(m)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 33, in trace
    print (matrix[row])
TypeError: list indices must be integers or slices, not list
>>> 4//2
2
>>> 4%2
0
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> a = [ 5, 2, 39, 16, 1 ]
>>> b = [ 8, 0, 19 ]
>>> getEvenTuples(a,b):
	
SyntaxError: invalid syntax
>>> getEvenTuples(a,b)
(5, 19)
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> a = [ 5, 2, 39, 16, 1 ]
>>> b = [ 8, 0, 19 ]
>>> getEvenTuples(a,b)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    getEvenTuples(a,b)
  File "C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py", line 62, in getEvenTuples
    indies.append((i, j))
AttributeError: 'tuple' object has no attribute 'append'
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> a = [ 5, 2, 39, 16, 1 ]
>>> b = [ 8, 0, 19 ]
>>> getEvenTuples(a,b)
[(5, 19), (2, 8), (2, 0), (39, 19), (16, 8), (16, 0), (1, 19)]
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
done checking!
>>> a = [3,5,0]
>>> b = [1,13,10]
>>> getEvenTuples(a,b)
[(3, 1), (3, 13), (5, 1), (5, 13), (0, 10)]
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> a = [3,5,0]
>>> b = [1,13,10]
>>> getEvenTuples(a,b)
done checking!
[(3, 1), (3, 13), (5, 1), (5, 13), (0, 10)]
>>> a = [ 5, 2, 39, 16, 1 ]
>>> b = [ 8, 0, 19 ]
>>> getEvenTuples(a,b)
done checking!
[(5, 19), (2, 8), (2, 0), (39, 19), (16, 8), (16, 0), (1, 19)]
>>> 
 RESTART: C:\Users\rebec\OneDrive\Documents\DePaul\Introduction to Programming\HW\hw4.py 
>>> hidden( message.txt)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    hidden( message.txt)
NameError: name 'message' is not defined
>>> 
