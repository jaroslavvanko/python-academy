words = ['Python', 'is', 'a', 'widely', 'used',
        'high-level', 'programming', 'language',
        'for', 'general-purpose', 'programming,',
        'created', 'by', 'Guido', 'van', 'Rossum',
        'and', 'first', 'released', 'in', '1991.']

# 1.
max_word = ('',0)

while words:
    # 2.
    word = words.pop(0)
    # 3.
    if len(word) > max_word[1]:
        # 4.
        max_word = word, len(word)
# 5.
print(max_word)