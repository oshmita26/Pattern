s = input("Enter a string: ")
n = len(s)
space = 0
for i in range(n, 0, -1):
    print(s[0:i], end='')
    for j in range(0, space):
        print(end='  ')
    print(s[i-1::-1])
    space += 1

space = n - 1
for i in range(1, n+1):
    print(s[0:i], end='')
    for j in range(space, 0, -1):
        print(end='  ')
    print(s[i-1::-1])
    space -= 1
