#!/usr/bin/env python
# coding: utf-8

# ### 02 Feb Assignmet No. 1

# In[ ]:


# Q. 1 Explain with an example each when to use a for loop and a while loop.


# In[1]:


# For Loop: Use a for loop when you know how many iterations you'll need ahead 
# of time or when you wish to iterate over items in a sequence (e.g., lists, tuples, strings) 
# or any other iterable.
# Ex. : Summing up a list of numbers
numbers = [40, 25, 32, 44, 51]


# In[2]:


sum_result = 0

for i in numbers:
    sum_result += i

print(sum_result) 


# In[3]:


# Ex. : Iterating over a string
text = "Hello, Yogesh!"


# In[4]:


for i in text:
    print(i)


# In[10]:


# When you want to repeat a block of code as long as a given condition is true, use a while loop. 
# The loop will continue to execute until the condition is evaluated as False.
# Ex. : Countdown
counter = 85


# In[11]:


while counter > 50:
    print(counter)
    counter -= 1


# In[27]:


# Q. 2 Write a python program to print the sum and product of the first 10 natural 
# numbers using for and while loop.
# Using for loop to calculate the sum and product of the first 10 natural numbers


# In[18]:


# numbers using for loop.
N = 10


# In[24]:


Sum_result = 0
for i in range(N+1) :
    Sum_result += i
print("Using for loop:")
print("Sum of the first 10 natural numbers:", sum_result)


# In[26]:


product_result = 1
for i in range(1, N) :
    product_result *= i
print("Using for loop:")
print("Product of the first 10 natural numbers:", product_result)


# In[1]:


# numbers using while loop.


# In[2]:


# Using while loop to calculate the sum and product of the first 10 natural numbers
n = 10
sum_result = 0
product_result = 1
i = 1

# Calculate sum and product using while loop
while i <= n:
    sum_result += i
    product_result *= i
    i += 1

# Print the results
print("Using while loop:")
print("Sum of the first 10 natural numbers:", sum_result)
print("Product of the first 10 natural numbers:", product_result)


# In[3]:


# Q. 3. Create a python program to compute the electricity bill for a household. 
# The per-unit charges in rupees are as follows: For the first 100 units, 
# the user will be charged Rs. 4.5 per unit, for the next 100 units, 
# the user will be charged Rs. 6 per unit, and for the next 100 units, 
# the user will be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit. 
# You are required to take the units of electricity consumed in a month from the user as input.


# In[5]:


def calculate_electricity_bill(units):
    first_100_units_rate = 4.5
    next_100_units_rate = 6
    next_100_units_after_200_rate = 10
    above_300_units_rate = 20

    total_bill = 0

    if units <= 100 :
        total_bill = units * first_100_units_rate
    elif units <= 200 :
        total_bill = 100 * first_100_units_rate
        remaining_units = units - 100
        total_bill += remaining_units * next_100_units_rate
    elif units <= 300 :
        total_bill = 100 * first_100_units_rate + 100 * next_100_units_rate
        remaining_units = units - 200
        total_bill += remaining_units * next_100_units_after_200_rate
    else :
        total_bill = 100 * first_100_units_rate + 100 * next_100_units_rate + 100 * next_100_units_after_200_rate
        remaining_units = units - 300
        total_bill += remaining_units * above_300_units_rate

    return total_bill

def main():
    try:
        units_consumed = float(input("Enter the number of units of electricity consumed in a month: "))
        if units_consumed < 0:
            print("Invalid input. Units consumed cannot be negative.")
        else:
            bill_amount = calculate_electricity_bill(units_consumed)
            print(f"Electricity bill amount: Rs. {bill_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number of units.")

if __name__ == "__main__":
    main()


# In[6]:


# Q. 4 Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each 
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print 
# that list.


# In[7]:


# For loop


# In[8]:


numbers_list = list(range(1, 101))
cubes_divisible_by_4_or_5 = []

for num in numbers_list:
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        cubes_divisible_by_4_or_5.append(num)

print("Numbers whose cube is divisible by 4 or 5:")
print(cubes_divisible_by_4_or_5)


# In[9]:


# While loop


# In[10]:


numbers_list = list(range(1, 101))
cubes_divisible_by_4_or_5 = []
index = 0

while index < len(numbers_list):
    num = numbers_list[index]
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        cubes_divisible_by_4_or_5.append(num)
    index += 1

print("Numbers whose cube is divisible by 4 or 5:")
print(cubes_divisible_by_4_or_5)


# In[11]:


# Q. 5  Write a program to filter count vowels in the below-given string. 
string = "I want to become a data scientist"


# In[14]:


def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

def main():
    input_string = "I want to become a data scientist"
    vowel_count = count_vowels(input_string)
    print("Number of vowels in the string:", vowel_count)

if __name__ == "__main__":
    main()


# In[ ]:




