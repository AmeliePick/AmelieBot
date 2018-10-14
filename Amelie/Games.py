import random,re
#main-massif
with open("Games/Towns/Cities.txt") as f:
    City = f.read().split()

Readlist = []


def Cities():
    if lastChar != "Ь":
        matching_cities=[]
        for towns in City:
            if towns.startswith(lastChar):
                matching_cities.append(towns)
        Rcity = random.choice(matching_cities)
        lastSymbol = Rcity[-1:].title()
        lastSymbol2 = Rcity[-2:].title()
        available_cities =[]

        if lastSymbol == "Ь":
            for last in City:
                if last.startswith(lastSymbol2):
                    available_cities.append(last)
            A1 = available_cities          
            Readlist.extend(A1)
                        
        elif lastSymbol != "Ь":
            for last in City:
                if last.startswith(lastSymbol):
                    available_cities.append(last)
            AA = available_cities
            Readlist.extend(AA)
            print ("\n<-- ",Rcity)

            #remove program output from main-massif
            City.remove(Rcity)
            City.remove(user_input)

    elif lastChar == "Ь":
        soft_matching_cities =[]
        for soft in City:
            if soft.startswith(lastChar2):
                soft_matching_cities.append(soft)

        SoftRcity = random.choice(soft_matching_cities)
        Soft_lastSymbol = SoftRcity[-1:].title()
        Soft_lastSymbol2 = SoftRcity[-2:].title()
        Soft_available_cities =[]

        if Soft_lastSymbol == "Ь":
            for Soft_last in City:
                if Soft_last.startswith(Soft_lastSymbol2):
                    Soft_available_cities.append(Soft_last)
            B1 = Soft_available_cities
            Readlist.append(B1)
                    
        elif Soft_lastSymbol != "Ь":
            for Soft_last in City:
                if Soft_last.startswith(Soft_lastSymbol):
                    Soft_available_cities.append(Soft_last)

            BB = Soft_available_cities
            Readlist.append(BB)
            print ("\n<-- ",SoftRcity)

            #remove program output from main-massif
            City.remove(SoftRcity)
            City.remove(user_input)

            #end of main

def main():
    while (True):
        
        #Input
        global user_input
        user_input = input("\n--> Enter a city: ").title()
        global lastChar
        lastChar = user_input[-1:].title()
        global lastChar2
        lastChar2 = user_input[-2:].title()

        #checking values
        
        if user_input == "Stop":
                break
       
        if user_input in City:
            if not Readlist:
                #MAIN
                Cities()
            
                #end of core
        
         
        

        
            
            elif Readlist and user_input not in Readlist:
                    print ("Enter the city on the last letter")
                    continue
            elif Readlist and user_input in Readlist:
                Cities()
        elif user_input not in City:
            print("This city was")
            continue

main()