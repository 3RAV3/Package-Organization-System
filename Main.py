import time
from ast import literal_eval

# Initialize Variables -------------------------------------------------------------------------------------------------

section_number = 0
rows = []
columns = []

# Read files from Data.txt ------------------------------------------------------------------------------------

datafile = open("Data.txt", "r")
x = datafile.read().splitlines()
packages = literal_eval(x[0])
location_data = literal_eval(x[1])
grid_layout = literal_eval(x[2])
for k in range(len(grid_layout)):
    rows.append(grid_layout[k][0])
    columns.append(grid_layout[k][1])
datafile.close()


# Define Minor Subroutines ---------------------------------------------------------------------------------------------

def clean_data_and_save(packages, location_data, grid_layout):

    # When a remove function is called, a 0 is inserted wherever the name for that package was. This function finds
    # these 0's and removed their list from the broader list of all data, then saves and writes that data to the 
    # Data.txt file.

    if packages:
        lenname = len(packages)
        for k in range(lenname):
            if packages[(lenname - 1) - k] == 0:
                packages.pop((lenname - 1) - k)
                location_data.pop((lenname - 1) - k)
    print_data(packages, location_data, False)
    save_to_file(packages, location_data, grid_layout)
    return packages, location_data


def save_to_file(packages, location_data, grid_layout):

    # Writes the data which is given to it, including the names on the packages, the location data for the packages, 
    # and the grid layout to the Data.txt file. Part of the clean_data_and_save function.

    datafile = open("Data.txt", "w")
    datafile.write(str(packages))
    datafile.write("\n")
    datafile.write(str(location_data))
    datafile.write("\n")
    datafile.write(str(grid_layout))
    datafile.close()
    print("Data Saved\n")


def print_data(name_list, data_list, finding_boolean):
    
    # This function prints the package's owner and location in a clean formatted list so that the user can understand 
    # where the packages are and can find them easily. 
    # "finding_boolean" is used when locating an individual package. This will remove the "Existing Packages"
    # text and just print the value which is trying to be found.
    
    if not finding_boolean:
        print("\nExisting Packages:\n")
        time.sleep(1)
    if name_list.count(0) == len(name_list):
        print("\nNone\n")
    else:
        for number in range(len(name_list)):
            if 0 != name_list[number]:
                if type(data_list[number]) is not int:
                    print("\npackages: ", name_list[number][0], ", ", name_list[number][1], "\n", "Row Number:",
                          data_list[number][1], "   Column:", data_list[number][2], " to ", data_list[number][2] +
                          data_list[number][0] - 1, "\n")
                    time.sleep(0.5)


def check_for_cancel(_input_):
    
    # This function checks the given input for the inputted word "cancel" in order to determine if the current function
    # should be abandoned or continue. Outputs a boolean.
    
    temp = [_input_.lower() for _input_ in _input_]
    _input_ = "".join(temp).capitalize()
    if _input_ == 'Cancel':
        return False
    else:
        return True


def newline(number, row, column, location_data, section_number):

    # newline allows for the system to recognize that the current section of rows and columns has been filled up, and
    # should transition to using the next set of rows and columns.

    if section_number > 0:
        row += rows[section_number]
    if number != 0:
        if row - location_data[number - 1][1] == 1:
            column = 1
    return row, column


# Define Major Subroutines----------------------------------------------------------------------------------------------

def update_data(packages, location_data, rows, columns, section_number):

    # update_data asks for an input from the user in terms of the package owner's name and the width of the package.
    # From there, it assigns the package a location, logs the location of the package for later, and at the end of the
    # function, prints out all the packages which are being stored so that the information can be verified.

    lenname = len(packages)
    lendata = len(location_data)
    added = 0
    position = 0
    row = 0
    column = 0

    if lendata == 0:
        section_number = 0

    for k in range(lenname):
        if packages[(lenname - 1) - k] == 0:
            packages.pop((lenname - 1) - k)
            location_data.pop((lenname - 1) - k)
        else:
            break
    while True:
        _input_ = input("\nEnter 'last name' or type 'done' when finished ===> \n    ")
        temp = [_input_.lower() for _input_ in _input_]
        if " " in temp:
            break
        _input_ = "".join(temp).capitalize()
        if _input_ == 'Done':
            break
        else:
            _input2_ = input("\nEnter 'first name' or 'cancel' ===>\n     ")
            if check_for_cancel(_input2_):
                _input3_ = input("\nEnter package width or 'cancel' ===>\n     ")
                if check_for_cancel(_input3_) == (True and _input3_.isdigit()):
                    _input3_ = int(_input3_)
                    if [_input_, _input2_] not in packages:
                        packages.append([_input_, _input2_.capitalize()])
                        location_data.append([_input3_, 0])
                        added += 1
                        print("\nAdded\n\n")
                        time.sleep(0.5)
                else:
                    print("\nCancelled or Invalid Width\n")
                    time.sleep(0.5)

    def getnumber(list):
        return list[1]

    for y in range(len(rows)):
        if location_data[lendata - 1][1] > rows[y]:
            section_number = y + 1
            break

    total = columns[section_number] * rows[section_number]

    for k in range(len(location_data)):

        for y in range(len(rows)):
            if location_data[lendata - 1][1] > rows[y]:
                total = rows[y] * columns[y]
                section_number = y + 1
                break

        for h in range(len(location_data)):
            if location_data[h][1] == 0:
                position = ((location_data[h - 1][1] - rows[section_number] - 1) * columns[section_number]) + location_data[h - 1][0]
                break
            else:
                position = 0

        startlist = [0]
        endlist = [0]
        otherlist = []
        namelist = []

        if position > rows[section_number] * columns[section_number]:
            if len(rows) > section_number + 1:
                section_number += 1
                row = 1
                column = 1
                total = 0
                for h in range(section_number):
                    total += rows[h] * columns[h]
                    position -= total
            else:
                if len(rows) == section_number + 1:
                    print("Not enough space!")
                    row = 0
                    for we in range(len(rows)):
                        row += rows[we]

                    e = 0
                    while True:
                        if e + 1 == len(location_data):
                            break
                        if location_data[e][1] > row or location_data[e][1] == 0:
                            location_data.pop(e)
                            packages.pop(e)
                        if e < len(location_data):
                            e += 1
                    break

        for b in range(len(packages)):
            if location_data[b][1] != 0:
                if section_number > 0:
                    position = ((location_data[b][1] - rows[section_number] - 1) * columns[section_number]) + location_data[b][2] - total
                else:
                    position = ((location_data[b][1] - rows[section_number] - 1) * columns[section_number]) + location_data[b][2]
                startlistnum = position + total

                endlistnum = position + location_data[b][0] - 1 + total

                endlist.append(endlistnum)

                startlist.append(startlistnum)

                namelist.append(packages[b])
            else:
                otherlist.append([packages[b], location_data[b][0]])
        position = 0
        otherlist.sort(reverse=True, key=getnumber)
        for t in range(len(otherlist)):
            otherlist[t].pop(1)
            otherlist[t] = otherlist[t][0]
        namelist += otherlist
        for f in range(len(namelist)):
            for g in range(len(location_data)):
                if packages[g] == namelist[f]:
                    packages.insert(f, packages[g])
                    location_data.insert(f, location_data[g])
                    location_data.pop(g + 1)
                    packages.pop(g + 1)

        if location_data[k][1] == 0:
            if len(startlist) > 1:
                for a in range(len(startlist) - 1):
                    if (startlist[a + 1] - endlist[a]) - 1 >= location_data[k][0]:
                        position = endlist[a] + 1
                        row = (position + location_data[k][0] - 2) // columns[section_number] + 1
                        column = position - ((row - 1) * columns[section_number])
                        row, column = newline(a, row, column, location_data, section_number)
                        location_data.insert(a, [location_data[k][0], row, column])
                        location_data.pop(k + 1)
                        packages.insert(a, packages[k])
                        packages.pop(k + 1)
                        break

        if location_data[k][1] == 0:
            position = endlist[len(endlist) - 1] + 1
            row = (position + location_data[k][0] - 2) // columns[section_number] + 1
            column = position - ((row - 1) * columns[section_number])
            row, column = newline(k, row, column, location_data, section_number)
            location_data[k] = [location_data[k][0], row, column]
            if section_number > 0:
                position = ((location_data[k][1] - rows[section_number] - 1) * columns[section_number]) + location_data[k][2] + total
            else:
                position = ((location_data[k][1] - rows[section_number] - 1) * columns[section_number]) + location_data[k][2]
            position += location_data[k][0] - 1
            endlist.append(position)
    clean_data_and_save(packages, location_data, grid_layout)
    return packages, location_data, row, column, section_number


def remove(name_list, data_list, grid_layout):

    # remove is a function which asks the user to pick a certain package, whether by using its location or name, and
    # then removes that package from the data set. It can also be used to remove all current packages to clear the
    # system and create a blank slate. At the end of the function, the package information is printed for user ease.

    while True:
        if len(name_list) == 0:
            print("No Names Left!")
            break
        lastname = input("\nEnter 'ByPosition', 'ByName', 'all', or 'done' ==> \n     ")
        temp = [lastname.lower() for lastname in lastname]
        temp = "".join(temp)
        lastname = temp.capitalize()
        if lastname == "Done":
            break
        elif lastname == "All":
            name_list = []
            data_list = []
            return name_list, data_list, grid_layout
        else:
            if lastname == "Byposition":
                while True:
                    temprow = input("\nInput Row Number ===>\n     ")
                    if temprow.isdigit():
                        temprow = int(temprow)
                        tempcol = input("\nInput Column Number ===>\n     ")
                        if tempcol.isdigit():
                            tempcol = int(tempcol)
                            removed = False
                            for k in range(len(location_data)):
                                if location_data[k][1] == temprow and location_data[k][2] <= tempcol <= (location_data[k][2] + location_data[k][0] - 1):
                                    packages.pop(k)
                                    location_data.pop(k)
                                    print("\nRemoved\n")
                                    removed = True
                                    break
                            if not removed:
                                print("\nNot Found\n")
                                break
                        else:
                            print("\nInvalid Column Number\n")
                            break
                    else:
                        print("\nInvalid Row Number\n")
                        break
                    break

            elif lastname == "Byname":
                last = input("\nEnter last name ===>\n     ")
                firstname = input("\nEnter first name ===>\n     ")
                temp = [firstname.lower() for firstname in firstname]
                temp = "".join(temp)
                firstname = temp.capitalize()
                last = last.lower().capitalize()
                inpname = [last, firstname]
                if inpname in packages:
                    for num in range(len(packages)):
                        if inpname == packages[num]:
                            name_list.pop(num)
                            data_list.pop(num)
                            print("\nValid Name\n")
                            break
                else:
                    print("\nInvalid Name\n")
            else:
                print("\nInvalid Command\n")
    clean_data_and_save(name_list, data_list, grid_layout)
    return name_list, data_list, grid_layout


def find(name_list, data_list):

    # find asks the user for the person who is trying to find their package's name. After the name is correctly
    # inputted, the function sifts through the data to find the location of the package and then prints out the correct
    # location.

    while True:
        lastname = str(input("Enter last name or 'done'===> \n     ")).lower().capitalize()
        if lastname != "Done":
            firstname = str(input("Enter first name ===> \n     ")).lower().capitalize()
            for k in range(len(name_list)):
                if [lastname, firstname] == name_list[k]:
                    tempname = name_list
                    name_list = [name_list[k]]
                    tempdata = data_list
                    data_list = [data_list[k]]
                    print_data(name_list, data_list, True)
                    name_list = tempname
                    data_list = tempdata
                    return name_list, data_list
            print("Name not found")
        else:
            return name_list, data_list


# Initialize Program ---------------------------------------------------------------------------------------------------

print("\nWelcome to the Package Sorting System!\n")
time.sleep(2)
print_data(packages, location_data, False)

# Run Loop -------------------------------------------------------------------------------------------------------------

while True:
    _input_ = input("\n\nType 'find', 'update', 'remove', or 'stop'; type 'details' for more information ===>\n     ")
    temp = [_input_.lower() for _input_ in _input_]
    _input_ = "".join(temp)
    if _input_ == "find":
        find(packages, location_data)
    elif _input_ == "update":
        packages, location_data, rows, columns, section_number = update_data(packages, location_data, rows, columns, section_number)
    elif _input_ == "remove":
        packages, location_data, grid_layout = remove(packages, location_data, grid_layout)
    elif _input_ == "stop":
        packages, location_data = clean_data_and_save(packages, location_data, grid_layout)
        break
    elif _input_ == "details":
        print("\n-----------------------------------------------------------------------------------------------------"
              "\n\n The 'find' function prints the details about the package for the given name.\n"
              "     This function should be used to locate packages.\n\n")
        print("The 'update' function adds names to the existing roster.\n"
              "     This function should be used for incoming packages.\n\n")
        print("The 'remove' function removes names from the existing roster.\n"
              "     This function should be used for when packages are to be removed from the system.\n\n")
        print("The 'stop' function saves the required data before terminating the program.\n"
              "     This function should be used whenever all other functions are run.\n"
              "     This program will save all required data, so the user can close out as much as needed.\n\n"
              "-----------------------------------------------------------------------------------------------------")
    else:
        print("\nInvalid Command\n")

# Finish Program -------------------------------------------------------------------------------------------------------
