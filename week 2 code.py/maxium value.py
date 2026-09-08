n = 3  #assign value for you want
i = 0 #consider starting 0 
max = 0 #maximum value will be 0
print("Enter" , n , "number") #print the value of n 
while i < n: #check whether the value will be i < n
    i += 1 #add value 1 each excutes
    x = int(input(""))  #enter the number
    if x > max : #if condition for check the maxmium value
        max = x # if "x > max" store the value in max
    else : #else condition
        print("MAX : ",max)  #print the value in max 