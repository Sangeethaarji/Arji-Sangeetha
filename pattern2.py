for i in range(1,5):
    for j in range(1,8):
        if (i+j==5 or j-i==3 or i==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
