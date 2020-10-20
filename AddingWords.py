


import  pandas as pd
English = ""
German = ""

duplicate = False

with open("GermanDictionary.txt", "r+") as f1:
    i = 0
    while English != "Exit" and German != "Exit":
        if i >= 2:
            print("You have added " + str(i) + " words so far.")
        elif i == 1:
            print("You have added " + str(i) + " word so far.")

        English = input("Write the English word here: ")
        German = input("Write the German word here: ")
        for lines in f1:
            if lines.strip("\n") == "-" + English + ";" + German:
                duplicate = True
                print("This entry has already been added to the dictionary")
                i = i - 1
        if duplicate == False:
            f1.write("-" + English + ";" + German + "\n")
        elif duplicate == True:
            duplicate = False
        i = i + 1
    else:
        print("You have finished adding words")


with open("GermanDictionary.txt", "r+") as h:
    pd.Index(h).duplicated(keep="first")

with open("GermanDictionary.txt", "r") as f:
    lines = f.readlines()
with open("GermanDictionary.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "-Exit;" and line.strip("\n") != "-Exit;Exit":
            f.write(line)

# a(umlaut) = ae
# o(umlaut) = oe
# u(umlaut) = ue