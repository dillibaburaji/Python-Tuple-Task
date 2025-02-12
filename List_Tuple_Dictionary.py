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

"""
6. You have been given three lists. 
Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists ?
"""
def find_duplicate_list(L1,L2,L3):
    duplicate_list=[]      # List to store duplicate elements
    for i in L1:
            if i in L2 and i in L3 and i not in duplicate_list:   # Check if the item is present in all three lists and not already added
                duplicate_list.append(i)     #adding duplicate element 
    return duplicate_list

first_list=[10,20,30]
second_list=[12,21,34,30]
third_list=[10,20,30,44,44]
print(find_duplicate_list(first_list,second_list,third_list)) 

"""7.Write a python program to find the first non repeating elements in a given list of integers?"""
def first_non_repeating(non_rep):
    
    non_repeating_count = {} # Dictionary to store occurrences and duplication not allowed
    
    for ele in non_rep:
        if ele in non_repeating_count:    
            non_repeating_count[ele]+=1    # Increment count if already in dictionary
        else:
            non_repeating_count[ele]=1       #for first occurrences
        
    for ele in non_rep:
        if non_repeating_count[ele]==1:
            return ele              # Return first non-repeating element

python_list = [10,20,20,20,30,30,4,40]
print(first_non_repeating(python_list))


"""8. Write a python program to find the minimum element in a rated and sorted list ?"""
def find_minimum_ele_list(list_ele):
    if not list_ele:   # checking for empty list
        return None
    minimum_ele_in_list = list_ele[0] # Assume first element is the minimum
    
    for ele in list_ele:
        if ele < minimum_ele_in_list:   
            minimum_ele_in_list = ele    # Update if a smaller element is found in the list
    return minimum_ele_in_list   #return the minimum element in the list

python_list = [10,20,30,1,30,4,5,5,3]

print("minimum ele in list",(find_minimum_ele_list(python_list)))
