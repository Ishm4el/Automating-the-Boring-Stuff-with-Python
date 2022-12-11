import random

streakCounter = 0
streak = 0
head = False
tail = False
side = False
for i in range(10000):
    toss = random.randint(0, 1)
    if toss == 0:
        side = False
    else:
        side = True

    # Check for tail
    if side == False and tail == False:
        tail = True
        head = False
        streak = 1
    elif side == False and tail == True:
        streak += 1

    # Check for head
    elif side == True and head == False:
        tail = False
        head = True
        streak = 1
    elif side == True and head == True:
        streak += 1

    if streak == 6:
        print('STREAK!')
        streakCounter += 1
        streak = 5

print('We got ' + str(streakCounter) + ' streaks!')
print('Chance of streak: %s%%' % (streakCounter / 100))

