file = open('numbers.txt', 'r')
total = 0
for line in file:
    number = int(line)
    total += number
print(total)
file.close()