from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        return DynamicLabels()

class DynamicLabels(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        names = ["Alice", "Bob", "Charlie", "Diana"]
        for name in names:
            self.ids.main.add_widget(Label(text=name))

class DynamicLabelsApp(App):
    def build(self):
        return DynamicLabels()

if __name__ == '__main__':
    DynamicLabelsApp().run()
