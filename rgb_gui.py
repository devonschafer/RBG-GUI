#!/usr/bin/python3
#This app uses the GUIZERO module
from guizero import *
import random

#define RGB colors
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
off_white = 255, 255, 200
black = 0, 0, 0
slider_width = 206

#create random numbers for random color generation at startup
rr = random.randint(0, 255)
rg = random.randint(0, 255)
rb = random.randint(0, 255)

#function for the back ground color of the app
def bg_color():
    #this function basically controls the app's background, so you can see new color
    red = red_slide.value
    green = green_slide.value
    blue = blue_slide.value
    app.bg = (red, green, blue)
    #if statement to change text to white beyond a certain point so its readable
    if red and green and blue <= 50:
        red_slide.text_color = off_white
        green_slide.text_color = off_white
        blue_slide.text_color = off_white
        rgb_output.text_color = off_white
        hex_output.text_color = off_white
    #otherwise black text
    else:
        red_slide.text_color = black
        green_slide.text_color = black
        blue_slide.text_color = black
        rgb_output.text_color = black
        hex_output.text_color = black

#function for the text output, to copy and paste if needed
def rgbout():
    red = red_slide.value
    green = green_slide.value
    blue = blue_slide.value
    #RGB output
    rgb_output.value = ('(%s,%s,%s)' % (red, green, blue))
    #HEX output
    hex_output.value = ('#{:02x}{:02x}{:02x}'.format( red, green , blue ))

#parameters for creating the window
app = App(title='RGB GUI', width=400, height=400)
app.repeat(100, bg_color)

#all the red stuff
red_text = Text(app, text='RED', size=20)
red_text.text_color='red'
red_slide = Slider(app, command=None, start=0, end=255)
red_slide.value=(rr)
red_slide.width=slider_width
red_slide.bg=red

#all the green stuff
green_text = Text(app, text='GREEN', size=20)
green_text.text_color='green'
green_slide = Slider(app, command=None, start=0, end=255)
green_slide.value=(rg)
green_slide.width=slider_width
green_slide.bg=green

#all the blue stuff
blue_text = Text(app, text='BLUE', size=20)
blue_text.text_color='blue'
blue_slide = Slider(app, command=None, start=0, end=255)
blue_slide.value=(rb)
blue_slide.width=slider_width
blue_slide.bg=blue

#for the text output
rgb_output = TextBox(app)
rgb_output.width=12
rgb_output.bg=off_white
rgb_output.text_size = 20
rgb_output.repeat(100, rgbout)

#for hex output
hex_output = TextBox(app)
hex_output.width=12
hex_output.bg=off_white
hex_output.text_size = 20
hex_output.repeat(100, rgbout)

#allow the app to be displayed
app.display()
