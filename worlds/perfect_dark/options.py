from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Goal(Choice):
    """
    Sets the goal in order to beat the game. 

    - Complete Skedar Ruins: Only requires you completing Skedar Ruins on any difficulty.
    - Collect Mission Stars: Requires you to collect mission stars by completing missions.
    """

    display_name = "Goal"

    option_complete_skedar_ruins = 0
    option_collect_mission_stars = 1
    option_collect_challenge_stars = 2

    default = option_complete_skedar_ruins


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
    This option only matters if goal is set to collect mission stars.
    If you are playing more than one difficulty, then you just have 
    to reach the total amount of mission stars for the goal.
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
    This option only matters if goal is set to collect mission stars.
    If you are playing more than one difficulty, then you just have 
    to reach the total amount of mission stars for the goal.
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
    This option only matters if goal is set to collect mission stars.
    If you are playing more than one difficulty, then you just have 
    to reach the total amount of mission stars for the goal.
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

    - Vanilla:
        You have to find each weapon in order to use and pick them up.
        You can only use weapons that normally appear in the missions/challenges.
    
    - Progressive Weapon:
        You will progress through weapons from weakest to strongest. 
        Allowing you to use weapons in missions/challenges they don't appear in. 
        Any previous progressive weapons will be in your inventory. Weapons required  
        for mission objectives are in the itempool so you can do some locations earlier.
    
    - Progressive Weapon (One Gun):
        You progress through the weapons in the same order, but you are stuck 
        with the current progressive weapon until you find another one. 
        You are given infinite ammo and, on certain missions, a laser to prevent softlocks. 
        In missions, only weapons required for some objectives can be picked up. 
        In challenges, you are allowed to pick up other weapons. 
        Only recommended for people who are looking for a challenging run.
    """

    display_name = "Weapon Progression"

    option_vanilla = 0
    option_progressive_weapon = 1
    option_progressive_weapon_one_gun = 2

    default = option_vanilla


class ProgressiveWeaponsInChallenges(Toggle):
    """
    Allows you to use progressive weapons in challenges.
    This option only works if challenges are enabled.

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
    Adds all 30 combat simulator challenges as checks.
    Each challenge is an item you need to find in order to play it.
    Only recommend enabling this if you can handle the harder challenges.
    If goal is set to collect challenge stars, then make sure this option is enabled.
    """

    display_name = "Challenges"


class RequiredChallengeStars(Range):
    """
    Sets the required amount of challenge stars to beat the game.
    This option only matters if goal is set to collect challenge stars.
    """

    display_name = "Required Challenge Stars"

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
    Start with all 30 combat simulator challenges in your inventory. 
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
    required_challenge_stars: RequiredChallengeStars
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
        "mission_logic": MissionLogic.option_normal,
        "agent": False,
        "required_agent_mission_stars": 7,
        "special_agent": False,
        "required_special_agent_mission_stars": 7,
        "perfect_agent": True,
        "required_perfect_agent_mission_stars": 7,
        "start_with_mission": True,
        "weapon_progression": WeaponProgression.option_vanilla,
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
        "goal": Goal.option_collect_mission_stars,
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
