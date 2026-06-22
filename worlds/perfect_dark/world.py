from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as pd_options

class PerfectDarkWorld(World):
    game = "Perfect Dark"

    web = web_world.PerfectDarkWebWorld()

    options_dataclass = pd_options.PerfectDarkOptions
    options: pd_options.PerfectDarkOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Carrington Institute"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.PerfectDarkItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        required_mission_stars = 0
        if self.options.agent:
            required_mission_stars += self.options.required_agent_mission_stars.value
        if self.options.special_agent:
            required_mission_stars += self.options.required_special_agent_mission_stars.value
        if self.options.perfect_agent:
            required_mission_stars += self.options.required_perfect_agent_mission_stars.value

        slot_data = {
            "options": {
                "goal": self.options.goal.value,
                "required_mission_stars": required_mission_stars,
                "weapon_progression": self.options.weapon_progression.value,
                "allow_progressive_weapon_in_challenges": self.options.allow_progressive_weapon_in_challenges.value,
                "challenges": self.options.challenges.value,
                "weapon_training": self.options.weapon_training.value,
                "device_training": self.options.device_training.value,
                "holotraining": self.options.holotraining.value,
                "unlock_cheats": self.options.unlock_cheats.value,
                "deathlink": self.options.deathlink.value,
            },
        }

        return slot_data
