from kivy.app import App
from kivy.uix.widget import Widget
import GlassHouse

class GlassHouseApp(app):
    def build(self):
        return GlassHouse()

if __name__ == '__main__':
    GlassHouseApp().run()
