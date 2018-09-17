







PERIODS = [x/120. for x in range(6, 16)] # fastest = 30hz, slowest = 8hz
ORIENTATIONS = [1, -1]
NUM_REPS = 1
NUM_BLOCKS = 5

ANI_DURATION = 3.0
ISI = .5
JITTER = 1.0

SPACING_RECT = 300
RECT_DIM = 500

ORIENT_FONT = 50
INST_FONT = 35
INST_TEXT = """[b]Welcome to SSVEPExp[/b]

Today, you will be seeing a series of boxes flashing at different frequencies. Your goal is to look directly at a fixation cross (or plus sign) that is in the center of the screen and not to look awayself. These flashing boxes will appear on either the left or the right of the fixation cross, and it is your goal to focus your attention on the box without actually looking at the box.

Try to not to look directly at the flashing boxes, but instead try to focus your attention on the flashing. It is extremely important that you look only at the fixation cross for the duration of this experiment. You should also try your best not to blink while there is a box on the screen, but instead blink during the wait time between presentations of flashing boxes.

When you are ready to continue, please press SPACEBAR!
"""
