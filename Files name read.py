file = open('name.txt', mode='r')
name = file.read().strip()
print('Your name is ', name)
file.close()