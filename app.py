from app import App
from app_components import clear_background
import simple_tildagon as st
from events.input import Buttons, BUTTON_TYPES
import time


class Magic8Ball(App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        clear_background(ctx)
        ctx.text_align = ctx.CENTER
        ctx.text_baseline = ctx.MIDDLE
        if st.imu.is_shaken():
            ctx.move_to(0, 0).gray(1).text("Shaken...")
        else:
            ctx.move_to(0, 0).gray(1).text("Hello, world!")
        time.sleep(2)


__app_export__ = Magic8Ball
