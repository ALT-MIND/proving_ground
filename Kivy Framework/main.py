from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

math_space = ObjectProperty()
class Root(BoxLayout):
    Builder.load_file('My.kv')

    def calculate_result(self):
        calc_entry = self.math_space.text
        result = eval(str(calc_entry))
        if type(result) == type(.5):
            self.math_space.text = str(round(result, 3))
        elif type(result) == type(9):
            self.math_space.text = str(result)
class MyApp(App):
    def build(self):
        return Root()
    
MyApp().run()