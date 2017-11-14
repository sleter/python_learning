#import kivy
#kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy import Config
Config.set('graphics', 'multisamples', '0')

class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

if __name__ == '__main__':
    calcApp = CalculatorApp()
    calcApp.run()
