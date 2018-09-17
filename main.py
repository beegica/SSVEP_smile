from smile.common import *
from smile.scale import scale as s
from math import sin, pi

from list_gen import gen_stim

@Subroutine
def SSVEPExp(self, config):

    res = Func(gen_stim, config)

    Wait(.5)

    Label(text=config.INST_TEXT,
          markup=True,
          text_width=(s(700), None),
          font_size=s(config.INST_FONT)
          )
    with UntilDone():

        KeyPress(keys=['SPACEBAR'])

    Wait(1.0)

    with Loop(res.result) as block:

        Label(text="+", font_size=s(config.ORIENT_FONT))
        with UntilDone():

            with Loop(block.current) as trial:

                rect = Rectangle(center_x=self.exp.screen.center_x + \
                                          s(config.SPACING_RECT)*trial.current['orientation'],
                                 alpha=0.0, height=config.RECT_DIM,
                                 width=config.RECT_DIM)
                with UntilDone():

                    rect.animate(color=lambda t, initial: (1.0, 1.0, 1.0,
                                                           (1. + Ref(sin, 2*pi*t/trial.current['period']))/2.),
                                 duration=config.ANI_DURATION)

                Wait(config.ISI, jitter=config.JITTER)


if __name__ == "__main__":
    import config as config

    exp = Experiment()
    SSVEPExp(config)

    exp.run()
