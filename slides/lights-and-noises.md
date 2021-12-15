# Brainstorm

---

# Planning

- how much planning is good?
    - *what's the cost of a mistake?*
- Software vs Hardware?
    - usually low cost of mistake vs higher (exception: safety!)
- find a good balance between planning and trying!

---

# Work Together!

<iframe width="560" height="315" src="https://www.youtube.com/embed/1COvnSjLLw4?start=44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

===

- unlike rally driving, best to take turns at doing the coding!
- COMMUNICATE ideas, problems
- "IMPOSTER SYNDROME is REAL"... and it's ok, and everyone has it

---

# What is a Program?

I am a robot... teach me to "square"

---

# Key Concepts

- specific actions
- logic (decision making)
- loops
- blocks of code (eg what to repeat in a loop)
- functions/subroutines
- Less code is MORE (usually)
    - less places to make mistakes, so long as you can understand it!

---

# Python

---

<img src="https://imgs.xkcd.com/comics/python.png">

---

# Python Example

```
import time

for i in range(2, 15):
    if num % 2 == 0:
        print("Found an even number", num)
    else:
        print("Found an odd number", num)
print("All done!")
```

Note: Python uses spaces for marking blocks


---

# Pi Pico

- ~$8 computer
- dual core
- appears as a USB flash drive
- online simulator
- can be programmed in CircuitPython
    - beginner friendly version with many libraries

---

# Editors

- Web based editor (must use chrome): https://urfdvw.github.io/CircuitPython-online-IDE/
- Mu (if you can install it)


*Use these if you're working on sound*


- Ocenaudio or Audacity to create sound files

---

# Wokwi Simulator

- example set up to do NeoPixel LEDS: https://wokwi.com/arduino/projects/317983734672392770


---

# Circuit Python References

- https://learn.adafruit.com/welcome-to-circuitpython
- https://learn.adafruit.com/circuitpython-essentials


---

# Circuit Python References: LEDs

- https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/neopixel-leds
- https://learn.adafruit.com/circuitpython-led-animations

---

# Circuit Python References: Sound

- https://learn.adafruit.com/mp3-playback-rp2040/pico-mp3
    - Note [this known issue with start/end clicks](https://github.com/adafruit/circuitpython/issues/5136)
- Use Audacity or Ocenaudio to prepare sound files

---

# Extra References

- https://circuitpython.readthedocs.io/en/latest/docs/index.html
- https://www.recantha.co.uk/blog/?p=20950
- https://circuitpython.org/board/raspberry_pi_pico/
- https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/usage