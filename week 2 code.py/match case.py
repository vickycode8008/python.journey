#using the match case are also same that if,elif,else condition but here
#  will be use only case condition cxan do the program 

number = int(input("Enter a number:"))
match number:
    case 0:
        print("MONDAY")
    case 1:
        print("TUESDAY")
    case 2:
        print("WEDNESDAY")
    case 3:
        print("THURSDAY")
    case 4:
        print("FRIDAY")
    case 5:
        print("SATURDAY")
    case 6:
        print("SUNDAY")
    case _:
        print("INVALID INPUT")