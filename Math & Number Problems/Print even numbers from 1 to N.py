n = 7
first = True
for i in range(1, n+1):
    if i%2==0:
        if first:
            print(i, end="")
            first = False
        else:
            print(",", i, end="")