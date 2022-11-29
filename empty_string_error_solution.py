age = input("How old are you? ")
    # veryfing if input isn't empty

if age:
        # turning string into integer
    age = int(age)
        
        #under 18 can not enter
    if age >= 18 and age <21:
        print("Come in but wear wristbank!")

        # 18-21 wristband
    elif age >= 21:
        print("Come in and have fun with drinking")

        # over 21 free to enter and drink
    else:
        print("You are too young, sorry.")

        # if user inputs empty answer
else:
    print("Please enter your age.")


