from app import App
from app_components import clear_background
import simple_tildagon as st
from events.input import Buttons, BUTTON_TYPES
import time
from random import randint
from math import sqrt

TRIANGLE_X = 60 * sqrt(3)

RESPONSES = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
]


class Magic8Ball(App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.last_shaken = 0
        self.current_response = ""

    def recently_shaken(self):
        return time.time() - self.last_shaken < 10

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.last_shaken = 0
            self.current_response = ""
            self.minimise()

        if st.imu.is_shaken() and not self.recently_shaken():
            self.current_response = RESPONSES[randint(0, len(RESPONSES) - 1)]
            self.last_shaken = time.time()
            time.sleep(0.5)

    def _draw_triangle(self, ctx):
        ctx.rgb(0, 0, 1)
        ctx.begin_path()
        ctx.move_to(-TRIANGLE_X, -60)
        ctx.line_to(TRIANGLE_X, -60)
        ctx.line_to(0, 120)
        ctx.close_path()
        ctx.fill()

    def draw(self, ctx):
        clear_background(ctx)
        ctx.text_align = ctx.CENTER
        ctx.text_baseline = ctx.MIDDLE

        if self.recently_shaken() and self.current_response:
            ctx.font_size = 20
            ctx.gray(0.0).rectangle(-120, -120, 240, 240).fill()
            self._draw_triangle(ctx)
            ctx.move_to(0, 0).gray(1).text(self.current_response)
        else:
            ctx.font_size = 140
            ctx.gray(1.0).rectangle(-120, -120, 240, 240).fill()
            ctx.gray(0.0).move_to(0, 5).text("8")


__app_export__ = Magic8Ball
