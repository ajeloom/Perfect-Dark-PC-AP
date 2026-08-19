from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionSet

class Goal(Choice):
    """
    Sets the goal in order to beat the game.

    - Complete Skedar Ruins: Finish the game with Skedar Ruins.
    - Complete Missions: Complete a set number of missions.
    - Complete Challenges: Complete a set number of challenges.
    - Complete Both: Complete a set number of missions and challenges.
    """

    display_name = "Goal"

    option_complete_skedar_ruins = 0
    option_complete_missions = 1
    option_complete_challenges = 2
    option_complete_both = 3

    default = option_complete_skedar_ruins


class SkedarRuinsRequirements(Choice):
    """
    Sets the requirements to unlock Skedar Ruins.
    This option only matters if goal is set to Complete Skedar Ruins.

    - Item: You can get Skedar Ruins as an item which could make the run shorter.
    - Collect Mission Stars: Unlocks after you collect enough mission stars.
    - Collect Challenge Stars: Unlocks after you collect enough challenge stars.
    - Collect Both Stars: Unlocks after you collect enough mission and challenge stars.
    """

    display_name = "Skedar Ruins Requirements"

    option_item = 0
    option_collect_mission_stars = 1
    option_collect_challenge_stars = 2
    option_collect_both_stars = 3
    
    default = option_collect_mission_stars


class PlaceStarsAnywhere(Toggle):
    """
    Choose if you want mission stars and challenge stars to be placed in any location. 
    This option only matters if you need to collect stars for the goal.
    Recommend disabling if you are only playing Perfect Dark by itself.

    - False: Mission stars and challenge stars can only be acquired 
             from completing missions and challenges in your game.
    
    - True: Mission stars and challenge stars can be found in anyone's game.
    """

    display_name = "Place Stars Anywhere"


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
    You must have one of the difficulties enabled if you have 
    to do missions for the goal or Skedar Ruins requirements.
    """

    display_name = "Include Agent"


class RequiredAgentMissionStars(Range):
    """
    Sets the required amount of Agent mission stars to beat the game.
    This option only matters if you have to collect mission stars and Agent is enabled.
    If you are playing more than one difficulty, then the number of mission stars 
    you must collect for the goal is combined from each enabled difficulty.

    The max is 20 if the goal is set to Complete Skedar Ruins.
    """

    display_name = "Required Agent Mission Stars"

    range_start = 1
    range_end = 21
    default = 7


class IncludeSpecialAgent(Toggle):
    """
    Determines whether Special Agent sends location checks.
    You must have one of the difficulties enabled if you have 
    to do missions for the goal or Skedar Ruins requirements.
    """

    display_name = "Include Special Agent"
    default = True


class RequiredSpecialAgentMissionStars(Range):
    """
    Sets the required amount of Special Agent mission stars to beat the game.
    This option only matters if you have to collect mission stars and Special Agent is enabled.
    If you are playing more than one difficulty, then the number of mission stars 
    you must collect for the goal is combined from each enabled difficulty.

    The max is 20 if the goal is set to Complete Skedar Ruins.
    """

    display_name = "Required Special Agent Mission Stars"

    range_start = 1
    range_end = 21
    default = 7


class IncludePerfectAgent(Toggle):
    """
    Determines whether Perfect Agent sends location checks.
    You must have one of the difficulties enabled if you have 
    to do missions for the goal or Skedar Ruins requirements.

    If Perfect Agent is too difficult, you can use Perfect Dark mode
    to lower enemies' health, damage, and accuracy to make it easier.
    Note: Lowering enemy health will also lower your ally's health. 
          Keep this in mind when playing missions with allies you need to keep alive.
    """

    display_name = "Include Perfect Agent"


class RequiredPerfectAgentMissionStars(Range):
    """
    Sets the required amount of Perfect Agent mission stars to beat the game.
    This option only matters if you have to collect mission stars and Perfect Agent is enabled.
    If you are playing more than one difficulty, then the number of mission stars 
    you must collect for the goal is combined from each enabled difficulty.

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

    display_name = "Start with a Mission"


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

    - Progressive Types:
        This splits the progressive weapon into five types:
        Pistols, SMGs, Rifles, Explosives, and Other.
        Your inventory will only be filled with the current
        progressive weapon for each type at the start of a mission.
        You cannot pick up weapons except for the ones required in certain missions.
    """

    display_name = "Weapon Progression"

    option_normal = 0
    option_all_guns = 1
    option_progressive_weapon = 2
    option_progressive_one_gun = 3
    option_progressive_types = 4

    default = option_normal


class ProgressiveWeaponsInChallenges(Toggle):
    """
    Allows you to use progressive weapons in challenges.
    This option only works if challenges are enabled 
    weapon progression is not set to normal.

    - False: You will not start with any weapons in your inventory
             and must pick up weapons that you have unlocked.

    - True: Your progressive weapons will be in your inventory.
    """

    display_name = "Progressive Weapons In Challenges"


class StartWithWeapon(Toggle):
    """
    Start with a weapon in your inventory.

    - Normal and All Guns: You will start with a random weapon.
    - Progressive Weapon and One Gun: You will start with the first progressive weapon.
    - Progressive Types: You will start with a random weapon type.
    """

    display_name = "Start with a Weapon"


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
    If challenge stars are part of the goal, then this option is automatically enabled.
    """

    display_name = "Challenges"


class RequiredChallengeStars(Range):
    """
    Sets the required amount of challenge stars to beat the game.
    This option only matters if you are required to collect challenge stars for the goal.

    If you exclude any challenges and set the required amount of challenge stars to a number
    greater than you can earn, then it automatically sets this to the maximum you can earn.
    """

    display_name = "Required Challenge Stars"

    range_start = 1
    range_end = 30
    default = 15


class ExcludedChallenges(OptionSet):
    """
    Sets which challenges will not appear in the run. 
    Valid challenges are Challenge 1 through Challenge 30.
    Ex: ['Challenge 1', 'Challenge 5', 'Challenge 26']
    """
    display_name = "Excluded Challenges"
    valid_keys = frozenset({
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
        "Challenge 30"
    })
    default = frozenset({})


class ChallengeLogic(Choice):
    """
    Choose how hard the logic will be for the challenges. 

    - Strict: The logic expects you to have every weapon and device in the weapon set.
    - Normal: The logic expects you to have some weapons in the weapon set.
    - Hard: The logic expects you to have one of the weapons in the weapon set.
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

    default = True


class StartWithAllChallenges(Toggle):
    """
    Start with all combat simulator challenges in your inventory.
    This option will only work if challenges are enabled.
    Recommend enabling this if there are not enough locations in your multiworld.
    """

    display_name = "Start with All Challenges"


class WeaponTraining(Toggle):
    """
    Adds the 96 firing range medals as checks.
    Recommend enabling this if you are doing a solo world.
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
    Recommend enabling this so you have checks at the start.
    """

    display_name = "Holotraining"

    default = True


class CompletionCheatUnlocks(Toggle):
    """
    Adds the 17 cheat unlocks that require you to
    complete a mission on any difficulty as checks.
    """

    display_name = "Completion Cheat Unlocks"


class TimedCheatUnlocks(Toggle):
    """
    Adds the 17 cheat unlocks that require you to 
    complete a mission within a time limit as checks.
    Some checks require certain difficulties.
    """

    display_name = "Timed Cheat Unlocks"


class WeaponCheatUnlocks(Toggle):
    """
    Adds the 8 cheat unlocks that require you to
    get gold medals in the firing range as checks.
    """

    display_name = "Weapon Cheat Unlocks"


class IncludeCheatsInItemPool(Toggle):
    """
    Adds the cheats to the item pool.
    
    - False: Cheats will not be sent to you. They can be unlocked the normal way.
    - True: Cheats will be sent to you. They cannot be unlocked the normal way.
    """

    display_name = "Cheats in the Item Pool"


class NPCs(Toggle):
    """
    Adds important NPCs to the item pool.
    They are Cassandra, Dr. Caroll, Jonathan, Elvis, and the President.
    You will not be able to do certain objectives and some missions if they are missing.
    """

    display_name = "NPCs in the Item Pool"


class MultiplayerUnlocks(Toggle):
    """
    Adds 65 checks for getting the multiplayer unlockables
    by completing a number of challenges.
    This option only matters if you have challenges enabled.
    """

    display_name = "Multiplayer Unlocks"


class TrapChance(Range):
    """
    Percentage chance that any filler will be replaced by a trap.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0


class ExcludedTraps(OptionSet):
    """
    Sets which traps will not appear in the item pool. 
    Valid traps are:
        - DK Mode Trap
        - Small Jo Trap
        - Small Characters Trap
        - Slow Motion Trap
        - Enemy Rockets Trap
        - Perfect Darkness Trap
        - Fast Animations Trap
        - Skedar Trap
    Ex: ['DK Mode Trap', 'Slow Motion Trap', 'Skedar Trap']
    """
    display_name = "Excluded Traps"
    valid_keys = frozenset({
        "DK Mode Trap",
        "Small Jo Trap",
        "Small Characters Trap",
        "Slow Motion Trap",
        "Enemy Rockets Trap",
        "Perfect Darkness Trap",
        "Fast Animations Trap",
        "Skedar Trap"
    })
    default = frozenset({})


class DeathLink(Toggle):
    """
    Enables death link in your game, making you die at the same time as other players.
    You can send and receive death links during single player missions.
    You can receive death links in combat simulator but can't send it.
    """

    display_name = "Death Link"


@dataclass
class PerfectDarkOptions(PerGameCommonOptions):
    goal: Goal
    skedar_ruins_requirements: SkedarRuinsRequirements
    place_stars_anywhere: PlaceStarsAnywhere
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
    required_challenge_stars: RequiredChallengeStars
    challenge_logic: ChallengeLogic
    excluded_challenges: ExcludedChallenges
    shorter_challenges: ShorterChallenges
    start_with_all_challenges: StartWithAllChallenges
    weapon_training: WeaponTraining
    device_training: DeviceTraining
    holotraining: Holotraining
    completion_cheats: CompletionCheatUnlocks
    timed_cheats: TimedCheatUnlocks
    weapon_cheats: WeaponCheatUnlocks
    include_cheats_in_item_pool: IncludeCheatsInItemPool
    npcs: NPCs
    multiplayer_unlocks: MultiplayerUnlocks
    trap_chance: TrapChance
    excluded_traps: ExcludedTraps
    deathlink: DeathLink


option_groups = [
    OptionGroup(
        "Gameplay Options",
        [
            Goal,
            SkedarRuinsRequirements,
            PlaceStarsAnywhere,
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
            RequiredChallengeStars,
            ChallengeLogic,
            ExcludedChallenges,
            ShorterChallenges,
            StartWithAllChallenges,
            WeaponTraining,
            DeviceTraining,
            Holotraining,
            CompletionCheatUnlocks,
            TimedCheatUnlocks,
            WeaponCheatUnlocks,
            IncludeCheatsInItemPool,
            NPCs,
            MultiplayerUnlocks,
            TrapChance,
            ExcludedTraps,
            DeathLink
        ],
    ),
]

option_presets = {
    "default": {
        "goal": Goal.option_complete_skedar_ruins,
        "skedar_ruins_requirements": SkedarRuinsRequirements.option_item,
        "place_stars_anywhere:": False,
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
        "required_challenge_stars": 15,
        "challenge_logic": ChallengeLogic.option_normal,
        "shorter_challenges": False,
        "start_with_all_challenges": False,
        "weapon_training": False,
        "device_training": False,
        "holotraining": False,
        "completion_cheats": False,
        "timed_cheats": False,
        "weapon_cheats": False,
        "include_cheats_in_item_pool": True,
        "npcs": False,
        "multiplayer_unlocks": False,
        "trap_chance": 0,
        "deathlink": False,
    },
    "hard": {
        "goal": Goal.option_complete_skedar_ruins,
        "skedar_ruins_requirements": SkedarRuinsRequirements.option_collect_mission_stars,
        "place_stars_anywhere:": False,
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
        "required_challenge_stars": 30,
        "challenge_logic": ChallengeLogic.option_hard,
        "shorter_challenges": False,
        "start_with_all_challenges": False,
        "weapon_training": True,
        "device_training": True,
        "holotraining": True,
        "completion_cheats": True,
        "timed_cheats": True,
        "weapon_cheats": True,
        "include_cheats_in_item_pool": False,
        "npcs": True,
        "multiplayer_unlocks": True,
        "trap_chance": 100,
        "deathlink": True,
    },
}
