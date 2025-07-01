#Joe Melia EET-107

from adafruit_circuitplayground import cp
import time

def main():
    while True:
        if cp.touch_A1:
            On()
        else:
            Off()

def On():
    for light in range(10):
        cp.pixels[light] = (0, 100, 0)
        time.sleep(.01)

def Off():
    for light in range(10 -1, -1, -1):
        cp.pixels[light] = (0, 0, 0)
        time.sleep(.01)

main()
