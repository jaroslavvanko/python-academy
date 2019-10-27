myNewDict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 13579}
maximalValueofKey = max(myNewDict.keys())
print("the maximal value of key is",  maximalValueofKey)
if max(myNewDict.values()) > myNewDict[maximalValueofKey]:
    del myNewDict[maximalValueofKey]
print(myNewDict)