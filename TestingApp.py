from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from PlaceCollection import PlaceCollection
from Place import Place

class TestingApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')


    def build(self):
        self.title = "testing"
        self.root = Builder.load_file('TestingApp.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        index = 1
        for place in self.place_collection.file_places:
            location_button = Button(text=str(place))
            location_button.place = place
            location_button.bind(on_release=self.press_entry)
            self.root.ids.entry_box.add_widget(location_button)
            index = index + 1

    def press_entry(self, instance):
        self.root.ids.press_status.text = "You pressed " + instance.id

TestingApp().run()