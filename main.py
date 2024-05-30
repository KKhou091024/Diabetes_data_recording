import json


def take_in():
    date = str(input("Enter the date "))
    typeinput = input("""enter the type of data being recorded 
    1. empty stomach 
    2. pre-meal
    3. post meal\n""")
    if typeinput != "b":
        try:
            typeinput = int(typeinput)
        except ValueError:
            print("Error, try again")
            take_in()
    if typeinput == 1:
        typeinput = "empty stomach"
    elif typeinput == 2:
        typeinput = "pre-meal"
    elif typeinput == 3:
        typeinput = "postmeal"
    else:
        take_in()
    sugarinput = input("what are your sugar levels? ")
    if sugarinput != "b":
        try:
            sugarinput = int(sugarinput)
        except ValueError:
            print("An error ocuured")
            UI()
    else:
        UI()
    sugarvalue = sugarinput/18
    sugarvalue = float((round(sugarvalue, 1)))
    results = {"date": date, "type": typeinput, "sugar level": sugarvalue}
    if date == "b" or typeinput == "b":
        UI()
    return results


def update():
    with open('diabetes info.txt', 'a') as convert_file:
        convert_file.write(json.dumps(intake))
        convert_file.write("\n")
        convert_file.close()


def show():
    f = open("diabetes info.txt", 'r')
    print()
    print(f.read())
    f.close()


def UI():
    global intake
    while True:
        print("""1.add to data 
2.show data
3.quit 
b. back (Works at all times(make sure it is lowercase))""")
        inp = input("type the number of the operation you would like to use: ")
        try:
            inp = int(inp)
        except ValueError:
            print("try again, that was not one of the options")
        if inp == 1:
            intake = take_in()
            update()
        elif inp == 2:
            show()
        elif inp == 3:
            break
        elif inp == "b":
            UI()
        else:
            UI()


UI()
