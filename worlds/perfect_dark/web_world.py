from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class PerfectDarkWebWorld(WebWorld):
    game = "Perfect Dark"

    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Perfect Dark for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ajeloom"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
