data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)

letters.append(True)

numbers.insert(numbers.index(3)+1, 2)

numbers.sort()

letters.reverse()

letters[1] = 'G'
letters[7] = 'c'

numbers = [x ** 2 for x in numbers]

letters = tuple(letters)
numbers = tuple(numbers)
print("letters: " + str(letters))
print("numbers: " + str(numbers))

