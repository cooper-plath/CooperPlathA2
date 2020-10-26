from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from PlaceCollection import PlaceCollection
from Place import Place
from kivy.properties import ListProperty

dictionary = {'Visited': "Visited", 'Priority': "Priority", 'Country': "Country", 'Name': "Name"}

class TestingApp(App):
    current_category = StringProperty()
    dictionary_codes = ListProperty()

    def __init__(self):
    #     super().__init__(**kwargs)
    #     self.place_collection = PlaceCollection()
    #     self.place_collection.load_places('places.csv')
        place_collection = PlaceCollection()



    # def build(self):
    #     self.title = "testing"
    #     self.root = Builder.load_file('TestingApp.kv')
    #     self.test
    #     self.dictionary_codes = dictionary.keys()
    #     self.current_category = self.dictionary_codes[0]
    #     return self.root
    #
    # # def change_status(self, dictionary_code):
    # #     self.root.ids.output_label.text = dictionary[dictionary_code]
    # #     print("change to", dictionary_code)
    #
    #
    # def test(self):
    #     self.root.ids.testing.text = self.place_collection.total_unvisited_places()
    #     print(self.place_collection.total_unvisited_places)
    # #
    # def press_add(self, instance):
    #     test = self.root.ids.testing.text







    # def change_status(self):
    #     self.root.ids.status.text = "Places to visit: " + str(self.place_collection.total_unvisited_places())
    #     print("hello")



    # def create_widgets(self):
    #     index = 1
    #     for place in self.place_collection.file_places:
    #         location_button = Button(text=str(place))
    #         location_button.place = place
    #         location_button.bind(on_release=self.press_entry)
    #         self.root.ids.entry_box.add_widget(location_button)
    #         index = index + 1
    #
    # def press_entry(self, instance):
    #     self.root.ids.press_status.text = "You pressed " + instance.id
    #
    # def status(self):
    #     self.root.ids.status_message.text = 'hello'

TestingApp().run()