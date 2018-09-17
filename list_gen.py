
from random import shuffle




def gen_stim(config):

    blocks = []
    for x in range(config.NUM_BLOCKS):            # Spread out over multi blocks
        block = []
        for period in config.PERIODS:             # All periods
            for i in range(config.NUM_REPS):      # Reps of all orientations
                for ori in config.ORIENTATIONS:   # Orientations
                    block.append({'period':period,
                                  'orientation':ori,
                                  })
        shuffle(block)
        blocks.append(block)
    shuffle(blocks)
    return blocks
