from collections.abc import Mapping
from typing import Any

from core.worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as wesnoth_options


class WesnothWorld(World):
    """
    A turn based tactical combat game in which you take your rag-tag group of forces fight and level up together as you
    face progressively more powerful foes, until you complete a story, and achieve some sort of resolution. Also, you
    will defy statistics.
    """

    game = "Wesnoth"

    web = web_world.WesnothWebWorld()

    options_dataclass = wesnoth_options.WesnothOptions
    options: wesnoth_options.WesnothOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.WesnothItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "TBD0", "TBD1", "TBD2"
        )
