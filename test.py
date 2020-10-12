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
print(len(file_entry))
print(file_entry[2].name)
file_entry.append(Place("Townsville", "Australia", 0, "v"))
print(file_entry[3].is_visited())

print(len(file_entry))

