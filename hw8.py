# hw8.py due 11/9/2016
# Becky Jacob

#Problem 1
def alt( s1, s2 ):
    'returns a string that is the result of alternating the letters of s1 and s2'
    if len(s1) == 0 and len(s2) == 0:
        return ''
    elif len(s1) == 0:
        return s2[:]
    elif len(s2) == 0:
        return s1[:]
    else:
        return s1[0] + s2[0] + alt( s1[1:], s2[1:] )

'''
>>> alt( 'cat', 'dog' )
'cdaotg'
>>> alt( 'kitty' , 'dog' )
'kdiotgty'
>>> alt( 'cat' , 'puppy' )
'cpautppy'
'''

#Problem 2
import os

def getBytes( pathname ):
    'return the sum of the total number of bytes of files in pathname'

    print('Scanning: {}'.format( pathname ) )
    cnt = 0
    for name in os.listdir( pathname ):
        subname = os.path.join( pathname, name )

        if os.path.isfile( subname ):
            cnt += os.path.getsize( subname )

        elif os.path.isdir( subname ):
            cnt += getBytes( subname )

        else:
            pass
        
    return cnt
'''
>>> getBytes ('test')
Scanning: test
Scanning: test\ch06
Scanning: test\folder1
Scanning: test\folder1\folder11
Scanning: test\folder2
427601
'''


#Problem 3
#Problem 3a
'''
>>> 30 in lst - 11
>>> 72 in lst - 3
'''

#Problem 3b
'''
>>> lst.sort()
>>> lst
[21, 28, 32, 40, 42, 44, 50, 55, 68, 72, 77]
'''

#Problem 3c
'''
First time call binary search
slice: lst[ 0:11 ] = [ 21, 28, 32, 40, 42, 44, 50, 55, 68, 72, 77 ]
mid = (0 + 11)//2 = 5
lst[ mid ] = 44
50 > 44, so search upper half

Second time call binary search
slice: lst[ 6:11 ] = [ 50, 55, 68, 72, 77 ]
mid = (6 + 11)//2 = 8
lst[ mid ] = 68
50 < 68, so search lower half

Third time call binary search
slice: lst[ 6:8 ] = [ 50, 55 ]
mid = (6 + 8)//2 = 7
lst[ mid ] = 55
50 < 55, so search lower half

Fourth time call binary search
slice: lst[ 6:7 ] = [ 50 ]
mid = (6 + 7)//2 = 6
lst[ mid ] = 50
50 == 50, so we return index 6
'''
