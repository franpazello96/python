# A

def pot(num, n):
    if num == 0:
        return 1
    elif num == 1:
        return num
    else:
        p = 1
        for i in range(n):
            p += num
        return p

print(pot(2,8))

#B

def pot(num, n):
    if n == 0:
        return 1
    elif n == 1:
        return num
    else:
        return num * pot(num, n-1)
pot(2, 10)
