from __future__ import annotations

from typing import TYPE_CHECKING

from core.BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import WesnothWorld


def create_and_connect_regions(world: WesnothWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: WesnothWorld) -> None:
    rooting_out_a_mage = Region("Rooting Out a Mage", world.player, world.multiworld)
    the_chase = Region("The Chase", world.player, world.multiworld)
    guarded_castle = Region("Guarded Castle", world.player, world.multiworld)
    return_to_the_village = Region("Return to the Village", world.player, world.multiworld)

    regions = [rooting_out_a_mage, the_chase, guarded_castle, return_to_the_village]

    world.multiworld.regions += regions


def connect_regions(world: WesnothWorld) -> None:
    rooting_out_a_mage = world.get_region("Rooting Out a Mage")
    the_chase = world.get_region("The Chase")
    guarded_castle = world.get_region("Guarded Castle")
    return_to_the_village = world.get_region("Return to the Village")

