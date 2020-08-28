from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

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
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" 
        self.theme_cls.primary_palette = "DeepPurple"
        return Root()
    
MyApp().run()