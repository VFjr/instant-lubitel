# Control the neopixel on the rp2040 using serial, while connected to the computer

import machine
import neopixel
import time
import sys

# Setup NeoPixel
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return int(v * 255), int(v * 255), int(v * 255)
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - (s * f))
    t = v * (1.0 - (s * (1.0 - f)))
    i = i % 6
    if i == 0:
        return int(v * 255), int(t * 255), int(p * 255)
    elif i == 1:
        return int(q * 255), int(v * 255), int(p * 255)
    elif i == 2:
        return int(p * 255), int(v * 255), int(t * 255)
    elif i == 3:
        return int(p * 255), int(q * 255), int(v * 255)
    elif i == 4:
        return int(t * 255), int(p * 255), int(v * 255)
    else:
        return int(v * 255), int(p * 255), int(q * 255)

print("NeoPixel Control")
print("Commands:")
print("'r' - Red")
print("'g' - Green")
print("'b' - Blue")
print("'w' - White")
print("'o' - Off")
print("'f' - Start color fade")
print("'s' - Stop color fade")
print("'q' - Quit")

running_fade = False

def fade_colors(speed=0.008):
    for hue in range(0, 360, 1):
        if not running_fade:
            break
        rgb = hsv_to_rgb(hue / 360.0, 1.0, 1.0)
        pixel.fill(rgb)
        pixel.write()
        time.sleep(speed)

while True:
    print("Waiting for command")
    try:
        command = input()[0]  # Take first character of input
        
        if command == 'r':
            running_fade = False
            pixel.fill((255, 0, 0))
            print("Red")
        elif command == 'g':
            running_fade = False
            pixel.fill((0, 255, 0))
            print("Green")
        elif command == 'b':
            running_fade = False
            pixel.fill((0, 0, 255))
            print("Blue")
        elif command == 'w':
            running_fade = False
            pixel.fill((255, 255, 255))
            print("White")
        elif command == 'o':
            running_fade = False
            pixel.fill((0, 0, 0))
            print("Off")
        elif command == 'f':
            running_fade = True
            print("Starting fade")
        elif command == 's':
            running_fade = False
            print("Stopping fade")
        elif command == 'q':
            pixel.fill((0, 0, 0))
            pixel.write()
            print("Quitting...")
            break
        pixel.write()
    except:
        print("No command received")

    if running_fade:
        fade_colors()