from kivy.app import App
from kvui.main_window import MainWindow

class MainApp(App):
    def build(self):
        return MainWindow()

if '__main__' == __name__:
    MainApp().run()
