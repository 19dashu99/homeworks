a = True
b = False
print(a and b)  # True and False = False, т.к. есть хотя бы 1 False
print((a and b) or b)  # False or False = False
print((a and b) or not (a and b))  # False or not(False) = False or True = True
print(a and b or not (a or b) or b)  # 1 and 0 or not(1) or 0 = 1 and 0 or 0 or 0 = 0 or 0 or 0 = 0
print(b and b or not a and (a or b or a) or not (a or b)) # 0 and 0 or not 1 and (1) or not (1) = 0 and 0 or 0 and 1 or 0 = 0
print(1 << 2)  # = 4 .Бинарный сдвиг влево на 2 позиции, т.е. 100, 100 - это бинарная 4
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010)
print(1 & 0 )
