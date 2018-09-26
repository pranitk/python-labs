oldList = [1,2,4,9,17,25,53]
numToBeInserted = 13


def insertNum(oldList,number):

    if isinstance(number,int) == False:
        print("1. Argument passed as a number is invalid")
        return

    if isinstance(oldList,list) == False:
        print("1. Argument passed as a list is invalid")
        return
    
    insertionIndex = 0

    # Search for the correct position for the number
    for index in range(len(oldList)):
        if oldList[index] <= number and oldList[index+1] >= number:
            insertionIndex = index+1

    print("1)")
    if insertionIndex == len(oldList):  # The number needs to be inserted at the end of the list
        newList = oldList[0:insertionIndex] + [number]

        print("OldList = ",oldList)
        print("NewList = ",newList)
        #print(newList)
    else:
        newList = oldList[0:insertionIndex] + [number] + oldList[insertionIndex:]

        print("OldList = ",oldList)
        print("NewList = ",newList)

insertNum(oldList,numToBeInserted)


def calculateBounceDistance(height,numOfBounces):
    
    if numOfBounces <= 0 or height <= 0:
        print("Invalid height or number of bounces")
        return 0

    totalDistance = height

    remainingHeight = height/2  # Height reduces to half after each bounce
    remainingBounces = numOfBounces

    while remainingBounces > 1:
        totalDistance += remainingHeight*2  
        remainingHeight = remainingHeight/2 # Height reduces to half after each bounce
        remainingBounces -= 1

    totalDistance += remainingHeight    # Add the final bounce distance
    print("After bouncing %s times, the ball bounces back to %s meters height"%(numOfBounces,remainingHeight))

    return totalDistance
    



print("\n2)")
totalDistanceByBall = calculateBounceDistance(100,3)
if totalDistanceByBall > 0:
    print("The total distance travelled by the ball is %s meters"%totalDistanceByBall)


# -------------- Functions required for Part 3 of assignment -----------------
inputDict = {'a': 97, 't': 116, 'w': 119,
'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k':
107, 'j': 106, 'm': 109, 'l': 108, 'o': 96, 'n': 110, 'q': 113, 'p': 112, 's': 115,
'r': 114, 'u': 117, 'v': 118, 'y': 121, 'x': 120, 'z': 122}



def sortDictionary():
    sortedKeys = sorted(inputDict)   
    newDict = {}

    # Form a dictionary with sorted order...
    for key in sortedKeys:
        newDict[key] = inputDict[key]

    return newDict

def fixDictValues():
    flag = False    # Helps to know if a fix was required

    for key,value in inputDict.items():  # iterate over the dictionary
        if value != ord(key):
            print("\nFound wrong value for ",key)
            flag = True
            inputDict[key] = ord(key)
    
    if flag == False:
        print("No fix required in the dictionary")
    else:
        print("Here is the fixed dictionary -> ",inputDict)

def generateUpperCaseDict():
    upperCaseDict = {}
    for key,value in inputDict.items():
        upperCaseValue = value - 32 # 32 is the difference between ASCII values of upper & lower case letters
        newChar = chr(upperCaseValue)   # Get the char from the ASCII value
        upperCaseDict[newChar] = upperCaseValue

    return upperCaseDict


def combineDict(lowerCaseDict,upperCaseDict):

    if isinstance(lowerCaseDict,dict) == False or isinstance(upperCaseDict,dict) == False:
        print("\nCannot combine dictionary. Pass valid dictionaries")
        return

    combinedDict = lowerCaseDict.copy()
    combinedDict.update(upperCaseDict)

    print("\nCombined dictionary ->",combinedDict)


def convertDictToHexa():

    try:

        for key,value in inputDict.items():
            hexaValue = hex(value)
            inputDict[key] = hexaValue

        print("\nHexa decimal converted dictionary -> ",inputDict)

    except error:
        print("\nCould not convert dictionary to Hex decimal values")
#-----------------------------------------------------------

#1
inputDict = sortDictionary()
print("\n3)\nSorted dictionary -> ",inputDict)

#2
fixDictValues()

#3
upperCaseDict = generateUpperCaseDict()
print("\nDictionary with upper case letters ->",upperCaseDict)

#4
combineDict(inputDict,upperCaseDict)

#5
convertDictToHexa()