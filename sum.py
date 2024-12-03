def summ(num):
    Sum = 0 # начальное значение
    for i in num: 
        Sum = Sum + i # находим находим сумму всех чисел в списке
    return Sum

print('сумма всех чисел в списке:',summ([1,3,5,7,9]))
