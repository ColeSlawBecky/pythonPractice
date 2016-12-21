import time
from random import randrange


#non-recursive solution for fibonacci
def fibIter( n ):
    'returns the nth Fibonacci number, where index starts at 0'
    prev = 0       # Fibonacci number 0
    current = 1    # Fibonacci number 1
    
    for i in range( 2, n+1 ): # compute ith Fibonacci number (current)
        prev, current = current, prev+current

    return current

#best version: using iteration
def fibIter2( n ):
    a,b = 0,1
    for i in range( n-1 ):
        a,b = b,a+b

    return b


#recursive solution for fibonacci
def rfib( n ):
    #print( n )
    
    if n <= 1:
        return n
    
    else:
        return rfib( n-1 ) + rfib( n-2 )


def timing( f, n ):
    'time function f on input n'
    start = time.time()
    f( n )
    end = time.time()

    return end - start


def test( func, a, b, c ):
    #get runtimes for inputs a to b, step c
    times = {}

    for i in range( a, b, c ):
        times[i] = timing( func, i )
        print( 'Run time of {0}({1}) is {2:.7f} seconds'.format( func.__name__, i, times[i] ) )
# test( rfib, 20, 36, 5 )
# test( fibIter, 1000, 10000, 1000 )


def linearSearch( lst, x ):
    'find element x in lst using linear search'
    cnt = 0
    found = False
    
    for item in lst:
        cnt += 1
        
        if item == x:
            found = True
            break

    return found, cnt
    

def binarySearchLoop( lst, x ):
    'find element x in sorted lst using binary search'
    first = 0
    last = len(lst)-1
    found = False

    while first <= last and not found:
        mid = ( first + last )//2

        if lst[ mid ] == x:
            found = True

        else:
            if x < lst[ mid ]:
                last = mid-1
                
            else:
                first = mid+1

    return found


def rbinarySearch( lst, x, i, j ):
    '''
    search for element x in sorted sublist[i:j];
    return index of x if found, else return -1
    '''
    
    if i == j:
        return -1

    mid = ( i+j )//2

    print( lst[i:j], 'mid =', mid )

    if lst[ mid ] == x:
        return mid

    if x < lst[ mid ]:
        # target is less than lst[mid] so search before middle
        return rbinarySearch( lst, x, i, mid )

    else:
        # target is greater than lst[mid] so search after middle
        return rbinarySearch( lst, x, mid+1, j )

lst = [2, 5, 11, 13, 16, 24, 28, 41, 42, 43, 45, 57, 72, 73, 89, 90, 99] 
lsta = [ 7, 22, 29, 32, 42, 52, 59, 66, 69, 76 ]
lstb = [50, 92, 35, 97, 2, 66, 8, 64, 5, 77, 87]
lstc = [21, 28, 32, 40, 42, 44, 50, 55, 68, 72, 77]
# if lst not sorted, lst.sort() which sorts lst in place

#test find using a lst of 5000 random elements, try changing values
def test_f():
    lst = [randrange(10000) for i in range(5000)]
    lst.sort()
    find( lst, 2370 )


#iterative solution
def merge( lst1, lst2 ):
    lst3 = []
    while( len( lst1 ) > 0 and len( lst2 ) > 0 ):
        # pick first elements of lst1 and lst2
        a = lst1[0] 
        b = lst2[0]

        # append whichever is smaller, and remove from that lst
        if a < b: 
            lst3.append( a )
            lst1 = lst1[1:]
            
        else:
            lst3.append(b)
            lst2 = lst2[1:]
            
    if len( lst1 ) == 0:
        lst3 += lst2 #add rest of lst2
        
    else:
        lst3 += lst1 #add rest of lst1

    return lst3

    
def mergesort( lst ):
    'recusive mergesort'
    n = len(lst)
    if n <= 1:
        return lst

    else:
        mid = n//2
        left = mergesort( lst[:mid] )
        right = mergesort( lst[mid:] )
        return merge( left, right )

lst2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

#test running mergesort on list of 10000 random elements
def test_mergesort():
    lst = [randrange(1000) for i in range(100)]
    print( lst )
    return mergesort(lst)
