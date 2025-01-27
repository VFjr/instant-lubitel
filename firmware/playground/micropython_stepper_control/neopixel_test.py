# initial test of a built in neopixel on rp2040 zero, just to make sure everything is working as expected

import machine
import neopixel
import time
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

def fade_colors(speed=0.008):
    for hue in range(0, 360, 1):
        rgb = hsv_to_rgb(hue / 360.0, 1.0, 1.0)
        pixel.fill(rgb)
        pixel.write()
        time.sleep(speed)

while True:
    fade_colors()