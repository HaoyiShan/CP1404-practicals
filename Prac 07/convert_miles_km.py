from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometres(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        try:
            result = float(self.root.ids.input_num.text) + change
            self.root.ids.input_num.text = str(result)
            self.convert(result)
        except ValueError:
            self.root.ids.input_num.text = str(0)

    def convert(self, value):
        try:
            result = float(value) * 1.609344
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.input_num.text = str(0)


ConvertMilesToKilometres().run()
