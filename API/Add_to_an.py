file  = open ("answers.txt", "a")
while (True):
    Input = input("\n ---> Enter: ").replace("  ", " @ ")
    if Input == "Save":
        break

    file.write(Input+ '\n')


print ("\nStopped")
