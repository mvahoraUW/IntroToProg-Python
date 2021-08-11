# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Moiz Vahora, 8/10/21,Modified code to look cleaner):
# RRoot,08.06.2021,Created started script
# <Moiz Vahora>,<08.10.2021>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
# strMenu didn't need to be used so I commented it out. Though I can define it as the menu option listed in the code
# strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# Process the data
objFile_IO = open(objFile, "r")  # open file for reading

# Format data from file into a list that is processed by user
for row in objFile_IO:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    lstTable.append(dicRow)
objFile_IO.close() # closing file

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for i_entry, objRow in enumerate(lstTable):  # using i_entry to display index of list for user reference (added 1 since index starts at 0)
            print("Entry ", i_entry + 1)
            print('Task: ' + objRow["Task"] + ' ' + 'Priority: ' + objRow["Priority"])

        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        # Ask for user input
        I_task = input("Enter a task: ")
        I_priority = input("Enter a priority: ")
        # appending list variable with user input using a dictionary
        dicRow = {"Task": I_task, "Priority": I_priority + '\n'}
        lstTable.append(dicRow)

    # Step 5 - Deleting item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        for i_entry, objRow in enumerate(lstTable):
            # displaying current data for user reference (copied from option 1)
            print("Entry ", i_entry + 1)
            print('Task: ' + objRow["Task"] + ' ' + 'Priority ' + objRow["Priority"])
        # Asking user which entry to delete (0 to cancel)
        delete = int(input("Which entry would you like to delete? 0 to cancel "))

        if delete == 0:
            # cancel deletion and return to menu
            print("No user input deleted")
        else:
            # Removing selected entry (subtract 1 since count starts at 0) and displaying entry number deleted
            lstTable.remove(lstTable[delete - 1])
            print("Entry " + str(delete) + " deleted!!!")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # Opening file and overwriting my previous input, in case we deleted entries
        objFile_IO = open(objFile, "w")
        for objRow in lstTable:
            # Writing entries in list to the file from each dictionary entry
            objFile_IO.write(objRow["Task"] + ',' + objRow["Priority"])
        objFile_IO.close()  # close file
        print("User edits saved to file!!!")

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        # nothing to add program loop is broken and the program exits
        break  # and Exit the program
