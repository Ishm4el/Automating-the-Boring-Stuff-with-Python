spam = ['dad', 'mom', 'grandma', 'grandpa']

def printList(dec):
    aString = str()
    for i in range(len(dec)):
        if i != len(dec) - 1:
            aString += dec[i] + ', '
        else:
            aString += dec[i]
    return aString

print(printList(spam))
