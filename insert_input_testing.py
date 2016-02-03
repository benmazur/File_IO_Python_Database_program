FIRSTNAME = 0
LASTNAME = 1
SECTION = 2
GRADE = 3
MERGEDLIST = [['Bud', 'Abbott', '51', '92.3'], ['Don', 'Adams', '51', '90.4'],\
              ['Mary', 'Boyd', '52', '91.4'], ['Jill', 'Carney', '53', '76.3'],\
              ['Hillary', 'Clinton', '50', '82.1'], ['Randy', 'Newman', '50', '41.2']]

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

insert()
