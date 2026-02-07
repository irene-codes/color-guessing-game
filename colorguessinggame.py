
import random
x=['red','green','blue','black']
while True:
    for i in x:
        print(i, end=' ')
    n = input('\nenter your choice')
    c = random.choice(x)
    print(c)
    if c == n:
        print("you won")
    else:
        print("try again")
    b = input("do u want to continue playing (yes/no)")
    print(b)
    if b != 'yes':
        break
    else:
        continue