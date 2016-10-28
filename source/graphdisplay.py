#!/usr/bin/python

#### Copyright (c) 2015, swpm, Jeffrey E. Erickson
#### All rights reserved.
#### See the accompanying LICENSE file for terms of use


from SwpmGraph import GraphWorldLoader

import kivy

kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.input.shape import ShapeRect
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.input.motionevent import MotionEvent


def GetGraph():
    loader = GraphWorldLoader()
    world = loader.load_map()
    map_data = world.cities

    x = []
    y = []
    lines = []
    for city in map_data:
        x.append(city.location[0])
        y.append(city.location[1])
        for link in city.links:
            if link.lCity == city.idx:
                for otherCity in map_data:
                    if otherCity.idx == link.rCity:
                        line_x = []
                        line_y = []
                        line_x.append(city.location[0])
                        line_x.append(otherCity.location[0])
                        line_y.append(city.location[1])
                        line_y.append(otherCity.location[1])
                        line = [line_x, line_y]
                        lines.append(line)
            else:
                for otherCity in map_data:
                    if otherCity.idx == link.lCity:
                        line_x = []
                        line_y = []
                        line_x.append(city.location[0])
                        line_x.append(otherCity.location[0])
                        line_y.append(city.location[1])
                        line_y.append(otherCity.location[1])
                        line = [line_x, line_y]
                        lines.append(line)
    return map_data, lines

class MyWidget(ScatterLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.update_canvas()
        self.do_rotation = False

    def update_canvas(self, **kwargs):
        self.canvas.clear()
        with self.canvas:
            Color(1,1,0)
            mapData = GetGraph()[0]
            print(mapData)
            for city in mapData:
                Line(circle=(city.location[0], city.location[1] - 3382, 1), width=1)
        self.scale = 1.0

    def on_touch_down(self, touch):


        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(ScatterLayout, self).on_touch_down(touch)
        touch.pop()
        return ret

class MyApp(App):
    def build(self):
        base_view = RelativeLayout()
        graph_widget = MyWidget()
        base_view.add_widget(graph_widget)
        return base_view


if __name__ == "__main__":
    MyApp().run()
