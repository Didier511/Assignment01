#if assignment 5

user_year=int(input("What year is this?: "))
if user_year%4==0:
    print("It's a leap year!")
elif user_year%4!=0:
    print("It's not a leap year")
