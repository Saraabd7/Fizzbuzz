from Fizzbuzz_finction import *
# ==== test one ====
# Check to see if number is divisible by mod
# Is divisible by should return true if number is divisible  by mod
# Is divisible by should return false if number is  not divisible  by mod
# Function (my_inputs) -->  expected results
# Is divisible by (10,5) --> True

# add(2,3) == 5
# is is_divisible_by(10, 5) == True
# is is_divisible_by(11, 5) == False

print(is_divisible_by(9, 3) == True)
# return 9 ∞ 3 == 0
# it will print true because 9 % 3 = 0
# return (0) == 0
# return True

# print()
# def add(x, y)
#     return x + y
# This function returns a boolean (true, false)
# def is_divisible_by(number, mod) == False
# return number ∞ mod == 0


print(is_divisible_by(20, 5) == False)

# Test function 2:
# If i call play_bizzzzuu with the number 4
# It should return 4
print('Test two')
print(play_bizzzzuu(4) == 4)
print(play_bizzzzuu(4) == '4')

print(play_bizzzzuu(7) == 7)
print(play_bizzzzuu(7) == 5)
print(play_bizzzzuu(9) == 'bizz')

# number 9 will take bizz and print true because as it in the main so it will be 9 % 3 == 0 print bizz
# for '4' will print false because it won't give me a number.

# def play_bizzzzuu(number):
#     if is_divisible_by(number, 3) and is_divisible_by(number, 5):
#         return("bizzzzuu")
#     # if it is a multiple of 3 it returns bizz
#     elif is_divisible_by(number, 3):
#         return("bizz")
#     # if a multiple of 5 it return zzuu
#     elif is_divisible_by(number, 5):
#         return("zzuu")
#     # if a multiple of 3 and 5 it return bizzzzuu
#     else:
#         return(number)
