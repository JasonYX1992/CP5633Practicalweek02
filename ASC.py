finished = False
result = 0
while not finished:
    try:
        result = int(input('enter a number:'))
        print('valid result is', result)
    except ValueError:
        print('Please enter a valid integer.')
print('valid result is', result)

""" """
def get_number(lower, upper):
    if