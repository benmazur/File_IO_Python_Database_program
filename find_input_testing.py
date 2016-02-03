FIRSTNAME = 0
LASTNAME = 1
SECTION = 2
GRADE = 3
MERGEDLIST = [['Bud', 'Abbott', '51', '92.3'],\
              ['Don', 'Adams', '51', '90.4'],\
              ['Mary', 'Boyd', '52', '91.4'],\
              ['Jill', 'Carney', '53', '76.3'],\
              ['Hillary', 'Clinton', '50', '82.1'],\
              ['Randy', 'Newman', '50', '41.2']]
    
def find():

    global MERGEDLIST
    findname = input('Please state the lastname of the record that you wish to find: ')
    for element in range(len(MERGEDLIST)):
        if MERGEDLIST[element][LASTNAME] == findname:
            print(MERGEDLIST[element])
            break
        if (element == (len(MERGEDLIST)-1)) and (MERGEDLIST[element][LASTNAME] != findname):
            print("Database does not contain a record for: ", findname)
            

find()
