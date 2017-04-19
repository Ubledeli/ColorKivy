from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.colorpicker import ColorWheel, ColorPicker
from kivy.uix.label import Label
from kivy.clock import Clock
from random import randint
from uclient import UdpClient
import math
delta_time = 1/30
T = 4

class Colors(BoxLayout, UdpClient):
    data = [1023 for i in range(7)]
	#clr_picker = ColorPicker()
    led_input=ObjectProperty()
    wheel_1_input=ObjectProperty()
    wheel_2_input=ObjectProperty()
    client = UdpClient(('192.168.0.16',25000))
    n = 0
    def shine(self,dt):
        global delta_time, T
        Colors.n +=1
        t = (Colors.n*2*math.pi*delta_time/T)
        data1 = [randint(0,1023) for i in range(7)]
        data2 = [1000 for i in range(7)]
        data3 = [round(500*math.sin(t) + 510)] + data2
        #print(data3)
        Colors.client.jsend(data2)
        if randint(0,round(1/delta_time)) <= 1:
            #print((dt-delta_time)*100/delta_time)
            #Colors.client.jsend(data2)
            pass

    def on_touch_up(self, touch):
        Colors.client.jsend(self.data)

    def light(self):
        self.data = [round(self.wheel_1_input.b*1023),
                round(self.wheel_1_input.r*1023),
                round(self.wheel_1_input.g*1023),
                round(self.wheel_2_input.b*1023),
                round(self.wheel_2_input.r*1023),
                round(self.wheel_2_input.g*1023),
                round(self.led_input.value)]
        self.data = [1023-i for i in self.data]


class AutonomousColorWheel(ColorWheel):
    def __init__(self, **kwarg):
        super(AutonomousColorWheel, self).__init__(**kwarg)
        self.init_wheel(dt = 0)

    def on__hsv(self, instance, value):
        super(AutonomousColorWheel, self).on__hsv(instance, value)
        print(self.rgba)     #Or any method you want to trigger


class ColorApp(App):
    def build(self):
        colors = Colors()
        global delta_time
        Clock.schedule_interval(colors.shine, delta_time)
        return colors

if __name__ in ('__main__','__android__'):
    ColorApp().run()
