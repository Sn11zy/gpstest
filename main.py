from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from plyer import gps
from android.permissions import request_permissions, Permission

class tekst(BoxLayout):
    pass


class testApp(App): 
    kordinaadid=StringProperty('')
    
    def on_start(self):
        request_permissions([Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])
        gps.configure(on_location=self.info)
        gps.start()

    def info(self, **kwargs):
        self.kordinaadid=str(kwargs['lat'])+str(kwargs['lon'])
             
    
    def build(self):
        return tekst()
    




testApp().run()
