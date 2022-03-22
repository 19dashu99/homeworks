# Задание 1
# Допишите функцию, которая принимает список, выбирает из него все элементы с четным индексом
# и возвращает их в виде списка

def func1():
    print('Напишите числа: ', end='')
    b = [int(i) for i in input().split()]
    print(f'Введенный список: {b}')
    chet = []
    l1 = []
    for i in b:
        if i % 2 == 0:
            chet.append(i)
    i += 1
    return chet


c = func1()
print(f'Список чётных элементов: {c}')
print('')

# Задание 2
# Допишите функцию, которая принимает список
# и выбирает из него все элементы, которые больше предыдущего и возвращает их в виде списка


def func2():
    l1 = []
    print('Введите список: ', end='')
    l = [int(i) for i in input().split()]
    for i in range(len(l)):
        if l[i] > l[i-1] :
            l1.append(l[i])
    i += 1
    return l1

f = func2()
print(f'Список элементов, которые больше предыдущего: {f}')


# Задание 3
# Допишите функцию, которая принимает список, меняет местами наибольший и наименьший элементы и возвращает этот список
def func3():
    print('Введите список: ', end='')
    l = [int(i) for i in input().split()]
    naim = min(l)
    naib = max(l)
    a = l.index(max(l))
    b = l.index(min(l))
    l.remove(naib)
    l.insert(b, naib)
    l.remove(naim)
    l.insert(a, naim)
    return l


g = func3()
print(f'Меняем местами наиб и наим элементы начального списка и получаем другой список: {g}')


