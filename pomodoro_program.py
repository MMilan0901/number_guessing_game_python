# Pomodoro Program

import time

print("Welcome in my Pomodoro Program!")
print("If you enter 'START', the program will set a 25-minutes timer.")
print("After 25 minutes you can start again or quit.")
print("")

while True:

    user_input = input("START or QUIT? ")
    
    if user_input == 'START':
        print("Timer has started...")
        time.sleep(1500)                # 25 mins = 1500 secs
        print("Timer has stopped.")
        print("You've got 5 minutes of break now...")
        time.sleep(300)
        print("Your break is over.")
    elif user_input == 'QUIT':
        break
    else:
        print("Please, try again!")
