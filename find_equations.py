# this programm helps you find the right equation for the variables given
# -*- coding: utf-8 -*-

import csv
#make new dictionary for the data 
variables = {}
equations = {}
#add the data to the dictionary

#load data to the dictionary
with open('variables.csv', 'r', newline='', encoding='cp1252') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #print("row: ", row)
        # add the variable to the dictionary
        # check if its not empty and it has two elements
        if row != "" and len(row) == 2:
            variables[row[0]] = row[1]
    #print ("variables: ", variables)

#load data to the dictionary
with open('equations.csv', 'r', newline='', encoding='cp1252') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #print("row: ", row)
        # add the equation to the dictionary
        # join the variables in the list to a string except the last one
        eqStr = ",".join(row[:-1])
        # add it to the dictionary
        equations[eqStr] = row[-1]

    #print ("equations: ", equations)


def add_new_variable(exImput):
    if exImput == "":
        print("enter variable Letter/name than comma and longer name/description. exaple: P, Power \n")
        var = input()
    else:
        var = exImput
    if var == "":
        print("you have to enter at least one variable if you want to quit press enter again")
        var = input()
        if var == "":
            return
    var = var.split(",") # split the input into a list of variables
    var = [x.strip() for x in var] # remove whitespace
    var = [x for x in var if x != ""] # remove empty strings
    # check if there are only two variables
    if len(var) != 2:
        print("you have to enter exactly two variables")
    else:
        # check if the first variable is already in the dictionary
        if var[0] in variables:
            print("Variable {} already in the dictionary!".format(var[0]))
        else:
            # add the variable to the dictionary
            variables[var[0]] = var[1]
            #print("Variable {} added to the dictionary".format(var[0]))
            # add it to the csv file
            with open('variables.csv', 'a', newline='', encoding='cp1252') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(var)
                print("Variable {} added.".format(var[0]))
    #print (variables)


def add_new_equation(exImput):
    if exImput == "":      
        print("enter equation variables and equation explanation separated by semicoln. exaple: U, R, I, U = R*I Ohms law")
        equation = input()
    else:
        equation = exImput
    if equation == "":
        print("you have to enter at least one equation if you want to quit press enter again")
        equation = input()
        if equation == "":
            return
    equation = equation.split(",") # split the input into a list of equations
    equation = [x.strip() for x in equation] # remove whitespace
    equation = [x for x in equation if x != ""] # remove empty strings
    # sort the equation variables
    
    # sort the equation variables by alphabetical order
    eqSort = equation[:-1]
    eqSort.sort()
    # check if all the variables are in the dictionary
    for var in eqSort:
        if var not in variables:
            print("Variable {} not in the dictionary! (You need to add it first to use it)".format(var))
            return  
    # check if the equation is already in the dictionary
    # equation[0] is a list of variables, convert it to a string
    eqStr = ",".join(eqSort)
    if eqStr in equations:
        print("Equation {} already in the dictionary!".format(eqStr))
    else:
        # add the equation to the dictionary
        equations[eqStr] = equation[-1]
        #print("Equation {} added to the dictionary".format(eqStr))
        # add it to the csv file
        with open('equations.csv', 'a', newline='', encoding='cp1252') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([eqStr, equation[-1]])
            print("Equation {} added.".format(eqStr))
    #print (equations)

def findpath(exImput):
    if exImput == "":
        print("enter the variable you want to find the equation for")
        findvars = input()
    else:
        findvars = exImput
    if findvars == "":
        print("You have to enter at least one variable!")
        return
    findvars = findvars.split(",") # split the input into a list of variables
    findvars = [x.strip() for x in findvars] # remove whitespace
    findvars = [x for x in findvars if x != ""] # remove empty strings
    #print ("var: ", findvars)
    candidates = {}
    # check if all the variables are in the dictionary
    for var in findvars:
        if var not in variables:
            print("Variable {} not in the dictionary! (You need to add it first to use it)".format(var))
            return
        # find all the equations that have the variable in it
        for eq in equations:
            eqs = eq.split(",") # split the input into a list of variables
            eqs = [x.strip() for x in eqs] # remove whitespace
            eqs = [x for x in eqs if x != ""] # remove empty strings
            if var in eqs:
                # add the equation to the candidates dictionary and +1 to the count of the equation
                if eq in candidates:
                    candidates[eq] += 1
                else:
                    candidates[eq] = 1
    # print the candidates in a sorted way by the count of the equation 
    for key, value in sorted(candidates.items(), key=lambda item: item[1]):
        # value but only 2 decimal places
        print (value, ":" , equations[key], "\n")
    
    print ("found {} equations with these {} ({}) variables".format(len(candidates), len(findvars), ", ".join(findvars)))



choice = ""
while True:
    if choice == "":
        print("what do you want to do? \n (1) add new variable \n (2) add new equation \n (3) exit \n (4) show variables \n (5) show equations \n (6) find path \n (7) look up a variable \n (8) search by description")
        choice = input()
    if choice == "1":
        add_new_variable("")
    elif choice == "2":
        add_new_equation("")
    elif choice == "3":
        break
    elif choice == "4":
        for key in variables:
            print(key, " : ", variables[key], "\n")

        print ("found {} variables".format(len(variables)))
    elif choice == "5":
        # print equations each in new line
        for key, value in equations.items():
            print(key, " : ", value, "\n")

        print("found {} equations".format(len(equations)))
    
    elif choice == "6":
        findpath("")
    elif choice == "7":
        varin = input("enter the variable you are looking for: ")
        # check if the variable is in the dictionary
        if varin in variables:
            print (varin , " : ", variables[varin])
        else:
            print ("Variable not in the dictionary!")

    elif choice == "8":
        search = input("enter the description you are looking for: ")
        for key, value in variables.items():
            if search in value:
                print (key , " : ", value)
        
        for key, value in equations.items():
            if search in value:
                print (key , " : ", value)
    elif "," in choice:
        print("Trying to guess what you mean...")
        if choice.count(",") == 1:
            add_new_variable(choice)
        elif choice.split(",")[-1].strip() in variables:
            findpath(choice)
        else:
            add_new_equation(choice)
    elif variables.get(choice) != None:
        print(choice, " : ", variables[choice])
        
    choice = input ("Press enter to continue \n")
