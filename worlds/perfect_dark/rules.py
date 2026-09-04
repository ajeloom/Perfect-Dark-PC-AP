from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, HasFromList

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements, MissionLogic, WeaponProgression, ChallengeLogic, NPCs
from .items import has_challenges

npc_filter = OptionFilter(NPCs, True)

HAS_DD_KEYS = (Has("De Vries' Necklace") | Has("dataDyne Master Key")) & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
HAS_CASS_OFFICE_KEY = Has("Cassandra's Office Key Card") | Has("dataDyne Master Key")
HAS_G5_KEYS = HasAll("G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card") | Has("G5 Building Master Key")
HAS_A51_INFIL_KEYS = Has("Area 51 Lift Key Card") | Has("Area 51 Master Key")
HAS_A51_RESCUE_FIRST_KEY = Has("Medlab 2 Key Card") | Has("Area 51 Master Key")
HAS_A51_RESCUE_ALL_KEYS = HasAll("Medlab 2 Key Card", "Op Room Key Card") | Has("Area 51 Master Key")
HAS_AFO_LIFT_KEY = Has("Air Force One Lift Key Card") | Has("Air Force One Master Key")
HAS_AFO_EXTRA_KEYS = Has("Air Force One Left Room Key Card") | Has("Air Force One Right Room Key Card") | Has("Air Force One Master Key")
HAS_AFO_LEFT_KEY = Has("Air Force One Left Room Key Card") | Has("Air Force One Master Key")
HAS_AFO_RIGHT_KEY = Has("Air Force One Right Room Key Card") | Has("Air Force One Master Key")
HAS_AFO_ALL_KEYS = (Has("Air Force One Lift Key Card") & (Has("Air Force One Left Room Key Card") | Has("Air Force One Right Room Key Card"))) | Has("Air Force One Master Key")

HAS_SKEDAR_RUINS_AGENT = Has("Skedar Ruins - Agent") | Has("Skedar Ruins")
HAS_SKEDAR_RUINS_SP_AGENT = Has("Skedar Ruins - Special Agent") | Has("Skedar Ruins")
HAS_SKEDAR_RUINS_PF_AGENT = Has("Skedar Ruins - Perfect Agent") | Has("Skedar Ruins")

normal_weapon_filter = OptionFilter(WeaponProgression, WeaponProgression.option_normal)
all_guns_filter = OptionFilter(WeaponProgression, WeaponProgression.option_all_guns)
progressive_weapon_filter = [
                                OptionFilter(WeaponProgression, WeaponProgression.option_progressive_weapon),
                                OptionFilter(WeaponProgression, WeaponProgression.option_progressive_one_gun),
                            ]
progressive_types_filter = OptionFilter(WeaponProgression, WeaponProgression.option_progressive_types)

# All Guns Weapon Progression
WEAPON_NAME_LIST = (
    # "Combat Knife",
    # "Psychosis Gun",
    # "Tranquilizer",
    "KL01313",
    "CC13",
    "Laser",
    "Crossbow",
    "Sniper Rifle",
    "Falcon 2",
    "Falcon 2 (Silencer)",
    "Falcon 2 (Scope)",
    "PP9i",
    "MagSec 4",
    "DY357 Magnum",
    "Shotgun",
    "KF7 Special",
    "DMC",
    "ZZT (9mm)",
    "CMP150",
    "Dragon",
    "Reaper",
    "AR34",
    "Cyclone",
    "Laptop Gun",
    # "Timed Mine",
    # "Proximity Mine",
    # "Grenade",
    # "Slayer",
    # "Remote Mine",
    # "N-Bomb",
    "K7 Avenger",
    "Callisto NTG",
    "AR53",
    # "Rocket Launcher",
    # "Devastator",
    "SuperDragon",
    "Mauler",
    "Phoenix",
    "RC-P45",
    "RC-P120",
    "DY357-LX",
    "FarSight XR-20")

# HAS_ANY_PISTOL = HasAny(
#     "CC13",
#     "Falcon 2",
#     "Falcon 2 (Silencer)",
#     "Falcon 2 (Scope)",
#     "PP9i",
#     "MagSec 4",
#     "DY357 Magnum",
#     "Mauler",
#     "Phoenix",
#     "DY357-LX")

# HAS_ANY_SMG = HasAny(
#     "KL01313",
#     "DMC",
#     "ZZT (9mm)",
#     "CMP150",
#     "Cyclone",
#     "Laptop Gun",
#     "Callisto NTG",
#     "RC-P45",
#     "RC-P120")

HAS_ANY_RIFLE = HasAny(
    "KF7 Special",
    "Dragon",
    "AR34",
    "K7 Avenger",
    "AR53",
    "SuperDragon")

EXPLOSIVE_LIST = (
    "Timed Mine",
    "Proximity Mine",
    "Grenade",
    "Slayer",
    "Remote Mine",
    "Rocket Launcher",
    "Devastator",
    "SuperDragon",
    "Phoenix")

# HAS_ANY_OTHER_WEAPON = HasAny(
#     "Combat Knife",
#     "Psychosis Gun",
#     "Tranquilizer",
#     "Laser",
#     "Crossbow",
#     "Sniper Rifle",
#     "Shotgun",
#     "Reaper",
#     "FarSight XR-20")

# Progressive Weapon
PROGRESSIVE_WEAPON_NAME_TO_ID = {
    "Combat Knife": 1,
    "Psychosis Gun": 2,
    "Tranquilizer": 3,
    "KL01313": 4,
    "CC13": 5,
    "Laser": 6,
    "Crossbow": 7,
    "Sniper Rifle": 8,
    "Falcon 2": 9,
    "Falcon 2 (Silencer)": 10,
    "Falcon 2 (Scope)": 11,
    "PP9i": 12,
    "MagSec 4": 13,
    "DY357 Magnum": 14,
    "Shotgun": 15,
    "KF7 Special": 16,
    "DMC": 17,
    "ZZT (9mm)": 18,
    "CMP150": 19,
    "Dragon": 20,
    "Reaper": 21,
    "AR34": 22,
    "Cyclone": 23,
    "Laptop Gun": 24,
    "Timed Mine": 25,
    "Proximity Mine": 26,
    "Grenade": 27,
    "Slayer": 28,
    "Remote Mine": 29,
    "N-Bomb": 30,
    "K7 Avenger": 31,
    "Callisto NTG": 32,
    "AR53": 33,
    "Rocket Launcher": 34,
    "Devastator": 35,
    "SuperDragon": 36,
    "Mauler": 37,
    "Phoenix": 38,
    "RC-P45": 39,
    "RC-P120": 40,
    "DY357-LX": 41,
    "FarSight XR-20": 42,
}

PROGRESSIVE_PISTOL_NAME_TO_ID = {
    "CC13": 1,
    "Falcon 2": 2,
    "Falcon 2 (Silencer)": 3,
    "Falcon 2 (Scope)": 4,
    "PP9i": 5,
    "MagSec 4": 6,
    "DY357 Magnum": 7,
    "Mauler": 8,
    "Phoenix": 9,
    "DY357-LX": 10,
}

PROGRESSIVE_SMG_NAME_TO_ID = {
    "KL01313": 1,
    "DMC": 2,
    "ZZT (9mm)": 3,
    "CMP150": 4,
    "Cyclone": 5,
    "Laptop Gun": 6,
    "Callisto NTG": 7,
    "RC-P45": 8,
    "RC-P120": 9,
}

PROGRESSIVE_RIFLE_NAME_TO_ID = {
    "KF7 Special": 1,
    "Dragon": 2,
    "AR34": 3,
    "K7 Avenger": 4,
    "AR53": 5,
    "SuperDragon": 6,
}

PROGRESSIVE_EXPLOSIVE_NAME_TO_ID = {
    "Timed Mine": 1,
    "Proximity Mine": 2,
    "Grenade": 3,
    "Slayer": 4,
    "Remote Mine": 5,
    "N-Bomb": 6,
    "Rocket Launcher": 7,
    "Devastator": 8,
}

PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID = {
    "Combat Knife": 1,
    "Psychosis Gun": 2,
    "Tranquilizer": 3,
    "Laser": 4,
    "Crossbow": 5,
    "Sniper Rifle": 6,
    "Shotgun": 7,
    "Reaper": 8,
    "FarSight XR-20": 9,
}

weapon_types = ("Progressive Pistol", "Progressive SMG", "Progressive Rifle", "Progressive Explosive")
HAS_ANY_WEAPON_TYPE = ((Has("Progressive Other Weapon", count=4) & HasFromList(*weapon_types, count=1)) | HasFromList(*weapon_types, count=2))

def set_all_rules(world: PerfectDarkWorld) -> None:
    set_all_entrance_rules(world)

    if world.options.mission_logic.value == MissionLogic.option_normal:
        set_all_normal_location_rules(world)
    elif world.options.mission_logic.value == MissionLogic.option_veteran:
        set_all_veteran_location_rules(world)
    elif world.options.mission_logic.value == MissionLogic.option_hard:
        set_all_hard_location_rules(world)
    elif world.options.mission_logic.value == MissionLogic.option_perfect:
        set_all_perfect_location_rules(world)
 
    if ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_mission_stars)
            or world.options.goal.value == Goal.option_complete_missions):
        required_mission_stars = get_mission_stars(world)

        collect_stars = world.get_location("Collect All Stars")
        world.set_rule(collect_stars, Has("Mission Star", count=required_mission_stars))
    
    elif ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_challenge_stars)
            or world.options.goal.value == Goal.option_complete_challenges):
        required_challenge_stars = get_challenge_stars(world)

        collect_stars = world.get_location("Collect All Stars")
        world.set_rule(collect_stars, Has("Challenge Star", count=required_challenge_stars))

    elif ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_both_stars)
            or world.options.goal.value == Goal.option_complete_both):
        required_mission_stars = get_mission_stars(world)
        required_challenge_stars = get_challenge_stars(world)

        collect_stars = world.get_location("Collect All Stars")
        world.set_rule(collect_stars, Has("Mission Star", count=required_mission_stars) & Has("Challenge Star", count=required_challenge_stars))

    set_all_extra_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: PerfectDarkWorld) -> None:
    ci_to_defection = world.get_entrance("Carrington Institute to Defection")
    ci_to_investigation = world.get_entrance("Carrington Institute to Investigation")
    ci_to_extraction = world.get_entrance("Carrington Institute to Extraction")
    ci_to_villa = world.get_entrance("Carrington Institute to Carrington Villa")
    ci_to_chicago = world.get_entrance("Carrington Institute to Chicago")
    ci_to_g5_building = world.get_entrance("Carrington Institute to G5 Building")
    ci_to_infiltration = world.get_entrance("Carrington Institute to Infiltration")
    ci_to_rescue = world.get_entrance("Carrington Institute to Rescue")
    ci_to_escape = world.get_entrance("Carrington Institute to Escape")
    ci_to_air_base = world.get_entrance("Carrington Institute to Air Base")
    ci_to_air_force_one = world.get_entrance("Carrington Institute to Air Force One")
    ci_to_crash_site = world.get_entrance("Carrington Institute to Crash Site")
    ci_to_pelagic = world.get_entrance("Carrington Institute to Pelagic II")
    ci_to_deep_sea = world.get_entrance("Carrington Institute to Deep Sea")
    ci_to_defense = world.get_entrance("Carrington Institute to Defense")
    ci_to_attack_ship = world.get_entrance("Carrington Institute to Attack Ship")
    ci_to_skedar_ruins = world.get_entrance("Carrington Institute to Skedar Ruins")
    ci_to_mbr = world.get_entrance("Carrington Institute to Mr. Blonde's Revenge")
    ci_to_maian_sos = world.get_entrance("Carrington Institute to Maian SOS")
    ci_to_war = world.get_entrance("Carrington Institute to War!")
    ci_to_duel = world.get_entrance("Carrington Institute to The Duel")

    world.set_rule(ci_to_defection, Has("dD Defection - Agent") | Has("dD Defection - Special Agent") | Has("dD Defection - Perfect Agent"))
    world.set_rule(ci_to_investigation, Has("dD Investigation - Agent") | Has("dD Investigation - Special Agent") | Has("dD Investigation - Perfect Agent"))
    world.set_rule(ci_to_extraction, Has("dD Extraction - Agent") | Has("dD Extraction - Special Agent") | Has("dD Extraction - Perfect Agent"))
    world.set_rule(ci_to_villa, Has("Carrington Villa - Agent") | Has("Carrington Villa - Special Agent") | Has("Carrington Villa - Perfect Agent"))
    world.set_rule(ci_to_chicago, Has("Chicago - Agent") | Has("Chicago - Special Agent") | Has("Chicago - Perfect Agent"))
    world.set_rule(ci_to_g5_building, Has("G5 Building - Agent") | Has("G5 Building - Special Agent") | Has("G5 Building - Perfect Agent"))
    world.set_rule(ci_to_infiltration, Has("A51 Infiltration - Agent") | Has("A51 Infiltration - Special Agent") | Has("A51 Infiltration - Perfect Agent"))
    world.set_rule(ci_to_rescue, Has("A51 Rescue - Agent") | Has("A51 Rescue - Special Agent") | Has("A51 Rescue - Perfect Agent"))
    world.set_rule(ci_to_escape, Has("A51 Escape - Agent") | Has("A51 Escape - Special Agent") | Has("A51 Escape - Perfect Agent"))
    world.set_rule(ci_to_air_base, Has("Air Base - Agent") | Has("Air Base - Special Agent") | Has("Air Base - Perfect Agent"))
    world.set_rule(ci_to_air_force_one, Has("Air Force One - Agent") | Has("Air Force One - Special Agent") | Has("Air Force One - Perfect Agent"))
    world.set_rule(ci_to_crash_site, Has("Crash Site - Agent") | Has("Crash Site - Special Agent") | Has("Crash Site - Perfect Agent"))
    world.set_rule(ci_to_pelagic, Has("Pelagic II - Agent") | Has("Pelagic II - Special Agent") | Has("Pelagic II - Perfect Agent"))
    world.set_rule(ci_to_deep_sea, Has("Deep Sea - Agent") | Has("Deep Sea - Special Agent") | Has("Deep Sea - Perfect Agent"))
    world.set_rule(ci_to_defense, Has("CI Defense - Agent") | Has("CI Defense - Special Agent") | Has("CI Defense - Perfect Agent"))
    world.set_rule(ci_to_attack_ship, Has("Attack Ship - Agent") | Has("Attack Ship - Special Agent") | Has("Attack Ship - Perfect Agent"))
    world.set_rule(ci_to_skedar_ruins, Has("Skedar Ruins - Agent") | Has("Skedar Ruins - Special Agent") | Has("Skedar Ruins - Perfect Agent") | Has("Skedar Ruins"))
    world.set_rule(ci_to_mbr, Has("Mr. Blonde's Revenge - Agent") | Has("Mr. Blonde's Revenge - Special Agent") | Has("Mr. Blonde's Revenge - Perfect Agent"))
    world.set_rule(ci_to_maian_sos, Has("Maian SOS - Agent") | Has("Maian SOS - Special Agent") | Has("Maian SOS - Perfect Agent"))
    world.set_rule(ci_to_war, Has("WAR! - Agent") | Has("WAR! - Special Agent") | Has("WAR! - Perfect Agent"))
    world.set_rule(ci_to_duel, Has("The Duel - Agent") | Has("The Duel - Special Agent") | Has("The Duel - Perfect Agent"))


def set_all_normal_location_rules(world: PerfectDarkWorld) -> None:
    agent_rules_normal = {
        # Stage 1 - Defection
        "dD Defection - Agent Objective 1": Has("dD Defection - Agent")
                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Agent": Has("dD Defection - Agent")
                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                          | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Agent Objective 1": HasAll("dD Investigation - Agent", "CamSpy")
                                                & (Has("Falcon 2")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Agent Objective 2": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Agent": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & (HasAll("Falcon 2", "CMP150")
                                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Agent Objective 1": HasAll("dD Extraction - Agent", "Night Vision")
                                             & (Has("Falcon 2 (Scope)")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 2": HasAll("dD Extraction - Agent", "Night Vision")
                                             & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 3": HasAll("dD Extraction - Agent", "Night Vision")
                                             & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Agent": HasAll("dD Extraction - Agent", "Night Vision")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                           | HAS_ANY_WEAPON_TYPE),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Agent Objective 1": Has("Carrington Villa - Agent")
                                                & (Has("Sniper Rifle")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 2": Has("Carrington Villa - Agent")
                                                & (HasAll("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 3": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Agent": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                              & (HasAll("Sniper Rifle", "CMP150")
                                              | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago (Normal)
        "Chicago - Agent Objective 1": HasAll("Chicago - Agent", "Data Uplink")
                                       & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Agent Objective 2": HasAll("Chicago - Agent", "Data Uplink")
                                       & (Has("Falcon 2 (Scope)")
                                       | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                       | HAS_ANY_WEAPON_TYPE),

        "Chicago - Agent Objective 3": HasAll("Chicago - Agent", "Data Uplink")
                                       & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Agent": HasAll("Chicago - Agent", "Data Uplink")
                                     & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                     | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                     | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                     | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Agent Objective 1": HasAll("G5 Building - Agent", "CamSpy")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (Has("Falcon 2 (Silencer)")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 2": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 3": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: G5 Building - Agent": HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Agent Objective 1": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & (Has("Falcon 2")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 2": Has("A51 Infiltration - Agent")
                                                & HAS_A51_INFIL_KEYS
                                                & (Has("Falcon 2")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 3": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & HAS_A51_INFIL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Agent": HasAll("A51 Infiltration - Agent", "Explosives")
                                            & HAS_A51_INFIL_KEYS
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Agent Objective 1": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 2": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_FIRST_KEY
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 3": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_ALL_KEYS
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Agent": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                        & HAS_A51_RESCUE_ALL_KEYS
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Agent Objective 1": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 2": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 3": HasAll("A51 Escape - Agent", "Alien Medpack")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Agent": HasAll("A51 Escape - Agent", "Alien Medpack")
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Agent Objective 1": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Agent Objective 2": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Agent Objective 3": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                        & (HasAll("Dragon", "K7 Avenger")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Agent": HasAll("Air Base - Agent", "Stewardess Disguise")
                                      & (HasAny("Crossbow", "CamSpy")
                                      | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                      & (HasAll("Dragon", "K7 Avenger")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One (Normal)
        "Air Force One - Agent Objective 1": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Agent Objective 2": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Laptop Gun", "K7 Avenger")
                                             | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Agent Objective 3": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Laptop Gun", "Timed Mine")
                                             | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                             | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                             | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Agent": HasAll("Air Force One - Agent", "Suitcase")
                                           & Has("President", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Laptop Gun", "K7 Avenger", "Timed Mine")
                                           | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                           | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                           | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Agent Objective 1": Has("Crash Site - Agent")
                                          & (Has("Falcon 2 (Scope)")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Agent Objective 2": HasAll("Crash Site - Agent", "President Scanner")
                                          & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Agent Objective 3": HasAll("Crash Site - Agent", "President Scanner")
                                          & Has("President", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Agent": HasAll("Crash Site - Agent", "President Scanner")
                                        & Has("President", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Agent Objective 1": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 2": Has("Pelagic II - Agent")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 3": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Agent": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Agent Objective 1": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 2": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 3": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Agent": HasAll("Deep Sea - Agent", "IR Scanner")
                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                      & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                      & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - Carrington Institute Defense
        "CI Defense - Agent Objective 1": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (Has("AR34")
                                          | (all_guns_filter & HAS_ANY_RIFLE)
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                          | HAS_ANY_WEAPON_TYPE),

        "CI Defense - Agent Objective 2": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("AR34", "RC-P120")
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "CI Defense - Agent Objective 3": HasAll("CI Defense - Agent", "Data Uplink")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("AR34", "RC-P120")
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: CI Defense - Agent": HasAll("CI Defense - Agent", "Data Uplink")
                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("AR34", "RC-P120")
                                        | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                        | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                        | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 16 - Attack Ship
        "Attack Ship - Agent Objective 1": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 2": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler", "AR34")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 3": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler", "AR34")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Agent": Has("Attack Ship - Agent")
                                         & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Combat Knife", "Mauler", "AR34")
                                         | (all_guns_filter & HAS_ANY_RIFLE)
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                         | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Agent Objective 1": HAS_SKEDAR_RUINS_AGENT
                                            & HasAll("R-Tracker", "Target Amplifier")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Agent Objective 2": HAS_SKEDAR_RUINS_AGENT
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Agent Objective 3": HAS_SKEDAR_RUINS_AGENT
                                            & Has("IR Scanner")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Agent": HAS_SKEDAR_RUINS_AGENT
                                          & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                          | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                          | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Agent Objective 1": HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (Has("Mauler")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Agent": HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                                  & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                  & (Has("Mauler")
                                                  | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Agent Objective 1": Has("Maian SOS - Agent")
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Falcon 2", "Dragon")
                                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                         | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Agent": Has("Maian SOS - Agent")
                                       & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                       & (HasAll("Falcon 2", "Dragon")
                                       | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                       | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Agent Objective 1": Has("WAR! - Agent")
                                    & (Has("Phoenix")
                                    | (all_guns_filter & HAS_ANY_RIFLE)
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Agent": Has("WAR! - Agent")
                                  & (Has("Phoenix")
                                  | (all_guns_filter & HAS_ANY_RIFLE)
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Agent Objective 1": Has("The Duel - Agent")
                                        & (Has("Falcon 2 (Scope)")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Agent": Has("The Duel - Agent")
                                      & (Has("Falcon 2 (Scope)")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                      | HAS_ANY_WEAPON_TYPE),
    }


    special_agent_rules_normal = {
        # Stage 1 - Defection
        "dD Defection - Special Agent Objective 1": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 2": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 3": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 4": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Special Agent": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                & HAS_DD_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Special Agent Objective 1": HasAll("dD Investigation - Special Agent", "CamSpy")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 2": Has("dD Investigation - Special Agent")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 3": Has("dD Investigation - Special Agent")
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 4": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Special Agent": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Special Agent Objective 1": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & (Has("Falcon 2 (Scope)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 2": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Special Agent Objective 3": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 4": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Special Agent": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Special Agent Objective 1": Has("Carrington Villa - Special Agent")
                                                        & (Has("Sniper Rifle")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 2": Has("Carrington Villa - Special Agent")
                                                        & (Has("Sniper Rifle")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 3": Has("Carrington Villa - Special Agent")
                                                        & (HasAll("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 4": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Special Agent": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Sniper Rifle", "CMP150")
                                                    | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago (Normal)
        "Chicago - Special Agent Objective 1": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 2": Has("Chicago - Special Agent")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 3": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Special Agent Objective 4": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Special Agent": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Special Agent Objective 1": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 2": HasAll("G5 Building - Special Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 3": HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 4": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Special Agent": HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Special Agent Objective 1": HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 2": HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 3": Has("A51 Infiltration - Special Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 4": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Special Agent": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Special Agent Objective 1": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 2": HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 3": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 4": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Special Agent": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Special Agent Objective 1": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 2": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 3": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 4": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Special Agent": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Special Agent Objective 1": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 2": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 3": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 4": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Special Agent": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAll("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One (Normal)
        "Air Force One - Special Agent Objective 1": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Special Agent Objective 2": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Special Agent Objective 3": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Laptop Gun", "K7 Avenger")
                                                    | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Special Agent Objective 4": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Laptop Gun", "Timed Mine")
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Special Agent": HasAll("Air Force One - Special Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Laptop Gun", "K7 Avenger", "Timed Mine")
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Special Agent Objective 1": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 2": Has("Crash Site - Special Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 3": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 4": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Special Agent": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Special Agent Objective 1": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 2": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 3": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 4": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Special Agent": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Special Agent Objective 1": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 2": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 3": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 4": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Special Agent": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - CI Defense
        "CI Defense - Special Agent Objective 1": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 2": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 3": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "CI Defense - Special Agent Objective 4": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "Complete: CI Defense - Special Agent": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Special Agent Objective 1": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 2": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 3": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 4": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Special Agent": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Special Agent Objective 1": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Special Agent Objective 2": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 3": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 4": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Special Agent": HAS_SKEDAR_RUINS_SP_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Special Agent Objective 1": HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Special Agent Objective 2": HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Special Agent": HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (Has("Mauler")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Special Agent Objective 1": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Special Agent Objective 2": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Special Agent": Has("Maian SOS - Special Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Special Agent Objective 1": Has("WAR! - Special Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Special Agent Objective 2": Has("WAR! - Special Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Special Agent": Has("WAR! - Special Agent")
                                        & (Has("Phoenix")
                                        | (all_guns_filter & HAS_ANY_RIFLE)
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Special Agent Objective 1": Has("The Duel - Special Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Special Agent Objective 2": Has("The Duel - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Special Agent": Has("The Duel - Special Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),
    }


    perfect_agent_rules_normal = {
        # Stage 1 - Defection
        "dD Defection - Perfect Agent Objective 1": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 2": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 3": HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 4": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 5": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Perfect Agent": HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink")
                                                & HAS_DD_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Perfect Agent Objective 1": HasAll("dD Investigation - Perfect Agent", "CamSpy")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 2": Has("dD Investigation - Perfect Agent")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 3": Has("dD Investigation - Perfect Agent")
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 4": HasAll("dD Investigation - Perfect Agent", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Investigation - Perfect Agent Objective 5": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: dD Investigation - Perfect Agent": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 3 - Extraction
        "dD Extraction - Perfect Agent Objective 1": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & (Has("Falcon 2 (Scope)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 2": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & ((Has("Falcon 2 (Scope)") & HasAny("CMP150", "Shotgun"))
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 3": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Perfect Agent Objective 4": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 5": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Perfect Agent": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa (Normal)
        "Carrington Villa - Perfect Agent Objective 1": Has("Carrington Villa - Perfect Agent")
                                                        & (Has("Laptop Gun")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 2": Has("Carrington Villa - Perfect Agent")
                                                        & (Has("Laptop Gun")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 3": Has("Carrington Villa - Perfect Agent")
                                                        & (HasAll("Laptop Gun", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 4": Has("Carrington Villa - Perfect Agent"),

        "Carrington Villa - Perfect Agent Objective 5": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Laptop Gun", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Perfect Agent": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Laptop Gun", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago (Normal)
        "Chicago - Perfect Agent Objective 1": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 2": HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 3": Has("Chicago - Perfect Agent")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 4": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 5": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Perfect Agent": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Perfect Agent Objective 1": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 2": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 3": HasAll("G5 Building - Perfect Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 4": HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 5": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Perfect Agent": HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Perfect Agent Objective 1": HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 2": HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 3": Has("A51 Infiltration - Perfect Agent")
                                                        & (HasAll("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 4": Has("A51 Infiltration - Perfect Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 5": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Perfect Agent": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Perfect Agent Objective 1": HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 2": HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 3": HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 4": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 5": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Perfect Agent": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Perfect Agent Objective 1": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 2": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 3": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 4": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 5": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Perfect Agent": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base (Normal)
        "Air Base - Perfect Agent Objective 1": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 2": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 3": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 4": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Air Base - Perfect Agent Objective 5": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Perfect Agent": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAll("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One (Normal)
        "Air Force One - Perfect Agent Objective 1": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Perfect Agent Objective 2": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Perfect Agent Objective 3": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Laptop Gun", "K7 Avenger")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Perfect Agent Objective 4": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Laptop Gun", "Timed Mine")
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Air Force One - Perfect Agent Objective 5": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Laptop Gun", "Timed Mine")
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Perfect Agent": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Laptop Gun", "K7 Avenger", "Timed Mine")
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site (Normal)
        "Crash Site - Perfect Agent Objective 1": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 2": Has("Crash Site - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 3": Has("Crash Site - Perfect Agent")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "Remote Mine")
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 4": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 5": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Perfect Agent": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "Remote Mine")
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Perfect Agent Objective 1": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 2": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 3": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 4": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 5": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Perfect Agent": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Perfect Agent Objective 1": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Perfect Agent Objective 2": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 3": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 4": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 5": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Deep Sea - Perfect Agent": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                            | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 15 - CI Defense (Normal)
        "CI Defense - Perfect Agent Objective 1": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 2": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 3": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))),

        "CI Defense - Perfect Agent Objective 4": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120", "Laser")
                                                | (all_guns_filter & HasAll("RC-P120", "Laser") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "CI Defense - Perfect Agent Objective 5": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120", "Laser")
                                                | (all_guns_filter & HasAll("RC-P120", "Laser") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "Complete: CI Defense - Perfect Agent": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120", "Laser")
                                                | (all_guns_filter & HasAll("RC-P120", "Laser") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Perfect Agent Objective 1": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 2": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 3": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 4": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 5": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Perfect Agent": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Perfect Agent Objective 1": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Perfect Agent Objective 2": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 3": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 4": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 5": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Perfect Agent": HAS_SKEDAR_RUINS_PF_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Perfect Agent Objective 1": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Perfect Agent Objective 2": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Perfect Agent Objective 3": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Perfect Agent": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (Has("Mauler")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Perfect Agent Objective 1": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 2": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon", "DY357-LX")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 3": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Perfect Agent": Has("Maian SOS - Perfect Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon", "DY357-LX")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Perfect Agent Objective 1": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 2": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 3": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Perfect Agent": Has("WAR! - Perfect Agent")
                                        & (Has("Phoenix")
                                        | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Perfect Agent Objective 1": Has("The Duel - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Perfect Agent Objective 2": Has("The Duel - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Perfect Agent Objective 3": Has("The Duel - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Perfect Agent": Has("The Duel - Perfect Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),
    }


    cheat_rules_normal = {
        # Defection
        "Cheat Unlock: Complete dD Defection": (agent_rules_normal["Complete: dD Defection - Agent"])
                                                | (special_agent_rules_normal["Complete: dD Defection - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: dD Defection - Perfect Agent"]),

        # Investigation
        "Cheat Unlock: Complete dD Investigation": (agent_rules_normal["Complete: dD Investigation - Agent"])
                                                | (special_agent_rules_normal["Complete: dD Investigation - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: dD Investigation - Perfect Agent"]),

        # Extraction
        "Cheat Unlock: Complete dD Extraction": (agent_rules_normal["Complete: dD Extraction - Agent"])
                                                | (special_agent_rules_normal["Complete: dD Extraction - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: dD Extraction - Perfect Agent"]),

        # Villa
        "Cheat Unlock: Complete Carrington Villa": (agent_rules_normal["Complete: Carrington Villa - Agent"])
                                                | (special_agent_rules_normal["Complete: Carrington Villa - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Carrington Villa - Perfect Agent"]),
        
        # Chicago
        "Cheat Unlock: Complete Chicago": (agent_rules_normal["Complete: Chicago - Agent"])
                                                | (special_agent_rules_normal["Complete: Chicago - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Chicago - Perfect Agent"]),

        # G5 Building
        "Cheat Unlock: Complete G5 Building": (agent_rules_normal["Complete: G5 Building - Agent"])
                                                | (special_agent_rules_normal["Complete: G5 Building - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: G5 Building - Perfect Agent"]),

        # A51 Infiltration
        "Cheat Unlock: Complete A51 Infiltration": (agent_rules_normal["Complete: A51 Infiltration - Agent"])
                                                | (special_agent_rules_normal["Complete: A51 Infiltration - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: A51 Infiltration - Perfect Agent"]),

        # A51 Rescue
        "Cheat Unlock: Complete A51 Rescue": (agent_rules_normal["Complete: A51 Rescue - Agent"])
                                                | (special_agent_rules_normal["Complete: A51 Rescue - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: A51 Rescue - Perfect Agent"]),

        # A51 Escape
        "Cheat Unlock: Complete A51 Escape": (agent_rules_normal["Complete: A51 Escape - Agent"])
                                                | (special_agent_rules_normal["Complete: A51 Escape - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: A51 Escape - Perfect Agent"]),

        # Air Base
        "Cheat Unlock: Complete Air Base": (agent_rules_normal["Complete: Air Base - Agent"])
                                                | (special_agent_rules_normal["Complete: Air Base - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Air Base - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Air Force One": (agent_rules_normal["Complete: Air Force One - Agent"])
                                                | (special_agent_rules_normal["Complete: Air Force One - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Air Force One - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Crash Site": (agent_rules_normal["Complete: Crash Site - Agent"])
                                                | (special_agent_rules_normal["Complete: Crash Site - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Crash Site - Perfect Agent"]),

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II": (agent_rules_normal["Complete: Pelagic II - Agent"])
                                                | (special_agent_rules_normal["Complete: Pelagic II - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Pelagic II - Perfect Agent"]),

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea": (agent_rules_normal["Complete: Deep Sea - Agent"])
                                                | (special_agent_rules_normal["Complete: Deep Sea - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Deep Sea - Perfect Agent"]),

        # CI Defense
        "Cheat Unlock: Complete CI Defense": (agent_rules_normal["Complete: CI Defense - Agent"])
                                                | (special_agent_rules_normal["Complete: CI Defense - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: CI Defense - Perfect Agent"]),

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship": (agent_rules_normal["Complete: Attack Ship - Agent"])
                                                | (special_agent_rules_normal["Complete: Attack Ship - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Attack Ship - Perfect Agent"]),

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins": (agent_rules_normal["Complete: Skedar Ruins - Agent"])
                                                | (special_agent_rules_normal["Complete: Skedar Ruins - Special Agent"])
                                                | (perfect_agent_rules_normal["Complete: Skedar Ruins - Perfect Agent"]),
    }


    cheat_agent_rules_normal = {
        # Extraction
        "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03": agent_rules_normal["Complete: dD Extraction - Agent"],

        # G5 Building
        "Cheat Unlock: Complete G5 Building (Agent) in under 1:40": agent_rules_normal["Complete: G5 Building - Agent"],

        # Escape
        "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50": agent_rules_normal["Complete: A51 Escape - Agent"],

        # Crash Site
        "Cheat Unlock: Complete Crash Site (Agent) in under 2:50": agent_rules_normal["Complete: Crash Site - Agent"],

        # CI Defense
        "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": agent_rules_normal["Complete: CI Defense - Agent"],
    }


    cheat_sp_agent_rules_normal = {
        # Defection
        "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30": special_agent_rules_normal["Complete: dD Defection - Special Agent"],

        # Villa
        "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30": special_agent_rules_normal["Complete: Carrington Villa - Special Agent"],

        # Infiltration
        "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00": special_agent_rules_normal["Complete: A51 Infiltration - Special Agent"],

        # Air Base
        "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11": special_agent_rules_normal["Complete: Air Base - Special Agent"],

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07": special_agent_rules_normal["Complete: Pelagic II - Special Agent"],

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17": special_agent_rules_normal["Complete: Attack Ship - Special Agent"],
    }


    cheat_pf_agent_rules_normal = {
        # Investigation
        "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30": perfect_agent_rules_normal["Complete: dD Investigation - Perfect Agent"],

        # Chicago
        "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00": perfect_agent_rules_normal["Complete: Chicago - Perfect Agent"] & Has("CamSpy"),

        # Rescue
        "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59": perfect_agent_rules_normal["Complete: A51 Rescue - Perfect Agent"],

        # Air Force One
        "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55": perfect_agent_rules_normal["Complete: Air Force One - Perfect Agent"],

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27": perfect_agent_rules_normal["Complete: Deep Sea - Perfect Agent"],

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31": perfect_agent_rules_normal["Complete: Skedar Ruins - Perfect Agent"],
    }


    agent_alternate_exits_normal = {
        "Complete A51 Escape (Agent): UFO Escape": agent_rules_normal["Complete: A51 Escape - Agent"],
        "Complete A51 Escape (Agent): Alternate Escape": agent_rules_normal["Complete: A51 Escape - Agent"],
        "Complete Air Base (Agent): Shuttle Exit": agent_rules_normal["Complete: Air Base - Agent"],
        "Complete Air Base (Agent): Ladder Exit": agent_rules_normal["Complete: Air Base - Agent"],
    }


    special_agent_alternate_exits_normal = {
        "Complete A51 Escape (Special Agent): UFO Escape": special_agent_rules_normal["Complete: A51 Escape - Special Agent"],
        "Complete A51 Escape (Special Agent): Alternate Escape": special_agent_rules_normal["Complete: A51 Escape - Special Agent"],
        "Complete Air Base (Special Agent): Shuttle Exit": special_agent_rules_normal["Complete: Air Base - Special Agent"],
        "Complete Air Base (Special Agent): Ladder Exit": special_agent_rules_normal["Complete: Air Base - Special Agent"],
    }


    perfect_agent_alternate_exits_normal = {
        "Complete A51 Escape (Perfect Agent): UFO Escape": perfect_agent_rules_normal["Complete: A51 Escape - Perfect Agent"],
        "Complete A51 Escape (Perfect Agent): Alternate Escape": perfect_agent_rules_normal["Complete: A51 Escape - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Shuttle Exit": perfect_agent_rules_normal["Complete: Air Base - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Ladder Exit": perfect_agent_rules_normal["Complete: Air Base - Perfect Agent"],
    }


    if world.options.agent:
        add_rule(world, agent_rules_normal)

        if world.options.alternate_exits:
            add_rule(world, agent_alternate_exits_normal)

    if world.options.special_agent:
        add_rule(world, special_agent_rules_normal)

        if world.options.alternate_exits:
            add_rule(world, special_agent_alternate_exits_normal)

    if world.options.perfect_agent:
        add_rule(world, perfect_agent_rules_normal)

        if world.options.alternate_exits:
            add_rule(world, perfect_agent_alternate_exits_normal)

    if world.options.completion_cheats:
        if world.options.agent or world.options.special_agent or world.options.perfect_agent:
            add_rule(world, cheat_rules_normal)

    if world.options.timed_cheats:
        if world.options.agent:
            add_rule(world, cheat_agent_rules_normal)
        if world.options.special_agent:
            add_rule(world, cheat_sp_agent_rules_normal)
        if world.options.perfect_agent:
            add_rule(world, cheat_pf_agent_rules_normal)

    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent:
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 1"), agent_rules_normal["Skedar Ruins - Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 2"), agent_rules_normal["Skedar Ruins - Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 3"), agent_rules_normal["Skedar Ruins - Agent Objective 3"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Agent"), agent_rules_normal["Complete: Skedar Ruins - Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 1"), special_agent_rules_normal["Skedar Ruins - Special Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 2"), special_agent_rules_normal["Skedar Ruins - Special Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 3"), special_agent_rules_normal["Skedar Ruins - Special Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 4"), special_agent_rules_normal["Skedar Ruins - Special Agent Objective 4"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Special Agent"), special_agent_rules_normal["Complete: Skedar Ruins - Special Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 1"), perfect_agent_rules_normal["Skedar Ruins - Perfect Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 2"), perfect_agent_rules_normal["Skedar Ruins - Perfect Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 3"), perfect_agent_rules_normal["Skedar Ruins - Perfect Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 4"), perfect_agent_rules_normal["Skedar Ruins - Perfect Agent Objective 4"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 5"), perfect_agent_rules_normal["Skedar Ruins - Perfect Agent Objective 5"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Perfect Agent"), perfect_agent_rules_normal["Complete: Skedar Ruins - Perfect Agent"])

        if world.options.completion_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins"), cheat_rules_normal["Cheat Unlock: Complete Skedar Ruins"])
        if world.options.timed_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"), cheat_pf_agent_rules_normal["Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"])


def set_all_veteran_location_rules(world: PerfectDarkWorld) -> None:
    agent_rules_veteran = {
        # Stage 1 - Defection
        "dD Defection - Agent Objective 1": Has("dD Defection - Agent")
                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Agent": Has("dD Defection - Agent")
                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                          | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Agent Objective 1": HasAll("dD Investigation - Agent", "CamSpy")
                                                & (Has("Falcon 2")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Agent Objective 2": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Agent": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & (HasAll("Falcon 2", "CMP150")
                                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Agent Objective 1": HasAll("dD Extraction - Agent", "Night Vision")
                                             & (Has("Falcon 2 (Scope)")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 2": HasAll("dD Extraction - Agent", "Night Vision")
                                             & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 3": HasAll("dD Extraction - Agent", "Night Vision")
                                             & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Agent": HasAll("dD Extraction - Agent", "Night Vision")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                           | HAS_ANY_WEAPON_TYPE),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Agent Objective 1": Has("Carrington Villa - Agent")
                                                & (Has("Sniper Rifle")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 2": Has("Carrington Villa - Agent")
                                                & (HasAll("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 3": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Agent": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                              & (HasAll("Sniper Rifle", "CMP150")
                                              | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago (Veteran)
        "Chicago - Agent Objective 1": HasAll("Chicago - Agent", "Data Uplink")
                                       & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Agent Objective 2": Has("Chicago - Agent")
                                       & HasAny("Data Uplink", "CamSpy")
                                       & (Has("Falcon 2 (Scope)")
                                       | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                       | HAS_ANY_WEAPON_TYPE),

        "Chicago - Agent Objective 3": HasAll("Chicago - Agent", "Data Uplink")
                                       & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Agent": HasAll("Chicago - Agent", "Data Uplink")
                                     & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                     | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                     | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                     | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Agent Objective 1": HasAll("G5 Building - Agent", "CamSpy")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (Has("Falcon 2 (Silencer)")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 2": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 3": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: G5 Building - Agent": HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Agent Objective 1": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & (Has("Falcon 2")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 2": Has("A51 Infiltration - Agent")
                                                & HAS_A51_INFIL_KEYS
                                                & (Has("Falcon 2")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 3": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & HAS_A51_INFIL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Agent": HasAll("A51 Infiltration - Agent", "Explosives")
                                            & HAS_A51_INFIL_KEYS
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Agent Objective 1": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 2": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_FIRST_KEY
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 3": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_ALL_KEYS
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Agent": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                        & HAS_A51_RESCUE_ALL_KEYS
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Agent Objective 1": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 2": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 3": HasAll("A51 Escape - Agent", "Alien Medpack")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Agent": HasAll("A51 Escape - Agent", "Alien Medpack")
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Agent Objective 1": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Agent Objective 2": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Agent Objective 3": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                        & (HasAll("Dragon", "K7 Avenger")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Agent": HasAll("Air Base - Agent", "Stewardess Disguise")
                                      & (HasAny("Crossbow", "CamSpy")
                                      | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                      & (HasAll("Dragon", "K7 Avenger")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One (Veteran)
        "Air Force One - Agent Objective 1": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Agent Objective 2": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                                             | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Agent Objective 3": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                             & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                             | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                             | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                             | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Agent": HasAll("Air Force One - Agent", "Suitcase")
                                           & Has("President", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & HasAll("K7 Avenger", "Timed Mine"))
                                           | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                           | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                           | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Agent Objective 1": Has("Crash Site - Agent")
                                          & (Has("Falcon 2 (Scope)")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Agent Objective 2": HasAll("Crash Site - Agent", "President Scanner")
                                          & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Agent Objective 3": HasAll("Crash Site - Agent", "President Scanner")
                                          & Has("President", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Agent": HasAll("Crash Site - Agent", "President Scanner")
                                        & Has("President", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Agent Objective 1": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 2": Has("Pelagic II - Agent")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 3": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Agent": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Agent Objective 1": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 2": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 3": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Agent": HasAll("Deep Sea - Agent", "IR Scanner")
                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                      & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                      & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - Carrington Institute Defense
        "CI Defense - Agent Objective 1": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (Has("AR34")
                                          | (all_guns_filter & HAS_ANY_RIFLE)
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                          | HAS_ANY_WEAPON_TYPE),

        "CI Defense - Agent Objective 2": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("AR34", "RC-P120")
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "CI Defense - Agent Objective 3": HasAll("CI Defense - Agent", "Data Uplink")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("AR34", "RC-P120")
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: CI Defense - Agent": HasAll("CI Defense - Agent", "Data Uplink")
                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("AR34", "RC-P120")
                                        | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                        | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                        | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 16 - Attack Ship
        "Attack Ship - Agent Objective 1": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 2": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler", "AR34")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 3": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler", "AR34")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Agent": Has("Attack Ship - Agent")
                                         & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Combat Knife", "Mauler", "AR34")
                                         | (all_guns_filter & HAS_ANY_RIFLE)
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                         | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Agent Objective 1": HAS_SKEDAR_RUINS_AGENT
                                            & HasAll("R-Tracker", "Target Amplifier")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Agent Objective 2": HAS_SKEDAR_RUINS_AGENT
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Agent Objective 3": HAS_SKEDAR_RUINS_AGENT
                                            & Has("IR Scanner")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Agent": HAS_SKEDAR_RUINS_AGENT
                                          & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                          | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                          | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Agent Objective 1": HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (Has("Mauler")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Agent": HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                                  & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                  & (Has("Mauler")
                                                  | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Agent Objective 1": Has("Maian SOS - Agent")
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Falcon 2", "Dragon")
                                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                         | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Agent": Has("Maian SOS - Agent")
                                       & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                       & (HasAll("Falcon 2", "Dragon")
                                       | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                       | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Agent Objective 1": Has("WAR! - Agent")
                                    & (Has("Phoenix")
                                    | (all_guns_filter & HAS_ANY_RIFLE)
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Agent": Has("WAR! - Agent")
                                  & (Has("Phoenix")
                                  | (all_guns_filter & HAS_ANY_RIFLE)
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Agent Objective 1": Has("The Duel - Agent")
                                        & (Has("Falcon 2 (Scope)")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Agent": Has("The Duel - Agent")
                                      & (Has("Falcon 2 (Scope)")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                      | HAS_ANY_WEAPON_TYPE),
    }


    special_agent_rules_veteran = {
        # Stage 1 - Defection
        "dD Defection - Special Agent Objective 1": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 2": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 3": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 4": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Special Agent": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                & HAS_DD_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Special Agent Objective 1": HasAll("dD Investigation - Special Agent", "CamSpy")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 2": Has("dD Investigation - Special Agent")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 3": Has("dD Investigation - Special Agent")
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 4": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Special Agent": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Special Agent Objective 1": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & (Has("Falcon 2 (Scope)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 2": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Special Agent Objective 3": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 4": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Special Agent": HasAll("dD Extraction - Special Agent", "Night Vision")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Special Agent Objective 1": Has("Carrington Villa - Special Agent")
                                                        & (Has("Sniper Rifle")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 2": Has("Carrington Villa - Special Agent")
                                                        & (Has("Sniper Rifle")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 3": Has("Carrington Villa - Special Agent")
                                                        & (HasAll("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 4": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Special Agent": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Sniper Rifle", "CMP150")
                                                    | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago (Veteran)
        "Chicago - Special Agent Objective 1": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 2": Has("Chicago - Special Agent")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 3": Has("Chicago - Special Agent")
                                            & HasAny("Data Uplink", "CamSpy")
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Special Agent Objective 4": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Special Agent": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Special Agent Objective 1": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 2": HasAll("G5 Building - Special Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 3": HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 4": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Special Agent": HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Special Agent Objective 1": HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 2": HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 3": Has("A51 Infiltration - Special Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 4": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Special Agent": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Special Agent Objective 1": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 2": HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 3": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 4": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Special Agent": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Special Agent Objective 1": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 2": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 3": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 4": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Special Agent": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Special Agent Objective 1": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 2": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 3": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 4": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Special Agent": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAll("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One (Veteran)
        "Air Force One - Special Agent Objective 1": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Special Agent Objective 2": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Special Agent Objective 3": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                                                    | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Special Agent Objective 4": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Special Agent": HasAll("Air Force One - Special Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & HasAll("K7 Avenger", "Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Special Agent Objective 1": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 2": Has("Crash Site - Special Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 3": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 4": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Special Agent": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Special Agent Objective 1": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 2": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 3": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 4": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Special Agent": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Special Agent Objective 1": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 2": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 3": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 4": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Special Agent": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - CI Defense
        "CI Defense - Special Agent Objective 1": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 2": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 3": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "CI Defense - Special Agent Objective 4": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "Complete: CI Defense - Special Agent": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Special Agent Objective 1": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 2": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 3": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 4": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Special Agent": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Special Agent Objective 1": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Special Agent Objective 2": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 3": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 4": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Special Agent": HAS_SKEDAR_RUINS_SP_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Special Agent Objective 1": HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Special Agent Objective 2": HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Special Agent": HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (Has("Mauler")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Special Agent Objective 1": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Special Agent Objective 2": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Special Agent": Has("Maian SOS - Special Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Special Agent Objective 1": Has("WAR! - Special Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Special Agent Objective 2": Has("WAR! - Special Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Special Agent": Has("WAR! - Special Agent")
                                        & (Has("Phoenix")
                                        | (all_guns_filter & HAS_ANY_RIFLE)
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Special Agent Objective 1": Has("The Duel - Special Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Special Agent Objective 2": Has("The Duel - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Special Agent": Has("The Duel - Special Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),
    }


    perfect_agent_rules_veteran = {
        # Stage 1 - Defection
        "dD Defection - Perfect Agent Objective 1": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 2": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (Has("Falcon 2 (Silencer)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 3": HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 4": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 5": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Perfect Agent": HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink")
                                                & HAS_DD_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Perfect Agent Objective 1": HasAll("dD Investigation - Perfect Agent", "CamSpy")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 2": Has("dD Investigation - Perfect Agent")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 3": Has("dD Investigation - Perfect Agent")
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 4": HasAll("dD Investigation - Perfect Agent", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Investigation - Perfect Agent Objective 5": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: dD Investigation - Perfect Agent": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 3 - Extraction
        "dD Extraction - Perfect Agent Objective 1": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & (Has("Falcon 2 (Scope)")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 2": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & ((Has("Falcon 2 (Scope)") & HasAny("CMP150", "Shotgun"))
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 3": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Perfect Agent Objective 4": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 5": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Perfect Agent": HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa (Veteran)
        "Carrington Villa - Perfect Agent Objective 1": Has("Carrington Villa - Perfect Agent")
                                                        & (Has("Laptop Gun")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 2": Has("Carrington Villa - Perfect Agent")
                                                        & (Has("Laptop Gun")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 3": Has("Carrington Villa - Perfect Agent")
                                                        & ((Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 4": Has("Carrington Villa - Perfect Agent"),

        "Carrington Villa - Perfect Agent Objective 5": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & ((Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Perfect Agent": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & ((Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago (Veteran)
        "Chicago - Perfect Agent Objective 1": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 2": HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 3": Has("Chicago - Perfect Agent")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 4": Has("Chicago - Perfect Agent")
                                            & HasAny("Data Uplink", "CamSpy")
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 5": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Perfect Agent": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Perfect Agent Objective 1": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 2": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 3": HasAll("G5 Building - Perfect Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Silencer)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 4": HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 5": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Perfect Agent": HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Perfect Agent Objective 1": HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 2": HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 3": Has("A51 Infiltration - Perfect Agent")
                                                        & (HasAll("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 4": Has("A51 Infiltration - Perfect Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (Has("Falcon 2")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 5": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Perfect Agent": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Perfect Agent Objective 1": HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 2": HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 3": HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 4": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 5": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Perfect Agent": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Perfect Agent Objective 1": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 2": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 3": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 4": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 5": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Perfect Agent": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base (Veteran)
        "Air Base - Perfect Agent Objective 1": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 2": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 3": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 4": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & ((Has("Dragon") & HasAny("K7 Avenger", "Proximity Mine"))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Air Base - Perfect Agent Objective 5": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Perfect Agent": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAll("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One (Veteran)
        "Air Force One - Perfect Agent Objective 1": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Perfect Agent Objective 2": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Perfect Agent Objective 3": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Perfect Agent Objective 4": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Air Force One - Perfect Agent Objective 5": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Perfect Agent": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & HasAll("K7 Avenger", "Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site (Veteran)
        "Crash Site - Perfect Agent Objective 1": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 2": Has("Crash Site - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 3": Has("Crash Site - Perfect Agent")
                                                & ((HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle") & (Has("Remote Mine") | HasAll("DY357-LX", "President Scanner")))
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 4": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 5": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Perfect Agent": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle") & HasAny("Remote Mine", "DY357-LX"))
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Perfect Agent Objective 1": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 2": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 3": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 4": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 5": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Perfect Agent": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Perfect Agent Objective 1": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Perfect Agent Objective 2": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 3": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 4": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 5": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Deep Sea - Perfect Agent": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                            | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 15 - CI Defense (Veteran)
        "CI Defense - Perfect Agent Objective 1": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 2": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 3": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))),

        "CI Defense - Perfect Agent Objective 4": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((Has("AR34") & (HasAll("RC-P120", "Laser") | Has("Devastator")))
                                                | (all_guns_filter & HasAll("RC-P120", "Laser") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "CI Defense - Perfect Agent Objective 5": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("AR34", "RC-P120") & HasAny("Laser", "Devastator"))
                                                | (all_guns_filter & HasAll("RC-P120", "Laser") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "Complete: CI Defense - Perfect Agent": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("AR34", "RC-P120") & HasAny("Laser", "Devastator"))
                                                | (all_guns_filter & HasAll("RC-P120", "Laser") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Perfect Agent Objective 1": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 2": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 3": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 4": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 5": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Perfect Agent": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Perfect Agent Objective 1": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Perfect Agent Objective 2": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 3": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 4": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 5": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Perfect Agent": HAS_SKEDAR_RUINS_PF_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Perfect Agent Objective 1": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Perfect Agent Objective 2": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Perfect Agent Objective 3": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (Has("Mauler")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Perfect Agent": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (Has("Mauler")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Perfect Agent Objective 1": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 2": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon", "DY357-LX")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 3": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Perfect Agent": Has("Maian SOS - Perfect Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon", "DY357-LX")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Perfect Agent Objective 1": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 2": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 3": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Perfect Agent": Has("WAR! - Perfect Agent")
                                        & (Has("Phoenix")
                                        | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Perfect Agent Objective 1": Has("The Duel - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Perfect Agent Objective 2": Has("The Duel - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Perfect Agent Objective 3": Has("The Duel - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Perfect Agent": Has("The Duel - Perfect Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),
    }


    cheat_rules_veteran = {
        # Defection
        "Cheat Unlock: Complete dD Defection": (agent_rules_veteran["Complete: dD Defection - Agent"])
                                                | (special_agent_rules_veteran["Complete: dD Defection - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: dD Defection - Perfect Agent"]),

        # Investigation
        "Cheat Unlock: Complete dD Investigation": (agent_rules_veteran["Complete: dD Investigation - Agent"])
                                                | (special_agent_rules_veteran["Complete: dD Investigation - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: dD Investigation - Perfect Agent"]),

        # Extraction
        "Cheat Unlock: Complete dD Extraction": (agent_rules_veteran["Complete: dD Extraction - Agent"])
                                                | (special_agent_rules_veteran["Complete: dD Extraction - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: dD Extraction - Perfect Agent"]),

        # Villa
        "Cheat Unlock: Complete Carrington Villa": (agent_rules_veteran["Complete: Carrington Villa - Agent"])
                                                | (special_agent_rules_veteran["Complete: Carrington Villa - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Carrington Villa - Perfect Agent"]),
        
        # Chicago
        "Cheat Unlock: Complete Chicago": (agent_rules_veteran["Complete: Chicago - Agent"])
                                                | (special_agent_rules_veteran["Complete: Chicago - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Chicago - Perfect Agent"]),

        # G5 Building
        "Cheat Unlock: Complete G5 Building": (agent_rules_veteran["Complete: G5 Building - Agent"])
                                                | (special_agent_rules_veteran["Complete: G5 Building - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: G5 Building - Perfect Agent"]),

        # A51 Infiltration
        "Cheat Unlock: Complete A51 Infiltration": (agent_rules_veteran["Complete: A51 Infiltration - Agent"])
                                                | (special_agent_rules_veteran["Complete: A51 Infiltration - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: A51 Infiltration - Perfect Agent"]),

        # A51 Rescue
        "Cheat Unlock: Complete A51 Rescue": (agent_rules_veteran["Complete: A51 Rescue - Agent"])
                                                | (special_agent_rules_veteran["Complete: A51 Rescue - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: A51 Rescue - Perfect Agent"]),

        # A51 Escape
        "Cheat Unlock: Complete A51 Escape": (agent_rules_veteran["Complete: A51 Escape - Agent"])
                                                | (special_agent_rules_veteran["Complete: A51 Escape - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: A51 Escape - Perfect Agent"]),

        # Air Base
        "Cheat Unlock: Complete Air Base": (agent_rules_veteran["Complete: Air Base - Agent"])
                                                | (special_agent_rules_veteran["Complete: Air Base - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Air Base - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Air Force One": (agent_rules_veteran["Complete: Air Force One - Agent"])
                                                | (special_agent_rules_veteran["Complete: Air Force One - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Air Force One - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Crash Site": (agent_rules_veteran["Complete: Crash Site - Agent"])
                                                | (special_agent_rules_veteran["Complete: Crash Site - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Crash Site - Perfect Agent"]),

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II": (agent_rules_veteran["Complete: Pelagic II - Agent"])
                                                | (special_agent_rules_veteran["Complete: Pelagic II - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Pelagic II - Perfect Agent"]),

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea": (agent_rules_veteran["Complete: Deep Sea - Agent"])
                                                | (special_agent_rules_veteran["Complete: Deep Sea - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Deep Sea - Perfect Agent"]),

        # CI Defense
        "Cheat Unlock: Complete CI Defense": (agent_rules_veteran["Complete: CI Defense - Agent"])
                                                | (special_agent_rules_veteran["Complete: CI Defense - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: CI Defense - Perfect Agent"]),

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship": (agent_rules_veteran["Complete: Attack Ship - Agent"])
                                                | (special_agent_rules_veteran["Complete: Attack Ship - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Attack Ship - Perfect Agent"]),

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins": (agent_rules_veteran["Complete: Skedar Ruins - Agent"])
                                                | (special_agent_rules_veteran["Complete: Skedar Ruins - Special Agent"])
                                                | (perfect_agent_rules_veteran["Complete: Skedar Ruins - Perfect Agent"]),
    }


    cheat_agent_rules_veteran = {
        # Extraction
        "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03": agent_rules_veteran["Complete: dD Extraction - Agent"],

        # G5 Building
        "Cheat Unlock: Complete G5 Building (Agent) in under 1:40": agent_rules_veteran["Complete: G5 Building - Agent"],

        # Escape
        "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50": agent_rules_veteran["Complete: A51 Escape - Agent"],

        # Crash Site
        "Cheat Unlock: Complete Crash Site (Agent) in under 2:50": agent_rules_veteran["Complete: Crash Site - Agent"],

        # CI Defense
        "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": agent_rules_veteran["Complete: CI Defense - Agent"],
    }


    cheat_sp_agent_rules_veteran = {
        # Defection
        "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30": special_agent_rules_veteran["Complete: dD Defection - Special Agent"],

        # Villa
        "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30": special_agent_rules_veteran["Complete: Carrington Villa - Special Agent"],

        # Infiltration
        "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00": special_agent_rules_veteran["Complete: A51 Infiltration - Special Agent"],

        # Air Base
        "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11": special_agent_rules_veteran["Complete: Air Base - Special Agent"],

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07": special_agent_rules_veteran["Complete: Pelagic II - Special Agent"],

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17": special_agent_rules_veteran["Complete: Attack Ship - Special Agent"],
    }


    cheat_pf_agent_rules_veteran = {
        # Investigation
        "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30": perfect_agent_rules_veteran["Complete: dD Investigation - Perfect Agent"],

        # Chicago
        "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00": perfect_agent_rules_veteran["Complete: Chicago - Perfect Agent"] & Has("CamSpy"),

        # Rescue
        "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59": perfect_agent_rules_veteran["Complete: A51 Rescue - Perfect Agent"],

        # Air Force One
        "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55": perfect_agent_rules_veteran["Complete: Air Force One - Perfect Agent"],

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27": perfect_agent_rules_veteran["Complete: Deep Sea - Perfect Agent"],

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31": perfect_agent_rules_veteran["Complete: Skedar Ruins - Perfect Agent"],
    }


    agent_alternate_exits_veteran = {
        "Complete A51 Escape (Agent): UFO Escape": agent_rules_veteran["Complete: A51 Escape - Agent"],
        "Complete A51 Escape (Agent): Alternate Escape": agent_rules_veteran["Complete: A51 Escape - Agent"],
        "Complete Air Base (Agent): Shuttle Exit": agent_rules_veteran["Complete: Air Base - Agent"],
        "Complete Air Base (Agent): Ladder Exit": agent_rules_veteran["Complete: Air Base - Agent"],
    }


    special_agent_alternate_exits_veteran = {
        "Complete A51 Escape (Special Agent): UFO Escape": special_agent_rules_veteran["Complete: A51 Escape - Special Agent"],
        "Complete A51 Escape (Special Agent): Alternate Escape": special_agent_rules_veteran["Complete: A51 Escape - Special Agent"],
        "Complete Air Base (Special Agent): Shuttle Exit": special_agent_rules_veteran["Complete: Air Base - Special Agent"],
        "Complete Air Base (Special Agent): Ladder Exit": special_agent_rules_veteran["Complete: Air Base - Special Agent"],
    }


    perfect_agent_alternate_exits_veteran = {
        "Complete A51 Escape (Perfect Agent): UFO Escape": perfect_agent_rules_veteran["Complete: A51 Escape - Perfect Agent"],
        "Complete A51 Escape (Perfect Agent): Alternate Escape": perfect_agent_rules_veteran["Complete: A51 Escape - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Shuttle Exit": perfect_agent_rules_veteran["Complete: Air Base - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Ladder Exit": perfect_agent_rules_veteran["Complete: Air Base - Perfect Agent"],
    }


    if world.options.agent:
        add_rule(world, agent_rules_veteran)

        if world.options.alternate_exits:
            add_rule(world, agent_alternate_exits_veteran)

    if world.options.special_agent:
        add_rule(world, special_agent_rules_veteran)

        if world.options.alternate_exits:
            add_rule(world, special_agent_alternate_exits_veteran)

    if world.options.perfect_agent:
        add_rule(world, perfect_agent_rules_veteran)

        if world.options.alternate_exits:
            add_rule(world, perfect_agent_alternate_exits_veteran)

    if world.options.completion_cheats:
        if world.options.agent or world.options.special_agent or world.options.perfect_agent:
            add_rule(world, cheat_rules_veteran)

    if world.options.timed_cheats:
        if world.options.agent:
            add_rule(world, cheat_agent_rules_veteran)
        if world.options.special_agent:
            add_rule(world, cheat_sp_agent_rules_veteran)
        if world.options.perfect_agent:
            add_rule(world, cheat_pf_agent_rules_veteran)

    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent:
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 1"), agent_rules_veteran["Skedar Ruins - Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 2"), agent_rules_veteran["Skedar Ruins - Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 3"), agent_rules_veteran["Skedar Ruins - Agent Objective 3"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Agent"), agent_rules_veteran["Complete: Skedar Ruins - Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 1"), special_agent_rules_veteran["Skedar Ruins - Special Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 2"), special_agent_rules_veteran["Skedar Ruins - Special Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 3"), special_agent_rules_veteran["Skedar Ruins - Special Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 4"), special_agent_rules_veteran["Skedar Ruins - Special Agent Objective 4"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Special Agent"), special_agent_rules_veteran["Complete: Skedar Ruins - Special Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 1"), perfect_agent_rules_veteran["Skedar Ruins - Perfect Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 2"), perfect_agent_rules_veteran["Skedar Ruins - Perfect Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 3"), perfect_agent_rules_veteran["Skedar Ruins - Perfect Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 4"), perfect_agent_rules_veteran["Skedar Ruins - Perfect Agent Objective 4"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 5"), perfect_agent_rules_veteran["Skedar Ruins - Perfect Agent Objective 5"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Perfect Agent"), perfect_agent_rules_veteran["Complete: Skedar Ruins - Perfect Agent"])

        if world.options.completion_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins"), cheat_rules_veteran["Cheat Unlock: Complete Skedar Ruins"])
        if world.options.timed_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"), cheat_pf_agent_rules_veteran["Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"])


def set_all_hard_location_rules(world: PerfectDarkWorld) -> None:
    agent_rules_hard = {
        # Stage 1 - Defection
        "dD Defection - Agent Objective 1": Has("dD Defection - Agent")
                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                            & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Agent": Has("dD Defection - Agent")
                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                          | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Agent Objective 1": HasAll("dD Investigation - Agent", "CamSpy")
                                                & (HasAny("Falcon 2", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Agent Objective 2": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Agent": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & (HasAll("Falcon 2", "CMP150")
                                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Agent Objective 1": Has("dD Extraction - Agent")
                                             & (HasAny("Falcon 2 (Scope)", "CMP150")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 2": Has("dD Extraction - Agent")
                                             & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 3": Has("dD Extraction - Agent")
                                             & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                             & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Agent": Has("dD Extraction - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                           | HAS_ANY_WEAPON_TYPE),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Agent Objective 1": Has("Carrington Villa - Agent")
                                                & (Has("Sniper Rifle")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 2": Has("Carrington Villa - Agent")
                                                & (HasAll("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 3": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Agent": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                              & (HasAll("Sniper Rifle", "CMP150")
                                              | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago  
        "Chicago - Agent Objective 1": HasAll("Chicago - Agent", "Data Uplink")
                                       & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150"))
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Agent Objective 2": Has("Chicago - Agent")
                                       & HasAny("Data Uplink", "CamSpy")
                                       & (HasAny("Falcon 2 (Scope)", "CMP150")
                                       | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                       | HAS_ANY_WEAPON_TYPE),

        "Chicago - Agent Objective 3": HasAll("Chicago - Agent", "Data Uplink")
                                       & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Agent": HasAll("Chicago - Agent", "Data Uplink")
                                     & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                     | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                     | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                     | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Agent Objective 1": HasAll("G5 Building - Agent", "CamSpy")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 2": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 3": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: G5 Building - Agent": HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Agent Objective 1": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & (HasAny("Falcon 2", "MagSec 4")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 2": Has("A51 Infiltration - Agent")
                                                & HAS_A51_INFIL_KEYS
                                                & (HasAny("Falcon 2", "MagSec 4")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 3": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & HAS_A51_INFIL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Agent": HasAll("A51 Infiltration - Agent", "Explosives")
                                            & HAS_A51_INFIL_KEYS
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Agent Objective 1": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 2": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_FIRST_KEY
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 3": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_ALL_KEYS
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Agent": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                        & HAS_A51_RESCUE_ALL_KEYS
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Agent Objective 1": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 2": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 3": HasAll("A51 Escape - Agent", "Alien Medpack")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Agent": HasAll("A51 Escape - Agent", "Alien Medpack")
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Agent Objective 1": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Agent Objective 2": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Agent Objective 3": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                        & (HasAll("Dragon", "K7 Avenger")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Agent": HasAll("Air Base - Agent", "Stewardess Disguise")
                                      & (HasAny("Crossbow", "CamSpy")
                                      | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                      & (HasAll("Dragon", "K7 Avenger")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One  
        "Air Force One - Agent Objective 1": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Agent Objective 2": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                                             | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Agent Objective 3": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                             & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                             | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                             | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                             | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Agent": HasAll("Air Force One - Agent", "Suitcase")
                                           & Has("President", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & HasAll("K7 Avenger", "Timed Mine"))
                                           | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                           | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                           | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Agent Objective 1": Has("Crash Site - Agent"),

        "Crash Site - Agent Objective 2": Has("Crash Site - Agent")
                                          & (HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Agent Objective 3": Has("Crash Site - Agent")
                                          & Has("President", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Agent": Has("Crash Site - Agent")
                                        & Has("President", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Agent Objective 1": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 2": Has("Pelagic II - Agent")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 3": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Agent": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Agent Objective 1": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 2": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 3": HasAll("Deep Sea - Agent", "IR Scanner")
                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Agent": HasAll("Deep Sea - Agent", "IR Scanner")
                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                      & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                      & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - Carrington Institute Defense
        "CI Defense - Agent Objective 1": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (Has("AR34")
                                          | (all_guns_filter & HAS_ANY_RIFLE)
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                          | HAS_ANY_WEAPON_TYPE),

        "CI Defense - Agent Objective 2": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("AR34", "RC-P120")
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "CI Defense - Agent Objective 3": HasAll("CI Defense - Agent", "Data Uplink")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("AR34", "RC-P120")
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: CI Defense - Agent": HasAll("CI Defense - Agent", "Data Uplink")
                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                        & (HasAll("AR34", "RC-P120")
                                        | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                        | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                        | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 16 - Attack Ship
        "Attack Ship - Agent Objective 1": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 2": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler", "AR34")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 3": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (HasAll("Combat Knife", "Mauler", "AR34")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Agent": Has("Attack Ship - Agent")
                                         & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Combat Knife", "Mauler", "AR34")
                                         | (all_guns_filter & HAS_ANY_RIFLE)
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                         | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Agent Objective 1": HAS_SKEDAR_RUINS_AGENT
                                            & HasAll("R-Tracker", "Target Amplifier")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Agent Objective 2": HAS_SKEDAR_RUINS_AGENT
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Agent Objective 3": HAS_SKEDAR_RUINS_AGENT
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Agent": HAS_SKEDAR_RUINS_AGENT
                                          & HasAll("R-Tracker", "Target Amplifier")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                          | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                          | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Agent Objective 1": HasAll("Mr. Blonde's Revenge - Agent")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAny("Mauler", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Agent": HasAll("Mr. Blonde's Revenge - Agent")
                                                  & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                  & (HasAny("Mauler", "CMP150")
                                                  | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Agent Objective 1": Has("Maian SOS - Agent")
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Falcon 2", "Dragon")
                                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                         | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Agent": Has("Maian SOS - Agent")
                                       & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                       & (HasAll("Falcon 2", "Dragon")
                                       | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                       | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Agent Objective 1": Has("WAR! - Agent")
                                    & (Has("Phoenix")
                                    | (all_guns_filter & HAS_ANY_RIFLE)
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Agent": Has("WAR! - Agent")
                                  & (Has("Phoenix")
                                  | (all_guns_filter & HAS_ANY_RIFLE)
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Agent Objective 1": Has("The Duel - Agent")
                                        & (Has("Falcon 2 (Scope)")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Agent": Has("The Duel - Agent")
                                      & (Has("Falcon 2 (Scope)")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                      | HAS_ANY_WEAPON_TYPE),
    }


    special_agent_rules_hard = {
        # Stage 1 - Defection
        "dD Defection - Special Agent Objective 1": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 2": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 3": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 4": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Special Agent": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                & HAS_DD_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Special Agent Objective 1": HasAll("dD Investigation - Special Agent", "CamSpy")
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 2": Has("dD Investigation - Special Agent")
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 3": Has("dD Investigation - Special Agent")
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 4": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Special Agent": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Special Agent Objective 1": Has("dD Extraction - Special Agent")
                                                    & (HasAny("Falcon 2 (Scope)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 2": Has("dD Extraction - Special Agent")
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Special Agent Objective 3": Has("dD Extraction - Special Agent")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 4": Has("dD Extraction - Special Agent")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Special Agent": Has("dD Extraction - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Special Agent Objective 1": Has("Carrington Villa - Special Agent")
                                                        & (Has("Sniper Rifle")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 2": Has("Carrington Villa - Special Agent")
                                                        & (HasAny("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)"))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 3": Has("Carrington Villa - Special Agent")
                                                        & (HasAll("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 4": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Special Agent": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Sniper Rifle", "CMP150")
                                                    | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago  
        "Chicago - Special Agent Objective 1": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 2": Has("Chicago - Special Agent")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 3": Has("Chicago - Special Agent")
                                            & HasAny("Data Uplink", "CamSpy")
                                            & (HasAny("Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Special Agent Objective 4": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Special Agent": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Special Agent Objective 1": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 2": HasAll("G5 Building - Special Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 3": HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 4": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Special Agent": HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Special Agent Objective 1": HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 2": HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 3": Has("A51 Infiltration - Special Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 4": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Special Agent": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Special Agent Objective 1": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 2": HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 3": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 4": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Special Agent": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Special Agent Objective 1": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 2": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 3": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 4": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Special Agent": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Special Agent Objective 1": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 2": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 3": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 4": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Special Agent": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAll("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One  
        "Air Force One - Special Agent Objective 1": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Special Agent Objective 2": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Special Agent Objective 3": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                                                    | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Special Agent Objective 4": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Special Agent": HasAll("Air Force One - Special Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & HasAll("K7 Avenger", "Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Special Agent Objective 1": HasAll("Crash Site - Special Agent", "President Scanner"),

        "Crash Site - Special Agent Objective 2": Has("Crash Site - Special Agent"),

        "Crash Site - Special Agent Objective 3": Has("Crash Site - Special Agent")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 4": Has("Crash Site - Special Agent")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Special Agent": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Special Agent Objective 1": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 2": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 3": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 4": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Special Agent": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Special Agent Objective 1": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 2": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 3": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 4": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Special Agent": HasAll("Deep Sea - Special Agent", "IR Scanner")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - CI Defense
        "CI Defense - Special Agent Objective 1": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 2": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 3": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "CI Defense - Special Agent Objective 4": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "Complete: CI Defense - Special Agent": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Special Agent Objective 1": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 2": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 3": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 4": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Special Agent": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Special Agent Objective 1": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Special Agent Objective 2": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 3": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 4": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Special Agent": HAS_SKEDAR_RUINS_SP_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Special Agent Objective 1": HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Special Agent Objective 2": Has("Mr. Blonde's Revenge - Special Agent")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Special Agent": HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAny("Mauler", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Special Agent Objective 1": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Special Agent Objective 2": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Special Agent": Has("Maian SOS - Special Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Special Agent Objective 1": Has("WAR! - Special Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Special Agent Objective 2": Has("WAR! - Special Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Special Agent": Has("WAR! - Special Agent")
                                        & (Has("Phoenix")
                                        | (all_guns_filter & HAS_ANY_RIFLE)
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Special Agent Objective 1": Has("The Duel - Special Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Special Agent Objective 2": Has("The Duel - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Special Agent": Has("The Duel - Special Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),
    }


    perfect_agent_rules_hard = {
        # Stage 1 - Defection
        "dD Defection - Perfect Agent Objective 1": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 2": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 3": HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 4": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 5": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Perfect Agent": HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink")
                                                & HAS_DD_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Perfect Agent Objective 1": HasAll("dD Investigation - Perfect Agent", "CamSpy")
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 2": Has("dD Investigation - Perfect Agent")
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 3": Has("dD Investigation - Perfect Agent")
                                                        & (HasAll("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 4": HasAll("dD Investigation - Perfect Agent", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Investigation - Perfect Agent Objective 5": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: dD Investigation - Perfect Agent": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "CMP150", "K7 Avenger")
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 3 - Extraction
        "dD Extraction - Perfect Agent Objective 1": Has("dD Extraction - Perfect Agent")
                                                    & (HasAny("Falcon 2 (Scope)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 2": Has("dD Extraction - Perfect Agent")
                                                    & (HasAny("Falcon 2 (Scope)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 3": Has("dD Extraction - Perfect Agent")
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Perfect Agent Objective 4": Has("dD Extraction - Perfect Agent")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 5": Has("dD Extraction - Perfect Agent")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Perfect Agent": Has("dD Extraction - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa  
        "Carrington Villa - Perfect Agent Objective 1": Has("Carrington Villa - Perfect Agent")
                                                        & (HasAny("Laptop Gun", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 2": Has("Carrington Villa - Perfect Agent")
                                                        & (HasAny("Laptop Gun", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 3": Has("Carrington Villa - Perfect Agent")
                                                        & ((Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 4": Has("Carrington Villa - Perfect Agent"),

        "Carrington Villa - Perfect Agent Objective 5": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & ((Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Perfect Agent": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & ((Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago  
        "Chicago - Perfect Agent Objective 1": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 2": HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                            & (HasAny("Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 3": Has("Chicago - Perfect Agent")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 4": Has("Chicago - Perfect Agent")
                                            & HasAny("Data Uplink", "CamSpy")
                                            & (HasAny("Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 5": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Perfect Agent": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & (HasAll("Remote Mine", "Falcon 2 (Scope)", "CMP150")
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Perfect Agent Objective 1": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 2": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 3": HasAll("G5 Building - Perfect Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 4": HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 5": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Perfect Agent": HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "CMP150", "Remote Mine")
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Perfect Agent Objective 1": HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 2": HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 3": Has("A51 Infiltration - Perfect Agent")
                                                        & (HasAll("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 4": Has("A51 Infiltration - Perfect Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 5": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Perfect Agent": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2", "MagSec 4", "Dragon")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Perfect Agent Objective 1": HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 2": HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 3": HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 4": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 5": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Perfect Agent": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Perfect Agent Objective 1": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 2": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 3": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 4": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 5": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Perfect Agent": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "SuperDragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base  
        "Air Base - Perfect Agent Objective 1": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 2": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 3": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 4": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & ((Has("Dragon") & HasAny("K7 Avenger", "Proximity Mine"))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Air Base - Perfect Agent Objective 5": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAll("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Perfect Agent": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAll("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One  
        "Air Force One - Perfect Agent Objective 1": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Perfect Agent Objective 2": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Perfect Agent Objective 3": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Perfect Agent Objective 4": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Air Force One - Perfect Agent Objective 5": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Perfect Agent": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (((Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & HasAll("K7 Avenger", "Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site  
        "Crash Site - Perfect Agent Objective 1": HasAll("Crash Site - Perfect Agent", "President Scanner"),

        "Crash Site - Perfect Agent Objective 2": Has("Crash Site - Perfect Agent"),

        "Crash Site - Perfect Agent Objective 3": Has("Crash Site - Perfect Agent")
                                                & ((HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle") & (Has("Remote Mine") | HasAll("DY357-LX", "President Scanner")))
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 4": Has("Crash Site - Perfect Agent")
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 5": Has("Crash Site - Perfect Agent")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Perfect Agent": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle") & HasAny("Remote Mine", "DY357-LX"))
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Perfect Agent Objective 1": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 2": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 3": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 4": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 5": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Perfect Agent": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Perfect Agent Objective 1": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Perfect Agent Objective 2": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 3": HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 4": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 5": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Deep Sea - Perfect Agent": HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                            | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 15 - CI Defense  
        "CI Defense - Perfect Agent Objective 1": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 2": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 3": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))),

        "CI Defense - Perfect Agent Objective 4": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((Has("AR34") & (HasAll("RC-P120", "Laser") | Has("Devastator")))
                                                | (all_guns_filter & (HAS_ANY_RIFLE & HasAll("RC-P120", "Laser")) | HasAny(*EXPLOSIVE_LIST))
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "CI Defense - Perfect Agent Objective 5": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("AR34", "RC-P120") & HasAny("Laser", "Devastator"))
                                                | (all_guns_filter & HAS_ANY_RIFLE & Has("RC-P120") & (Has("Laser") | HasAny(*EXPLOSIVE_LIST)))
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "Complete: CI Defense - Perfect Agent": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("AR34", "RC-P120") & HasAny("Laser", "Devastator"))
                                                | (all_guns_filter & HAS_ANY_RIFLE & Has("RC-P120") & (Has("Laser") | HasAny(*EXPLOSIVE_LIST)))
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Perfect Agent Objective 1": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 2": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 3": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 4": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 5": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Perfect Agent": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Combat Knife", "Mauler", "AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Perfect Agent Objective 1": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Perfect Agent Objective 2": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 3": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 4": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 5": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Perfect Agent": HAS_SKEDAR_RUINS_PF_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Perfect Agent Objective 1": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Perfect Agent Objective 2": Has("Mr. Blonde's Revenge - Perfect Agent")
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge - Perfect Agent Objective 3": Has("Mr. Blonde's Revenge - Perfect Agent")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Perfect Agent": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAny("Mauler", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Perfect Agent Objective 1": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 2": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon", "DY357-LX")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 3": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Perfect Agent": Has("Maian SOS - Perfect Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon", "DY357-LX")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Perfect Agent Objective 1": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 2": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 3": Has("WAR! - Perfect Agent")
                                            & (Has("Phoenix")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Perfect Agent": Has("WAR! - Perfect Agent")
                                        & (Has("Phoenix")
                                        | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Perfect Agent Objective 1": Has("The Duel - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Perfect Agent Objective 2": Has("The Duel - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "The Duel - Perfect Agent Objective 3": Has("The Duel - Perfect Agent")
                                                & (Has("Falcon 2 (Scope)")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: The Duel - Perfect Agent": Has("The Duel - Perfect Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (Has("Falcon 2 (Scope)")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),
    }


    cheat_rules_hard = {
        # Defection
        "Cheat Unlock: Complete dD Defection": (agent_rules_hard["Complete: dD Defection - Agent"])
                                                | (special_agent_rules_hard["Complete: dD Defection - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: dD Defection - Perfect Agent"]),

        # Investigation
        "Cheat Unlock: Complete dD Investigation": (agent_rules_hard["Complete: dD Investigation - Agent"])
                                                | (special_agent_rules_hard["Complete: dD Investigation - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: dD Investigation - Perfect Agent"]),

        # Extraction
        "Cheat Unlock: Complete dD Extraction": (agent_rules_hard["Complete: dD Extraction - Agent"])
                                                | (special_agent_rules_hard["Complete: dD Extraction - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: dD Extraction - Perfect Agent"]),

        # Villa
        "Cheat Unlock: Complete Carrington Villa": (agent_rules_hard["Complete: Carrington Villa - Agent"])
                                                | (special_agent_rules_hard["Complete: Carrington Villa - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Carrington Villa - Perfect Agent"]),
        
        # Chicago
        "Cheat Unlock: Complete Chicago": (agent_rules_hard["Complete: Chicago - Agent"])
                                                | (special_agent_rules_hard["Complete: Chicago - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Chicago - Perfect Agent"]),

        # G5 Building
        "Cheat Unlock: Complete G5 Building": (agent_rules_hard["Complete: G5 Building - Agent"])
                                                | (special_agent_rules_hard["Complete: G5 Building - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: G5 Building - Perfect Agent"]),

        # A51 Infiltration
        "Cheat Unlock: Complete A51 Infiltration": (agent_rules_hard["Complete: A51 Infiltration - Agent"])
                                                | (special_agent_rules_hard["Complete: A51 Infiltration - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: A51 Infiltration - Perfect Agent"]),

        # A51 Rescue
        "Cheat Unlock: Complete A51 Rescue": (agent_rules_hard["Complete: A51 Rescue - Agent"])
                                                | (special_agent_rules_hard["Complete: A51 Rescue - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: A51 Rescue - Perfect Agent"]),

        # A51 Escape
        "Cheat Unlock: Complete A51 Escape": (agent_rules_hard["Complete: A51 Escape - Agent"])
                                                | (special_agent_rules_hard["Complete: A51 Escape - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: A51 Escape - Perfect Agent"]),

        # Air Base
        "Cheat Unlock: Complete Air Base": (agent_rules_hard["Complete: Air Base - Agent"])
                                                | (special_agent_rules_hard["Complete: Air Base - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Air Base - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Air Force One": (agent_rules_hard["Complete: Air Force One - Agent"])
                                                | (special_agent_rules_hard["Complete: Air Force One - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Air Force One - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Crash Site": (agent_rules_hard["Complete: Crash Site - Agent"])
                                                | (special_agent_rules_hard["Complete: Crash Site - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Crash Site - Perfect Agent"]),

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II": (agent_rules_hard["Complete: Pelagic II - Agent"])
                                                | (special_agent_rules_hard["Complete: Pelagic II - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Pelagic II - Perfect Agent"]),

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea": (agent_rules_hard["Complete: Deep Sea - Agent"])
                                                | (special_agent_rules_hard["Complete: Deep Sea - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Deep Sea - Perfect Agent"]),

        # CI Defense
        "Cheat Unlock: Complete CI Defense": (agent_rules_hard["Complete: CI Defense - Agent"])
                                                | (special_agent_rules_hard["Complete: CI Defense - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: CI Defense - Perfect Agent"]),

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship": (agent_rules_hard["Complete: Attack Ship - Agent"])
                                                | (special_agent_rules_hard["Complete: Attack Ship - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Attack Ship - Perfect Agent"]),

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins": (agent_rules_hard["Complete: Skedar Ruins - Agent"])
                                                | (special_agent_rules_hard["Complete: Skedar Ruins - Special Agent"])
                                                | (perfect_agent_rules_hard["Complete: Skedar Ruins - Perfect Agent"]),
    }


    cheat_agent_rules_hard = {
        # Extraction
        "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03": agent_rules_hard["Complete: dD Extraction - Agent"],

        # G5 Building
        "Cheat Unlock: Complete G5 Building (Agent) in under 1:40": agent_rules_hard["Complete: G5 Building - Agent"],

        # Escape
        "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50": agent_rules_hard["Complete: A51 Escape - Agent"],

        # Crash Site
        "Cheat Unlock: Complete Crash Site (Agent) in under 2:50": agent_rules_hard["Complete: Crash Site - Agent"],

        # CI Defense
        "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": agent_rules_hard["Complete: CI Defense - Agent"],
    }


    cheat_sp_agent_rules_hard = {
        # Defection
        "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30": special_agent_rules_hard["Complete: dD Defection - Special Agent"],

        # Villa
        "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30": special_agent_rules_hard["Complete: Carrington Villa - Special Agent"],

        # Infiltration
        "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00": special_agent_rules_hard["Complete: A51 Infiltration - Special Agent"],

        # Air Base
        "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11": special_agent_rules_hard["Complete: Air Base - Special Agent"],

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07": special_agent_rules_hard["Complete: Pelagic II - Special Agent"],

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17": special_agent_rules_hard["Complete: Attack Ship - Special Agent"],
    }


    cheat_pf_agent_rules_hard = {
        # Investigation
        "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30": perfect_agent_rules_hard["Complete: dD Investigation - Perfect Agent"],

        # Chicago
        "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00": perfect_agent_rules_hard["Complete: Chicago - Perfect Agent"] & Has("CamSpy"),

        # Rescue
        "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59": perfect_agent_rules_hard["Complete: A51 Rescue - Perfect Agent"],

        # Air Force One
        "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55": perfect_agent_rules_hard["Complete: Air Force One - Perfect Agent"],

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27": perfect_agent_rules_hard["Complete: Deep Sea - Perfect Agent"],

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31": perfect_agent_rules_hard["Complete: Skedar Ruins - Perfect Agent"],
    }


    agent_alternate_exits_hard = {
        "Complete A51 Escape (Agent): UFO Escape": agent_rules_hard["Complete: A51 Escape - Agent"],
        "Complete A51 Escape (Agent): Alternate Escape": agent_rules_hard["Complete: A51 Escape - Agent"],
        "Complete Air Base (Agent): Shuttle Exit": agent_rules_hard["Complete: Air Base - Agent"],
        "Complete Air Base (Agent): Ladder Exit": agent_rules_hard["Complete: Air Base - Agent"],
    }


    special_agent_alternate_exits_hard = {
        "Complete A51 Escape (Special Agent): UFO Escape": special_agent_rules_hard["Complete: A51 Escape - Special Agent"],
        "Complete A51 Escape (Special Agent): Alternate Escape": special_agent_rules_hard["Complete: A51 Escape - Special Agent"],
        "Complete Air Base (Special Agent): Shuttle Exit": special_agent_rules_hard["Complete: Air Base - Special Agent"],
        "Complete Air Base (Special Agent): Ladder Exit": special_agent_rules_hard["Complete: Air Base - Special Agent"],
    }


    perfect_agent_alternate_exits_hard = {
        "Complete A51 Escape (Perfect Agent): UFO Escape": perfect_agent_rules_hard["Complete: A51 Escape - Perfect Agent"],
        "Complete A51 Escape (Perfect Agent): Alternate Escape": perfect_agent_rules_hard["Complete: A51 Escape - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Shuttle Exit": perfect_agent_rules_hard["Complete: Air Base - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Ladder Exit": perfect_agent_rules_hard["Complete: Air Base - Perfect Agent"],
    }


    if world.options.agent:
        add_rule(world, agent_rules_hard)

        if world.options.alternate_exits:
            add_rule(world, agent_alternate_exits_hard)

    if world.options.special_agent:
        add_rule(world, special_agent_rules_hard)

        if world.options.alternate_exits:
            add_rule(world, special_agent_alternate_exits_hard)

    if world.options.perfect_agent:
        add_rule(world, perfect_agent_rules_hard)

        if world.options.alternate_exits:
            add_rule(world, perfect_agent_alternate_exits_hard)

    if world.options.completion_cheats:
        if world.options.agent or world.options.special_agent or world.options.perfect_agent:
            add_rule(world, cheat_rules_hard)

    if world.options.timed_cheats:
        if world.options.agent:
            add_rule(world, cheat_agent_rules_hard)
        if world.options.special_agent:
            add_rule(world, cheat_sp_agent_rules_hard)
        if world.options.perfect_agent:
            add_rule(world, cheat_pf_agent_rules_hard)

    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent:
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 1"), agent_rules_hard["Skedar Ruins - Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 2"), agent_rules_hard["Skedar Ruins - Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 3"), agent_rules_hard["Skedar Ruins - Agent Objective 3"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Agent"), agent_rules_hard["Complete: Skedar Ruins - Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 1"), special_agent_rules_hard["Skedar Ruins - Special Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 2"), special_agent_rules_hard["Skedar Ruins - Special Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 3"), special_agent_rules_hard["Skedar Ruins - Special Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 4"), special_agent_rules_hard["Skedar Ruins - Special Agent Objective 4"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Special Agent"), special_agent_rules_hard["Complete: Skedar Ruins - Special Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 1"), perfect_agent_rules_hard["Skedar Ruins - Perfect Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 2"), perfect_agent_rules_hard["Skedar Ruins - Perfect Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 3"), perfect_agent_rules_hard["Skedar Ruins - Perfect Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 4"), perfect_agent_rules_hard["Skedar Ruins - Perfect Agent Objective 4"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 5"), perfect_agent_rules_hard["Skedar Ruins - Perfect Agent Objective 5"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Perfect Agent"), perfect_agent_rules_hard["Complete: Skedar Ruins - Perfect Agent"])

        if world.options.completion_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins"), cheat_rules_hard["Cheat Unlock: Complete Skedar Ruins"])
        if world.options.timed_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"), cheat_pf_agent_rules_hard["Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"])


def set_all_perfect_location_rules(world: PerfectDarkWorld) -> None:
    agent_rules_perfect = {
        # Stage 1 - Defection
        "dD Defection - Agent Objective 1": Has("dD Defection - Agent")
                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True),

        "Complete: dD Defection - Agent": Has("dD Defection - Agent")
                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True),


        # Stage 2 - Investigation
        "dD Investigation - Agent Objective 1": HasAll("dD Investigation - Agent", "CamSpy"),

        "dD Investigation - Agent Objective 2": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Agent": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & (HasAny("Falcon 2", "CMP150")
                                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Agent Objective 1": Has("dD Extraction - Agent")
                                             & (HasAny("Falcon 2 (Scope)", "CMP150")
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 2": Has("dD Extraction - Agent")
                                             & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                             & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Agent Objective 3": Has("dD Extraction - Agent")
                                             & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                             & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                             | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Agent": Has("dD Extraction - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                           & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                           | HAS_ANY_WEAPON_TYPE),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Agent Objective 1": Has("Carrington Villa - Agent")
                                                & (HasAny("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 2": Has("Carrington Villa - Agent")
                                                & (HasAny("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Agent Objective 3": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Sniper Rifle", "CMP150")
                                                | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Agent": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                              & (HasAny("Sniper Rifle", "CMP150")
                                              | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago  
        "Chicago - Agent Objective 1": HasAll("Chicago - Agent", "Data Uplink")
                                       & (Has("Remote Mine")
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"])),

        "Chicago - Agent Objective 2": Has("Chicago - Agent")
                                       & HasAny("Data Uplink", "CamSpy")
                                       & (HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum")
                                       | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                       | HAS_ANY_WEAPON_TYPE),

        "Chicago - Agent Objective 3": HasAll("Chicago - Agent", "Data Uplink")
                                       & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                       | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                       | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                       | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Agent": HasAll("Chicago - Agent", "Data Uplink")
                                     & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                     | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                     | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                     | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Agent Objective 1": HasAll("G5 Building - Agent", "CamSpy")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 2": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Agent Objective 3": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: G5 Building - Agent": HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                        & HAS_G5_KEYS
                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Agent Objective 1": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & (HasAny("Falcon 2", "MagSec 4")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 2": Has("A51 Infiltration - Agent")
                                                & HAS_A51_INFIL_KEYS
                                                & (HasAny("Falcon 2", "MagSec 4")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Agent Objective 3": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & HAS_A51_INFIL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Agent": HasAll("A51 Infiltration - Agent", "Explosives")
                                            & HAS_A51_INFIL_KEYS
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                            & (HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2)
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Agent Objective 1": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 2": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_FIRST_KEY
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Agent Objective 3": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_ALL_KEYS
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Agent": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                        & HAS_A51_RESCUE_ALL_KEYS
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Agent Objective 1": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 2": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Agent Objective 3": HasAll("A51 Escape - Agent", "Alien Medpack")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Agent": HasAll("A51 Escape - Agent", "Alien Medpack")
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Agent Objective 1": HasAll("Air Base - Agent", "Stewardess Disguise"),

        "Air Base - Agent Objective 2": HasAll("Air Base - Agent", "Stewardess Disguise"),

        "Air Base - Agent Objective 3": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & (HasAny("Crossbow", "CamSpy")
                                        | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                        & (HasAll("Dragon", "K7 Avenger")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Agent": HasAll("Air Base - Agent", "Stewardess Disguise")
                                      & (HasAny("Crossbow", "CamSpy")
                                      | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                      & (HasAll("Dragon", "K7 Avenger")
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One  
        "Air Force One - Agent Objective 1": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Agent Objective 2": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & (HasAny("Laptop Gun", "Cyclone", "K7 Avenger")
                                             | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                             | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Agent Objective 3": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                             & ((HasAny("Laptop Gun", "Cyclone", "K7 Avenger") & Has("Timed Mine"))
                                             | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                             | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                             | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Agent": HasAll("Air Force One - Agent", "Suitcase")
                                           & Has("President", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & ((HasAny("Laptop Gun", "Cyclone", "K7 Avenger") & Has("Timed Mine"))
                                           | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                           | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                           | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Agent Objective 1": Has("Crash Site - Agent"),

        "Crash Site - Agent Objective 2": Has("Crash Site - Agent")
                                          & (HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Agent Objective 3": Has("Crash Site - Agent")
                                          & Has("President", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2)
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Agent": Has("Crash Site - Agent")
                                        & Has("President", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2)
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Agent Objective 1": Has("Pelagic II - Agent")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 2": Has("Pelagic II - Agent")
                                          & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Agent Objective 3": Has("Pelagic II - Agent")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2)
                                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                          | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Agent": Has("Pelagic II - Agent")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2)
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Agent Objective 1": Has("Deep Sea - Agent")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 2": Has("Deep Sea - Agent")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Agent Objective 3": Has("Deep Sea - Agent")
                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Agent": Has("Deep Sea - Agent")
                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                      & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                      & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                      | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                      | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - Carrington Institute Defense
        "CI Defense - Agent Objective 1": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & (HasAny("AR34", "Mauler")
                                          | (all_guns_filter & HAS_ANY_RIFLE)
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                          | HAS_ANY_WEAPON_TYPE),

        "CI Defense - Agent Objective 2": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & ((HasAny("AR34", "Mauler") & Has("RC-P120"))
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "CI Defense - Agent Objective 3": HasAll("CI Defense - Agent", "Data Uplink")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & ((HasAny("AR34", "Mauler") & Has("RC-P120"))
                                          | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                          | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                          | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: CI Defense - Agent": HasAll("CI Defense - Agent", "Data Uplink")
                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                        & ((HasAny("AR34", "Mauler") & Has("RC-P120"))
                                        | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                        | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                        | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 16 - Attack Ship
        "Attack Ship - Agent Objective 1": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & (Has("Mauler")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 2": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (Has("Mauler")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Agent Objective 3": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & (Has("Mauler")
                                           | (all_guns_filter & HAS_ANY_RIFLE)
                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                           | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Agent": Has("Attack Ship - Agent")
                                         & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (Has("Mauler")
                                         | (all_guns_filter & HAS_ANY_RIFLE)
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                         | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Agent Objective 1": HAS_SKEDAR_RUINS_AGENT
                                            & HasAll("R-Tracker", "Target Amplifier")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Agent Objective 2": HAS_SKEDAR_RUINS_AGENT
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Agent Objective 3": HAS_SKEDAR_RUINS_AGENT
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Agent": HAS_SKEDAR_RUINS_AGENT
                                          & HasAll("R-Tracker", "Target Amplifier")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                          | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                          | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Agent Objective 1": HasAll("Mr. Blonde's Revenge - Agent")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (Has("Mauler")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Agent": HasAll("Mr. Blonde's Revenge - Agent")
                                                  & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                  & (Has("Mauler")
                                                  | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Agent Objective 1": Has("Maian SOS - Agent")
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & (HasAll("Falcon 2", "Dragon")
                                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                         | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Agent": Has("Maian SOS - Agent")
                                       & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                       & (HasAll("Falcon 2", "Dragon")
                                       | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                       | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Agent Objective 1": Has("WAR! - Agent")
                                    & (HasAny("Phoenix", "Callisto NTG", "Mauler")
                                    | (all_guns_filter & HAS_ANY_RIFLE)
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Agent": Has("WAR! - Agent")
                                  & (HasAny("Phoenix", "Callisto NTG", "Mauler")
                                  | (all_guns_filter & HAS_ANY_RIFLE)
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                  | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Agent Objective 1": Has("The Duel - Agent"),

        "Complete: The Duel - Agent": Has("The Duel - Agent"),
    }


    special_agent_rules_perfect = {
        # Stage 1 - Defection
        "dD Defection - Special Agent Objective 1": HasAll("dD Defection - Special Agent", "ECM Mine"),

        "dD Defection - Special Agent Objective 2": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS,

        "dD Defection - Special Agent Objective 3": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Special Agent Objective 4": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Special Agent": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                & HAS_DD_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Special Agent Objective 1": HasAll("dD Investigation - Special Agent", "CamSpy"),

        "dD Investigation - Special Agent Objective 2": Has("dD Investigation - Special Agent"),

        "dD Investigation - Special Agent Objective 3": Has("dD Investigation - Special Agent")
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Special Agent Objective 4": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Investigation - Special Agent": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAny("Falcon 2", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 3 - Extraction
        "dD Extraction - Special Agent Objective 1": Has("dD Extraction - Special Agent")
                                                    & (HasAny("Falcon 2 (Scope)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 2": Has("dD Extraction - Special Agent")
                                                    & ((HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                        | (HasAny("Falcon 2 (Scope)", "CMP150") & Has("Rocket Launcher")))
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Special Agent Objective 3": Has("dD Extraction - Special Agent")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Special Agent Objective 4": Has("dD Extraction - Special Agent")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Special Agent": Has("dD Extraction - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Special Agent Objective 1": Has("Carrington Villa - Special Agent")
                                                        & (HasAny("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 2": Has("Carrington Villa - Special Agent")
                                                        & (HasAny("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 3": Has("Carrington Villa - Special Agent")
                                                        & (HasAny("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Special Agent Objective 4": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAny("Sniper Rifle", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Special Agent": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAny("Sniper Rifle", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago  
        "Chicago - Special Agent Objective 1": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & (Has("Remote Mine")
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                                            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"])),

        "Chicago - Special Agent Objective 2": Has("Chicago - Special Agent")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Special Agent Objective 3": Has("Chicago - Special Agent")
                                            & HasAny("Data Uplink", "CamSpy")
                                            & (HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Special Agent Objective 4": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Special Agent": HasAll("Chicago - Special Agent", "Data Uplink")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Special Agent Objective 1": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 2": HasAll("G5 Building - Special Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 3": HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Special Agent Objective 4": Has("G5 Building - Special Agent")
                                                & HAS_G5_KEYS
                                                & ((HasAny("Falcon 2 (Silencer)", "CMP150") & Has("Remote Mine"))
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Special Agent": HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Silencer)", "CMP150") & Has("Remote Mine"))
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Special Agent Objective 1": HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 2": HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 3": Has("A51 Infiltration - Special Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Special Agent Objective 4": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2)
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Special Agent": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Special Agent Objective 1": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 2": HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 3": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Special Agent Objective 4": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Special Agent": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Special Agent Objective 1": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 2": Has("A51 Escape - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 3": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Special Agent Objective 4": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Special Agent": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base
        "Air Base - Special Agent Objective 1": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 2": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 3": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Special Agent Objective 4": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAny("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Special Agent": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAny("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One  
        "Air Force One - Special Agent Objective 1": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Special Agent Objective 2": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Special Agent Objective 3": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAny("Laptop Gun", "Cyclone", "K7 Avenger")
                                                    | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Special Agent Objective 4": HasAll("Air Force One - Special Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAny("Laptop Gun", "Cyclone", "K7 Avenger")
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=1))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Special Agent": HasAll("Air Force One - Special Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Laptop Gun", "Cyclone", "K7 Avenger")
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*exclude_weapons_from_list(["Timed Mine"]), count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site
        "Crash Site - Special Agent Objective 1": HasAll("Crash Site - Special Agent", "President Scanner"),

        "Crash Site - Special Agent Objective 2": Has("Crash Site - Special Agent"),

        "Crash Site - Special Agent Objective 3": Has("Crash Site - Special Agent")
                                                & (HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Special Agent Objective 4": Has("Crash Site - Special Agent")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Special Agent": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Special Agent Objective 1": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 2": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 3": Has("Pelagic II - Special Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Special Agent Objective 4": Has("Pelagic II - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Special Agent": Has("Pelagic II - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Special Agent Objective 1": Has("Deep Sea - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 2": Has("Deep Sea - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 3": Has("Deep Sea - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Special Agent Objective 4": Has("Deep Sea - Special Agent")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Deep Sea - Special Agent": Has("Deep Sea - Special Agent")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasFromList("Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", count=2)
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 15 - CI Defense
        "CI Defense - Special Agent Objective 1": Has("CI Defense - Special Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True),

        "CI Defense - Special Agent Objective 2": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("AR34", "Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"])),

        "CI Defense - Special Agent Objective 3": Has("CI Defense - Special Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("AR34", "Mauler") & Has("RC-P120"))
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "CI Defense - Special Agent Objective 4": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("AR34", "Mauler") & Has("RC-P120"))
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),

        "Complete: CI Defense - Special Agent": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("AR34", "Mauler") & Has("RC-P120"))
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["KF7 Special"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Special Agent Objective 1": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 2": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 3": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Special Agent Objective 4": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Special Agent": Has("Attack Ship - Special Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Special Agent Objective 1": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Special Agent Objective 2": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 3": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Special Agent Objective 4": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Special Agent": HAS_SKEDAR_RUINS_SP_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Special Agent Objective 1": HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE
                                                            | Has("Cloaking Device")),

        "Mr. Blonde's Revenge - Special Agent Objective 2": HasAll("Mr. Blonde's Revenge - Special Agent")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Special Agent": HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAny("Mauler", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Special Agent Objective 1": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Special Agent Objective 2": Has("Maian SOS - Special Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Special Agent": Has("Maian SOS - Special Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Special Agent Objective 1": Has("WAR! - Special Agent")
                                            & (HasAny("Phoenix", "Callisto NTG", "Mauler")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Special Agent Objective 2": Has("WAR! - Special Agent")
                                            & (HasAny("Phoenix", "Callisto NTG", "Mauler")
                                            | (all_guns_filter & HAS_ANY_RIFLE)
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Special Agent": Has("WAR! - Special Agent")
                                        & (HasAny("Phoenix", "Callisto NTG", "Mauler")
                                        | (all_guns_filter & HAS_ANY_RIFLE)
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Special Agent Objective 1": Has("The Duel - Special Agent"),

        "The Duel - Special Agent Objective 2": Has("The Duel - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True),

        "Complete: The Duel - Special Agent": Has("The Duel - Special Agent")
                                              & Has("Jonathan", options=[npc_filter], filtered_resolution=True),
    }


    perfect_agent_rules_perfect = {
        # Stage 1 - Defection
        "dD Defection - Perfect Agent Objective 1": HasAll("dD Defection - Perfect Agent", "ECM Mine"),

        "dD Defection - Perfect Agent Objective 2": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS,

        "dD Defection - Perfect Agent Objective 3": HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 4": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Defection - Perfect Agent Objective 5": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Defection - Perfect Agent": HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink")
                                                & HAS_DD_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 2 - Investigation
        "dD Investigation - Perfect Agent Objective 1": HasAll("dD Investigation - Perfect Agent", "CamSpy"),

        "dD Investigation - Perfect Agent Objective 2": Has("dD Investigation - Perfect Agent"),

        "dD Investigation - Perfect Agent Objective 3": Has("dD Investigation - Perfect Agent")
                                                        & (HasAny("Falcon 2", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "dD Investigation - Perfect Agent Objective 4": HasAll("dD Investigation - Perfect Agent", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & ((HasAny("Falcon 2", "CMP150") & Has("K7 Avenger"))
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Investigation - Perfect Agent Objective 5": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & ((HasAny("Falcon 2", "CMP150") & Has("K7 Avenger"))
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: dD Investigation - Perfect Agent": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & ((HasAny("Falcon 2", "CMP150") & Has("K7 Avenger"))
                                                        | (all_guns_filter & Has("K7 Avenger") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | ((Has("K7 Avenger") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
                                                        | (Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 3 - Extraction
        "dD Extraction - Perfect Agent Objective 1": Has("dD Extraction - Perfect Agent")
                                                    & (HasAny("Falcon 2 (Scope)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 2": Has("dD Extraction - Perfect Agent")
                                                    & (HasAny("Falcon 2 (Scope)", "CMP150")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 3": Has("dD Extraction - Perfect Agent")
                                                    & ((HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                        | (HasAny("Falcon 2 (Scope)", "CMP150") & Has("Rocket Launcher")))
                                                    | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),

        "dD Extraction - Perfect Agent Objective 4": Has("dD Extraction - Perfect Agent")
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "dD Extraction - Perfect Agent Objective 5": Has("dD Extraction - Perfect Agent")
                                                    & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Complete: dD Extraction - Perfect Agent": Has("dD Extraction - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2)
                                                | (all_guns_filter & HasAny("Rocket Launcher", "Slayer", "Devastator") & HasFromList(*exclude_weapons_from_list(["Rocket Launcher", "Slayer", "Devastator"]), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 4 - Carrington Villa  
        "Carrington Villa - Perfect Agent Objective 1": Has("Carrington Villa - Perfect Agent")
                                                        & (HasAny("Laptop Gun", "CMP150", "Sniper Rifle")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 2": Has("Carrington Villa - Perfect Agent")
                                                        & (HasAny("Laptop Gun", "CMP150", "Sniper Rifle")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 3": Has("Carrington Villa - Perfect Agent")
                                                        & (HasAny("Laptop Gun", "CMP150", "Sniper Rifle")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Carrington Villa - Perfect Agent Objective 4": Has("Carrington Villa - Perfect Agent"),

        "Carrington Villa - Perfect Agent Objective 5": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & (HasFromList("Laptop Gun", "CMP150", "Sniper Rifle", count=2)
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: Carrington Villa - Perfect Agent": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Laptop Gun", "CMP150", "Sniper Rifle", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 5 - Chicago  
        "Chicago - Perfect Agent Objective 1": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                            & (Has("Remote Mine")
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                                            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"])),

        "Chicago - Perfect Agent Objective 2": HasAll("Chicago - Perfect Agent", "Tracer Bug"),

        "Chicago - Perfect Agent Objective 3": Has("Chicago - Perfect Agent")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Chicago - Perfect Agent Objective 4": Has("Chicago - Perfect Agent")
                                            & HasAny("Data Uplink", "CamSpy")
                                            & (HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum")
                                            | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Chicago - Perfect Agent Objective 5": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Chicago - Perfect Agent": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                            & ((Has("Remote Mine") & HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum"))
                                            | (all_guns_filter & Has("Remote Mine") & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                                            | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                            | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 6 - G5 Building
        "G5 Building - Perfect Agent Objective 1": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 2": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 3": HasAll("G5 Building - Perfect Agent", "CamSpy")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 4": HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & (HasAny("Falcon 2 (Silencer)", "CMP150")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "G5 Building - Perfect Agent Objective 5": Has("G5 Building - Perfect Agent")
                                                & HAS_G5_KEYS
                                                & ((HasAny("Falcon 2 (Silencer)", "CMP150") & Has("Remote Mine"))
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: G5 Building - Perfect Agent": HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                & HAS_G5_KEYS
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Silencer)", "CMP150") & Has("Remote Mine"))
                                                | (all_guns_filter & Has("Remote Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Remote Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Perfect Agent Objective 1": HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 2": HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 3": Has("A51 Infiltration - Perfect Agent")
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 4": Has("A51 Infiltration - Perfect Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & (HasAny("Falcon 2", "MagSec 4")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "A51 Infiltration - Perfect Agent Objective 5": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & (HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2)
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Infiltration - Perfect Agent": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                    & HAS_A51_INFIL_KEYS
                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                    & (HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2)
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),


        # Stage 8 - A51 Rescue
        "A51 Rescue - Perfect Agent Objective 1": HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 2": HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Silencer)", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 3": HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 4": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_FIRST_KEY
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Rescue - Perfect Agent Objective 5": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Rescue - Perfect Agent": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 9 - A51 Escape
        "A51 Escape - Perfect Agent Objective 1": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 2": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 3": Has("A51 Escape - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 4": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "A51 Escape - Perfect Agent Objective 5": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: A51 Escape - Perfect Agent": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 10 - Air Base  
        "Air Base - Perfect Agent Objective 1": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 2": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 3": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base - Perfect Agent Objective 4": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & ((Has("Dragon") & HasAny("K7 Avenger", "Proximity Mine"))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Air Base - Perfect Agent Objective 5": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                & (HasAny("Crossbow", "CamSpy")
                                                | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                & (HasAny("Dragon", "K7 Avenger")
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Air Base - Perfect Agent": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                              & (HasAny("Crossbow", "CamSpy")
                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                              & (HasAny("Dragon", "K7 Avenger")
                                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                              | HAS_ANY_WEAPON_TYPE),


        # Stage 11 - Air Force One  
        "Air Force One - Perfect Agent Objective 1": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY,

        "Air Force One - Perfect Agent Objective 2": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Perfect Agent Objective 3": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAny("Laptop Gun", "Cyclone", "K7 Avenger")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Air Force One - Perfect Agent Objective 4": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                    & HAS_AFO_LIFT_KEY
                                                    & Has("President", options=[npc_filter], filtered_resolution=True)
                                                    & ((HasAny("Laptop Gun", "Cyclone", "K7 Avenger") & Has("Timed Mine"))
                                                    | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Air Force One - Perfect Agent Objective 5": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Laptop Gun", "Cyclone", "K7 Avenger") & Has("Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Air Force One - Perfect Agent": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                & HAS_AFO_LIFT_KEY
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Laptop Gun", "Cyclone", "K7 Avenger") & Has("Timed Mine"))
                                                | (all_guns_filter & Has("Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | ((Has("Timed Mine") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 12 - Crash Site  
        "Crash Site - Perfect Agent Objective 1": HasAll("Crash Site - Perfect Agent", "President Scanner"),

        "Crash Site - Perfect Agent Objective 2": Has("Crash Site - Perfect Agent"),

        "Crash Site - Perfect Agent Objective 3": Has("Crash Site - Perfect Agent")
                                                & ((HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2) & (Has("Remote Mine") | HasAll("DY357-LX", "President Scanner")))
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 4": Has("Crash Site - Perfect Agent")
                                                & (HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Crash Site - Perfect Agent Objective 5": Has("Crash Site - Perfect Agent")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Crash Site - Perfect Agent": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2) & HasAny("Remote Mine", "DY357-LX"))
                                                | (all_guns_filter & HasAny("Remote Mine", "Proximity Mine", "Timed Mine") & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 13 - Pelagic II
        "Pelagic II - Perfect Agent Objective 1": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 2": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 3": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 4": Has("Pelagic II - Perfect Agent")
                                                & (HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Pelagic II - Perfect Agent Objective 5": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Pelagic II - Perfect Agent": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 14 - Deep Sea
        "Deep Sea - Perfect Agent Objective 1": Has("Deep Sea - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAny("Falcon 2 (Scope)", "Shotgun")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Deep Sea - Perfect Agent Objective 2": Has("Deep Sea - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 3": Has("Deep Sea - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 4": HasAll("Deep Sea - Perfect Agent", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Deep Sea - Perfect Agent Objective 5": HasAll("Deep Sea - Perfect Agent", "Backup Disk")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                                | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                                | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Deep Sea - Perfect Agent": HasAll("Deep Sea - Perfect Agent", "Backup Disk")
                                            & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & ((HasAny("Falcon 2 (Scope)", "Shotgun") & Has("FarSight XR-20"))
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2) & Has("FarSight XR-20"))
                                            | ((Has("FarSight XR-20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
                                            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 15 - CI Defense  
        "CI Defense - Perfect Agent Objective 1": Has("CI Defense - Perfect Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True),

        "CI Defense - Perfect Agent Objective 2": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (Has("AR34")
                                                | (all_guns_filter & HAS_ANY_RIFLE)
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "CI Defense - Perfect Agent Objective 3": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("AR34", "RC-P120")
                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))),

        "CI Defense - Perfect Agent Objective 4": Has("CI Defense - Perfect Agent")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((Has("AR34") & (HasAll("RC-P120", "Laser") | Has("Devastator")))
                                                | (all_guns_filter & (HAS_ANY_RIFLE & HasAll("RC-P120", "Laser")) | HasAny(*EXPLOSIVE_LIST))
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "CI Defense - Perfect Agent Objective 5": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("AR34", "RC-P120") & HasAny("Laser", "Devastator"))
                                                | (all_guns_filter & HAS_ANY_RIFLE & Has("RC-P120") & (Has("Laser") | HasAny(*EXPLOSIVE_LIST)))
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),

        "Complete: CI Defense - Perfect Agent": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & ((HasAll("AR34", "RC-P120") & HasAny("Laser", "Devastator"))
                                                | (all_guns_filter & HAS_ANY_RIFLE & Has("RC-P120") & (Has("Laser") | HasAny(*EXPLOSIVE_LIST)))
                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) 
                                                    & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])
                                                    & Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))),


        # Stage 16 - Attack Ship
        "Attack Ship - Perfect Agent Objective 1": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 2": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 3": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 4": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Attack Ship - Perfect Agent Objective 5": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Attack Ship - Perfect Agent": Has("Attack Ship - Perfect Agent")
                                                & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (Has("Mauler")
                                                | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                | HAS_ANY_WEAPON_TYPE),


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Perfect Agent Objective 1": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG")
                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                                    | HAS_ANY_WEAPON_TYPE),

        "Skedar Ruins - Perfect Agent Objective 2": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 3": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 4": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Skedar Ruins - Perfect Agent Objective 5": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),

        "Complete: Skedar Ruins - Perfect Agent": HAS_SKEDAR_RUINS_PF_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)),


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Perfect Agent Objective 1": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE
                                                            | Has("Cloaking Device")),

        "Mr. Blonde's Revenge - Perfect Agent Objective 2": HasAll("Mr. Blonde's Revenge - Perfect Agent")
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE
                                                            | (HasAll("CamSpy", "Cloaking Device"))),

        "Mr. Blonde's Revenge - Perfect Agent Objective 3": HasAll("Mr. Blonde's Revenge - Perfect Agent")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & (HasAny("Mauler", "CMP150")
                                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: Mr. Blonde's Revenge - Perfect Agent": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                        & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                        & (HasAny("Mauler", "CMP150")
                                                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 19 - Maian SOS
        "Maian SOS - Perfect Agent Objective 1": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 2": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Maian SOS - Perfect Agent Objective 3": Has("Maian SOS - Perfect Agent")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & (HasAll("Falcon 2", "Dragon")
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                                | HAS_ANY_WEAPON_TYPE),

        "Complete: Maian SOS - Perfect Agent": Has("Maian SOS - Perfect Agent")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & (HasAll("Falcon 2", "Dragon")
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                            | HAS_ANY_WEAPON_TYPE),


        # Stage 20 - WAR!
        "WAR! - Perfect Agent Objective 1": Has("WAR! - Perfect Agent")
                                            & (HasAll("Phoenix", "Callisto NTG", "Mauler")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 2": Has("WAR! - Perfect Agent")
                                            & (HasAll("Phoenix", "Callisto NTG", "Mauler")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "WAR! - Perfect Agent Objective 3": Has("WAR! - Perfect Agent")
                                            & (HasAll("Phoenix", "Callisto NTG", "Mauler")
                                            | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                            | HAS_ANY_WEAPON_TYPE),

        "Complete: WAR! - Perfect Agent": Has("WAR! - Perfect Agent")
                                        & (HasAll("Phoenix", "Callisto NTG", "Mauler")
                                        | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                        | HAS_ANY_WEAPON_TYPE),


        # Stage 21 - The Duel
        "The Duel - Perfect Agent Objective 1": Has("The Duel - Perfect Agent"),

        "The Duel - Perfect Agent Objective 2": Has("The Duel - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True),

        "The Duel - Perfect Agent Objective 3": Has("The Duel - Perfect Agent"),

        "Complete: The Duel - Perfect Agent": Has("The Duel - Perfect Agent")
                                            & Has("Jonathan", options=[npc_filter], filtered_resolution=True),
    }


    cheat_rules_perfect = {
        # Defection
        "Cheat Unlock: Complete dD Defection": (agent_rules_perfect["Complete: dD Defection - Agent"])
                                                | (special_agent_rules_perfect["Complete: dD Defection - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: dD Defection - Perfect Agent"]),

        # Investigation
        "Cheat Unlock: Complete dD Investigation": (agent_rules_perfect["Complete: dD Investigation - Agent"])
                                                | (special_agent_rules_perfect["Complete: dD Investigation - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: dD Investigation - Perfect Agent"]),

        # Extraction
        "Cheat Unlock: Complete dD Extraction": (agent_rules_perfect["Complete: dD Extraction - Agent"])
                                                | (special_agent_rules_perfect["Complete: dD Extraction - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: dD Extraction - Perfect Agent"]),

        # Villa
        "Cheat Unlock: Complete Carrington Villa": (agent_rules_perfect["Complete: Carrington Villa - Agent"])
                                                | (special_agent_rules_perfect["Complete: Carrington Villa - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Carrington Villa - Perfect Agent"]),
        
        # Chicago
        "Cheat Unlock: Complete Chicago": (agent_rules_perfect["Complete: Chicago - Agent"])
                                                | (special_agent_rules_perfect["Complete: Chicago - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Chicago - Perfect Agent"]),

        # G5 Building
        "Cheat Unlock: Complete G5 Building": (agent_rules_perfect["Complete: G5 Building - Agent"])
                                                | (special_agent_rules_perfect["Complete: G5 Building - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: G5 Building - Perfect Agent"]),

        # A51 Infiltration
        "Cheat Unlock: Complete A51 Infiltration": (agent_rules_perfect["Complete: A51 Infiltration - Agent"])
                                                | (special_agent_rules_perfect["Complete: A51 Infiltration - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: A51 Infiltration - Perfect Agent"]),

        # A51 Rescue
        "Cheat Unlock: Complete A51 Rescue": (agent_rules_perfect["Complete: A51 Rescue - Agent"])
                                                | (special_agent_rules_perfect["Complete: A51 Rescue - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: A51 Rescue - Perfect Agent"]),

        # A51 Escape
        "Cheat Unlock: Complete A51 Escape": (agent_rules_perfect["Complete: A51 Escape - Agent"])
                                                | (special_agent_rules_perfect["Complete: A51 Escape - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: A51 Escape - Perfect Agent"]),

        # Air Base
        "Cheat Unlock: Complete Air Base": (agent_rules_perfect["Complete: Air Base - Agent"])
                                                | (special_agent_rules_perfect["Complete: Air Base - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Air Base - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Air Force One": (agent_rules_perfect["Complete: Air Force One - Agent"])
                                                | (special_agent_rules_perfect["Complete: Air Force One - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Air Force One - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Crash Site": (agent_rules_perfect["Complete: Crash Site - Agent"])
                                                | (special_agent_rules_perfect["Complete: Crash Site - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Crash Site - Perfect Agent"]),

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II": (agent_rules_perfect["Complete: Pelagic II - Agent"])
                                                | (special_agent_rules_perfect["Complete: Pelagic II - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Pelagic II - Perfect Agent"]),

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea": (agent_rules_perfect["Complete: Deep Sea - Agent"])
                                                | (special_agent_rules_perfect["Complete: Deep Sea - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Deep Sea - Perfect Agent"]),

        # CI Defense
        "Cheat Unlock: Complete CI Defense": (agent_rules_perfect["Complete: CI Defense - Agent"])
                                                | (special_agent_rules_perfect["Complete: CI Defense - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: CI Defense - Perfect Agent"]),

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship": (agent_rules_perfect["Complete: Attack Ship - Agent"])
                                                | (special_agent_rules_perfect["Complete: Attack Ship - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Attack Ship - Perfect Agent"]),

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins": (agent_rules_perfect["Complete: Skedar Ruins - Agent"])
                                                | (special_agent_rules_perfect["Complete: Skedar Ruins - Special Agent"])
                                                | (perfect_agent_rules_perfect["Complete: Skedar Ruins - Perfect Agent"]),
    }


    cheat_agent_rules_perfect = {
        # Extraction
        "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03": agent_rules_perfect["Complete: dD Extraction - Agent"],

        # G5 Building
        "Cheat Unlock: Complete G5 Building (Agent) in under 1:40": agent_rules_perfect["Complete: G5 Building - Agent"],

        # Escape
        "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50": agent_rules_perfect["Complete: A51 Escape - Agent"],

        # Crash Site
        "Cheat Unlock: Complete Crash Site (Agent) in under 2:50": agent_rules_perfect["Complete: Crash Site - Agent"],

        # CI Defense
        # "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": agent_rules_perfect["Complete: CI Defense - Agent"],
        "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                                & (HasAll("AR34", "RC-P120")
                                                                | (all_guns_filter & Has("RC-P120") & HAS_ANY_RIFLE)
                                                                | ((Has("RC-P120") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                                | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]) & HAS_ANY_WEAPON_TYPE)),

    }


    cheat_sp_agent_rules_perfect = {
        # Defection
        "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30": special_agent_rules_perfect["Complete: dD Defection - Special Agent"],

        # Villa
        "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30": special_agent_rules_perfect["Complete: Carrington Villa - Special Agent"],

        # Infiltration
        "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00": special_agent_rules_perfect["Complete: A51 Infiltration - Special Agent"],

        # Air Base
        "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11": special_agent_rules_perfect["Complete: Air Base - Special Agent"],

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07": special_agent_rules_perfect["Complete: Pelagic II - Special Agent"],

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17": special_agent_rules_perfect["Complete: Attack Ship - Special Agent"],
    }


    cheat_pf_agent_rules_perfect = {
        # Investigation
        "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30": perfect_agent_rules_perfect["Complete: dD Investigation - Perfect Agent"],

        # Chicago
        "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00": perfect_agent_rules_perfect["Complete: Chicago - Perfect Agent"] & Has("CamSpy"),

        # Rescue
        "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59": perfect_agent_rules_perfect["Complete: A51 Rescue - Perfect Agent"],

        # Air Force One
        "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55": perfect_agent_rules_perfect["Complete: Air Force One - Perfect Agent"],

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27": perfect_agent_rules_perfect["Complete: Deep Sea - Perfect Agent"],

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31": perfect_agent_rules_perfect["Complete: Skedar Ruins - Perfect Agent"],
    }


    agent_alternate_exits_perfect = {
        "Complete A51 Escape (Agent): UFO Escape": agent_rules_perfect["Complete: A51 Escape - Agent"],
        "Complete A51 Escape (Agent): Alternate Escape": agent_rules_perfect["Complete: A51 Escape - Agent"],
        "Complete Air Base (Agent): Shuttle Exit": agent_rules_perfect["Complete: Air Base - Agent"],
        "Complete Air Base (Agent): Ladder Exit": agent_rules_perfect["Complete: Air Base - Agent"],
    }


    special_agent_alternate_exits_perfect = {
        "Complete A51 Escape (Special Agent): UFO Escape": special_agent_rules_perfect["Complete: A51 Escape - Special Agent"],
        "Complete A51 Escape (Special Agent): Alternate Escape": special_agent_rules_perfect["Complete: A51 Escape - Special Agent"],
        "Complete Air Base (Special Agent): Shuttle Exit": special_agent_rules_perfect["Complete: Air Base - Special Agent"],
        "Complete Air Base (Special Agent): Ladder Exit": special_agent_rules_perfect["Complete: Air Base - Special Agent"],
    }


    perfect_agent_alternate_exits_perfect = {
        "Complete A51 Escape (Perfect Agent): UFO Escape": perfect_agent_rules_perfect["Complete: A51 Escape - Perfect Agent"],
        "Complete A51 Escape (Perfect Agent): Alternate Escape": perfect_agent_rules_perfect["Complete: A51 Escape - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Shuttle Exit": perfect_agent_rules_perfect["Complete: Air Base - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Ladder Exit": perfect_agent_rules_perfect["Complete: Air Base - Perfect Agent"],
    }


    if world.options.agent:
        add_rule(world, agent_rules_perfect)

        if world.options.alternate_exits:
            add_rule(world, agent_alternate_exits_perfect)

    if world.options.special_agent:
        add_rule(world, special_agent_rules_perfect)

        if world.options.alternate_exits:
            add_rule(world, special_agent_alternate_exits_perfect)

    if world.options.perfect_agent:
        add_rule(world, perfect_agent_rules_perfect)

        if world.options.alternate_exits:
            add_rule(world, perfect_agent_alternate_exits_perfect)

    if world.options.completion_cheats:
        if world.options.agent or world.options.special_agent or world.options.perfect_agent:
            add_rule(world, cheat_rules_perfect)

    if world.options.timed_cheats:
        if world.options.agent:
            add_rule(world, cheat_agent_rules_perfect)
        if world.options.special_agent:
            add_rule(world, cheat_sp_agent_rules_perfect)
        if world.options.perfect_agent:
            add_rule(world, cheat_pf_agent_rules_perfect)

    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent:
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 1"), agent_rules_perfect["Skedar Ruins - Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 2"), agent_rules_perfect["Skedar Ruins - Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 3"), agent_rules_perfect["Skedar Ruins - Agent Objective 3"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Agent"), agent_rules_perfect["Complete: Skedar Ruins - Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 1"), special_agent_rules_perfect["Skedar Ruins - Special Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 2"), special_agent_rules_perfect["Skedar Ruins - Special Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 3"), special_agent_rules_perfect["Skedar Ruins - Special Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 4"), special_agent_rules_perfect["Skedar Ruins - Special Agent Objective 4"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Special Agent"), special_agent_rules_perfect["Complete: Skedar Ruins - Special Agent"])
        
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 1"), perfect_agent_rules_perfect["Skedar Ruins - Perfect Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 2"), perfect_agent_rules_perfect["Skedar Ruins - Perfect Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 3"), perfect_agent_rules_perfect["Skedar Ruins - Perfect Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 4"), perfect_agent_rules_perfect["Skedar Ruins - Perfect Agent Objective 4"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 5"), perfect_agent_rules_perfect["Skedar Ruins - Perfect Agent Objective 5"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Perfect Agent"), perfect_agent_rules_perfect["Complete: Skedar Ruins - Perfect Agent"])

        if world.options.completion_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins"), cheat_rules_perfect["Cheat Unlock: Complete Skedar Ruins"])
        if world.options.timed_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"), cheat_pf_agent_rules_perfect["Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"])


def set_all_extra_location_rules(world: PerfectDarkWorld) -> None:
    weapon_training_rules = {
        "Firing Range: Falcon 2 - Bronze":
            Has("Falcon 2")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]),

        "Firing Range: Falcon 2 - Silver":
            Has("Falcon 2")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]),

        "Firing Range: Falcon 2 - Gold":
            Has("Falcon 2")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]),

        "Firing Range: Falcon 2 (Silencer) - Bronze":
            Has("Falcon 2 (Silencer)")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]),

        "Firing Range: Falcon 2 (Silencer) - Silver":
            Has("Falcon 2 (Silencer)")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]),

        "Firing Range: Falcon 2 (Silencer) - Gold":
            Has("Falcon 2 (Silencer)")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]),

        "Firing Range: Falcon 2 (Scope) - Bronze":
            Has("Falcon 2 (Scope)")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]),

        "Firing Range: Falcon 2 (Scope) - Silver":
            Has("Falcon 2 (Scope)")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]),

        "Firing Range: Falcon 2 (Scope) - Gold":
            Has("Falcon 2 (Scope)")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]),

        "Firing Range: MagSec 4 - Bronze":
            Has("MagSec 4")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]),

        "Firing Range: MagSec 4 - Silver":
            Has("MagSec 4")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]),

        "Firing Range: MagSec 4 - Gold":
            Has("MagSec 4")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]),

        "Firing Range: Mauler - Bronze":
            Has("Mauler")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]),

        "Firing Range: Mauler - Silver":
            Has("Mauler")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]),

        "Firing Range: Mauler - Gold":
            Has("Mauler")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]),

        "Firing Range: Phoenix - Bronze":
            Has("Phoenix")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"]),

        "Firing Range: Phoenix - Silver":
            Has("Phoenix")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"]),

        "Firing Range: Phoenix - Gold":
            Has("Phoenix")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"]),

        "Firing Range: DY357 Magnum - Bronze":
            Has("DY357 Magnum")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]),

        "Firing Range: DY357 Magnum - Silver":
            Has("DY357 Magnum")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]),

        "Firing Range: DY357 Magnum - Gold":
            Has("DY357 Magnum")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]),

        "Firing Range: DY357-LX - Bronze":
            Has("DY357-LX")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]),

        "Firing Range: DY357-LX - Silver":
            Has("DY357-LX")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]),

        "Firing Range: DY357-LX - Gold":
            Has("DY357-LX")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]),

        "Firing Range: CMP150 - Bronze":
            Has("CMP150")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]),

        "Firing Range: CMP150 - Silver":
            Has("CMP150")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]),

        "Firing Range: CMP150 - Gold":
            Has("CMP150")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]),

        "Firing Range: Cyclone - Bronze":
            Has("Cyclone")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]),

        "Firing Range: Cyclone - Silver":
            Has("Cyclone")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]),

        "Firing Range: Cyclone - Gold":
            Has("Cyclone")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]),

        "Firing Range: Callisto NTG - Bronze":
            Has("Callisto NTG")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Callisto NTG"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Callisto NTG"]),

        "Firing Range: Callisto NTG - Silver":
            Has("Callisto NTG")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Callisto NTG"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Callisto NTG"]),

        "Firing Range: Callisto NTG - Gold":
            Has("Callisto NTG")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Callisto NTG"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Callisto NTG"]),

        "Firing Range: RC-P120 - Bronze":
            Has("RC-P120", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]),

        "Firing Range: RC-P120 - Silver":
            Has("RC-P120", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]),

        "Firing Range: RC-P120 - Gold":
            Has("RC-P120", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]),

        "Firing Range: Laptop Gun - Bronze":
            Has("Laptop Gun")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]),

        "Firing Range: Laptop Gun - Silver":
            Has("Laptop Gun")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]),

        "Firing Range: Laptop Gun - Gold":
            Has("Laptop Gun")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]),


        "Firing Range: Dragon - Bronze":
            Has("Dragon")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]),

        "Firing Range: Dragon - Silver":
            Has("Dragon")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]),

        "Firing Range: Dragon - Gold":
            Has("Dragon")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]),

        "Firing Range: K7 Avenger - Bronze":
            Has("K7 Avenger", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]),

        "Firing Range: K7 Avenger - Silver":
            Has("K7 Avenger", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]),

        "Firing Range: K7 Avenger - Gold":
            Has("K7 Avenger", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]),

        "Firing Range: AR34 - Bronze":
            Has("AR34")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]),

        "Firing Range: AR34 - Silver":
            Has("AR34")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]),

        "Firing Range: AR34 - Gold":
            Has("AR34")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]),

        "Firing Range: SuperDragon - Bronze":
            Has("SuperDragon")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]),

        "Firing Range: SuperDragon - Silver":
            Has("SuperDragon")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]),

        "Firing Range: SuperDragon - Gold":
            Has("SuperDragon")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
            | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]),

        "Firing Range: Shotgun - Bronze":
            Has("Shotgun")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]),

        "Firing Range: Shotgun - Silver":
            Has("Shotgun")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]),

        "Firing Range: Shotgun - Gold":
            Has("Shotgun")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]),

        "Firing Range: Reaper - Bronze":
            Has("Reaper")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Reaper"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]),

        "Firing Range: Reaper - Silver":
            Has("Reaper")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Reaper"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]),

        "Firing Range: Reaper - Gold":
            Has("Reaper")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Reaper"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]),

        "Firing Range: Sniper Rifle - Bronze":
            Has("Sniper Rifle")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]),

        "Firing Range: Sniper Rifle - Silver":
            Has("Sniper Rifle")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]),

        "Firing Range: Sniper Rifle - Gold":
            Has("Sniper Rifle")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]),

        "Firing Range: FarSight XR-20 - Bronze":
            Has("FarSight XR-20", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]),

        "Firing Range: FarSight XR-20 - Silver":
            Has("FarSight XR-20", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]),

        "Firing Range: FarSight XR-20 - Gold":
            Has("FarSight XR-20", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]),

        "Firing Range: Devastator - Bronze":
            Has("Devastator", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]),

        "Firing Range: Devastator - Silver":
            Has("Devastator", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]),

        "Firing Range: Devastator - Gold":
            Has("Devastator", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]),

        "Firing Range: Rocket Launcher - Bronze":
            Has("Rocket Launcher")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]),

        "Firing Range: Rocket Launcher - Silver":
            Has("Rocket Launcher")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]),

        "Firing Range: Rocket Launcher - Gold":
            Has("Rocket Launcher")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]),

        "Firing Range: Slayer - Bronze":
            Has("Slayer")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]),

        "Firing Range: Slayer - Silver":
            Has("Slayer")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]),

        "Firing Range: Slayer - Gold":
            Has("Slayer")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]),

        "Firing Range: Combat Knife - Bronze":
            Has("Combat Knife")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Combat Knife"]),

        "Firing Range: Combat Knife - Silver":
            Has("Combat Knife")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Combat Knife"]),

        "Firing Range: Combat Knife - Gold":
            Has("Combat Knife")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Combat Knife"]),

        "Firing Range: Crossbow - Bronze":
            Has("Crossbow")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Crossbow"]),

        "Firing Range: Crossbow - Silver":
            Has("Crossbow")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Crossbow"]),

        "Firing Range: Crossbow - Gold":
            Has("Crossbow")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Crossbow"]),

        "Firing Range: Tranquilizer - Bronze":
            Has("Tranquilizer")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]),

        "Firing Range: Tranquilizer - Silver":
            Has("Tranquilizer")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]),

        "Firing Range: Tranquilizer - Gold":
            Has("Tranquilizer")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]),

        "Firing Range: Laser - Bronze":
            Has("Laser")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]),

        "Firing Range: Laser - Silver":
            Has("Laser")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]),

        "Firing Range: Laser - Gold":
            Has("Laser")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"])
            | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]),

        "Firing Range: Grenade - Bronze":
            Has("Grenade")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]),

        "Firing Range: Grenade - Silver":
            Has("Grenade")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]),

        "Firing Range: Grenade - Gold":
            Has("Grenade")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]),

        "Firing Range: Timed Mine - Bronze":
            Has("Timed Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]),

        "Firing Range: Timed Mine - Silver":
            Has("Timed Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]),

        "Firing Range: Timed Mine - Gold":
            Has("Timed Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]),

        "Firing Range: Proximity Mine - Bronze":
            Has("Proximity Mine")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]),

        "Firing Range: Proximity Mine - Silver":
            Has("Proximity Mine")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]),

        "Firing Range: Proximity Mine - Gold":
            Has("Proximity Mine")
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]),

        "Firing Range: Remote Mine - Bronze":
            Has("Remote Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]),

        "Firing Range: Remote Mine - Silver":
            Has("Remote Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]),

        "Firing Range: Remote Mine - Gold":
            Has("Remote Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]),
    }

    weapon_training_cheat_rules = {
        "Cheat Unlock: Get gold medals for Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)":
            HasAll("Falcon 2", "Falcon 2 (Silencer)", "Falcon 2 (Scope)", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]),

        "Cheat Unlock: Get gold medals for MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX":
            HasAll("MagSec 4", "Mauler", "Phoenix", "DY357 Magnum", "DY357-LX", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]),

        "Cheat Unlock: Get gold medals for CMP150, Cyclone, Callisto NTG, and RC-P120":
            HasAll("CMP150", "Cyclone", "Callisto NTG", "RC-P120", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]),

        "Cheat Unlock: Get gold medals for Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon":
            HasAll("Laptop Gun", "Dragon", "K7 Avenger", "AR34", "SuperDragon", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
            | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"])
                & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Cheat Unlock: Get gold medals for Shotgun, Sniper Rifle, Rocket Launcher, and Slayer":
            HasAll("Shotgun", "Sniper Rifle", "Rocket Launcher", "Slayer", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"])
                & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"])),

        "Cheat Unlock: Get gold medals for Timed Mine, Proximity Mine, and Remote Mine":
            HasAll("Timed Mine", "Proximity Mine", "Remote Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]),

        "Cheat Unlock: Get gold medals for FarSight XR-20, Crossbow, Combat Knife, and Grenade":
            HasAll("FarSight XR-20", "Crossbow", "Combat Knife", "Grenade", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])
                & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"])),

        "Cheat Unlock: Get gold medals for Tranquilizer, Reaper, and Devastator":
            HasAll("Tranquilizer", "Reaper", "Devastator", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"])
                & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"])),
    }

    strict_challenge_rules = {
        "Challenge 1": Has("Challenge 1")
                       & (HasAll("Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "Challenge 2": Has("Challenge 2")
                       & (HasAll("Combat Knife", "Falcon 2", "Cyclone", "Dragon", "Rocket Launcher")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"])),

        "Challenge 3": Has("Challenge 3")
                       & (HasAll("MagSec 4", "CMP150", "Timed Mine", "Dragon", "AR34")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"])),

        "Challenge 4": HasAll("Challenge 4", "Shield")
                       & (HasAll("MagSec 4", "CMP150", "Dragon", "K7 Avenger")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 5": HasAll("Challenge 5", "Shield")
                       & (HasAll("Cyclone", "Grenade", "AR34", "FarSight XR-20")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                       | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 6": HasAll("Challenge 6", "Briefcase", "Shield")
                       & (HasAll("CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 7": HasAll("Challenge 7", "Shield")
                       & (HasAll("Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"])),

        "Challenge 8": HasAll("Challenge 8", "Briefcase", "Shield")
                       & (HasAll("MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Challenge 9": Has("Challenge 9")
                       & (HasAll("Falcon 2", "DY357 Magnum", "Timed Mine", "Laptop Gun", "FarSight XR-20")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                       | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 10": HasAll("Challenge 10", "Data Uplink", "Shield")
                        & (HasAll("CMP150", "Cyclone", "Remote Mine", "AR34")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"])),

        "Challenge 11": HasAll("Challenge 11", "Shield")
                        & (HasAll("MagSec 4", "Tranquilizer", "Shotgun", "K7 Avenger")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 12": HasAll("Challenge 12", "Shield")
                        & (HasAll("Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Challenge 13": Has("Challenge 13")
                        & (HasAll("Falcon 2 (Silencer)", "Tranquilizer", "Laptop Gun", "Grenade", "Reaper")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"])),

        "Challenge 14": HasAll("Challenge 14", "Briefcase", "Cloaking Device")
                        & (HasAll("Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 15": HasAll("Challenge 15", "Briefcase", "Shield")
                        & (HasAll("MagSec 4", "Dragon", "Shotgun", "Devastator")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"])),

        "Challenge 16": HasAll("Challenge 16", "Shield")
                        & (HasAll("Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Challenge 17": HasAll("Challenge 17", "Shield")
                        & (HasAll("DY357 Magnum", "AR34", "Reaper", "Slayer")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"])),

        "Challenge 18": HasAll("Challenge 18", "Shield", "Cloaking Device")
                        & (HasAll("Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"])),

        "Challenge 19": HasAll("Challenge 19", "Shield", "Combat Boost")
                        & (HasAll("CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 20": HasAll("Challenge 20", "Shield")
                        & (HasAll("Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),

        "Challenge 21": HasAll("Challenge 21", "Data Uplink", "Cloaking Device")
                        & (HasAll("Mauler", "Reaper", "Shotgun", "Callisto NTG")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),

        "Challenge 22": HasAll("Challenge 22", "Briefcase", "Shield")
                        & (HasAll("Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 23": HasAll("Challenge 23", "Shield", "Combat Boost")
                        & (HasAll("MagSec 4", "Grenade", "Laptop Gun", "RC-P120")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"])),

        "Challenge 24": HasAll("Challenge 24", "Briefcase")
                        & (HasAll("CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"])),

        "Challenge 25": HasAll("Challenge 25", "Cloaking Device")
                        & (HasAll("Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 26": Has("Challenge 26")
                        & (HasAll("Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),

        "Challenge 27": HasAll("Challenge 27", "Data Uplink", "Shield")
                        & (HasAll("Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"])),

        "Challenge 28": HasAll("Challenge 28", "Briefcase")
                        & (HasAll("Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"])),

        "Challenge 29": Has("Challenge 29")
                        & (HasAll("Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"])),

        "Challenge 30": Has("Challenge 30")
                        & (HasAll("Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),
    }

    normal_challenge_rules = {
        "Challenge 1": Has("Challenge 1")
                       & (HasAny("Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"])),

        "Challenge 2": Has("Challenge 2")
                       & (Has("Rocket Launcher")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"])),

        "Challenge 3": HasAll("Challenge 3")
                       & (HasAll("Timed Mine", "Dragon", "AR34")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"])),

        "Challenge 4": HasAll("Challenge 4", "Shield")
                       & (Has("K7 Avenger")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 5": Has("Challenge 5")
                       & (Has("FarSight XR-20")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                       | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 6": HasAll("Challenge 6", "Briefcase")
                       & (HasAny("CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 7": Has("Challenge 7")
                       & (HasAny("Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
                       | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"])),

        "Challenge 8": HasAll("Challenge 8", "Briefcase")
                       & (HasAny("MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Challenge 9": Has("Challenge 9")
                       & (HasAll("FarSight XR-20", "Laptop Gun")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                       | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 10": HasAll("Challenge 10", "Data Uplink")
                        & (HasAny("CMP150", "Cyclone", "Remote Mine", "AR34")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"])),

        "Challenge 11": Has("Challenge 11")
                        & (HasAll("Shotgun", "Tranquilizer")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"])),

        "Challenge 12": Has("Challenge 12")
                        & (HasAny("Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Challenge 13": Has("Challenge 13")
                        & (Has("Tranquilizer")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"])),

        "Challenge 14": HasAll("Challenge 14", "Briefcase", "Cloaking Device")
                        & (HasAny("Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 15": HasAll("Challenge 15", "Briefcase")
                        & (Has("Devastator")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"])),

        "Challenge 16": HasAll("Challenge 16", "Shield")
                        & (HasAll("Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Challenge 17": HasAll("Challenge 17", "Shield")
                        & (HasAll("DY357 Magnum", "AR34", "Reaper", "Slayer")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"])),

        "Challenge 18": HasAll("Challenge 18", "Shield", "Cloaking Device")
                        & (HasAll("Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"])),

        "Challenge 19": HasAll("Challenge 19", "Shield")
                        & (HasAll("CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 20": HasAll("Challenge 20", "Shield")
                        & (HasAll("Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),

        "Challenge 21": HasAll("Challenge 21", "Data Uplink", "Cloaking Device")
                        & (HasAll("Mauler", "Reaper", "Shotgun", "Callisto NTG")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),

        "Challenge 22": HasAll("Challenge 22", "Briefcase", "Shield")
                        & (HasAll("Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"])),

        "Challenge 23": HasAll("Challenge 23", "Shield")
                        & (HasAll("MagSec 4", "Grenade", "Laptop Gun", "RC-P120")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"])),

        "Challenge 24": HasAll("Challenge 24", "Briefcase")
                        & (HasAll("CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"])),

        "Challenge 25": HasAll("Challenge 25", "Cloaking Device")
                        & (HasAll("Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])),

        "Challenge 26": Has("Challenge 26")
                        & (HasAll("Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),

        "Challenge 27": HasAll("Challenge 27", "Data Uplink", "Shield")
                        & (HasAll("Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"])),

        "Challenge 28": HasAll("Challenge 28", "Briefcase")
                        & (HasAll("Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"])),

        "Challenge 29": Has("Challenge 29")
                        & (HasAll("Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"])),

        "Challenge 30": Has("Challenge 30")
                        & (HasAll("Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"])),
    }

    hard_challenge_rules = {
        "Challenge 1": Has("Challenge 1")
                       & (HasAny("Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                       | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"])),

        "Challenge 2": Has("Challenge 2")
                       & (HasAny("Combat Knife", "Falcon 2", "Cyclone", "Dragon", "Rocket Launcher")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"])
                       | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Combat Knife"])),

        "Challenge 3": Has("Challenge 3")
                       & (HasAny("MagSec 4", "CMP150", "Timed Mine", "Dragon", "AR34")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
                       | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"])),

        "Challenge 4": Has("Challenge 4")
                       & (HasAny("MagSec 4", "CMP150", "Dragon", "K7 Avenger")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
                       | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"])),

        "Challenge 5": Has("Challenge 5")
                       & (HasAny("Cyclone", "Grenade", "AR34", "FarSight XR-20")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"])
                       | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"])),

        "Challenge 6": HasAll("Challenge 6", "Briefcase")
                       & (HasAny("CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"])
                       | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"])),

        "Challenge 7": Has("Challenge 7")
                       & (HasAny("Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"])
                       | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"])),

        "Challenge 8": HasAll("Challenge 8", "Briefcase")
                       & (HasAny("MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
                       | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"])),

        "Challenge 9": Has("Challenge 9")
                       & (HasAny("Falcon 2", "DY357 Magnum", "Timed Mine", "Laptop Gun", "FarSight XR-20")
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                       | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 10": HasAll("Challenge 10", "Data Uplink")
                        & (HasAny("CMP150", "Cyclone", "Remote Mine", "AR34")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["CMP150"])),

        "Challenge 11": Has("Challenge 11")
                        & (HasAny("MagSec 4", "Tranquilizer", "Shotgun", "K7 Avenger")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"])),

        "Challenge 12": Has("Challenge 12")
                        & (HasAny("Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"])),

        "Challenge 13": Has("Challenge 13")
                        & (HasAny("Falcon 2 (Silencer)", "Tranquilizer", "Laptop Gun", "Grenade", "Reaper")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"])),

        "Challenge 14": HasAll("Challenge 14", "Briefcase")
                        & (HasAny("Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"])),

        "Challenge 15": HasAll("Challenge 15", "Briefcase")
                        & (HasAny("MagSec 4", "Dragon", "Shotgun", "Devastator")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"])),

        "Challenge 16": Has("Challenge 16")
                        & (HasAny("Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 17": Has("Challenge 17")
                        & (HasAny("DY357 Magnum", "AR34", "Reaper", "Slayer")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"])),

        "Challenge 18": Has("Challenge 18")
                        & (HasAny("Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"])),

        "Challenge 19": Has("Challenge 19")
                        & (HasAny("CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"])),

        "Challenge 20": Has("Challenge 20")
                        & (HasAny("Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 21": HasAll("Challenge 21", "Data Uplink")
                        & (HasAny("Mauler", "Reaper", "Shotgun", "Callisto NTG")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"])),

        "Challenge 22": HasAll("Challenge 22", "Briefcase")
                        & (HasAny("Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Crossbow"])),

        "Challenge 23": Has("Challenge 23")
                        & (HasAny("MagSec 4", "Grenade", "Laptop Gun", "RC-P120")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"])),

        "Challenge 24": HasAll("Challenge 24", "Briefcase")
                        & (HasAny("CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"])),

        "Challenge 25": Has("Challenge 25")
                        & (HasAny("Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["N-Bomb"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["N-Bomb"])),

        "Challenge 26": Has("Challenge 26")
                        & (HasAny("Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 27": HasAll("Challenge 27", "Data Uplink")
                        & (HasAny("Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 28": HasAll("Challenge 28", "Briefcase")
                        & (HasAny("Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 29": Has("Challenge 29")
                        & (HasAny("Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),

        "Challenge 30": Has("Challenge 30")
                        & (HasAny("Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"])),
    }

    def location_count(state: CollectionState) -> int:
        completable_locations = 0

        for x in range(1, 31):
            challenge_name = f"Challenge {x}"
            if challenge_name not in world.options.excluded_challenges \
                    and world.get_location(f"Complete: {challenge_name}").can_reach(state):
                completable_locations += 1

        return completable_locations

    can_complete_one_challenge = lambda state: (location_count(state) >= 1)
    can_complete_two_challenges = lambda state: (location_count(state) >= 2)
    can_complete_three_challenges = lambda state: (location_count(state) >= 3)
    can_complete_four_challenges = lambda state: (location_count(state) >= 4)
    can_complete_five_challenges = lambda state: (location_count(state) >= 5)
    can_complete_six_challenges = lambda state: (location_count(state) >= 6)
    can_complete_seven_challenges = lambda state: (location_count(state) >= 7)
    can_complete_eight_challenges = lambda state: (location_count(state) >= 8)
    can_complete_nine_challenges = lambda state: (location_count(state) >= 9)
    can_complete_ten_challenges = lambda state: (location_count(state) >= 10)
    can_complete_eleven_challenges = lambda state: (location_count(state) >= 11)
    can_complete_twelve_challenges = lambda state: (location_count(state) >= 12)
    can_complete_thirteen_challenges = lambda state: (location_count(state) >= 13)
    can_complete_fourteen_challenges = lambda state: (location_count(state) >= 14)
    can_complete_fifteen_challenges = lambda state: (location_count(state) >= 15)
    can_complete_sixteen_challenges = lambda state: (location_count(state) >= 16)
    can_complete_seventeen_challenges = lambda state: (location_count(state) >= 17)
    can_complete_eighteen_challenges = lambda state: (location_count(state) >= 18)
    can_complete_nineteen_challenges = lambda state: (location_count(state) >= 19)
    can_complete_twenty_challenges = lambda state: (location_count(state) >= 20)
    can_complete_twenty_one_challenges = lambda state: (location_count(state) >= 21)
    can_complete_twenty_two_challenges = lambda state: (location_count(state) >= 22)
    # can_complete_twenty_three_challenges = lambda state: (location_count(state) >= 23)
    can_complete_twenty_four_challenges = lambda state: (location_count(state) >= 24)

    complete_challenge_unlock_rules = {
        # "Complete Challenges: Unused First Unlock": can_complete_one_challenge,
        "Complete 1 Challenge: FarSight XR-20 Unlock": can_complete_one_challenge,
        "Complete 7 Challenges: Tranquilizer Unlock": can_complete_seven_challenges,
        "Complete 4 Challenges: SuperDragon Unlock": can_complete_four_challenges,
        "Complete 13 Challenges: Slayer Unlock": can_complete_thirteen_challenges,
        "Complete 3 Challenges: Falcon 2 (Silencer) Unlock": can_complete_three_challenges,
        "Complete 8 Challenges: Falcon 2 (Scope) Unlock": can_complete_eight_challenges,
        "Complete 16 Challenges: Mauler Unlock": can_complete_sixteen_challenges,
        "Complete 14 Challenges: Phoenix Unlock": can_complete_fourteen_challenges,
        "Complete 20 Challenges: DY357-LX Unlock": can_complete_twenty_challenges,
        "Complete 17 Challenges: Callisto NTG Unlock": can_complete_seventeen_challenges,
        "Complete 5 Challenges: Laptop Gun Unlock": can_complete_five_challenges,
        # "Complete Challenges: K7 Avenger Unlock": can_complete_one_challenge,
        "Complete 19 Challenges: RC-P120 Unlock": can_complete_nineteen_challenges,
        "Complete 2 Challenges: Shotgun Unlock": can_complete_two_challenges,
        "Complete 9 Challenges: Reaper Unlock": can_complete_nine_challenges,
        "Complete 11 Challenges: Devastator Unlock": can_complete_eleven_challenges,
        "Complete 18 Challenges: Crossbow Unlock": can_complete_eighteen_challenges,
        "Complete 21 Challenges: N-Bomb Unlock": can_complete_twenty_one_challenges,
        "Complete 12 Challenges: Proximity Mine Unlock": can_complete_twelve_challenges,
        "Complete 6 Challenges: Remote Mine Unlock": can_complete_six_challenges,
        # "Complete Challenges: X-Ray Scanner Unlock": can_complete_one_challenge,
        # "Complete Challenges: Shield Unlock": can_complete_one_challenge,
        "Complete 10 Challenges: Cloaking Device Unlock": can_complete_ten_challenges,
        "Complete 15 Challenges: Combat Boost Unlock": can_complete_fifteen_challenges,
        "Complete 7 Challenges: Hard Bot Difficulty Unlock": can_complete_seven_challenges,
        "Complete 12 Challenges: Perfect Bot Difficulty Unlock": can_complete_twelve_challenges,
        # "Complete Challenges: Unused 1B Unlock": can_complete_one_challenge,
        "Complete 22 Challenges: Dark Bot Difficulty Unlock": can_complete_twenty_two_challenges,
        "Complete 8 Challenges: Slow Motion Unlock": can_complete_eight_challenges,
        "Complete 3 Challenges: One-Hit Kills Unlock": can_complete_three_challenges,
        # "Complete Challenges: King of the Hill Unlock": can_complete_one_challenge,
        "Complete 2 Challenges: Hold the Briefcase Unlock": can_complete_two_challenges,
        "Complete 4 Challenges: Capture the Case Unlock": can_complete_four_challenges,
        # "Complete Challenges: Unused 22 Unlock": can_complete_one_challenge,
        "Complete 17 Challenges: Car Park Unlock": can_complete_seventeen_challenges,
        "Complete 1 Challenge: Complex Unlock": can_complete_one_challenge,
        "Complete 3 Challenges: Warehouse Unlock": can_complete_three_challenges,
        "Complete 5 Challenges: Ravine Unlock": can_complete_five_challenges,
        "Complete 6 Challenges: Temple Unlock": can_complete_six_challenges,
        "Complete 9 Challenges: G5 Building Unlock": can_complete_nine_challenges,
        "Complete 11 Challenges: Grid Unlock": can_complete_eleven_challenges,
        "Complete 12 Challenges: Felicity Unlock": can_complete_twelve_challenges,
        "Complete 14 Challenges: Villa Unlock": can_complete_fourteen_challenges,
        "Complete 16 Challenges: Sewers Unlock": can_complete_sixteen_challenges,
        "Complete 22 Challenges: Ruins Unlock": can_complete_twenty_two_challenges,
        "Complete 18 Challenges: Base Unlock": can_complete_eighteen_challenges,
        # "Complete Challenges: Unused 2F Unlock": can_complete_one_challenge,
        "Complete 20 Challenges: Fortress Unlock": can_complete_twenty_challenges,
        # "Complete Challenges: Unused 31 Unlock": can_complete_one_challenge,
        "Complete 1 Challenge: dataDyne Female Guard Unlock": can_complete_one_challenge,
        "Complete 2 Challenges: Office Suit and Office Casual Unlock": can_complete_two_challenges,
        "Complete 4 Challenges: Carrington Villa Outfits Unlock": can_complete_four_challenges,
        "Complete 5 Challenges: Trent Unlock": can_complete_five_challenges,
        "Complete 5 Challenges: NSA Lackey Unlock": can_complete_five_challenges,
        "Complete 6 Challenges: G5 Building Outfits Unlock": can_complete_six_challenges,
        "Complete 7 Challenges: Mr. Blonde Unlock": can_complete_seven_challenges,
        "Complete 9 Challenges: CIA Agent and FBI Agent Unlock": can_complete_nine_challenges,
        "Complete 10 Challenges: A51 Infiltration Outfits Unlock": can_complete_ten_challenges,
        "Complete 11 Challenges: Lab Technician Outfits Unlock": can_complete_eleven_challenges,
        "Complete 12 Challenges: Biotechnician Unlock": can_complete_twelve_challenges,
        "Complete 14 Challenges: Elvis and Maian Soldier Unlock": can_complete_fourteen_challenges,
        "Complete 17 Challenges: Alaskan Guard Unlock": can_complete_seventeen_challenges,
        "Complete 16 Challenges: Air Force One Outfits Unlock": can_complete_sixteen_challenges,
        "Complete 7 Challenges: 8 Bots and Dinner Jacket Outfits Unlock": can_complete_seven_challenges,
        "Complete 18 Challenges: Party Frock, Party (Ripped), Evening Wear, and President Unlock": can_complete_eighteen_challenges,
        "Complete 19 Challenges: President's Clone Unlock": can_complete_nineteen_challenges,
        "Complete 18 Challenges: Presidential Security Unlock": can_complete_eighteen_challenges,
        "Complete 19 Challenges: NSA Bodyguard Unlock": can_complete_nineteen_challenges,
        "Complete 24 Challenges: Pelagic II Outfits Unlock": can_complete_twenty_four_challenges,
        "Complete 8 Challenges: Joanna Trench Unlock": can_complete_eight_challenges,
        # "Complete Challenges: Unused Jo Snow Unlock": can_complete_one_challenge,
        # "Complete Challenges: Unused 48 Unlock": can_complete_one_challenge,
        # "Complete Challenges: Unused 49 Unlock": can_complete_one_challenge,
        "Complete 17 Challenges: Joanna Arctic Unlock": can_complete_seventeen_challenges,
        # "Complete Challenges: Unused 4B Unlock": can_complete_one_challenge,
        # "Complete Challenges: Jonathan Unlock": can_complete_one_challenge,
        "Complete 12 Challenges: Pop a Cap Unlock": can_complete_twelve_challenges,
        "Complete 6 Challenges: Hacker Central Unlock": can_complete_six_challenges,
        # "Complete Challenges: Laser Unlock": can_complete_one_challenge,
    }

    has_defection = Has("dD Defection - Agent") | Has("dD Defection - Special Agent") | Has("dD Defection - Perfect Agent")
    has_investigation = Has("dD Investigation - Agent") | Has("dD Investigation - Special Agent") | Has("dD Investigation - Perfect Agent")
    has_extraction = Has("dD Extraction - Agent") | Has("dD Extraction - Special Agent") | Has("dD Extraction - Perfect Agent")
    has_villa = Has("Carrington Villa - Agent") | Has("Carrington Villa - Special Agent") | Has("Carrington Villa - Perfect Agent")
    has_chicago = Has("Chicago - Agent") | Has("Chicago - Special Agent") | Has("Chicago - Perfect Agent")
    has_g5 = Has("G5 Building - Agent") | Has("G5 Building - Special Agent") | Has("G5 Building - Perfect Agent")
    has_infiltration = Has("A51 Infiltration - Agent") | Has("A51 Infiltration - Special Agent") | Has("A51 Infiltration - Perfect Agent")
    has_rescue = Has("A51 Rescue - Agent") | Has("A51 Rescue - Special Agent") | Has("A51 Rescue - Perfect Agent")
    has_escape = Has("A51 Escape - Agent") | Has("A51 Escape - Special Agent") | Has("A51 Escape - Perfect Agent")
    has_air_base = Has("Air Base - Agent") | Has("Air Base - Special Agent") | Has("Air Base - Perfect Agent")
    has_air_force_one = Has("Air Force One - Agent") | Has("Air Force One - Special Agent") | Has("Air Force One - Perfect Agent")
    has_crash_site = Has("Crash Site - Agent") | Has("Crash Site - Special Agent") | Has("Crash Site - Perfect Agent")
    has_pelagic = Has("Pelagic II - Agent") | Has("Pelagic II - Special Agent") | Has("Pelagic II - Perfect Agent")
    has_deep_sea = Has("Deep Sea - Agent") | Has("Deep Sea - Special Agent") | Has("Deep Sea - Perfect Agent")
    has_defense = Has("CI Defense - Agent") | Has("CI Defense - Special Agent") | Has("CI Defense - Perfect Agent")
    has_attack_ship = Has("Attack Ship - Agent") | Has("Attack Ship - Special Agent") | Has("Attack Ship - Perfect Agent")
    has_skedar_ruins = Has("Skedar Ruins - Agent") | Has("Skedar Ruins - Special Agent") | Has("Skedar Ruins - Perfect Agent") | Has("Skedar Ruins")
    has_mbr = Has("Mr. Blonde's Revenge - Agent") | Has("Mr. Blonde's Revenge - Special Agent") | Has("Mr. Blonde's Revenge - Perfect Agent")
    has_maian_sos = Has("Maian SOS - Agent") | Has("Maian SOS - Special Agent") | Has("Maian SOS - Perfect Agent")

    has_weapon_for_defection = (HasAny("Falcon 2 (Silencer)", "CMP150")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_investigation = (HasAny("Falcon 2", "CMP150")
                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                    | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_extraction = (HasAny("Falcon 2 (Scope)", "CMP150")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_villa = (HasAny("Laptop Gun", "CMP150", "Sniper Rifle")
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_chicago = (HasAny("Falcon 2 (Scope)", "CMP150")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_g5 = (HasAny("Falcon 2 (Silencer)", "CMP150")
                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                        | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_infiltration = (HasAny("Falcon 2", "CMP150")
                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                    | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_rescue = (HasAny("Falcon 2 (Silencer)", "Dragon")
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_escape = (Has("Falcon 2 (Scope)")
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_crash_site = (HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_pelagic = (HasAny("Falcon 2 (Silencer)", "Laptop Gun")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_deep_sea = (HasAny("Falcon 2 (Scope)", "Shotgun")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_defense = (Has("AR34")
                                | (all_guns_filter & HAS_ANY_RIFLE)
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                                | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))

    has_weapon_for_attack_ship = (HasAll("Combat Knife", "Mauler", "AR34")
                                    | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                    | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_mbr = (Has("Mauler")
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_maian_sos = (HasAll("Falcon 2", "Dragon")
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_falcon2 = (Has("Falcon 2")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                    | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]))

    has_falcon2_silencer = (Has("Falcon 2 (Silencer)")
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"])
                            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]))

    has_falcon2_scope = (Has("Falcon 2 (Scope)")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]))

    has_magsec4 = (Has("MagSec 4")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"])
                    | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]))

    has_mauler = (Has("Mauler")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"])
                        | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]))

    has_phoenix = (Has("Phoenix")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"])
                    | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"]))

    has_dy357 = (Has("DY357 Magnum")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"])
                    | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]))

    has_dy357lx = (Has("DY357-LX")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
                    | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]))

    has_cmp150 = (Has("CMP150")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]))

    has_cyclone = (Has("Cyclone")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]))

    has_laptop_gun = (Has("Laptop Gun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"])
                        | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]))

    has_dragon = (Has("Dragon")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])
                        | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))

    has_shotgun = (Has("Shotgun")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                    | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]))

    has_sniper_rifle = (Has("Sniper Rifle")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]))

    has_devastator = (Has("Devastator", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"])
                            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]))

    has_rocket_launcher = (Has("Rocket Launcher")
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
                            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]))

    has_slayer = (Has("Slayer")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])
                    | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]))

    has_crossbow = (Has("Crossbow")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"])
                    | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Crossbow"]))

    has_grenade = (Has("Grenade")
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"])
                    | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]))

    has_proxy_mine = (Has("Proximity Mine")
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"])
                            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]))

    has_remote_mine = (Has("Remote Mine")
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                                | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]))

    has_nbomb = (Has("N-Bomb")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["N-Bomb"])
                        | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["N-Bomb"]))

    has_psychosis_gun = (Has("Psychosis Gun")
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Psychosis Gun"])
                        | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Psychosis Gun"]))

    pickupsanity_rules = {
        "dD Defection: Pick up double Falcon 2 (silencer) from guard in the room next to the office worker's office": has_defection
                                                                                                                      & has_falcon2_silencer,

        "dD Defection: Pick up Laptop Gun in the room that the office worker hides in": has_defection
                                                                                        & has_falcon2_silencer
                                                                                        & has_laptop_gun,

        "dD Defection: Pick up Falcon 2 (silencer) on the right side of the room that the office worker hides in": has_defection
                                                                                                                   & has_falcon2_silencer,

        "dD Defection: Pick up Falcon 2 (silencer) on the left side of the room that the office worker hides in": has_defection
                                                                                                                  & has_falcon2_silencer,

        "dD Defection: Pick up tiny ammo box on the desk in the corner room with 4 windows (floor below Cassandra's office)": has_defection
                                                                                                                              & has_weapon_for_defection,

        "dD Defection: Pick up tiny ammo box on the desk in the room next to the computer room (floor below Cassandra's office)": has_defection 
                                                                                                                                  & has_weapon_for_defection,

        "dD Defection: Pick up tiny ammo box on the desk in the room next to the room the office worker hides in (2nd floor below Cassandra's office)": has_defection 
                                                                                                                                                        & has_weapon_for_defection,

        "dD Defection: Pick up tiny ammo box on the desk in room across the elevator (2nd floor below Cassandra's office)": has_defection 
                                                                                                                            & has_weapon_for_defection,

        "dD Defection: Pick up Falcon 2 (silencer) on the desk in the corner room (2nd floor below Cassandra's office)": has_defection 
                                                                                                                         & has_weapon_for_defection,

        "dD Defection: Pick up tiny ammo box under the stairs that leads to the 2nd floor below Cassandra's office": has_defection 
                                                                                                                     & has_weapon_for_defection,

        "dD Defection: Pick up right CMP150 behind the front desk": has_defection
                                                                    & has_cmp150
                                                                    & has_weapon_for_defection,

        "dD Defection: Pick up left CMP150 behind the front desk": has_defection
                                                                   & has_cmp150
                                                                   & has_weapon_for_defection,

        "dD Investigation: Pick up left ammo box in the room above the K7 Avenger guard": has_investigation
                                                                                          & has_weapon_for_investigation,

        "dD Investigation: Pick up right ammo box in the room above the K7 Avenger guard": has_investigation
                                                                                           & has_weapon_for_investigation,

        "dD Investigation: Pick up left ammo box in the room with the Night Vision": has_investigation
                                                                                     & has_weapon_for_investigation,

        "dD Investigation: Pick up right ammo box in the room with the Night Vision": has_investigation 
                                                                                      & has_weapon_for_investigation,

        "dD Investigation: Pick up first CMP150 on the table in the room past the laser grids": has_investigation
                                                                                                & has_cmp150
                                                                                                & has_weapon_for_investigation,

        "dD Investigation: Pick up second CMP150 on the table in the room past the laser grids": has_investigation
                                                                                                 & has_cmp150
                                                                                                 & has_weapon_for_investigation,

        "dD Investigation: Pick up left CMP150 in the secret weapons compartment": has_investigation
                                                                                   & Has("CamSpy")
                                                                                   & has_cmp150
                                                                                   & has_weapon_for_investigation,

        "dD Investigation: Pick up right CMP150 in the secret weapons compartment": has_investigation
                                                                                    & Has("CamSpy")
                                                                                    & has_cmp150
                                                                                    & has_weapon_for_investigation,

        "dD Investigation: Pick up Proximity Mine behind the radioactive isotope": has_investigation
                                                                                   & has_proxy_mine
                                                                                   & has_weapon_for_investigation,
        
        "dD Extraction: Pick up DY357 Magnum from the fifth guard after defeating the first five guards without being seen": has_extraction 
                                                                                                                             & has_dy357 
                                                                                                                             & has_weapon_for_extraction,

        "dD Extraction: Pick up the Rocket Launcher in the room outside Cassandra's office": has_extraction 
                                                                                             & has_rocket_launcher 
                                                                                             & has_weapon_for_extraction,

        "dD Extraction: Pick up Grenade on Cassandra's desk": has_extraction
                                                              & HAS_CASS_OFFICE_KEY
                                                              & has_grenade
                                                              & has_weapon_for_extraction,

        "dD Extraction: Pick up Dragon in the hidden room near Cassandra's office": has_extraction
                                                                                    & HAS_CASS_OFFICE_KEY
                                                                                    & (has_grenade | has_rocket_launcher)
                                                                                    & has_dragon
                                                                                    & has_weapon_for_extraction,

        "dD Extraction: Pick up first rocket ammo box on the roof": has_extraction 
                                                                    & has_rocket_launcher 
                                                                    & has_weapon_for_extraction,

        "dD Extraction: Pick up second rocket ammo box on the roof": has_extraction 
                                                                     & has_rocket_launcher 
                                                                     & has_weapon_for_extraction,
    
        "Carrington Villa: Pick up Devastator hidden in crate near the helipad": has_villa
                                                                                 & has_devastator
                                                                                 & has_weapon_for_villa,

        "Carrington Villa: Pick up first ammo box hidden in crate leading to the observatory": has_villa
                                                                                               & has_weapon_for_villa,

        "Carrington Villa: Pick up second ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,

        "Carrington Villa: Pick up third ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,

        "Carrington Villa: Pick up fourth ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,

        "Carrington Villa: Pick up fifth ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,

        "Carrington Villa: Pick up sixth ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,

        "Carrington Villa: Pick up seventh ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,
        
        "Carrington Villa: Pick up eighth ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,
        
        "Carrington Villa: Pick up ninth ammo box hidden in crate leading to the observatory": has_villa & has_weapon_for_villa,
        
        "Carrington Villa: Pick up double CMP150 dropped from the sniper near the helipad in under 38 seconds": has_villa 
                                                                                                                & has_cmp150
                                                                                                                & has_weapon_for_villa,
            
        "Chicago: Pick up BombSpy hidden in the dumpster": has_chicago & Has("CamSpy") & has_weapon_for_chicago,

        "Chicago: Pick up double Falcon 2 (scope) inside the Pond Punk": has_chicago 
                                                                         & has_falcon2_scope 
                                                                         & has_weapon_for_chicago,
    
        "G5 Building: Pick up Crossbow after knocking out the first two guards": has_g5 & has_crossbow,
    
        "A51 Infiltration: Pick up Rocket Launcher in the mine field": has_infiltration 
                                                                       & has_rocket_launcher 
                                                                       & has_weapon_for_infiltration,
        
        "A51 Rescue: Pick up Phoenix after knocking out technician in A51 Infiltration then getting them to open the door to the right of the first elevator": has_rescue
                                                                                                                                                               & has_phoenix
                                                                                                                                                               & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                                                                                                                               & has_weapon_for_rescue
                                                                                                                                                               & has_infiltration 
                                                                                                                                                               & has_weapon_for_infiltration,

        "A51 Rescue: Pick up Falcon 2 (silencer) hidden in barrel under the stack of the crates": has_rescue
                                                                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                                                                  & has_falcon2_silencer,
        
        "A51 Escape: Pick up double Falcon 2 (scope) in the room where the two biotechnicians are in": has_escape
                                                                                                       & has_falcon2_scope,
        
        "A51 Escape: Pick up Remote Mine in the room before the secret hangar after moving Elvis to safety within 36 seconds": has_escape
                                                                                                                               & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                                               & has_remote_mine
                                                                                                                               & has_weapon_for_escape,
    
        "Air Base: Pick up double DY357 Magnum after knocking out the three NSA Lackeys": has_air_base
                                                                                          & has_dy357
                                                                                          & Has("Stewardess Disguise")
                                                                                          & (HasAny("Crossbow", "CamSpy")
                                                                                          | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base: Pick up Proximity Mine past the cave": has_air_base
                                                          & has_proxy_mine
                                                          & (HasAny("Crossbow", "CamSpy")
                                                          | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),
        
        "Air Force One: Pick up Cyclone in the small room to the right of the stairs": has_air_force_one
                                                                                       & HAS_AFO_RIGHT_KEY
                                                                                       & has_cyclone,

        "Air Force One: Pick up Cyclone in the small room to the left of the stairs": has_air_force_one 
                                                                                      & HAS_AFO_LEFT_KEY
                                                                                      & has_cyclone,
    
        # "Crash Site: Pick up DY357-LX from Trent": 1,
        
        "Crash Site: Get Proximity Mine from Elvis before completing any objective": has_crash_site
                                                                                     & has_proxy_mine
                                                                                     & has_weapon_for_crash_site,
    
        "Pelagic II: Pick up double Falcon 2 (silencer) dropped by the guard past the fourth door from the start of the mission without setting off the alarm": has_pelagic
                                                                                                                                                                     & has_falcon2_silencer,
    
        "Deep Sea: Pick up Proximity Mine dropped by guard on the far left from the dead Skedar before Elvis gets them": has_deep_sea
                                                                                                                         & has_proxy_mine
                                                                                                                         & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=True)
                                                                                                                         & has_weapon_for_deep_sea,
        
        "Deep Sea: Pick up Shotgun next to the Shield on the left path from the first teleportal": has_deep_sea
                                                                                                   & has_shotgun
                                                                                                   & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=True)
                                                                                                   & has_weapon_for_deep_sea,
    
        "CI Defense: Pick up Devastator in the Info Room after saving most of the hostages": has_defense
                                                                                             & has_devastator
                                                                                             & has_weapon_for_defense,
        
        "Attack Ship: Pick up double Mauler in the final room from the Skedar on top of the bridge": has_attack_ship
                                                                                                     & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                                                                     & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                     & has_mauler
                                                                                                     & has_weapon_for_attack_ship,

        "Attack Ship: Pick up Slayer in the room straight ahead from the lift you take with Elvis": has_attack_ship
                                                                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                    & has_slayer
                                                                                                    & has_weapon_for_attack_ship,
        
        "Skedar Ruins: Pick up double Phoenix near the gap after blowing up the two pillars that didn't need the target amplifier": has_skedar_ruins
                                                                                                                                    & has_phoenix
                                                                                                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                                                                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                                                    & ((HasAny("Falcon 2 (Scope)", "Callisto NTG") & Has("Devastator"))
                                                                                                                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1) & HasFromList(*EXPLOSIVE_LIST, count=1))
                                                                                                                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                                                                                                    | (HAS_ANY_WEAPON_TYPE & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))),
        
        "Mr. Blonde's Revenge: Pick up double CMP150 from guard near the elevator where you plant the bomb": has_mbr
                                                                                                             & has_cmp150
                                                                                                             & has_weapon_for_mbr
                                                                                                             & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up Laptop Gun in the room that the office worker hides in": has_mbr 
                                                                                                & has_laptop_gun
                                                                                                & has_weapon_for_mbr
                                                                                                & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up Falcon 2 on the right side of the room that the office worker hides in": has_mbr
                                                                                                                & has_falcon2 
                                                                                                                & has_weapon_for_mbr
                                                                                                                & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up Falcon 2 on the left side of the room that the office worker hides in": has_mbr 
                                                                                                               & has_falcon2 
                                                                                                               & has_weapon_for_mbr
                                                                                                               & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
        

        "Mr. Blonde's Revenge: Pick up tiny ammo box on the desk in the corner room with 4 windows (floor below Cassandra's office)": has_mbr
                                                                                                                                      & has_weapon_for_mbr
                                                                                                                                      & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up tiny ammo box on the desk in the room next to the computer room (floor below Cassandra's office)": has_mbr 
                                                                                                                                          & has_weapon_for_mbr
                                                                                                                                          & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up tiny ammo box on the desk in the room next to the room the office worker hides in (2nd floor below Cassandra's office)": has_mbr 
                                                                                                                                                                & has_weapon_for_mbr
                                                                                                                                                                & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
        
        "Mr. Blonde's Revenge: Pick up tiny ammo box on the desk in room across the elevator (2nd floor below Cassandra's office)": has_mbr 
                                                                                                                                    & has_weapon_for_mbr
                                                                                                                                    & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up Falcon 2 on the desk in the corner room (2nd floor below Cassandra's office)": has_mbr 
                                                                                                                      & has_weapon_for_mbr
                                                                                                                      & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
        
        "Mr. Blonde's Revenge: Pick up tiny ammo box under the stairs that leads to the 2nd floor below Cassandra's office": has_mbr 
                                                                                                                             & has_weapon_for_mbr
                                                                                                                             & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: Pick up right CMP150 behind the front desk": has_mbr
                                                                            & has_cmp150,
        
        "Mr. Blonde's Revenge: Pick up left CMP150 behind the front desk": has_mbr
                                                                           & has_cmp150,
        
    
        "Maian SOS: Pick up double DY357-LX from guard in the circular room with the exit": has_maian_sos 
                                                                                            & has_dy357lx 
                                                                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                            & has_weapon_for_maian_sos,

        "Maian SOS: Pick up Psychosis Gun on the desk near the start of the mission": has_maian_sos & has_psychosis_gun,
    }

    pickupsanity_rules_agent_only = {
        "dD Defection (Agent): Pick up Shield next to the elevator on the bottom floor": Has("dD Defection - Agent") 
                                                                                        & Has("Shield")
                                                                                        & has_weapon_for_defection,

        "dD Investigation (Agent): Pick up Shield on the crate in the room with the maintenance hatch": Has("dD Investigation - Agent") 
                                                                                                        & Has("Shield")
                                                                                                        & has_weapon_for_investigation,

        "dD Extraction (Agent): Pick up Shield inside the room to the left of the elevator (2nd floor under Cassandra's office)": Has("dD Extraction - Agent") 
                                                                                                                                  & Has("Shield")
                                                                                                                                  & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                                                                                                  & has_weapon_for_extraction,

        "Carrington Villa (Agent): Pick up Shield on the crate near the helipad": Has("Carrington Villa - Agent") 
                                                                                  & Has("Shield")
                                                                                  & has_weapon_for_villa,

        "Carrington Villa (Agent): Pick up Shield inside the bathroom": Has("Carrington Villa - Agent") 
                                                                        & Has("Shield")
                                                                        & has_weapon_for_villa,

        "Chicago (Agent): Pick up Shield in the grate under the taxi": Has("Chicago - Agent") & Has("Shield"),

        "G5 Building (Agent): Pick up Shield in the room before the room with the lasers": Has("G5 Building - Agent") 
                                                                                           & Has("Shield")
                                                                                           & HAS_G5_KEYS
                                                                                           & has_weapon_for_g5,

        "A51 Infiltration (Agent): Pick up Shield under the gun turret near the hoverbike": Has("A51 Infiltration - Agent") 
                                                                                            & Has("Shield")
                                                                                            & has_weapon_for_infiltration,

        "A51 Rescue (Agent): Pick up Shield from the guard past the bottom of the first elevator": Has("A51 Rescue - Agent") 
                                                                                                   & Has("Shield")
                                                                                                   & has_weapon_for_rescue,

        "A51 Escape (Agent): Pick up Shield dropped by the biotechnician in the circular room without the slope after moving Elvis to safety": Has("A51 Escape - Agent") 
                                                                                                                                               & Has("Shield")
                                                                                                                                               & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                                                               & has_weapon_for_escape,

        "Air Base (Agent): Pick up Shield dropped by NSA Lackey near the elevator door": Has("Air Base - Agent") 
                                                                                         & Has("Shield")
                                                                                         & Has("Stewardess Disguise")
                                                                                         & (HasAny("Crossbow", "CamSpy")
                                                                                         | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Force One (Agent): Pick up Shield in the small kitchen past the stairs that leads to the lower deck": Has("Air Force One - Agent") 
                                                                                                                   & Has("Shield"),

        "Crash Site (Agent): Pick up Shield near the crashed UFO": Has("Crash Site - Agent") 
                                                                   & Has("Shield"), 

        "Pelagic II (Agent): Pick up Shield on the helipad": Has("Pelagic II - Agent") 
                                                             & Has("Shield")
                                                             & has_weapon_for_pelagic,

        # "Deep Sea (Agent): Pick up Shield dropped from Sniper guard": Has("Deep Sea - Agent") 
        #                                                               & Has("Shield")
        #                                                               & has_weapon_for_deep_sea,

        "CI Defense (Agent): Pick up Shield on the second floor at the dead end opposite from Carrington's office": Has("CI Defense - Agent") 
                                                                                                                    & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                                                                                    & Has("Shield"),

        "Skedar Ruins (Agent): Pick up Shield behind the fallen pillar": HAS_SKEDAR_RUINS_AGENT
                                                                         & Has("Shield")
                                                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                         & (HasAny("Falcon 2 (Scope)", "Callisto NTG")
                                                                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                                         | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge (Agent): Pick up Shield next to the glass elevator on the bottom floor": Has("Mr. Blonde's Revenge - Agent") 
                                                                                                       & Has("Shield")
                                                                                                       & (has_weapon_for_mbr
                                                                                                       | Has("Cloaking Device")),
    }

    pickupsanity_rules_agent_or_special = {
        "dD Defection (Agent/Special): Pick up Shield from the guard on the floor below Cassandra's office": (Has("dD Defection - Agent") | Has("dD Defection - Special Agent")) 
                                                                                                             & Has("Shield")
                                                                                                             & has_weapon_for_defection,

        "dD Investigation (Agent/Special): Pick up Shield inside the glass enclosure in the room past the laser grids": (Has("dD Investigation - Agent") | Has("dD Investigation - Special Agent")) 
                                                                                                                        & Has("Shield")
                                                                                                                        & has_weapon_for_investigation,

        "Chicago (Agent/Special): Pick up Shield under the stairs that leads to the Pond Punk": (Has("Chicago - Agent") | Has("Chicago - Special Agent")) 
                                                                                                & Has("Shield")
                                                                                                & has_weapon_for_chicago,

        "G5 Building (Agent/Special): Pick up Shield on the stairs leading to the upper exit": (Has("G5 Building - Agent") | Has("G5 Building - Special Agent")) 
                                                                                               & Has("Shield")
                                                                                               & HAS_G5_KEYS
                                                                                               & has_weapon_for_g5,

        "A51 Infiltration (Agent/Special): Pick up Shield in the crawl space that leads to the mine field": (Has("A51 Infiltration - Agent") | Has("A51 Infiltration - Special Agent")) 
                                                                                                            & Has("Shield")
                                                                                                            & has_weapon_for_infiltration,

        "A51 Rescue (Agent/Special): Pick up Shield on the desk in the room next to the locked room at the top of the sloping corridor": (Has("A51 Rescue - Agent") | Has("A51 Rescue - Special Agent")) 
                                                                                                                                         & Has("Shield")
                                                                                                                                         & has_weapon_for_rescue,

        "A51 Escape (Agent/Special): Pick up Shield after unlocking the medical containment doors": (Has("A51 Escape - Agent") | Has("A51 Escape - Special Agent")) 
                                                                                                    & Has("Shield")
                                                                                                    & has_weapon_for_escape,

        "Air Base (Agent/Special): Pick up Shield in the safe with the flight plans": (Has("Air Base - Agent") | Has("Air Base - Special Agent")) 
                                                                                      & Has("Shield")
                                                                                      & Has("Stewardess Disguise")
                                                                                      & (HasAny("Crossbow", "CamSpy")
                                                                                      | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                                                      & (HasAll("Dragon", "K7 Avenger")
                                                                                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
                                                                                      | HAS_ANY_WEAPON_TYPE),

        "Air Force One (Agent/Special): Pick up Shield in the room with the piano": (Has("Air Force One - Agent") | Has("Air Force One - Special Agent")) & Has("Shield"),

        "Crash Site (Agent/Special): Pick up Shield behind the President's clone": (Has("Crash Site - Agent") | Has("Crash Site - Special Agent")) 
                                                                                   & Has("Shield")
                                                                                   & Has("Night Vision")
                                                                                   & has_weapon_for_crash_site,

        "Pelagic II (Agent/Special): Pick up Shield on the crate in the Moon Pool room": (Has("Pelagic II - Agent") | Has("Pelagic II - Special Agent")) 
                                                                                         & Has("Shield")
                                                                                         & has_weapon_for_pelagic,

        "Deep Sea (Agent/Special): Pick up Shield on the left path from the first teleportal": (Has("Deep Sea - Agent") | Has("Deep Sea - Special Agent")) 
                                                                                               & Has("Shield")
                                                                                               & has_weapon_for_deep_sea,

        "CI Defense (Agent/Special): Pick up Shield in the basement room with the two small hangar doors": (Has("CI Defense - Agent") | Has("CI Defense - Special Agent")) 
                                                                                                           & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                                                                           & Has("Shield")
                                                                                                           & has_weapon_for_defense,

        "Attack Ship (Agent/Special): Pick up Shield on table in the room to the right after taking the lift with Elvis": (Has("Attack Ship - Agent") | Has("Attack Ship - Special Agent")) 
                                                                                                                          & Has("Shield")
                                                                                                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                                                                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                                          & has_weapon_for_attack_ship,

        "Skedar Ruins (Agent/Special): Pick up Shield in the area past the gap to the right near the cheese": (HAS_SKEDAR_RUINS_AGENT | HAS_SKEDAR_RUINS_SP_AGENT) 
                                                                                                                & Has("Shield")
                                                                                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                                                & ((HasAny("Falcon 2 (Scope)", "Callisto NTG") & Has("Devastator"))
                                                                                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1) & HasFromList(*EXPLOSIVE_LIST, count=1))
                                                                                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                                                                                | (HAS_ANY_WEAPON_TYPE & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))),

        "Mr. Blonde's Revenge (Agent/Special): Pick up Shield from the guard on the floor below Cassandra's office": (Has("Mr. Blonde's Revenge - Agent") | Has("Mr. Blonde's Revenge - Special Agent")) 
                                                                                                                     & Has("Shield")
                                                                                                                     & has_weapon_for_mbr
                                                                                                                     & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
    }

    pickupsanity_rules_special_or_perfect = {
        "dD Investigation (Special/Perfect): Pick up left ammo box in the room with one scientist": (Has("dD Investigation - Special Agent") | Has("dD Investigation - Perfect Agent"))
                                                                                                    & has_weapon_for_investigation,
        
        "dD Investigation (Special/Perfect): Pick up right ammo box in the room with one scientist": (Has("dD Investigation - Special Agent") | Has("dD Investigation - Perfect Agent"))
                                                                                                     & has_weapon_for_investigation,

        "dD Investigation (Special/Perfect): Pick up left ammo box in the first room near the two scientists": (Has("dD Investigation - Special Agent") | Has("dD Investigation - Perfect Agent")) 
                                                                                                               & has_weapon_for_investigation,
        
        "dD Investigation (Special/Perfect): Pick up right ammo box in the first room near the two scientists": (Has("dD Investigation - Special Agent") | Has("dD Investigation - Perfect Agent")) 
                                                                                                                & has_weapon_for_investigation,

        "G5 Building (Special/Perfect): Pick up N-Bomb near the upper exit after placing Remote Mine on the upper exit in Chicago": (Has("G5 Building - Special Agent") | Has("G5 Building - Perfect Agent"))
                                                                                                                                    & HAS_G5_KEYS
                                                                                                                                    & has_nbomb
                                                                                                                                    & has_weapon_for_g5
                                                                                                                                    & (Has("Chicago - Special Agent") | Has("Chicago - Perfect Agent"))
                                                                                                                                    & Has("Remote Mine")
                                                                                                                                    & has_weapon_for_chicago,

        "A51 Infiltration (Special/Perfect): Pick up double MagSec 4 from A51 guard after placing comms rider": (Has("A51 Infiltration - Special Agent") | Has("A51 Infiltration - Perfect Agent"))
                                                                                                                & Has("Comms Rider")
                                                                                                                & has_magsec4
                                                                                                                & has_weapon_for_infiltration,
    }

    if world.options.weapon_training:
        add_rule(world, weapon_training_rules)

    if world.options.weapon_cheats:
        add_rule(world, weapon_training_cheat_rules)

    if has_challenges(world):
        if world.options.challenge_logic.value == ChallengeLogic.option_strict:
            add_challenge_rules(world, strict_challenge_rules)
        elif world.options.challenge_logic.value == ChallengeLogic.option_normal:
            add_challenge_rules(world, normal_challenge_rules)
        elif world.options.challenge_logic.value == ChallengeLogic.option_hard:
            add_challenge_rules(world, hard_challenge_rules)

        if world.options.multiplayer_unlocks:
            add_rule(world, complete_challenge_unlock_rules)

    if world.options.holotraining:
        ht7 = world.get_location("Holotraining 7: Live Combat 2")
        world.set_rule(ht7, Has("Falcon 2")
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]))

    if world.options.device_training:
        dt_data_uplink = world.get_location("Device Training: Data Uplink")
        world.set_rule(dt_data_uplink, Has("Data Uplink"))

        dt_ecm_mine = world.get_location("Device Training: ECM Mine")
        world.set_rule(dt_ecm_mine, Has("ECM Mine"))

        dt_camspy = world.get_location("Device Training: CamSpy")
        world.set_rule(dt_camspy, Has("CamSpy"))

        dt_night_vision = world.get_location("Device Training: Night Vision")
        world.set_rule(dt_night_vision, Has("Night Vision"))

        dt_door_decoder = world.get_location("Device Training: Door Decoder")
        world.set_rule(dt_door_decoder, Has("Door Decoder"))

        dt_rtracker = world.get_location("Device Training: R-Tracker")
        world.set_rule(dt_rtracker, HasAll("R-Tracker", "IR Scanner"))

        dt_ir_scanner = world.get_location("Device Training: IR Scanner")
        world.set_rule(dt_ir_scanner, Has("IR Scanner"))

        dt_xray_scanner = world.get_location("Device Training: X-Ray Scanner")
        world.set_rule(dt_xray_scanner, Has("X-Ray Scanner"))

        dt_disguise = world.get_location("Device Training: Disguise")
        world.set_rule(dt_disguise, Has("Stewardess Disguise"))

        dt_cloaking_device = world.get_location("Device Training: Cloaking Device")
        world.set_rule(dt_cloaking_device, (Has("Cloaking Device") & Has("Carrington", options=[npc_filter], filtered_resolution=True)))

    if world.options.pickupsanity:
        if world.options.agent or world.options.special_agent or world.options.perfect_agent:
            add_rule(world, pickupsanity_rules)

        if world.options.agent:
            add_rule(world, pickupsanity_rules_agent_only)

        if world.options.agent or world.options.special_agent:
            add_rule(world, pickupsanity_rules_agent_or_special)

        if world.options.perfect_agent:
            villa_sniper_rifle = world.get_location("Carrington Villa (Perfect Agent): Pick up Sniper Rifle in the bathroom")
            world.set_rule(villa_sniper_rifle, Has("Carrington Villa - Perfect Agent")
                                               & has_sniper_rifle
                                               & ((Has("Laptop Gun") | Has("CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False))
                                               | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                               | HAS_ANY_WEAPON_TYPE))

        if world.options.special_agent or world.options.perfect_agent:
            add_rule(world, pickupsanity_rules_special_or_perfect)


def set_completion_condition(world: PerfectDarkWorld) -> None:
    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        has_skedar_ruins = Has("Skedar Ruins - Agent") | Has("Skedar Ruins - Special Agent") | Has("Skedar Ruins - Perfect Agent") | Has("Skedar Ruins")

        has_items_for_skedar = (HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)))

        has_items_for_skedar_hard = (HasAll("R-Tracker", "Target Amplifier")
                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                    & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)))

        if world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_item:
            if world.options.mission_logic < MissionLogic.option_hard:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar)
            else:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar_hard)

        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_mission_stars:
            required_mission_stars = get_mission_stars(world)

            if world.options.mission_logic < MissionLogic.option_hard:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar
                                        & Has("Mission Star", count=required_mission_stars))
            else:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar_hard
                                        & Has("Mission Star", count=required_mission_stars))

        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_challenge_stars:
            required_challenge_stars = get_challenge_stars(world)

            if world.options.mission_logic < MissionLogic.option_hard:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar
                                        & Has("Challenge Star", count=required_challenge_stars))
            else:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar_hard
                                        & Has("Challenge Star", count=required_challenge_stars))
                    
        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_both_stars:
            required_mission_stars = get_mission_stars(world)
            required_challenge_stars = get_challenge_stars(world)

            if world.options.mission_logic < MissionLogic.option_hard:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar
                                        & Has("Mission Star", count=required_mission_stars)
                                        & Has("Challenge Star", count=required_challenge_stars))
            else:
                world.set_completion_rule(has_skedar_ruins
                                        & has_items_for_skedar_hard
                                        & Has("Mission Star", count=required_mission_stars)
                                        & Has("Challenge Star", count=required_challenge_stars))

    elif world.options.goal.value == Goal.option_complete_missions:
        required_mission_stars = get_mission_stars(world)
        world.set_completion_rule(Has("Mission Star", count=required_mission_stars))

    elif world.options.goal.value == Goal.option_complete_challenges:
        required_challenge_stars = get_challenge_stars(world)
        world.set_completion_rule(Has("Challenge Star", count=required_challenge_stars))

    elif world.options.goal.value == Goal.option_complete_both:
        required_mission_stars = get_mission_stars(world)
        required_challenge_stars = get_challenge_stars(world)
        world.set_completion_rule(Has("Mission Star", count=required_mission_stars) & Has("Challenge Star", count=required_challenge_stars))


def get_mission_stars(world: PerfectDarkWorld) -> int:
    required_mission_stars = 0

    if world.options.agent:
        if (world.options.goal.value == Goal.option_complete_skedar_ruins 
                and world.options.required_agent_mission_stars == 21):
            required_mission_stars += 20
        else:
            required_mission_stars += world.options.required_agent_mission_stars.value
    if world.options.special_agent:
        if (world.options.goal.value == Goal.option_complete_skedar_ruins 
                and world.options.required_special_agent_mission_stars == 21):
            required_mission_stars += 20
        else:
            required_mission_stars += world.options.required_special_agent_mission_stars.value
    if world.options.perfect_agent:
        if (world.options.goal.value == Goal.option_complete_skedar_ruins 
                and world.options.required_perfect_agent_mission_stars == 21):
            required_mission_stars += 20
        else:
            required_mission_stars += world.options.required_perfect_agent_mission_stars.value

    return required_mission_stars


def get_challenge_stars(world: PerfectDarkWorld) -> int:
    required_challenge_stars = 0
    number_of_challenges = 30 - len(world.options.excluded_challenges.value)

    if (world.options.required_challenge_stars.value > number_of_challenges):
        required_challenge_stars = number_of_challenges
    else:
        required_challenge_stars = world.options.required_challenge_stars.value

    return required_challenge_stars


def add_rule(world: PerfectDarkWorld, rules: dict) -> None:
    for location, rule in rules.items():
        location_name = world.get_location(location)
        # print(location_name)
        # print(rule)
        # print(world.options.weapon_progression.value)
        world.set_rule(location_name, rule)


def add_challenge_rules(world: PerfectDarkWorld, challenge_rules: dict) -> None:
    for challenge, rule in challenge_rules.items():
        if challenge not in world.options.excluded_challenges:
            challenge_location = world.get_location(f"Complete: {challenge}")
            world.set_rule(challenge_location, rule)


def exclude_weapons_from_list(excluded_weapons: list[str]) -> list[str]:
    new_list = []

    for weapon in WEAPON_NAME_LIST:
        if weapon not in excluded_weapons:
            new_list.append(weapon)

    return new_list