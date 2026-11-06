import sys

bookName = sys.argv[1]
testText = "the cat sat on the mat. the cat ate the fish. the dog sat on the cat."
bookLocation = f"books/{bookName}"

# with open(bookLocation) as f:
#    print(f.read())


testList = testText.split()

# version A
testDict = {}

for i in range(0, len(testList) - 1):
    if testList[i] not in testDict:
        testDict[testList[i]] = list()
    testDict[testList[i]].append(testList[i + 1])

    print(f"{testList[i]} -> {testList[i + 1]}")
# version B
testDictB = {}
for i in range(0, len(testList) - 1):
    if testList[i] not in testDictB:
        testDictB[testList[i]] = dict()
    if testList[i + 1] not in testDictB[testList[i]]:
        testDictB[testList[i]][testList[i + 1]] = 0

    testDictB[testList[i]][testList[i + 1]] += 1


print(testList, len(testList))
print(testDict)
print(testDictB)
