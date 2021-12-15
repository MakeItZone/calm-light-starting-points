"""
Quick test/example of playing audio + NeoPixel Animations
"""

import board
import time
import array
import math

# audio libraries
import audiomp3
import audiopwmio

# neopixel & animation libraries
import neopixel
from rainbowio import colorwheel
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence

# set up audio playback
audio = audiopwmio.PWMAudioOut(board.GP0)
decoder = audiomp3.MP3Decoder(open("slow.mp3", "rb"))

# set up the NeoPixels
pixel_pin = board.GP15
pixel_num = 5
pixel_brightness = 0.75
pixels = neopixel.NeoPixel(
    pixel_pin, pixel_num, brightness=pixel_brightness, auto_write=False
)

# set up an animation
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet_fast = RainbowComet(pixels, speed=0.1, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=3)

# create a sequence of animations for bright lighting
animations = AnimationSequence(
    rainbow_chase,
    rainbow_comet_fast,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

if __name__=="__main__":
    while True:
        print("Starting audio playback...")        
        audio.play(decoder)
        while audio.playing:
            result = animations.animate()
            time.sleep(0.1)
            #pixels.show()
        print("...finished audio")
