n = 3                                         #assign value for you want
i = 0                                          #consider starting 0 
min = 0                                         #maximum value will be 0
print("Enter" , n , "number")                   #print the value of n 
while i < n:                                    #check whether the value will be i < n
    i += 1                                       #add value 1 each excutes
    x = int(input(""))                           #enter the number
    if min < x :
        print(min)                               # if "x > max" store the value in max
    else:                                           #else condition
        print("MIN : ",min)                         #print the value in max 