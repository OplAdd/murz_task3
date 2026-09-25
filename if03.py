# If3. Положительное +1, отрицательное -2, ноль заменить на 10.
number = int(input())
if number > 0:
    number += 1
elif number < 0:
    number -= 2
else:
    number = 10
print(number)
