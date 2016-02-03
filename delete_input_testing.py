FIRSTNAME = 0
LASTNAME = 1
SECTION = 2
GRADE = 3
MERGEDLIST = [['Bud', 'Abbott', '51', '92.3'], ['Don', 'Adams', '51', '90.4'],\
              ['Mary', 'Boyd', '52', '91.4'], ['Jill', 'Carney', '53', '76.3'],\
              ['Hillary', 'Clinton', '50', '82.1'], ['Randy', 'Newman', '50', '41.2']]

def delete():

    global MERGEDLIST
    
    findname = str(input('Please state the last name of the record to delete: '))
    for element in MERGEDLIST:
        if element[LASTNAME] == findname:
            print("The following record has been deleted:")

            print("\t", MERGEDLIST.pop(MERGEDLIST.index(element)))
            break
        else:
            print("Database does not contain a record for: ", findname)
            break

delete()

