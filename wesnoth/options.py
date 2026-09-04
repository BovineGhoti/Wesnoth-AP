from dataclasses import dataclass

from core.Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class ConfettiExplosiveness(Range):
    """
    How much confetti does the cannon fire?
    """

    display_name = "Confetti Explosiveness"

    range_start = 0
    range_end = 10

    default = 3


class Difficulty(Choice):
    """
    Select chosen difficulty
    """

    display_name = "Difficulty"

    option_easy = 0
    option_hard = 1

    default = option_easy
    alias_default = option_easy


@dataclass
class WesnothOptions(PerGameCommonOptions):
    confetti_explosiveness = ConfettiExplosiveness
    difficulty = Difficulty