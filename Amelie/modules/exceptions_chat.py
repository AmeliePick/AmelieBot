# -*- coding: utf-8 -*-
from libs.configParser import DisplayText

'''
Request module for adding a program to the database

'''





def AddProgramm():
    while(True):
        rowInput_ = input("\nWrite break that would leave \nThe addition is as follows: program Name = Path\n\nEnter: ")
        if rowInput_ == "Break" or  rowInput_ == "break":
            print("Exiting...")
                
            return 0 

        else:
            # If program name is in file already, that will be replace this line with new input of user

            input_ = rowInput_.split(" = ")
            lines = list()
            editInFile = False

            with open('../DataBase/added_programms.json', 'r') as file_read:
                for fileLine in file_read:
                    rowLine = fileLine.replace('\n', '')
                    fileLine = fileLine.split(" = ")
                    
                    if fileLine[0] == input_[0]:
                        rowLine = fileLine[0] + " = " + input_[1]
                        lines.append(rowLine)

                        editInFile = True
                        break
                        
                    else:
                        lines.append(rowLine)
                        

            if editInFile == False:
                lines.append(rowInput_)

            with open('../DataBase/added_programms.json', 'w') as file_write:
                for line in lines:
                    file_write.write(line + '\n')

    return


def programmNotFound():
    print("<--- "+ DisplayText.print("n_found"))
    print(DisplayText.print("addPr"))
    input_ = input("--> ")

    if input_ == "Y" or  input_ == "y":
        AddProgramm()
    else:
        return 0