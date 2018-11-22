# -*- coding: utf-8 -*-

'''
The module adds to the database data on the location of user applications for further work with them.

'''

print("\nHey, you can add the location of any program to my database. Alas, I'm not very trained and can't find it =(\n\nBut my Creator is working on it")

def AddProgramm():
    with open('../DataBase/added_programms.txt', 'a') as file_added_programms:
        

        while(True):
            Add = input("\nWrite break that would leave \nThe addition is as follows: program Name = Path\n\nEnter: ")
            if Add == "Break" or  Add == "break":
                print("Exiting...")
                
                return 0 

            else:
                #make exception TypeError
                Add_programm = file_added_programms.write('\n'+ Add)
            
            




