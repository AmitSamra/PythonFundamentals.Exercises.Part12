# Lab 1 Exercise 6

c_temps = [-32, 0, 16, 32]
f_temps = [(x-32)*(5/9) for x in c_temps]
print(f_temps)

# Lab 2 Exercise 1

a = ['Darth Vader','Guido van Rossum']
b = [f'Hello ' + x for x in a]
print(b)

# Lab 5 list_utils

a = list(range(0,11))
b = [x for x in a if x % 2 != 0]
print(b)

