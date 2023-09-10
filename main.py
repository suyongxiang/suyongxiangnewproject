from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
import time

keypico = PMK(Hardware())
keys = keypico.keys

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], 
                          out_channel=0)

# Colour selection
snow = (0, 0, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)

# Set key colours for all keys
keypico.set_all(*snow)
import random
a=random.randint(0,15)
b=random.randint(0,255)
c=random.randint(0,255)
abba=(a,b,c)
# Orientation
# keypico.set_led(0, *red)
# keypico.set_led(3, *green)
# keypico.set_led(12, *blue)
# keypico.set_led(15, *purple)

# Set sleep time
keypico.led_sleep_enabled = True
keypico.led_sleep_time = 10

# Midi

start_note = 68
velocity = 127

# Loop to create the patterns
counter = 0

while counter < 10:
    a=random.randint(0,15)

    keypico.set_led(a,*red)
    counter = counter+1

counter = 0

#for when you press the buttons
for key in keys:
    @keypico.on_press(key)
    def press_handler(key):
        print("Key {} released".format(key.number))
        if key.rgb == [0,0,255]:
            key.set_led(*red)
        elif key.rgb == [0,255,0]:
            key.set_led(*blue)  
        else:
            key.set_led(*snow)
    


        
            


level = 0
##to make a level harder
while True:
    keypico.update()  
    note = start_note + key.number
    midi.send(NoteOff(note, 0))
    level = level+1
    @keypico.on_hold(key)
    def hold_handler(key):
        print("Key {} held".format(key.number))
        key.set_led(*green)
        counter = 0

        while counter < 10:
            a=random.randint(0,15)
            if level ==1:
                b = random.randint(1,10)
            if level == 2:
                b = random.randint(2,11)
            if level > 2:
                b = random.randint(3,12)
            if b > 10:
                keypico.set_led(a,*green)
            elif b < 11 and b > 5:
                keypico.set_led(a,*blue)
            elif b <6:
                keypico.set_led(a,*red)
            counter = counter+1



