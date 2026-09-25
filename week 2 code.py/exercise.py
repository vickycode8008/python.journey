for i in range(1,6):   #using for loop we assign the range value
    print('*'* i)      #Using the print statement we print the start 

# anthor code 
for i in range(1,6):
 for j in range(1,6):
   if i==j or i>=j:
    print('*',end='')
 print('') 