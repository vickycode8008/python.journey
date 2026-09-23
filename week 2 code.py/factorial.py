n = int(input("Enter the number:")) #get input from user
for i in range(1,n+1):        #for the range will be 1 to n+1 coz, the value shoulsd be start from 1 anfd end with n +1 boz, 
                              #--then only it will check the v alue to n otherwise they stop beforf n
    if n % i == 0:           #using "%" to print the remainder
        print(i)             #print the value pf i