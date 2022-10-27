from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from plyer import gps

class tekst(BoxLayout):
    pass

class testApp(App):
    kordinaadid=''
    
    def on_start(self):
        gps.configure(on_location=self.info)
        gps.start()

    def info(self, **kwargs):
        self.kordinaadid=str(kwargs['lat'])+str(kwargs['lon'])
             
    
    def build(self):
        return tekst()
    




testApp().run()