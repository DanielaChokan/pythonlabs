from mod import product
import math

def expression (x):

    return (1- 2 * (math.sin(x))**2 / (1 + (math.sin(x))**2))

x = int(input("Введіть значення x: "))

print ("Значення виразу = ",float('{:.4f}'.format(expression(x))))

x = int(input("Введіть від якого числа х знаходити суму парних чисел: "))

y = int(input("Введіть до якого числа y знаходити суму парних чисел: "))

while x > y:

    x = int(input("у не може бути менше за х, введіть ще раз значення x: "))

    y = int(input("Введіть ще раз значення y: "))

print("Сума парних чисел від х до у = ", product (x, y))
