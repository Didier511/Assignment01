#Task5.Assignment: while loop
#Password Attempts:(Limmited tries)
correct_password="secret"
user_attempt=3
attempt_left=3
while attempt_left>0 and user_attempt!=correct_password:
    user_attempt=input(f"Enter password(Attempts left,{attempt_left}): ")
    if user_attempt==correct_password:
        print("Acces Granted!")
    else:
        print("Acces Denied!")
    attempt_left-=1

