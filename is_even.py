n = int('введите число которое хотите узнать: ',input()) # вводим число
def is_even(n):
    if n % 2 == 0: # если число делится на 2 без остатка то число четное
        return print('число четное') # число четное
    else:
        return print("число не четное") # число не четное
result = is_even(n)
print(result)