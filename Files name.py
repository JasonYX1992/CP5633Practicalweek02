open('data.txt', mode='w')

file = open('name.txt', mode='w')
name = input('Enter your name:')
print(file.write(name))
file.close()

