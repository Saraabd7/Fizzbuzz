# def is_fizz(number):
#     (number % 3 == 0)
#     return number % 3 == 0
# # The number is boolean here because it is returning True or False.
#
# # my_number = is_fizz()
# # print(my_number)
# # print(type(my_number))
#
# def is_buzz(number):
#     (number % 5 == 0)
#     return number % 5 == 0
#
# def check_number(number, mod):
#     return number % mod == 0
# mod is 5 or 3 and we used this function to not be similar.

# check_number(number, mod)
# return number % 3 ==0 // return number % 5 == 0



def is_divisible_by(number, mod):
    return number % mod == 0

def play_bizzzzuu(number):
    if is_divisible_by(number, 3) and is_divisible_by(number, 5):
        return("bizzzzuu")
    # if it is a multiple of 3 it returns bizz
    elif is_divisible_by(number, 3):
        return("bizz")
    # if a multiple of 5 it return zzuu
    elif is_divisible_by(number, 5):
        return("zzuu")
    # if a multiple of 3 and 5 it return bizzzzuu
    else:
        return(number)