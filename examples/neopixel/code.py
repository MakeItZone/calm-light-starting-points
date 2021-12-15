import time
import board
import analogio
import neopixel
from rainbowio import colorwheel
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence

# hardware connections and details
pixel_pin = board.GP22
pixel_num = 5
pixel_brightness = 0.75

# create the software interface to control the LEDs
pixels = neopixel.NeoPixel(
    pixel_pin, pixel_num, brightness=pixel_brightness, auto_write=False
)

# create objects that perform animations
rainbow = Rainbow(pixels, speed=0.1, period=3)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet_fast = RainbowComet(pixels, speed=0.1, bounce=True)
rainbow_comet_slow = RainbowComet(pixels, speed=0.25, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=3)

# create a sequence of animations
animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet_fast,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,

)

while True:
    result = animations.animate()
    time.sleep(0.1)
