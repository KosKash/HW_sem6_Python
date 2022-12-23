# расстояние в 2D
#     old_code
# import math
# x_1 = int(input("Введите X1 "))
# y_1 = int(input("Введите Y1 "))
# x_2 = int(input("Введите X2 "))
# y_2 = int(input("Введите Y2 "))
# dist = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
# print(round(dist, 3))

import math
coor = list(map(float,(input('Введите X1 Y1 X2 Y2 через пробел ')).split()))
dist = math.sqrt(((coor[2]-coor[0])**2)+((coor[3]-coor[1])**2))
print(round(dist,3)) 