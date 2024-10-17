import random

original_list = [random.randint(-50, 50) for _ in range(25)]
print("Початковий список:", original_list)

A1 = [num for num in original_list if num > 0]  
A2 = [num for num in original_list if num < 0]  

print("Список додатних елементів (A1):", A1)
print("Список від'ємних елементів (A2):", A2)
