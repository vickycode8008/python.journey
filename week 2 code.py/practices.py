n = int(input("Enter the number:"))   #user data
rev = 0 #reverse value will be 0 
while n>0:
    r = n%10    #for getting last digit
    rev = rev*10+r #for rev value ypu should "*"byu 10 then only you got crt answer otherwise you are get the sum 
    n = n//10  #for removing the last digit
    print(rev) 

