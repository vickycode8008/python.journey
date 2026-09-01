#palindrome check 
n = int(input("Enter the number:")) 
rev = 0
a = n #for store value n at one variable bcoz, it easy to check it pali or not
while n>0:
    r = n%10
    rev = rev*10+r #just reversse the value
    n = n//10
if rev == a: #used to check it pali or not
    print("palindrome")
else:  #if not
    print("Not palindrome")