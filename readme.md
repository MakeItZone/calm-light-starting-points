# Making a Calming Sounds Night Light

These are some starting points for Sofie's Inventors Club @ Highland Secondary.

Their goal for this project is to create a soft glowing night light that also plays calming sounds. It is being developed for a real person, so they will be adjusting things based on the recipients feedback.

I suggested they explore using a Raspberry Pi Pico with Circuit Python.

Motivations for this suggestion:

- easy to code using CircuitPython (using version 7)
- CircuitPython has drivers & libraries for NeoPixels, advanced animations, and playing MP3 files
- incredibly low cost
- small size

## Introductory Slides 

Some thoughts & references are in [slides/static/index.html](slides/static/index.html).

It includes links to a Wokwi Pi Pico simulator setup with CircuitPython and a NeoPixel strip.

They were created using [reveal-md](https://github.com/webpro/reveal-md).

## Example Starter Code

### NeoPixels

[examples/neopixel](examples/neopixel)

Uses the Adafruit LED Animation library.

### Audio MP3 Playback

[examples/AudioPlayback-PWM](examples/AudioPlayback-PWM)

Uses the Adafruit audio libraries. Example audio mp3 file from [this Adafruit example](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/MP3_Playback_RP2040/Pico_Single_File)

