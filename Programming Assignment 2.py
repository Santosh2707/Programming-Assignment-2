#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python program to convert kilometers to miles?


# In[3]:


km=float(input("Enter your value in Kilometers: "))
miles=(0.621371)*km
print(km, "Kilometers will be", miles, "miles")


# In[6]:


#2. Write a Python program to convert Celsius to Fahrenheit?


# In[8]:


celsius=float(input("Enter your value in Celcius: "))
fahrenheit=(33.8)*celsius
print(celsius, "Celsius will be", fahrenheit, "Fahrenheit")


# In[9]:


#3. Write a Python program to display calendar?


# In[10]:


import calendar
year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
calendar=calendar.month(year, month)
print(calendar)


# In[11]:


#4. Write a Python program to solve quadratic equation?


# In[17]:


#Quadratic Equation ax**2+bx+c=0
#a, b and c are real numbers
#a!=0
import cmath
a=int(input("Enter number (remember a is not equal to 0): "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))

#Formula for Discriminant
d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))
root2=(-b+cmath.sqrt(d))
print("The roots are", root1, "and", root2)


# In[18]:


#5. Write a Python program to swap two variables without temp variable?


# In[20]:


x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
x,y=y,x
print("After Swapping: \n x=",x,"y=",y)


# In[ ]:




