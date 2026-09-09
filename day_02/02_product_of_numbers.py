"""
write a program to display product of number from  1 to n
"""

num = int(input("enter number: "))
product=1

for i in range(1,num+1):

    product = product*i

print(product)
