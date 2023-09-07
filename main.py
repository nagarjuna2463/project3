import kivy
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class myapp(App):
    def build(self):
        return Button(text="Welcome")
    
if __name__=="__main__":
    myapp().run()