import pyttsx3

engine = pyttsx3.init()

while True:
    password = input("Enter your password: ")

    if password == "abc123":
        print("Password accepted")
        engine.say("Password accepted " )
        engine.runAndWait()
        break   # exit loop after correct password
    else:
        print("Incorrect password, please try again")
        engine.say("Incorrect password, please try again")
        engine.runAndWait()
