#!/usr/bin/env python
# coding: utf-8

# In[27]:


#accept two integer numbers from a user and return their product and if the product is greater than 1000, then retuen their sum 
a=int(input('enter the 1st no.'))
b=int(input('enter the 2nd no.'))
if((a*b)<=1000):
    print('the product is',a*b)
else:
    print('the sum is:',a+b)


# In[28]:


#accept n number from user and calculate the sum of all numbers between 1 and n
summ=0
lim=int(input('enter the limit:'))
for i in range(lim+1):
    summ=summ+i
print('\nthe sum is:',summ)


# In[30]:


#given a number count the total number of digits in a number
a=input('enter the number:')
print('the no.of digits are:',len(a))


# In[53]:


#accept string from a user and display only those characters which are present at an even index number
string=input('enter the string:')
print(string[::2])


# In[1]:


#to print all the prime numbers in a given interval and also check if a given input number is prime or not
p=0
num=int(input('enter a number:'))
if(num==1):
    print('neither prime nor composite')
else:    
    for i in range(num+1):
         if(num%(i+1)==0):
            p=p+1 
    if(p==2):
        print('prime number')
    else:
        print('not a prime number')
        
def even_number_in_given_interval(n1,n2):
    a=[]
    for i in range(n1,n2+1):
        for j in range(2,i-1):
            if(i%j==0):
                break
        else:
            a.append(i)
    return(a)

num1=int(input("Enter the starting point: "))
num2=int(input("Enter the ending point: "))

prime_num=even_number_in_given_interval(num1,num2)
print("Prime no.s are: ",prime_num)


# In[2]:


#Write a python program to print the Fibonacci series and also check if a given input number is Fibonacci number or not.

def fibonacci_series(n1,n2,n3):
    a=[n1,n2]
    count=n3
    while(count>2):
        sum=n1+n2
        n1=n2
        n2=sum
        count-=1
        a.append(sum)
    return(a)    

num1=int(input("Enter the 1st no: "))    
num2=int(input("Enter the 2nd no: "))
num3=int(input("Enter upto how many terms: "))
final_series=fibonacci_series(num1,num2,num3)
print("The final fibonacci series is: ",final_series)

import math
def check_perfect_square(x):
    s=int(math.sqrt(x))
    return s*s==x

def check_fibonacci_no(n):
    r1=check_perfect_square(5*n*n+4)
    r2=check_perfect_square(5*n*n-4)
    return r1 or r2

num=int(input("Enter the no. to be checked: "))

if (check_fibonacci_no(num)==True):
    print(num,"is a fibonacci no.")
else:
    print(num,"is not a fibonacci no.")


# In[ ]:





# In[ ]:




