def f(n,m):
    if m==0:
        return 1
    return n*f(n,m-1)
a=f(2,3)
print(a)

        
