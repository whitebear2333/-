import math
a = int(input('a值？'))
b = int(input('b值？'))
c = int(input('c值？'))
print('判别式的值为')
print((b ** 2) - 4 * a * c)
if ((b ** 2) - 4 * a * c) >= 0:
        print("方程的两个解分别为：")
        print((-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a))
        print((-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a))
else:
        print("此方程无解")




