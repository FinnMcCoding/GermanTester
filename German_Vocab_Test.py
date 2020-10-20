import numpy as np
import random




def test():
    file = open("GermanDictionary.txt", "r")

    translations = file.read().split("-")
    for i in range(0, len(translations)): translations[i] = translations[i].split(';')
    path = np.array(translations)
    Dictionary = [[s.rstrip("\n") for s in nested] for nested in path]
    print(Dictionary)

    no_q = ""
    test_type = ""
    try:
        no_q = int(input("How many questions would you like the test to have?: "))
    except ValueError:
        print("Please enter an integer for the number of questions")
        exit()
    if no_q < 1:
        print("Pick a value of greater than 0")
        exit()
    try:
        test_type = int(input("Type 1 for english to german OR\nType 2 for german to english:"))
    except ValueError:
        print("Please only enter either 1 or 2")
        exit()
    if test_type != 1 and test_type != 2:
        print("Pick a valid test type (e.g. 1 or 2)")
        exit()
    i = 1
    score = 0
    if test_type == 1:
        while i <= no_q :
            h = random.randrange(0, len(translations))
            # random german word
            p = Dictionary[h][1]
            # random english word
            g = Dictionary[h][0]
            ans = input("What is the German for " + g + " ?:")
            if ans == p or ans == p.lower() or ans.lower() == p or ans.lower() == p.lower():
                print("That is the correct answer")
                score = score + 1
            else:
                print("That is incorrect, the correct answer was " + p)

            i = i + 1
    else:
        while i <= no_q:
            h = random.randrange(0, len(translations))
            # random german word
            p = Dictionary[h][1]
            # random english word
            g = Dictionary[h][0]
            ans = input("What is the English for " + p + " ?:")
            if ans == g or ans == g.lower() or ans.lower() == g or ans.lower() == g.lower():
                print("That is the correct answer")
                score = score + 1
            else:
                print("That is incorrect, the correct answer was " + g)

            i = i + 1
    print("Your score is : " + str(score) + "/" + str(no_q))
    repeat = input("Would you like to do another test?: ")
    if repeat == "Yes":
        test()
    else:
        exit()



test()

file.close()

