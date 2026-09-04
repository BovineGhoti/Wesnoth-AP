from __future__ import annotations

from typing import TYPE_CHECKING

from core.rule_builder.options import OptionFilter
from core.rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import WesnothWorld


def set_all_rules(world: WesnothWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: WesnothWorld) -> None:
    pass


def set_all_location_rules(world: WesnothWorld) -> None:
    pass


def set_completion_condition(world: WesnothWorld) -> None:
    world.set_completion_rule(Has("Victory"))

