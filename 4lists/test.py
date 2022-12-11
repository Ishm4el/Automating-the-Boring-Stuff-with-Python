row = 3
col = 3
for x in range(row):
    for y in range(col):
        print(x, y)
        print((x - 1) % row)

a = -3 % 3
print()
print(a)

print()
print('a' == 'a')

print()
spam = ['a', 'b', 'c']
print(len(spam))
for i in range(len(spam)):
    print(i)
