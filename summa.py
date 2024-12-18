def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
gcd1 = gcd(a, b)
print("НОД: ")
print(gcd1)