from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionSet

class Goal(Choice):
    """
    Sets the goal in order to beat the game. 

    - Complete Skedar Ruins: Finish the game with Skedar Ruins.
    - Complete # of Missions: Complete a set number of missions.
    """

    display_name = "Goal"

    option_complete_skedar_ruins = 0
    option_collect_mission_stars = 1
    option_collect_challenge_stars = 2

    default = option_complete_skedar_ruins


class SkedarRuinsRequirements(Choice):
    """
    Sets the requirements to unlock Skedar Ruins.
    This option only matters if goal is set to Complete Skedar Ruins.

    - Item: You can get Skedar Ruins as an item which could make the run shorter.
    - Collect Mission Stars: Unlocks after you collect enough mission stars.
    """

    display_name = "Skedar Ruins Requirements"

    option_item = 0
    option_collect_mission_stars = 1

    default = option_collect_mission_stars


class MissionLogic(Choice):
    """
    Choose how hard the logic will be for the missions. 
    This will also affect cheats as they share the same logic.

    - Normal: The logic expects you to have the starting weapon in missions.
    - Veteran: The logic is the same as Normal but it expects you to use hidden items.
    - Hard: The logic expects you to disarm enemies for a weapon in missions.
    - Perfect: The logic expects you to play near perfect in missions.

    Note: Hard and Perfect includes the hidden items in logic
    """

    display_name = "Mission Logic"

    option_normal = 0
    option_veteran = 1
    option_hard = 2
    option_perfect = 3

    default = option_normal


class IncludeAgent(Toggle):
    """
    Determines whether Agent sends location checks.
    """

    display_name = "Include Agent"


class RequiredAgentMissionStars(Range):
    """
    Sets the required amount of Agent mission stars to beat the game.
    This option only matters if you have to collect mission stars and Agent is enabled.
    If you are playing more than one difficulty, then you just have 
    to reach the total amount of mission stars for the goal.

    The max is 20 if the goal is set to Complete Skedar Ruins.
    """

    display_name = "Required Agent Mission Stars"

    range_start = 1
    range_end = 21
    default = 7


class IncludeSpecialAgent(Toggle):
    """
    Determines whether Special Agent sends location checks.
    """

    display_name = "Include Special Agent"
    default = True


class RequiredSpecialAgentMissionStars(Range):
    """
    Sets the required amount of Special Agent mission stars to beat the game.
    This option only matters if you have to collect mission stars and Special Agent is enabled.
    If you are playing more than one difficulty, then you just have 
    to reach the total amount of mission stars for the goal.

    The max is 20 if the goal is set to Complete Skedar Ruins.
    """

    display_name = "Required Special Agent Mission Stars"

    range_start = 1
    range_end = 21
    default = 7


class IncludePerfectAgent(Toggle):
    """
    Determines whether Perfect Agent sends location checks.
    If Perfect Agent is too difficult, you can use Perfect Dark mode
    to lower enemies' health, damage, and accuracy to make it easier.
    """

    display_name = "Include Perfect Agent"


class RequiredPerfectAgentMissionStars(Range):
    """
    Sets the required amount of Perfect Agent mission stars to beat the game.
    This option only matters if you have to collect mission stars and Perfect Agent is enabled.
    If you are playing more than one difficulty, then you just have 
    to reach the total amount of mission stars for the goal.

    The max is 20 if the goal is set to Complete Skedar Ruins.
    """

    display_name = "Required Perfect Agent Mission Stars"

    range_start = 1
    range_end = 21
    default = 7


class StartWithMission(Toggle):
    """
    Start with a random mission in your inventory.
    """

    display_name = "Start With a Mission"


class WeaponProgression(Choice):
    """
    Choose how weapon progression will work in your game.

    - Normal:
        Every weapon, except for the classic weapons, is its own item in the itempool.
        You start a mission with the weapons that you normally would once you unlock them.
        You can only pick up unlocked weapons and use them.
        Pick this for the most vanilla experience.

    - All Guns:
        Every weapon in the game is its own item in the itempool.
        Every weapon you unlocked will be in your inventory at the start of a mission.
        This allows you to use weapons in missions they normally don't appear in.
    
    - Progressive Weapon:
        You will progress through weapons from weakest to strongest. 
        Every weapon you progress through will be in your inventory at the start of a mission.
        Some weapons required for mission objectives are in the itempool so that some locations can be done earlier.
    
    - Progressive One Gun:
        You progress through the weapons in the same order, but you will only have
        the current progressive weapon in your inventory at the start of a mission. 
        You are given infinite ammo and a laser on some missions to prevent softlocks. 
        In missions, other weapons cannot be picked up except for the ones required for some objectives. 
        In challenges, you are allowed to pick up other weapons. 
        Only recommended for people who are looking for a challenging run.
    """

    display_name = "Weapon Progression"

    option_normal = 0
    option_all_guns = 1
    option_progressive_weapon = 2
    option_progressive_one_gun = 3

    default = option_normal


class ProgressiveWeaponsInChallenges(Toggle):
    """
    Allows you to use progressive weapons in challenges.
    This option only works if challenges are enabled 
    weapon progression is not set to vanilla.

    - False: You will have to pick up weapons in the challenge 
             that you have reached progressively.
             
    - True: Your progressive weapons will be in your inventory.
    """

    display_name = "Progressive Weapons In Challenges"


class StartWithWeapon(Toggle):
    """
    Start with a weapon in your inventory.
    If weapon progression is vanilla, then you will 
    start with a random weapon in your inventory.
    """

    display_name = "Start With a Weapon"


class MasterKey(Toggle):
    """
    Combines any key cards into one item for the mission area.
    Any missions that only have one key card will just use that item.
    You will still need to pick up the key card in the mission to use it.
    """

    display_name = "Master Key"


class Challenges(Toggle):
    """
    Adds the combat simulator challenges as checks.
    Each challenge is an item you need to find in order to play it.
    Only recommend enabling this if you can handle the harder challenges.
    If goal is set to collect challenge stars, then make sure this option is enabled.
    """

    display_name = "Challenges"


class AllowedChallenges(OptionSet):
    """
    Sets which challenges you have to do.
    """
    display_name = "Allowed Challenges"
    valid_keys = [
        "Challenge 1",
        "Challenge 2",
        "Challenge 3",
        "Challenge 4",
        "Challenge 5",
        "Challenge 6",
        "Challenge 7",
        "Challenge 8",
        "Challenge 9",
        "Challenge 10",
        "Challenge 11",
        "Challenge 12",
        "Challenge 13",
        "Challenge 14",
        "Challenge 15",
        "Challenge 16",
        "Challenge 17",
        "Challenge 18",
        "Challenge 19",
        "Challenge 20",
        "Challenge 21",
        "Challenge 22",
        "Challenge 23",
        "Challenge 24",
        "Challenge 25",
        "Challenge 26",
        "Challenge 27",
        "Challenge 28",
        "Challenge 29",
        "Challenge 30",
    ]
    default = valid_keys.copy()



    range_start = 1
    range_end = 30
    default = 15


class ChallengeLogic(Choice):
    """
    Choose how hard the logic will be for the challenges. 

    No Progressive Weapons
    - Strict: The logic expects you to have every weapon in the weapon set.
    - Normal: The logic expects you to have some weapons in the weapon set.
    - Hard: The logic expects you to have one of the weapons in the weapon set.

    Progressive Weapons
    - Strict: The logic expects you to have the highest progressive weapon in the weapon set.
    - Normal: The logic is more balanced.
    - Hard: The logic expects you to have the lowest progressive weapon in the weapon set.
    """

    display_name = "Challenge Logic"

    option_strict = 0
    option_normal = 1
    option_hard = 2

    default = option_normal


class ShorterChallenges(Toggle):
    """
    Shortens each challenge's time limit and score limit.
    """

    display_name = "Shorter Challenges"


class StartWithAllChallenges(Toggle):
    """
    Start with all combat simulator challenges in your inventory.
    This option will only work if challenges are enabled. 
    Recommend enabling this if there are not enough locations in your multiworld.
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


class UnlockCheats(Toggle):
    """
    Adds the unlockable cheats as checks.
    Some checks require certain difficulties or weapon training.

    - False: Meeting the requirements to unlock a cheat won't send a check.
             You can unlock the cheat the normal way or wait for it to be sent to you.

    - True: Meeting the requirements to unlock a cheat will send a check.
            You can't unlock cheats the normal way, so you have to wait for it be sent to you.
    """

    display_name = "Unlock Cheats"


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
    skedar_ruins_requirements : SkedarRuinsRequirements
    mission_logic: MissionLogic
    agent: IncludeAgent
    required_agent_mission_stars: RequiredAgentMissionStars
    special_agent: IncludeSpecialAgent
    required_special_agent_mission_stars: RequiredSpecialAgentMissionStars
    perfect_agent: IncludePerfectAgent
    required_perfect_agent_mission_stars: RequiredPerfectAgentMissionStars
    start_with_mission: StartWithMission
    weapon_progression: WeaponProgression
    allow_progressive_weapon_in_challenges: ProgressiveWeaponsInChallenges
    start_with_weapon: StartWithWeapon
    master_key: MasterKey
    challenges: Challenges
    challenge_logic: ChallengeLogic
    allowed_challenges: AllowedChallenges
    shorter_challenges: ShorterChallenges
    start_with_all_challenges: StartWithAllChallenges
    weapon_training: WeaponTraining
    device_training: DeviceTraining
    holotraining: Holotraining
    unlock_cheats: UnlockCheats
    deathlink: DeathLink


option_groups = [
    OptionGroup(
        "Gameplay Options",
        [
            Goal,
            SkedarRuinsRequirements,
            MissionLogic,
            IncludeAgent,
            RequiredAgentMissionStars,
            IncludeSpecialAgent,
            RequiredSpecialAgentMissionStars,
            IncludePerfectAgent,
            RequiredPerfectAgentMissionStars,
            StartWithMission,
            WeaponProgression,
            ProgressiveWeaponsInChallenges,
            StartWithWeapon,
            MasterKey,
            Challenges,
            ChallengeLogic,
            RequiredChallengeStars,
            ShorterChallenges,
            StartWithAllChallenges,
            WeaponTraining,
            DeviceTraining,
            Holotraining,
            UnlockCheats,
            DeathLink
        ],
    ),
]

option_presets = {
    "default": {
        "goal": Goal.option_complete_skedar_ruins,
        "skedar_ruins_requirements": SkedarRuinsRequirements.option_item,
        "mission_logic": MissionLogic.option_normal,
        "agent": False,
        "required_agent_mission_stars": 7,
        "special_agent": False,
        "required_special_agent_mission_stars": 7,
        "perfect_agent": True,
        "required_perfect_agent_mission_stars": 7,
        "start_with_mission": True,
        "weapon_progression": WeaponProgression.option_normal,
        "allow_progressive_weapon_in_challenges": False,
        "start_with_weapon": True,
        "master_key": False,
        "challenges": False,
        "challenge_logic": ChallengeLogic.option_normal,
        "required_challenge_stars": 15,
        "shorter_challenges": False,
        "start_with_all_challenges": False,
        "weapon_training": False,
        "device_training": False,
        "holotraining": False,
        "unlock_cheats": False,
        "deathlink": False,
    },
    "hard": {
        "goal": Goal.option_complete_skedar_ruins,
        "skedar_ruins_requirements": SkedarRuinsRequirements.option_collect_mission_stars,
        "mission_logic": MissionLogic.option_hard,
        "agent": False,
        "required_agent_mission_stars": 7,
        "special_agent": False,
        "required_special_agent_mission_stars": 7,
        "perfect_agent": True,
        "required_perfect_agent_mission_stars": 21,
        "start_with_mission": True,
        "weapon_progression": WeaponProgression.option_progressive_weapon,
        "allow_progressive_weapon_in_challenges": False,
        "start_with_weapon": True,
        "master_key": False,
        "challenges": True,
        "challenge_logic": ChallengeLogic.option_hard,
        "required_challenge_stars": 30,
        "shorter_challenges": False,
        "start_with_all_challenges": False,
        "weapon_training": True,
        "device_training": True,
        "holotraining": True,
        "unlock_cheats": True,
        "deathlink": True,
    },
}
