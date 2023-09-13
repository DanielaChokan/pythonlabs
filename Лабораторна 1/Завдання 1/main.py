a = int(input ("Введіть значення а: "))

while (a < 1 or a > 100):

    a = int(input ("Введіть ще раз значення а: "))

b = int(input ("Введіть значення b: "))

while (b < 1 or b > 100):

    b = int(input ("Введіть ще раз значення b: "))

if a < b:

    x = (b / a + 1)

elif a == b:

    x = 25

else:

    x = (a - 5) / b

print("Результат обчислення виразу: " , x)
