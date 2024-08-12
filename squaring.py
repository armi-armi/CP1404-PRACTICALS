from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class SquareNumberApp(App):
    def build(self):
        return SquareNumber()

class SquareNumber(BoxLayout):
    output_text = StringProperty('')

    def calculate_square(self):
        try:
            value = int(self.ids.input_number.text)
            self.output_text = str(value ** 2)
        except ValueError:
            self.output_text = '0.0'

class SquareNumberApp(App):
    def build(self):
        return SquareNumber()

if __name__ == '__main__':
    SquareNumberApp().run()
