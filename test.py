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



# print(len(file_entry))
# print(file_entry[2].name)
# file_entry.append(Place("Townsville", "Australia", 0, "v"))
# print(file_entry[3].is_visited())
#
# print(len(file_entry[1].name))
# display_file = open("places.csv")
# # print(display_file.read())
# list = []
# total = 0
# for lines in display_file:
#     parts = lines.strip()
#     parts = lines.split(',')
#     list.append(Place(parts[0],parts[1],parts[2],parts[3]))
#     print(list[total])
#     total += 1
# # print("")
# # if list[1].priority == 2:
# #     print('True')
# # else:
# #     print('False')
# # # print("Comprehension")
# # # print([str(place) for place in list ])
# # new_row = 0
# # integer = int(input("Number: "))
# #
# # # for i in range(3):
# # #     if list[new_row].priority == integer:
# # #         print("Priority is in list")
# # #     else:
# # #         new_row += 1
# row = 0
# for i in range(3):
#     if file_entry[row].is_visited() == False:
#         print(f"{file_entry[row].name}: Not visited")
#     row += 1

# PlaceCollection.load_places('places.csv')
# print(PlaceCollection.load_places())


from PlaceCollection import PlaceCollection
from Place import Place

# place_collection = PlaceCollection()
# print(place_collection)
# place_collection.load_places('places.csv')
# print(place_collection)
# print(place_collection.total_unvisited_places())
# place_collection.add_place(Place('Townsville','Australia', 4, True))
# print(place_collection)
# print(place_collection.file_places[-1])
# print(place_collection)


file_list = []
file_list.append(Place('Townsville','Australia', 4, False))
print(file_list[0].is_visited())





# place_collection = PlaceCollection()
# print(place_collection)
# place_collection.load_places('places.csv')
# print(place_collection.file_places[0])
# print(len(place_collection.file_places))
# print("total unvisited test")
# print(place_collection.total_unvisited_places())

# new_row = 0
# file_entry = []
# display_file = open('places.csv')
# for line in display_file:
#     line = line.strip()
#     parts = line.split(',')
#     parts[2] = int(parts[2])
#     new_row += 1
#     file_entry.append(Place(parts[0], parts[1], parts[2], parts[3]))
# print(file_entry[0].name)



# placecollection = PlaceCollection()
# print(placecollection.file_places)
# print(placecollection.load_places('places.csv'))
# entry = 0
# print(placecollection.file_places[0])



# total_places = []
# placecollection.load_places('places.csv')
# print(f"Total Places {total_places}")
# print(placecollection)
# print(total_places.append(placecollection))
# print(total_places.)



