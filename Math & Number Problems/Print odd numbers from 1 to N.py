n = int(input("Enter the number: "))
for i in range(1, n+1):
    if i%2 != 0:
        if i == n or i == n-1:
            print(i)
        else:
            print(i, end=",")