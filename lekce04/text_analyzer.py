'''
author = Jaroslav Vanko
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
# Greet users in app and check password
data = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
print("Welcome my lord. Please login in app.")
username = input("Please lord, enter your username:")
password = input("Please lord, enter your password:")
if data.get(username) == password:
    print("Everything is all right")
else:
    data.get(username) != password
    print("Password or username is wrong, my lord")
    print("Access denied")
    quit()

print("=" * 50)
# Selecting text
print("We have 3 texts to be analyzed.")
result = 0
selection = input("Enter the number btw. 1 and 3 to select:")
if not selection:
    print("We need number!")
    quit()
elif not selection.isnumeric():
    print("We need only number!")
    quit()
elif selection not in ["1", "2", "3"]:
    print("We need number btw 1 and 3!!")
    quit()
else:
    result = int(selection)
print("=" * 50)
# Calculate words in selected text, lowercase, titlecase, uppercase, numeric string

text = TEXTS[result - 1]
words = text.split()
just_words =[]
for words in just_words:
    just_word = words.pop()
    just_word = just_word.strip(",.:")
    if just_word:
        just_words.append(just_word)
print("There are", len(just_words), "words in selected text.")

# titlecase, uppercase, lowercase, numeric

i = 0
for w in just_words:
    if w[0].isupper():
        i = i + 1
print("There are ", i, "titlecase words.")
i = 0
for x in just_words:
    if x.isupper():
        i = i + 1
print("Thera are ", i, "uppercase words.")
i = 0
for y in just_words:
    if y.islower():
        i = i + 1
print("There are ", i, "lowercase words.")
i = 0
for z in just_words:
    if z.isnumeric():
        i = i + 1
print("There are", i, "numeric string. ")
print("=" * 50)
# Create a bar chart depicting the frequencies of word lengths in the text

word_length = {}
for w in just_words:
    length = len(w)
    if length in word_length:
        word_length[length] = word_length[length] + 1
    else:
        word_length[length] = 1

for key, value in sorted(word_length.items()):
    print(key, "*" * value, value)
# Sum all numeric words
def calsum(l):
    return sum([int(i) for i in l if type(i) == int or i.isdigit()])
sum_list = just_words
print("=" * 50)
print("If we summed all the numbers in this text, we get:", calsum(sum_list))
print("=" * 50)