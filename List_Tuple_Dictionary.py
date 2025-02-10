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
