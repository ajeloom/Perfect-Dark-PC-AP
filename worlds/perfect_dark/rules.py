from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, HasFromList

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements, MissionLogic, WeaponProgression, ChallengeLogic, NPCs, AlternateExits
from .items import has_challenges

npc_filter = OptionFilter(NPCs, True)

HAS_DD_KEYS = HasAny("De Vries' Necklace", "dataDyne Master Key") & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
HAS_CASS_OFFICE_KEY = HasAny("Cassandra's Office Key Card", "dataDyne Master Key")
HAS_G5_KEYS = HasAll("G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card") | Has("G5 Building Master Key")
HAS_A51_INFIL_KEYS = HasAny("Area 51 Lift Key Card", "Area 51 Master Key")
HAS_A51_RESCUE_FIRST_KEY = HasAny("Medlab 2 Key Card", "Area 51 Master Key")
HAS_A51_RESCUE_ALL_KEYS = HasAll("Medlab 2 Key Card", "Op Room Key Card") | Has("Area 51 Master Key")
HAS_AFO_LIFT_KEY = HasAny("Air Force One Lift Key Card", "Air Force One Master Key")
HAS_AFO_EXTRA_KEYS = HasAny("Air Force One Left Room Key Card", "Air Force One Right Room Key Card", "Air Force One Master Key")
HAS_AFO_LEFT_KEY = HasAny("Air Force One Left Room Key Card", "Air Force One Master Key")
HAS_AFO_RIGHT_KEY = HasAny("Air Force One Right Room Key Card", "Air Force One Master Key")

HAS_SKEDAR_RUINS_AGENT = HasAny("Skedar Ruins - Agent", "Skedar Ruins")
HAS_SKEDAR_RUINS_SP_AGENT = HasAny("Skedar Ruins - Special Agent", "Skedar Ruins")
HAS_SKEDAR_RUINS_PF_AGENT = HasAny("Skedar Ruins - Perfect Agent", "Skedar Ruins")

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
HAS_ANY_WEAPON_TYPE_ATTACKSHIP = (HasAll("Progressive SMG", "Progressive Rifle", "Progressive Pistol"))

has_defection = HasAny("dD Defection - Agent", "dD Defection - Special Agent", "dD Defection - Perfect Agent")
has_investigation = HasAny("dD Investigation - Agent", "dD Investigation - Special Agent", "dD Investigation - Perfect Agent")
has_extraction = HasAny("dD Extraction - Agent", "dD Extraction - Special Agent", "dD Extraction - Perfect Agent")
has_villa = HasAny("Carrington Villa - Agent", "Carrington Villa - Special Agent", "Carrington Villa - Perfect Agent")
has_chicago = HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
has_g5 = HasAny("G5 Building - Agent", "G5 Building - Special Agent", "G5 Building - Perfect Agent")
has_infiltration = HasAny("A51 Infiltration - Agent", "A51 Infiltration - Special Agent", "A51 Infiltration - Perfect Agent")
has_rescue = HasAny("A51 Rescue - Agent", "A51 Rescue - Special Agent", "A51 Rescue - Perfect Agent")
has_escape = HasAny("A51 Escape - Agent", "A51 Escape - Special Agent", "A51 Escape - Perfect Agent")
has_air_base = HasAny("Air Base - Agent", "Air Base - Special Agent", "Air Base - Perfect Agent")
has_air_force_one = HasAny("Air Force One - Agent", "Air Force One - Special Agent", "Air Force One - Perfect Agent")
has_crash_site = HasAny("Crash Site - Agent", "Crash Site - Special Agent", "Crash Site - Perfect Agent")
has_pelagic = HasAny("Pelagic II - Agent", "Pelagic II - Special Agent", "Pelagic II - Perfect Agent")
has_deep_sea = HasAny("Deep Sea - Agent", "Deep Sea - Special Agent", "Deep Sea - Perfect Agent")
has_defense = HasAny("CI Defense - Agent", "CI Defense - Special Agent", "CI Defense - Perfect Agent")
has_attack_ship = HasAny("Attack Ship - Agent", "Attack Ship - Special Agent", "Attack Ship - Perfect Agent")
has_skedar_ruins = HasAny("Skedar Ruins - Agent", "Skedar Ruins - Special Agent", "Skedar Ruins - Perfect Agent", "Skedar Ruins")
has_mbr = HasAny("Mr. Blonde's Revenge - Agent", "Mr. Blonde's Revenge - Special Agent", "Mr. Blonde's Revenge - Perfect Agent")
has_maian_sos = HasAny("Maian SOS - Agent", "Maian SOS - Special Agent", "Maian SOS - Perfect Agent")
has_war = HasAny("WAR! - Agent", "WAR! - Special Agent", "WAR! - Perfect Agent")
has_duel = HasAny("The Duel - Agent", "The Duel - Special Agent", "The Duel - Perfect Agent")

def set_all_rules(world: PerfectDarkWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
 
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

    world.set_rule(ci_to_defection, has_defection)
    world.set_rule(ci_to_investigation, has_investigation)
    world.set_rule(ci_to_extraction, has_extraction)
    world.set_rule(ci_to_villa, has_villa)
    world.set_rule(ci_to_chicago, has_chicago)
    world.set_rule(ci_to_g5_building, has_g5)
    world.set_rule(ci_to_infiltration, has_infiltration)
    world.set_rule(ci_to_rescue, has_rescue)
    world.set_rule(ci_to_escape, has_escape)
    world.set_rule(ci_to_air_base, has_air_base)
    world.set_rule(ci_to_air_force_one, has_air_force_one)
    world.set_rule(ci_to_crash_site, has_crash_site)
    world.set_rule(ci_to_pelagic, has_pelagic)
    world.set_rule(ci_to_deep_sea, has_deep_sea)
    world.set_rule(ci_to_defense, has_defense)
    world.set_rule(ci_to_attack_ship, has_attack_ship)
    world.set_rule(ci_to_skedar_ruins, has_skedar_ruins)
    world.set_rule(ci_to_mbr, has_mbr)
    world.set_rule(ci_to_maian_sos, has_maian_sos)
    world.set_rule(ci_to_war, has_war)
    world.set_rule(ci_to_duel, has_duel)


def set_all_location_rules(world: PerfectDarkWorld) -> None:
    normal_logic = OptionFilter(MissionLogic, MissionLogic.option_normal)
    veteran_logic = OptionFilter(MissionLogic, MissionLogic.option_veteran)
    hard_logic = OptionFilter(MissionLogic, MissionLogic.option_hard)
    perfect_logic = OptionFilter(MissionLogic, MissionLogic.option_perfect)


    # Defection
    has_defection_weapon = (Has("Falcon 2 (Silencer)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                           | HasAny("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                           | HAS_ANY_WEAPON_TYPE)

    complete_defection_weapons = (HasAll("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                 | HasAny("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                 | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                 | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                 | HAS_ANY_WEAPON_TYPE)


    # Investigation
    has_investigation_weapon = (Has("Falcon 2", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                               | HasAny("Falcon 2", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                               | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                               | HAS_ANY_WEAPON_TYPE)

    complete_investigation_weapons = (HasAll("Falcon 2", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                     | HasAny("Falcon 2", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                     | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                     | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                     | HAS_ANY_WEAPON_TYPE)

    has_k7 = (Has("K7 Avenger")
             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])
             | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]))


    # Extraction
    has_extraction_weapon = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                            | HasAny("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    complete_extraction_weapons = (HasAll("Falcon 2 (Scope)", "CMP150", "Shotgun", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                  | HasFromList("Falcon 2 (Scope)", "CMP150", "Shotgun", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                  | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                  | HAS_ANY_WEAPON_TYPE)

    has_extraction_explosive = (Has("Rocket Launcher")
                               | (all_guns_filter & HasFromList(*EXPLOSIVE_LIST, count=1))
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                               | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))


    # Villa
    has_villa_weapon = (Has("Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                       | HasAny("Sniper Rifle", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                       | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                       | HAS_ANY_WEAPON_TYPE)

    complete_villa_weapons = (HasAll("Sniper Rifle", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                             | HasAny("Sniper Rifle", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                             | (all_guns_filter & HasAny("Sniper Rifle", "Falcon 2 (Scope)") & HasFromList(*exclude_weapons_from_list(["Sniper Rifle", "Falcon 2 (Scope)"]), count=1))
                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                             | HAS_ANY_WEAPON_TYPE)

    has_villa_weapon_perfect = (Has("Laptop Gun", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                               | HasAny("Laptop Gun", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                               | HasAny("Laptop Gun", "CMP150", "Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                               | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                               | HAS_ANY_WEAPON_TYPE)

    complete_villa_weapons_perfect = (HasAll("Laptop Gun", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_normal, operator="eq")], filtered_resolution=False)
                                     | (veteran_logic & Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                     | (hard_logic & Has("Laptop Gun") & HasAny("CMP150", "Sniper Rifle"))
                                     | HasFromList("Laptop Gun", "CMP150", "Sniper Rifle", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                     | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                     | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])
                                     | HAS_ANY_WEAPON_TYPE)


    # Chicago
    has_chicago_weapon = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                         | HasAny("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                         | HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                         | HAS_ANY_WEAPON_TYPE)

    complete_chicago_weapons = (HasAll("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                               | HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                               | (all_guns_filter & HasFromList(*exclude_weapons_from_list(["Remote Mine"]), count=2))
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                               | HAS_ANY_WEAPON_TYPE)

    has_remote_mine = (Has("Remote Mine")
                      | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
                      | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]))


    # G5 Building
    has_g5_weapon = (Has("Falcon 2 (Silencer)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                    | HasAny("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                    | HAS_ANY_WEAPON_TYPE)

    complete_g5_weapons = (HasAll("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                          | HasAny("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                          | HAS_ANY_WEAPON_TYPE)


    # Infiltration
    has_infiltration_weapon = (Has("Falcon 2", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                              | HasAny("Falcon 2", "MagSec 4", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                              | HAS_ANY_WEAPON_TYPE)
    
    complete_infiltration_weapons = (HasAll("Falcon 2", "MagSec 4", "Dragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                    | HasFromList("Falcon 2", "MagSec 4", "Dragon", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                    | HAS_ANY_WEAPON_TYPE)


    # Rescue
    has_rescue_weapon = (HasAll("Falcon 2 (Silencer)", "Dragon", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                        | HasAny("Falcon 2 (Silencer)", "Dragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | HAS_ANY_WEAPON_TYPE)

    complete_rescue_weapons = (HasAll("Falcon 2 (Silencer)", "Dragon", "SuperDragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                              | HasFromList("Falcon 2 (Silencer)", "Dragon", "SuperDragon", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                              | HAS_ANY_WEAPON_TYPE)


    # Escape
    has_escape_weapon = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                        | HasAny("Falcon 2 (Scope)", "SuperDragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                        | HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                        | HAS_ANY_WEAPON_TYPE)

    complete_escape_weapons = (HasAll("Falcon 2 (Scope)", "SuperDragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                              | HasFromList("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                              | HAS_ANY_WEAPON_TYPE)


    # Air Base
    complete_air_base_weapons = (HasAll("Dragon", "K7 Avenger", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                | HasAny("Dragon", "K7 Avenger", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                | HAS_ANY_WEAPON_TYPE)

    has_sedate = (HasAny("Crossbow", "CamSpy")
                 | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))

    has_air_base_explosive = (([OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="ge")] & Has("Dragon") & HasAny("K7 Avenger", "Proximity Mine"))
                             | (all_guns_filter & HasFromList(*EXPLOSIVE_LIST, count=1))
                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                             | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))


    # Air Force One
    has_afo_weapon = ((normal_logic & Has("Laptop Gun"))
                     | (veteran_logic & (Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)))
                     | (hard_logic & (Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)))
                     | (perfect_logic & HasAny("Laptop Gun", "Cyclone", "K7 Avenger"))
                     | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                     | (Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                     | HAS_ANY_WEAPON_TYPE)

    complete_afo_weapons = ((normal_logic & HasAll("Laptop Gun", "K7 Avenger"))
                           | (veteran_logic & (Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                           | (hard_logic & (Has("Laptop Gun") | (Has("Cyclone") & HAS_AFO_EXTRA_KEYS)) & Has("K7 Avenger"))
                           | (perfect_logic & HasAny("Laptop Gun", "Cyclone", "K7 Avenger"))
                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                           | (Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                           | HAS_ANY_WEAPON_TYPE)

    has_timed_mine = (Has("Timed Mine")
                     | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                     | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))


    # Crash Site
    has_crash_site_weapon = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                            | HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                            | HAS_ANY_WEAPON_TYPE)

    complete_crash_site_weapons = (HasAll("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                  | HasFromList("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                  | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                  | HAS_ANY_WEAPON_TYPE)

    has_crash_site_explosive = (Has("Remote Mine")
                               | (all_guns_filter & HasFromList(*EXPLOSIVE_LIST, count=1))
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                               | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))

    has_dy357lx = (Has("DY357-LX")
                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
                  | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]))


    # Pelagic II
    has_pelagic_weapon = (HasAny("Falcon 2 (Silencer)", "Laptop Gun", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                         | HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                         | HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                         | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                         | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                         | HAS_ANY_WEAPON_TYPE)

    complete_pelagic_weapons = (HasAll("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                               | HasFromList("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", count=2, options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                               | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                               | HAS_ANY_WEAPON_TYPE)


    # Deep Sea
    has_deep_sea_weapon = (HasAny("Falcon 2 (Scope)", "Shotgun")
                          | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                          | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                          | HAS_ANY_WEAPON_TYPE)

    complete_deep_sea_weapons = (HasAll("Falcon 2 (Scope)", "Shotgun", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Scope)", "Shotgun", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=3))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                | HAS_ANY_WEAPON_TYPE)

    has_farsight = (Has("FarSight XR-20")
                   | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
                   | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]))


    # CI Defense
    complete_defense_weapons = (Has("AR34")
                               | (all_guns_filter & HAS_ANY_RIFLE)
                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"])
                               | Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]))

    has_rcp120 = (Has("RC-P120")
                 | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
                 | Has("Progressive Other Weapon", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]))

    has_laser = (Has("Laser")
                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"])
                | Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Laser"]))

    has_defense_explosive = (Has("Devastator")
                            | (all_guns_filter & HasAny(*EXPLOSIVE_LIST))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))

    has_defense_destroy_weapon = (has_laser
                                 | (OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="ge") & has_defense_explosive))


    # Attack Ship
    has_attack_ship_weapon = (HasAll("Combat Knife", "Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                             | Has("Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                             | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                             | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                             | HAS_ANY_WEAPON_TYPE_ATTACKSHIP)
    
    complete_attack_ship_weapons = (HasAll("Combat Knife", "Mauler", "AR34", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                   | Has("Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                   | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                   | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                   | HAS_ANY_WEAPON_TYPE_ATTACKSHIP)


    # Skedar Ruins
    has_skedar_ruins_weapon = (HasAny("Falcon 2 (Scope)", "Callisto NTG")
                              | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                              | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                              | HAS_ANY_WEAPON_TYPE)

    complete_skedar_ruins_weapons = (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                    | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                    | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE))


    # Mr. Blonde's Revenge
    complete_mbr_weapons = (Has("Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                           | HasAny("Mauler", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                           | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                           | HAS_ANY_WEAPON_TYPE)


    # Maian SOS
    complete_maian_sos_weapons = (HasAll("Falcon 2", "Dragon")
                                 | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=2))
                                 | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                 | HAS_ANY_WEAPON_TYPE)


    # WAR!
    complete_war_weapons = (Has("Phoenix", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                           | HasAny("Phoenix", "Callisto NTG", "Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                           | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=2))
                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                           | HAS_ANY_WEAPON_TYPE)


    # The Duel
    complete_duel_weapons = (Has("Falcon 2 (Scope)")
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)


    agent_rules = {
        # Stage 1 - Defection
        "dD Defection - Agent Objective 1": Has("dD Defection - Agent")
                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                            & (complete_defection_weapons
                                            | perfect_logic),

        "Complete: dD Defection - Agent": Has("dD Defection - Agent")
                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                          & (complete_defection_weapons
                                          | perfect_logic),


        # Stage 2 - Investigation
        "dD Investigation - Agent Objective 1": HasAll("dD Investigation - Agent", "CamSpy")
                                                & has_investigation_weapon,

        "dD Investigation - Agent Objective 2": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & complete_investigation_weapons,

        "Complete: dD Investigation - Agent": HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & complete_investigation_weapons,


        # Stage 3 - Extraction
        "dD Extraction - Agent Objective 1": Has("dD Extraction - Agent")
                                             & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                             & has_extraction_weapon,

        "dD Extraction - Agent Objective 2": Has("dD Extraction - Agent")
                                             & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                             & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                             & complete_extraction_weapons,

        "dD Extraction - Agent Objective 3": Has("dD Extraction - Agent")
                                             & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                             & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                             & complete_extraction_weapons,

        "Complete: dD Extraction - Agent": Has("dD Extraction - Agent")
                                           & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                           & complete_extraction_weapons,


        # Stage 4 - Carrington Villa
        "Carrington Villa - Agent Objective 1": Has("Carrington Villa - Agent")
                                                & has_villa_weapon,

        "Carrington Villa - Agent Objective 2": Has("Carrington Villa - Agent")
                                                & complete_villa_weapons,

        "Carrington Villa - Agent Objective 3": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & complete_villa_weapons,

        "Complete: Carrington Villa - Agent": HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                              & complete_villa_weapons,


        # Stage 5 - Chicago
        "Chicago - Agent Objective 1": HasAll("Chicago - Agent", "Data Uplink")
                                       & has_chicago_weapon
                                       & has_remote_mine,

        "Chicago - Agent Objective 2": HasAll("Chicago - Agent", "Data Uplink")
                                       & has_chicago_weapon,

        "Chicago - Agent Objective 3": HasAll("Chicago - Agent", "Data Uplink")
                                       & complete_chicago_weapons
                                       & has_remote_mine,

        "Complete: Chicago - Agent": HasAll("Chicago - Agent", "Data Uplink")
                                     & complete_chicago_weapons
                                     & has_remote_mine,


        # Stage 6 - G5 Building
        "G5 Building - Agent Objective 1": HasAll("G5 Building - Agent", "CamSpy")
                                           & HAS_G5_KEYS
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & has_g5_weapon,

        "G5 Building - Agent Objective 2": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                           & HAS_G5_KEYS
                                           & complete_g5_weapons,

        "G5 Building - Agent Objective 3": HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk")
                                           & HAS_G5_KEYS
                                           & complete_g5_weapons,

        "Complete: G5 Building - Agent": HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                         & HAS_G5_KEYS
                                         & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                         & complete_g5_weapons,


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Agent Objective 1": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & has_infiltration_weapon,

        "A51 Infiltration - Agent Objective 2": Has("A51 Infiltration - Agent")
                                                & HAS_A51_INFIL_KEYS
                                                & has_infiltration_weapon,

        "A51 Infiltration - Agent Objective 3": HasAll("A51 Infiltration - Agent", "Explosives")
                                                & HAS_A51_INFIL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & complete_infiltration_weapons,

        "Complete: A51 Infiltration - Agent": HasAll("A51 Infiltration - Agent", "Explosives")
                                              & HAS_A51_INFIL_KEYS
                                              & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                              & complete_infiltration_weapons,


        # Stage 8 - A51 Rescue
        "A51 Rescue - Agent Objective 1": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & has_rescue_weapon,

        "A51 Rescue - Agent Objective 2": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_FIRST_KEY
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & has_rescue_weapon,

        "A51 Rescue - Agent Objective 3": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                          & HAS_A51_RESCUE_ALL_KEYS
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & complete_rescue_weapons,

        "Complete: A51 Rescue - Agent": HasAll("A51 Rescue - Agent", "Lab Clothes")
                                        & HAS_A51_RESCUE_ALL_KEYS
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & complete_rescue_weapons,


        # Stage 9 - A51 Escape
        "A51 Escape - Agent Objective 1": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & has_escape_weapon,

        "A51 Escape - Agent Objective 2": Has("A51 Escape - Agent")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & complete_escape_weapons,

        "A51 Escape - Agent Objective 3": HasAll("A51 Escape - Agent", "Alien Medpack")
                                          & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & complete_escape_weapons,

        "Complete: A51 Escape - Agent": HasAll("A51 Escape - Agent", "Alien Medpack")
                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & complete_escape_weapons,


        # Stage 10 - Air Base
        "Air Base - Agent Objective 1": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & has_sedate,

        "Air Base - Agent Objective 2": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & has_sedate,

        "Air Base - Agent Objective 3": HasAll("Air Base - Agent", "Stewardess Disguise")
                                        & has_sedate
                                        & complete_air_base_weapons,

        "Complete: Air Base - Agent": HasAll("Air Base - Agent", "Stewardess Disguise")
                                      & has_sedate
                                      & complete_air_base_weapons,


        # Stage 11 - Air Force One
        "Air Force One - Agent Objective 1": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Agent Objective 2": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & complete_afo_weapons,

        "Air Force One - Agent Objective 3": HasAll("Air Force One - Agent", "Suitcase")
                                             & Has("President", options=[npc_filter], filtered_resolution=True)
                                             & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                             & has_afo_weapon
                                             & has_timed_mine,

        "Complete: Air Force One - Agent": HasAll("Air Force One - Agent", "Suitcase")
                                           & Has("President", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & complete_afo_weapons
                                           & has_timed_mine,


        # Stage 12 - Crash Site
        "Crash Site - Agent Objective 1": Has("Crash Site - Agent")
                                          & (has_crash_site_weapon
                                          | hard_logic
                                          | perfect_logic),

        "Crash Site - Agent Objective 2": HasAll("Crash Site - Agent", "President Scanner")
                                          & complete_crash_site_weapons,

        "Crash Site - Agent Objective 3": HasAll("Crash Site - Agent", "President Scanner")
                                          & Has("President", options=[npc_filter], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & complete_crash_site_weapons,

        "Complete: Crash Site - Agent": HasAll("Crash Site - Agent", "President Scanner")
                                        & Has("President", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & complete_crash_site_weapons,


        # Stage 13 - Pelagic II
        "Pelagic II - Agent Objective 1": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & has_pelagic_weapon,

        "Pelagic II - Agent Objective 2": Has("Pelagic II - Agent")
                                          & has_pelagic_weapon,

        "Pelagic II - Agent Objective 3": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & complete_pelagic_weapons,

        "Complete: Pelagic II - Agent": HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & complete_pelagic_weapons,


        # Stage 14 - Deep Sea
        "Deep Sea - Agent Objective 1": Has("Deep Sea - Agent")
                                        & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & has_deep_sea_weapon,

        "Deep Sea - Agent Objective 2": Has("Deep Sea - Agent")
                                        & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & complete_deep_sea_weapons 
                                        & (has_farsight
                                        | hard_logic
                                        | perfect_logic),

        "Deep Sea - Agent Objective 3": Has("Deep Sea - Agent")
                                        & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                        & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                        & complete_deep_sea_weapons 
                                        & (has_farsight
                                        | hard_logic
                                        | perfect_logic),

        "Complete: Deep Sea - Agent": Has("Deep Sea - Agent")
                                      & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                      & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                      & complete_deep_sea_weapons 
                                      & (has_farsight
                                      | hard_logic
                                      | perfect_logic),


        # Stage 15 - CI Defense
        "CI Defense - Agent Objective 1": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & complete_defense_weapons,

        "CI Defense - Agent Objective 2": Has("CI Defense - Agent")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & complete_defense_weapons
                                          & has_rcp120,

        "CI Defense - Agent Objective 3": HasAll("CI Defense - Agent", "Data Uplink")
                                          & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                          & complete_defense_weapons
                                          & has_rcp120,

        "Complete: CI Defense - Agent": HasAll("CI Defense - Agent", "Data Uplink")
                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                        & complete_defense_weapons
                                        & has_rcp120,


        # Stage 16 - Attack Ship
        "Attack Ship - Agent Objective 1": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & has_attack_ship_weapon,

        "Attack Ship - Agent Objective 2": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & complete_attack_ship_weapons,

        "Attack Ship - Agent Objective 3": Has("Attack Ship - Agent")
                                           & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                           & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                           & complete_attack_ship_weapons,

        "Complete: Attack Ship - Agent": Has("Attack Ship - Agent")
                                         & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & complete_attack_ship_weapons,


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Agent Objective 1": HAS_SKEDAR_RUINS_AGENT
                                            & HasAll("R-Tracker", "Target Amplifier")
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & has_skedar_ruins_weapon,

        "Skedar Ruins - Agent Objective 2": HAS_SKEDAR_RUINS_AGENT
                                            & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & complete_skedar_ruins_weapons,

        "Skedar Ruins - Agent Objective 3": HAS_SKEDAR_RUINS_AGENT
                                            & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                            & complete_skedar_ruins_weapons,

        "Complete: Skedar Ruins - Agent": HAS_SKEDAR_RUINS_AGENT
                                          & HasAll("R-Tracker", "Target Amplifier")
                                          & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                          & complete_skedar_ruins_weapons,


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Agent Objective 1": Has("Mr. Blonde's Revenge - Agent")
                                                    & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                    & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                    & complete_mbr_weapons,

        "Complete: Mr. Blonde's Revenge - Agent": Has("Mr. Blonde's Revenge - Agent")
                                                  & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                  & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                  & complete_mbr_weapons,


        # Stage 19 - Maian SOS
        "Maian SOS - Agent Objective 1": Has("Maian SOS - Agent")
                                         & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                         & complete_maian_sos_weapons,

        "Complete: Maian SOS - Agent": Has("Maian SOS - Agent")
                                       & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                       & complete_maian_sos_weapons,


        # Stage 20 - WAR!
        "WAR! - Agent Objective 1": Has("WAR! - Agent")
                                    & complete_war_weapons,

        "Complete: WAR! - Agent": Has("WAR! - Agent")
                                  & complete_war_weapons,


        # Stage 21 - The Duel
        "The Duel - Agent Objective 1": Has("The Duel - Agent")
                                        & (complete_duel_weapons
                                        | perfect_logic),

        "Complete: The Duel - Agent": Has("The Duel - Agent")
                                      & (complete_duel_weapons
                                      | perfect_logic),
    }


    special_agent_rules = {
        # Stage 1 - Defection
        "dD Defection - Special Agent Objective 1": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & (has_defection_weapon
                                                    | perfect_logic),

        "dD Defection - Special Agent Objective 2": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & (has_defection_weapon
                                                    | perfect_logic),

        "dD Defection - Special Agent Objective 3": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                    & complete_defection_weapons,

        "dD Defection - Special Agent Objective 4": Has("dD Defection - Special Agent")
                                                    & HAS_DD_KEYS
                                                    & complete_defection_weapons,

        "Complete: dD Defection - Special Agent": HasAll("dD Defection - Special Agent", "ECM Mine")
                                                & HAS_DD_KEYS
                                                & complete_defection_weapons,


        # Stage 2 - Investigation
        "dD Investigation - Special Agent Objective 1": HasAll("dD Investigation - Special Agent", "CamSpy")
                                                        & has_investigation_weapon,

        "dD Investigation - Special Agent Objective 2": Has("dD Investigation - Special Agent")
                                                        & has_investigation_weapon,

        "dD Investigation - Special Agent Objective 3": Has("dD Investigation - Special Agent")
                                                        & has_investigation_weapon,

        "dD Investigation - Special Agent Objective 4": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & complete_investigation_weapons,

        "Complete: dD Investigation - Special Agent": HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                      & complete_investigation_weapons,


        # Stage 3 - Extraction
        "dD Extraction - Special Agent Objective 1": Has("dD Extraction - Special Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & has_extraction_weapon,

        "dD Extraction - Special Agent Objective 2": Has("dD Extraction - Special Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & complete_extraction_weapons
                                                     & (has_extraction_explosive
                                                     | perfect_logic),

        "dD Extraction - Special Agent Objective 3": Has("dD Extraction - Special Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                     & complete_extraction_weapons,

        "dD Extraction - Special Agent Objective 4": Has("dD Extraction - Special Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                     & complete_extraction_weapons,

        "Complete: dD Extraction - Special Agent": Has("dD Extraction - Special Agent")
                                                   & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                   & complete_extraction_weapons
                                                   & (has_extraction_explosive
                                                   | perfect_logic),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Special Agent Objective 1": Has("Carrington Villa - Special Agent")
                                                        & has_villa_weapon,

        "Carrington Villa - Special Agent Objective 2": Has("Carrington Villa - Special Agent")
                                                        & has_villa_weapon,

        "Carrington Villa - Special Agent Objective 3": Has("Carrington Villa - Special Agent")
                                                        & complete_villa_weapons,

        "Carrington Villa - Special Agent Objective 4": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & complete_villa_weapons,

        "Complete: Carrington Villa - Special Agent": HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                      & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                      & complete_villa_weapons,


        # Stage 5 - Chicago
        "Chicago - Special Agent Objective 1": HasAll("Chicago - Special Agent", "Data Uplink")
                                               & has_chicago_weapon
                                               & has_remote_mine,

        "Chicago - Special Agent Objective 2": Has("Chicago - Special Agent")
                                               & has_chicago_weapon
                                               & has_remote_mine,

        "Chicago - Special Agent Objective 3": HasAll("Chicago - Special Agent", "Data Uplink")
                                               & has_chicago_weapon,

        "Chicago - Special Agent Objective 4": HasAll("Chicago - Special Agent", "Data Uplink")
                                               & complete_chicago_weapons
                                               & has_remote_mine,

        "Complete: Chicago - Special Agent": HasAll("Chicago - Special Agent", "Data Uplink")
                                             & complete_chicago_weapons
                                             & has_remote_mine,


        # Stage 6 - G5 Building
        "G5 Building - Special Agent Objective 1": Has("G5 Building - Special Agent")
                                                   & HAS_G5_KEYS
                                                   & has_g5_weapon,

        "G5 Building - Special Agent Objective 2": HasAll("G5 Building - Special Agent", "CamSpy")
                                                   & HAS_G5_KEYS
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & has_g5_weapon,

        "G5 Building - Special Agent Objective 3": HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk")
                                                   & HAS_G5_KEYS
                                                   & complete_g5_weapons,

        "G5 Building - Special Agent Objective 4": Has("G5 Building - Special Agent")
                                                   & HAS_G5_KEYS
                                                   & complete_g5_weapons
                                                   & has_remote_mine,

        "Complete: G5 Building - Special Agent": HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                 & HAS_G5_KEYS
                                                 & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                 & complete_g5_weapons
                                                 & has_remote_mine,


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Special Agent Objective 1": HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Special Agent Objective 2": HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Special Agent Objective 3": Has("A51 Infiltration - Special Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Special Agent Objective 4": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & complete_infiltration_weapons,

        "Complete: A51 Infiltration - Special Agent": HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider")
                                                      & HAS_A51_INFIL_KEYS
                                                      & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                      & complete_infiltration_weapons,


        # Stage 8 - A51 Rescue
        "A51 Rescue - Special Agent Objective 1": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & has_rescue_weapon,

        "A51 Rescue - Special Agent Objective 2": HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & has_rescue_weapon,

        "A51 Rescue - Special Agent Objective 3": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                  & HAS_A51_RESCUE_FIRST_KEY
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & complete_rescue_weapons,

        "A51 Rescue - Special Agent Objective 4": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                  & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_rescue_weapons,

        "Complete: A51 Rescue - Special Agent": HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_rescue_weapons,


        # Stage 9 - A51 Escape
        "A51 Escape - Special Agent Objective 1": Has("A51 Escape - Special Agent")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & has_escape_weapon,

        "A51 Escape - Special Agent Objective 2": Has("A51 Escape - Special Agent")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_escape_weapons,

        "A51 Escape - Special Agent Objective 3": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_escape_weapons,

        "A51 Escape - Special Agent Objective 4": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_escape_weapons,

        "Complete: A51 Escape - Special Agent": HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_escape_weapons,


        # Stage 10 - Air Base
        "Air Base - Special Agent Objective 1": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & has_sedate,

        "Air Base - Special Agent Objective 2": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & has_sedate,

        "Air Base - Special Agent Objective 3": HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                & has_sedate,

        "Air Base - Special Agent Objective 4": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                & has_sedate
                                                & complete_air_base_weapons,

        "Complete: Air Base - Special Agent": HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                              & has_sedate
                                              & complete_air_base_weapons,


        # Stage 11 - Air Force One
        "Air Force One - Special Agent Objective 1": HasAll("Air Force One - Special Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY,

        "Air Force One - Special Agent Objective 2": HasAll("Air Force One - Special Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Special Agent Objective 3": HasAll("Air Force One - Special Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True)
                                                     & complete_afo_weapons,

        "Air Force One - Special Agent Objective 4": HasAll("Air Force One - Special Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True)
                                                     & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                     & has_afo_weapon
                                                     & has_timed_mine,

        "Complete: Air Force One - Special Agent": HasAll("Air Force One - Special Agent", "Suitcase")
                                                   & HAS_AFO_LIFT_KEY
                                                   & Has("President", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_afo_weapons
                                                   & has_timed_mine,


        # Stage 12 - Crash Site
        "Crash Site - Special Agent Objective 1": HasAll("Crash Site - Special Agent", "President Scanner")
                                                  & (has_crash_site_weapon
                                                  | hard_logic
                                                  | perfect_logic),

        "Crash Site - Special Agent Objective 2": Has("Crash Site - Special Agent")
                                                  & (has_crash_site_weapon
                                                  | hard_logic
                                                  | perfect_logic),

        "Crash Site - Special Agent Objective 3": HasAll("Crash Site - Special Agent", "President Scanner")
                                                  & complete_crash_site_weapons,

        "Crash Site - Special Agent Objective 4": HasAll("Crash Site - Special Agent", "President Scanner")
                                                  & Has("President", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_crash_site_weapons,

        "Complete: Crash Site - Special Agent": HasAll("Crash Site - Special Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_crash_site_weapons,


        # Stage 13 - Pelagic II
        "Pelagic II - Special Agent Objective 1": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                  & has_pelagic_weapon,

        "Pelagic II - Special Agent Objective 2": Has("Pelagic II - Special Agent")
                                                  & has_pelagic_weapon,

        "Pelagic II - Special Agent Objective 3": Has("Pelagic II - Special Agent")
                                                  & has_pelagic_weapon,

        "Pelagic II - Special Agent Objective 4": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_pelagic_weapons,

        "Complete: Pelagic II - Special Agent": HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_pelagic_weapons,


        # Stage 14 - Deep Sea
        "Deep Sea - Special Agent Objective 1": Has("Deep Sea - Special Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & has_deep_sea_weapon,

        "Deep Sea - Special Agent Objective 2": Has("Deep Sea - Special Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & (has_farsight
                                                | hard_logic
                                                | perfect_logic),

        "Deep Sea - Special Agent Objective 3": Has("Deep Sea - Special Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & (has_farsight
                                                | hard_logic
                                                | perfect_logic),

        "Deep Sea - Special Agent Objective 4": Has("Deep Sea - Special Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & (has_farsight
                                                | hard_logic
                                                | perfect_logic),

        "Complete: Deep Sea - Special Agent": Has("Deep Sea - Special Agent")
                                              & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                              & complete_deep_sea_weapons
                                              & (has_farsight
                                              | hard_logic
                                              | perfect_logic),


        # Stage 15 - CI Defense
        "CI Defense - Special Agent Objective 1": Has("CI Defense - Special Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons,

        "CI Defense - Special Agent Objective 2": Has("CI Defense - Special Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons,

        "CI Defense - Special Agent Objective 3": Has("CI Defense - Special Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons
                                                  & has_rcp120,

        "CI Defense - Special Agent Objective 4": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons
                                                  & has_rcp120,

        "Complete: CI Defense - Special Agent": HasAll("CI Defense - Special Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & complete_defense_weapons
                                                & has_rcp120,


        # Stage 16 - Attack Ship
        "Attack Ship - Special Agent Objective 1": Has("Attack Ship - Special Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & has_attack_ship_weapon,

        "Attack Ship - Special Agent Objective 2": Has("Attack Ship - Special Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_attack_ship_weapons,

        "Attack Ship - Special Agent Objective 3": Has("Attack Ship - Special Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_attack_ship_weapons,

        "Attack Ship - Special Agent Objective 4": Has("Attack Ship - Special Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_attack_ship_weapons,

        "Complete: Attack Ship - Special Agent": Has("Attack Ship - Special Agent")
                                                 & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_attack_ship_weapons,


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Special Agent Objective 1": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & has_skedar_ruins_weapon,

        "Skedar Ruins - Special Agent Objective 2": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Skedar Ruins - Special Agent Objective 3": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Skedar Ruins - Special Agent Objective 4": HAS_SKEDAR_RUINS_SP_AGENT
                                                    & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Complete: Skedar Ruins - Special Agent": HAS_SKEDAR_RUINS_SP_AGENT
                                                & HasAll("R-Tracker", "Target Amplifier")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_skedar_ruins_weapons,


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Special Agent Objective 1": HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                            & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                            & (complete_mbr_weapons
                                                            | Has("Cloaking Device")),

        "Mr. Blonde's Revenge - Special Agent Objective 2": Has("Mr. Blonde's Revenge - Special Agent")
                                                            & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & complete_mbr_weapons,

        "Complete: Mr. Blonde's Revenge - Special Agent": HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                          & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                          & complete_mbr_weapons,


        # Stage 19 - Maian SOS
        "Maian SOS - Special Agent Objective 1": Has("Maian SOS - Special Agent")
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_maian_sos_weapons,

        "Maian SOS - Special Agent Objective 2": Has("Maian SOS - Special Agent")
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_maian_sos_weapons,

        "Complete: Maian SOS - Special Agent": Has("Maian SOS - Special Agent")
                                               & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                               & complete_maian_sos_weapons,


        # Stage 20 - WAR!
        "WAR! - Special Agent Objective 1": Has("WAR! - Special Agent")
                                            & complete_war_weapons,

        "WAR! - Special Agent Objective 2": Has("WAR! - Special Agent")
                                            & complete_war_weapons,

        "Complete: WAR! - Special Agent": Has("WAR! - Special Agent")
                                          & complete_war_weapons,


        # Stage 21 - The Duel
        "The Duel - Special Agent Objective 1": Has("The Duel - Special Agent")
                                                & (complete_duel_weapons
                                                | perfect_logic),

        "The Duel - Special Agent Objective 2": Has("The Duel - Special Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (complete_duel_weapons
                                                | perfect_logic),

        "Complete: The Duel - Special Agent": Has("The Duel - Special Agent")
                                              & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                              & (complete_duel_weapons
                                              | perfect_logic),
    }


    perfect_agent_rules = {
        # Stage 1 - Defection
        "dD Defection - Perfect Agent Objective 1": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & (has_defection_weapon
                                                    | perfect_logic),

        "dD Defection - Perfect Agent Objective 2": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & (has_defection_weapon
                                                    | perfect_logic),

        "dD Defection - Perfect Agent Objective 3": HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                    & complete_defection_weapons,

        "dD Defection - Perfect Agent Objective 4": HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                    & complete_defection_weapons,

        "dD Defection - Perfect Agent Objective 5": Has("dD Defection - Perfect Agent")
                                                    & HAS_DD_KEYS
                                                    & complete_defection_weapons,

        "Complete: dD Defection - Perfect Agent": HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink")
                                                  & HAS_DD_KEYS
                                                  & complete_defection_weapons,


        # Stage 2 - Investigation
        "dD Investigation - Perfect Agent Objective 1": HasAll("dD Investigation - Perfect Agent", "CamSpy")
                                                        & has_investigation_weapon,

        "dD Investigation - Perfect Agent Objective 2": Has("dD Investigation - Perfect Agent")
                                                        & has_investigation_weapon,

        "dD Investigation - Perfect Agent Objective 3": Has("dD Investigation - Perfect Agent")
                                                        & has_investigation_weapon,

        "dD Investigation - Perfect Agent Objective 4": HasAll("dD Investigation - Perfect Agent", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & complete_investigation_weapons
                                                        & has_k7,

        "dD Investigation - Perfect Agent Objective 5": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                        & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                        & complete_investigation_weapons
                                                        & has_k7,

        "Complete: dD Investigation - Perfect Agent": HasAll("dD Investigation - Perfect Agent", "CamSpy", "Data Uplink", "Night Vision", "Shield Tech Item")
                                                      & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                      & complete_investigation_weapons
                                                      & has_k7,


        # Stage 3 - Extraction
        "dD Extraction - Perfect Agent Objective 1": Has("dD Extraction - Perfect Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & has_extraction_weapon,

        "dD Extraction - Perfect Agent Objective 2": Has("dD Extraction - Perfect Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & has_extraction_weapon,

        "dD Extraction - Perfect Agent Objective 3": Has("dD Extraction - Perfect Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & complete_extraction_weapons
                                                     & (has_extraction_explosive
                                                     | perfect_logic),

        "dD Extraction - Perfect Agent Objective 4": Has("dD Extraction - Perfect Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                     & complete_extraction_weapons,

        "dD Extraction - Perfect Agent Objective 5": Has("dD Extraction - Perfect Agent")
                                                     & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                     & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                     & complete_extraction_weapons,

        "Complete: dD Extraction - Perfect Agent": Has("dD Extraction - Perfect Agent")
                                                   & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                   & complete_extraction_weapons
                                                   & (has_extraction_explosive
                                                   | perfect_logic),


        # Stage 4 - Carrington Villa
        "Carrington Villa - Perfect Agent Objective 1": Has("Carrington Villa - Perfect Agent")
                                                        & has_villa_weapon_perfect,

        "Carrington Villa - Perfect Agent Objective 2": Has("Carrington Villa - Perfect Agent")
                                                        & has_villa_weapon_perfect,

        "Carrington Villa - Perfect Agent Objective 3": Has("Carrington Villa - Perfect Agent")
                                                        & complete_villa_weapons_perfect,

        "Carrington Villa - Perfect Agent Objective 4": Has("Carrington Villa - Perfect Agent"),

        "Carrington Villa - Perfect Agent Objective 5": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                        & complete_villa_weapons_perfect,

        "Complete: Carrington Villa - Perfect Agent": HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                      & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                      & complete_villa_weapons_perfect,


        # Stage 5 - Chicago
        "Chicago - Perfect Agent Objective 1": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                               & has_chicago_weapon
                                               & has_remote_mine,

        "Chicago - Perfect Agent Objective 2": HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                               & has_chicago_weapon,

        "Chicago - Perfect Agent Objective 3": Has("Chicago - Perfect Agent")
                                               & has_chicago_weapon
                                               & has_remote_mine,

        "Chicago - Perfect Agent Objective 4": HasAll("Chicago - Perfect Agent", "Data Uplink")
                                               & has_chicago_weapon,

        "Chicago - Perfect Agent Objective 5": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                               & complete_chicago_weapons
                                               & has_remote_mine,

        "Complete: Chicago - Perfect Agent": HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug")
                                             & complete_chicago_weapons
                                             & has_remote_mine,


        # Stage 6 - G5 Building
        "G5 Building - Perfect Agent Objective 1": Has("G5 Building - Perfect Agent")
                                                   & HAS_G5_KEYS
                                                   & has_g5_weapon,

        "G5 Building - Perfect Agent Objective 2": Has("G5 Building - Perfect Agent")
                                                   & HAS_G5_KEYS
                                                   & has_g5_weapon,

        "G5 Building - Perfect Agent Objective 3": HasAll("G5 Building - Perfect Agent", "CamSpy")
                                                   & HAS_G5_KEYS
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & has_g5_weapon,

        "G5 Building - Perfect Agent Objective 4": HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk")
                                                   & HAS_G5_KEYS
                                                   & complete_g5_weapons,

        "G5 Building - Perfect Agent Objective 5": Has("G5 Building - Perfect Agent")
                                                   & HAS_G5_KEYS
                                                   & complete_g5_weapons
                                                   & has_remote_mine,

        "Complete: G5 Building - Perfect Agent": HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk")
                                                 & HAS_G5_KEYS
                                                 & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                 & complete_g5_weapons
                                                 & has_remote_mine,


        # Stage 7 - A51 Infiltration
        "A51 Infiltration - Perfect Agent Objective 1": HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Perfect Agent Objective 2": HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Perfect Agent Objective 3": Has("A51 Infiltration - Perfect Agent")
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Perfect Agent Objective 4": Has("A51 Infiltration - Perfect Agent")
                                                        & HAS_A51_INFIL_KEYS
                                                        & has_infiltration_weapon,

        "A51 Infiltration - Perfect Agent Objective 5": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                        & HAS_A51_INFIL_KEYS
                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                        & complete_infiltration_weapons,

        "Complete: A51 Infiltration - Perfect Agent": HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider")
                                                      & HAS_A51_INFIL_KEYS
                                                      & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                      & complete_infiltration_weapons,


        # Stage 8 - A51 Rescue
        "A51 Rescue - Perfect Agent Objective 1": HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & has_rescue_weapon,

        "A51 Rescue - Perfect Agent Objective 2": HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & has_rescue_weapon,

        "A51 Rescue - Perfect Agent Objective 3": HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & has_rescue_weapon,

        "A51 Rescue - Perfect Agent Objective 4": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                  & HAS_A51_RESCUE_FIRST_KEY
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & complete_rescue_weapons,

        "A51 Rescue - Perfect Agent Objective 5": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                  & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_rescue_weapons,

        "Complete: A51 Rescue - Perfect Agent": HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes")
                                                & HAS_A51_RESCUE_ALL_KEYS
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_rescue_weapons,


        # Stage 9 - A51 Escape
        "A51 Escape - Perfect Agent Objective 1": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & has_escape_weapon,

        "A51 Escape - Perfect Agent Objective 2": Has("A51 Escape - Perfect Agent")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & has_escape_weapon,

        "A51 Escape - Perfect Agent Objective 3": Has("A51 Escape - Perfect Agent")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_escape_weapons,

        "A51 Escape - Perfect Agent Objective 4": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_escape_weapons,

        "A51 Escape - Perfect Agent Objective 5": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                  & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_escape_weapons,

        "Complete: A51 Escape - Perfect Agent": HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_escape_weapons,


        # Stage 10 - Air Base
        "Air Base - Perfect Agent Objective 1": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & has_sedate,

        "Air Base - Perfect Agent Objective 2": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                & has_sedate,

        "Air Base - Perfect Agent Objective 3": HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                & has_sedate,

        "Air Base - Perfect Agent Objective 4": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                & has_sedate
                                                & (complete_air_base_weapons
                                                | has_air_base_explosive),

        "Air Base - Perfect Agent Objective 5": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                & has_sedate
                                                & complete_air_base_weapons,

        "Complete: Air Base - Perfect Agent": HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                              & has_sedate
                                              & complete_air_base_weapons,


        # Stage 11 - Air Force One
        "Air Force One - Perfect Agent Objective 1": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY,

        "Air Force One - Perfect Agent Objective 2": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True),

        "Air Force One - Perfect Agent Objective 3": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True)
                                                     & complete_afo_weapons,

        "Air Force One - Perfect Agent Objective 4": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True)
                                                     & has_afo_weapon
                                                     & has_timed_mine,

        "Air Force One - Perfect Agent Objective 5": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                     & HAS_AFO_LIFT_KEY
                                                     & Has("President", options=[npc_filter], filtered_resolution=True)
                                                     & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                     & has_afo_weapon
                                                     & has_timed_mine,

        "Complete: Air Force One - Perfect Agent": HasAll("Air Force One - Perfect Agent", "Suitcase")
                                                   & HAS_AFO_LIFT_KEY
                                                   & Has("President", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_afo_weapons
                                                   & has_timed_mine,


        # Stage 12 - Crash Site
        "Crash Site - Perfect Agent Objective 1": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                  & (has_crash_site_weapon
                                                  | hard_logic
                                                  | perfect_logic),

        "Crash Site - Perfect Agent Objective 2": Has("Crash Site - Perfect Agent")
                                                  & (has_crash_site_weapon
                                                  | hard_logic
                                                  | perfect_logic),

        "Crash Site - Perfect Agent Objective 3": Has("Crash Site - Perfect Agent")
                                                  & complete_crash_site_weapons
                                                  & (has_crash_site_explosive
                                                  | has_dy357lx
                                                  | perfect_logic),

        "Crash Site - Perfect Agent Objective 4": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                  & complete_crash_site_weapons,

        "Crash Site - Perfect Agent Objective 5": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                  & Has("President", options=[npc_filter], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_crash_site_weapons,

        "Complete: Crash Site - Perfect Agent": HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                & Has("President", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_crash_site_weapons
                                                & (has_crash_site_explosive
                                                | has_dy357lx
                                                | perfect_logic),


        # Stage 13 - Pelagic II
        "Pelagic II - Perfect Agent Objective 1": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                  & has_pelagic_weapon,

        "Pelagic II - Perfect Agent Objective 2": HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                  & has_pelagic_weapon,

        "Pelagic II - Perfect Agent Objective 3": Has("Pelagic II - Perfect Agent")
                                                  & has_pelagic_weapon,

        "Pelagic II - Perfect Agent Objective 4": Has("Pelagic II - Perfect Agent")
                                                  & has_pelagic_weapon,

        "Pelagic II - Perfect Agent Objective 5": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_pelagic_weapons,

        "Complete: Pelagic II - Perfect Agent": HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_pelagic_weapons,


        # Stage 14 - Deep Sea
        "Deep Sea - Perfect Agent Objective 1": Has("Deep Sea - Perfect Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & has_deep_sea_weapon,

        "Deep Sea - Perfect Agent Objective 2": Has("Deep Sea - Perfect Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & has_farsight,

        "Deep Sea - Perfect Agent Objective 3": Has("Deep Sea - Perfect Agent")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & has_farsight,

        "Deep Sea - Perfect Agent Objective 4": HasAll("Deep Sea - Perfect Agent", "Backup Disk")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & has_farsight,

        "Deep Sea - Perfect Agent Objective 5": HasAll("Deep Sea - Perfect Agent", "Backup Disk")
                                                & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                                & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                & complete_deep_sea_weapons
                                                & has_farsight,

        "Complete: Deep Sea - Perfect Agent": HasAll("Deep Sea - Perfect Agent", "Backup Disk")
                                              & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                              & Has("Dr. Caroll", options=[npc_filter], filtered_resolution=True)
                                              & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                              & complete_deep_sea_weapons
                                              & has_farsight,


        # Stage 15 - CI Defense
        "CI Defense - Perfect Agent Objective 1": Has("CI Defense - Perfect Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons,

        "CI Defense - Perfect Agent Objective 2": Has("CI Defense - Perfect Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons,

        "CI Defense - Perfect Agent Objective 3": Has("CI Defense - Perfect Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons
                                                  & has_rcp120,

        "CI Defense - Perfect Agent Objective 4": Has("CI Defense - Perfect Agent")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons
                                                  & ((has_rcp120 & has_laser)
                                                  | (OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="ge") & has_defense_explosive)),

        "CI Defense - Perfect Agent Objective 5": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                  & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                  & complete_defense_weapons
                                                  & has_rcp120
                                                  & has_defense_destroy_weapon,

        "Complete: CI Defense - Perfect Agent": HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                & complete_defense_weapons
                                                & has_rcp120
                                                & has_defense_destroy_weapon,


        # Stage 16 - Attack Ship
        "Attack Ship - Perfect Agent Objective 1": Has("Attack Ship - Perfect Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & has_attack_ship_weapon,

        "Attack Ship - Perfect Agent Objective 2": Has("Attack Ship - Perfect Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & has_attack_ship_weapon,

        "Attack Ship - Perfect Agent Objective 3": Has("Attack Ship - Perfect Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_attack_ship_weapons,

        "Attack Ship - Perfect Agent Objective 4": Has("Attack Ship - Perfect Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_attack_ship_weapons,

        "Attack Ship - Perfect Agent Objective 5": Has("Attack Ship - Perfect Agent")
                                                   & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                   & complete_attack_ship_weapons,

        "Complete: Attack Ship - Perfect Agent": Has("Attack Ship - Perfect Agent")
                                                 & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_attack_ship_weapons,


        # Stage 17 - Skedar Ruins
        "Skedar Ruins - Perfect Agent Objective 1": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & HasAll("R-Tracker", "Target Amplifier")
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & has_skedar_ruins_weapon,

        "Skedar Ruins - Perfect Agent Objective 2": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Skedar Ruins - Perfect Agent Objective 3": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Skedar Ruins - Perfect Agent Objective 4": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Skedar Ruins - Perfect Agent Objective 5": HAS_SKEDAR_RUINS_PF_AGENT
                                                    & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                    & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                    & complete_skedar_ruins_weapons,

        "Complete: Skedar Ruins - Perfect Agent": HAS_SKEDAR_RUINS_PF_AGENT
                                                  & HasAll("R-Tracker", "Target Amplifier")
                                                  & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                  & complete_skedar_ruins_weapons,


        # Stage 18 - Mr. Blonde's Revenge
        "Mr. Blonde's Revenge - Perfect Agent Objective 1": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                            & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                            & (complete_mbr_weapons
                                                            | Has("Cloaking Device")),

        "Mr. Blonde's Revenge - Perfect Agent Objective 2": Has("Mr. Blonde's Revenge - Perfect Agent")
                                                            & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                            & (complete_mbr_weapons
                                                            | (hard_logic & Has("CamSpy"))
                                                            | (perfect_logic & Has("CamSpy"))),

        "Mr. Blonde's Revenge - Perfect Agent Objective 3": Has("Mr. Blonde's Revenge - Perfect Agent")
                                                            & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & complete_mbr_weapons,

        "Complete: Mr. Blonde's Revenge - Perfect Agent": HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                          & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                          & complete_mbr_weapons,


        # Stage 19 - Maian SOS
        "Maian SOS - Perfect Agent Objective 1": Has("Maian SOS - Perfect Agent")
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_maian_sos_weapons,

        "Maian SOS - Perfect Agent Objective 2": Has("Maian SOS - Perfect Agent")
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_maian_sos_weapons
                                                 & has_dy357lx,

        "Maian SOS - Perfect Agent Objective 3": Has("Maian SOS - Perfect Agent")
                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                 & complete_maian_sos_weapons,

        "Complete: Maian SOS - Perfect Agent": Has("Maian SOS - Perfect Agent")
                                               & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                               & complete_maian_sos_weapons
                                               & has_dy357lx,


        # Stage 20 - WAR!
        "WAR! - Perfect Agent Objective 1": Has("WAR! - Perfect Agent")
                                            & complete_war_weapons,

        "WAR! - Perfect Agent Objective 2": Has("WAR! - Perfect Agent")
                                            & complete_war_weapons,

        "WAR! - Perfect Agent Objective 3": Has("WAR! - Perfect Agent")
                                            & complete_war_weapons,

        "Complete: WAR! - Perfect Agent": Has("WAR! - Perfect Agent")
                                          & complete_war_weapons,


        # Stage 21 - The Duel
        "The Duel - Perfect Agent Objective 1": Has("The Duel - Perfect Agent")
                                                & (complete_duel_weapons
                                                | perfect_logic),

        "The Duel - Perfect Agent Objective 2": Has("The Duel - Perfect Agent")
                                                & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                & (complete_duel_weapons
                                                | perfect_logic),

        "The Duel - Perfect Agent Objective 3": Has("The Duel - Perfect Agent")
                                                & (complete_duel_weapons
                                                | perfect_logic),

        "Complete: The Duel - Perfect Agent": Has("The Duel - Perfect Agent")
                                              & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                              & (complete_duel_weapons
                                              | perfect_logic),
    }


    cheat_rules = {
        # Defection
        "Cheat Unlock: Complete dD Defection": (agent_rules["Complete: dD Defection - Agent"])
                                               | (special_agent_rules["Complete: dD Defection - Special Agent"])
                                               | (perfect_agent_rules["Complete: dD Defection - Perfect Agent"]),

        # Investigation
        "Cheat Unlock: Complete dD Investigation": (agent_rules["Complete: dD Investigation - Agent"])
                                                   | (special_agent_rules["Complete: dD Investigation - Special Agent"])
                                                   | (perfect_agent_rules["Complete: dD Investigation - Perfect Agent"]),

        # Extraction
        "Cheat Unlock: Complete dD Extraction": (agent_rules["Complete: dD Extraction - Agent"])
                                                | (special_agent_rules["Complete: dD Extraction - Special Agent"])
                                                | (perfect_agent_rules["Complete: dD Extraction - Perfect Agent"]),

        # Villa
        "Cheat Unlock: Complete Carrington Villa": (agent_rules["Complete: Carrington Villa - Agent"])
                                                   | (special_agent_rules["Complete: Carrington Villa - Special Agent"])
                                                   | (perfect_agent_rules["Complete: Carrington Villa - Perfect Agent"]),
        
        # Chicago
        "Cheat Unlock: Complete Chicago": (agent_rules["Complete: Chicago - Agent"])
                                          | (special_agent_rules["Complete: Chicago - Special Agent"])
                                          | (perfect_agent_rules["Complete: Chicago - Perfect Agent"]),

        # G5 Building
        "Cheat Unlock: Complete G5 Building": (agent_rules["Complete: G5 Building - Agent"])
                                              | (special_agent_rules["Complete: G5 Building - Special Agent"])
                                              | (perfect_agent_rules["Complete: G5 Building - Perfect Agent"]),

        # A51 Infiltration
        "Cheat Unlock: Complete A51 Infiltration": (agent_rules["Complete: A51 Infiltration - Agent"])
                                                   | (special_agent_rules["Complete: A51 Infiltration - Special Agent"])
                                                   | (perfect_agent_rules["Complete: A51 Infiltration - Perfect Agent"]),

        # A51 Rescue
        "Cheat Unlock: Complete A51 Rescue": (agent_rules["Complete: A51 Rescue - Agent"])
                                             | (special_agent_rules["Complete: A51 Rescue - Special Agent"])
                                             | (perfect_agent_rules["Complete: A51 Rescue - Perfect Agent"]),

        # A51 Escape
        "Cheat Unlock: Complete A51 Escape": (agent_rules["Complete: A51 Escape - Agent"])
                                             | (special_agent_rules["Complete: A51 Escape - Special Agent"])
                                             | (perfect_agent_rules["Complete: A51 Escape - Perfect Agent"]),

        # Air Base
        "Cheat Unlock: Complete Air Base": (agent_rules["Complete: Air Base - Agent"])
                                           | (special_agent_rules["Complete: Air Base - Special Agent"])
                                           | (perfect_agent_rules["Complete: Air Base - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Air Force One": (agent_rules["Complete: Air Force One - Agent"])
                                                | (special_agent_rules["Complete: Air Force One - Special Agent"])
                                                | (perfect_agent_rules["Complete: Air Force One - Perfect Agent"]),

        # Air Force One
        "Cheat Unlock: Complete Crash Site": (agent_rules["Complete: Crash Site - Agent"])
                                             | (special_agent_rules["Complete: Crash Site - Special Agent"])
                                             | (perfect_agent_rules["Complete: Crash Site - Perfect Agent"]),

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II": (agent_rules["Complete: Pelagic II - Agent"])
                                             | (special_agent_rules["Complete: Pelagic II - Special Agent"])
                                             | (perfect_agent_rules["Complete: Pelagic II - Perfect Agent"]),

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea": (agent_rules["Complete: Deep Sea - Agent"])
                                           | (special_agent_rules["Complete: Deep Sea - Special Agent"])
                                           | (perfect_agent_rules["Complete: Deep Sea - Perfect Agent"]),

        # CI Defense
        "Cheat Unlock: Complete CI Defense": (agent_rules["Complete: CI Defense - Agent"])
                                             | (special_agent_rules["Complete: CI Defense - Special Agent"])
                                             | (perfect_agent_rules["Complete: CI Defense - Perfect Agent"]),

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship": (agent_rules["Complete: Attack Ship - Agent"])
                                              | (special_agent_rules["Complete: Attack Ship - Special Agent"])
                                              | (perfect_agent_rules["Complete: Attack Ship - Perfect Agent"]),

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins": (agent_rules["Complete: Skedar Ruins - Agent"])
                                               | (special_agent_rules["Complete: Skedar Ruins - Special Agent"])
                                               | (perfect_agent_rules["Complete: Skedar Ruins - Perfect Agent"]),
    }


    cheat_agent_rules = {
        # Extraction
        "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03": agent_rules["Complete: dD Extraction - Agent"],

        # G5 Building
        "Cheat Unlock: Complete G5 Building (Agent) in under 1:40": agent_rules["Complete: G5 Building - Agent"],

        # Escape
        "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50": agent_rules["Complete: A51 Escape - Agent"],

        # Crash Site
        "Cheat Unlock: Complete Crash Site (Agent) in under 2:50": agent_rules["Complete: Crash Site - Agent"],

        # CI Defense
        "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": agent_rules["Complete: CI Defense - Agent"],
    }


    cheat_sp_agent_rules = {
        # Defection
        "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30": special_agent_rules["Complete: dD Defection - Special Agent"],

        # Villa
        "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30": special_agent_rules["Complete: Carrington Villa - Special Agent"],

        # Infiltration
        "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00": special_agent_rules["Complete: A51 Infiltration - Special Agent"],

        # Air Base
        "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11": special_agent_rules["Complete: Air Base - Special Agent"],

        # Pelagic II
        "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07": special_agent_rules["Complete: Pelagic II - Special Agent"],

        # Attack Ship
        "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17": special_agent_rules["Complete: Attack Ship - Special Agent"],
    }


    cheat_pf_agent_rules = {
        # Investigation
        "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30": perfect_agent_rules["Complete: dD Investigation - Perfect Agent"],

        # Chicago
        "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00": perfect_agent_rules["Complete: Chicago - Perfect Agent"]
                                                                        & Has("CamSpy"),

        # Rescue
        "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59": perfect_agent_rules["Complete: A51 Rescue - Perfect Agent"],

        # Air Force One
        "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55": perfect_agent_rules["Complete: Air Force One - Perfect Agent"],

        # Deep Sea
        "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27": perfect_agent_rules["Complete: Deep Sea - Perfect Agent"],

        # Skedar Ruins
        "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31": perfect_agent_rules["Complete: Skedar Ruins - Perfect Agent"],
    }


    alternate_exits_rules = {
        "Complete G5 Building (Agent): Bottom Exit": agent_rules["Complete: G5 Building - Agent"]
                                                     & HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
                                                     & has_remote_mine
                                                     & has_chicago_weapon,
        "Complete G5 Building (Agent): Upper Exit": agent_rules["Complete: G5 Building - Agent"] 
                                                    & HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
                                                    & has_remote_mine
                                                    & has_chicago_weapon,
        "Complete A51 Escape (Agent): UFO Escape": agent_rules["Complete: A51 Escape - Agent"],
        "Complete A51 Escape (Agent): Alternate Escape": agent_rules["Complete: A51 Escape - Agent"],
        "Complete Air Base (Agent): Shuttle Exit": agent_rules["Complete: Air Base - Agent"],
        "Complete Air Base (Agent): Ladder Exit": agent_rules["Complete: Air Base - Agent"],
        "Complete G5 Building (Special Agent): Bottom Exit": special_agent_rules["Complete: G5 Building - Special Agent"]
                                                             & HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
                                                             & has_remote_mine
                                                             & has_chicago_weapon,
        "Complete G5 Building (Special Agent): Upper Exit": special_agent_rules["Complete: G5 Building - Special Agent"] 
                                                            & HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
                                                            & has_remote_mine
                                                            & has_chicago_weapon,
        "Complete A51 Escape (Special Agent): UFO Escape": special_agent_rules["Complete: A51 Escape - Special Agent"],
        "Complete A51 Escape (Special Agent): Alternate Escape": special_agent_rules["Complete: A51 Escape - Special Agent"],
        "Complete Air Base (Special Agent): Shuttle Exit": special_agent_rules["Complete: Air Base - Special Agent"],
        "Complete Air Base (Special Agent): Ladder Exit": special_agent_rules["Complete: Air Base - Special Agent"],
        "Complete G5 Building (Perfect Agent): Bottom Exit": perfect_agent_rules["Complete: G5 Building - Perfect Agent"]
                                                             & HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
                                                             & has_remote_mine
                                                             & has_chicago_weapon,
        "Complete G5 Building (Perfect Agent): Upper Exit": perfect_agent_rules["Complete: G5 Building - Perfect Agent"]
                                                            & HasAny("Chicago - Agent", "Chicago - Special Agent", "Chicago - Perfect Agent")
                                                            & has_remote_mine
                                                            & has_chicago_weapon,
        "Complete A51 Escape (Perfect Agent): UFO Escape": perfect_agent_rules["Complete: A51 Escape - Perfect Agent"],
        "Complete A51 Escape (Perfect Agent): Alternate Escape": perfect_agent_rules["Complete: A51 Escape - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Shuttle Exit": perfect_agent_rules["Complete: Air Base - Perfect Agent"],
        "Complete Air Base (Perfect Agent): Ladder Exit": perfect_agent_rules["Complete: Air Base - Perfect Agent"],
    }


    if world.options.agent:
        add_rule(world, agent_rules)

    if world.options.special_agent:
        add_rule(world, special_agent_rules)

    if world.options.perfect_agent:
        add_rule(world, perfect_agent_rules)

    if world.options.alternate_exits.value >= AlternateExits.option_one:
        add_exit_rules(world, alternate_exits_rules)

    if world.options.completion_cheats:
        if world.options.agent or world.options.special_agent or world.options.perfect_agent:
            add_rule(world, cheat_rules)

    if world.options.timed_cheats:
        if world.options.agent:
            add_rule(world, cheat_agent_rules)
        if world.options.special_agent:
            add_rule(world, cheat_sp_agent_rules)
        if world.options.perfect_agent:
            add_rule(world, cheat_pf_agent_rules)

    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not (world.options.agent or world.options.special_agent or world.options.perfect_agent):
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 1"), agent_rules["Skedar Ruins - Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 2"), agent_rules["Skedar Ruins - Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Agent Objective 3"), agent_rules["Skedar Ruins - Agent Objective 3"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Agent"), agent_rules["Complete: Skedar Ruins - Agent"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 1"), special_agent_rules["Skedar Ruins - Special Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 2"), special_agent_rules["Skedar Ruins - Special Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 3"), special_agent_rules["Skedar Ruins - Special Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Special Agent Objective 4"), special_agent_rules["Skedar Ruins - Special Agent Objective 4"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Special Agent"), special_agent_rules["Complete: Skedar Ruins - Special Agent"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 1"), perfect_agent_rules["Skedar Ruins - Perfect Agent Objective 1"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 2"), perfect_agent_rules["Skedar Ruins - Perfect Agent Objective 2"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 3"), perfect_agent_rules["Skedar Ruins - Perfect Agent Objective 3"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 4"), perfect_agent_rules["Skedar Ruins - Perfect Agent Objective 4"])
        world.set_rule(world.get_location("Skedar Ruins - Perfect Agent Objective 5"), perfect_agent_rules["Skedar Ruins - Perfect Agent Objective 5"])
        world.set_rule(world.get_location("Complete: Skedar Ruins - Perfect Agent"), perfect_agent_rules["Complete: Skedar Ruins - Perfect Agent"])

        if world.options.completion_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins"), cheat_rules["Cheat Unlock: Complete Skedar Ruins"])
        if world.options.timed_cheats:
            world.set_rule(world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"), cheat_pf_agent_rules["Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"])


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
        "Cheat Unlock: Get gold on Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)":
            HasAll("Falcon 2", "Falcon 2 (Silencer)", "Falcon 2 (Scope)", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]),

        "Cheat Unlock: Get gold on MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX":
            HasAll("MagSec 4", "Mauler", "Phoenix", "DY357 Magnum", "DY357-LX", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"])
            | Has("Progressive Pistol", count=PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]),

        "Cheat Unlock: Get gold on CMP150, Cyclone, Callisto NTG, and RC-P120":
            HasAll("CMP150", "Cyclone", "Callisto NTG", "RC-P120", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])
            | Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]),

        "Cheat Unlock: Get gold on Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon":
            HasAll("Laptop Gun", "Dragon", "K7 Avenger", "AR34", "SuperDragon", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"])
            | (Has("Progressive SMG", count=PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"])
                & Has("Progressive Rifle", count=PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"])),

        "Cheat Unlock: Get gold on Shotgun, Sniper Rifle, Rocket Launcher, and Slayer":
            HasAll("Shotgun", "Sniper Rifle", "Rocket Launcher", "Slayer", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"])
            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"])
                & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"])),

        "Cheat Unlock: Get gold on Timed Mine, Proximity Mine, and Remote Mine":
            HasAll("Timed Mine", "Proximity Mine", "Remote Mine", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])
            | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]),

        "Cheat Unlock: Get gold on FarSight XR-20, Crossbow, Combat Knife, and Grenade":
            HasAll("FarSight XR-20", "Crossbow", "Combat Knife", "Grenade", options=[OptionFilter(WeaponProgression, WeaponProgression.option_all_guns, operator="le")])
            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])
            | (Has("Progressive Other Weapon", count=PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"])
                & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"])),

        "Cheat Unlock: Get gold on Tranquilizer, Reaper, and Devastator":
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
        "Complete 18 Challenges: Formal Outfits and President Unlock": can_complete_eighteen_challenges,
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

    has_weapon_for_defection = (Has("Falcon 2 (Silencer)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_investigation = (Has("Falcon 2", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                    | HasAny("Falcon 2", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                    | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_extraction_bottom_floor = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                                | HasAny("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_extraction_upper_floors = (HasAll("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                            | HasAny("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                            | HAS_ANY_WEAPON_TYPE)

    has_villa_agent_or_special = (HasAny("Carrington Villa - Agent", "Carrington Villa - Special Agent"))

    has_weapon_for_villa = (has_villa_agent_or_special & Has("Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                            | (has_villa_agent_or_special & HasAny("Sniper Rifle", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False))
                            | (Has("Carrington Villa - Perfect Agent") & Has("Laptop Gun", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False))
                            | (Has("Carrington Villa - Perfect Agent") & HasAny("Laptop Gun", "CMP150", "Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False))
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_chicago = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Scope)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Scope)", "CMP150", "DY357 Magnum", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_g5 = (Has("Falcon 2 (Silencer)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                        | HasAny("Falcon 2 (Silencer)", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                        | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                        | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                        | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_infiltration = (Has("Falcon 2", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                    | HasAny("Falcon 2", "MagSec 4", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                                    | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                    | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_rescue = (Has("Falcon 2 (Silencer)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                            | HasAny("Falcon 2 (Silencer)", "Dragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_escape = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                            | HasAny("Falcon 2 (Scope)", "SuperDragon", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                            | HasAny("Falcon 2 (Scope)", "SuperDragon", "Tranquilizer", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_air_base = (HasAll("Dragon", "K7 Avenger", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                | HasAny("Dragon", "K7 Avenger", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_crash_site = (Has("Falcon 2 (Scope)", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_pelagic = (HasAny("Falcon 2 (Silencer)", "Laptop Gun", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="eq")], filtered_resolution=False)
                                | HasAny("Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "Phoenix", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
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

    has_weapon_for_attack_ship = (HasAll("Combat Knife", "Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=False)
                                    | Has("Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                    | (all_guns_filter & HAS_ANY_RIFLE & HasFromList(*WEAPON_NAME_LIST, count=3))
                                    | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                    | HAS_ANY_WEAPON_TYPE_ATTACKSHIP)

    has_weapon_for_mbr = (Has("Mauler", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                            | HasAny("Mauler", "CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False)
                            | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                            | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                            | HAS_ANY_WEAPON_TYPE)

    has_weapon_for_maian_sos = (HasAll("Falcon 2", "Dragon", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)
                                | Has("Falcon 2", options=[OptionFilter(MissionLogic, MissionLogic.option_perfect, operator="eq")], filtered_resolution=False)
                                | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
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
        "dD Defection: 2F double Falcon 2 (silencer)": has_defection
                                                       & has_falcon2_silencer,

        "dD Defection: 3F tiny ammo box (on corner desk)": has_defection
                                                           & has_weapon_for_defection,

        "dD Defection: 3F tiny ammo box (on table near couch)": has_defection 
                                                                & has_weapon_for_defection,

        "dD Defection: 2F tiny ammo box (on desk across the stairs)": has_defection 
                                                                      & has_weapon_for_defection,

        "dD Defection: 2F tiny ammo box (on desk across the elevator)": has_defection 
                                                                        & has_weapon_for_defection,

        "dD Defection: 2F Falcon 2 (silencer) (on desk)": has_defection 
                                                          & has_weapon_for_defection,

        "dD Defection: 2F tiny ammo box (under stairs)": has_defection 
                                                         & has_weapon_for_defection,

        "dD Defection: 1F CMP150 (on right of front desk)": has_defection
                                                            & has_cmp150
                                                            & has_weapon_for_defection,

        "dD Defection: 1F CMP150 (on left of front desk)": has_defection
                                                           & has_cmp150
                                                           & has_weapon_for_defection,

        "dD Investigation: ammo box (front of room above the K7 Avenger)": has_investigation
                                                                           & has_weapon_for_investigation,

        "dD Investigation: ammo box (back of room above the K7 Avenger)": has_investigation
                                                                          & has_weapon_for_investigation,

        "dD Investigation: ammo box (front of Night Vision room)": has_investigation
                                                                   & has_weapon_for_investigation,

        "dD Investigation: ammo box (back of Night Vision room)": has_investigation 
                                                                  & has_weapon_for_investigation,

        "dD Investigation: CMP150 (on front of table)": has_investigation
                                                        & has_cmp150
                                                        & has_weapon_for_investigation,

        "dD Investigation: CMP150 (on back of table)": has_investigation
                                                       & has_cmp150
                                                       & has_weapon_for_investigation,

        "dD Investigation: CMP150 (left of secret weapons compartment)": has_investigation
                                                                         & Has("CamSpy")
                                                                         & has_cmp150
                                                                         & has_weapon_for_investigation,

        "dD Investigation: CMP150 (right of secret weapons compartment)": has_investigation
                                                                          & Has("CamSpy")
                                                                          & has_cmp150
                                                                          & has_weapon_for_investigation,

        "dD Investigation: Proximity Mine (in radioactive room)": has_investigation
                                                                  & has_proxy_mine
                                                                  & has_weapon_for_investigation,
        
        "dD Extraction: 1F DY357 Magnum (from fifth guard)": has_extraction
                                                             & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True) 
                                                             & has_dy357 
                                                             & has_weapon_for_extraction_bottom_floor,

        "dD Extraction: 4F Rocket Launcher": has_extraction 
                                             & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                             & has_rocket_launcher 
                                             & has_weapon_for_extraction_upper_floors,

        "dD Extraction: 4F Grenade (on Cassandra's desk)": has_extraction
                                                           & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                           & HAS_CASS_OFFICE_KEY
                                                           & has_grenade
                                                           & has_weapon_for_extraction_upper_floors,

        "dD Extraction: 4F Dragon (in hidden room in Cassandra's office)": has_extraction
                                                                           & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                                                           & HAS_CASS_OFFICE_KEY
                                                                           & (HasAny("Grenade", "Rocket Launcher")
                                                                           | (all_guns_filter & HasFromList(*EXPLOSIVE_LIST, count=1))
                                                                           | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                                           | Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))
                                                                           & has_dragon
                                                                           & has_weapon_for_extraction_upper_floors,
    
        "Carrington Villa: Devastator (in helipad crate)": has_villa
                                                           & has_devastator
                                                           & has_weapon_for_villa,

        "Carrington Villa: 1st ammo box (in crate on observatory path)": has_villa
                                                                         & has_weapon_for_villa,

        "Carrington Villa: 2nd ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,

        "Carrington Villa: 3rd ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,

        "Carrington Villa: 4th ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,

        "Carrington Villa: 5th ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,

        "Carrington Villa: 6th ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,

        "Carrington Villa: 7th ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,
        
        "Carrington Villa: 8th ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,
        
        "Carrington Villa: 9th ammo box (in crate on observatory path)": has_villa 
                                                                         & has_weapon_for_villa,
        
        "Carrington Villa: double CMP150 (from sniper near the helipad)": has_villa 
                                                                          & has_cmp150
                                                                          & has_weapon_for_villa,
            
        "Chicago: BombSpy (in the dumpster)": has_chicago 
                                              & Has("CamSpy") 
                                              & has_weapon_for_chicago,

        "Chicago: double Falcon 2 (scope) (in the Pond Punk)": has_chicago 
                                                               & has_falcon2_scope 
                                                               & has_cmp150
                                                               & has_weapon_for_chicago,
    
        "G5 Building: Crossbow (after knocking out first two guards)": has_g5 
                                                                       & has_crossbow,

        "G5 Building: N-Bomb (near the upper exit)": has_g5
                                                     & HAS_G5_KEYS
                                                     & has_nbomb
                                                     & has_weapon_for_g5
                                                     & has_chicago
                                                     & has_remote_mine
                                                     & has_weapon_for_chicago,
    
        "A51 Infiltration: Rocket Launcher (in mine field)": has_infiltration 
                                                             & has_rocket_launcher 
                                                             & has_weapon_for_infiltration,
        
        "A51 Rescue: Phoenix (past locked hangar door)": has_rescue
                                                         & has_phoenix
                                                         & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                         & has_weapon_for_rescue
                                                         & has_infiltration 
                                                         & has_weapon_for_infiltration,

        "A51 Rescue: double Falcon 2 (silencer) (hidden in barrel)": has_rescue
                                                                     & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                                     & has_falcon2_silencer,
        
        "A51 Escape: double Falcon 2 (scope) (behind you at the start)": has_escape
                                                                         & has_falcon2_scope,
        
        "A51 Escape: Remote Mine (in first room with guards)": has_escape
                                                               & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                               & has_remote_mine
                                                               & has_weapon_for_escape,
    
        "Air Base: double DY357 Magnum (after knocking out all NSA Lackeys)": has_air_base
                                                                              & has_dy357
                                                                              & Has("Stewardess Disguise")
                                                                              & (HasAny("Crossbow", "CamSpy")
                                                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Base: Proximity Mine (past the cave)": has_air_base
                                                    & has_proxy_mine
                                                    & (HasAny("Crossbow", "CamSpy")
                                                    | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),
        
        "Air Force One: Cyclone (in room right of stairs)": has_air_force_one
                                                            & HAS_AFO_RIGHT_KEY
                                                            & has_cyclone,

        "Air Force One: Cyclone (in room left of stairs)": has_air_force_one 
                                                           & HAS_AFO_LEFT_KEY
                                                           & has_cyclone,
    
        "Crash Site: DY357-LX (from disarming Trent)": has_crash_site
                                                       & has_dy357lx
                                                       & has_weapon_for_crash_site,
        
        "Crash Site: Proximity Mine (from Elvis before doing any objective)": has_crash_site
                                                                              & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                              & has_proxy_mine
                                                                              & has_weapon_for_crash_site,
    
        "Pelagic II: double Falcon 2 (silencer) (from guard and no alarm)": has_pelagic
                                                                            & has_falcon2_silencer,
    
        "Deep Sea: Proximity Mine (from guard in 2nd room with cloaked guards)": has_deep_sea
                                                                                 & has_proxy_mine
                                                                                 & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=True)
                                                                                 & has_weapon_for_deep_sea,
        
        # "Deep Sea: Shotgun (near Shield on the left path)": has_deep_sea
        #                                                     & has_shotgun
        #                                                     & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="le")], filtered_resolution=True)
        #                                                     & has_weapon_for_deep_sea,
    
        "CI Defense: Devastator (dropped after saving most of the hostages)": has_defense
                                                                              & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                                              & has_devastator
                                                                              & has_weapon_for_defense,
        
        "Attack Ship: double Mauler (dropped from Skedar in final room)": has_attack_ship
                                                                          & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                          & has_mauler
                                                                          & has_weapon_for_attack_ship,

        "Attack Ship: Slayer (in the room past green chambers)": has_attack_ship
                                                                 & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                 & has_slayer
                                                                 & has_weapon_for_attack_ship,
        
        "Skedar Ruins: double Phoenix (near the gap)": has_skedar_ruins
                                                       & has_phoenix
                                                       & HasAll("R-Tracker", "Target Amplifier")
                                                       & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                       & ((HasAny("Falcon 2 (Scope)", "Callisto NTG") & Has("Devastator"))
                                                       | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1) & HasFromList(*EXPLOSIVE_LIST, count=1))
                                                       | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                       | (HAS_ANY_WEAPON_TYPE & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))),
        
        "Mr. Blonde's Revenge: 1F double CMP150 (from guard near bottom elevator)": has_mbr
                                                                                    & has_cmp150
                                                                                    & has_weapon_for_mbr
                                                                                    & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: 3F tiny ammo box (on corner desk)": has_mbr
                                                                   & has_weapon_for_mbr
                                                                   & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: 3F tiny ammo box (on table near couch)": has_mbr 
                                                                        & has_weapon_for_mbr
                                                                        & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the stairs)": has_mbr 
                                                                              & has_weapon_for_mbr
                                                                              & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
        
        "Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the elevator)": has_mbr 
                                                                                & has_weapon_for_mbr
                                                                                & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: 2F Falcon 2 (on desk)": has_mbr 
                                                       & has_weapon_for_mbr
                                                       & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
        
        "Mr. Blonde's Revenge: 2F tiny ammo box (under stairs)": has_mbr 
                                                                 & has_weapon_for_mbr
                                                                 & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),

        "Mr. Blonde's Revenge: 1F CMP150 (on right of front desk)": has_mbr
                                                                    & has_cmp150,
        
        "Mr. Blonde's Revenge: 1F CMP150 (on left of front desk)": has_mbr
                                                                   & has_cmp150,
            
        "Maian SOS: double DY357-LX (from dual-wielding guard)": has_maian_sos 
                                                                 & has_dy357lx 
                                                                 & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                 & has_weapon_for_maian_sos,

        "Maian SOS: Psychosis Gun (on desk near the start)": has_maian_sos 
                                                             & has_psychosis_gun,
    }

    pickupsanity_rules_agent_only = {
        "dD Defection: 1F Shield - (Agent)": Has("dD Defection - Agent") 
                                             & Has("Shield")
                                             & has_weapon_for_defection,

        "dD Investigation: Shield (on crate) - (Agent)": Has("dD Investigation - Agent") 
                                                         & Has("Shield")
                                                         & has_weapon_for_investigation,

        "dD Extraction: 2F Shield - (Agent)": Has("dD Extraction - Agent") 
                                              & Has("Shield")
                                              & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                              & has_weapon_for_extraction_upper_floors,

        "dD Extraction: Roof ammo box (on left) - (Agent)": Has("dD Extraction - Agent") 
                                                            & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True) 
                                                            & has_rocket_launcher 
                                                            & has_weapon_for_extraction_upper_floors,

        "dD Extraction: Roof ammo box (on right) - (Agent)": Has("dD Extraction - Agent") 
                                                             & Has("Night Vision", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True) 
                                                             & has_rocket_launcher 
                                                             & has_weapon_for_extraction_upper_floors,

        "Carrington Villa: Shield (on helipad crate) - (Agent)": Has("Carrington Villa - Agent") 
                                                                 & Has("Shield")
                                                                 & has_weapon_for_villa,

        "Carrington Villa: Shield (in the bathroom) - (Agent)": Has("Carrington Villa - Agent") 
                                                                & Has("Shield")
                                                                & has_weapon_for_villa,

        "Chicago: Shield (near the taxi) - (Agent)": Has("Chicago - Agent") 
                                                     & Has("Shield"),

        "G5 Building: Shield (in room before the laser grids) - (Agent)": Has("G5 Building - Agent") 
                                                                          & Has("Shield")
                                                                          & HAS_G5_KEYS
                                                                          & has_weapon_for_g5,

        "A51 Infiltration: Shield (near hoverbike) - (Agent)": Has("A51 Infiltration - Agent") 
                                                               & Has("Shield")
                                                               & has_weapon_for_infiltration,

        "A51 Rescue: Shield (guard past first elevator) - (Agent)": Has("A51 Rescue - Agent")
                                                                    & Has("Jonathan", options=[npc_filter], filtered_resolution=True) 
                                                                    & Has("Shield")
                                                                    & has_weapon_for_rescue,

        "A51 Escape: Shield (dropped by biotechnician) - (Agent)": Has("A51 Escape - Agent") 
                                                                   & Has("Shield")
                                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                   & has_weapon_for_escape,

        "Air Base: Shield (dropped by NSA Lackey) - (Agent)": Has("Air Base - Agent") 
                                                              & Has("Shield")
                                                              & Has("Stewardess Disguise")
                                                              & (HasAny("Crossbow", "CamSpy")
                                                              | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer"))),

        "Air Force One: Shield (in small kitchen) - (Agent)": Has("Air Force One - Agent") 
                                                              & Has("Shield"),

        "Crash Site: Shield (near the crashed UFO) - (Agent)": Has("Crash Site - Agent") 
                                                               & Has("Shield")
                                                               & has_weapon_for_crash_site, 

        "Pelagic II: Shield (on the helipad) - (Agent)": Has("Pelagic II - Agent") 
                                                         & Has("Shield")
                                                         & has_weapon_for_pelagic,

        # "Deep Sea: Shield (dropped from guard) - (Agent)": Has("Deep Sea - Agent") 
        #                                                    & Has("Shield")
        #                                                    & has_weapon_for_deep_sea,

        "CI Defense: 2F Shield - (Agent)": Has("CI Defense - Agent") 
                                           & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                           & Has("Shield"),

        "Skedar Ruins: Shield (behind the fallen pillar) - (Agent)": HAS_SKEDAR_RUINS_AGENT
                                                                     & Has("Shield")
                                                                     & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                     & (HasAny("Falcon 2 (Scope)", "Callisto NTG")
                                                                     | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                                                     | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                                                     | HAS_ANY_WEAPON_TYPE),

        "Mr. Blonde's Revenge: 1F Shield - (Agent)": Has("Mr. Blonde's Revenge - Agent") 
                                                     & Has("Shield")
                                                     & (has_weapon_for_mbr
                                                     | Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=False)),
    }

    pickupsanity_rules_agent_or_special = {
        "dD Defection: 3F Shield - (Agent/Special)": HasAny("dD Defection - Agent", "dD Defection - Special Agent")
                                                     & Has("Shield")
                                                     & has_weapon_for_defection,

        "dD Investigation: Shield (behind the glass) - (Agent/Special)": HasAny("dD Investigation - Agent", "dD Investigation - Special Agent") 
                                                                         & Has("Shield")
                                                                         & has_weapon_for_investigation,

        "Chicago: Shield (under stairs near Pond Punk) - (Agent/Special)": HasAny("Chicago - Agent", "Chicago - Special Agent") 
                                                                           & Has("Shield")
                                                                           & has_weapon_for_chicago,

        "G5 Building: Shield (on stairs to the upper exit) - (Agent/Special)": HasAny("G5 Building - Agent", "G5 Building - Special Agent")
                                                                               & Has("Shield")
                                                                               & HAS_G5_KEYS
                                                                               & has_weapon_for_g5,

        "A51 Infiltration: Shield (in the crawl space) - (Agent/Special)": HasAny("A51 Infiltration - Agent", "A51 Infiltration - Special Agent")
                                                                           & Has("Shield")
                                                                           & has_weapon_for_infiltration,

        "A51 Rescue: Shield (on desk near computer) - (Agent/Special)": HasAny("A51 Rescue - Agent", "A51 Rescue - Special Agent")
                                                                        & Has("Jonathan", options=[npc_filter], filtered_resolution=True)
                                                                        & Has("Shield")
                                                                        & has_weapon_for_rescue,

        "A51 Escape: Shield (behind locked medical containment doors) - (Agent/Special)": HasAny("A51 Escape - Agent", "A51 Escape - Special Agent")
                                                                                          & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                          & Has("Shield")
                                                                                          & has_weapon_for_escape,

        "Air Base: Shield (in the safe) - (Agent/Special)": HasAny("Air Base - Agent", "Air Base - Special Agent") 
                                                            & Has("Shield")
                                                            & Has("Stewardess Disguise")
                                                            & (HasAny("Crossbow", "CamSpy")
                                                            | (all_guns_filter & HasAny("Crossbow", "CamSpy", "Tranquilizer")))
                                                            & has_weapon_for_air_base,

        "Air Force One: Shield (in piano room) - (Agent/Special)": HasAny("Air Force One - Agent", "Air Force One - Special Agent")
                                                                   & Has("Shield"),

        "Crash Site: Shield (behind President's clone) - (Agent/Special)": HasAny("Crash Site - Agent", "Crash Site - Special Agent")
                                                                           & Has("Shield")
                                                                           & Has("Night Vision")
                                                                           & has_weapon_for_crash_site,

        "Pelagic II: Shield (on the sub hangar crate) - (Agent/Special)": HasAny("Pelagic II - Agent", "Pelagic II - Special Agent")
                                                                          & Has("Shield")
                                                                          & has_weapon_for_pelagic,

        "Deep Sea: Shield (on the left path) - (Agent/Special)": HasAny("Deep Sea - Agent", "Deep Sea - Special Agent")
                                                                 & Has("Shield")
                                                                 & has_weapon_for_deep_sea,

        "CI Defense: Basement Shield - (Agent/Special)": HasAny("CI Defense - Agent", "CI Defense - Special Agent")
                                                         & Has("Carrington", options=[npc_filter], filtered_resolution=True)
                                                         & Has("Shield")
                                                         & has_weapon_for_defense,

        "Attack Ship: Shield (on table) - (Agent/Special)": HasAny("Attack Ship - Agent", "Attack Ship - Special Agent")
                                                            & Has("Shield")
                                                            & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                            & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                            & has_weapon_for_attack_ship,

        "Skedar Ruins: Shield (area past the gap to the right) - (Agent/Special)": HasAny("Skedar Ruins - Agent", "Skedar Ruins - Special Agent", "Skedar Ruins")
                                                                                   & Has("Shield")
                                                                                   & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                                                                   & ((HasAny("Falcon 2 (Scope)", "Callisto NTG") & Has("Devastator"))
                                                                                   | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1) & HasFromList(*EXPLOSIVE_LIST, count=1))
                                                                                   | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                                                                   | (HAS_ANY_WEAPON_TYPE & Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]))),

        "Mr. Blonde's Revenge: 3F Shield - (Agent/Special)": HasAny("Mr. Blonde's Revenge - Agent", "Mr. Blonde's Revenge - Special Agent")
                                                             & Has("Shield")
                                                             & has_weapon_for_mbr
                                                             & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True),
    }

    pickupsanity_rules_special_or_perfect = {
        "dD Investigation: ammo box (front of room with one scientist)": HasAny("dD Investigation - Special Agent", "dD Investigation - Perfect Agent")
                                                                         & has_weapon_for_investigation,
        
        "dD Investigation: ammo box (back of room with one scientist)": HasAny("dD Investigation - Special Agent", "dD Investigation - Perfect Agent")
                                                                        & has_weapon_for_investigation,

        "dD Investigation: ammo box (front of room near two scientists)": HasAny("dD Investigation - Special Agent", "dD Investigation - Perfect Agent")
                                                                          & has_weapon_for_investigation,
        
        "dD Investigation: ammo box (back of room near two scientists)": HasAny("dD Investigation - Special Agent", "dD Investigation - Perfect Agent") 
                                                                         & has_weapon_for_investigation,

        "A51 Infiltration: double MagSec 4 (after placing comms rider)": HasAny("A51 Infiltration - Special Agent", "A51 Infiltration - Perfect Agent")
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
            villa_sniper_rifle = world.get_location("Carrington Villa: Sniper Rifle (in the bathroom) - (Perfect Agent)")
            world.set_rule(villa_sniper_rifle, Has("Carrington Villa - Perfect Agent")
                                               & has_sniper_rifle
                                               & ((Has("Laptop Gun") | Has("CMP150", options=[OptionFilter(MissionLogic, MissionLogic.option_hard, operator="ge")], filtered_resolution=False))
                                               | (all_guns_filter & HasFromList(*WEAPON_NAME_LIST, count=1))
                                               | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])
                                               | HAS_ANY_WEAPON_TYPE))

            attack_ship_necklace = world.get_location("Attack Ship: De Vries' necklace - (Perfect Agent)")
            world.set_rule(attack_ship_necklace, Has("Attack Ship - Perfect Agent")
                                                 & Has("Cassandra", options=[npc_filter], filtered_resolution=True)
                                                 & HAS_DD_KEYS)

        if world.options.special_agent or world.options.perfect_agent:
            add_rule(world, pickupsanity_rules_special_or_perfect)

        if world.options.perfect_agent \
                or world.options.mission_logic.value == MissionLogic.option_perfect:
            defection_laptop_gun = world.get_location("dD Defection: 2F Laptop Gun")
            world.set_rule(defection_laptop_gun, has_defection
                                                 & has_laptop_gun
                                                 & has_weapon_for_defection)

            defection_right_falcon2 = world.get_location("dD Defection: 2F Falcon 2 (silencer) (right side)")
            world.set_rule(defection_right_falcon2, has_defection
                                                    & has_falcon2_silencer)

            defection_left_falcon2 = world.get_location("dD Defection: 2F Falcon 2 (silencer) (left side)")
            world.set_rule(defection_left_falcon2, has_defection
                                                   & has_falcon2_silencer)

        if world.options.mission_logic.value == MissionLogic.option_perfect:
            mbr_laptop_gun = world.get_location("Mr. Blonde's Revenge: 2F Laptop Gun")
            world.set_rule(mbr_laptop_gun, has_mbr 
                                           & has_laptop_gun
                                           & has_weapon_for_mbr
                                           & Has("Cloaking Device", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True))
            
            mbr_falcon2_1 = world.get_location("Mr. Blonde's Revenge: 2F Falcon 2 (right side)")
            world.set_rule(mbr_falcon2_1, has_mbr
                                          & has_falcon2 
                                          & has_weapon_for_mbr)

            mbr_falcon2_2 = world.get_location("Mr. Blonde's Revenge: 2F Falcon 2 (left side)")
            world.set_rule(mbr_falcon2_2, has_mbr
                                          & has_falcon2 
                                          & has_weapon_for_mbr)


def set_completion_condition(world: PerfectDarkWorld) -> None:
    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        complete_skedar_weapons = (HasAll("R-Tracker", "Target Amplifier")
                                  & Has("IR Scanner", options=[OptionFilter(MissionLogic, MissionLogic.option_veteran, operator="le")], filtered_resolution=True)
                                  & Has("Elvis", options=[npc_filter], filtered_resolution=True)
                                  & (HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator")
                                  | (all_guns_filter & HasAny(*EXPLOSIVE_LIST) & HasFromList(*exclude_weapons_from_list(EXPLOSIVE_LIST), count=2))
                                  | Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])
                                  | (Has("Progressive Explosive", count=PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]) & HAS_ANY_WEAPON_TYPE)))

        if world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_item:
            world.set_completion_rule(has_skedar_ruins & complete_skedar_weapons)             

        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_mission_stars:
            required_mission_stars = get_mission_stars(world)

            world.set_completion_rule(has_skedar_ruins
                                      & complete_skedar_weapons
                                      & Has("Mission Star", count=required_mission_stars))

        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_challenge_stars:
            required_challenge_stars = get_challenge_stars(world)

            world.set_completion_rule(has_skedar_ruins
                                      & complete_skedar_weapons
                                      & Has("Challenge Star", count=required_challenge_stars))
                    
        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_both_stars:
            required_mission_stars = get_mission_stars(world)
            required_challenge_stars = get_challenge_stars(world)

            world.set_completion_rule(has_skedar_ruins
                                      & complete_skedar_weapons
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


def add_exit_rules(world: PerfectDarkWorld, exit_rules: dict) -> None:
    for location in world.multiworld.get_locations(world.player):
        if location.name in exit_rules:
            exit_location = world.get_location(location.name)
            world.set_rule(exit_location, exit_rules[location.name])


def exclude_weapons_from_list(excluded_weapons: list[str]) -> list[str]:
    new_list = []

    for weapon in WEAPON_NAME_LIST:
        if weapon not in excluded_weapons:
            new_list.append(weapon)

    return new_list