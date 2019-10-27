num_repeat = int(input('Enter the # of repetitions: '))
sentence = input('Enter the string: ')

words = sentence.split()

result = []

while words:
    word = [words.pop(0)]
    word = word * num_repeat
    result = result + word

result = " ".join(result)
print(result)