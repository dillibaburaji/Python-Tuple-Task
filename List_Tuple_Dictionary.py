""" 
1.You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351]
your task is to create two List one which have all the Even Numbers 
and another List which will have all the ODD numbers in it?
 """

my_list =  [10, 501, 22, 37, 100, 999, 87, 351] # Given list
my_even_list = []   #even empty list
my_odd_list = []    #odd empty list

for i in my_list:
    if i % 2 == 0: 
        my_even_list.append(i)
    else:
        my_odd_list.append(i)
        
print("Even numbers list:", my_even_list)
print("Odd number list:", my_odd_list)

"""
2.Given a Python List [10, 501, 22, 37, 100, 999, 87, 351]-your task 
is to Count all the Prime Numbers and create a new Python List which will contain all the Prime Numbers in it?
"""
def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 501, 22, 37, 100, 999, 87, 351] # Given list
                       
prime_numbers = [] # prime numbers empty list
for num in numbers:
    if prime_number(num):
        prime_numbers.append(num)
        
prime_count = len(prime_numbers) # Count the number of prime numbers

print("Prime Numbers:", prime_numbers)
print("Count of Prime Numbers:", prime_count)


"""3.Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] 
Find out how many numbers are there in the given Python List which are Happy Numbers ?
"""
def happy_num(n):   
    rem =0
    sum =0
    while (n > 0):    #square each digit
        rem = n%10    
        sum = sum + (rem*rem)    
        n = n//10
    return sum == 1   #if sum reach 1 it is happpy number
        
    
my_list = [10, 501, 22, 37, 100, 999, 82, 87, 351] #given list
happy_number_list =[]
for num in my_list:
    if happy_num(num):
        happy_number_list.append(num) 
print(happy_number_list)
print("In Given list happy number is ", len(happy_number_list))

""""4. Write a python program to find the sum of the first and last digit of an integer?""""

def first_digit(n): # Function for first digit of a number
    while n >= 10:  # this loop Keep dividing until we get the first digit
        n = n // 10
    return n        
             
def last_digit(n):   # Function for last digit of a number
    return n % 10  

print("Please enter an integer number:") # Take user input
number = int(input())  # Convert input to an integer

first = first_digit(number)
last = last_digit(number)
sum_of_first_last_digit = first + last
print("Sum of first and last digit:", sum_of_first_last_digit)
