vowels = "aeiou"
sentence = "A speech sound that is produced by comparatively open configuration of the vocal tract."
counts = {"cons": 0, "vowels": 0 }
for char in sentence:
    if not char.isalpha():
        continue
    if char.lower() in vowels:
        counts["vowels"] += 1
    else:
        counts["cons"] += 1
print('No. consonants: ' + str(counts['cons']) + ' | No. vowels: ' + str(counts['vowels']))
