from kivy.app import App
from kivy.uix.label import Label

class LuminaApp(App):
    def build(self):
        return Label(text="Lumina App Running Successfully!")

if __name__ == "__main__":
    LuminaApp().run()

