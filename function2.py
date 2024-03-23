def check(n):
    if n%10==5:
        return n**2
    if n%10==3:
        return n**3
    if n%10==6:
        return (n-1)
    else:
        return (n/2)
a=check(15)
print(a)
