command = ""
started = False

while True:
    command = input("> ")
    if command == "start":
        if not started:
            print("car started...")
            started = True
        else:
            print("The car is already started!")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car      
quit - to quit  
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
