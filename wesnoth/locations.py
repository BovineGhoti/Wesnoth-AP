from __future__ import annotations

from typing import TYPE_CHECKING

from core.BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import WesnothWorld

LOCATION_NAME_TO_ID = {
    "Rooting Out a Mage - Victory": 1,
    "The Chase - Victory": 2,
    "Guarded Castle - Victory": 3,
    "Return to the Village - Victory": 4,
}


class WesnothLocation(Location):
    game = "wesnoth"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: WesnothWorld) -> None:
    create_regular_locations(world)
#    create_events(world)


def create_regular_locations(world: WesnothWorld) -> None:
    rooting_out_a_mage = world.get_region("Rooting Out a Mage")
    the_chase = world.get_region("The Chase")
    guarded_castle = world.get_region("Guarded Castle")
    return_to_the_village = world.get_region("Return to the Village")

# EVENTS ARE NOT SOMETHING WE CARE ABOUT RIGHT NOW
# THEY ARE A LATER ISSUE
# def create_events(world: WesnothWorld) -> None:
#    if not True:
#        j: int = 0
#    else:
#        j: int = 1


def create_events(world: WesnothWorld) -> None:
    return_to_the_village = world.get_region("Return to the Village")
    return_to_the_village.add_event("Final Scenario Completed", "Victory", location_type=WesnothLocation,
                                    item_type=items.WesnothItem)

