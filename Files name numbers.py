open('numbers.txt', mode='r')

file = open('numbers.txt', mode='r')
number1 = int(file.readline())
number2 = int(file.readline())
print(number1 + number2)
file.close()

