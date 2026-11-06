import sys

bookName = sys.argv[1]
testText = "the cat sat on the mat. the cat ate the fish. the dog sat on the cat."
bookLocation = f"books/{bookName}"

# with open(bookLocation) as f:
#    print(f.read())


testList = testText.split()


testDict = {}

for i in range(0, len(testList) - 1):
    if testList[i] not in testDict:
        testDict[testList[i]] = list()
    testDict[testList[i]].append(testList[i + 1])

    print(f"{testList[i]} -> {testList[i + 1]}")


print(testList, len(testList))
print(testDict)
