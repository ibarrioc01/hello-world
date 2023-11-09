def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_number(0)
radio.on_received_number(on_received_number)

# Crea el canal 12 cuando se pulsa el botón A

def on_button_pressed_a():
    radio.set_group(12)
    radio.send_string("IRENE")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.set_group(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "SERGIO":
        basic.show_string("OK")
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.set_group(6)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    music.play(music.tone_playable(175, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    pass
basic.forever(on_forever)
