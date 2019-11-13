# hours1 = int(input('Введите часы: '))
# minut1 = int(input('Введите минуты: '))
# second1 = int(input('Введите секунды: '))
# sec1 = ((hours1*60)*60)
# sec2 = minut1*60
# sec3 = second1
# point1 = sec1 + sec2 + sec3
# hours2 = int(input('Введите часы: '))
# minut2 = int(input('Введите минуты: '))
# second2 = int(input('Введите секунды: '))
# sec21 = ((hours2*60)*60)
# sec22 = minut2*60
# sec23 = second2
# point2 = sec21 + sec22 + sec23
# result = point1-point2
# final_result = abs(result)
# print('Результат: ' + str(final_result) + ' cекунд.')

point1 = input('Введите часы, минуты и секунды через пробел: ').split()
h = int(point1[0])*60*60
m = int(point1[1])*60
s = int(point1[2])
seconds_point1 = h + m + s
point2 = input('Введите часы, минуты и секунды через пробел: ').split()
h2 = int(point2[0])*60*60
m2 = int(point2[1])*60
s2 = int(point2[2])
seconds_point2 = h2 + m2 + s2
all_seconds = seconds_point1 - seconds_point2
result = abs(all_seconds)
print('Результат: ' + str(result) + ' cекунд.')
