#!/usr/bin/python3
#This app uses the GUIZERO module
from guizero import *

#define RGB colors
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
off_white = 255, 255, 200

#function for the back ground color of the app
def bg_color():
    red = red_slide.value
    green = green_slide.value
    blue = blue_slide.value
    app.bg = (red, green, blue)

#function for the text output, to copy and paste if needed
def rgbout():
    red = red_slide.value
    green = green_slide.value
    blue = blue_slide.value
    rgb_output.value = ('(%s,%s,%s)' % (red, green, blue))

#parameters for creating the window
app = App(title='RGB GUI', width=400, height=400)
app.repeat(100, bg_color)

#all the red stuff
red_text = Text(app, text='RED', font='Linux Biolinum Keyboard O', size=20)
red_text.text_color='red'
red_slide = Slider(app, command=None, start=0, end=255)
red_slide.value=(116)
red_slide.width=200
red_slide.bg=red

#all the green stuff
green_text = Text(app, text='GREEN', font='Linux Biolinum Keyboard O', size=20)
green_text.text_color='green'
green_slide = Slider(app, command=None, start=0, end=255)
green_slide.value=(158)
green_slide.width=200
green_slide.bg=green

#all the blue stuff
blue_text = Text(app, text='BLUE', font='Linux Biolinum Keyboard O', size=20)
blue_text.text_color='blue'
blue_slide = Slider(app, command=None, start=0, end=255)
blue_slide.value=(225)
blue_slide.width=200
blue_slide.bg=blue

#for the text output
rgb_output = TextBox(app)
rgb_output.width=15
rgb_output.bg=off_white
rgb_output.repeat(100, rgbout)

#allow the app to be displayed
app.display()
