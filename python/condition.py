'''
condition in python
1.if
if(conidtion)
body of if

2.elif
3.else


else
body of else
'''


'''n =25
if n>20:
    print(n,"is greater than 20")
    

#print("hello")
number=int(input("any number"))'''

#if number%3==0 and number%7==0:
    #print(number, "is divisible by both 3 and 7")
'''n=int(input("any number"))
if n%2==0:
    print(n,'is even number')
else:
    print(n,'is odd number')'''

n=int(input('any number'))
if n%3==0 and n%7==0:
    print(n, "is divisible by both 3 and 7")
else:
    if n%3==0 or n%7==0:


        if n%3==0:
           print(n, 'is divisible by 3')
        else:
           print(n,"is divisible by 7")
    else:
        print(n,"is not divisible by both 3 and 7")


