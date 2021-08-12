basic.show_icon(IconNames.LEFT_TRIANGLE)

def on_forever():
    basic.show_icon(IconNames.SQUARE)
    basic.show_leds("""
        . . # . #
                # # # # .
                . # # # #
                # # . . .
                . . . . .
    """)
    basic.show_string("IM ASYRAF")
    basic.show_number(22)
    basic.pause(100)
basic.forever(on_forever)
