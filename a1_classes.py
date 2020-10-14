"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from Place import Place
from Place import file_entry

"""
Name: Cooper Plath
Date started: 11-10-20
GitHub URL: https://github.com/cooper-plath/CooperPlathA2
"""



def main():
    # Display_File = open("places.csv")
    # Reads places.csv file and adds information to list
    # Add_File_Contents_To_List(Display_File, Places_List)
    print("Travel Tracker 2.0 - by Cooper Plath")
    Total_List_Items()
    print(f" {Total_List_Items()} places loaded from places.csv")
    Menu_Input = Display_Menu()
    """Run until the user presses Q"""
    while Menu_Input != "Q":
        # List places
        if Menu_Input == "L":
            Display_List_Options()
            Menu_Input = Display_Menu()
        # Add new place
        elif Menu_Input == "A":
            Add_New_Place()
            Menu_Input = Display_Menu()
        # Mark a place as visited
        elif Menu_Input == "M":
            Mark_Place_As_Visited()
            Menu_Input = Display_Menu()
    else:
        Add_List_To_File(Places_List)
        print(f"{Total_List_Items()} places saved to places.csv")
        print("Have a nice day :)")


# def Add_List_To_File(Places_List):
#     Save_To_File = open("Places.csv", "w")
#     New_Row = 0
#     for i in range(Total_List_Items(Places_List)):
#         Save_To_File.write("{}, {}, {}, {} \n".format(Places_List[New_Row][0], Places_List[New_Row][1], Places_List[New_Row][2], Places_List[New_Row][3]))
#         New_Row += 1
#     Save_To_File.close()

# def Add_File_Contents_To_List(Display_File, Places_List):
#     for line in Display_File:
#         line = line.strip()
#         Line_Parts = line.split(',')
#         Line_Parts[2] = int(Line_Parts[2])
#         Places_List.append(Line_Parts)
#     return Places_List

def Total_List_Items():
    # Counts how many entries are in list
    Total_List_Items = len(file_entry)
    return Total_List_Items

def Display_List_Options():
    # Finds longest 'name' and 'location' strings as to dynamically format list
    Name_Length = Find_Name_String_Length()
    Location_Length = Find_Location_String_Length()
    row_in_file = 0
    list_number = 1
    for i in range(Total_List_Items()):
        if file_entry[row_in_file].is_visited() == False:
            print(f" *{list_number}. {file_entry[row_in_file].name:{Name_Length}} in {file_entry[row_in_file].country:{Location_Length}} priority {file_entry[row_in_file].priority}")
        else:
            print(
                f"  {list_number}. {file_entry[row_in_file].name:{Name_Length}} in {file_entry[row_in_file].country:{Location_Length}} priority {file_entry[row_in_file].priority}")
        row_in_file += 1
        list_number += 1
    print(f"  {Total_List_Items()} Total places. You still want to visit {total_unvisited()} places")

def total_unvisited():
    total = 0
    new_row = 0
    for i in range(Total_List_Items()):
        if file_entry[new_row].is_visited() == False:
            total += 1
        new_row += 1
    return total


def Find_Name_String_Length():
    File_List_Entry = 0
    Max_Name_String = 0
    # Runs through each sublist in global list and to find longest string entry
    for i in range(Total_List_Items()):
        if len(file_entry[File_List_Entry].name) > Max_Name_String:
            Max_Name_String = len(file_entry[File_List_Entry].name)
            File_List_Entry += 1
    return Max_Name_String


def Find_Location_String_Length():
    File_List_Entry = 0
    Max_Location_String = 0
    for i in range(Total_List_Items()):
        if len(file_entry[File_List_Entry].country) > Max_Location_String:
            Max_Location_String = len(file_entry[File_List_Entry].country)
            File_List_Entry += 1
    return Max_Location_String





def Display_Menu():
    print(""" Menu:  
 L - List Places
 A - Add new place
 M - Mark a place as visited
 Q - Quit""")

    Menu_Input = str(input(" >>> ").upper())
    Program_Key_List = ['L', 'A', 'M', 'Q']
    # Error checking that user inputs correct key to navigate menu
    while not Menu_Input in Program_Key_List:
        print("Invalid menu choice")
        Menu_Input = str(input(" >>> ").upper())
    return Menu_Input


def Add_New_Place():
    Location = Location_Error_Checking()
    Country = Country_Error_Checking()
    Priority_Input = Integer_Error_Checking()
    print(f"{Location} in {Country} (priority {Priority_Input}) added to Travel Tracker")
    file_entry.insert(0, Place(Location, Country, Priority_Input, 'n'))

    # Inserts new sublist at beginning of global list once user enters correct information

def Location_Error_Checking():
    # Error checking that str input isn't an integer or blank. Than checks if location is already in list
    Valid_Entry = False
    while not Valid_Entry:
        Location_Input = str(input("Name?: "))
        if len(Location_Input) <= 0:
            print("Can't be blank")
        elif Location_Input.isalpha() == False:
            print("Can't be a number")
        else:
            Location_In_List = Check_Location_In_List(Location_Input)
            if Location_In_List == True:
                print("That place is already visited")
            else:
                Valid_Entry = True

    return Location_Input.capitalize()

def Check_Location_In_List(Location_Input):
    # Checks that location input isn't identical to element in list
    Location_In_List = False
    Next_Row = 0
    for i in range(Total_List_Items()):
        if Location_Input.capitalize() in file_entry[Next_Row].name:
            Location_In_List = True
        else:
            Next_Row += 1
    return Location_In_List

def Integer_Error_Checking():
    valid_integer = False
    while not valid_integer:
        try:
            Priority_Input = int(input("Priority: "))
            if Priority_Input <= 0:
                print("Number must be > 0")
            else:
                Input_In_List = check_priority_in_list(Priority_Input)
                if Input_In_List == True:
                    print("Invalid place number")
                else:
                    valid_integer = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return Priority_Input

def check_priority_in_list(Priority_Input):
    # Checks that priority input isn't identical to element in list
    Input_In_List = False
    Next_Row = 0
    for i in range(Total_List_Items()):
        if file_entry[Next_Row].priority == Priority_Input:
            Input_In_List = True
        else:
            Next_Row += 1
    return Input_In_List



def Country_Error_Checking():
    Valid_Entry = False
    while not Valid_Entry:
        Country_Input = str(input("Country?: "))
        if len(Country_Input) <= 0:
            print("Can't be blank")
        elif Country_Input.isalpha() == False:
            print("Can't be a number")
        else:
            Valid_Entry = True

    return Country_Input.capitalize()








def Mark_Place_As_Visited():
    Display_List_Options()
    # Checks if all locations have been visited already, prints message
    All_Visited = Check_If_Locations_Are_Visited()
    if All_Visited == True:
        print(" No unvisited places")
    else:
        print(" Mark the number of a place to mark as visited")
        Mark_Visited = Mark_Visited_Input_Error_Check()
        print(f" {file_entry[Mark_Visited].name} in {file_entry[Mark_Visited].country} visited!")
        # Once user marks location as visited, sublist element -1 is marked as visited
        file_entry[Mark_Visited].visited == 'v'

def Check_If_Locations_Are_Visited():
    # Runs through each sublist and checks if 'n', not visited is still in list
    new_row = 0
    all_visited = True
    for i in range(Total_List_Items()):
        if file_entry[new_row].is_visited():
            all_visited = False
        else:
            new_row += 1
    return all_visited



def Mark_Visited_Input_Error_Check():
    valid_integer = False
    while not valid_integer:
        try:
            Mark_Visited_Input = int(input(" >>> "))
            Mark_Visited_Input -= 1
            if Mark_Visited_Input < 0:
                print("Number must be > 0")
            elif Mark_Visited_Input > Total_List_Items():
                print("Invalid place number")
            else:
                if file_entry[Mark_Visited_Input].is_visited():
                    print("That place is already visited")
                else:
                    valid_integer = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return Mark_Visited_Input



main()
