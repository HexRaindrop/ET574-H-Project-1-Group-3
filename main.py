from tracker import add_session, view_summary, view_all_session

def main_loop():

    #greeting
    x = input("Welcome to screen time tracker! \n1. Add Screen Time Session\n2. View Summary \n3. View All Sessions\n4. Exit \nEnter choice:  ")
    #pathhing: use the match statment to asign the correct function for the users choise
    match x:
        case "1":
            add_session()
        case "2":
            view_summary()
        case "3":
            view_all_session()
        case "4":
            print("exiting program \nGoodbye.")
            return False
        case _:
            print("⚠ ⚠ ⚠\t invalid input \t\t⚠ ⚠ ⚠ \n⚠ ⚠ ⚠\t error[400]Badrequest,\t⚠ ⚠ ⚠\n⚠ ⚠ ⚠\t please try again using\t⚠ ⚠ ⚠\n⚠ ⚠ ⚠\t the options given\t⚠ ⚠ ⚠")
    return
#call main_loop function and put it in a while loop. the program will continue to run untill our function returns a "False" which we get in case 4
while True:
    if main_loop() == False: break
    else: pass