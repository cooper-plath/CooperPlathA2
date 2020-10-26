"""
Name: Cooper Plath
Date: 12/10/20
Brief Project Description: Kivy program that reads a csv file into a list and allows user to add new locations
GitHub URL: https://github.com/cooper-plath/CooperPlathA2
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from PlaceCollection import PlaceCollection
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from Place import Place

SORTING_CATAGORIES = {'Visited': 'is_visited', 'Priority': 'priority', 'Country': 'country', 'Name': 'name'}


class TravelTrackerApp(App):
    """TravelTrackerApp is a kivy based program to read and display location entries from a file as well as add new locations"""
    category_codes = ListProperty()
    current_category = StringProperty()
    """Initialise application and load location entries from places.csv into main list (place_collection)"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')
        self.place_collection.save_places('places.csv')

    def build(self):
        """ Link app.kv file to main build"""
        self.title = "CooperPlathA2"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.total_unvisited_status()
        self.location_pressed_status()
        self.category_codes = SORTING_CATAGORIES.keys()
        self.current_category = self.category_codes[0]
        return self.root

    """Reads main list of locations and creates buttons in the kv app for each entry"""

    def create_widgets(self):
        index = 1
        for place in self.place_collection.file_places:
            # Creates button with place class str for each and assigns an index number
            location_button = Button(text=str(place), id=str(index))
            location_button.place = place
            location_button.bind(on_release=self.press_entry)
            self.root.ids.locations_box.add_widget(location_button)
            index += 1

    """Assigns method for whenever a button or item is clicked in app.kv"""

    def press_entry(self, instance):
        # location button clicked changes its is.visited status to True
        instance.place.is_visited = True
        # Status label displays location clicked
        self.root.ids.location_clicked_status.text = "You visited " + instance.place.country
        self.root.ids.locations_box.clear_widgets()
        self.create_widgets()
        self.total_unvisited_status()

    """Create new location function that adds new entry to list through inputs on the kv app with error checking"""

    def press_add(self, name_input, country_input, priority_input):
        # if any text_input boxes on app.kv are empty, display message
        if self.root.ids.name_input.text == '' or self.root.ids.country_input.text == '' or self.root.ids.priority_input.text == '':
            self.root.ids.location_clicked_status.text = "All fields must be completed"
        # if priority input is less than 0, display message
        elif int(self.root.ids.priority_input.text) < 0:
            self.root.ids.location_clicked_status.text = "Priority must be > 0"
        else:
            # append new entry to main list and create widget
            place = Place(name_input, country_input, priority_input, False)
            location_button = Button(text=str(place))
            location_button.place = place
            location_button.bind(on_release=self.press_entry)

            self.root.ids.locations_box.add_widget(location_button)
            self.place_collection.add_place(place)

    """Clear kv TextInputs of str"""

    def press_clear(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""

    """Using spinner dynamic, sorts location widgets by chosen category"""

    def change_category(self, category_code):
        self.place_collection.sort(SORTING_CATAGORIES[category_code])
        print(SORTING_CATAGORIES[category_code])

    """Using dynamic status, displays total unvisited locations"""

    def total_unvisited_status(self):
        self.root.ids.total_unvisited_status.text = "Places to visit: " + str(
            self.place_collection.total_unvisited_places())

    """Displays static message"""

    def location_pressed_status(self):
        self.root.ids.location_clicked_status.text = "Welcome to Travel Tracker 2.0"

    def on_stop(self):
        self.place_collection.save_places('places.csv')

TravelTrackerApp().run()
