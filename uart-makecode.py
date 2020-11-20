msg = ""
serial.write_line("Demo")

def on_forever():
    global msg
    msg = serial.read_until(serial.delimiters(Delimiters.FULLSTOP))
    serial.write_line(msg)
    basic.show_string("Hello!")
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """)
basic.forever(on_forever)