""" 
1.You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351]
your task is to create two List one which have all the Even Numbers 
and another List which will have all the ODD numbers in it?
 """

my_list =  [10, 501, 22, 37, 100, 999, 87, 351] 
my_even_list = []
my_odd_list = []

for i in my_list:
    if i % 2 == 0:
        my_even_list.append(i)
    else:
        my_odd_list.append(i)
        
print("Even numbers list:", my_even_list)
print("Odd number list:", my_odd_list)

