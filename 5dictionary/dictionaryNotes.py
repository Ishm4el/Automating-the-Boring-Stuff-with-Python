# Dictionary Data Type:
# mutable
# collection of many values
# indexes for dictionaries are called 'keys'
# and a key is associated value is called a 'key-value pair'
# typed with a brace { }
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('printing myCat')
print(myCat)
print()
print('printing myCat "size"')

## dictionaries vs Lists
# items in a dictionary are unordered
spam = ['cat', 'dog']
bacon = ['dog', 'cat']
eggs = {'color': 'blue', 'size': 'large'}
ham = {'size': 'large', 'color': 'blue'}
print('spam', spam)
print('bacon', bacon)
print('eggs', eggs)
print('ham', ham)

print('\ncompare spam and bacon')
print(spam == bacon)

print('\ncompare eggs and ham')
print(eggs == ham)
print()

## keys(), values(), and itemss() methods
print('looping through keys()')
for k in myCat.keys():
    print(k)
print()

print('looping through values()')
for v in myCat.values():
    print(v)
print()

print('looping through items()')
for i in myCat.items():
    print(i)
print()

print('looping through items() using i and j')
for i, j in myCat.items():
    print('key: ' + i + ', value: ' + j)
print()

print('converting myCat.keys() to a list')
listCat = list(myCat.keys())
print(listCat)
print()

## checking whether a key or a value exists in a dictionary
# x in spam.key() is equivalent to x in spam
# x in spam.values() 
print("'size' in myCat")
print('size' in myCat)
print("'size' in myCat.values()")
print('size' in myCat.values())
print()

## get() method
# checks if a key exists with a fallback method
print("myCat.get('age', 3)")
print(myCat.get('age', 3))
print("myCat.get('color', 'white')")
print(myCat.get('color', 'white'))
print()

## setdefault(key, value)
# ensures if a key exists, if not insert it
print("myCat.setdefault('fav food', 'steak')")
print(myCat.setdefault('fav food', 'steak'))
print("myCat.setdefault('color', 'white')")
print(myCat.setdefault('color', 'white'))
print()

## pretty printing
# import pprint
import pprint
phrase = "Shadwos arose from the depths of hells and the moon watched"
count = {}
for character in phrase:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
print()

# We can collect a string version of pprint by using:
# .pformat
pphrase = pprint.pformat(phrase)
print(pprint.pformat(count))
print()

## nested dictionaries
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print("Number of things being brought: ")
print(' - Apples            ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups              ' + str(totalBrought(allGuests, 'cups')))
print(' - cakes             ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches    ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies        ' + str(totalBrought(allGuests, 'apple pies')))
