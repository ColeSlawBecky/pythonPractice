# hw6.py due 10/26/2016
# Becky Jacob

#Problem 1
def openFile():
    'open hambone.txt and read content'
    infile = open( 'hambone.txt', 'r' )
    content = infile.read()
    infile.close()

def tryOpenFile():
    'print out the stated message, instead of moving into an erroneous state'
    try:
        openFile()
    except:
        print( 'hambone.txt file could not be found' )

#Problem 2
def x( a ):
    print( 'x() local vars:', vars() )
    print()
    return a+c #a is local to x(), c is global, so 2 + 4

def y( b ):
    c = 5 #c is local to y() unless 'global' is used
    print( 'y() local vars:', vars() )
    print()
    return b*c #b and c are local to y(), so 3*5

c = 4 #c is global
res = x(2) + y(3) #res is global
print( 'res = {0}'.format( res ) )
