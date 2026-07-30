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

    def generate_early(self) -> None:
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Perfect Dark" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Perfect Dark"]

                # Sync options for weighted values
                self.options.goal.value = passthrough["options"]["goal"]
                self.options.skedar_ruins_requirements.value = passthrough["options"]["skedar_ruins_requirements"]
                self.options.mission_logic.value = passthrough["options"]["mission_logic"]
                self.options.agent.value = passthrough["options"]["agent"]
                self.options.required_agent_mission_stars.value = passthrough["options"]["required_agent_mission_stars"]
                self.options.special_agent.value = passthrough["options"]["special_agent"]
                self.options.required_special_agent_mission_stars.value = passthrough["options"]["required_special_agent_mission_stars"]
                self.options.perfect_agent.value = passthrough["options"]["perfect_agent"]
                self.options.required_perfect_agent_mission_stars.value = passthrough["options"]["required_perfect_agent_mission_stars"]
                self.options.weapon_progression.value = passthrough["options"]["weapon_progression"]
                self.options.challenges.value = passthrough["options"]["challenges"]
                self.options.required_challenge_stars.value = passthrough["options"]["required_challenge_stars"]
                self.options.challenge_logic.value = passthrough["options"]["challenge_logic"]
                self.options.weapon_training.value = passthrough["options"]["weapon_training"]
                self.options.device_training.value = passthrough["options"]["device_training"]
                self.options.holotraining.value = passthrough["options"]["holotraining"]
                self.options.unlock_cheats.value = passthrough["options"]["unlock_cheats"]

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

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data: dict[str, Any] = {
            "options": {
                "goal": self.options.goal.value,
                "skedar_ruins_requirements": self.options.skedar_ruins_requirements.value,
                "mission_logic": self.options.mission_logic.value,
                "agent": self.options.agent.value,
                "required_agent_mission_stars": self.options.required_agent_mission_stars.value,
                "special_agent": self.options.special_agent.value,
                "required_special_agent_mission_stars": self.options.required_special_agent_mission_stars.value,
                "perfect_agent": self.options.perfect_agent.value,
                "required_perfect_agent_mission_stars": self.options.required_perfect_agent_mission_stars.value,
                "weapon_progression": self.options.weapon_progression.value,
                "allow_progressive_weapon_in_challenges": self.options.allow_progressive_weapon_in_challenges.value,
                "master_key": self.options.master_key.value,
                "challenges": self.options.challenges.value,
                "required_challenge_stars": self.options.required_challenge_stars.value,
                "challenge_logic": self.options.challenge_logic.value,
                "shorter_challenges": self.options.shorter_challenges.value,
                "weapon_training": self.options.weapon_training.value,
                "device_training": self.options.device_training.value,
                "holotraining": self.options.holotraining.value,
                "unlock_cheats": self.options.unlock_cheats.value,
                "deathlink": self.options.deathlink.value,
            },
        }

        return slot_data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data
