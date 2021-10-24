def print_triangle(n):
    z = 1
    for i in range(n):
        for j in range(i+1):
            print(z,end = " ")
            z= z+1 
        print("\r")

print_triangle(3)
            

