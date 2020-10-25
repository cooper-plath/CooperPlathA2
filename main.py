"""
Name: Cooper Plath
Date: 12/10/20
Brief Project Description:
GitHub URL: https://github.com/cooper-plath/CooperPlathA2
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from PlaceCollection import PlaceCollection
from kivy.properties import StringProperty
from Place import Place



class TravelTrackerApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')



    def build(self):
        """ Link app.kv file to main build"""
        self.title = "CooperPlathA2"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.total_unvisited_status()
        self.location_pressed_status()

        return self.root

    def create_widgets(self):
        index = 1
        for place in self.place_collection.file_places:
            location_button = Button(text=str(place))
            location_button.place = place
            location_button.bind(on_release=self.press_entry)
            self.root.ids.locations_box.add_widget(location_button)
            index = index + 1

    def press_entry(self, instance):
        self.root.ids.press_status.text = "You pressed " + instance.id

    def total_unvisited_status(self):
        self.root.ids.total_unvisited_status.text = "Places to visit: " + str(self.place_collection.total_unvisited_places())

    def location_pressed_status(self):
        self.root.ids.location_clicked_status.text = "work in progress"

TravelTrackerApp().run()
