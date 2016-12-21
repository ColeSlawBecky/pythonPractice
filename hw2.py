# hw2.py due 9/21/2016
# Becky Jacob

# Problem 1
import math
def radians_to_degrees(radians):
    'function will return the value of angle in degrees' #function that multiplies radians by 180 and divides by pi
    Degrees = ((radians*180)/ math.pi)
    return Degrees

'''
>>> radians_to_degrees(1.5708)
90.0002104591497
>>>
'''

#Problem 2
def isEligible():
    'function will determine eligibility based on gender and age'
    gender = input("Gender, listed as 'm' or 'f': ")
    age = eval(input('Age: '))
    if (gender == 'm' and 9<=age<=11) or (gender == 'f' and age == 10): #chained comparison for male ages
        print('Yay! Eligible!')
    else:
        print('Sorry, not eligible.')

'''
>>> isEligible()
Gender, listed as 'm' or 'f': f
Age: 9
Sorry, not eligible.
>>> isEligible()
Gender, listed as 'm' or 'f': m
Age: 9
Yay! Eligible!
>>> '''

#Problem 3
def convertCurrency( ccy, amount ):
    'convert a desired amount of USD to a desired currency'

    if ccy == 'EUR':
        amt = amount * .90 #conversion rate for USD to EUR
    else:
        amt = amount * 1.38 #conversion rate for USD to SGD

    return amt


'''>>> currency = input( 'enter desired currency: ')
enter desired currency: EUR
>>> desired_USD = eval (input ( 'enter desired amount in USD: '))
enter desired amount in USD: 105.50
>>> new_amount = convertCurrency( currency, desired_USD)
>>> print ( 'new amount = ', new_amount, currency )
new amount =  94.95 EUR
>>> 
>>> currency = input( 'enter desired currency: ')
enter desired currency: SGD
>>> desired_USD = eval (input ( 'enter desired amount in USD: '))
enter desired amount in USD: 79
>>> new_amount = convertCurrency( currency, desired_USD)
>>> print ( 'new amount = ', new_amount, currency )
new amount =  109.02 SGD
>>> '''

#Problem 4
def oddNumbers():
    'print all odd numbers between 1 and 17, inclusive'
    for i in range(1,18): #we must go up to 18 so n-1 includes 17
        if i % 2 != 0:
            print(i)

'''>>> oddNumbers()
1
3
5
7
9
11
13
15
17
>>> '''

