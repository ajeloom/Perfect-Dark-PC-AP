from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Goal(Choice):
    """
    Sets the goal in order to beat the game. 
    - Complete Skedar Ruins: only requires you fully completing this mission
    - Collect Mission Stars: requires you to collect mission stars by completing missions
    """

    display_name = "Goal"

    option_complete_skedar_ruins = 0
    option_collect_mission_stars = 1

    default = option_complete_skedar_ruins


class RequiredMissionStars(Range):
    """
    Sets the required amount of mission stars to beat the game.
    This option only matters if goal is set to collect mission stars.
    """

    display_name = "Required Mission Stars"

    range_start = 1
    range_end = 21
    default = 14


class StartWithMission(Toggle):
    """
    Start with a mission in your inventory.
    """

    display_name = "Start With a Mission"


class WeaponProgression(Choice):
    """
    Choose how weapon progression will work in your game.
    - Vanilla: You have to find each weapon in order to use and pick up in missions/challenges. 
               You can only use weapons that appear in the mission.
    - Progressive Weapon: You will progress through weapons from weakest to strongest. This allows you 
                          to use weapons in missions/challenges it doesn't appear in. Any previous 
                          progressive weapon will be in your inventory. Certain weapons will appear in 
                          the pool that are required for missions.
    - Progressive Weapon (One Gun): A harder challenge where you are stuck with your current progressive weapon
                                    in a mission until you find another one. You cannot pick up weapons on the
                                    ground unless it is required to beat the mission.
    """

    display_name = "Weapon Progression"

    option_vanilla = 0
    option_progressive_weapon = 1
    option_progressive_weapon_one_gun = 2

    default = option_vanilla


class ProgressiveWeaponsInChallenges(Toggle):
    """
    Allows you to have progressive weapons during challenges.
    If disabled, then you will have to pick up weapons in the challenge that you have reached progressively.
    If enabled, your progressive weapons will be in your inventory.
    This option only works if challenges are enabled.
    """

    display_name = "Progressive Weapons In Challenges"


class StartWithWeapon(Toggle):
    """
    Start with a weapon in your inventory.
    If weapon progression is vanilla, then you will start with a random weapon in your inventory.
    """

    display_name = "Start With a Weapon"


class Challenges(Toggle):
    """
    Adds all 30 combat simulator challenges as checks.
    Each challenge is an item you need to find in order to play it.
    """

    display_name = "Challenges"


class StartWithAllChallenges(Toggle):
    """
    Start with all 30 combat simulator challenges in your inventory. 
    This option will only work if challenges are in the itempool. 
    I recommend enabling this if there are not enough locations in your multiworld.
    """

    display_name = "Start With All Challenges"


class WeaponTraining(Toggle):
    """
    Adds the 96 firing range medals as checks.
    """

    display_name = "Weapon Training"


class DeviceTraining(Toggle):
    """
    Adds the 10 device training as checks.
    """

    display_name = "Device Training"


class Holotraining(Toggle):
    """
    Adds the 7 holotraining as checks.
    """

    display_name = "Holotraining"


class DeathLink(Toggle):
    """
    Enables death link in your game.
    You can send and receive death links during single player missions.
    You can receive death links in combat simulator but can't send it.
    """

    display_name = "Death Link"


@dataclass
class PerfectDarkOptions(PerGameCommonOptions):
    goal: Goal
    required_mission_stars: RequiredMissionStars
    start_with_mission: StartWithMission
    weapon_progression: WeaponProgression
    prog_weapon_in_challenges: ProgressiveWeaponsInChallenges
    start_with_weapon: StartWithWeapon
    challenges: Challenges
    start_with_all_challenges: StartWithAllChallenges
    weapon_training: WeaponTraining
    device_training: DeviceTraining
    holotraining: Holotraining
    deathlink: DeathLink


option_groups = [
    OptionGroup(
        "Gameplay Options",
        [
            Goal, 
            RequiredMissionStars, 
            StartWithMission, 
            WeaponProgression, 
            ProgressiveWeaponsInChallenges,
            StartWithWeapon, 
            Challenges, 
            StartWithAllChallenges, 
            WeaponTraining, 
            DeviceTraining, 
            Holotraining, 
            DeathLink
        ],
    ),
]

option_presets = {
    "default": {
        "goal": Goal.option_complete_skedar_ruins,
        "required_mission_stars": 14,
        "start_with_mission": True,
        "weapon_progression": WeaponProgression.option_vanilla,
        "prog_weapon_in_challenges": False,
        "start_with_weapon": True,
        "challenges": False,
        "start_with_all_challenges": False,
        "weapon_training": False,
        "device_training": False,
        "holotraining": False,
        "deathlink": False,
    },
    "hard": {
        "goal": Goal.option_collect_mission_stars,
        "required_mission_stars": 21,
        "start_with_mission": True,
        "weapon_progression": WeaponProgression.option_progressive_weapon,
        "prog_weapon_in_challenges": False,
        "start_with_weapon": True,
        "challenges": True,
        "start_with_all_challenges": False,
        "weapon_training": True,
        "device_training": True,
        "holotraining": True,
        "deathlink": True,
    },
}
