# Stephen Buchanan, Benjamin Mazur, Section 20L, 10/12/13
# Program 2

# Program 6-13

#imporing libraries
from cisc106_32 import*
import random

#Cosntants
CHART = 'c'
DELETE = 'd'
FIND = 'f'
INSERT = 'i'
PRINT = 'p'
READMERGE = 'r'
QUERY = 'q'
EXIT = 'e'
FIRSTNAME = 0
LASTNAME = 1
SECTION = 2
GRADE = 3
MERGEDLIST = []

# Functions

# Operations

# Delete operation
def delete():

    global MERGEDLIST
    
    findname = str(input('Please state the last name of the record to delete: '))
    for element in MERGEDLIST:
        if element[LASTNAME] == findname:
            print("The following record has been deleted:")

            print("\t", MERGEDLIST.pop(MERGEDLIST.index(element)))
    Print(MERGEDLIST) # call pirnt function

    
# Find operation
def find():

    global MERGEDLIST
    findname = input('Please state the lastname of the record that you wish to find: ')
    print()
    for element in MERGEDLIST:
        if element[LASTNAME] == findname:
            print(element)


# Insert operation
def insert():
    global MERGEDLIST
    
    print("Please enter new user record")
    insert_first_name= str(input("Enter first name: "))
    insert_last_name= str(input("Enter last name: "))
    insert_section= int(input("Enter section [50-53] (int): "))
    insert_grade= float(input("Enter grade [0.0-100.0] (float): "))

    newrecord = [insert_first_name]+[insert_last_name]+[insert_section]+[insert_grade]
    
    
    index = 0
    for record in MERGEDLIST:
        if record[LASTNAME] < newrecord[LASTNAME]:
            index += 1

    MERGEDLIST.insert(index, newrecord)
    print(index)
    print(MERGEDLIST)

# Print operation
def Print():

    global MERGEDLIST
    for record in MERGEDLIST:
        print(record)




# Read and Merge operation
def readmerge():

    global MERGEDLIST
    #input_file1 = input("Enter 1st filename to read and merge: ")
    #input_file2 = input("Enter 2nd filename to read and merge: ")

    input_file1 = "sample-r1.txt" #DELETE BEFORE SENDING!!!!
    input_file2 = "sample-r2.txt" #DELETE BEFORE SENDING!!!!

    list_file1 = [line.strip().split() for line in open(input_file1).readlines()]
    list_file2 = [line.strip().split() for line in open(input_file2).readlines()]

    while (len(list_file1) > 0 or len(list_file2)> 0 ):
        
        if (len(list_file1) == 0):
            MERGEDLIST += list_file2
            break
    
        if (len(list_file2) == 0):
            MERGEDLIST += list_file1
            break
        
        if (list_file1[0][LASTNAME] < list_file2[0][LASTNAME]):
            MERGEDLIST.append(list_file1.pop(0))
        else:
            MERGEDLIST.append(list_file2.pop(0))



# Query operation
def query():

    global MERGEDLIST

    # ---Getting the user to pick a what to query---
    selection = input("Please select a query: Grade (type g) or Section (type s): ")

    # ---Testing the users input to make sure that its valid---
    while selection != 's' or selection != 'g':
        print('Error: No such selection for Query.')
        selection = input("Please select a query: Grade (type g) or Section (type s): ")

    
    # The Grade Query
    if selection == 'g':
        inputGrade = input("Please state the grade threshold that you wish to search (the highest grade): ")

        # --Testing so that its only numbers--

        while inputGrade in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':

            print('Error: Grade must be a integer')

            inputGrade = input("Please state the grade threshold that you wish to search (the highest grade): ")

        else:
            inputGrade = float(inputGrade)

        # ----------Printing the Records with grades equal to or less then input----------  
        for record in MERGEDLIST:
            if record[GRADE] <= inputGrade:
                print(record)

    # The Section Query
    if selection == 's':

        inputSection = input("Please state the section that you wish to search (50-52): ")

        # -------------------------Input testing ----------------------

        # --Testing so that its only numbers--

        while inputSection in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':

            print('Error: Section must be a integer')

            inputSection = input("Please state the section that you wish to search (50-52): ")

        else:
            inputSection = int(inputGrade)

        # --Testing for the right section--

        while (inputSection != 50) or (inputSection != 51) or (inputSection != 52):

            print('Error: Sections are only 50-52')

            inputSection = input("Please state the section that you wish to search (50-52): ")


        # ------------Printing the Records with maching Sections---------------
        
        for record in MERGEDLIST:

            if record[SECTION] == inputSection:
                print(record)
    return()

# Secondary functions

# Convert function : converts from strings to int/floats
def convert():

    for record in MERGEDLIST:
        record[SECTION] = int(record[SECTION])
        record[GRADE] = float(record[GRADE])



# Welcome statment
def welcome():
    """
    Prints a welcome message to be viewed only at the opening of the program.
    Paramiters:
        None
    Variables:
        None >> just prints the welcome message
    """
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Welcome to the CISC 106 database compiler! This porgram can merge any 2 databases, search the database\
and alows you to interact with the database about students.")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return(None)




# The Menu       
def display_menu():

    """ Displays the main mein whenever called.
	Parameters:
        	None
	Variables:
        	None >> just prints the Menu strings
    """
    print("--------------------------------Main Menu-----------------------------------")
    print("Type any of the following single letter operations to start!\
{c, d, f, i, p, r, q, e}\n")
    
    print("\tc  for Chart")
    print("\td  for delete")
    print("\tf  for find")
    print("\ti  for insert")
    print("\tp  for print")
    print("\tr  for read and merge")
    print("\tq  for query")
    print("\te  to exit the program\n")
    return(None)





#The main body 
def main():

    




    
main()
