from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ConvertMilesKmApp(App):
    def build(self):
        return ConvertMilesKm()

class ConvertMilesKm(BoxLayout):
    output_text = StringProperty('')

    def convert(self):
        try:
            miles = float(self.ids.input_miles.text)
            self.output_text = str(miles * 1.60934)
        except ValueError:
            self.output_text = '0.0'

    def increment_miles(self, value):
        try:
            miles = float(self.ids.input_miles.text) + value
            self.ids.input_miles.text = str(miles)
        except ValueError:
            self.ids.input_miles.text = str(value)
        self.convert()

class ConvertMilesKmApp(App):
    def build(self):
        return ConvertMilesKm()

if __name__ == '__main__':
    ConvertMilesKmApp().run()
