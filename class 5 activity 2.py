def Ridaan(n):
   
    n=int(input("number of bits="))

    while(n):
        if(n<<(n-1)):
            print("SET")
        else:
            print('NO SET')
    
number=int(input("enter your number here: "))
Ridaan(number)