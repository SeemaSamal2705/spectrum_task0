#!/usr/bin/env python
# coding: utf-8

# PYTHON SOLUTIONS

# In[10]:


#1.Create an inner function to calculate the addition in the following way
#   ⦁Create an outer function that will accept two parameters ‘a’ and ‘b’ 
#   ⦁Create an inner function inside an outer function that will calculate the addition of ‘a’ and ‘b’ 
#   ⦁At last, an outer function will add 5 into addition and return it"""


def outerFun(a,b):
    def innerFun(a,b):
        return a+b
    return innerFun(a,b)+5

num1=int(input("Enter the 1st no: "))
num2=int(input("Enter the 2nd no: "))

result = outerFun(num1,num2)
print(result)


# In[3]:


#2.Given input String of combination of the lower and upper case ,arrange characters in such a way that alllowercase letters should come first.

inputStr = "PYTHONtask"
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedstring =''.join(lower+upper)
print("\narranging characters giving precedence to lowercase letters:")
print(sortedstring)


# In[4]:


#3.Given a Python list, remove all the even number from the list and save those even number in another list and print both the lists.

inputlist=[1,2,3,4,5,6,7,8,9,10]
even=[]
for i in inputlist:
    if (i%2==0):
       inputlist.remove(i)
       even.append(i)

print("The Input List after removing even no.s: ")        
print(inputlist)

print("The another list with even no.s: ")
print(even)


# In[5]:


#4.Get the key corresponding to the minimum value from the following dictionary using appropriate python.

d = {'physics':88 , 'maths':75, 'chemistry':72, 'Basic electrical':89}
min(d, key=d.get) 


# In[6]:


#5.Given two Python sets, update first set with items that exist only in the first set and not in the second set .

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,3,4,6,8,11,22,34,51,67}

set1.difference_update(set2)
print(set1)


# In[7]:


#6. Program to create simple calculator in Python which on input of 1,2,3,4 should add , subtract , multiply and divide respectively.

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

select = int(input("Select operations form 1, 2, 3, 4 : ")) 

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
  
if select == 1: 
    print(num1, "+", num2, "=", add(num1, num2)) 
  
elif select == 2: 
    print(num1, "-", num2, "=", subtract(num1, num2)) 
  
elif select == 3: 
    print(num1, "*", num2, "=", multiply(num1, num2)) 
  
elif select == 4: 
    print(num1, "/", num2, "=", divide(num1, num2)) 
else: 
    print("Invalid input")


# ## Pandas Solutions 

# In[1]:


import pandas as pd


# In[2]:


# Read the csv file and print the first 5 rows
df = pd.read_csv("diamonds.csv")


# In[3]:


df.head(5)


# In[4]:


# Print the content of a series of the dataframe provided to us
df["carat"]


# In[5]:


# Value count
df.cut.value_counts()


# In[6]:


# Display the max price for each type of cut 
df.groupby(["cut"])["price"].agg("max")


# In[7]:


# Display the min price for each type of cut 
df.groupby(["cut"])["price"].agg("min")


# In[8]:


# Display the count of prices for each type of cut 
df.groupby(["cut"])["price"].agg("count")


# In[9]:


# pandas to check the no of rows and columns
df.columns


# In[10]:


# The no of rows and columns are given by the shape 
print(f"The no of rows : {df.shape[0]}\nThe no of columns : {df.shape[1]}")


# In[11]:


# check if any na is present in the dataframe
df.isna().sum()


# ***Here there are no nan values present, hence we need not drop any row***

# In[12]:


df.dropna().shape


# ***Here we see that shape before drop na and after drop na remains same***

# In[13]:


df.duplicated(subset = df.columns, keep = False).sum()


# ***Even there are no duplicates of any rows present hence the final answer becomes zero***

# In[20]:


df[df.duplicated() == "True"]


# ***Here we see that we are getting no duplicated rows***

# In[15]:


shuf_df = df.sample(frac = 1)
size = int(0.75*shuf_df.shape[0])
df = shuf_df[:size]
test_df = shuf_df[size:]


# ***Here we did the splitting of the dataset***

# In[16]:


df


# In[17]:


test_df


# In[18]:


print(f"The no of rows in df : {df.shape[0]}\nThe no of columns in new_df : {test_df.shape[0]}")


# ***Here df-----> the 75% sample dataset, test_df------> the newly made 25% dataset***

# <br><br><center><b>--------------------------*******--------------------------</b></center>
