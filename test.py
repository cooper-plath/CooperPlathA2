# from Place import Place
# List = []
# display_file = open("places.csv")
#
# count = 0
# # # for line in display_file:
# # #     count += 1
# # #
# # #     List.append(display_file.readline())
# # List.append(display_file.readline().strip())
# # print(Place(List))
#
# for line in display_file:
#     line = line.strip()
#     Line_Parts = line.split(',')
#     Line_Parts[2] = int(Line_Parts[2])
#     name = Line_Parts[0]
#

from Place import Place
from Place import file_entry

# print(len(file_entry))
# print(file_entry[2].name)
# file_entry.append(Place("Townsville", "Australia", 0, "v"))
# print(file_entry[3].is_visited())
#
# print(len(file_entry[1].name))
display_file = open("places.csv")
# print(display_file.read())
list = []
total = 0
for lines in display_file:
    parts = lines.strip()
    parts = lines.split(',')
    list.append(Place(parts[0],parts[1],parts[2],parts[3]))
    print(list[total])
    total += 1
# print("")
# if list[1].priority == 2:
#     print('True')
# else:
#     print('False')
# # print("Comprehension")
# # print([str(place) for place in list ])
new_row = 0
integer = int(input("Number: "))

for i in range(3):
    if list[new_row].priority == integer:
        print("Priority is in list")
    else:
        new_row += 1


