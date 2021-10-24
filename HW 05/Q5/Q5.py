def pyramid(r):
    n=0
    #Rows
    for i in range(1,r+1):
        k=0
        #Spaces
        for s in range (1, r-i+1):
            print(end=" ")
        #Stars 
        while k < i:
            print("* ", end="")
            k += 1
        print()

pyramid(5)

