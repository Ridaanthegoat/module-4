def Ridaan(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
           print("*",end="")
           iteration+=1
        print("")
    print("\nWhen n is ", n ,"iteration =" , iteration,"\n")

Ridaan(10)
Ridaan(20)
Ridaan(30)
