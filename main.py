"""
Name: Cooper Plath
Date: 12/10/20
Brief Project Description:
GitHub URL: https://github.com/cooper-plath/CooperPlathA2
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder


class TravelTrackerApp(App):
    def build(self):
        """ Link app.kv file to main build"""
        self.title = "CooperPlathA2"
        self.root = Builder.load_file('app.kv')
        return self.root

if __name__ == '__main__':
    TravelTrackerApp().run()
