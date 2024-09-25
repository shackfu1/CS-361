def SuperMathyBot():
    command = input("SuperMathyBot> ")
    if command[0:4] == "quit":
        exit()
    elif not(command[4:5].isnumeric() and command[6:7].isnumeric()):
        #if the fifth or seventh characters are not numbers, print the usage message
        print("usage: add|sub|mul|div v0 v1\nquit")
    elif command[0:3] == "add":
        print(float(command[4:5]) + float(command[6:7]))
    elif command[0:3] == "sub":
        print(float(command[4:5]) - float(command[6:7]))
    elif command[0:3] == "mul":
        print(float(command[4:5]) * float(command[6:7]))
    elif command[0:3] == "div":
        if command[6:7] == "0":
            print("can't divide by zero")
        else:
            print(float(command[4:5]) / float(command[6:7]))
    else:
        #if the input is not a valid command, print the usage message
        print("usage: add|sub|mul|div v0 v1\nquit")
    #loops the function
    SuperMathyBot()


if __name__ == '__main__':
    SuperMathyBot()
