from __future__ import annotations

from typing import TYPE_CHECKING

from core.BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import WesnothWorld


    ITEM_NAME_TO_ID = {
        "Spearman": 1,
        "Heavy Infantryman": 2,
        "Bowman": 3,
        "Fencer": 4,
        "Horseman": 5,
        "Cavalryman": 6,
        "Merman Fighter": 7,
        "Mage": 8,
        "Elvish Archer": 9,
        "Elvish Fighter": 10,
        "Elvish Scout": 11,
        "Elvish Shaman": 12,
        "Wose": 13,
        "Merman Hunter": 14,
        "Confetti Cannon": 15,
        "Math Trap": 16,
    }  # TO ADD:
    # 5 Other default factions
    # Filler
    # Traps

    DEFAULT_ITEM_CLASSIFICATIONS = {
        "Spearman": ItemClassification.useful,
        "Heavy Infantryman": ItemClassification.useful,
        "Bowman": ItemClassification.useful,
        "Fencer": ItemClassification.useful,
        "Horseman": ItemClassification.useful,
        "Cavalryman": ItemClassification.useful,
        "Merman Fighter": ItemClassification.useful,
        "Mage": ItemClassification.useful,
        "Elvish Archer": ItemClassification.useful,
        "Elvish Fighter": ItemClassification.useful,
        "Elvish Scout": ItemClassification.useful,
        "Elvish Shaman": ItemClassification.useful,
        "Wose": ItemClassification.useful,
        "Merman Hunter": ItemClassification.useful,
        "Confetti Cannon": ItemClassification.filler,
        "Math Trap": ItemClassification.trap,
    }


class WesnothItem(Item):
    game = "Wesnoth"


def get_random_filler_item_name(world: WesnothWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "Math Trap"
    return "Confetti Cannon"


def create_item_with_correct_classification(world: WesnothWorld, name: str) -> WesnothItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return WesnothItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: WesnothWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Spearman"),
        world.create_item("Heavy Infantryman"),
        world.create_item("Bowman"),
        world.create_item("Fencer"),
        world.create_item("Horseman"),
        world.create_item("Cavalyrman"),
        world.create_item("Merman Fighter"),
        world.create_item("Mage"),
        world.create_item("Elvish Archer"),
        world.create_item("Elvish Fighter"),
        world.create_item("Elvish Scout"),
        world.create_item("Elvish Shaman"),
        world.create_item("Wose"),
        world.create_item("Merman Hunter"),
    ]
    #for itr in ITEM_NAME_TO_ID:
    #    itempool.append(world.create_item(itr))

    number_of_items: int = len(itempool)
    number_of_unfilled_locations: int = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items: int = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    ## PRECOLLECTED ITEMS HERE
    # 3x times
    # starting_rand_unit = world.create_item( (<RAND STARTING UINT>) )
    # world.push_precollected(starting_rand_unit)