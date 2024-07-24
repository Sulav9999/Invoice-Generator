'''
logical operator in python
logical and
logical or
logical nor


'''
#logical and 
'''
condition 1  condition 2  result(condition 1 and condition 2)
T             T              T and T=>T
T             F               T and F =>F
F              T              F and T=F
F              F              F and F =>F

'''
n1=12
n2=50
condition1=n1 > 10 
condition2=n1 >n2 > 50
condition3=n2 > 50
result=condition1 and condition2 and condition3


#print(result)


"""
logical or
condition 1    condition2   result(condition 1 or condition 2)
T               T              T or T =>T
T               F              T or F => F
F               T               F or T =>T
F                F              F or F =>F

"""
name = "hari"
address = "lalitpur"
res = name =="hari" or address=="lalitpur"
#print(res)

results =name =="hari" or address=="lalitpur" or login



"""
Logical not
condition1              reult(not condition)
T                        not T=>F
F                        not F=>T
"""
b= True
print(not b)