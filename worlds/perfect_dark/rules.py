from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from rule_builder.rules import Has, HasAll, HasAny

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements, MissionLogic, WeaponProgression, ChallengeLogic

HAS_DD_KEYS = Has("De Vries' Necklace") | Has("dataDyne Master Key")
HAS_G5_KEYS = HasAll("G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card") | Has("G5 Building Master Key")
HAS_A51_INFIL_KEYS = Has("Area 51 Lift Key Card") | Has("Area 51 Master Key")
HAS_A51_RESCUE_FIRST_KEY = Has("Medlab 2 Key Card") | Has("Area 51 Master Key")
HAS_A51_RESCUE_ALL_KEYS = HasAll("Medlab 2 Key Card", "Op Room Key Card") | Has("Area 51 Master Key")
HAS_AFO_LIFT_KEY = Has("Air Force One Lift Key Card") | Has("Air Force One Master Key")
HAS_AFO_EXTRA_KEYS = Has("Air Force One Left Room Key Card") | Has("Air Force One Right Room Key Card") | Has("Air Force One Master Key")
HAS_AFO_ALL_KEYS = (Has("Air Force One Lift Key Card") & (Has("Air Force One Left Room Key Card") | Has("Air Force One Right Room Key Card"))) | Has("Air Force One Master Key")

HAS_SKEDAR_RUINS_AGENT = Has("Skedar Ruins - Agent") | Has("Skedar Ruins")
HAS_SKEDAR_RUINS_SP_AGENT = Has("Skedar Ruins - Special Agent") | Has("Skedar Ruins")
HAS_SKEDAR_RUINS_PF_AGENT = Has("Skedar Ruins - Perfect Agent") | Has("Skedar Ruins")

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

def set_all_rules(world: PerfectDarkWorld) -> None:
    set_all_entrance_rules(world)

    if (world.options.mission_logic.value == MissionLogic.option_normal 
            | world.options.mission_logic.value == MissionLogic.option_veteran):
        set_all_location_rules(world)
    elif world.options.mission_logic.value == MissionLogic.option_hard:
        set_all_hard_location_rules(world)
    elif world.options.mission_logic.value == MissionLogic.option_perfect:
        set_all_perfect_location_rules(world)
 
    if ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_mission_stars)
            or world.options.goal.value == Goal.option_collect_mission_stars):
        required_mission_stars = get_mission_stars(world)

        mission_stars = world.get_location("Collect All Mission Stars")
        world.set_rule(mission_stars, Has("Mission Star", count=required_mission_stars))

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


def set_all_location_rules(world: PerfectDarkWorld) -> None:
    if world.options.weapon_progression.value == WeaponProgression.option_vanilla:
        if world.options.agent:
            # Stage 1 - Defection
            defection_agent_obj_1 = world.get_location("dD Defection - Agent Objective 1")
            world.set_rule(defection_agent_obj_1, HasAll("dD Defection - Agent", "Falcon 2 (Silencer)", "CMP150"))

            defection_agent_complete = world.get_location("Complete: dD Defection - Agent")
            world.set_rule(defection_agent_complete, HasAll("dD Defection - Agent", "Falcon 2 (Silencer)", "CMP150"))


            # Stage 2 - Investigation
            investigation_agent_obj_1 = world.get_location("dD Investigation - Agent Objective 1")
            world.set_rule(investigation_agent_obj_1, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2"))

            investigation_agent_obj_2 = world.get_location("dD Investigation - Agent Objective 2")
            world.set_rule(investigation_agent_obj_2, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))

            investigation_agent_complete = world.get_location("Complete: dD Investigation - Agent")
            world.set_rule(investigation_agent_complete, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))
            

            # Stage 3 - Extraction
            extraction_agent_obj_1 = world.get_location("dD Extraction - Agent Objective 1")
            world.set_rule(extraction_agent_obj_1, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)"))

            extraction_agent_obj_2 = world.get_location("dD Extraction - Agent Objective 2")
            world.set_rule(extraction_agent_obj_2, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))

            extraction_agent_obj_3 = world.get_location("dD Extraction - Agent Objective 3")
            world.set_rule(extraction_agent_obj_3, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))

            extraction_agent_complete = world.get_location("Complete: dD Extraction - Agent")
            world.set_rule(extraction_agent_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))


            # Stage 4 - Villa
            villa_agent_obj_1 = world.get_location("Carrington Villa - Agent Objective 1")
            world.set_rule(villa_agent_obj_1, HasAll("Carrington Villa - Agent", "Sniper Rifle"))

            villa_agent_obj_2 = world.get_location("Carrington Villa - Agent Objective 2")
            world.set_rule(villa_agent_obj_2, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150"))

            villa_agent_obj_3 = world.get_location("Carrington Villa - Agent Objective 3")
            world.set_rule(villa_agent_obj_3, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))

            villa_agent_complete = world.get_location("Complete: Carrington Villa - Agent")
            world.set_rule(villa_agent_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            if world.options.mission_logic.value == MissionLogic.option_normal:
                chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
                world.set_rule(chicago_agent_obj_1, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)"))

                
                chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
                world.set_rule(chicago_agent_obj_2, HasAll("Chicago - Agent", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
                world.set_rule(chicago_agent_obj_3, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))
                
                chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
                world.set_rule(chicago_agent_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
                world.set_rule(chicago_agent_obj_1, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)"))
            
                chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
                world.set_rule(chicago_agent_obj_2, HasAll("Chicago - Agent", "Falcon 2 (Scope)") & (Has("Data Uplink") | Has("CamSpy")))

                chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
                world.set_rule(chicago_agent_obj_3, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))
                
                chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
                world.set_rule(chicago_agent_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))


            # Stage 6 - G5 Building
            g5_agent_obj_1 = world.get_location("G5 Building - Agent Objective 1")
            world.set_rule(g5_agent_obj_1, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)

            g5_agent_obj_2 = world.get_location("G5 Building - Agent Objective 2")
            world.set_rule(g5_agent_obj_2, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_agent_obj_3 = world.get_location("G5 Building - Agent Objective 3")
            world.set_rule(g5_agent_obj_3, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_agent_complete = world.get_location("Complete: G5 Building - Agent")
            world.set_rule(g5_agent_complete, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)


            # Stage 7 - Infiltration
            infiltration_agent_obj_1 = world.get_location("A51 Infiltration - Agent Objective 1")
            world.set_rule(infiltration_agent_obj_1, HasAll("A51 Infiltration - Agent", "Falcon 2", "Explosives"))

            infiltration_agent_obj_2 = world.get_location("A51 Infiltration - Agent Objective 2")
            world.set_rule(infiltration_agent_obj_2, HasAll("A51 Infiltration - Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)

            infiltration_agent_obj_3 = world.get_location("A51 Infiltration - Agent Objective 3")
            world.set_rule(infiltration_agent_obj_3, HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)

            infiltration_agent_complete = world.get_location("Complete: A51 Infiltration - Agent")
            world.set_rule(infiltration_agent_complete, HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)


            # Stage 8 - Rescue
            rescue_agent_obj_1 = world.get_location("A51 Rescue - Agent Objective 1")
            world.set_rule(rescue_agent_obj_1, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes"))

            rescue_agent_obj_2 = world.get_location("A51 Rescue - Agent Objective 2")
            world.set_rule(rescue_agent_obj_2, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)

            rescue_agent_obj_3 = world.get_location("A51 Rescue - Agent Objective 3")
            world.set_rule(rescue_agent_obj_3, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
            
            rescue_agent_complete = world.get_location("Complete: A51 Rescue - Agent")
            world.set_rule(rescue_agent_complete, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


            # Stage 9 - Escape
            escape_agent_obj_1 = world.get_location("A51 Escape - Agent Objective 1")
            world.set_rule(escape_agent_obj_1, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_agent_obj_2 = world.get_location("A51 Escape - Agent Objective 2")
            world.set_rule(escape_agent_obj_2, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_agent_obj_3 = world.get_location("A51 Escape - Agent Objective 3")
            world.set_rule(escape_agent_obj_3, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))
            
            escape_agent_complete = world.get_location("Complete: A51 Escape - Agent")
            world.set_rule(escape_agent_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
            world.set_rule(air_base_agent_obj_1, HasAll("Air Base - Agent", "Crossbow", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

            air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
            world.set_rule(air_base_agent_obj_2, HasAll("Air Base - Agent", "Crossbow", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

            air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
            world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise"))
            
            air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
            world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise"))


            # Stage 11 - Air Force One
            if world.options.mission_logic.value == MissionLogic.option_normal:
                air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
                world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

                air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
                world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger"))

                air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
                world.set_rule(air_force_one_agent_obj_3, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "Timed Mine"))

                air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
                world.set_rule(air_force_one_agent_complete, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
                world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

                air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
                world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger")
                                                          | (HasAll("Air Force One - Agent", "Suitcase", "Cyclone", "K7 Avenger") & HAS_AFO_EXTRA_KEYS))

                air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
                world.set_rule(air_force_one_agent_obj_3, HasAll("Air Force One - Agent", "Laptop Gun", "Timed Mine")
                                                          | (HasAll("Air Force One - Agent", "Cyclone", "Timed Mine") & HAS_AFO_EXTRA_KEYS))

                air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
                world.set_rule(air_force_one_agent_complete, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine")
                                                             | (HasAll("Air Force One - Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_EXTRA_KEYS))            


            # Stage 12 - Crash Site
            crash_site_agent_obj_1 = world.get_location("Crash Site - Agent Objective 1")
            world.set_rule(crash_site_agent_obj_1, HasAll("Crash Site - Agent", "Falcon 2 (Scope)"))

            crash_site_agent_obj_2 = world.get_location("Crash Site - Agent Objective 2")
            world.set_rule(crash_site_agent_obj_2, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))

            crash_site_agent_obj_3 = world.get_location("Crash Site - Agent Objective 3")
            world.set_rule(crash_site_agent_obj_3, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_agent_complete = world.get_location("Complete: Crash Site - Agent")
            world.set_rule(crash_site_agent_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))


            # Stage 13 - Pelagic II
            pelagic_agent_obj_1 = world.get_location("Pelagic II - Agent Objective 1")
            world.set_rule(pelagic_agent_obj_1, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun", "X-Ray Scanner"))

            pelagic_agent_obj_2 = world.get_location("Pelagic II - Agent Objective 2")
            world.set_rule(pelagic_agent_obj_2, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun"))

            pelagic_agent_obj_3 = world.get_location("Pelagic II - Agent Objective 3")
            world.set_rule(pelagic_agent_obj_3, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))
            
            pelagic_agent_complete = world.get_location("Complete: Pelagic II - Agent")
            world.set_rule(pelagic_agent_complete, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))


            # Stage 14 - Deep Sea
            deep_sea_agent_obj_1 = world.get_location("Deep Sea - Agent Objective 1")
            world.set_rule(deep_sea_agent_obj_1, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "IR Scanner"))

            deep_sea_agent_obj_2 = world.get_location("Deep Sea - Agent Objective 2")
            world.set_rule(deep_sea_agent_obj_2, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_agent_obj_3 = world.get_location("Deep Sea - Agent Objective 3")
            world.set_rule(deep_sea_agent_obj_3, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_agent_complete = world.get_location("Complete: Deep Sea - Agent")
            world.set_rule(deep_sea_agent_complete, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_agent_obj_1 = world.get_location("CI Defense - Agent Objective 1")
            world.set_rule(institute_defense_agent_obj_1, HasAll("CI Defense - Agent", "AR34"))

            institute_defense_agent_obj_2 = world.get_location("CI Defense - Agent Objective 2")
            world.set_rule(institute_defense_agent_obj_2, HasAll("CI Defense - Agent", "AR34", "RC-P120"))

            institute_defense_agent_obj_3 = world.get_location("CI Defense - Agent Objective 3")
            world.set_rule(institute_defense_agent_obj_3, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))

            institute_defense_agent_complete = world.get_location("Complete: CI Defense - Agent")
            world.set_rule(institute_defense_agent_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_agent_obj_1 = world.get_location("Attack Ship - Agent Objective 1")
            world.set_rule(attack_ship_agent_obj_1, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler"))

            attack_ship_agent_obj_2 = world.get_location("Attack Ship - Agent Objective 2")
            world.set_rule(attack_ship_agent_obj_2, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_agent_obj_3 = world.get_location("Attack Ship - Agent Objective 3")
            world.set_rule(attack_ship_agent_obj_3, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_agent_complete = world.get_location("Complete: Attack Ship - Agent")
            world.set_rule(attack_ship_agent_complete, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
            world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
            world.set_rule(skedar_ruins_agent_obj_2, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
            world.set_rule(skedar_ruins_agent_obj_3, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
            world.set_rule(skedar_ruins_agent_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Agent Objective 1")
            world.set_rule(mbr_agent_obj_1, HasAll("Mr. Blonde's Revenge - Agent", "Mauler", "Cloaking Device"))

            mbr_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Agent")
            world.set_rule(mbr_agent_complete, HasAll("Mr. Blonde's Revenge - Agent", "Mauler", "Cloaking Device"))


            # Stage 19 - Maian SOS
            maian_sos_agent_obj_1 = world.get_location("Maian SOS - Agent Objective 1")
            world.set_rule(maian_sos_agent_obj_1, HasAll("Maian SOS - Agent", "Falcon 2", "Dragon"))

            maian_sos_agent_complete = world.get_location("Complete: Maian SOS - Agent")
            world.set_rule(maian_sos_agent_complete, HasAll("Maian SOS - Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_agent_obj_1 = world.get_location("WAR! - Agent Objective 1")
            world.set_rule(war_agent_obj_1, HasAll("WAR! - Agent", "Phoenix"))

            war_agent_complete = world.get_location("Complete: WAR! - Agent")
            world.set_rule(war_agent_complete, HasAll("WAR! - Agent", "Phoenix"))


            # Stage 21 - The Duel
            duel_agent_obj_1 = world.get_location("The Duel - Agent Objective 1")
            world.set_rule(duel_agent_obj_1, HasAll("The Duel - Agent", "Falcon 2 (Scope)"))

            duel_agent_complete = world.get_location("Complete: The Duel - Agent")
            world.set_rule(duel_agent_complete, HasAll("The Duel - Agent", "Falcon 2 (Scope)"))


        if world.options.special_agent:
            # Stage 1 - Defection
            defection_sp_agent_obj_1 = world.get_location("dD Defection - Special Agent Objective 1")
            world.set_rule(defection_sp_agent_obj_1, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)"))

            defection_sp_agent_obj_2 = world.get_location("dD Defection - Special Agent Objective 2")
            world.set_rule(defection_sp_agent_obj_2, HasAll("dD Defection - Special Agent", "Falcon 2 (Silencer)") & HAS_DD_KEYS)

            defection_sp_agent_obj_3 = world.get_location("dD Defection - Special Agent Objective 3")
            world.set_rule(defection_sp_agent_obj_3, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150"))

            defection_sp_agent_obj_4 = world.get_location("dD Defection - Special Agent Objective 4")
            world.set_rule(defection_sp_agent_obj_4, HasAll("dD Defection - Special Agent", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)

            defection_sp_agent_complete = world.get_location("Complete: dD Defection - Special Agent")
            world.set_rule(defection_sp_agent_complete, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)


            # Stage 2 - Investigation
            investigation_sp_agent_obj_1 = world.get_location("dD Investigation - Special Agent Objective 1")
            world.set_rule(investigation_sp_agent_obj_1, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2"))

            investigation_sp_agent_obj_2 = world.get_location("dD Investigation - Special Agent Objective 2")
            world.set_rule(investigation_sp_agent_obj_2, HasAll("dD Investigation - Special Agent", "Falcon 2"))

            investigation_sp_agent_obj_3 = world.get_location("dD Investigation - Special Agent Objective 3")
            world.set_rule(investigation_sp_agent_obj_3, HasAll("dD Investigation - Special Agent", "Falcon 2", "CMP150"))

            investigation_sp_agent_obj_4 = world.get_location("dD Investigation - Special Agent Objective 4")
            world.set_rule(investigation_sp_agent_obj_4, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))

            investigation_sp_agent_complete = world.get_location("Complete: dD Investigation - Special Agent")
            world.set_rule(investigation_sp_agent_complete, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))
            

            # Stage 3 - Extraction
            extraction_sp_agent_obj_1 = world.get_location("dD Extraction - Special Agent Objective 1")
            world.set_rule(extraction_sp_agent_obj_1, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)"))

            extraction_sp_agent_obj_2 = world.get_location("dD Extraction - Special Agent Objective 2")
            world.set_rule(extraction_sp_agent_obj_2, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher"))

            extraction_sp_agent_obj_3 = world.get_location("dD Extraction - Special Agent Objective 3")
            world.set_rule(extraction_sp_agent_obj_3, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))

            extraction_sp_agent_obj_4 = world.get_location("dD Extraction - Special Agent Objective 4")
            world.set_rule(extraction_sp_agent_obj_4, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))

            extraction_sp_agent_complete = world.get_location("Complete: dD Extraction - Special Agent")
            world.set_rule(extraction_sp_agent_complete, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher"))


            # Stage 4 - Villa
            villa_sp_agent_obj_1 = world.get_location("Carrington Villa - Special Agent Objective 1")
            world.set_rule(villa_sp_agent_obj_1, HasAll("Carrington Villa - Special Agent", "Sniper Rifle"))

            villa_sp_agent_obj_2 = world.get_location("Carrington Villa - Special Agent Objective 2")
            world.set_rule(villa_sp_agent_obj_2, HasAll("Carrington Villa - Special Agent", "Sniper Rifle"))

            villa_sp_agent_obj_3 = world.get_location("Carrington Villa - Special Agent Objective 3")
            world.set_rule(villa_sp_agent_obj_3, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150"))

            villa_sp_agent_obj_4 = world.get_location("Carrington Villa - Special Agent Objective 4")
            world.set_rule(villa_sp_agent_obj_4, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))

            villa_sp_agent_complete = world.get_location("Complete: Carrington Villa - Special Agent")
            world.set_rule(villa_sp_agent_complete, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            if world.options.mission_logic.value == MissionLogic.option_normal:
                chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
                world.set_rule(chicago_sp_agent_obj_1, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
                world.set_rule(chicago_sp_agent_obj_2, HasAll("Chicago - Special Agent", "Remote Mine", "Falcon 2 (Scope)"))

                chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
                world.set_rule(chicago_sp_agent_obj_3, HasAll("Chicago - Special Agent", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
                world.set_rule(chicago_sp_agent_obj_4, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))
                
                chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
                world.set_rule(chicago_sp_agent_complete, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
                world.set_rule(chicago_sp_agent_obj_1, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
                world.set_rule(chicago_sp_agent_obj_2, HasAll("Chicago - Special Agent", "Remote Mine", "Falcon 2 (Scope)"))

                chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
                world.set_rule(chicago_sp_agent_obj_3, HasAll("Chicago - Special Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                       | HasAll("Chicago - Special Agent", "CamSpy", "Falcon 2 (Scope)"))

                chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
                world.set_rule(chicago_sp_agent_obj_4, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))
                
                chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
                world.set_rule(chicago_sp_agent_complete, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))


            # Stage 6 - G5 Building
            g5_sp_agent_obj_1 = world.get_location("G5 Building - Special Agent Objective 1")
            world.set_rule(g5_sp_agent_obj_1, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)

            g5_sp_agent_obj_2 = world.get_location("G5 Building - Special Agent Objective 2")
            world.set_rule(g5_sp_agent_obj_2, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)

            g5_sp_agent_obj_3 = world.get_location("G5 Building - Special Agent Objective 3")
            world.set_rule(g5_sp_agent_obj_3, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_sp_agent_obj_4 = world.get_location("G5 Building - Special Agent Objective 4")
            world.set_rule(g5_sp_agent_obj_4, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "Remote Mine") & HAS_G5_KEYS)

            g5_sp_agent_complete = world.get_location("Complete: G5 Building - Special Agent")
            world.set_rule(g5_sp_agent_complete, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)


            # Stage 7 - Infiltration
            infiltration_sp_agent_obj_1 = world.get_location("A51 Infiltration - Special Agent Objective 1")
            world.set_rule(infiltration_sp_agent_obj_1, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Explosives"))

            infiltration_sp_agent_obj_2 = world.get_location("A51 Infiltration - Special Agent Objective 2")
            world.set_rule(infiltration_sp_agent_obj_2, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Comms Rider"))

            infiltration_sp_agent_obj_3 = world.get_location("A51 Infiltration - Special Agent Objective 3")
            world.set_rule(infiltration_sp_agent_obj_3, HasAll("A51 Infiltration - Special Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)

            infiltration_sp_agent_obj_4 = world.get_location("A51 Infiltration - Special Agent Objective 4")
            world.set_rule(infiltration_sp_agent_obj_4, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)

            infiltration_sp_agent_complete = world.get_location("Complete: A51 Infiltration - Special Agent")
            world.set_rule(infiltration_sp_agent_complete, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)


            # Stage 8 - Rescue
            rescue_sp_agent_obj_1 = world.get_location("A51 Rescue - Special Agent Objective 1")
            world.set_rule(rescue_sp_agent_obj_1, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "X-Ray Scanner"))

            rescue_sp_agent_obj_2 = world.get_location("A51 Rescue - Special Agent Objective 2")
            world.set_rule(rescue_sp_agent_obj_2, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes"))

            rescue_sp_agent_obj_3 = world.get_location("A51 Rescue - Special Agent Objective 3")
            world.set_rule(rescue_sp_agent_obj_3, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)

            rescue_sp_agent_obj_4 = world.get_location("A51 Rescue - Special Agent Objective 4")
            world.set_rule(rescue_sp_agent_obj_4, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
            
            rescue_sp_agent_complete = world.get_location("Complete: A51 Rescue - Special Agent")
            world.set_rule(rescue_sp_agent_complete, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


            # Stage 9 - Escape
            escape_sp_agent_obj_1 = world.get_location("A51 Escape - Special Agent Objective 1")
            world.set_rule(escape_sp_agent_obj_1, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_sp_agent_obj_2 = world.get_location("A51 Escape - Special Agent Objective 2")
            world.set_rule(escape_sp_agent_obj_2, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_sp_agent_obj_3 = world.get_location("A51 Escape - Special Agent Objective 3")
            world.set_rule(escape_sp_agent_obj_3, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))

            escape_sp_agent_obj_4 = world.get_location("A51 Escape - Special Agent Objective 4")
            world.set_rule(escape_sp_agent_obj_4, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))
            
            escape_sp_agent_complete = world.get_location("Complete: A51 Escape - Special Agent")
            world.set_rule(escape_sp_agent_complete, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
            world.set_rule(air_base_sp_agent_obj_1, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

            air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
            world.set_rule(air_base_sp_agent_obj_2, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

            air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
            world.set_rule(air_base_sp_agent_obj_3, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

            air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
            world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase"))
            
            air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
            world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                       | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase"))


            # Stage 11 - Air Force One
            if world.options.mission_logic.value == MissionLogic.option_normal:
                air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
                world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
                world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
                world.set_rule(air_force_one_sp_agent_obj_3, HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger") & HAS_AFO_LIFT_KEY)

                air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
                world.set_rule(air_force_one_sp_agent_obj_4, HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)

                air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
                world.set_rule(air_force_one_sp_agent_complete, HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
                world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
                world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
                world.set_rule(air_force_one_sp_agent_obj_3, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "K7 Avenger") & HAS_AFO_ALL_KEYS))

                air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
                world.set_rule(air_force_one_sp_agent_obj_4, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_ALL_KEYS))

                air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
                world.set_rule(air_force_one_sp_agent_complete, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                                | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


            # Stage 12 - Crash Site
            crash_site_sp_agent_obj_1 = world.get_location("Crash Site - Special Agent Objective 1")
            world.set_rule(crash_site_sp_agent_obj_1, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "President Scanner"))

            crash_site_sp_agent_obj_2 = world.get_location("Crash Site - Special Agent Objective 2")
            world.set_rule(crash_site_sp_agent_obj_2, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)"))

            crash_site_sp_agent_obj_3 = world.get_location("Crash Site - Special Agent Objective 3")
            world.set_rule(crash_site_sp_agent_obj_3, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))

            crash_site_sp_agent_obj_4 = world.get_location("Crash Site - Special Agent Objective 4")
            world.set_rule(crash_site_sp_agent_obj_4, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_sp_agent_complete = world.get_location("Complete: Crash Site - Special Agent")
            world.set_rule(crash_site_sp_agent_complete, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))


            # Stage 13 - Pelagic II
            pelagic_sp_agent_obj_1 = world.get_location("Pelagic II - Special Agent Objective 1")
            world.set_rule(pelagic_sp_agent_obj_1, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun", "X-Ray Scanner"))

            pelagic_sp_agent_obj_2 = world.get_location("Pelagic II - Special Agent Objective 2")
            world.set_rule(pelagic_sp_agent_obj_2, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun"))

            pelagic_sp_agent_obj_3 = world.get_location("Pelagic II - Special Agent Objective 3")
            world.set_rule(pelagic_sp_agent_obj_3, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun"))

            pelagic_sp_agent_obj_4 = world.get_location("Pelagic II - Special Agent Objective 4")
            world.set_rule(pelagic_sp_agent_obj_4, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))
            
            pelagic_sp_agent_complete = world.get_location("Complete: Pelagic II - Special Agent")
            world.set_rule(pelagic_sp_agent_complete, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))


            # Stage 14 - Deep Sea
            deep_sea_sp_agent_obj_1 = world.get_location("Deep Sea - Special Agent Objective 1")
            world.set_rule(deep_sea_sp_agent_obj_1, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "IR Scanner"))

            deep_sea_sp_agent_obj_2 = world.get_location("Deep Sea - Special Agent Objective 2")
            world.set_rule(deep_sea_sp_agent_obj_2, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_sp_agent_obj_3 = world.get_location("Deep Sea - Special Agent Objective 3")
            world.set_rule(deep_sea_sp_agent_obj_3, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_sp_agent_obj_4 = world.get_location("Deep Sea - Special Agent Objective 4")
            world.set_rule(deep_sea_sp_agent_obj_4, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))
            
            deep_sea_sp_agent_complete = world.get_location("Complete: Deep Sea - Special Agent")
            world.set_rule(deep_sea_sp_agent_complete, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_sp_agent_obj_1 = world.get_location("CI Defense - Special Agent Objective 1")
            world.set_rule(institute_defense_sp_agent_obj_1, HasAll("CI Defense - Special Agent", "AR34"))

            institute_defense_sp_agent_obj_2 = world.get_location("CI Defense - Special Agent Objective 2")
            world.set_rule(institute_defense_sp_agent_obj_2, HasAll("CI Defense - Special Agent", "AR34"))

            institute_defense_sp_agent_obj_3 = world.get_location("CI Defense - Special Agent Objective 3")
            world.set_rule(institute_defense_sp_agent_obj_3, HasAll("CI Defense - Special Agent", "AR34", "RC-P120"))

            institute_defense_sp_agent_obj_4 = world.get_location("CI Defense - Special Agent Objective 4")
            world.set_rule(institute_defense_sp_agent_obj_4, HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink"))

            institute_defense_sp_agent_complete = world.get_location("Complete: CI Defense - Special Agent")
            world.set_rule(institute_defense_sp_agent_complete, HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_sp_agent_obj_1 = world.get_location("Attack Ship - Special Agent Objective 1")
            world.set_rule(attack_ship_sp_agent_obj_1, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler"))

            attack_ship_sp_agent_obj_2 = world.get_location("Attack Ship - Special Agent Objective 2")
            world.set_rule(attack_ship_sp_agent_obj_2, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_sp_agent_obj_3 = world.get_location("Attack Ship - Special Agent Objective 3")
            world.set_rule(attack_ship_sp_agent_obj_3, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_sp_agent_obj_4 = world.get_location("Attack Ship - Special Agent Objective 4")
            world.set_rule(attack_ship_sp_agent_obj_4, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_sp_agent_complete = world.get_location("Complete: Attack Ship - Special Agent")
            world.set_rule(attack_ship_sp_agent_complete, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
            world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
            world.set_rule(skedar_ruins_sp_agent_obj_2, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
            world.set_rule(skedar_ruins_sp_agent_obj_3, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
            world.set_rule(skedar_ruins_sp_agent_obj_4, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
            world.set_rule(skedar_ruins_sp_agent_complete, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_sp_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 1")
            world.set_rule(mbr_sp_agent_obj_1, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb"))

            mbr_sp_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 2")
            world.set_rule(mbr_sp_agent_obj_2, HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler", "Cloaking Device"))

            mbr_sp_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Special Agent")
            world.set_rule(mbr_sp_agent_complete, HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler", "Cloaking Device", "Skedar Bomb"))


            # Stage 19 - Maian SOS
            maian_sos_sp_agent_obj_1 = world.get_location("Maian SOS - Special Agent Objective 1")
            world.set_rule(maian_sos_sp_agent_obj_1, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))

            maian_sos_sp_agent_obj_2 = world.get_location("Maian SOS - Special Agent Objective 2")
            world.set_rule(maian_sos_sp_agent_obj_2, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))

            maian_sos_sp_agent_complete = world.get_location("Complete: Maian SOS - Special Agent")
            world.set_rule(maian_sos_sp_agent_complete, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_sp_agent_obj_1 = world.get_location("WAR! - Special Agent Objective 1")
            world.set_rule(war_sp_agent_obj_1, HasAll("WAR! - Special Agent", "Phoenix"))

            war_sp_agent_obj_2 = world.get_location("WAR! - Special Agent Objective 2")
            world.set_rule(war_sp_agent_obj_2, HasAll("WAR! - Special Agent", "Phoenix"))

            war_sp_agent_complete = world.get_location("Complete: WAR! - Special Agent")
            world.set_rule(war_sp_agent_complete, HasAll("WAR! - Special Agent", "Phoenix"))


            # Stage 21 - The Duel
            duel_sp_agent_obj_1 = world.get_location("The Duel - Special Agent Objective 1")
            world.set_rule(duel_sp_agent_obj_1, HasAll("The Duel - Special Agent", "Falcon 2 (Scope)"))

            duel_sp_agent_obj_2 = world.get_location("The Duel - Special Agent Objective 2")
            world.set_rule(duel_sp_agent_obj_2, HasAll("The Duel - Special Agent", "Falcon 2 (Scope)"))

            duel_sp_agent_complete = world.get_location("Complete: The Duel - Special Agent")
            world.set_rule(duel_sp_agent_complete, HasAll("The Duel - Special Agent", "Falcon 2 (Scope)"))


        if world.options.perfect_agent:
            # Stage 1 - Defection
            defection_prf_agent_obj_1 = world.get_location("dD Defection - Perfect Agent Objective 1")
            world.set_rule(defection_prf_agent_obj_1, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Falcon 2 (Silencer)"))

            defection_prf_agent_obj_2 = world.get_location("dD Defection - Perfect Agent Objective 2")
            world.set_rule(defection_prf_agent_obj_2, HasAll("dD Defection - Perfect Agent", "Falcon 2 (Silencer)") & HAS_DD_KEYS)

            defection_prf_agent_obj_3 = world.get_location("dD Defection - Perfect Agent Objective 3")
            world.set_rule(defection_prf_agent_obj_3, HasAll("dD Defection - Perfect Agent", "Data Uplink", "Falcon 2 (Silencer)", "CMP150"))

            defection_prf_agent_obj_4 = world.get_location("dD Defection - Perfect Agent Objective 4")
            world.set_rule(defection_prf_agent_obj_4, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150"))

            defection_prf_agent_obj_5 = world.get_location("dD Defection - Perfect Agent Objective 5")
            world.set_rule(defection_prf_agent_obj_5, HasAll("dD Defection - Perfect Agent", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)

            defection_prf_agent_complete = world.get_location("Complete: dD Defection - Perfect Agent")
            world.set_rule(defection_prf_agent_complete, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)


            # Stage 2 - Investigation
            investigation_prf_agent_obj_1 = world.get_location("dD Investigation - Perfect Agent Objective 1")
            world.set_rule(investigation_prf_agent_obj_1, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2"))

            investigation_prf_agent_obj_2 = world.get_location("dD Investigation - Perfect Agent Objective 2")
            world.set_rule(investigation_prf_agent_obj_2, HasAll("dD Investigation - Perfect Agent", "Falcon 2"))

            investigation_prf_agent_obj_3 = world.get_location("dD Investigation - Perfect Agent Objective 3")
            world.set_rule(investigation_prf_agent_obj_3, HasAll("dD Investigation - Perfect Agent", "Falcon 2", "CMP150"))

            investigation_prf_agent_obj_4 = world.get_location("dD Investigation - Perfect Agent Objective 4")
            world.set_rule(investigation_prf_agent_obj_4, HasAll("dD Investigation - Perfect Agent", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))

            investigation_prf_agent_obj_5 = world.get_location("dD Investigation - Perfect Agent Objective 5")
            world.set_rule(investigation_prf_agent_obj_5, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))

            investigation_prf_agent_complete = world.get_location("Complete: dD Investigation - Perfect Agent")
            world.set_rule(investigation_prf_agent_complete, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))
            

            # Stage 3 - Extraction
            extraction_prf_agent_obj_1 = world.get_location("dD Extraction - Perfect Agent Objective 1")
            world.set_rule(extraction_prf_agent_obj_1, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)"))

            extraction_prf_agent_obj_2 = world.get_location("dD Extraction - Perfect Agent Objective 2")
            world.set_rule(extraction_prf_agent_obj_2, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun"))

            extraction_prf_agent_obj_3 = world.get_location("dD Extraction - Perfect Agent Objective 3")
            world.set_rule(extraction_prf_agent_obj_3, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher"))

            extraction_prf_agent_obj_4 = world.get_location("dD Extraction - Perfect Agent Objective 4")
            world.set_rule(extraction_prf_agent_obj_4, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))

            extraction_prf_agent_obj_5 = world.get_location("dD Extraction - Perfect Agent Objective 5")
            world.set_rule(extraction_prf_agent_obj_5, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))

            extraction_prf_agent_complete = world.get_location("Complete: dD Extraction - Perfect Agent")
            world.set_rule(extraction_prf_agent_complete, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher"))


            # Stage 4 - Villa
            if world.options.mission_logic.value == MissionLogic.option_normal:
                villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
                world.set_rule(villa_prf_agent_obj_1, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun"))

                villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
                world.set_rule(villa_prf_agent_obj_2, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun"))

                villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
                world.set_rule(villa_prf_agent_obj_3, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150"))

                villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
                world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

                villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
                world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"))

                villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
                world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
                world.set_rule(villa_prf_agent_obj_1, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun"))

                villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
                world.set_rule(villa_prf_agent_obj_2, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun"))

                villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
                world.set_rule(villa_prf_agent_obj_3, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150")
                                                      | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle"))

                villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
                world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

                villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
                world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card")
                                                      | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card"))

                villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
                world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card")
                                                         | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card"))


            # Stage 5 - Chicago
            if world.options.mission_logic.value == MissionLogic.option_normal:
                chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
                world.set_rule(chicago_prf_agent_obj_1, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
                world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
                world.set_rule(chicago_prf_agent_obj_3, HasAll("Chicago - Perfect Agent", "Remote Mine", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
                world.set_rule(chicago_prf_agent_obj_4, HasAll("Chicago - Perfect Agent", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
                world.set_rule(chicago_prf_agent_obj_5, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))
                
                chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
                world.set_rule(chicago_prf_agent_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
                world.set_rule(chicago_prf_agent_obj_1, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
                world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
                world.set_rule(chicago_prf_agent_obj_3, HasAll("Chicago - Perfect Agent", "Remote Mine", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
                world.set_rule(chicago_prf_agent_obj_4, HasAll("Chicago - Perfect Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                        | HasAll("Chicago - Perfect Agent", "CamSpy", "Falcon 2 (Scope)"))

                chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
                world.set_rule(chicago_prf_agent_obj_5, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))
                
                chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
                world.set_rule(chicago_prf_agent_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))


            # Stage 6 - G5 Building
            g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
            world.set_rule(g5_prf_agent_obj_1, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)

            g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
            world.set_rule(g5_prf_agent_obj_2, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)

            g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
            world.set_rule(g5_prf_agent_obj_3, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)

            g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
            world.set_rule(g5_prf_agent_obj_4, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
            world.set_rule(g5_prf_agent_obj_5, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "Remote Mine") & HAS_G5_KEYS)

            g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
            world.set_rule(g5_prf_agent_complete, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
            

            # Stage 7 - Infiltration
            infiltration_prf_agent_obj_1 = world.get_location("A51 Infiltration - Perfect Agent Objective 1")
            world.set_rule(infiltration_prf_agent_obj_1, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Explosives"))

            infiltration_prf_agent_obj_2 = world.get_location("A51 Infiltration - Perfect Agent Objective 2")
            world.set_rule(infiltration_prf_agent_obj_2, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Comms Rider"))

            infiltration_prf_agent_obj_3 = world.get_location("A51 Infiltration - Perfect Agent Objective 3")
            world.set_rule(infiltration_prf_agent_obj_3, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4"))

            infiltration_prf_agent_obj_4 = world.get_location("A51 Infiltration - Perfect Agent Objective 4")
            world.set_rule(infiltration_prf_agent_obj_4, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)

            infiltration_prf_agent_obj_5 = world.get_location("A51 Infiltration - Perfect Agent Objective 5")
            world.set_rule(infiltration_prf_agent_obj_5, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)

            infiltration_prf_agent_complete = world.get_location("Complete: A51 Infiltration - Perfect Agent")
            world.set_rule(infiltration_prf_agent_complete, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)


            # Stage 8 - Rescue
            rescue_prf_agent_obj_1 = world.get_location("A51 Rescue - Perfect Agent Objective 1")
            world.set_rule(rescue_prf_agent_obj_1, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink"))

            rescue_prf_agent_obj_2 = world.get_location("A51 Rescue - Perfect Agent Objective 2")
            world.set_rule(rescue_prf_agent_obj_2, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "X-Ray Scanner"))

            rescue_prf_agent_obj_3 = world.get_location("A51 Rescue - Perfect Agent Objective 3")
            world.set_rule(rescue_prf_agent_obj_3, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes"))

            rescue_prf_agent_obj_4 = world.get_location("A51 Rescue - Perfect Agent Objective 4")
            world.set_rule(rescue_prf_agent_obj_4, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)

            rescue_prf_agent_obj_5 = world.get_location("A51 Rescue - Perfect Agent Objective 5")
            world.set_rule(rescue_prf_agent_obj_5, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
            
            rescue_prf_agent_complete = world.get_location("Complete: A51 Rescue - Perfect Agent")
            world.set_rule(rescue_prf_agent_complete, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


            # Stage 9 - Escape
            escape_prf_agent_obj_1 = world.get_location("A51 Escape - Perfect Agent Objective 1")
            world.set_rule(escape_prf_agent_obj_1, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))

            escape_prf_agent_obj_2 = world.get_location("A51 Escape - Perfect Agent Objective 2")
            world.set_rule(escape_prf_agent_obj_2, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_prf_agent_obj_3 = world.get_location("A51 Escape - Perfect Agent Objective 3")
            world.set_rule(escape_prf_agent_obj_3, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_prf_agent_obj_4 = world.get_location("A51 Escape - Perfect Agent Objective 4")
            world.set_rule(escape_prf_agent_obj_4, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))

            escape_prf_agent_obj_5 = world.get_location("A51 Escape - Perfect Agent Objective 5")
            world.set_rule(escape_prf_agent_obj_5, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))
            
            escape_prf_agent_complete = world.get_location("Complete: A51 Escape - Perfect Agent")
            world.set_rule(escape_prf_agent_complete, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Stage 10 - Air Base
            if world.options.mission_logic.value == MissionLogic.option_normal:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Flight Plans")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Flight Plans"))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Flight Plans")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Flight Plans")
                                                         | HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "Proximity Mine", "Stewardess Disguise", "Flight Plans")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "Proximity Mine", "Stewardess Disguise", "Flight Plans"))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))


            # Stage 11 - Air Force One
            if world.options.mission_logic.value == MissionLogic.option_normal:
                air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
                world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
                world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
                world.set_rule(air_force_one_prf_agent_obj_3, HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
                world.set_rule(air_force_one_prf_agent_obj_4, HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
                world.set_rule(air_force_one_prf_agent_obj_5, HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
                world.set_rule(air_force_one_prf_agent_complete, HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
                world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
                world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

                air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
                world.set_rule(air_force_one_prf_agent_obj_3, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger") & HAS_AFO_LIFT_KEY)
                                                              | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger") & HAS_AFO_ALL_KEYS))

                air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
                world.set_rule(air_force_one_prf_agent_obj_4, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                              | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_ALL_KEYS))

                air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
                world.set_rule(air_force_one_prf_agent_obj_5, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                              | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_ALL_KEYS))

                air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
                world.set_rule(air_force_one_prf_agent_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                                 | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


            # Stage 12 - Crash Site
            if world.options.mission_logic.value == MissionLogic.option_normal:
                crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
                world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "President Scanner"))

                crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
                world.set_rule(crash_site_prf_agent_obj_2, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)"))

                crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
                world.set_rule(crash_site_prf_agent_obj_3, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "Remote Mine"))

                crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
                world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))

                crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
                world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
                
                crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
                world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
                world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "President Scanner"))

                crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
                world.set_rule(crash_site_prf_agent_obj_2, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)"))

                crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
                world.set_rule(crash_site_prf_agent_obj_3, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "Remote Mine")
                                                           | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"))

                crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
                world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))

                crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
                world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
                
                crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
                world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine")
                                                              | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"))


            # Stage 13 - Pelagic II
            pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
            world.set_rule(pelagic_prf_agent_obj_1, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "X-Ray Scanner"))

            pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
            world.set_rule(pelagic_prf_agent_obj_2, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "Research Tape"))

            pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
            world.set_rule(pelagic_prf_agent_obj_3, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun"))

            pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
            world.set_rule(pelagic_prf_agent_obj_4, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun"))

            pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
            world.set_rule(pelagic_prf_agent_obj_5, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))
            
            pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
            world.set_rule(pelagic_prf_agent_complete, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))


            # Stage 14 - Deep Sea
            deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
            world.set_rule(deep_sea_prf_agent_obj_1, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner"))

            deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
            world.set_rule(deep_sea_prf_agent_obj_2, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20"))

            deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
            world.set_rule(deep_sea_prf_agent_obj_3, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20"))

            deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
            world.set_rule(deep_sea_prf_agent_obj_4, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))

            deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
            world.set_rule(deep_sea_prf_agent_obj_5, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))
            
            deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
            world.set_rule(deep_sea_prf_agent_complete, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))


            # Stage 15 - Carrington Institute Defense
            if world.options.mission_logic.value == MissionLogic.option_normal:
                institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
                world.set_rule(institute_defense_prf_agent_obj_1, HasAll("CI Defense - Perfect Agent", "AR34"))

                institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
                world.set_rule(institute_defense_prf_agent_obj_2, HasAll("CI Defense - Perfect Agent", "AR34"))

                institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
                world.set_rule(institute_defense_prf_agent_obj_3, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120"))

                institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
                world.set_rule(institute_defense_prf_agent_obj_4, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser"))

                institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
                world.set_rule(institute_defense_prf_agent_obj_5, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink"))

                institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
                world.set_rule(institute_defense_prf_agent_complete, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
                world.set_rule(institute_defense_prf_agent_obj_1, HasAll("CI Defense - Perfect Agent", "AR34"))

                institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
                world.set_rule(institute_defense_prf_agent_obj_2, HasAll("CI Defense - Perfect Agent", "AR34"))

                institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
                world.set_rule(institute_defense_prf_agent_obj_3, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120"))

                institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
                world.set_rule(institute_defense_prf_agent_obj_4, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser")
                                                                  | HasAll("CI Defense - Perfect Agent", "AR34", "Devastator"))

                institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
                world.set_rule(institute_defense_prf_agent_obj_5, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                                  | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))

                institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
                world.set_rule(institute_defense_prf_agent_complete, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                                     | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
            world.set_rule(attack_ship_prf_agent_obj_1, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler"))

            attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
            world.set_rule(attack_ship_prf_agent_obj_2, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler"))

            attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
            world.set_rule(attack_ship_prf_agent_obj_3, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
            world.set_rule(attack_ship_prf_agent_obj_4, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
            world.set_rule(attack_ship_prf_agent_obj_5, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
            world.set_rule(attack_ship_prf_agent_complete, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
            world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
            world.set_rule(skedar_ruins_prf_agent_obj_2, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
            world.set_rule(skedar_ruins_prf_agent_obj_3, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
            world.set_rule(skedar_ruins_prf_agent_obj_4, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
            world.set_rule(skedar_ruins_prf_agent_obj_5, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
            world.set_rule(skedar_ruins_prf_agent_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            world.set_rule(mbr_prf_agent_obj_1, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb"))

            mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            world.set_rule(mbr_prf_agent_obj_2, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device"))

            mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            world.set_rule(mbr_prf_agent_obj_3, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device"))

            mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
            world.set_rule(mbr_prf_agent_complete, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device", "Skedar Bomb"))


            # Stage 19 - Maian SOS
            maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
            world.set_rule(maian_sos_prf_agent_obj_1, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
            world.set_rule(maian_sos_prf_agent_obj_2, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon", "DY357-LX"))

            maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
            world.set_rule(maian_sos_prf_agent_obj_3, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
            world.set_rule(maian_sos_prf_agent_complete, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon", "DY357-LX"))


            # Stage 20 - WAR!
            war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
            world.set_rule(war_prf_agent_obj_1, HasAll("WAR! - Perfect Agent", "Phoenix"))

            war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
            world.set_rule(war_prf_agent_obj_2, HasAll("WAR! - Perfect Agent", "Phoenix"))

            war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
            world.set_rule(war_prf_agent_obj_3, HasAll("WAR! - Perfect Agent", "Phoenix"))

            war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
            world.set_rule(war_prf_agent_complete, HasAll("WAR! - Perfect Agent", "Phoenix"))


            # Stage 21 - The Duel
            duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
            world.set_rule(duel_prf_agent_obj_1, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))

            duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
            world.set_rule(duel_prf_agent_obj_2, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))

            duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
            world.set_rule(duel_prf_agent_obj_3, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))
            
            duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
            world.set_rule(duel_prf_agent_complete, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))


        if world.options.unlock_cheats:
            # Defection
            cheat_defection_complete = world.get_location("Cheat Unlock: Complete dD Defection")
            world.set_rule(cheat_defection_complete, HasAll("dD Defection - Agent", "Falcon 2 (Silencer)", "CMP150")
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS))


            # Investigation
            cheat_investigation_complete = world.get_location("Cheat Unlock: Complete dD Investigation")
            world.set_rule(cheat_investigation_complete, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink")
                                                         | HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink")
                                                         | HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


            # Extraction
            cheat_extraction_complete = world.get_location("Cheat Unlock: Complete dD Extraction")
            world.set_rule(cheat_extraction_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun", "Rocket Launcher"))


            # Villa
            if world.options.mission_logic.value == MissionLogic.option_normal:
                cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
                world.set_rule(cheat_villa_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
                world.set_rule(cheat_villa_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card"))


            # Chicago
            cheat_chicago_complete = world.get_location("Cheat Unlock: Complete Chicago")
            world.set_rule(cheat_chicago_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))


            # G5 Building
            cheat_g5_complete = world.get_location("Cheat Unlock: Complete G5 Building")
            world.set_rule(cheat_g5_complete, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS))


            # Infiltration
            cheat_infiltration_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration")
            world.set_rule(cheat_infiltration_complete, (HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))


            # Rescue
            cheat_rescue_complete = world.get_location("Cheat Unlock: Complete A51 Rescue")
            world.set_rule(cheat_rescue_complete, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))


            # Escape
            cheat_escape_complete = world.get_location("Cheat Unlock: Complete A51 Escape")
            world.set_rule(cheat_escape_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Air Base
            cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
            world.set_rule(cheat_air_base_complete, HasAll("Air Base - Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                    | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))
    

            # Air Force One
            if world.options.mission_logic.value == MissionLogic.option_normal:
                cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
                world.set_rule(cheat_air_force_one_complete, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine")
                                                             | (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
                world.set_rule(cheat_air_force_one_complete, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine")
                                                             | (HasAll("Air Force One - Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_EXTRA_KEYS)
                                                             | (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS)
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


            # Crash Site
            if world.options.mission_logic.value == MissionLogic.option_normal:
                cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
                world.set_rule(cheat_crash_site_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                          | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
                world.set_rule(cheat_crash_site_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                          | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"))


            # Pelagic II
            cheat_pelagic_complete = world.get_location("Cheat Unlock: Complete Pelagic II")
            world.set_rule(cheat_pelagic_complete, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))


            # Deep Sea
            cheat_deep_sea_complete = world.get_location("Cheat Unlock: Complete Deep Sea")
            world.set_rule(cheat_deep_sea_complete, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))


            # CI Defense
            if world.options.mission_logic.value == MissionLogic.option_normal:
                cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
                world.set_rule(cheat_institute_defense_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink")
                                                                 | HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink")
                                                                 | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink"))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
                world.set_rule(cheat_institute_defense_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink")
                                                                 | HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink")
                                                                 | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                                 | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))


            # Attack Ship
            cheat_attack_ship_complete = world.get_location("Cheat Unlock: Complete Attack Ship")
            world.set_rule(cheat_attack_ship_complete, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34")
                                                       | HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34")
                                                       | HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))


            # Skedar Ruins
            cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
            world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))
                                                        | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))
                                                        | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")))


            if world.options.agent:
                # Extraction
                cheat_extraction_timed_complete = world.get_location("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
                world.set_rule(cheat_extraction_timed_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Shotgun"))


                # G5 Building
                cheat_g5_timed_complete = world.get_location("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
                world.set_rule(cheat_g5_timed_complete, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)


                # Escape
                cheat_escape_timed_complete = world.get_location("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
                world.set_rule(cheat_escape_timed_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


                # Crash Site
                cheat_crash_site_timed_complete = world.get_location("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
                world.set_rule(cheat_crash_site_timed_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))


                # CI Defense
                cheat_institute_defense_timed_complete = world.get_location("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")
                world.set_rule(cheat_institute_defense_timed_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))

            if world.options.special_agent:
                # Defection
                cheat_defection_timed_complete = world.get_location("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
                world.set_rule(cheat_defection_timed_complete, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)


                # Villa
                cheat_villa_timed_complete = world.get_location("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
                world.set_rule(cheat_villa_timed_complete, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))


                # Infiltration
                cheat_infiltration_timed_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
                world.set_rule(cheat_infiltration_timed_complete, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)


                # Air Base
                cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                                      | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase"))


                # Pelagic II
                cheat_pelagic_timed_complete = world.get_location("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
                world.set_rule(cheat_pelagic_timed_complete, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))


                # Attack Ship
                cheat_attack_ship_timed_complete = world.get_location("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")
                world.set_rule(cheat_attack_ship_timed_complete, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            if world.options.perfect_agent:
                # Investigation
                cheat_investigation_timed_complete = world.get_location("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
                world.set_rule(cheat_investigation_timed_complete, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


                # Chicago
                cheat_chicago_timed_complete = world.get_location("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
                world.set_rule(cheat_chicago_timed_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))


                # Rescue
                cheat_rescue_timed_complete = world.get_location("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
                world.set_rule(cheat_rescue_timed_complete, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


                # Air Force One
                if world.options.mission_logic.value == MissionLogic.option_normal:
                    cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                    world.set_rule(cheat_air_force_one_timed_complete, HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                
                elif world.options.mission_logic.value == MissionLogic.option_veteran:
                    cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                    world.set_rule(cheat_air_force_one_timed_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                                       | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


                # Deep Sea
                cheat_deep_sea_timed_complete = world.get_location("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
                world.set_rule(cheat_deep_sea_timed_complete, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))


                # Skedar Ruins
                cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                world.set_rule(cheat_skedar_ruins_timed_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


    elif world.options.weapon_progression.value > WeaponProgression.option_vanilla:
        if world.options.agent:
            # Stage 1 - Defection
            defection_agent_obj_1 = world.get_location("dD Defection - Agent Objective 1")
            world.set_rule(defection_agent_obj_1, Has("dD Defection - Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_agent_complete = world.get_location("Complete: dD Defection - Agent")
            world.set_rule(defection_agent_complete, Has("dD Defection - Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))


            # Stage 2 - Investigation
            investigation_agent_obj_1 = world.get_location("dD Investigation - Agent Objective 1")
            world.set_rule(investigation_agent_obj_1, HasAll("dD Investigation - Agent", "CamSpy")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_agent_obj_2 = world.get_location("dD Investigation - Agent Objective 2")
            world.set_rule(investigation_agent_obj_2, HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_agent_complete = world.get_location("Complete: dD Investigation - Agent")
            world.set_rule(investigation_agent_complete, HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
            

            # Stage 3 - Extraction
            extraction_agent_obj_1 = world.get_location("dD Extraction - Agent Objective 1")
            world.set_rule(extraction_agent_obj_1, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            extraction_agent_obj_2 = world.get_location("dD Extraction - Agent Objective 2")
            world.set_rule(extraction_agent_obj_2, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_agent_obj_3 = world.get_location("dD Extraction - Agent Objective 3")
            world.set_rule(extraction_agent_obj_3, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_agent_complete = world.get_location("Complete: dD Extraction - Agent")
            world.set_rule(extraction_agent_complete, HasAll("dD Extraction - Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 4 - Villa
            villa_agent_obj_1 = world.get_location("Carrington Villa - Agent Objective 1")
            world.set_rule(villa_agent_obj_1, Has("Carrington Villa - Agent")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_agent_obj_2 = world.get_location("Carrington Villa - Agent Objective 2")
            world.set_rule(villa_agent_obj_2, Has("Carrington Villa - Agent")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_agent_obj_3 = world.get_location("Carrington Villa - Agent Objective 3")
            world.set_rule(villa_agent_obj_3, HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_agent_complete = world.get_location("Complete: Carrington Villa - Agent")
            world.set_rule(villa_agent_complete, HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            if world.options.mission_logic.value == MissionLogic.option_normal:
                chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
                world.set_rule(chicago_agent_obj_1, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                    | (HasAll("Chicago - Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
                world.set_rule(chicago_agent_obj_2, HasAll("Chicago - Agent", "Data Uplink")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

                chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
                world.set_rule(chicago_agent_obj_3, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
                
                chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
                world.set_rule(chicago_agent_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Agent", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
                world.set_rule(chicago_agent_obj_1, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                    | (HasAll("Chicago - Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
                world.set_rule(chicago_agent_obj_2, (HasAll("Chicago - Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Agent", "CamSpy")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

                chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
                world.set_rule(chicago_agent_obj_3, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
                
                chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
                world.set_rule(chicago_agent_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Agent", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_agent_obj_1 = world.get_location("G5 Building - Agent Objective 1")
            world.set_rule(g5_agent_obj_1, HasAll("G5 Building - Agent", "CamSpy") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_obj_2 = world.get_location("G5 Building - Agent Objective 2")
            world.set_rule(g5_agent_obj_2, HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_obj_3 = world.get_location("G5 Building - Agent Objective 3")
            world.set_rule(g5_agent_obj_3, HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_complete = world.get_location("Complete: G5 Building - Agent")
            world.set_rule(g5_agent_complete, HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 7 - Infiltration
            infiltration_agent_obj_1 = world.get_location("A51 Infiltration - Agent Objective 1")
            world.set_rule(infiltration_agent_obj_1, HasAll("A51 Infiltration - Agent", "Explosives")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_obj_2 = world.get_location("A51 Infiltration - Agent Objective 2")
            world.set_rule(infiltration_agent_obj_2, HasAll("A51 Infiltration - Agent") & HAS_A51_INFIL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_obj_3 = world.get_location("A51 Infiltration - Agent Objective 3")
            world.set_rule(infiltration_agent_obj_3, HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_complete = world.get_location("Complete: A51 Infiltration - Agent")
            world.set_rule(infiltration_agent_complete, HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_agent_obj_1 = world.get_location("A51 Rescue - Agent Objective 1")
            world.set_rule(rescue_agent_obj_1, HasAll("A51 Rescue - Agent", "Lab Clothes")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_agent_obj_2 = world.get_location("A51 Rescue - Agent Objective 2")
            world.set_rule(rescue_agent_obj_2, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_agent_obj_3 = world.get_location("A51 Rescue - Agent Objective 3")
            world.set_rule(rescue_agent_obj_3, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_agent_complete = world.get_location("Complete: A51 Rescue - Agent")
            world.set_rule(rescue_agent_complete, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_agent_obj_1 = world.get_location("A51 Escape - Agent Objective 1")
            world.set_rule(escape_agent_obj_1, Has("A51 Escape - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_agent_obj_2 = world.get_location("A51 Escape - Agent Objective 2")
            world.set_rule(escape_agent_obj_2, Has("A51 Escape - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_agent_obj_3 = world.get_location("A51 Escape - Agent Objective 3")
            world.set_rule(escape_agent_obj_3, HasAll("A51 Escape - Agent", "Alien Medpack")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_agent_complete = world.get_location("Complete: A51 Escape - Agent")
            world.set_rule(escape_agent_complete, HasAll("A51 Escape - Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
                world.set_rule(air_base_agent_obj_1, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                     | (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")))

                air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
                world.set_rule(air_base_agent_obj_2, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                     | (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")))

                air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
                world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "Stewardess Disguise")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                
                air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
                world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
                world.set_rule(air_base_agent_obj_1, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

                air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
                world.set_rule(air_base_agent_obj_2, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

                air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
                world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

                air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
                world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 11 - Air Force One
            air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
            world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

            air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
            world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Suitcase")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
            world.set_rule(air_force_one_agent_obj_3, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Air Force One - Agent", "Suitcase")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
            world.set_rule(air_force_one_agent_complete, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Agent", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_agent_obj_1 = world.get_location("Crash Site - Agent Objective 1")
            world.set_rule(crash_site_agent_obj_1, Has("Crash Site - Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_agent_obj_2 = world.get_location("Crash Site - Agent Objective 2")
            world.set_rule(crash_site_agent_obj_2, HasAll("Crash Site - Agent", "President Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_agent_obj_3 = world.get_location("Crash Site - Agent Objective 3")
            world.set_rule(crash_site_agent_obj_3, HasAll("Crash Site - Agent", "President Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_agent_complete = world.get_location("Complete: Crash Site - Agent")
            world.set_rule(crash_site_agent_complete, HasAll("Crash Site - Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_agent_obj_1 = world.get_location("Pelagic II - Agent Objective 1")
            world.set_rule(pelagic_agent_obj_1, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_agent_obj_2 = world.get_location("Pelagic II - Agent Objective 2")
            world.set_rule(pelagic_agent_obj_2, Has("Pelagic II - Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_agent_obj_3 = world.get_location("Pelagic II - Agent Objective 3")
            world.set_rule(pelagic_agent_obj_3, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_agent_complete = world.get_location("Complete: Pelagic II - Agent")
            world.set_rule(pelagic_agent_complete, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_agent_obj_1 = world.get_location("Deep Sea - Agent Objective 1")
            world.set_rule(deep_sea_agent_obj_1, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_obj_2 = world.get_location("Deep Sea - Agent Objective 2")
            world.set_rule(deep_sea_agent_obj_2, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_obj_3 = world.get_location("Deep Sea - Agent Objective 3")
            world.set_rule(deep_sea_agent_obj_3, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_complete = world.get_location("Complete: Deep Sea - Agent")
            world.set_rule(deep_sea_agent_complete, HasAll("Deep Sea - Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 15 - Carrington Institute Defense
            institute_defense_agent_obj_1 = world.get_location("CI Defense - Agent Objective 1")
            world.set_rule(institute_defense_agent_obj_1, Has("CI Defense - Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_agent_obj_2 = world.get_location("CI Defense - Agent Objective 2")
            world.set_rule(institute_defense_agent_obj_2, (HasAll("CI Defense - Agent", "RC-P120")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                          | (Has("CI Defense - Agent")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_agent_obj_3 = world.get_location("CI Defense - Agent Objective 3")
            world.set_rule(institute_defense_agent_obj_3, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                          | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_agent_complete = world.get_location("Complete: CI Defense - Agent")
            world.set_rule(institute_defense_agent_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_agent_obj_1 = world.get_location("Attack Ship - Agent Objective 1")
            world.set_rule(attack_ship_agent_obj_1, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_obj_2 = world.get_location("Attack Ship - Agent Objective 2")
            world.set_rule(attack_ship_agent_obj_2, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_obj_3 = world.get_location("Attack Ship - Agent Objective 3")
            world.set_rule(attack_ship_agent_obj_3, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_complete = world.get_location("Complete: Attack Ship - Agent")
            world.set_rule(attack_ship_agent_complete, Has("Attack Ship - Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
                world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
                world.set_rule(skedar_ruins_agent_obj_2, (HAS_SKEDAR_RUINS_AGENT & Has("Devastator")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                         | (HAS_SKEDAR_RUINS_AGENT
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
                world.set_rule(skedar_ruins_agent_obj_3, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                         | (HAS_SKEDAR_RUINS_AGENT & HasAll("IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
                world.set_rule(skedar_ruins_agent_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
                world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
                world.set_rule(skedar_ruins_agent_obj_2, HAS_SKEDAR_RUINS_AGENT & Has("Devastator")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
                world.set_rule(skedar_ruins_agent_obj_3, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "IR Scanner")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
                world.set_rule(skedar_ruins_agent_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Agent Objective 1")
            world.set_rule(mbr_agent_obj_1, HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Agent")
            world.set_rule(mbr_agent_complete, HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_agent_obj_1 = world.get_location("Maian SOS - Agent Objective 1")
            world.set_rule(maian_sos_agent_obj_1, Has("Maian SOS - Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_agent_complete = world.get_location("Complete: Maian SOS - Agent")
            world.set_rule(maian_sos_agent_complete, Has("Maian SOS - Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 20 - WAR!
            war_agent_obj_1 = world.get_location("WAR! - Agent Objective 1")
            world.set_rule(war_agent_obj_1, Has("WAR! - Agent")
                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_agent_complete = world.get_location("Complete: WAR! - Agent")
            world.set_rule(war_agent_complete, Has("WAR! - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_agent_obj_1 = world.get_location("The Duel - Agent Objective 1")
            world.set_rule(duel_agent_obj_1, Has("The Duel - Agent")
                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_agent_complete = world.get_location("Complete: The Duel - Agent")
            world.set_rule(duel_agent_complete, Has("The Duel - Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


        if world.options.special_agent:
            # Stage 1 - Defection
            defection_sp_agent_obj_1 = world.get_location("dD Defection - Special Agent Objective 1")
            world.set_rule(defection_sp_agent_obj_1, HasAll("dD Defection - Special Agent", "ECM Mine")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_sp_agent_obj_2 = world.get_location("dD Defection - Special Agent Objective 2")
            world.set_rule(defection_sp_agent_obj_2, Has("dD Defection - Special Agent") & HAS_DD_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_sp_agent_obj_3 = world.get_location("dD Defection - Special Agent Objective 3")
            world.set_rule(defection_sp_agent_obj_3, HasAll("dD Defection - Special Agent", "ECM Mine")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_sp_agent_obj_4 = world.get_location("dD Defection - Special Agent Objective 4")
            world.set_rule(defection_sp_agent_obj_4, Has("dD Defection - Special Agent") & HAS_DD_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_sp_agent_complete = world.get_location("Complete: dD Defection - Special Agent")
            world.set_rule(defection_sp_agent_complete, HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 2 - Investigation
            investigation_sp_agent_obj_1 = world.get_location("dD Investigation - Special Agent Objective 1")
            world.set_rule(investigation_sp_agent_obj_1, HasAll("dD Investigation - Special Agent", "CamSpy")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_sp_agent_obj_2 = world.get_location("dD Investigation - Special Agent Objective 2")
            world.set_rule(investigation_sp_agent_obj_2, Has("dD Investigation - Special Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_sp_agent_obj_3 = world.get_location("dD Investigation - Special Agent Objective 3")
            world.set_rule(investigation_sp_agent_obj_3, Has("dD Investigation - Special Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_sp_agent_obj_4 = world.get_location("dD Investigation - Special Agent Objective 4")
            world.set_rule(investigation_sp_agent_obj_4, HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_sp_agent_complete = world.get_location("Complete: dD Investigation - Special Agent")
            world.set_rule(investigation_sp_agent_complete, HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
            

            # Stage 3 - Extraction
            extraction_sp_agent_obj_1 = world.get_location("dD Extraction - Special Agent Objective 1")
            world.set_rule(extraction_sp_agent_obj_1, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            extraction_sp_agent_obj_2 = world.get_location("dD Extraction - Special Agent Objective 2")
            world.set_rule(extraction_sp_agent_obj_2, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))

            extraction_sp_agent_obj_3 = world.get_location("dD Extraction - Special Agent Objective 3")
            world.set_rule(extraction_sp_agent_obj_3, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_obj_4 = world.get_location("dD Extraction - Special Agent Objective 4")
            world.set_rule(extraction_sp_agent_obj_4, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_complete = world.get_location("Complete: dD Extraction - Special Agent")
            world.set_rule(extraction_sp_agent_complete, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))


            # Stage 4 - Villa
            villa_sp_agent_obj_1 = world.get_location("Carrington Villa - Special Agent Objective 1")
            world.set_rule(villa_sp_agent_obj_1, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_obj_2 = world.get_location("Carrington Villa - Special Agent Objective 2")
            world.set_rule(villa_sp_agent_obj_2, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_obj_3 = world.get_location("Carrington Villa - Special Agent Objective 3")
            world.set_rule(villa_sp_agent_obj_3, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_sp_agent_obj_4 = world.get_location("Carrington Villa - Special Agent Objective 4")
            world.set_rule(villa_sp_agent_obj_4, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_complete = world.get_location("Complete: Carrington Villa - Special Agent")
            world.set_rule(villa_sp_agent_complete, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            if world.options.mission_logic.value == MissionLogic.option_normal:
                chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
                world.set_rule(chicago_sp_agent_obj_1, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                       | (HasAll("Chicago - Special Agent", "Data Uplink")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
                world.set_rule(chicago_sp_agent_obj_2, (HasAll("Chicago - Special Agent", "Remote Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (Has("Chicago - Special Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
                world.set_rule(chicago_sp_agent_obj_3, HasAll("Chicago - Special Agent", "Data Uplink")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

                chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
                world.set_rule(chicago_sp_agent_obj_4, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
                
                chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
                world.set_rule(chicago_sp_agent_complete, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
                world.set_rule(chicago_sp_agent_obj_1, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                       | (HasAll("Chicago - Special Agent", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
                world.set_rule(chicago_sp_agent_obj_2, (HasAll("Chicago - Special Agent", "Remote Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (Has("Chicago - Special Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
                world.set_rule(chicago_sp_agent_obj_3, (HasAll("Chicago - Special Agent", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Special Agent", "CamSpy")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

                chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
                world.set_rule(chicago_sp_agent_obj_4, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
                
                chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
                world.set_rule(chicago_sp_agent_complete, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_sp_agent_obj_1 = world.get_location("G5 Building - Special Agent Objective 1")
            world.set_rule(g5_sp_agent_obj_1, Has("G5 Building - Special Agent") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_2 = world.get_location("G5 Building - Special Agent Objective 2")
            world.set_rule(g5_sp_agent_obj_2, HasAll("G5 Building - Special Agent", "CamSpy") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_3 = world.get_location("G5 Building - Special Agent Objective 3")
            world.set_rule(g5_sp_agent_obj_3, HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_4 = world.get_location("G5 Building - Special Agent Objective 4")
            world.set_rule(g5_sp_agent_obj_4, (HasAll("G5 Building - Special Agent", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (Has("G5 Building - Special Agent") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            g5_sp_agent_complete = world.get_location("Complete: G5 Building - Special Agent")
            world.set_rule(g5_sp_agent_complete, (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                 | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 7 - Infiltration
            infiltration_sp_agent_obj_1 = world.get_location("A51 Infiltration - Special Agent Objective 1")
            world.set_rule(infiltration_sp_agent_obj_1, HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_2 = world.get_location("A51 Infiltration - Special Agent Objective 2")
            world.set_rule(infiltration_sp_agent_obj_2, HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_3 = world.get_location("A51 Infiltration - Special Agent Objective 3")
            world.set_rule(infiltration_sp_agent_obj_3, HasAll("A51 Infiltration - Special Agent") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_4 = world.get_location("A51 Infiltration - Special Agent Objective 4")
            world.set_rule(infiltration_sp_agent_obj_4, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_complete = world.get_location("Complete: A51 Infiltration - Special Agent")
            world.set_rule(infiltration_sp_agent_complete, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_sp_agent_obj_1 = world.get_location("A51 Rescue - Special Agent Objective 1")
            world.set_rule(rescue_sp_agent_obj_1, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_2 = world.get_location("A51 Rescue - Special Agent Objective 2")
            world.set_rule(rescue_sp_agent_obj_2, HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_3 = world.get_location("A51 Rescue - Special Agent Objective 3")
            world.set_rule(rescue_sp_agent_obj_3, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_4 = world.get_location("A51 Rescue - Special Agent Objective 4")
            world.set_rule(rescue_sp_agent_obj_4, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_sp_agent_complete = world.get_location("Complete: A51 Rescue - Special Agent")
            world.set_rule(rescue_sp_agent_complete, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_sp_agent_obj_1 = world.get_location("A51 Escape - Special Agent Objective 1")
            world.set_rule(escape_sp_agent_obj_1, Has("A51 Escape - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_sp_agent_obj_2 = world.get_location("A51 Escape - Special Agent Objective 2")
            world.set_rule(escape_sp_agent_obj_2, Has("A51 Escape - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_sp_agent_obj_3 = world.get_location("A51 Escape - Special Agent Objective 3")
            world.set_rule(escape_sp_agent_obj_3, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_sp_agent_obj_4 = world.get_location("A51 Escape - Special Agent Objective 4")
            world.set_rule(escape_sp_agent_obj_4, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_sp_agent_complete = world.get_location("Complete: A51 Escape - Special Agent")
            world.set_rule(escape_sp_agent_complete, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
                world.set_rule(air_base_sp_agent_obj_1, (HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise")))

                air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
                world.set_rule(air_base_sp_agent_obj_2, (HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")))

                air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
                world.set_rule(air_base_sp_agent_obj_3, (HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise")))

                air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
                world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
                world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
                world.set_rule(air_base_sp_agent_obj_1, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

                air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
                world.set_rule(air_base_sp_agent_obj_2, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
                world.set_rule(air_base_sp_agent_obj_3, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

                air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
                world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
                world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


            # Stage 11 - Air Force One
            air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
            world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
            world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
            world.set_rule(air_force_one_sp_agent_obj_3, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
            world.set_rule(air_force_one_sp_agent_obj_4, (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
            world.set_rule(air_force_one_sp_agent_complete, (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                            | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_sp_agent_obj_1 = world.get_location("Crash Site - Special Agent Objective 1")
            world.set_rule(crash_site_sp_agent_obj_1, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_2 = world.get_location("Crash Site - Special Agent Objective 2")
            world.set_rule(crash_site_sp_agent_obj_2, Has("Crash Site - Special Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_3 = world.get_location("Crash Site - Special Agent Objective 3")
            world.set_rule(crash_site_sp_agent_obj_3, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_4 = world.get_location("Crash Site - Special Agent Objective 4")
            world.set_rule(crash_site_sp_agent_obj_4, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_sp_agent_complete = world.get_location("Complete: Crash Site - Special Agent")
            world.set_rule(crash_site_sp_agent_complete, HasAll("Crash Site - Special Agent", "President Scanner")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_sp_agent_obj_1 = world.get_location("Pelagic II - Special Agent Objective 1")
            world.set_rule(pelagic_sp_agent_obj_1, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_2 = world.get_location("Pelagic II - Special Agent Objective 2")
            world.set_rule(pelagic_sp_agent_obj_2, Has("Pelagic II - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_3 = world.get_location("Pelagic II - Special Agent Objective 3")
            world.set_rule(pelagic_sp_agent_obj_3, Has("Pelagic II - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_4 = world.get_location("Pelagic II - Special Agent Objective 4")
            world.set_rule(pelagic_sp_agent_obj_4, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_sp_agent_complete = world.get_location("Complete: Pelagic II - Special Agent")
            world.set_rule(pelagic_sp_agent_complete, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_sp_agent_obj_1 = world.get_location("Deep Sea - Special Agent Objective 1")
            world.set_rule(deep_sea_sp_agent_obj_1, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_2 = world.get_location("Deep Sea - Special Agent Objective 2")
            world.set_rule(deep_sea_sp_agent_obj_2, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_3 = world.get_location("Deep Sea - Special Agent Objective 3")
            world.set_rule(deep_sea_sp_agent_obj_3, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_4 = world.get_location("Deep Sea - Special Agent Objective 4")
            world.set_rule(deep_sea_sp_agent_obj_4, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            
            deep_sea_sp_agent_complete = world.get_location("Complete: Deep Sea - Special Agent")
            world.set_rule(deep_sea_sp_agent_complete, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 15 - Carrington Institute Defense
            institute_defense_sp_agent_obj_1 = world.get_location("CI Defense - Special Agent Objective 1")
            world.set_rule(institute_defense_sp_agent_obj_1, Has("CI Defense - Special Agent")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_sp_agent_obj_2 = world.get_location("CI Defense - Special Agent Objective 2")
            world.set_rule(institute_defense_sp_agent_obj_2, Has("CI Defense - Special Agent")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_sp_agent_obj_3 = world.get_location("CI Defense - Special Agent Objective 3")
            world.set_rule(institute_defense_sp_agent_obj_3, (HasAll("CI Defense - Special Agent", "RC-P120")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (Has("CI Defense - Special Agent")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_sp_agent_obj_4 = world.get_location("CI Defense - Special Agent Objective 4")
            world.set_rule(institute_defense_sp_agent_obj_4, (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_sp_agent_complete = world.get_location("Complete: CI Defense - Special Agent")
            world.set_rule(institute_defense_sp_agent_complete, (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_sp_agent_obj_1 = world.get_location("Attack Ship - Special Agent Objective 1")
            world.set_rule(attack_ship_sp_agent_obj_1, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_2 = world.get_location("Attack Ship - Special Agent Objective 2")
            world.set_rule(attack_ship_sp_agent_obj_2, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_3 = world.get_location("Attack Ship - Special Agent Objective 3")
            world.set_rule(attack_ship_sp_agent_obj_3, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_4 = world.get_location("Attack Ship - Special Agent Objective 4")
            world.set_rule(attack_ship_sp_agent_obj_4, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_complete = world.get_location("Complete: Attack Ship - Special Agent")
            world.set_rule(attack_ship_sp_agent_complete, Has("Attack Ship - Special Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            

            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
                world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
                world.set_rule(skedar_ruins_sp_agent_obj_2, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
                world.set_rule(skedar_ruins_sp_agent_obj_3, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))
                
                skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
                world.set_rule(skedar_ruins_sp_agent_obj_4, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
                world.set_rule(skedar_ruins_sp_agent_complete, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                               | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))
            
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
                world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                
                skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
                world.set_rule(skedar_ruins_sp_agent_obj_2, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
                world.set_rule(skedar_ruins_sp_agent_obj_3, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                
                skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
                world.set_rule(skedar_ruins_sp_agent_obj_4, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
                world.set_rule(skedar_ruins_sp_agent_complete, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            # Stage 18 - Mr. Blonde's Revenge
            mbr_sp_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 1")
            world.set_rule(mbr_sp_agent_obj_1, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_sp_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 2")
            world.set_rule(mbr_sp_agent_obj_2, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_sp_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Special Agent")
            world.set_rule(mbr_sp_agent_complete, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_sp_agent_obj_1 = world.get_location("Maian SOS - Special Agent Objective 1")
            world.set_rule(maian_sos_sp_agent_obj_1, Has("Maian SOS - Special Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_sp_agent_obj_2 = world.get_location("Maian SOS - Special Agent Objective 2")
            world.set_rule(maian_sos_sp_agent_obj_2, Has("Maian SOS - Special Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_sp_agent_complete = world.get_location("Complete: Maian SOS - Special Agent")
            world.set_rule(maian_sos_sp_agent_complete, Has("Maian SOS - Special Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 20 - WAR!
            war_sp_agent_obj_1 = world.get_location("WAR! - Special Agent Objective 1")
            world.set_rule(war_sp_agent_obj_1, Has("WAR! - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_sp_agent_obj_2 = world.get_location("WAR! - Special Agent Objective 2")
            world.set_rule(war_sp_agent_obj_2, Has("WAR! - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_sp_agent_complete = world.get_location("Complete: WAR! - Special Agent")
            world.set_rule(war_sp_agent_complete, Has("WAR! - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_sp_agent_obj_1 = world.get_location("The Duel - Special Agent Objective 1")
            world.set_rule(duel_sp_agent_obj_1, Has("The Duel - Special Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_sp_agent_obj_2 = world.get_location("The Duel - Special Agent Objective 2")
            world.set_rule(duel_sp_agent_obj_2, Has("The Duel - Special Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_sp_agent_complete = world.get_location("Complete: The Duel - Special Agent")
            world.set_rule(duel_sp_agent_complete, Has("The Duel - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


        if world.options.perfect_agent:
            # Stage 1 - Defection
            defection_prf_agent_obj_1 = world.get_location("dD Defection - Perfect Agent Objective 1")
            world.set_rule(defection_prf_agent_obj_1, HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_prf_agent_obj_2 = world.get_location("dD Defection - Perfect Agent Objective 2")
            world.set_rule(defection_prf_agent_obj_2, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_prf_agent_obj_3 = world.get_location("dD Defection - Perfect Agent Objective 3")
            world.set_rule(defection_prf_agent_obj_3, HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_obj_4 = world.get_location("dD Defection - Perfect Agent Objective 4")
            world.set_rule(defection_prf_agent_obj_4, HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_obj_5 = world.get_location("dD Defection - Perfect Agent Objective 5")
            world.set_rule(defection_prf_agent_obj_5, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_complete = world.get_location("Complete: dD Defection - Perfect Agent")
            world.set_rule(defection_prf_agent_complete, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink") & HAS_DD_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 2 - Investigation
            investigation_prf_agent_obj_1 = world.get_location("dD Investigation - Perfect Agent Objective 1")
            world.set_rule(investigation_prf_agent_obj_1, HasAll("dD Investigation - Perfect Agent", "CamSpy")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_prf_agent_obj_2 = world.get_location("dD Investigation - Perfect Agent Objective 2")
            world.set_rule(investigation_prf_agent_obj_2, Has("dD Investigation - Perfect Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_prf_agent_obj_3 = world.get_location("dD Investigation - Perfect Agent Objective 3")
            world.set_rule(investigation_prf_agent_obj_3, Has("dD Investigation - Perfect Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_prf_agent_obj_4 = world.get_location("dD Investigation - Perfect Agent Objective 4")
            world.set_rule(investigation_prf_agent_obj_4, (HasAll("dD Investigation - Perfect Agent", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | HasAll("dD Investigation - Perfect Agent", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))

            investigation_prf_agent_obj_5 = world.get_location("dD Investigation - Perfect Agent Objective 5")
            world.set_rule(investigation_prf_agent_obj_5, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))

            investigation_prf_agent_complete = world.get_location("Complete: dD Investigation - Perfect Agent")
            world.set_rule(investigation_prf_agent_complete, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                             | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))
            

            # Stage 3 - Extraction
            extraction_prf_agent_obj_1 = world.get_location("dD Extraction - Perfect Agent Objective 1")
            world.set_rule(extraction_prf_agent_obj_1, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_2 = world.get_location("dD Extraction - Perfect Agent Objective 2")
            world.set_rule(extraction_prf_agent_obj_2, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_3 = world.get_location("dD Extraction - Perfect Agent Objective 3")
            world.set_rule(extraction_prf_agent_obj_3, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
            
            extraction_prf_agent_obj_4 = world.get_location("dD Extraction - Perfect Agent Objective 4")
            world.set_rule(extraction_prf_agent_obj_4, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_5 = world.get_location("dD Extraction - Perfect Agent Objective 5")
            world.set_rule(extraction_prf_agent_obj_5, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_complete = world.get_location("Complete: dD Extraction - Perfect Agent")
            world.set_rule(extraction_prf_agent_complete, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))


            # Stage 4 - Villa
            villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
            world.set_rule(villa_prf_agent_obj_1, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
            
            villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
            world.set_rule(villa_prf_agent_obj_2, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
            world.set_rule(villa_prf_agent_obj_3, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
            world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

            villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
            world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
            world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            if world.options.mission_logic.value == MissionLogic.option_normal:
                chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
                world.set_rule(chicago_prf_agent_obj_1, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
                world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

                chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
                world.set_rule(chicago_prf_agent_obj_3, (HasAll("Chicago - Perfect Agent", "Remote Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (Has("Chicago - Perfect Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
                world.set_rule(chicago_prf_agent_obj_4, HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

                chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
                world.set_rule(chicago_prf_agent_obj_5, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
                
                chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
                world.set_rule(chicago_prf_agent_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                           | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
                world.set_rule(chicago_prf_agent_obj_1, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
                world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

                chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
                world.set_rule(chicago_prf_agent_obj_3, (HasAll("Chicago - Perfect Agent", "Remote Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (Has("Chicago - Perfect Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

                chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
                world.set_rule(chicago_prf_agent_obj_4, (HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (HasAll("Chicago - Perfect Agent", "CamSpy")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

                chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
                world.set_rule(chicago_prf_agent_obj_5, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                        | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
                
                chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
                world.set_rule(chicago_prf_agent_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                           | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
            world.set_rule(g5_prf_agent_obj_1, Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
            world.set_rule(g5_prf_agent_obj_2, Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
            world.set_rule(g5_prf_agent_obj_3, HasAll("G5 Building - Perfect Agent", "CamSpy") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
            world.set_rule(g5_prf_agent_obj_4, HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
            world.set_rule(g5_prf_agent_obj_5, (HasAll("G5 Building - Perfect Agent", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                               | (Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
            world.set_rule(g5_prf_agent_complete, (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            

            # Stage 7 - Infiltration
            infiltration_prf_agent_obj_1 = world.get_location("A51 Infiltration - Perfect Agent Objective 1")
            world.set_rule(infiltration_prf_agent_obj_1, HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_2 = world.get_location("A51 Infiltration - Perfect Agent Objective 2")
            world.set_rule(infiltration_prf_agent_obj_2, HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_3 = world.get_location("A51 Infiltration - Perfect Agent Objective 3")
            world.set_rule(infiltration_prf_agent_obj_3, Has("A51 Infiltration - Perfect Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_4 = world.get_location("A51 Infiltration - Perfect Agent Objective 4")
            world.set_rule(infiltration_prf_agent_obj_4, HasAll("A51 Infiltration - Perfect Agent") & HAS_A51_INFIL_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_5 = world.get_location("A51 Infiltration - Perfect Agent Objective 5")
            world.set_rule(infiltration_prf_agent_obj_5, HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_complete = world.get_location("Complete: A51 Infiltration - Perfect Agent")
            world.set_rule(infiltration_prf_agent_complete, HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_prf_agent_obj_1 = world.get_location("A51 Rescue - Perfect Agent Objective 1")
            world.set_rule(rescue_prf_agent_obj_1, HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_2 = world.get_location("A51 Rescue - Perfect Agent Objective 2")
            world.set_rule(rescue_prf_agent_obj_2, HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_3 = world.get_location("A51 Rescue - Perfect Agent Objective 3")
            world.set_rule(rescue_prf_agent_obj_3, HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_4 = world.get_location("A51 Rescue - Perfect Agent Objective 4")
            world.set_rule(rescue_prf_agent_obj_4, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_5 = world.get_location("A51 Rescue - Perfect Agent Objective 5")
            world.set_rule(rescue_prf_agent_obj_5, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_prf_agent_complete = world.get_location("Complete: A51 Rescue - Perfect Agent")
            world.set_rule(rescue_prf_agent_complete, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_prf_agent_obj_1 = world.get_location("A51 Escape - Perfect Agent Objective 1")
            world.set_rule(escape_prf_agent_obj_1, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_2 = world.get_location("A51 Escape - Perfect Agent Objective 2")
            world.set_rule(escape_prf_agent_obj_2, Has("A51 Escape - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_3 = world.get_location("A51 Escape - Perfect Agent Objective 3")
            world.set_rule(escape_prf_agent_obj_3, Has("A51 Escape - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_4 = world.get_location("A51 Escape - Perfect Agent Objective 4")
            world.set_rule(escape_prf_agent_obj_4, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_5 = world.get_location("A51 Escape - Perfect Agent Objective 5")
            world.set_rule(escape_prf_agent_obj_5, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_prf_agent_complete = world.get_location("Complete: A51 Escape - Perfect Agent")
            world.set_rule(escape_prf_agent_complete, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            

            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, (HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                         | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise")))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, (HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                         | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase")))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, (HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                         | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise")))

                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
            
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))
                
                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


            # Stage 11 - Air Force One
            air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
            world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
            world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
            world.set_rule(air_force_one_prf_agent_obj_3, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
            world.set_rule(air_force_one_prf_agent_obj_4, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
            world.set_rule(air_force_one_prf_agent_obj_5, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
            world.set_rule(air_force_one_prf_agent_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
            world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
            world.set_rule(crash_site_prf_agent_obj_2, Has("Crash Site - Perfect Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
            world.set_rule(crash_site_prf_agent_obj_3, Has("Crash Site - Perfect Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
            world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
            world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
            world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
            world.set_rule(pelagic_prf_agent_obj_1, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
            world.set_rule(pelagic_prf_agent_obj_2, HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
            world.set_rule(pelagic_prf_agent_obj_3, Has("Pelagic II - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
            world.set_rule(pelagic_prf_agent_obj_4, Has("Pelagic II - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
            world.set_rule(pelagic_prf_agent_obj_5, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
            world.set_rule(pelagic_prf_agent_complete, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
            world.set_rule(deep_sea_prf_agent_obj_1, HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
            world.set_rule(deep_sea_prf_agent_obj_2, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
            world.set_rule(deep_sea_prf_agent_obj_3, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
            world.set_rule(deep_sea_prf_agent_obj_4, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
            world.set_rule(deep_sea_prf_agent_obj_5, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))
            
            deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
            world.set_rule(deep_sea_prf_agent_complete, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                        | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))
            

            # Stage 15 - Carrington Institute Defense
            if world.options.mission_logic.value == MissionLogic.option_normal:
                institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
                world.set_rule(institute_defense_prf_agent_obj_1, Has("CI Defense - Perfect Agent")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

                institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
                world.set_rule(institute_defense_prf_agent_obj_2, Has("CI Defense - Perfect Agent")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

                institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
                world.set_rule(institute_defense_prf_agent_obj_3, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                  | (Has("CI Defense - Perfect Agent")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

                institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
                world.set_rule(institute_defense_prf_agent_obj_4, HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

                institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
                world.set_rule(institute_defense_prf_agent_obj_5, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                  | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

                institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
                world.set_rule(institute_defense_prf_agent_complete, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                     | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            elif world.options.mission_logic.value == MissionLogic.option_veteran:
                institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
                world.set_rule(institute_defense_prf_agent_obj_1, Has("CI Defense - Perfect Agent")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

                institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
                world.set_rule(institute_defense_prf_agent_obj_2, Has("CI Defense - Perfect Agent")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

                institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
                world.set_rule(institute_defense_prf_agent_obj_3, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                  | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

                institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
                world.set_rule(institute_defense_prf_agent_obj_4, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                  | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))

                institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
                world.set_rule(institute_defense_prf_agent_obj_5, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                  | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

                institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
                world.set_rule(institute_defense_prf_agent_complete, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                     | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
            world.set_rule(attack_ship_prf_agent_obj_1, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
            world.set_rule(attack_ship_prf_agent_obj_2, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
            world.set_rule(attack_ship_prf_agent_obj_3, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
            world.set_rule(attack_ship_prf_agent_obj_4, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
            world.set_rule(attack_ship_prf_agent_obj_5, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
            world.set_rule(attack_ship_prf_agent_complete, Has("Attack Ship - Perfect Agent")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            

            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
                world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
                world.set_rule(skedar_ruins_prf_agent_obj_2, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
                world.set_rule(skedar_ruins_prf_agent_obj_3, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
                world.set_rule(skedar_ruins_prf_agent_obj_4, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
                world.set_rule(skedar_ruins_prf_agent_obj_5, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
                world.set_rule(skedar_ruins_prf_agent_complete, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                                | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
                world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
                world.set_rule(skedar_ruins_prf_agent_obj_2, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
                world.set_rule(skedar_ruins_prf_agent_obj_3, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
                world.set_rule(skedar_ruins_prf_agent_obj_4, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
                world.set_rule(skedar_ruins_prf_agent_obj_5, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
                world.set_rule(skedar_ruins_prf_agent_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            world.set_rule(mbr_prf_agent_obj_1, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            world.set_rule(mbr_prf_agent_obj_2, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            world.set_rule(mbr_prf_agent_obj_3, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
            world.set_rule(mbr_prf_agent_complete, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
            world.set_rule(maian_sos_prf_agent_obj_1, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
            world.set_rule(maian_sos_prf_agent_obj_2, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
            world.set_rule(maian_sos_prf_agent_obj_3, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
            world.set_rule(maian_sos_prf_agent_complete, Has("Maian SOS - Perfect Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
   

            # Stage 20 - WAR!
            war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
            world.set_rule(war_prf_agent_obj_1, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
            world.set_rule(war_prf_agent_obj_2, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
            world.set_rule(war_prf_agent_obj_3, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
            world.set_rule(war_prf_agent_complete, Has("WAR! - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
            world.set_rule(duel_prf_agent_obj_1, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
            world.set_rule(duel_prf_agent_obj_2, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
            world.set_rule(duel_prf_agent_obj_3, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
            
            duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
            world.set_rule(duel_prf_agent_complete, Has("The Duel - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
        

        if world.options.unlock_cheats:
            # Defection
            cheat_defection_complete = world.get_location("Cheat Unlock: Complete dD Defection")
            world.set_rule(cheat_defection_complete, (Has("dD Defection - Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))


            # Investigation
            cheat_investigation_complete = world.get_location("Cheat Unlock: Complete dD Investigation")
            world.set_rule(cheat_investigation_complete, (HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | ((HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))))


            # Extraction
            cheat_extraction_complete = world.get_location("Cheat Unlock: Complete dD Extraction")
            world.set_rule(cheat_extraction_complete, (HasAll("dD Extraction - Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                      | (HasAll("dD Extraction - Special Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
                                                      | (HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])))


            # Villa
            cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
            world.set_rule(cheat_villa_complete, (HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
                                                 | (HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
                                                 | (HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])))


            # Chicago
            cheat_chicago_complete = world.get_location("Cheat Unlock: Complete Chicago")
            world.set_rule(cheat_chicago_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                   | (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                   | (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # G5 Building
            cheat_g5_complete = world.get_location("Cheat Unlock: Complete G5 Building")
            world.set_rule(cheat_g5_complete, (HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                              | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                              | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Infiltration
            cheat_infiltration_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration")
            world.set_rule(cheat_infiltration_complete, (HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Rescue
            cheat_rescue_complete = world.get_location("Cheat Unlock: Complete A51 Rescue")
            world.set_rule(cheat_rescue_complete, (HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Escape
            cheat_escape_complete = world.get_location("Cheat Unlock: Complete A51 Escape")
            world.set_rule(cheat_escape_complete, (HasAll("A51 Escape - Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
                world.set_rule(cheat_air_base_complete, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                                                        | (HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))
    
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
                world.set_rule(cheat_air_base_complete, (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                                                        | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))


            # Air Force One
            cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
            world.set_rule(cheat_air_force_one_complete, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Agent", "Suitcase")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Crash Site
            cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
            world.set_rule(cheat_crash_site_complete, (HasAll("Crash Site - Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Crash Site - Special Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Pelagic II
            cheat_pelagic_complete = world.get_location("Cheat Unlock: Complete Pelagic II")
            world.set_rule(cheat_pelagic_complete, (HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                   | (HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                   | (HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Deep Sea
            cheat_deep_sea_complete = world.get_location("Cheat Unlock: Complete Deep Sea")
            world.set_rule(cheat_deep_sea_complete, (HasAll("Deep Sea - Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))


            # CI Defense
            cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
            world.set_rule(cheat_institute_defense_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                             | (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                             | (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Attack Ship
            cheat_attack_ship_complete = world.get_location("Cheat Unlock: Complete Attack Ship")
            world.set_rule(cheat_attack_ship_complete, (Has("Attack Ship - Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                       | (Has("Attack Ship - Special Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                       | (Has("Attack Ship - Perfect Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])))


            # Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
                world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
                world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])))


            if world.options.agent:
                # Extraction
                cheat_extraction_timed_complete = world.get_location("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
                world.set_rule(cheat_extraction_timed_complete, HasAll("dD Extraction - Agent", "Night Vision")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # G5 Building
                cheat_g5_timed_complete = world.get_location("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
                world.set_rule(cheat_g5_timed_complete, HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # Escape
                cheat_escape_timed_complete = world.get_location("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
                world.set_rule(cheat_escape_timed_complete, HasAll("A51 Escape - Agent", "Alien Medpack")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Crash Site
                cheat_crash_site_timed_complete = world.get_location("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
                world.set_rule(cheat_crash_site_timed_complete, HasAll("Crash Site - Agent", "President Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # CI Defense
                cheat_institute_defense_timed_complete = world.get_location("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")
                world.set_rule(cheat_institute_defense_timed_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                       | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            if world.options.special_agent:
                # Defection
                cheat_defection_timed_complete = world.get_location("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
                world.set_rule(cheat_defection_timed_complete, HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # Villa
                cheat_villa_timed_complete = world.get_location("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
                world.set_rule(cheat_villa_timed_complete, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


                # Infiltration
                cheat_infiltration_timed_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
                world.set_rule(cheat_infiltration_timed_complete, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Air Base
                if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                    cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                    world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                    cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                    world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


                # Pelagic II
                cheat_pelagic_timed_complete = world.get_location("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
                world.set_rule(cheat_pelagic_timed_complete, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Attack Ship
                cheat_attack_ship_timed_complete = world.get_location("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")
                world.set_rule(cheat_attack_ship_timed_complete, Has("Attack Ship - Special Agent")
                                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            if world.options.perfect_agent:
                # Investigation
                cheat_investigation_timed_complete = world.get_location("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
                world.set_rule(cheat_investigation_timed_complete, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                                   | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))


                # Chicago
                cheat_chicago_timed_complete = world.get_location("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
                world.set_rule(cheat_chicago_timed_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                             | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


                # Rescue
                cheat_rescue_timed_complete = world.get_location("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
                world.set_rule(cheat_rescue_timed_complete, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Air Force One
                cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                world.set_rule(cheat_air_force_one_timed_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                                   | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


                # Deep Sea
                cheat_deep_sea_timed_complete = world.get_location("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
                world.set_rule(cheat_deep_sea_timed_complete, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                              | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))


                # Skedar Ruins
                if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                    cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                    world.set_rule(cheat_skedar_ruins_timed_complete, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                                      | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                    cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                    world.set_rule(cheat_skedar_ruins_timed_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


def set_all_hard_location_rules(world: PerfectDarkWorld) -> None:
    if world.options.weapon_progression.value == WeaponProgression.option_vanilla:
        if world.options.agent:
            # Stage 1 - Defection
            defection_agent_obj_1 = world.get_location("dD Defection - Agent Objective 1")
            world.set_rule(defection_agent_obj_1, HasAll("dD Defection - Agent", "Falcon 2 (Silencer)")
                                                  | HasAll("dD Defection - Agent", "CMP150"))

            defection_agent_complete = world.get_location("Complete: dD Defection - Agent")
            world.set_rule(defection_agent_complete, HasAll("dD Defection - Agent", "Falcon 2 (Silencer)")
                                                     | HasAll("dD Defection - Agent", "CMP150"))


            # Stage 2 - Investigation
            investigation_agent_obj_1 = world.get_location("dD Investigation - Agent Objective 1")
            world.set_rule(investigation_agent_obj_1, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2")
                                                      | HasAll("dD Investigation - Agent", "CamSpy", "CMP150"))

            investigation_agent_obj_2 = world.get_location("dD Investigation - Agent Objective 2")
            world.set_rule(investigation_agent_obj_2, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))

            investigation_agent_complete = world.get_location("Complete: dD Investigation - Agent")
            world.set_rule(investigation_agent_complete, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))


            # Stage 3 - Extraction
            extraction_agent_obj_1 = world.get_location("dD Extraction - Agent Objective 1")
            world.set_rule(extraction_agent_obj_1, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)")
                                                           | HasAll("dD Extraction - Agent", "Night Vision", "CMP150"))

            extraction_agent_obj_2 = world.get_location("dD Extraction - Agent Objective 2")
            world.set_rule(extraction_agent_obj_2, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_agent_obj_3 = world.get_location("dD Extraction - Agent Objective 3")
            world.set_rule(extraction_agent_obj_3, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_agent_complete = world.get_location("Complete: dD Extraction - Agent")
            world.set_rule(extraction_agent_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))


            # Stage 4 - Villa
            villa_agent_obj_1 = world.get_location("Carrington Villa - Agent Objective 1")
            world.set_rule(villa_agent_obj_1, HasAll("Carrington Villa - Agent", "Sniper Rifle"))

            villa_agent_obj_2 = world.get_location("Carrington Villa - Agent Objective 2")
            world.set_rule(villa_agent_obj_2, HasAll("Carrington Villa - Agent", "CMP150"))

            villa_agent_obj_3 = world.get_location("Carrington Villa - Agent Objective 3")
            world.set_rule(villa_agent_obj_3, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))

            villa_agent_complete = world.get_location("Complete: Carrington Villa - Agent")
            world.set_rule(villa_agent_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
            world.set_rule(chicago_agent_obj_1, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "CMP150"))

            chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
            world.set_rule(chicago_agent_obj_2, HasAll("Chicago - Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                | HasAll("Chicago - Agent", "Data Uplink", "CMP150") 
                                                | HasAll("Chicago - Agent", "CamSpy", "Falcon 2 (Scope)")
                                                | HasAll("Chicago - Agent", "CamSpy", "CMP150"))

            chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
            world.set_rule(chicago_agent_obj_3, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))
            
            chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
            world.set_rule(chicago_agent_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))


            # Stage 6 - G5 Building
            g5_agent_obj_1 = world.get_location("G5 Building - Agent Objective 1")
            world.set_rule(g5_agent_obj_1, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)
                                           | (HasAll("G5 Building - Agent", "CMP150", "CamSpy") & HAS_G5_KEYS))

            g5_agent_obj_2 = world.get_location("G5 Building - Agent Objective 2")
            world.set_rule(g5_agent_obj_2, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_agent_obj_3 = world.get_location("G5 Building - Agent Objective 3")
            world.set_rule(g5_agent_obj_3, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_agent_complete = world.get_location("Complete: G5 Building - Agent")
            world.set_rule(g5_agent_complete, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
            

            # Stage 7 - Infiltration
            infiltration_agent_obj_1 = world.get_location("A51 Infiltration - Agent Objective 1")
            world.set_rule(infiltration_agent_obj_1, HasAll("A51 Infiltration - Agent", "Falcon 2", "Explosives")
                                                     | HasAll("A51 Infiltration - Agent", "MagSec 4", "Explosives"))

            infiltration_agent_obj_2 = world.get_location("A51 Infiltration - Agent Objective 2")
            world.set_rule(infiltration_agent_obj_2, (HasAll("A51 Infiltration - Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)
                                                     | (HasAll("A51 Infiltration - Agent", "MagSec 4") & HAS_A51_INFIL_KEYS))

            infiltration_agent_obj_3 = world.get_location("A51 Infiltration - Agent Objective 3")
            world.set_rule(infiltration_agent_obj_3, HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)

            infiltration_agent_complete = world.get_location("Complete: A51 Infiltration - Agent")
            world.set_rule(infiltration_agent_complete, HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)


            # Stage 8 - Rescue
            rescue_agent_obj_1 = world.get_location("A51 Rescue - Agent Objective 1")
            world.set_rule(rescue_agent_obj_1, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Lab Clothes")
                                               | HasAll("A51 Rescue - Agent", "Dragon", "Lab Clothes"))

            rescue_agent_obj_2 = world.get_location("A51 Rescue - Agent Objective 2")
            world.set_rule(rescue_agent_obj_2, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                               | (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                               | (HasAll("A51 Rescue - Agent", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY))

            rescue_agent_obj_3 = world.get_location("A51 Rescue - Agent Objective 3")
            world.set_rule(rescue_agent_obj_3, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
            
            rescue_agent_complete = world.get_location("Complete: A51 Rescue - Agent")
            world.set_rule(rescue_agent_complete, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


            # Stage 9 - Escape
            escape_agent_obj_1 = world.get_location("A51 Escape - Agent Objective 1")
            world.set_rule(escape_agent_obj_1, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)")
                                               | HasAll("A51 Escape - Agent", "SuperDragon"))

            escape_agent_obj_2 = world.get_location("A51 Escape - Agent Objective 2")
            world.set_rule(escape_agent_obj_2, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)")
                                               | HasAll("A51 Escape - Agent", "SuperDragon"))

            escape_agent_obj_3 = world.get_location("A51 Escape - Agent Objective 3")
            world.set_rule(escape_agent_obj_3, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))
            
            escape_agent_complete = world.get_location("Complete: A51 Escape - Agent")
            world.set_rule(escape_agent_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
            world.set_rule(air_base_agent_obj_1, HasAll("Air Base - Agent", "Crossbow", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

            air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
            world.set_rule(air_base_agent_obj_2, HasAll("Air Base - Agent", "Crossbow", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

            air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
            world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise"))
            
            air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
            world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise"))


            # Stage 11 - Air Force One
            air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
            world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

            air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
            world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger")
                                                      | (HasAll("Air Force One - Agent", "Suitcase", "Cyclone", "K7 Avenger") & HAS_AFO_EXTRA_KEYS))

            air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
            world.set_rule(air_force_one_agent_obj_3, HasAll("Air Force One - Agent", "Laptop Gun", "Timed Mine")
                                                      | (HasAll("Air Force One - Agent", "Cyclone", "Timed Mine") & HAS_AFO_EXTRA_KEYS))

            air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
            world.set_rule(air_force_one_agent_complete, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine")
                                                         | HasAll("Air Force One - Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_EXTRA_KEYS)


            # Stage 12 - Crash Site
            crash_site_agent_obj_1 = world.get_location("Crash Site - Agent Objective 1")
            world.set_rule(crash_site_agent_obj_1, HasAll("Crash Site - Agent", "Falcon 2 (Scope)")
                                                   | HasAll("Crash Site - Agent", "K7 Avenger")
                                                   | HasAll("Crash Site - Agent", "Sniper Rifle"))

            crash_site_agent_obj_2 = world.get_location("Crash Site - Agent Objective 2")
            world.set_rule(crash_site_agent_obj_2, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                   | HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                   | HasAll("Crash Site - Agent", "K7 Avenger", "Sniper Rifle", "President Scanner"))

            crash_site_agent_obj_3 = world.get_location("Crash Site - Agent Objective 3")
            world.set_rule(crash_site_agent_obj_3, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_agent_complete = world.get_location("Complete: Crash Site - Agent")
            world.set_rule(crash_site_agent_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))


            # Stage 13 - Pelagic II
            pelagic_agent_obj_1 = world.get_location("Pelagic II - Agent Objective 1")
            world.set_rule(pelagic_agent_obj_1, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "CMP150", "X-Ray Scanner"))

            pelagic_agent_obj_2 = world.get_location("Pelagic II - Agent Objective 2")
            world.set_rule(pelagic_agent_obj_2, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun")
                                                | HasAll("Pelagic II - Agent", "CMP150"))

            pelagic_agent_obj_3 = world.get_location("Pelagic II - Agent Objective 3")
            world.set_rule(pelagic_agent_obj_3, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))
            
            pelagic_agent_complete = world.get_location("Complete: Pelagic II - Agent")
            world.set_rule(pelagic_agent_complete, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))


            # Stage 14 - Deep Sea
            deep_sea_agent_obj_1 = world.get_location("Deep Sea - Agent Objective 1")
            world.set_rule(deep_sea_agent_obj_1, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "IR Scanner"))

            deep_sea_agent_obj_2 = world.get_location("Deep Sea - Agent Objective 2")
            world.set_rule(deep_sea_agent_obj_2, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_agent_obj_3 = world.get_location("Deep Sea - Agent Objective 3")
            world.set_rule(deep_sea_agent_obj_3, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_agent_complete = world.get_location("Complete: Deep Sea - Agent")
            world.set_rule(deep_sea_agent_complete, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_agent_obj_1 = world.get_location("CI Defense - Agent Objective 1")
            world.set_rule(institute_defense_agent_obj_1, HasAll("CI Defense - Agent", "AR34"))

            institute_defense_agent_obj_2 = world.get_location("CI Defense - Agent Objective 2")
            world.set_rule(institute_defense_agent_obj_2, HasAll("CI Defense - Agent", "AR34", "RC-P120"))

            institute_defense_agent_obj_3 = world.get_location("CI Defense - Agent Objective 3")
            world.set_rule(institute_defense_agent_obj_3, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))

            institute_defense_agent_complete = world.get_location("Complete: CI Defense - Agent")
            world.set_rule(institute_defense_agent_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_agent_obj_1 = world.get_location("Attack Ship - Agent Objective 1")
            world.set_rule(attack_ship_agent_obj_1, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler"))

            attack_ship_agent_obj_2 = world.get_location("Attack Ship - Agent Objective 2")
            world.set_rule(attack_ship_agent_obj_2, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_agent_obj_3 = world.get_location("Attack Ship - Agent Objective 3")
            world.set_rule(attack_ship_agent_obj_3, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_agent_complete = world.get_location("Complete: Attack Ship - Agent")
            world.set_rule(attack_ship_agent_complete, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
            world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
            world.set_rule(skedar_ruins_agent_obj_2, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
            world.set_rule(skedar_ruins_agent_obj_3, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
            world.set_rule(skedar_ruins_agent_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Agent Objective 1")
            world.set_rule(mbr_agent_obj_1, HasAll("Mr. Blonde's Revenge - Agent", "Mauler", "Cloaking Device"))

            mbr_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Agent")
            world.set_rule(mbr_agent_complete, HasAll("Mr. Blonde's Revenge - Agent", "Mauler", "Cloaking Device"))


            # Stage 19 - Maian SOS
            maian_sos_agent_obj_1 = world.get_location("Maian SOS - Agent Objective 1")
            world.set_rule(maian_sos_agent_obj_1, HasAll("Maian SOS - Agent", "Falcon 2", "Dragon"))

            maian_sos_agent_complete = world.get_location("Complete: Maian SOS - Agent")
            world.set_rule(maian_sos_agent_complete, HasAll("Maian SOS - Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_agent_obj_1 = world.get_location("WAR! - Agent Objective 1")
            world.set_rule(war_agent_obj_1, HasAll("WAR! - Agent", "Phoenix"))

            war_agent_complete = world.get_location("Complete: WAR! - Agent")
            world.set_rule(war_agent_complete, HasAll("WAR! - Agent", "Phoenix"))


            # Stage 21 - The Duel
            duel_agent_obj_1 = world.get_location("The Duel - Agent Objective 1")
            world.set_rule(duel_agent_obj_1, HasAll("The Duel - Agent", "Falcon 2 (Scope)"))

            duel_agent_complete = world.get_location("Complete: The Duel - Agent")
            world.set_rule(duel_agent_complete, HasAll("The Duel - Agent", "Falcon 2 (Scope)"))


        if world.options.special_agent:
            # Stage 1 - Defection
            defection_sp_agent_obj_1 = world.get_location("dD Defection - Special Agent Objective 1")
            world.set_rule(defection_sp_agent_obj_1, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)")
                                                     | HasAll("dD Defection - Special Agent", "ECM Mine", "CMP150"))

            defection_sp_agent_obj_2 = world.get_location("dD Defection - Special Agent Objective 2")
            world.set_rule(defection_sp_agent_obj_2, (HasAll("dD Defection - Special Agent", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Special Agent", "CMP150") & HAS_DD_KEYS))

            defection_sp_agent_obj_3 = world.get_location("dD Defection - Special Agent Objective 3")
            world.set_rule(defection_sp_agent_obj_3, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150"))

            defection_sp_agent_obj_4 = world.get_location("dD Defection - Special Agent Objective 4")
            world.set_rule(defection_sp_agent_obj_4, HasAll("dD Defection - Special Agent", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)

            defection_sp_agent_complete = world.get_location("Complete: dD Defection - Special Agent")
            world.set_rule(defection_sp_agent_complete, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)


            # Stage 2 - Investigation
            investigation_sp_agent_obj_1 = world.get_location("dD Investigation - Special Agent Objective 1")
            world.set_rule(investigation_sp_agent_obj_1, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2")
                                                         | HasAll("dD Investigation - Special Agent", "CamSpy", "CMP150"))

            investigation_sp_agent_obj_2 = world.get_location("dD Investigation - Special Agent Objective 2")
            world.set_rule(investigation_sp_agent_obj_2, HasAll("dD Investigation - Special Agent", "Falcon 2")
                                                         | HasAll("dD Investigation - Special Agent", "CMP150"))

            investigation_sp_agent_obj_3 = world.get_location("dD Investigation - Special Agent Objective 3")
            world.set_rule(investigation_sp_agent_obj_3, HasAll("dD Investigation - Special Agent", "Falcon 2", "CMP150"))

            investigation_sp_agent_obj_4 = world.get_location("dD Investigation - Special Agent Objective 4")
            world.set_rule(investigation_sp_agent_obj_4, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))

            investigation_sp_agent_complete = world.get_location("Complete: dD Investigation - Special Agent")
            world.set_rule(investigation_sp_agent_complete, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink"))


            # Stage 3 - Extraction
            extraction_sp_agent_obj_1 = world.get_location("dD Extraction - Special Agent Objective 1")
            world.set_rule(extraction_sp_agent_obj_1, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150"))

            extraction_sp_agent_obj_2 = world.get_location("dD Extraction - Special Agent Objective 2")
            world.set_rule(extraction_sp_agent_obj_2, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun", "Rocket Launcher"))

            extraction_sp_agent_obj_3 = world.get_location("dD Extraction - Special Agent Objective 3")
            world.set_rule(extraction_sp_agent_obj_3, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_sp_agent_obj_4 = world.get_location("dD Extraction - Special Agent Objective 4")
            world.set_rule(extraction_sp_agent_obj_4, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_sp_agent_complete = world.get_location("Complete: dD Extraction - Special Agent")
            world.set_rule(extraction_sp_agent_complete, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher")
                                                         | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun", "Rocket Launcher"))


            # Stage 4 - Villa
            villa_sp_agent_obj_1 = world.get_location("Carrington Villa - Special Agent Objective 1")
            world.set_rule(villa_sp_agent_obj_1, HasAll("Carrington Villa - Special Agent", "Sniper Rifle"))

            villa_sp_agent_obj_2 = world.get_location("Carrington Villa - Special Agent Objective 2")
            world.set_rule(villa_sp_agent_obj_2, HasAll("Carrington Villa - Special Agent", "Sniper Rifle")
                                                 | HasAll("Carrington Villa - Special Agent", "CMP150"))

            villa_sp_agent_obj_3 = world.get_location("Carrington Villa - Special Agent Objective 3")
            world.set_rule(villa_sp_agent_obj_3, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150"))

            villa_sp_agent_obj_4 = world.get_location("Carrington Villa - Special Agent Objective 4")
            world.set_rule(villa_sp_agent_obj_4, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))

            villa_sp_agent_complete = world.get_location("Complete: Carrington Villa - Special Agent")
            world.set_rule(villa_sp_agent_complete, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
            world.set_rule(chicago_sp_agent_obj_1, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "CMP150"))

            chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
            world.set_rule(chicago_sp_agent_obj_2, HasAll("Chicago - Special Agent", "Remote Mine", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "CMP150"))

            chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
            world.set_rule(chicago_sp_agent_obj_3, HasAll("Chicago - Special Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "Data Uplink", "CMP150") 
                                                   | HasAll("Chicago - Special Agent", "CamSpy", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "CamSpy", "CMP150"))

            chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
            world.set_rule(chicago_sp_agent_obj_4, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))
            
            chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
            world.set_rule(chicago_sp_agent_complete, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150"))


            # Stage 6 - G5 Building
            g5_sp_agent_obj_1 = world.get_location("G5 Building - Special Agent Objective 1")
            world.set_rule(g5_sp_agent_obj_1, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150") & HAS_G5_KEYS))

            g5_sp_agent_obj_2 = world.get_location("G5 Building - Special Agent Objective 2")
            world.set_rule(g5_sp_agent_obj_2, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150", "CamSpy") & HAS_G5_KEYS))

            g5_sp_agent_obj_3 = world.get_location("G5 Building - Special Agent Objective 3")
            world.set_rule(g5_sp_agent_obj_3, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_sp_agent_obj_4 = world.get_location("G5 Building - Special Agent Objective 4")
            world.set_rule(g5_sp_agent_obj_4, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "Remote Mine") & HAS_G5_KEYS)

            g5_sp_agent_complete = world.get_location("Complete: G5 Building - Special Agent")
            world.set_rule(g5_sp_agent_complete, HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
            

            # Stage 7 - Infiltration
            infiltration_sp_agent_obj_1 = world.get_location("A51 Infiltration - Special Agent Objective 1")
            world.set_rule(infiltration_sp_agent_obj_1, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Explosives")
                                                        | HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Explosives"))

            infiltration_sp_agent_obj_2 = world.get_location("A51 Infiltration - Special Agent Objective 2")
            world.set_rule(infiltration_sp_agent_obj_2, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Comms Rider")
                                                        | HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Comms Rider"))

            infiltration_sp_agent_obj_3 = world.get_location("A51 Infiltration - Special Agent Objective 3")
            world.set_rule(infiltration_sp_agent_obj_3, (HasAll("A51 Infiltration - Special Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "MagSec 4") & HAS_A51_INFIL_KEYS))

            infiltration_sp_agent_obj_4 = world.get_location("A51 Infiltration - Special Agent Objective 4")
            world.set_rule(infiltration_sp_agent_obj_4, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)

            infiltration_sp_agent_complete = world.get_location("Complete: A51 Infiltration - Special Agent")
            world.set_rule(infiltration_sp_agent_complete, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)


            # Stage 8 - Rescue
            rescue_sp_agent_obj_1 = world.get_location("A51 Rescue - Special Agent Objective 1")
            world.set_rule(rescue_sp_agent_obj_1, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                  | HasAll("A51 Rescue - Special Agent", "Dragon", "X-Ray Scanner"))

            rescue_sp_agent_obj_2 = world.get_location("A51 Rescue - Special Agent Objective 2")
            world.set_rule(rescue_sp_agent_obj_2, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes")
                                                  | HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes")
                                                  | HasAll("A51 Rescue - Special Agent", "Dragon", "SuperDragon", "Lab Clothes"))

            rescue_sp_agent_obj_3 = world.get_location("A51 Rescue - Special Agent Objective 3")
            world.set_rule(rescue_sp_agent_obj_3, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)

            rescue_sp_agent_obj_4 = world.get_location("A51 Rescue - Special Agent Objective 4")
            world.set_rule(rescue_sp_agent_obj_4, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
            
            rescue_sp_agent_complete = world.get_location("Complete: A51 Rescue - Special Agent")
            world.set_rule(rescue_sp_agent_complete, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


            # Stage 9 - Escape
            escape_sp_agent_obj_1 = world.get_location("A51 Escape - Special Agent Objective 1")
            world.set_rule(escape_sp_agent_obj_1, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)")
                                                  | HasAll("A51 Escape - Special Agent", "SuperDragon"))

            escape_sp_agent_obj_2 = world.get_location("A51 Escape - Special Agent Objective 2")
            world.set_rule(escape_sp_agent_obj_2, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_sp_agent_obj_3 = world.get_location("A51 Escape - Special Agent Objective 3")
            world.set_rule(escape_sp_agent_obj_3, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))

            escape_sp_agent_obj_4 = world.get_location("A51 Escape - Special Agent Objective 4")
            world.set_rule(escape_sp_agent_obj_4, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))
            
            escape_sp_agent_complete = world.get_location("Complete: A51 Escape - Special Agent")
            world.set_rule(escape_sp_agent_complete, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
            world.set_rule(air_base_sp_agent_obj_1, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

            air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
            world.set_rule(air_base_sp_agent_obj_2, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

            air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
            world.set_rule(air_base_sp_agent_obj_3, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

            air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
            world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase"))
            
            air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
            world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                       | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase"))


            # Stage 11 - Air Force One
            air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
            world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
            world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
            world.set_rule(air_force_one_sp_agent_obj_3, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "K7 Avenger") & HAS_AFO_ALL_KEYS))

            air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
            world.set_rule(air_force_one_sp_agent_obj_4, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_ALL_KEYS))

            air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
            world.set_rule(air_force_one_sp_agent_complete, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                            | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


            # Stage 12 - Crash Site
            crash_site_sp_agent_obj_1 = world.get_location("Crash Site - Special Agent Objective 1")
            world.set_rule(crash_site_sp_agent_obj_1, HasAll("Crash Site - Special Agent", "President Scanner", "Falcon 2 (Scope)")
                                                      | HasAll("Crash Site - Special Agent", "President Scanner", "K7 Avenger")
                                                      | HasAll("Crash Site - Special Agent", "President Scanner", "Sniper Rifle"))

            crash_site_sp_agent_obj_2 = world.get_location("Crash Site - Special Agent Objective 2")
            world.set_rule(crash_site_sp_agent_obj_2, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)")
                                                      | HasAll("Crash Site - Special Agent", "K7 Avenger")
                                                      | HasAll("Crash Site - Special Agent", "Sniper Rifle"))

            crash_site_sp_agent_obj_3 = world.get_location("Crash Site - Special Agent Objective 3")
            world.set_rule(crash_site_sp_agent_obj_3, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))

            crash_site_sp_agent_obj_4 = world.get_location("Crash Site - Special Agent Objective 4")
            world.set_rule(crash_site_sp_agent_obj_4, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_sp_agent_complete = world.get_location("Complete: Crash Site - Special Agent")
            world.set_rule(crash_site_sp_agent_complete, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))


            # Stage 13 - Pelagic II
            pelagic_sp_agent_obj_1 = world.get_location("Pelagic II - Special Agent Objective 1")
            world.set_rule(pelagic_sp_agent_obj_1, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "CMP150", "X-Ray Scanner"))

            pelagic_sp_agent_obj_2 = world.get_location("Pelagic II - Special Agent Objective 2")
            world.set_rule(pelagic_sp_agent_obj_2, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun")
                                                   | HasAll("Pelagic II - Special Agent", "CMP150"))

            pelagic_sp_agent_obj_3 = world.get_location("Pelagic II - Special Agent Objective 3")
            world.set_rule(pelagic_sp_agent_obj_3, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun")
                                                   | HasAll("Pelagic II - Special Agent", "CMP150"))

            pelagic_sp_agent_obj_4 = world.get_location("Pelagic II - Special Agent Objective 4")
            world.set_rule(pelagic_sp_agent_obj_4, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))
            
            pelagic_sp_agent_complete = world.get_location("Complete: Pelagic II - Special Agent")
            world.set_rule(pelagic_sp_agent_complete, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))


            # Stage 14 - Deep Sea
            deep_sea_sp_agent_obj_1 = world.get_location("Deep Sea - Special Agent Objective 1")
            world.set_rule(deep_sea_sp_agent_obj_1, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "IR Scanner"))

            deep_sea_sp_agent_obj_2 = world.get_location("Deep Sea - Special Agent Objective 2")
            world.set_rule(deep_sea_sp_agent_obj_2, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_sp_agent_obj_3 = world.get_location("Deep Sea - Special Agent Objective 3")
            world.set_rule(deep_sea_sp_agent_obj_3, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_sp_agent_obj_4 = world.get_location("Deep Sea - Special Agent Objective 4")
            world.set_rule(deep_sea_sp_agent_obj_4, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))
            
            deep_sea_sp_agent_complete = world.get_location("Complete: Deep Sea - Special Agent")
            world.set_rule(deep_sea_sp_agent_complete, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                       | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_sp_agent_obj_1 = world.get_location("CI Defense - Special Agent Objective 1")
            world.set_rule(institute_defense_sp_agent_obj_1, HasAll("CI Defense - Special Agent", "AR34"))

            institute_defense_sp_agent_obj_2 = world.get_location("CI Defense - Special Agent Objective 2")
            world.set_rule(institute_defense_sp_agent_obj_2, HasAll("CI Defense - Special Agent", "AR34"))

            institute_defense_sp_agent_obj_3 = world.get_location("CI Defense - Special Agent Objective 3")
            world.set_rule(institute_defense_sp_agent_obj_3, HasAll("CI Defense - Special Agent", "AR34", "RC-P120"))

            institute_defense_sp_agent_obj_4 = world.get_location("CI Defense - Special Agent Objective 4")
            world.set_rule(institute_defense_sp_agent_obj_4, HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink"))

            institute_defense_sp_agent_complete = world.get_location("Complete: CI Defense - Special Agent")
            world.set_rule(institute_defense_sp_agent_complete, HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_sp_agent_obj_1 = world.get_location("Attack Ship - Special Agent Objective 1")
            world.set_rule(attack_ship_sp_agent_obj_1, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler"))

            attack_ship_sp_agent_obj_2 = world.get_location("Attack Ship - Special Agent Objective 2")
            world.set_rule(attack_ship_sp_agent_obj_2, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_sp_agent_obj_3 = world.get_location("Attack Ship - Special Agent Objective 3")
            world.set_rule(attack_ship_sp_agent_obj_3, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_sp_agent_obj_4 = world.get_location("Attack Ship - Special Agent Objective 4")
            world.set_rule(attack_ship_sp_agent_obj_4, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_sp_agent_complete = world.get_location("Complete: Attack Ship - Special Agent")
            world.set_rule(attack_ship_sp_agent_complete, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
            world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
            world.set_rule(skedar_ruins_sp_agent_obj_2, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
            world.set_rule(skedar_ruins_sp_agent_obj_3, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
            world.set_rule(skedar_ruins_sp_agent_obj_4, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
            world.set_rule(skedar_ruins_sp_agent_complete, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_sp_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 1")
            world.set_rule(mbr_sp_agent_obj_1, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb"))

            mbr_sp_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 2")
            world.set_rule(mbr_sp_agent_obj_2, HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler", "Cloaking Device"))

            mbr_sp_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Special Agent")
            world.set_rule(mbr_sp_agent_complete, HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler", "Cloaking Device", "Skedar Bomb"))


            # Stage 19 - Maian SOS
            maian_sos_sp_agent_obj_1 = world.get_location("Maian SOS - Special Agent Objective 1")
            world.set_rule(maian_sos_sp_agent_obj_1, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))

            maian_sos_sp_agent_obj_2 = world.get_location("Maian SOS - Special Agent Objective 2")
            world.set_rule(maian_sos_sp_agent_obj_2, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))

            maian_sos_sp_agent_complete = world.get_location("Complete: Maian SOS - Special Agent")
            world.set_rule(maian_sos_sp_agent_complete, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_sp_agent_obj_1 = world.get_location("WAR! - Special Agent Objective 1")
            world.set_rule(war_sp_agent_obj_1, HasAll("WAR! - Special Agent", "Phoenix"))

            war_sp_agent_obj_2 = world.get_location("WAR! - Special Agent Objective 2")
            world.set_rule(war_sp_agent_obj_2, HasAll("WAR! - Special Agent", "Phoenix"))

            war_sp_agent_complete = world.get_location("Complete: WAR! - Special Agent")
            world.set_rule(war_sp_agent_complete, HasAll("WAR! - Special Agent", "Phoenix"))


            # Stage 21 - The Duel
            duel_sp_agent_obj_1 = world.get_location("The Duel - Special Agent Objective 1")
            world.set_rule(duel_sp_agent_obj_1, HasAll("The Duel - Special Agent", "Falcon 2 (Scope)"))

            duel_sp_agent_obj_2 = world.get_location("The Duel - Special Agent Objective 2")
            world.set_rule(duel_sp_agent_obj_2, HasAll("The Duel - Special Agent", "Falcon 2 (Scope)"))

            duel_sp_agent_complete = world.get_location("Complete: The Duel - Special Agent")
            world.set_rule(duel_sp_agent_complete, HasAll("The Duel - Special Agent", "Falcon 2 (Scope)"))


        if world.options.perfect_agent:
            # Stage 1 - Defection
            defection_prf_agent_obj_1 = world.get_location("dD Defection - Perfect Agent Objective 1")
            world.set_rule(defection_prf_agent_obj_1, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Falcon 2 (Silencer)")
                                                      | HasAll("dD Defection - Perfect Agent", "ECM Mine", "CMP150"))

            defection_prf_agent_obj_2 = world.get_location("dD Defection - Perfect Agent Objective 2")
            world.set_rule(defection_prf_agent_obj_2, (HasAll("dD Defection - Perfect Agent", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                      | (HasAll("dD Defection - Perfect Agent", "CMP150") & HAS_DD_KEYS))

            defection_prf_agent_obj_3 = world.get_location("dD Defection - Perfect Agent Objective 3")
            world.set_rule(defection_prf_agent_obj_3, HasAll("dD Defection - Perfect Agent", "Data Uplink", "Falcon 2 (Silencer)", "CMP150"))

            defection_prf_agent_obj_4 = world.get_location("dD Defection - Perfect Agent Objective 4")
            world.set_rule(defection_prf_agent_obj_4, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150"))

            defection_prf_agent_obj_5 = world.get_location("dD Defection - Perfect Agent Objective 5")
            world.set_rule(defection_prf_agent_obj_5, HasAll("dD Defection - Perfect Agent", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)

            defection_prf_agent_complete = world.get_location("Complete: dD Defection - Perfect Agent")
            world.set_rule(defection_prf_agent_complete, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)


            # Stage 2 - Investigation
            investigation_prf_agent_obj_1 = world.get_location("dD Investigation - Perfect Agent Objective 1")
            world.set_rule(investigation_prf_agent_obj_1, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2")
                                                          | HasAll("dD Investigation - Perfect Agent", "CamSpy", "CMP150"))

            investigation_prf_agent_obj_2 = world.get_location("dD Investigation - Perfect Agent Objective 2")
            world.set_rule(investigation_prf_agent_obj_2, HasAll("dD Investigation - Perfect Agent", "Falcon 2")
                                                          | HasAll("dD Investigation - Perfect Agent", "CMP150"))

            investigation_prf_agent_obj_3 = world.get_location("dD Investigation - Perfect Agent Objective 3")
            world.set_rule(investigation_prf_agent_obj_3, HasAll("dD Investigation - Perfect Agent", "Falcon 2", "CMP150"))

            investigation_prf_agent_obj_4 = world.get_location("dD Investigation - Perfect Agent Objective 4")
            world.set_rule(investigation_prf_agent_obj_4, HasAll("dD Investigation - Perfect Agent", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))

            investigation_prf_agent_obj_5 = world.get_location("dD Investigation - Perfect Agent Objective 5")
            world.set_rule(investigation_prf_agent_obj_5, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))

            investigation_prf_agent_complete = world.get_location("Complete: dD Investigation - Perfect Agent")
            world.set_rule(investigation_prf_agent_complete, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


            # Stage 3 - Extraction
            extraction_prf_agent_obj_1 = world.get_location("dD Extraction - Perfect Agent Objective 1")
            world.set_rule(extraction_prf_agent_obj_1, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150"))

            extraction_prf_agent_obj_2 = world.get_location("dD Extraction - Perfect Agent Objective 2")
            world.set_rule(extraction_prf_agent_obj_2, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150"))

            extraction_prf_agent_obj_3 = world.get_location("dD Extraction - Perfect Agent Objective 3")
            world.set_rule(extraction_prf_agent_obj_3, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun", "Rocket Launcher"))

            extraction_prf_agent_obj_4 = world.get_location("dD Extraction - Perfect Agent Objective 4")
            world.set_rule(extraction_prf_agent_obj_4, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_prf_agent_obj_5 = world.get_location("dD Extraction - Perfect Agent Objective 5")
            world.set_rule(extraction_prf_agent_obj_5, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_prf_agent_complete = world.get_location("Complete: dD Extraction - Perfect Agent")
            world.set_rule(extraction_prf_agent_complete, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher")
                                                          | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun", "Rocket Launcher"))


            # Stage 4 - Villa
            villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
            world.set_rule(villa_prf_agent_obj_1, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun")
                                                  | HasAll("Carrington Villa - Perfect Agent", "CMP150"))

            villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
            world.set_rule(villa_prf_agent_obj_2, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun")
                                                  | HasAll("Carrington Villa - Perfect Agent", "CMP150"))

            villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
            world.set_rule(villa_prf_agent_obj_3, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150"))

            villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
            world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

            villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
            world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"))

            villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
            world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
            world.set_rule(chicago_prf_agent_obj_1, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "CMP150"))

            chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
            world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "Tracer Bug", "CMP150"))

            chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
            world.set_rule(chicago_prf_agent_obj_3, HasAll("Chicago - Perfect Agent", "Remote Mine", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "Remote Mine", "CMP150"))

            chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
            world.set_rule(chicago_prf_agent_obj_4, HasAll("Chicago - Perfect Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "Data Uplink", "CMP150") 
                                                    | HasAll("Chicago - Perfect Agent", "CamSpy", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "CamSpy", "CMP150"))

            chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
            world.set_rule(chicago_prf_agent_obj_5, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))
            
            chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
            world.set_rule(chicago_prf_agent_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))


            # Stage 6 - G5 Building
            g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
            world.set_rule(g5_prf_agent_obj_1, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150") & HAS_G5_KEYS))

            g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
            world.set_rule(g5_prf_agent_obj_2, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150") & HAS_G5_KEYS))

            g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
            world.set_rule(g5_prf_agent_obj_3, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150", "CamSpy") & HAS_G5_KEYS))

            g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
            world.set_rule(g5_prf_agent_obj_4, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)

            g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
            world.set_rule(g5_prf_agent_obj_5, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "Remote Mine") & HAS_G5_KEYS)

            g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
            world.set_rule(g5_prf_agent_complete, HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
            

            # Stage 7 - Infiltration
            infiltration_prf_agent_obj_1 = world.get_location("A51 Infiltration - Perfect Agent Objective 1")
            world.set_rule(infiltration_prf_agent_obj_1, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Explosives")
                                                         | HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Explosives"))

            infiltration_prf_agent_obj_2 = world.get_location("A51 Infiltration - Perfect Agent Objective 2")
            world.set_rule(infiltration_prf_agent_obj_2, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Comms Rider")
                                                         | HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Comms Rider"))

            infiltration_prf_agent_obj_3 = world.get_location("A51 Infiltration - Perfect Agent Objective 3")
            world.set_rule(infiltration_prf_agent_obj_3, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4"))

            infiltration_prf_agent_obj_4 = world.get_location("A51 Infiltration - Perfect Agent Objective 4")
            world.set_rule(infiltration_prf_agent_obj_4, (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)
                                                         | (HasAll("A51 Infiltration - Perfect Agent", "MagSec 4") & HAS_A51_INFIL_KEYS))

            infiltration_prf_agent_obj_5 = world.get_location("A51 Infiltration - Perfect Agent Objective 5")
            world.set_rule(infiltration_prf_agent_obj_5, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)

            infiltration_prf_agent_complete = world.get_location("Complete: A51 Infiltration - Perfect Agent")
            world.set_rule(infiltration_prf_agent_complete, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)


            # Stage 8 - Rescue
            rescue_prf_agent_obj_1 = world.get_location("A51 Rescue - Perfect Agent Objective 1")
            world.set_rule(rescue_prf_agent_obj_1, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Data Uplink")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Dragon", "Data Uplink"))

            rescue_prf_agent_obj_2 = world.get_location("A51 Rescue - Perfect Agent Objective 2")
            world.set_rule(rescue_prf_agent_obj_2, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Dragon", "X-Ray Scanner"))

            rescue_prf_agent_obj_3 = world.get_location("A51 Rescue - Perfect Agent Objective 3")
            world.set_rule(rescue_prf_agent_obj_3, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Lab Clothes"))

            rescue_prf_agent_obj_4 = world.get_location("A51 Rescue - Perfect Agent Objective 4")
            world.set_rule(rescue_prf_agent_obj_4, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)

            rescue_prf_agent_obj_5 = world.get_location("A51 Rescue - Perfect Agent Objective 5")
            world.set_rule(rescue_prf_agent_obj_5, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
            
            rescue_prf_agent_complete = world.get_location("Complete: A51 Rescue - Perfect Agent")
            world.set_rule(rescue_prf_agent_complete, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


            # Stage 9 - Escape
            escape_prf_agent_obj_1 = world.get_location("A51 Escape - Perfect Agent Objective 1")
            world.set_rule(escape_prf_agent_obj_1, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "SuperDragon", "Alien Medpack"))

            escape_prf_agent_obj_2 = world.get_location("A51 Escape - Perfect Agent Objective 2")
            world.set_rule(escape_prf_agent_obj_2, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)")
                                                   | HasAll("A51 Escape - Perfect Agent", "SuperDragon"))

            escape_prf_agent_obj_3 = world.get_location("A51 Escape - Perfect Agent Objective 3")
            world.set_rule(escape_prf_agent_obj_3, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon"))

            escape_prf_agent_obj_4 = world.get_location("A51 Escape - Perfect Agent Objective 4")
            world.set_rule(escape_prf_agent_obj_4, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))

            escape_prf_agent_obj_5 = world.get_location("A51 Escape - Perfect Agent Objective 5")
            world.set_rule(escape_prf_agent_obj_5, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))
            
            escape_prf_agent_complete = world.get_location("Complete: A51 Escape - Perfect Agent")
            world.set_rule(escape_prf_agent_complete, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
            world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

            air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
            world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

            air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
            world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

            air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
            world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "Proximity Mine", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "Proximity Mine", "Stewardess Disguise", "Flight Plans"))

            air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
            world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))
            
            air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
            world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                        | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))


            # Stage 11 - Air Force One
            air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
            world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
            world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
            world.set_rule(air_force_one_prf_agent_obj_3, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger") & HAS_AFO_ALL_KEYS))

            air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
            world.set_rule(air_force_one_prf_agent_obj_4, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_ALL_KEYS))

            air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
            world.set_rule(air_force_one_prf_agent_obj_5, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_ALL_KEYS))

            air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
            world.set_rule(air_force_one_prf_agent_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


            # Stage 12 - Crash Site
            crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
            world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "President Scanner", "Falcon 2 (Scope)")
                                                       | HasAll("Crash Site - Perfect Agent", "President Scanner", "K7 Avenger")
                                                       | HasAll("Crash Site - Perfect Agent", "President Scanner", "Sniper Rifle"))

            crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
            world.set_rule(crash_site_prf_agent_obj_2, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)")
                                                       | HasAll("Crash Site - Perfect Agent", "K7 Avenger")
                                                       | HasAll("Crash Site - Perfect Agent", "Sniper Rifle"))
    
            crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
            world.set_rule(crash_site_prf_agent_obj_3, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "Remote Mine")
                                                       | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"))

            crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
            world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))

            crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
            world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
            world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"))


            # Stage 13 - Pelagic II
            pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
            world.set_rule(pelagic_prf_agent_obj_1, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "X-Ray Scanner")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150", "X-Ray Scanner"))

            pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
            world.set_rule(pelagic_prf_agent_obj_2, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150", "Research Tape"))

            pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
            world.set_rule(pelagic_prf_agent_obj_3, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150"))

            pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
            world.set_rule(pelagic_prf_agent_obj_4, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150"))

            pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
            world.set_rule(pelagic_prf_agent_obj_5, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))
            
            pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
            world.set_rule(pelagic_prf_agent_complete, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))


            # Stage 14 - Deep Sea
            deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
            world.set_rule(deep_sea_prf_agent_obj_1, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner"))

            deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
            world.set_rule(deep_sea_prf_agent_obj_2, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20"))

            deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
            world.set_rule(deep_sea_prf_agent_obj_3, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20"))

            deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
            world.set_rule(deep_sea_prf_agent_obj_4, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))

            deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
            world.set_rule(deep_sea_prf_agent_obj_5, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"))
            
            deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
            world.set_rule(deep_sea_prf_agent_complete, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                        | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
            world.set_rule(institute_defense_prf_agent_obj_1, HasAll("CI Defense - Perfect Agent", "AR34"))

            institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
            world.set_rule(institute_defense_prf_agent_obj_2, HasAll("CI Defense - Perfect Agent", "AR34"))

            institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
            world.set_rule(institute_defense_prf_agent_obj_3, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120"))

            institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
            world.set_rule(institute_defense_prf_agent_obj_4, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser")
                                                              | HasAll("CI Defense - Perfect Agent", "AR34", "Devastator"))

            institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
            world.set_rule(institute_defense_prf_agent_obj_5, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                              | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))

            institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
            world.set_rule(institute_defense_prf_agent_complete, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                                 | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
            world.set_rule(attack_ship_prf_agent_obj_1, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler"))

            attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
            world.set_rule(attack_ship_prf_agent_obj_2, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler"))

            attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
            world.set_rule(attack_ship_prf_agent_obj_3, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
            world.set_rule(attack_ship_prf_agent_obj_4, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
            world.set_rule(attack_ship_prf_agent_obj_5, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))

            attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
            world.set_rule(attack_ship_prf_agent_complete, HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))    


            # Stage 17 - Skedar Ruins
            skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
            world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
            world.set_rule(skedar_ruins_prf_agent_obj_2, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
            world.set_rule(skedar_ruins_prf_agent_obj_3, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
            world.set_rule(skedar_ruins_prf_agent_obj_4, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
            world.set_rule(skedar_ruins_prf_agent_obj_5, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
            world.set_rule(skedar_ruins_prf_agent_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            world.set_rule(mbr_prf_agent_obj_1, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb"))

            mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            world.set_rule(mbr_prf_agent_obj_2, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150", "Cloaking Device"))

            mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            world.set_rule(mbr_prf_agent_obj_3, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150", "Cloaking Device"))

            mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
            world.set_rule(mbr_prf_agent_complete, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device", "Skedar Bomb")
                                                   | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150", "Cloaking Device", "Skedar Bomb"))


            # Stage 19 - Maian SOS
            maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
            world.set_rule(maian_sos_prf_agent_obj_1, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
            world.set_rule(maian_sos_prf_agent_obj_2, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon", "DY357-LX"))

            maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
            world.set_rule(maian_sos_prf_agent_obj_3, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
            world.set_rule(maian_sos_prf_agent_complete, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon", "DY357-LX"))


            # Stage 20 - WAR!
            war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
            world.set_rule(war_prf_agent_obj_1, HasAll("WAR! - Perfect Agent", "Phoenix"))

            war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
            world.set_rule(war_prf_agent_obj_2, HasAll("WAR! - Perfect Agent", "Phoenix"))

            war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
            world.set_rule(war_prf_agent_obj_3, HasAll("WAR! - Perfect Agent", "Phoenix"))

            war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
            world.set_rule(war_prf_agent_complete, HasAll("WAR! - Perfect Agent", "Phoenix"))


            # Stage 21 - The Duel
            duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
            world.set_rule(duel_prf_agent_obj_1, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))

            duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
            world.set_rule(duel_prf_agent_obj_2, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))

            duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
            world.set_rule(duel_prf_agent_obj_3, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))
            
            duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
            world.set_rule(duel_prf_agent_complete, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)"))


        if world.options.unlock_cheats:
            # Defection
            cheat_defection_complete = world.get_location("Cheat Unlock: Complete dD Defection")
            world.set_rule(cheat_defection_complete, HasAll("dD Defection - Agent", "Falcon 2 (Silencer)")
                                                     | HasAll("dD Defection - Agent", "CMP150")
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS))


            # Investigation
            cheat_investigation_complete = world.get_location("Cheat Unlock: Complete dD Investigation")
            world.set_rule(cheat_investigation_complete, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink")
                                                         | HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "CMP150", "Data Uplink")
                                                         | HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


            # Extraction
            cheat_extraction_complete = world.get_location("Cheat Unlock: Complete dD Extraction")
            world.set_rule(cheat_extraction_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun", "Rocket Launcher"))


            # Villa
            cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
            world.set_rule(cheat_villa_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "CMP150", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"))


            # Chicago
            cheat_chicago_complete = world.get_location("Cheat Unlock: Complete Chicago")
            world.set_rule(cheat_chicago_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))


            # G5 Building
            cheat_g5_complete = world.get_location("Cheat Unlock: Complete G5 Building")
            world.set_rule(cheat_g5_complete, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS))


            # Infiltration
            cheat_infiltration_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration")
            world.set_rule(cheat_infiltration_complete, (HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))


            # Rescue
            cheat_rescue_complete = world.get_location("Cheat Unlock: Complete A51 Rescue")
            world.set_rule(cheat_rescue_complete, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))


            # Escape
            cheat_escape_complete = world.get_location("Cheat Unlock: Complete A51 Escape")
            world.set_rule(cheat_escape_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


            # Air Base
            cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
            world.set_rule(cheat_air_base_complete, HasAll("Air Base - Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                    | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"))
    

            # Air Force One
            cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
            world.set_rule(cheat_air_force_one_complete, HasAll("Air Force One - Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine")
                                                         | (HasAll("Air Force One - Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_EXTRA_KEYS)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS)
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


            # Crash Site
            cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
            world.set_rule(cheat_crash_site_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine")
                                                      | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"))


            # Pelagic II
            cheat_pelagic_complete = world.get_location("Cheat Unlock: Complete Pelagic II")
            world.set_rule(cheat_pelagic_complete, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))


            # Deep Sea
            cheat_deep_sea_complete = world.get_location("Cheat Unlock: Complete Deep Sea")
            world.set_rule(cheat_deep_sea_complete, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                    | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))


            # CI Defense
            cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
            world.set_rule(cheat_institute_defense_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                             | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))


            # Attack Ship
            cheat_attack_ship_complete = world.get_location("Cheat Unlock: Complete Attack Ship")
            world.set_rule(cheat_attack_ship_complete, HasAll("Attack Ship - Agent", "Combat Knife", "Mauler", "AR34")
                                                       | HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34")
                                                       | HasAll("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"))


            # Skedar Ruins
            cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
            world.set_rule(cheat_skedar_ruins_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                        | HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                        | HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))

            
            if world.options.agent:
                # Extraction
                cheat_extraction_timed_complete = world.get_location("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
                world.set_rule(cheat_extraction_timed_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                                | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))


                # G5 Building
                cheat_g5_timed_complete = world.get_location("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
                world.set_rule(cheat_g5_timed_complete, HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)


                # Escape
                cheat_escape_timed_complete = world.get_location("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
                world.set_rule(cheat_escape_timed_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"))


                # Crash Site
                cheat_crash_site_timed_complete = world.get_location("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
                world.set_rule(cheat_crash_site_timed_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "Sniper Rifle", "President Scanner"))


                # CI Defense
                cheat_institute_defense_timed_complete = world.get_location("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")
                world.set_rule(cheat_institute_defense_timed_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))


            if world.options.special_agent:
                # Defection
                cheat_defection_timed_complete = world.get_location("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
                world.set_rule(cheat_defection_timed_complete, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)", "CMP150") & HAS_DD_KEYS)


                # Villa
                cheat_villa_timed_complete = world.get_location("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
                world.set_rule(cheat_villa_timed_complete, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "CMP150", "Cellar Key Card"))


                # Infiltration
                cheat_infiltration_timed_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
                world.set_rule(cheat_infiltration_timed_complete, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)


                # Air Base
                cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                              | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "K7 Avenger", "Stewardess Disguise", "Suitcase"))


                # Pelagic II
                cheat_pelagic_timed_complete = world.get_location("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
                world.set_rule(cheat_pelagic_timed_complete, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "CMP150", "X-Ray Scanner"))


                # Attack Ship
                cheat_attack_ship_timed_complete = world.get_location("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")
                world.set_rule(cheat_attack_ship_timed_complete, HasAll("Attack Ship - Special Agent", "Combat Knife", "Mauler", "AR34"))


            if world.options.perfect_agent:
                # Investigation
                cheat_investigation_timed_complete = world.get_location("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
                world.set_rule(cheat_investigation_timed_complete, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


                # Chicago
                cheat_chicago_timed_complete = world.get_location("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
                world.set_rule(cheat_chicago_timed_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)", "CMP150"))


                # Rescue
                cheat_rescue_timed_complete = world.get_location("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
                world.set_rule(cheat_rescue_timed_complete, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)


                # Air Force One
                cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                world.set_rule(cheat_air_force_one_timed_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                                   | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "K7 Avenger", "Timed Mine") & HAS_AFO_ALL_KEYS))


                # Deep Sea
                cheat_deep_sea_timed_complete = world.get_location("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
                world.set_rule(cheat_deep_sea_timed_complete, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                              | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))


                # Skedar Ruins
                cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                world.set_rule(cheat_skedar_ruins_timed_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


    elif world.options.weapon_progression.value > WeaponProgression.option_vanilla:
        if world.options.agent:
            # Stage 1 - Defection
            defection_agent_obj_1 = world.get_location("dD Defection - Agent Objective 1")
            world.set_rule(defection_agent_obj_1, Has("dD Defection - Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_agent_complete = world.get_location("Complete: dD Defection - Agent")
            world.set_rule(defection_agent_complete, Has("dD Defection - Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))


            # Stage 2 - Investigation
            investigation_agent_obj_1 = world.get_location("dD Investigation - Agent Objective 1")
            world.set_rule(investigation_agent_obj_1, HasAll("dD Investigation - Agent", "CamSpy")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_agent_obj_2 = world.get_location("dD Investigation - Agent Objective 2")
            world.set_rule(investigation_agent_obj_2, HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_agent_complete = world.get_location("Complete: dD Investigation - Agent")
            world.set_rule(investigation_agent_complete, HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 3 - Extraction
            extraction_agent_obj_1 = world.get_location("dD Extraction - Agent Objective 1")
            world.set_rule(extraction_agent_obj_1, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            extraction_agent_obj_2 = world.get_location("dD Extraction - Agent Objective 2")
            world.set_rule(extraction_agent_obj_2, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_agent_obj_3 = world.get_location("dD Extraction - Agent Objective 3")
            world.set_rule(extraction_agent_obj_3, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_agent_complete = world.get_location("Complete: dD Extraction - Agent")
            world.set_rule(extraction_agent_complete, HasAll("dD Extraction - Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 4 - Villa
            villa_agent_obj_1 = world.get_location("Carrington Villa - Agent Objective 1")
            world.set_rule(villa_agent_obj_1, Has("Carrington Villa - Agent")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_agent_obj_2 = world.get_location("Carrington Villa - Agent Objective 2")
            world.set_rule(villa_agent_obj_2, Has("Carrington Villa - Agent")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_agent_obj_3 = world.get_location("Carrington Villa - Agent Objective 3")
            world.set_rule(villa_agent_obj_3, HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_agent_complete = world.get_location("Complete: Carrington Villa - Agent")
            world.set_rule(villa_agent_complete, HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
            world.set_rule(chicago_agent_obj_1, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                | (HasAll("Chicago - Agent", "Data Uplink")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
            world.set_rule(chicago_agent_obj_2, (HasAll("Chicago - Agent", "Data Uplink")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                | (HasAll("Chicago - Agent", "CamSpy")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

            chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
            world.set_rule(chicago_agent_obj_3, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                | (HasAll("Chicago - Agent", "Data Uplink") 
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
            world.set_rule(chicago_agent_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_agent_obj_1 = world.get_location("G5 Building - Agent Objective 1")
            world.set_rule(g5_agent_obj_1, HasAll("G5 Building - Agent", "CamSpy") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_obj_2 = world.get_location("G5 Building - Agent Objective 2")
            world.set_rule(g5_agent_obj_2, HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_obj_3 = world.get_location("G5 Building - Agent Objective 3")
            world.set_rule(g5_agent_obj_3, HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_complete = world.get_location("Complete: G5 Building - Agent")
            world.set_rule(g5_agent_complete, HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 7 - Infiltration
            infiltration_agent_obj_1 = world.get_location("A51 Infiltration - Agent Objective 1")
            world.set_rule(infiltration_agent_obj_1, HasAll("A51 Infiltration - Agent", "Explosives")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_obj_2 = world.get_location("A51 Infiltration - Agent Objective 2")
            world.set_rule(infiltration_agent_obj_2, HasAll("A51 Infiltration - Agent") & HAS_A51_INFIL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_obj_3 = world.get_location("A51 Infiltration - Agent Objective 3")
            world.set_rule(infiltration_agent_obj_3, HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_complete = world.get_location("Complete: A51 Infiltration - Agent")
            world.set_rule(infiltration_agent_complete, HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_agent_obj_1 = world.get_location("A51 Rescue - Agent Objective 1")
            world.set_rule(rescue_agent_obj_1, HasAll("A51 Rescue - Agent", "Lab Clothes")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_agent_obj_2 = world.get_location("A51 Rescue - Agent Objective 2")
            world.set_rule(rescue_agent_obj_2, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_agent_obj_3 = world.get_location("A51 Rescue - Agent Objective 3")
            world.set_rule(rescue_agent_obj_3, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_agent_complete = world.get_location("Complete: A51 Rescue - Agent")
            world.set_rule(rescue_agent_complete, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_agent_obj_1 = world.get_location("A51 Escape - Agent Objective 1")
            world.set_rule(escape_agent_obj_1, Has("A51 Escape - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_agent_obj_2 = world.get_location("A51 Escape - Agent Objective 2")
            world.set_rule(escape_agent_obj_2, Has("A51 Escape - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_agent_obj_3 = world.get_location("A51 Escape - Agent Objective 3")
            world.set_rule(escape_agent_obj_3, HasAll("A51 Escape - Agent", "Alien Medpack")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_agent_complete = world.get_location("Complete: A51 Escape - Agent")
            world.set_rule(escape_agent_complete, HasAll("A51 Escape - Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
                world.set_rule(air_base_agent_obj_1, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                     | (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")))

                air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
                world.set_rule(air_base_agent_obj_2, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                     | (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")))

                air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
                world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "Stewardess Disguise")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                
                air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
                world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
                world.set_rule(air_base_agent_obj_1, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

                air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
                world.set_rule(air_base_agent_obj_2, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

                air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
                world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

                air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
                world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 11 - Air Force One
            air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
            world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

            air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
            world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Suitcase")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
            world.set_rule(air_force_one_agent_obj_3, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Air Force One - Agent", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
            world.set_rule(air_force_one_agent_complete, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Agent", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_agent_obj_1 = world.get_location("Crash Site - Agent Objective 1")
            world.set_rule(crash_site_agent_obj_1, Has("Crash Site - Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_agent_obj_2 = world.get_location("Crash Site - Agent Objective 2")
            world.set_rule(crash_site_agent_obj_2, HasAll("Crash Site - Agent", "President Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_agent_obj_3 = world.get_location("Crash Site - Agent Objective 3")
            world.set_rule(crash_site_agent_obj_3, HasAll("Crash Site - Agent", "President Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_agent_complete = world.get_location("Complete: Crash Site - Agent")
            world.set_rule(crash_site_agent_complete, HasAll("Crash Site - Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_agent_obj_1 = world.get_location("Pelagic II - Agent Objective 1")
            world.set_rule(pelagic_agent_obj_1, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_agent_obj_2 = world.get_location("Pelagic II - Agent Objective 2")
            world.set_rule(pelagic_agent_obj_2, Has("Pelagic II - Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_agent_obj_3 = world.get_location("Pelagic II - Agent Objective 3")
            world.set_rule(pelagic_agent_obj_3, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_agent_complete = world.get_location("Complete: Pelagic II - Agent")
            world.set_rule(pelagic_agent_complete, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_agent_obj_1 = world.get_location("Deep Sea - Agent Objective 1")
            world.set_rule(deep_sea_agent_obj_1, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_obj_2 = world.get_location("Deep Sea - Agent Objective 2")
            world.set_rule(deep_sea_agent_obj_2, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_obj_3 = world.get_location("Deep Sea - Agent Objective 3")
            world.set_rule(deep_sea_agent_obj_3, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_complete = world.get_location("Complete: Deep Sea - Agent")
            world.set_rule(deep_sea_agent_complete, HasAll("Deep Sea - Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 15 - Carrington Institute Defense
            institute_defense_agent_obj_1 = world.get_location("CI Defense - Agent Objective 1")
            world.set_rule(institute_defense_agent_obj_1, Has("CI Defense - Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_agent_obj_2 = world.get_location("CI Defense - Agent Objective 2")
            world.set_rule(institute_defense_agent_obj_2, (HasAll("CI Defense - Agent", "RC-P120")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                          | (Has("CI Defense - Agent")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_agent_obj_3 = world.get_location("CI Defense - Agent Objective 3")
            world.set_rule(institute_defense_agent_obj_3, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                          | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_agent_complete = world.get_location("Complete: CI Defense - Agent")
            world.set_rule(institute_defense_agent_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_agent_obj_1 = world.get_location("Attack Ship - Agent Objective 1")
            world.set_rule(attack_ship_agent_obj_1, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_obj_2 = world.get_location("Attack Ship - Agent Objective 2")
            world.set_rule(attack_ship_agent_obj_2, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_obj_3 = world.get_location("Attack Ship - Agent Objective 3")
            world.set_rule(attack_ship_agent_obj_3, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_complete = world.get_location("Complete: Attack Ship - Agent")
            world.set_rule(attack_ship_agent_complete, Has("Attack Ship - Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
                world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
                world.set_rule(skedar_ruins_agent_obj_2, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                         | (HAS_SKEDAR_RUINS_AGENT
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
                world.set_rule(skedar_ruins_agent_obj_3, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                         | (HAS_SKEDAR_RUINS_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
                world.set_rule(skedar_ruins_agent_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
                world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
                world.set_rule(skedar_ruins_agent_obj_2, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
                world.set_rule(skedar_ruins_agent_obj_3, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "IR Scanner")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
                world.set_rule(skedar_ruins_agent_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Agent Objective 1")
            world.set_rule(mbr_agent_obj_1, HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Agent")
            world.set_rule(mbr_agent_complete, HasAll("Mr. Blonde's Revenge - Agent", "Cloaking Device")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_agent_obj_1 = world.get_location("Maian SOS - Agent Objective 1")
            world.set_rule(maian_sos_agent_obj_1, Has("Maian SOS - Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_agent_complete = world.get_location("Complete: Maian SOS - Agent")
            world.set_rule(maian_sos_agent_complete, Has("Maian SOS - Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 20 - WAR!
            war_agent_obj_1 = world.get_location("WAR! - Agent Objective 1")
            world.set_rule(war_agent_obj_1, Has("WAR! - Agent")
                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_agent_complete = world.get_location("Complete: WAR! - Agent")
            world.set_rule(war_agent_complete, Has("WAR! - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_agent_obj_1 = world.get_location("The Duel - Agent Objective 1")
            world.set_rule(duel_agent_obj_1, Has("The Duel - Agent")
                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_agent_complete = world.get_location("Complete: The Duel - Agent")
            world.set_rule(duel_agent_complete, Has("The Duel - Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


        if world.options.special_agent:
            # Stage 1 - Defection
            defection_sp_agent_obj_1 = world.get_location("dD Defection - Special Agent Objective 1")
            world.set_rule(defection_sp_agent_obj_1, HasAll("dD Defection - Special Agent", "ECM Mine")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_sp_agent_obj_2 = world.get_location("dD Defection - Special Agent Objective 2")
            world.set_rule(defection_sp_agent_obj_2, Has("dD Defection - Special Agent") & HAS_DD_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_sp_agent_obj_3 = world.get_location("dD Defection - Special Agent Objective 3")
            world.set_rule(defection_sp_agent_obj_3, HasAll("dD Defection - Special Agent", "ECM Mine")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_sp_agent_obj_4 = world.get_location("dD Defection - Special Agent Objective 4")
            world.set_rule(defection_sp_agent_obj_4, Has("dD Defection - Special Agent") & HAS_DD_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_sp_agent_complete = world.get_location("Complete: dD Defection - Special Agent")
            world.set_rule(defection_sp_agent_complete, HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 2 - Investigation
            investigation_sp_agent_obj_1 = world.get_location("dD Investigation - Special Agent Objective 1")
            world.set_rule(investigation_sp_agent_obj_1, HasAll("dD Investigation - Special Agent", "CamSpy")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_sp_agent_obj_2 = world.get_location("dD Investigation - Special Agent Objective 2")
            world.set_rule(investigation_sp_agent_obj_2, Has("dD Investigation - Special Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_sp_agent_obj_3 = world.get_location("dD Investigation - Special Agent Objective 3")
            world.set_rule(investigation_sp_agent_obj_3, Has("dD Investigation - Special Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_sp_agent_obj_4 = world.get_location("dD Investigation - Special Agent Objective 4")
            world.set_rule(investigation_sp_agent_obj_4, HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_sp_agent_complete = world.get_location("Complete: dD Investigation - Special Agent")
            world.set_rule(investigation_sp_agent_complete, HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 3 - Extraction
            extraction_sp_agent_obj_1 = world.get_location("dD Extraction - Special Agent Objective 1")
            world.set_rule(extraction_sp_agent_obj_1, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            extraction_sp_agent_obj_2 = world.get_location("dD Extraction - Special Agent Objective 2")
            world.set_rule(extraction_sp_agent_obj_2, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))

            extraction_sp_agent_obj_3 = world.get_location("dD Extraction - Special Agent Objective 3")
            world.set_rule(extraction_sp_agent_obj_3, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_obj_4 = world.get_location("dD Extraction - Special Agent Objective 4")
            world.set_rule(extraction_sp_agent_obj_4, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_complete = world.get_location("Complete: dD Extraction - Special Agent")
            world.set_rule(extraction_sp_agent_complete, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))


            # Stage 4 - Villa
            villa_sp_agent_obj_1 = world.get_location("Carrington Villa - Special Agent Objective 1")
            world.set_rule(villa_sp_agent_obj_1, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_obj_2 = world.get_location("Carrington Villa - Special Agent Objective 2")
            world.set_rule(villa_sp_agent_obj_2, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_obj_3 = world.get_location("Carrington Villa - Special Agent Objective 3")
            world.set_rule(villa_sp_agent_obj_3, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_sp_agent_obj_4 = world.get_location("Carrington Villa - Special Agent Objective 4")
            world.set_rule(villa_sp_agent_obj_4, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_complete = world.get_location("Complete: Carrington Villa - Special Agent")
            world.set_rule(villa_sp_agent_complete, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
            world.set_rule(chicago_sp_agent_obj_1, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                   | (HasAll("Chicago - Special Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
            world.set_rule(chicago_sp_agent_obj_2, (HasAll("Chicago - Special Agent", "Remote Mine")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (Has("Chicago - Special Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
            world.set_rule(chicago_sp_agent_obj_3, (HasAll("Chicago - Special Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "CamSpy")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

            chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
            world.set_rule(chicago_sp_agent_obj_4, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
            world.set_rule(chicago_sp_agent_complete, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                      | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_sp_agent_obj_1 = world.get_location("G5 Building - Special Agent Objective 1")
            world.set_rule(g5_sp_agent_obj_1, Has("G5 Building - Special Agent") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_2 = world.get_location("G5 Building - Special Agent Objective 2")
            world.set_rule(g5_sp_agent_obj_2, HasAll("G5 Building - Special Agent", "CamSpy") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_3 = world.get_location("G5 Building - Special Agent Objective 3")
            world.set_rule(g5_sp_agent_obj_3, HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_4 = world.get_location("G5 Building - Special Agent Objective 4")
            world.set_rule(g5_sp_agent_obj_4, (HasAll("G5 Building - Special Agent", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (Has("G5 Building - Special Agent") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            g5_sp_agent_complete = world.get_location("Complete: G5 Building - Special Agent")
            world.set_rule(g5_sp_agent_complete, ((HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                 | ((HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 7 - Infiltration
            infiltration_sp_agent_obj_1 = world.get_location("A51 Infiltration - Special Agent Objective 1")
            world.set_rule(infiltration_sp_agent_obj_1, HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_2 = world.get_location("A51 Infiltration - Special Agent Objective 2")
            world.set_rule(infiltration_sp_agent_obj_2, HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_3 = world.get_location("A51 Infiltration - Special Agent Objective 3")
            world.set_rule(infiltration_sp_agent_obj_3, HasAll("A51 Infiltration - Special Agent") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_4 = world.get_location("A51 Infiltration - Special Agent Objective 4")
            world.set_rule(infiltration_sp_agent_obj_4, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_complete = world.get_location("Complete: A51 Infiltration - Special Agent")
            world.set_rule(infiltration_sp_agent_complete, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_sp_agent_obj_1 = world.get_location("A51 Rescue - Special Agent Objective 1")
            world.set_rule(rescue_sp_agent_obj_1, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_2 = world.get_location("A51 Rescue - Special Agent Objective 2")
            world.set_rule(rescue_sp_agent_obj_2, HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_3 = world.get_location("A51 Rescue - Special Agent Objective 3")
            world.set_rule(rescue_sp_agent_obj_3, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_4 = world.get_location("A51 Rescue - Special Agent Objective 4")
            world.set_rule(rescue_sp_agent_obj_4, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_sp_agent_complete = world.get_location("Complete: A51 Rescue - Special Agent")
            world.set_rule(rescue_sp_agent_complete, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_sp_agent_obj_1 = world.get_location("A51 Escape - Special Agent Objective 1")
            world.set_rule(escape_sp_agent_obj_1, Has("A51 Escape - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_sp_agent_obj_2 = world.get_location("A51 Escape - Special Agent Objective 2")
            world.set_rule(escape_sp_agent_obj_2, Has("A51 Escape - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_sp_agent_obj_3 = world.get_location("A51 Escape - Special Agent Objective 3")
            world.set_rule(escape_sp_agent_obj_3, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_sp_agent_obj_4 = world.get_location("A51 Escape - Special Agent Objective 4")
            world.set_rule(escape_sp_agent_obj_4, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_sp_agent_complete = world.get_location("Complete: A51 Escape - Special Agent")
            world.set_rule(escape_sp_agent_complete, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
                world.set_rule(air_base_sp_agent_obj_1, (HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise")))

                air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
                world.set_rule(air_base_sp_agent_obj_2, (HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")))

                air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
                world.set_rule(air_base_sp_agent_obj_3, (HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise")))

                air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
                world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
                world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
                world.set_rule(air_base_sp_agent_obj_1, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

                air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
                world.set_rule(air_base_sp_agent_obj_2, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
                world.set_rule(air_base_sp_agent_obj_3, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

                air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
                world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
                world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


            # Stage 11 - Air Force One
            air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
            world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
            world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
            world.set_rule(air_force_one_sp_agent_obj_3, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
            world.set_rule(air_force_one_sp_agent_obj_4, (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
            world.set_rule(air_force_one_sp_agent_complete, (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                            | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_sp_agent_obj_1 = world.get_location("Crash Site - Special Agent Objective 1")
            world.set_rule(crash_site_sp_agent_obj_1, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_2 = world.get_location("Crash Site - Special Agent Objective 2")
            world.set_rule(crash_site_sp_agent_obj_2, Has("Crash Site - Special Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_3 = world.get_location("Crash Site - Special Agent Objective 3")
            world.set_rule(crash_site_sp_agent_obj_3, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_4 = world.get_location("Crash Site - Special Agent Objective 4")
            world.set_rule(crash_site_sp_agent_obj_4, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_sp_agent_complete = world.get_location("Complete: Crash Site - Special Agent")
            world.set_rule(crash_site_sp_agent_complete, HasAll("Crash Site - Special Agent", "President Scanner")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_sp_agent_obj_1 = world.get_location("Pelagic II - Special Agent Objective 1")
            world.set_rule(pelagic_sp_agent_obj_1, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_2 = world.get_location("Pelagic II - Special Agent Objective 2")
            world.set_rule(pelagic_sp_agent_obj_2, Has("Pelagic II - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_3 = world.get_location("Pelagic II - Special Agent Objective 3")
            world.set_rule(pelagic_sp_agent_obj_3, Has("Pelagic II - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_4 = world.get_location("Pelagic II - Special Agent Objective 4")
            world.set_rule(pelagic_sp_agent_obj_4, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_sp_agent_complete = world.get_location("Complete: Pelagic II - Special Agent")
            world.set_rule(pelagic_sp_agent_complete, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_sp_agent_obj_1 = world.get_location("Deep Sea - Special Agent Objective 1")
            world.set_rule(deep_sea_sp_agent_obj_1, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_2 = world.get_location("Deep Sea - Special Agent Objective 2")
            world.set_rule(deep_sea_sp_agent_obj_2, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_3 = world.get_location("Deep Sea - Special Agent Objective 3")
            world.set_rule(deep_sea_sp_agent_obj_3, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_4 = world.get_location("Deep Sea - Special Agent Objective 4")
            world.set_rule(deep_sea_sp_agent_obj_4, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            
            deep_sea_sp_agent_complete = world.get_location("Complete: Deep Sea - Special Agent")
            world.set_rule(deep_sea_sp_agent_complete, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 15 - Carrington Institute Defense
            institute_defense_sp_agent_obj_1 = world.get_location("CI Defense - Special Agent Objective 1")
            world.set_rule(institute_defense_sp_agent_obj_1, Has("CI Defense - Special Agent")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_sp_agent_obj_2 = world.get_location("CI Defense - Special Agent Objective 2")
            world.set_rule(institute_defense_sp_agent_obj_2, Has("CI Defense - Special Agent")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_sp_agent_obj_3 = world.get_location("CI Defense - Special Agent Objective 3")
            world.set_rule(institute_defense_sp_agent_obj_3, (HasAll("CI Defense - Special Agent", "RC-P120")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (Has("CI Defense - Special Agent")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_sp_agent_obj_4 = world.get_location("CI Defense - Special Agent Objective 4")
            world.set_rule(institute_defense_sp_agent_obj_4, (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_sp_agent_complete = world.get_location("Complete: CI Defense - Special Agent")
            world.set_rule(institute_defense_sp_agent_complete, (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_sp_agent_obj_1 = world.get_location("Attack Ship - Special Agent Objective 1")
            world.set_rule(attack_ship_sp_agent_obj_1, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_2 = world.get_location("Attack Ship - Special Agent Objective 2")
            world.set_rule(attack_ship_sp_agent_obj_2, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_3 = world.get_location("Attack Ship - Special Agent Objective 3")
            world.set_rule(attack_ship_sp_agent_obj_3, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_4 = world.get_location("Attack Ship - Special Agent Objective 4")
            world.set_rule(attack_ship_sp_agent_obj_4, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_complete = world.get_location("Complete: Attack Ship - Special Agent")
            world.set_rule(attack_ship_sp_agent_complete, Has("Attack Ship - Special Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            

            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
                world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
                world.set_rule(skedar_ruins_sp_agent_obj_2, (HAS_SKEDAR_RUINS_SP_AGENT & Has("Devastator")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
                world.set_rule(skedar_ruins_sp_agent_obj_3, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & Has("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))
                
                skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
                world.set_rule(skedar_ruins_sp_agent_obj_4, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & Has("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
                world.set_rule(skedar_ruins_sp_agent_complete, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                               | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))
            
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
                world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
                world.set_rule(skedar_ruins_sp_agent_obj_2, HAS_SKEDAR_RUINS_SP_AGENT & Has("Devastator")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
                world.set_rule(skedar_ruins_sp_agent_obj_3, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                
                skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
                world.set_rule(skedar_ruins_sp_agent_obj_4, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
                world.set_rule(skedar_ruins_sp_agent_complete, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_sp_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 1")
            world.set_rule(mbr_sp_agent_obj_1, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_sp_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 2")
            world.set_rule(mbr_sp_agent_obj_2, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_sp_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Special Agent")
            world.set_rule(mbr_sp_agent_complete, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_sp_agent_obj_1 = world.get_location("Maian SOS - Special Agent Objective 1")
            world.set_rule(maian_sos_sp_agent_obj_1, Has("Maian SOS - Special Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_sp_agent_obj_2 = world.get_location("Maian SOS - Special Agent Objective 2")
            world.set_rule(maian_sos_sp_agent_obj_2, Has("Maian SOS - Special Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_sp_agent_complete = world.get_location("Complete: Maian SOS - Special Agent")
            world.set_rule(maian_sos_sp_agent_complete, Has("Maian SOS - Special Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 20 - WAR!
            war_sp_agent_obj_1 = world.get_location("WAR! - Special Agent Objective 1")
            world.set_rule(war_sp_agent_obj_1, Has("WAR! - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_sp_agent_obj_2 = world.get_location("WAR! - Special Agent Objective 2")
            world.set_rule(war_sp_agent_obj_2, Has("WAR! - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_sp_agent_complete = world.get_location("Complete: WAR! - Special Agent")
            world.set_rule(war_sp_agent_complete, Has("WAR! - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_sp_agent_obj_1 = world.get_location("The Duel - Special Agent Objective 1")
            world.set_rule(duel_sp_agent_obj_1, Has("The Duel - Special Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_sp_agent_obj_2 = world.get_location("The Duel - Special Agent Objective 2")
            world.set_rule(duel_sp_agent_obj_2, Has("The Duel - Special Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_sp_agent_complete = world.get_location("Complete: The Duel - Special Agent")
            world.set_rule(duel_sp_agent_complete, Has("The Duel - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


        if world.options.perfect_agent:
            # Stage 1 - Defection
            defection_prf_agent_obj_1 = world.get_location("dD Defection - Perfect Agent Objective 1")
            world.set_rule(defection_prf_agent_obj_1, HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_prf_agent_obj_2 = world.get_location("dD Defection - Perfect Agent Objective 2")
            world.set_rule(defection_prf_agent_obj_2, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            defection_prf_agent_obj_3 = world.get_location("dD Defection - Perfect Agent Objective 3")
            world.set_rule(defection_prf_agent_obj_3, HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_obj_4 = world.get_location("dD Defection - Perfect Agent Objective 4")
            world.set_rule(defection_prf_agent_obj_4, HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_obj_5 = world.get_location("dD Defection - Perfect Agent Objective 5")
            world.set_rule(defection_prf_agent_obj_5, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_complete = world.get_location("Complete: dD Defection - Perfect Agent")
            world.set_rule(defection_prf_agent_complete, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink") & HAS_DD_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 2 - Investigation
            investigation_prf_agent_obj_1 = world.get_location("dD Investigation - Perfect Agent Objective 1")
            world.set_rule(investigation_prf_agent_obj_1, HasAll("dD Investigation - Perfect Agent", "CamSpy")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_prf_agent_obj_2 = world.get_location("dD Investigation - Perfect Agent Objective 2")
            world.set_rule(investigation_prf_agent_obj_2, Has("dD Investigation - Perfect Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            investigation_prf_agent_obj_3 = world.get_location("dD Investigation - Perfect Agent Objective 3")
            world.set_rule(investigation_prf_agent_obj_3, Has("dD Investigation - Perfect Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_prf_agent_obj_4 = world.get_location("dD Investigation - Perfect Agent Objective 4")
            world.set_rule(investigation_prf_agent_obj_4, (HasAll("dD Investigation - Perfect Agent", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | HasAll("dD Investigation - Perfect Agent", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))

            investigation_prf_agent_obj_5 = world.get_location("dD Investigation - Perfect Agent Objective 5")
            world.set_rule(investigation_prf_agent_obj_5, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))

            investigation_prf_agent_complete = world.get_location("Complete: dD Investigation - Perfect Agent")
            world.set_rule(investigation_prf_agent_complete, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                             | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))


            # Stage 3 - Extraction
            extraction_prf_agent_obj_1 = world.get_location("dD Extraction - Perfect Agent Objective 1")
            world.set_rule(extraction_prf_agent_obj_1, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_2 = world.get_location("dD Extraction - Perfect Agent Objective 2")
            world.set_rule(extraction_prf_agent_obj_2, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_3 = world.get_location("dD Extraction - Perfect Agent Objective 3")
            world.set_rule(extraction_prf_agent_obj_3, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
            
            extraction_prf_agent_obj_4 = world.get_location("dD Extraction - Perfect Agent Objective 4")
            world.set_rule(extraction_prf_agent_obj_4, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_5 = world.get_location("dD Extraction - Perfect Agent Objective 5")
            world.set_rule(extraction_prf_agent_obj_5, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_complete = world.get_location("Complete: dD Extraction - Perfect Agent")
            world.set_rule(extraction_prf_agent_complete, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))


            # Stage 4 - Villa
            villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
            world.set_rule(villa_prf_agent_obj_1, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
            
            villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
            world.set_rule(villa_prf_agent_obj_2, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
            world.set_rule(villa_prf_agent_obj_3, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
            world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

            villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
            world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
            world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
            world.set_rule(chicago_prf_agent_obj_1, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
            world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
            world.set_rule(chicago_prf_agent_obj_3, (HasAll("Chicago - Perfect Agent", "Remote Mine")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (Has("Chicago - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
            world.set_rule(chicago_prf_agent_obj_4, (HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Perfect Agent", "CamSpy")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

            chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
            world.set_rule(chicago_prf_agent_obj_5, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
            world.set_rule(chicago_prf_agent_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))     


            # Stage 6 - G5 Building
            g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
            world.set_rule(g5_prf_agent_obj_1, Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
            world.set_rule(g5_prf_agent_obj_2, Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
            world.set_rule(g5_prf_agent_obj_3, HasAll("G5 Building - Perfect Agent", "CamSpy") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
            world.set_rule(g5_prf_agent_obj_4, HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
            world.set_rule(g5_prf_agent_obj_5, (HasAll("G5 Building - Perfect Agent", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                               | (Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
            world.set_rule(g5_prf_agent_complete, (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            

            # Stage 7 - Infiltration
            infiltration_prf_agent_obj_1 = world.get_location("A51 Infiltration - Perfect Agent Objective 1")
            world.set_rule(infiltration_prf_agent_obj_1, HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_2 = world.get_location("A51 Infiltration - Perfect Agent Objective 2")
            world.set_rule(infiltration_prf_agent_obj_2, HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_3 = world.get_location("A51 Infiltration - Perfect Agent Objective 3")
            world.set_rule(infiltration_prf_agent_obj_3, Has("A51 Infiltration - Perfect Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_4 = world.get_location("A51 Infiltration - Perfect Agent Objective 4")
            world.set_rule(infiltration_prf_agent_obj_4, HasAll("A51 Infiltration - Perfect Agent") & HAS_A51_INFIL_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_5 = world.get_location("A51 Infiltration - Perfect Agent Objective 5")
            world.set_rule(infiltration_prf_agent_obj_5, HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_complete = world.get_location("Complete: A51 Infiltration - Perfect Agent")
            world.set_rule(infiltration_prf_agent_complete, HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_prf_agent_obj_1 = world.get_location("A51 Rescue - Perfect Agent Objective 1")
            world.set_rule(rescue_prf_agent_obj_1, HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_2 = world.get_location("A51 Rescue - Perfect Agent Objective 2")
            world.set_rule(rescue_prf_agent_obj_2, HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_3 = world.get_location("A51 Rescue - Perfect Agent Objective 3")
            world.set_rule(rescue_prf_agent_obj_3, HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_4 = world.get_location("A51 Rescue - Perfect Agent Objective 4")
            world.set_rule(rescue_prf_agent_obj_4, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_5 = world.get_location("A51 Rescue - Perfect Agent Objective 5")
            world.set_rule(rescue_prf_agent_obj_5, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_prf_agent_complete = world.get_location("Complete: A51 Rescue - Perfect Agent")
            world.set_rule(rescue_prf_agent_complete, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_prf_agent_obj_1 = world.get_location("A51 Escape - Perfect Agent Objective 1")
            world.set_rule(escape_prf_agent_obj_1, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_2 = world.get_location("A51 Escape - Perfect Agent Objective 2")
            world.set_rule(escape_prf_agent_obj_2, Has("A51 Escape - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_3 = world.get_location("A51 Escape - Perfect Agent Objective 3")
            world.set_rule(escape_prf_agent_obj_3, Has("A51 Escape - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_4 = world.get_location("A51 Escape - Perfect Agent Objective 4")
            world.set_rule(escape_prf_agent_obj_4, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_5 = world.get_location("A51 Escape - Perfect Agent Objective 5")
            world.set_rule(escape_prf_agent_obj_5, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_prf_agent_complete = world.get_location("Complete: A51 Escape - Perfect Agent")
            world.set_rule(escape_prf_agent_complete, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            

            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, (HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                         | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise")))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, (HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                         | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase")))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, (HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                         | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise")))

                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
            
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))
                
                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


            # Stage 11 - Air Force One
            air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
            world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
            world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
            world.set_rule(air_force_one_prf_agent_obj_3, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
            world.set_rule(air_force_one_prf_agent_obj_4, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
            world.set_rule(air_force_one_prf_agent_obj_5, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
            world.set_rule(air_force_one_prf_agent_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
            world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
            world.set_rule(crash_site_prf_agent_obj_2, Has("Crash Site - Perfect Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
            world.set_rule(crash_site_prf_agent_obj_3, Has("Crash Site - Perfect Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
            world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
            world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
            world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
            world.set_rule(pelagic_prf_agent_obj_1, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
            world.set_rule(pelagic_prf_agent_obj_2, HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
            world.set_rule(pelagic_prf_agent_obj_3, Has("Pelagic II - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
            world.set_rule(pelagic_prf_agent_obj_4, Has("Pelagic II - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
            world.set_rule(pelagic_prf_agent_obj_5, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
            world.set_rule(pelagic_prf_agent_complete, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
            world.set_rule(deep_sea_prf_agent_obj_1, HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
            world.set_rule(deep_sea_prf_agent_obj_2, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
            world.set_rule(deep_sea_prf_agent_obj_3, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
            world.set_rule(deep_sea_prf_agent_obj_4, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
            world.set_rule(deep_sea_prf_agent_obj_5, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))
            
            deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
            world.set_rule(deep_sea_prf_agent_complete, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                        | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))
            

            # Stage 15 - Carrington Institute Defense
            institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
            world.set_rule(institute_defense_prf_agent_obj_1, Has("CI Defense - Perfect Agent")
                                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
            world.set_rule(institute_defense_prf_agent_obj_2, Has("CI Defense - Perfect Agent")
                                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
            world.set_rule(institute_defense_prf_agent_obj_3, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                              | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
            world.set_rule(institute_defense_prf_agent_obj_4, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                              | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                              | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))

            institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
            world.set_rule(institute_defense_prf_agent_obj_5, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                              | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
            world.set_rule(institute_defense_prf_agent_complete, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                 | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))) 


            # Stage 16 - Attack Ship
            attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
            world.set_rule(attack_ship_prf_agent_obj_1, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
            world.set_rule(attack_ship_prf_agent_obj_2, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
            world.set_rule(attack_ship_prf_agent_obj_3, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
            world.set_rule(attack_ship_prf_agent_obj_4, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
            world.set_rule(attack_ship_prf_agent_obj_5, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
            world.set_rule(attack_ship_prf_agent_complete, Has("Attack Ship - Perfect Agent")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            

            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
                world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
                world.set_rule(skedar_ruins_prf_agent_obj_2, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
                world.set_rule(skedar_ruins_prf_agent_obj_3, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
                world.set_rule(skedar_ruins_prf_agent_obj_4, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
                world.set_rule(skedar_ruins_prf_agent_obj_5, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
                world.set_rule(skedar_ruins_prf_agent_complete, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                                | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
                world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
                world.set_rule(skedar_ruins_prf_agent_obj_2, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
                world.set_rule(skedar_ruins_prf_agent_obj_3, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
                world.set_rule(skedar_ruins_prf_agent_obj_4, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
                world.set_rule(skedar_ruins_prf_agent_obj_5, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
                world.set_rule(skedar_ruins_prf_agent_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            world.set_rule(mbr_prf_agent_obj_1, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            world.set_rule(mbr_prf_agent_obj_2, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            world.set_rule(mbr_prf_agent_obj_3, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
            world.set_rule(mbr_prf_agent_complete, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
            world.set_rule(maian_sos_prf_agent_obj_1, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
            world.set_rule(maian_sos_prf_agent_obj_2, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
            world.set_rule(maian_sos_prf_agent_obj_3, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
            world.set_rule(maian_sos_prf_agent_complete, Has("Maian SOS - Perfect Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
   

            # Stage 20 - WAR!
            war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
            world.set_rule(war_prf_agent_obj_1, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
            world.set_rule(war_prf_agent_obj_2, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
            world.set_rule(war_prf_agent_obj_3, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
            world.set_rule(war_prf_agent_complete, Has("WAR! - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
            world.set_rule(duel_prf_agent_obj_1, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
            world.set_rule(duel_prf_agent_obj_2, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
            world.set_rule(duel_prf_agent_obj_3, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
            
            duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
            world.set_rule(duel_prf_agent_complete, Has("The Duel - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


        if world.options.unlock_cheats:
            # Defection
            cheat_defection_complete = world.get_location("Cheat Unlock: Complete dD Defection")
            world.set_rule(cheat_defection_complete, (Has("dD Defection - Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))


            # Investigation
            cheat_investigation_complete = world.get_location("Cheat Unlock: Complete dD Investigation")
            world.set_rule(cheat_investigation_complete, (HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))


            # Extraction
            cheat_extraction_complete = world.get_location("Cheat Unlock: Complete dD Extraction")
            world.set_rule(cheat_extraction_complete, (HasAll("dD Extraction - Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                      | (HasAll("dD Extraction - Special Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
                                                      | (HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"])))


            # Villa
            cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
            world.set_rule(cheat_villa_complete, (HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
                                                 | (HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
                                                 | (HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])))


            # Chicago
            cheat_chicago_complete = world.get_location("Cheat Unlock: Complete Chicago")
            world.set_rule(cheat_chicago_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                   | (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                   | (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # G5 Building
            cheat_g5_complete = world.get_location("Cheat Unlock: Complete G5 Building")
            world.set_rule(cheat_g5_complete, (HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                              | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                              | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Infiltration
            cheat_infiltration_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration")
            world.set_rule(cheat_infiltration_complete, (HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Rescue
            cheat_rescue_complete = world.get_location("Cheat Unlock: Complete A51 Rescue")
            world.set_rule(cheat_rescue_complete, (HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Escape
            cheat_escape_complete = world.get_location("Cheat Unlock: Complete A51 Escape")
            world.set_rule(cheat_escape_complete, (HasAll("A51 Escape - Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
                world.set_rule(cheat_air_base_complete, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                                                        | (HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))
    
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
                world.set_rule(cheat_air_base_complete, (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                                                        | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))


            # Air Force One
            cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
            world.set_rule(cheat_air_force_one_complete, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Agent", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Crash Site
            cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
            world.set_rule(cheat_crash_site_complete, (HasAll("Crash Site - Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Crash Site - Special Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Pelagic II
            cheat_pelagic_complete = world.get_location("Cheat Unlock: Complete Pelagic II")
            world.set_rule(cheat_pelagic_complete, (HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                   | (HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                   | (HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Deep Sea
            cheat_deep_sea_complete = world.get_location("Cheat Unlock: Complete Deep Sea")
            world.set_rule(cheat_deep_sea_complete, (HasAll("Deep Sea - Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))


            # CI Defense
            cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
            world.set_rule(cheat_institute_defense_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                             | (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                             | (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Attack Ship
            cheat_attack_ship_complete = world.get_location("Cheat Unlock: Complete Attack Ship")
            world.set_rule(cheat_attack_ship_complete, (Has("Attack Ship - Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                       | (Has("Attack Ship - Special Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                       | (Has("Attack Ship - Perfect Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])))


            # Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
                world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
                world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])))


            if world.options.agent:
                # Extraction
                cheat_extraction_timed_complete = world.get_location("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
                world.set_rule(cheat_extraction_timed_complete, HasAll("dD Extraction - Agent", "Night Vision")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # G5 Building
                cheat_g5_timed_complete = world.get_location("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
                world.set_rule(cheat_g5_timed_complete, HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # Escape
                cheat_escape_timed_complete = world.get_location("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
                world.set_rule(cheat_escape_timed_complete, HasAll("A51 Escape - Agent", "Alien Medpack")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Crash Site
                cheat_crash_site_timed_complete = world.get_location("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
                world.set_rule(cheat_crash_site_timed_complete, HasAll("Crash Site - Agent", "President Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # CI Defense
                cheat_institute_defense_timed_complete = world.get_location("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")
                world.set_rule(cheat_institute_defense_timed_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                       | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            if world.options.special_agent:
                # Defection
                cheat_defection_timed_complete = world.get_location("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
                world.set_rule(cheat_defection_timed_complete, HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # Villa
                cheat_villa_timed_complete = world.get_location("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
                world.set_rule(cheat_villa_timed_complete, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


                # Infiltration
                cheat_infiltration_timed_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
                world.set_rule(cheat_infiltration_timed_complete, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Air Base
                if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                    cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                    world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                    cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                    world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


                # Pelagic II
                cheat_pelagic_timed_complete = world.get_location("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
                world.set_rule(cheat_pelagic_timed_complete, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Attack Ship
                cheat_attack_ship_timed_complete = world.get_location("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")
                world.set_rule(cheat_attack_ship_timed_complete, Has("Attack Ship - Special Agent")
                                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            if world.options.perfect_agent:
                # Investigation
                cheat_investigation_timed_complete = world.get_location("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
                world.set_rule(cheat_investigation_timed_complete, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                                   | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))


                # Chicago
                cheat_chicago_timed_complete = world.get_location("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
                world.set_rule(cheat_chicago_timed_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                             | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


                # Rescue
                cheat_rescue_timed_complete = world.get_location("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
                world.set_rule(cheat_rescue_timed_complete, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Air Force One
                cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                world.set_rule(cheat_air_force_one_timed_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                                   | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


                # Deep Sea
                cheat_deep_sea_timed_complete = world.get_location("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
                world.set_rule(cheat_deep_sea_timed_complete, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                              | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))


                # Skedar Ruins
                if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                    cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                    world.set_rule(cheat_skedar_ruins_timed_complete, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                                      | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                    cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                    world.set_rule(cheat_skedar_ruins_timed_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


def set_all_perfect_location_rules(world: PerfectDarkWorld) -> None:
    if world.options.weapon_progression.value == WeaponProgression.option_vanilla:
        if world.options.agent:
            # Stage 1 - Defection
            defection_agent_obj_1 = world.get_location("dD Defection - Agent Objective 1")
            world.set_rule(defection_agent_obj_1, Has("dD Defection - Agent"))

            defection_agent_complete = world.get_location("Complete: dD Defection - Agent")
            world.set_rule(defection_agent_complete, Has("dD Defection - Agent"))


            # Stage 2 - Investigation
            investigation_agent_obj_1 = world.get_location("dD Investigation - Agent Objective 1")
            world.set_rule(investigation_agent_obj_1, HasAll("dD Investigation - Agent", "CamSpy"))

            investigation_agent_obj_2 = world.get_location("dD Investigation - Agent Objective 2")
            world.set_rule(investigation_agent_obj_2, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "Data Uplink")
                                                      | HasAll("dD Investigation - Agent", "CamSpy", "CMP150", "Data Uplink"))

            investigation_agent_complete = world.get_location("Complete: dD Investigation - Agent")
            world.set_rule(investigation_agent_complete, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "Data Uplink")
                                                         | HasAll("dD Investigation - Agent", "CamSpy", "CMP150", "Data Uplink"))

            
            # Stage 3 - Extraction
            extraction_agent_obj_1 = world.get_location("dD Extraction - Agent Objective 1")
            world.set_rule(extraction_agent_obj_1, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "CMP150"))

            extraction_agent_obj_2 = world.get_location("dD Extraction - Agent Objective 2")
            world.set_rule(extraction_agent_obj_2, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_agent_obj_3 = world.get_location("dD Extraction - Agent Objective 3")
            world.set_rule(extraction_agent_obj_3, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                   | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_agent_complete = world.get_location("Complete: dD Extraction - Agent")
            world.set_rule(extraction_agent_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))


            # Stage 4 - Villa
            villa_agent_obj_1 = world.get_location("Carrington Villa - Agent Objective 1")
            world.set_rule(villa_agent_obj_1, HasAll("Carrington Villa - Agent", "Sniper Rifle")
                                              | HasAll("Carrington Villa - Agent", "CMP150"))

            villa_agent_obj_2 = world.get_location("Carrington Villa - Agent Objective 2")
            world.set_rule(villa_agent_obj_2, HasAll("Carrington Villa - Agent", "Sniper Rifle")
                                              | HasAll("Carrington Villa - Agent", "CMP150"))

            villa_agent_obj_3 = world.get_location("Carrington Villa - Agent Objective 3")
            world.set_rule(villa_agent_obj_3, HasAll("Carrington Villa - Agent", "Sniper Rifle", "Cellar Key Card")
                                              | HasAll("Carrington Villa - Agent", "CMP150", "Cellar Key Card"))

            villa_agent_complete = world.get_location("Complete: Carrington Villa - Agent")
            world.set_rule(villa_agent_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Agent", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
            world.set_rule(chicago_agent_obj_1, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink"))

            chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
            world.set_rule(chicago_agent_obj_2, HasAll("Chicago - Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                | HasAll("Chicago - Agent", "Data Uplink", "CMP150")
                                                | HasAll("Chicago - Agent", "Data Uplink", "DY357 Magnum")
                                                | HasAll("Chicago - Agent", "CamSpy", "Falcon 2 (Scope)")
                                                | HasAll("Chicago - Agent", "CamSpy", "CMP150")
                                                | HasAll("Chicago - Agent", "CamSpy", "DY357 Magnum"))

            chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
            world.set_rule(chicago_agent_obj_3, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "CMP150")
                                                | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "DY357 Magnum"))
            
            chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
            world.set_rule(chicago_agent_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "CMP150")
                                                   | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "DY357 Magnum"))


            # Stage 6 - G5 Building
            g5_agent_obj_1 = world.get_location("G5 Building - Agent Objective 1")
            world.set_rule(g5_agent_obj_1, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)
                                           | (HasAll("G5 Building - Agent", "CMP150", "CamSpy") & HAS_G5_KEYS))

            g5_agent_obj_2 = world.get_location("G5 Building - Agent Objective 2")
            world.set_rule(g5_agent_obj_2, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                           | (HasAll("G5 Building - Agent", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS))

            g5_agent_obj_3 = world.get_location("G5 Building - Agent Objective 3")
            world.set_rule(g5_agent_obj_3, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                           | (HasAll("G5 Building - Agent", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS))

            g5_agent_complete = world.get_location("Complete: G5 Building - Agent")
            world.set_rule(g5_agent_complete, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS))


            # Stage 7 - Infiltration
            infiltration_agent_obj_1 = world.get_location("A51 Infiltration - Agent Objective 1")
            world.set_rule(infiltration_agent_obj_1, HasAll("A51 Infiltration - Agent", "Falcon 2", "Explosives")
                                                     | HasAll("A51 Infiltration - Agent", "MagSec 4", "Explosives"))

            infiltration_agent_obj_2 = world.get_location("A51 Infiltration - Agent Objective 2")
            world.set_rule(infiltration_agent_obj_2, (HasAll("A51 Infiltration - Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)
                                                     | (HasAll("A51 Infiltration - Agent", "MagSec 4") & HAS_A51_INFIL_KEYS))

            infiltration_agent_obj_3 = world.get_location("A51 Infiltration - Agent Objective 3")
            world.set_rule(infiltration_agent_obj_3, (HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Explosives") & HAS_A51_INFIL_KEYS)
                                                     | (HasAll("A51 Infiltration - Agent", "Falcon 2", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)
                                                     | (HasAll("A51 Infiltration - Agent", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS))

            infiltration_agent_complete = world.get_location("Complete: A51 Infiltration - Agent")
            world.set_rule(infiltration_agent_complete, (HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Agent", "Falcon 2", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Agent", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS))


            # Stage 8 - Rescue
            rescue_agent_obj_1 = world.get_location("A51 Rescue - Agent Objective 1")
            world.set_rule(rescue_agent_obj_1, HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Lab Clothes")
                                               | HasAll("A51 Rescue - Agent", "Dragon", "Lab Clothes"))

            rescue_agent_obj_2 = world.get_location("A51 Rescue - Agent Objective 2")
            world.set_rule(rescue_agent_obj_2, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                               | (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                               | (HasAll("A51 Rescue - Agent", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY))

            rescue_agent_obj_3 = world.get_location("A51 Rescue - Agent Objective 3")
            world.set_rule(rescue_agent_obj_3, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                               | (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                               | (HasAll("A51 Rescue - Agent", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))
            
            rescue_agent_complete = world.get_location("Complete: A51 Rescue - Agent")
            world.set_rule(rescue_agent_complete, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Agent", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))


            # Stage 9 - Escape
            escape_agent_obj_1 = world.get_location("A51 Escape - Agent Objective 1")
            world.set_rule(escape_agent_obj_1, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)")
                                               | HasAll("A51 Escape - Agent", "Tranquilizer")
                                               | HasAll("A51 Escape - Agent", "SuperDragon"))

            escape_agent_obj_2 = world.get_location("A51 Escape - Agent Objective 2")
            world.set_rule(escape_agent_obj_2, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)")
                                               | HasAll("A51 Escape - Agent", "Tranquilizer")
                                               | HasAll("A51 Escape - Agent", "SuperDragon"))

            escape_agent_obj_3 = world.get_location("A51 Escape - Agent Objective 3")
            world.set_rule(escape_agent_obj_3, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                               | HasAll("A51 Escape - Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                               | HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))
            
            escape_agent_complete = world.get_location("Complete: A51 Escape - Agent")
            world.set_rule(escape_agent_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
            world.set_rule(air_base_agent_obj_1, HasAll("Air Base - Agent", "Stewardess Disguise"))

            air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
            world.set_rule(air_base_agent_obj_2, HasAll("Air Base - Agent", "Stewardess Disguise"))

            air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
            world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "Crossbow", "Dragon", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise")
                                                 | HasAll("Air Base - Agent", "CamSpy", "Dragon", "Stewardess Disguise"))
            
            air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
            world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "Crossbow", "Dragon", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "CamSpy", "Dragon", "Stewardess Disguise"))


            # Stage 11 - Air Force One
            air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
            world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

            air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
            world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Laptop Gun")
                                                      | HasAll("Air Force One - Agent", "Cyclone")
                                                      | HasAll("Air Force One - Agent", "K7 Avenger"))

            air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
            world.set_rule(air_force_one_agent_obj_3, HasAll("Air Force One - Agent", "Laptop Gun", "Timed Mine")
                                                      | HasAll("Air Force One - Agent", "Cyclone", "Timed Mine")
                                                      | HasAll("Air Force One - Agent", "K7 Avenger", "Timed Mine"))

            air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
            world.set_rule(air_force_one_agent_complete, HasAll("Air Force One - Agent", "Laptop Gun", "Timed Mine")
                                                         | HasAll("Air Force One - Agent", "Cyclone", "Timed Mine")
                                                         | HasAll("Air Force One - Agent", "K7 Avenger", "Timed Mine"))


            # Stage 12 - Crash Site
            crash_site_agent_obj_1 = world.get_location("Crash Site - Agent Objective 1")
            world.set_rule(crash_site_agent_obj_1, Has("Crash Site - Agent"))

            crash_site_agent_obj_2 = world.get_location("Crash Site - Agent Objective 2")
            world.set_rule(crash_site_agent_obj_2, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "President Scanner")
                                                   | HasAll("Crash Site - Agent", "K7 Avenger", "President Scanner")
                                                   | HasAll("Crash Site - Agent", "Sniper Rifle", "President Scanner"))

            crash_site_agent_obj_3 = world.get_location("Crash Site - Agent Objective 3")
            world.set_rule(crash_site_agent_obj_3, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                   | HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                   | HasAll("Crash Site - Agent", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_agent_complete = world.get_location("Complete: Crash Site - Agent")
            world.set_rule(crash_site_agent_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                      | HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Agent", "K7 Avenger", "Sniper Rifle", "President Scanner"))


            # Stage 13 - Pelagic II
            pelagic_agent_obj_1 = world.get_location("Pelagic II - Agent Objective 1")
            world.set_rule(pelagic_agent_obj_1, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "CMP150", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "Phoenix", "X-Ray Scanner"))

            pelagic_agent_obj_2 = world.get_location("Pelagic II - Agent Objective 2")
            world.set_rule(pelagic_agent_obj_2, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun")
                                                | HasAll("Pelagic II - Agent", "CMP150")
                                                | HasAll("Pelagic II - Agent", "Phoenix"))

            pelagic_agent_obj_3 = world.get_location("Pelagic II - Agent Objective 3")
            world.set_rule(pelagic_agent_obj_3, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                | HasAll("Pelagic II - Agent", "Laptop Gun", "CMP150", "X-Ray Scanner"))
            
            pelagic_agent_complete = world.get_location("Complete: Pelagic II - Agent")
            world.set_rule(pelagic_agent_complete, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Agent", "Laptop Gun", "CMP150", "X-Ray Scanner"))


            # Stage 14 - Deep Sea
            deep_sea_agent_obj_1 = world.get_location("Deep Sea - Agent Objective 1")
            world.set_rule(deep_sea_agent_obj_1, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "IR Scanner"))

            deep_sea_agent_obj_2 = world.get_location("Deep Sea - Agent Objective 2")
            world.set_rule(deep_sea_agent_obj_2, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_agent_obj_3 = world.get_location("Deep Sea - Agent Objective 3")
            world.set_rule(deep_sea_agent_obj_3, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                 | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_agent_complete = world.get_location("Complete: Deep Sea - Agent")
            world.set_rule(deep_sea_agent_complete, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                    | HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_agent_obj_1 = world.get_location("CI Defense - Agent Objective 1")
            world.set_rule(institute_defense_agent_obj_1, HasAll("CI Defense - Agent", "AR34")
                                                          | HasAll("CI Defense - Agent", "Mauler"))

            institute_defense_agent_obj_2 = world.get_location("CI Defense - Agent Objective 2")
            world.set_rule(institute_defense_agent_obj_2, HasAll("CI Defense - Agent", "AR34", "RC-P120")
                                                          | HasAll("CI Defense - Agent", "Mauler", "RC-P120"))

            institute_defense_agent_obj_3 = world.get_location("CI Defense - Agent Objective 3")
            world.set_rule(institute_defense_agent_obj_3, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink")
                                                          | HasAll("CI Defense - Agent", "Mauler", "RC-P120", "Data Uplink"))

            institute_defense_agent_complete = world.get_location("Complete: CI Defense - Agent")
            world.set_rule(institute_defense_agent_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Agent", "Mauler", "RC-P120", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_agent_obj_1 = world.get_location("Attack Ship - Agent Objective 1")
            world.set_rule(attack_ship_agent_obj_1, HasAll("Attack Ship - Agent", "Mauler"))

            attack_ship_agent_obj_2 = world.get_location("Attack Ship - Agent Objective 2")
            world.set_rule(attack_ship_agent_obj_2, HasAll("Attack Ship - Agent", "Mauler"))

            attack_ship_agent_obj_3 = world.get_location("Attack Ship - Agent Objective 3")
            world.set_rule(attack_ship_agent_obj_3, HasAll("Attack Ship - Agent", "Mauler"))

            attack_ship_agent_complete = world.get_location("Complete: Attack Ship - Agent")
            world.set_rule(attack_ship_agent_complete, HasAll("Attack Ship - Agent", "Mauler"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
            world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
            world.set_rule(skedar_ruins_agent_obj_2, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
            world.set_rule(skedar_ruins_agent_obj_3, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
            world.set_rule(skedar_ruins_agent_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Agent Objective 1")
            world.set_rule(mbr_agent_obj_1, HasAll("Mr. Blonde's Revenge - Agent", "Mauler"))

            mbr_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Agent")
            world.set_rule(mbr_agent_complete, HasAll("Mr. Blonde's Revenge - Agent", "Mauler"))


            # Stage 19 - Maian SOS
            maian_sos_agent_obj_1 = world.get_location("Maian SOS - Agent Objective 1")
            world.set_rule(maian_sos_agent_obj_1, HasAll("Maian SOS - Agent", "Falcon 2", "Dragon"))

            maian_sos_agent_complete = world.get_location("Complete: Maian SOS - Agent")
            world.set_rule(maian_sos_agent_complete, HasAll("Maian SOS - Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_agent_obj_1 = world.get_location("WAR! - Agent Objective 1")
            world.set_rule(war_agent_obj_1, HasAll("WAR! - Agent", "Phoenix")
                                            | HasAll("WAR! - Agent", "Callisto NTG")
                                            | HasAll("WAR! - Agent", "Mauler"))

            war_agent_complete = world.get_location("Complete: WAR! - Agent")
            world.set_rule(war_agent_complete, HasAll("WAR! - Agent", "Phoenix")
                                               | HasAll("WAR! - Agent", "Callisto NTG")
                                               | HasAll("WAR! - Agent", "Mauler"))


            # Stage 21 - The Duel
            duel_agent_obj_1 = world.get_location("The Duel - Agent Objective 1")
            world.set_rule(duel_agent_obj_1, Has("The Duel - Agent"))

            duel_agent_complete = world.get_location("Complete: The Duel - Agent")
            world.set_rule(duel_agent_complete, Has("The Duel - Agent"))


        if world.options.special_agent:
            # Stage 1 - Defection
            defection_sp_agent_obj_1 = world.get_location("dD Defection - Special Agent Objective 1")
            world.set_rule(defection_sp_agent_obj_1, HasAll("dD Defection - Special Agent", "ECM Mine"))

            defection_sp_agent_obj_2 = world.get_location("dD Defection - Special Agent Objective 2")
            world.set_rule(defection_sp_agent_obj_2, Has("dD Defection - Special Agent") & HAS_DD_KEYS)

            defection_sp_agent_obj_3 = world.get_location("dD Defection - Special Agent Objective 3")
            world.set_rule(defection_sp_agent_obj_3, HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)")
                                                     | HasAll("dD Defection - Special Agent", "ECM Mine", "CMP150"))

            defection_sp_agent_obj_4 = world.get_location("dD Defection - Special Agent Objective 4")
            world.set_rule(defection_sp_agent_obj_4, (HasAll("dD Defection - Special Agent", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Special Agent", "CMP150") & HAS_DD_KEYS))

            defection_sp_agent_complete = world.get_location("Complete: dD Defection - Special Agent")
            world.set_rule(defection_sp_agent_complete, (HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                        | (HasAll("dD Defection - Special Agent", "ECM Mine", "CMP150") & HAS_DD_KEYS))


            # Stage 2 - Investigation
            investigation_sp_agent_obj_1 = world.get_location("dD Investigation - Special Agent Objective 1")
            world.set_rule(investigation_sp_agent_obj_1, HasAll("dD Investigation - Special Agent", "CamSpy"))

            investigation_sp_agent_obj_2 = world.get_location("dD Investigation - Special Agent Objective 2")
            world.set_rule(investigation_sp_agent_obj_2, Has("dD Investigation - Special Agent"))

            investigation_sp_agent_obj_3 = world.get_location("dD Investigation - Special Agent Objective 3")
            world.set_rule(investigation_sp_agent_obj_3, HasAll("dD Investigation - Special Agent", "Falcon 2")
                                                         | HasAll("dD Investigation - Special Agent", "CMP150"))

            investigation_sp_agent_obj_4 = world.get_location("dD Investigation - Special Agent Objective 4")
            world.set_rule(investigation_sp_agent_obj_4, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "Data Uplink")
                                                         | HasAll("dD Investigation - Special Agent", "CamSpy", "CMP150", "Data Uplink"))

            investigation_sp_agent_complete = world.get_location("Complete: dD Investigation - Special Agent")
            world.set_rule(investigation_sp_agent_complete, HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "Data Uplink")
                                                            | HasAll("dD Investigation - Special Agent", "CamSpy", "CMP150", "Data Uplink"))


            # Stage 3 - Extraction
            extraction_sp_agent_obj_1 = world.get_location("dD Extraction - Special Agent Objective 1")
            world.set_rule(extraction_sp_agent_obj_1, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150"))

            extraction_sp_agent_obj_2 = world.get_location("dD Extraction - Special Agent Objective 2")
            world.set_rule(extraction_sp_agent_obj_2, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Rocket Launcher")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_sp_agent_obj_3 = world.get_location("dD Extraction - Special Agent Objective 3")
            world.set_rule(extraction_sp_agent_obj_3, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_sp_agent_obj_4 = world.get_location("dD Extraction - Special Agent Objective 4")
            world.set_rule(extraction_sp_agent_obj_4, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_sp_agent_complete = world.get_location("Complete: dD Extraction - Special Agent")
            world.set_rule(extraction_sp_agent_complete, HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                         | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                         | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun"))


            # Stage 4 - Villa
            villa_sp_agent_obj_1 = world.get_location("Carrington Villa - Special Agent Objective 1")
            world.set_rule(villa_sp_agent_obj_1, HasAll("Carrington Villa - Special Agent", "Sniper Rifle")
                                                 | HasAll("Carrington Villa - Special Agent", "CMP150"))

            villa_sp_agent_obj_2 = world.get_location("Carrington Villa - Special Agent Objective 2")
            world.set_rule(villa_sp_agent_obj_2, HasAll("Carrington Villa - Special Agent", "Sniper Rifle")
                                                 | HasAll("Carrington Villa - Special Agent", "CMP150"))

            villa_sp_agent_obj_3 = world.get_location("Carrington Villa - Special Agent Objective 3")
            world.set_rule(villa_sp_agent_obj_3, HasAll("Carrington Villa - Special Agent", "Sniper Rifle")
                                                 | HasAll("Carrington Villa - Special Agent", "CMP150"))

            villa_sp_agent_obj_4 = world.get_location("Carrington Villa - Special Agent Objective 4")
            world.set_rule(villa_sp_agent_obj_4, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Special Agent", "CMP150", "Cellar Key Card"))

            villa_sp_agent_complete = world.get_location("Complete: Carrington Villa - Special Agent")
            world.set_rule(villa_sp_agent_complete, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "Cellar Key Card")
                                                    | HasAll("Carrington Villa - Special Agent", "CMP150", "Cellar Key Card"))


            # Stage 5 - Chicago
            chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
            world.set_rule(chicago_sp_agent_obj_1, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink"))

            chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
            world.set_rule(chicago_sp_agent_obj_2, HasAll("Chicago - Special Agent", "Remote Mine", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "CMP150")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "DY357 Magnum"))

            chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
            world.set_rule(chicago_sp_agent_obj_3, HasAll("Chicago - Special Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "Data Uplink", "CMP150") 
                                                   | HasAll("Chicago - Special Agent", "Data Uplink", "DY357 Magnum")
                                                   | HasAll("Chicago - Special Agent", "CamSpy", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "CamSpy", "CMP150")
                                                   | HasAll("Chicago - Special Agent", "CamSpy", "DY357 Magnum"))

            chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
            world.set_rule(chicago_sp_agent_obj_4, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)") 
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "CMP150")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "DY357 Magnum"))
            
            chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
            world.set_rule(chicago_sp_agent_complete, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)") 
                                                      | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "CMP150")
                                                      | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "DY357 Magnum"))


            # Stage 6 - G5 Building
            g5_sp_agent_obj_1 = world.get_location("G5 Building - Special Agent Objective 1")
            world.set_rule(g5_sp_agent_obj_1, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150") & HAS_G5_KEYS))

            g5_sp_agent_obj_2 = world.get_location("G5 Building - Special Agent Objective 2")
            world.set_rule(g5_sp_agent_obj_2, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150", "CamSpy") & HAS_G5_KEYS))

            g5_sp_agent_obj_3 = world.get_location("G5 Building - Special Agent Objective 3")
            world.set_rule(g5_sp_agent_obj_3, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS))

            g5_sp_agent_obj_4 = world.get_location("G5 Building - Special Agent Objective 4")
            world.set_rule(g5_sp_agent_obj_4, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "Remote Mine") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150", "Remote Mine") & HAS_G5_KEYS))

            g5_sp_agent_complete = world.get_location("Complete: G5 Building - Special Agent")
            world.set_rule(g5_sp_agent_complete, (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                                 | (HasAll("G5 Building - Special Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS))


            # Stage 7 - Infiltration
            infiltration_sp_agent_obj_1 = world.get_location("A51 Infiltration - Special Agent Objective 1")
            world.set_rule(infiltration_sp_agent_obj_1, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Explosives")
                                                        | HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Explosives"))

            infiltration_sp_agent_obj_2 = world.get_location("A51 Infiltration - Special Agent Objective 2")
            world.set_rule(infiltration_sp_agent_obj_2, HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Comms Rider")
                                                        | HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Comms Rider"))

            infiltration_sp_agent_obj_3 = world.get_location("A51 Infiltration - Special Agent Objective 3")
            world.set_rule(infiltration_sp_agent_obj_3, (HasAll("A51 Infiltration - Special Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "MagSec 4") & HAS_A51_INFIL_KEYS))

            infiltration_sp_agent_obj_4 = world.get_location("A51 Infiltration - Special Agent Objective 4")
            world.set_rule(infiltration_sp_agent_obj_4, (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Dragon" "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))

            infiltration_sp_agent_complete = world.get_location("Complete: A51 Infiltration - Special Agent")
            world.set_rule(infiltration_sp_agent_complete, (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                           | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                           | (HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Dragon" "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))


            # Stage 8 - Rescue
            rescue_sp_agent_obj_1 = world.get_location("A51 Rescue - Special Agent Objective 1")
            world.set_rule(rescue_sp_agent_obj_1, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                  | HasAll("A51 Rescue - Special Agent", "Dragon", "X-Ray Scanner"))

            rescue_sp_agent_obj_2 = world.get_location("A51 Rescue - Special Agent Objective 2")
            world.set_rule(rescue_sp_agent_obj_2, HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes")
                                                  | HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes")
                                                  | HasAll("A51 Rescue - Special Agent", "Dragon", "SuperDragon", "Lab Clothes"))

            rescue_sp_agent_obj_3 = world.get_location("A51 Rescue - Special Agent Objective 3")
            world.set_rule(rescue_sp_agent_obj_3, (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                                  | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                                  | (HasAll("A51 Rescue - Special Agent", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY))

            rescue_sp_agent_obj_4 = world.get_location("A51 Rescue - Special Agent Objective 4")
            world.set_rule(rescue_sp_agent_obj_4, (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))
            
            rescue_sp_agent_complete = world.get_location("Complete: A51 Rescue - Special Agent")
            world.set_rule(rescue_sp_agent_complete, (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                     | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                     | (HasAll("A51 Rescue - Special Agent", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))


            # Stage 9 - Escape
            escape_sp_agent_obj_1 = world.get_location("A51 Escape - Special Agent Objective 1")
            world.set_rule(escape_sp_agent_obj_1, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)")
                                                  | HasAll("A51 Escape - Special Agent", "SuperDragon")
                                                  | HasAll("A51 Escape - Special Agent", "Tranquilizer"))

            escape_sp_agent_obj_2 = world.get_location("A51 Escape - Special Agent Objective 2")
            world.set_rule(escape_sp_agent_obj_2, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon")
                                                  | HasAll("A51 Escape - Special Agent", "Tranquilizer", "SuperDragon")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "Tranquilizer",))

            escape_sp_agent_obj_3 = world.get_location("A51 Escape - Special Agent Objective 3")
            world.set_rule(escape_sp_agent_obj_3, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))

            escape_sp_agent_obj_4 = world.get_location("A51 Escape - Special Agent Objective 4")
            world.set_rule(escape_sp_agent_obj_4, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))
            
            escape_sp_agent_complete = world.get_location("Complete: A51 Escape - Special Agent")
            world.set_rule(escape_sp_agent_complete, HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                     | HasAll("A51 Escape - Special Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                     | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
            world.set_rule(air_base_sp_agent_obj_1, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

            air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
            world.set_rule(air_base_sp_agent_obj_2, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

            air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
            world.set_rule(air_base_sp_agent_obj_3, HasAll("Air Base - Special Agent", "Crossbow", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

            air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
            world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase"))
            
            air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
            world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase")
                                                       | HasAll("Air Base - Special Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                       | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase"))


            # Stage 11 - Air Force One
            air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
            world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
            world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
            world.set_rule(air_force_one_sp_agent_obj_3, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "K7 Avenger") & HAS_AFO_LIFT_KEY))

            air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
            world.set_rule(air_force_one_sp_agent_obj_4, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))

            air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
            world.set_rule(air_force_one_sp_agent_complete, (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                            | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                            | (HasAll("Air Force One - Special Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))


            # Stage 12 - Crash Site
            crash_site_sp_agent_obj_1 = world.get_location("Crash Site - Special Agent Objective 1")
            world.set_rule(crash_site_sp_agent_obj_1, HasAll("Crash Site - Special Agent", "President Scanner"))

            crash_site_sp_agent_obj_2 = world.get_location("Crash Site - Special Agent Objective 2")
            world.set_rule(crash_site_sp_agent_obj_2, Has("Crash Site - Special Agent"))

            crash_site_sp_agent_obj_3 = world.get_location("Crash Site - Special Agent Objective 3")
            world.set_rule(crash_site_sp_agent_obj_3, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "K7 Avenger", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "Sniper Rifle", "President Scanner"))

            crash_site_sp_agent_obj_4 = world.get_location("Crash Site - Special Agent Objective 4")
            world.set_rule(crash_site_sp_agent_obj_4, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "K7 Avenger", "Sniper Rifle", "President Scanner"))
            
            crash_site_sp_agent_complete = world.get_location("Complete: Crash Site - Special Agent")
            world.set_rule(crash_site_sp_agent_complete, HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                         | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                         | HasAll("Crash Site - Special Agent", "K7 Avenger", "Sniper Rifle", "President Scanner"))


            # Stage 13 - Pelagic II
            pelagic_sp_agent_obj_1 = world.get_location("Pelagic II - Special Agent Objective 1")
            world.set_rule(pelagic_sp_agent_obj_1, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Phoenix", "X-Ray Scanner"))

            pelagic_sp_agent_obj_2 = world.get_location("Pelagic II - Special Agent Objective 2")
            world.set_rule(pelagic_sp_agent_obj_2, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun")
                                                   | HasAll("Pelagic II - Special Agent", "CMP150")
                                                   | HasAll("Pelagic II - Special Agent", "Phoenix"))

            pelagic_sp_agent_obj_3 = world.get_location("Pelagic II - Special Agent Objective 3")
            world.set_rule(pelagic_sp_agent_obj_3, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun")
                                                   | HasAll("Pelagic II - Special Agent", "CMP150"))

            pelagic_sp_agent_obj_4 = world.get_location("Pelagic II - Special Agent Objective 4")
            world.set_rule(pelagic_sp_agent_obj_4, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun", "CMP150", "X-Ray Scanner"))
            
            pelagic_sp_agent_complete = world.get_location("Complete: Pelagic II - Special Agent")
            world.set_rule(pelagic_sp_agent_complete, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                      | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                      | HasAll("Pelagic II - Special Agent", "Laptop Gun", "CMP150", "X-Ray Scanner"))


            # Stage 14 - Deep Sea
            deep_sea_sp_agent_obj_1 = world.get_location("Deep Sea - Special Agent Objective 1")
            world.set_rule(deep_sea_sp_agent_obj_1, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "IR Scanner"))

            deep_sea_sp_agent_obj_2 = world.get_location("Deep Sea - Special Agent Objective 2")
            world.set_rule(deep_sea_sp_agent_obj_2, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_sp_agent_obj_3 = world.get_location("Deep Sea - Special Agent Objective 3")
            world.set_rule(deep_sea_sp_agent_obj_3, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_sp_agent_obj_4 = world.get_location("Deep Sea - Special Agent Objective 4")
            world.set_rule(deep_sea_sp_agent_obj_4, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))
            
            deep_sea_sp_agent_complete = world.get_location("Complete: Deep Sea - Special Agent")
            world.set_rule(deep_sea_sp_agent_complete, HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                       | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                       | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_sp_agent_obj_1 = world.get_location("CI Defense - Special Agent Objective 1")
            world.set_rule(institute_defense_sp_agent_obj_1, Has("CI Defense - Special Agent"))

            institute_defense_sp_agent_obj_2 = world.get_location("CI Defense - Special Agent Objective 2")
            world.set_rule(institute_defense_sp_agent_obj_2, HasAll("CI Defense - Special Agent", "AR34")
                                                             | HasAll("CI Defense - Special Agent", "Mauler"))

            institute_defense_sp_agent_obj_3 = world.get_location("CI Defense - Special Agent Objective 3")
            world.set_rule(institute_defense_sp_agent_obj_3, HasAll("CI Defense - Special Agent", "AR34", "RC-P120")
                                                             | HasAll("CI Defense - Special Agent", "Mauler", "RC-P120"))

            institute_defense_sp_agent_obj_4 = world.get_location("CI Defense - Special Agent Objective 4")
            world.set_rule(institute_defense_sp_agent_obj_4, HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Special Agent", "Mauler", "RC-P120", "Data Uplink"))

            institute_defense_sp_agent_complete = world.get_location("Complete: CI Defense - Special Agent")
            world.set_rule(institute_defense_sp_agent_complete, HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink")
                                                                | HasAll("CI Defense - Special Agent", "Mauler", "RC-P120", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_sp_agent_obj_1 = world.get_location("Attack Ship - Special Agent Objective 1")
            world.set_rule(attack_ship_sp_agent_obj_1, HasAll("Attack Ship - Special Agent", "Mauler"))

            attack_ship_sp_agent_obj_2 = world.get_location("Attack Ship - Special Agent Objective 2")
            world.set_rule(attack_ship_sp_agent_obj_2, HasAll("Attack Ship - Special Agent", "Mauler"))

            attack_ship_sp_agent_obj_3 = world.get_location("Attack Ship - Special Agent Objective 3")
            world.set_rule(attack_ship_sp_agent_obj_3, HasAll("Attack Ship - Special Agent", "Mauler"))

            attack_ship_sp_agent_obj_4 = world.get_location("Attack Ship - Special Agent Objective 4")
            world.set_rule(attack_ship_sp_agent_obj_4, HasAll("Attack Ship - Special Agent", "Mauler"))

            attack_ship_sp_agent_complete = world.get_location("Complete: Attack Ship - Special Agent")
            world.set_rule(attack_ship_sp_agent_complete, HasAll("Attack Ship - Special Agent", "Mauler"))


            # Stage 17 - Skedar Ruins
            skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
            world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
            world.set_rule(skedar_ruins_sp_agent_obj_2, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
            world.set_rule(skedar_ruins_sp_agent_obj_3, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
            world.set_rule(skedar_ruins_sp_agent_obj_4, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
            world.set_rule(skedar_ruins_sp_agent_complete, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_sp_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 1")
            world.set_rule(mbr_sp_agent_obj_1, HasAll("Mr. Blonde's Revenge - Special Agent", "Cloaking Device", "Skedar Bomb")
                                               | HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler", "Skedar Bomb"))

            mbr_sp_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 2")
            world.set_rule(mbr_sp_agent_obj_2, HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler"))

            mbr_sp_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Special Agent")
            world.set_rule(mbr_sp_agent_complete, HasAll("Mr. Blonde's Revenge - Special Agent", "Mauler", "Skedar Bomb"))


            # Stage 19 - Maian SOS
            maian_sos_sp_agent_obj_1 = world.get_location("Maian SOS - Special Agent Objective 1")
            world.set_rule(maian_sos_sp_agent_obj_1, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))

            maian_sos_sp_agent_obj_2 = world.get_location("Maian SOS - Special Agent Objective 2")
            world.set_rule(maian_sos_sp_agent_obj_2, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))

            maian_sos_sp_agent_complete = world.get_location("Complete: Maian SOS - Special Agent")
            world.set_rule(maian_sos_sp_agent_complete, HasAll("Maian SOS - Special Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_sp_agent_obj_1 = world.get_location("WAR! - Special Agent Objective 1")
            world.set_rule(war_sp_agent_obj_1, HasAll("WAR! - Special Agent", "Phoenix")
                                               | HasAll("WAR! - Special Agent", "Callisto NTG")
                                               | HasAll("WAR! - Special Agent", "Mauler"))

            war_sp_agent_obj_2 = world.get_location("WAR! - Special Agent Objective 2")
            world.set_rule(war_sp_agent_obj_2, HasAll("WAR! - Special Agent", "Phoenix")
                                               | HasAll("WAR! - Special Agent", "Callisto NTG")
                                               | HasAll("WAR! - Special Agent", "Mauler"))

            war_sp_agent_complete = world.get_location("Complete: WAR! - Special Agent")
            world.set_rule(war_sp_agent_complete, HasAll("WAR! - Special Agent", "Phoenix")
                                                  | HasAll("WAR! - Special Agent", "Callisto NTG")
                                                  | HasAll("WAR! - Special Agent", "Mauler"))


            # Stage 21 - The Duel
            duel_sp_agent_obj_1 = world.get_location("The Duel - Special Agent Objective 1")
            world.set_rule(duel_sp_agent_obj_1, Has("The Duel - Special Agent"))

            duel_sp_agent_obj_2 = world.get_location("The Duel - Special Agent Objective 2")
            world.set_rule(duel_sp_agent_obj_2, Has("The Duel - Special Agent"))

            duel_sp_agent_complete = world.get_location("Complete: The Duel - Special Agent")
            world.set_rule(duel_sp_agent_complete, Has("The Duel - Special Agent"))


        if world.options.perfect_agent:
            # Stage 1 - Defection
            defection_prf_agent_obj_1 = world.get_location("dD Defection - Perfect Agent Objective 1")
            world.set_rule(defection_prf_agent_obj_1, HasAll("dD Defection - Perfect Agent", "ECM Mine"))

            defection_prf_agent_obj_2 = world.get_location("dD Defection - Perfect Agent Objective 2")
            world.set_rule(defection_prf_agent_obj_2, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS)

            defection_prf_agent_obj_3 = world.get_location("dD Defection - Perfect Agent Objective 3")
            world.set_rule(defection_prf_agent_obj_3, HasAll("dD Defection - Perfect Agent", "Data Uplink", "Falcon 2 (Silencer)")
                                                      | HasAll("dD Defection - Perfect Agent", "Data Uplink", "CMP150"))

            defection_prf_agent_obj_4 = world.get_location("dD Defection - Perfect Agent Objective 4")
            world.set_rule(defection_prf_agent_obj_4, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Falcon 2 (Silencer)")
                                                      | HasAll("dD Defection - Perfect Agent", "ECM Mine", "CMP150"))

            defection_prf_agent_obj_5 = world.get_location("dD Defection - Perfect Agent Objective 5")
            world.set_rule(defection_prf_agent_obj_5, (HasAll("dD Defection - Perfect Agent", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                      | (HasAll("dD Defection - Perfect Agent", "CMP150") & HAS_DD_KEYS))

            defection_prf_agent_complete = world.get_location("Complete: dD Defection - Perfect Agent")
            world.set_rule(defection_prf_agent_complete, (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                         | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "CMP150") & HAS_DD_KEYS))


            # Stage 2 - Investigation
            investigation_prf_agent_obj_1 = world.get_location("dD Investigation - Perfect Agent Objective 1")
            world.set_rule(investigation_prf_agent_obj_1, HasAll("dD Investigation - Perfect Agent", "CamSpy"))

            investigation_prf_agent_obj_2 = world.get_location("dD Investigation - Perfect Agent Objective 2")
            world.set_rule(investigation_prf_agent_obj_2, Has("dD Investigation - Perfect Agent"))

            investigation_prf_agent_obj_3 = world.get_location("dD Investigation - Perfect Agent Objective 3")
            world.set_rule(investigation_prf_agent_obj_3, HasAll("dD Investigation - Perfect Agent", "Falcon 2")
                                                          | HasAll("dD Investigation - Perfect Agent", "CMP150"))

            investigation_prf_agent_obj_4 = world.get_location("dD Investigation - Perfect Agent Objective 4")
            world.set_rule(investigation_prf_agent_obj_4, HasAll("dD Investigation - Perfect Agent", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                          | HasAll("dD Investigation - Perfect Agent", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))

            investigation_prf_agent_obj_5 = world.get_location("dD Investigation - Perfect Agent Objective 5")
            world.set_rule(investigation_prf_agent_obj_5, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                          | HasAll("dD Investigation - Perfect Agent", "CamSpy", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))

            investigation_prf_agent_complete = world.get_location("Complete: dD Investigation - Perfect Agent")
            world.set_rule(investigation_prf_agent_complete, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                             | HasAll("dD Investigation - Perfect Agent", "CamSpy", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))
            

            # Stage 3 - Extraction
            extraction_prf_agent_obj_1 = world.get_location("dD Extraction - Perfect Agent Objective 1")
            world.set_rule(extraction_prf_agent_obj_1, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150"))

            extraction_prf_agent_obj_2 = world.get_location("dD Extraction - Perfect Agent Objective 2")
            world.set_rule(extraction_prf_agent_obj_2, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150"))

            extraction_prf_agent_obj_3 = world.get_location("dD Extraction - Perfect Agent Objective 3")
            world.set_rule(extraction_prf_agent_obj_3, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Rocket Launcher")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Rocket Launcher")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_prf_agent_obj_4 = world.get_location("dD Extraction - Perfect Agent Objective 4")
            world.set_rule(extraction_prf_agent_obj_4, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_prf_agent_obj_5 = world.get_location("dD Extraction - Perfect Agent Objective 5")
            world.set_rule(extraction_prf_agent_obj_5, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                       | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))

            extraction_prf_agent_complete = world.get_location("Complete: dD Extraction - Perfect Agent")
            world.set_rule(extraction_prf_agent_complete, HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                          | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                          | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))


            # Stage 4 - Villa
            villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
            world.set_rule(villa_prf_agent_obj_1, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun")
                                                  | HasAll("Carrington Villa - Perfect Agent", "CMP150")
                                                  | HasAll("Carrington Villa - Perfect Agent", "Sniper Rifle"))

            villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
            world.set_rule(villa_prf_agent_obj_2, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun")
                                                  | HasAll("Carrington Villa - Perfect Agent", "CMP150")
                                                  | HasAll("Carrington Villa - Perfect Agent", "Sniper Rifle"))

            villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
            world.set_rule(villa_prf_agent_obj_3, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150")
                                                  | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle")
                                                  | HasAll("Carrington Villa - Perfect Agent", "CMP150", "Sniper Rifle"))

            villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
            world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

            villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
            world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card")
                                                  | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card")
                                                  | HasAll("Carrington Villa - Perfect Agent", "CMP150", "Sniper Rifle", "Cellar Key Card"))

            villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
            world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card")
                                                     | HasAll("Carrington Villa - Perfect Agent", "CMP150", "Sniper Rifle", "Cellar Key Card"))


            # Stage 5 - Chicago
            chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
            world.set_rule(chicago_prf_agent_obj_1, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink"))

            chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
            world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug"))

            chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
            world.set_rule(chicago_prf_agent_obj_3, HasAll("Chicago - Perfect Agent", "Remote Mine", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "Remote Mine", "CMP150")
                                                    | HasAll("Chicago - Perfect Agent", "Remote Mine", "DY357 Magnum"))

            chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
            world.set_rule(chicago_prf_agent_obj_4, HasAll("Chicago - Perfect Agent", "Data Uplink", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "Data Uplink", "CMP150")
                                                    | HasAll("Chicago - Perfect Agent", "Data Uplink", "DY357 Magnum")
                                                    | HasAll("Chicago - Perfect Agent", "CamSpy", "Falcon 2 (Scope)")
                                                    | HasAll("Chicago - Perfect Agent", "CamSpy", "CMP150")
                                                    | HasAll("Chicago - Perfect Agent", "CamSpy", "DY357 Magnum"))

            chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
            world.set_rule(chicago_prf_agent_obj_5, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)") 
                                                    | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "CMP150")
                                                    | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "DY357 Magnum"))
            
            chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
            world.set_rule(chicago_prf_agent_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)")
                                                       | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "CMP150")
                                                       | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "DY357 Magnum"))


            # Stage 6 - G5 Building
            g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
            world.set_rule(g5_prf_agent_obj_1, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150") & HAS_G5_KEYS))

            g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
            world.set_rule(g5_prf_agent_obj_2, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150") & HAS_G5_KEYS))

            g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
            world.set_rule(g5_prf_agent_obj_3, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CamSpy") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150", "CamSpy") & HAS_G5_KEYS))

            g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
            world.set_rule(g5_prf_agent_obj_4, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150", "Door Decoder", "Backup Disk") & HAS_G5_KEYS))

            g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
            world.set_rule(g5_prf_agent_obj_5, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "Remote Mine") & HAS_G5_KEYS)
                                               | (HasAll("G5 Building - Perfect Agent", "CMP150", "Remote Mine") & HAS_G5_KEYS))

            g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
            world.set_rule(g5_prf_agent_complete, (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                                  | (HasAll("G5 Building - Perfect Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS))


            # Stage 7 - Infiltration
            infiltration_prf_agent_obj_1 = world.get_location("A51 Infiltration - Perfect Agent Objective 1")
            world.set_rule(infiltration_prf_agent_obj_1, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Explosives")
                                                         | HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Explosives"))

            infiltration_prf_agent_obj_2 = world.get_location("A51 Infiltration - Perfect Agent Objective 2")
            world.set_rule(infiltration_prf_agent_obj_2, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Comms Rider")
                                                         | HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Comms Rider"))

            infiltration_prf_agent_obj_3 = world.get_location("A51 Infiltration - Perfect Agent Objective 3")
            world.set_rule(infiltration_prf_agent_obj_3, HasAll("A51 Infiltration - Perfect Agent", "Falcon 2")
                                                         | HasAll("A51 Infiltration - Perfect Agent", "MagSec 4"))

            infiltration_prf_agent_obj_4 = world.get_location("A51 Infiltration - Perfect Agent Objective 4")
            world.set_rule(infiltration_prf_agent_obj_4, (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2") & HAS_A51_INFIL_KEYS)
                                                         | (HasAll("A51 Infiltration - Perfect Agent", "MagSec 4") & HAS_A51_INFIL_KEYS))

            infiltration_prf_agent_obj_5 = world.get_location("A51 Infiltration - Perfect Agent Objective 5")
            world.set_rule(infiltration_prf_agent_obj_5, (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                         | (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                         | (HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))

            infiltration_prf_agent_complete = world.get_location("Complete: A51 Infiltration - Perfect Agent")
            world.set_rule(infiltration_prf_agent_complete, (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                            | (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                            | (HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))            


            # Stage 8 - Rescue
            rescue_prf_agent_obj_1 = world.get_location("A51 Rescue - Perfect Agent Objective 1")
            world.set_rule(rescue_prf_agent_obj_1, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Data Uplink")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Dragon", "Data Uplink"))

            rescue_prf_agent_obj_2 = world.get_location("A51 Rescue - Perfect Agent Objective 2")
            world.set_rule(rescue_prf_agent_obj_2, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Dragon", "X-Ray Scanner"))

            rescue_prf_agent_obj_3 = world.get_location("A51 Rescue - Perfect Agent Objective 3")
            world.set_rule(rescue_prf_agent_obj_3, HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes")
                                                   | HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Lab Clothes"))

            rescue_prf_agent_obj_4 = world.get_location("A51 Rescue - Perfect Agent Objective 4")
            world.set_rule(rescue_prf_agent_obj_4, (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                                   | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY)
                                                   | (HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY))

            rescue_prf_agent_obj_5 = world.get_location("A51 Rescue - Perfect Agent Objective 5")
            world.set_rule(rescue_prf_agent_obj_5, (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                   | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                   | (HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))
            
            rescue_prf_agent_complete = world.get_location("Complete: A51 Rescue - Perfect Agent")
            world.set_rule(rescue_prf_agent_complete, (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                      | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                      | (HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))
            

            # Stage 9 - Escape
            escape_prf_agent_obj_1 = world.get_location("A51 Escape - Perfect Agent Objective 1")
            world.set_rule(escape_prf_agent_obj_1, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "SuperDragon", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "Tranquilizer", "Alien Medpack"))

            escape_prf_agent_obj_2 = world.get_location("A51 Escape - Perfect Agent Objective 2")
            world.set_rule(escape_prf_agent_obj_2, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)")
                                                   | HasAll("A51 Escape - Perfect Agent", "SuperDragon")
                                                   | HasAll("A51 Escape - Perfect Agent", "Tranquilizer"))

            escape_prf_agent_obj_3 = world.get_location("A51 Escape - Perfect Agent Objective 3")
            world.set_rule(escape_prf_agent_obj_3, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon")
                                                   | HasAll("A51 Escape - Perfect Agent", "Tranquilizer", "SuperDragon")
                                                   | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Tranquilizer"))

            escape_prf_agent_obj_4 = world.get_location("A51 Escape - Perfect Agent Objective 4")
            world.set_rule(escape_prf_agent_obj_4, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))

            escape_prf_agent_obj_5 = world.get_location("A51 Escape - Perfect Agent Objective 5")
            world.set_rule(escape_prf_agent_obj_5, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                   | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))
            
            escape_prf_agent_complete = world.get_location("Complete: A51 Escape - Perfect Agent")
            world.set_rule(escape_prf_agent_complete, HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                      | HasAll("A51 Escape - Perfect Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                      | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))


            # Stage 10 - Air Base
            air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
            world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

            air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
            world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise", "Suitcase")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

            air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
            world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

            air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
            world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "Crossbow", "Proximity Mine", "Stewardess Disguise", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Proximity Mine", "Stewardess Disguise", "Flight Plans"))

            air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
            world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                     | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"))
            
            air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
            world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                        | HasAll("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                        | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"))


            # Stage 11 - Air Force One
            air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
            world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
            world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
            world.set_rule(air_force_one_prf_agent_obj_3, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "K7 Avenger") & HAS_AFO_LIFT_KEY))

            air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
            world.set_rule(air_force_one_prf_agent_obj_4, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))

            air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
            world.set_rule(air_force_one_prf_agent_obj_5, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))

            air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
            world.set_rule(air_force_one_prf_agent_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))


            # Stage 12 - Crash Site
            crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
            world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "President Scanner"))

            crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
            world.set_rule(crash_site_prf_agent_obj_2, Has("Crash Site - Perfect Agent"))
    
            crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
            world.set_rule(crash_site_prf_agent_obj_3, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Remote Mine")
                                                       | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "Remote Mine")
                                                       | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "Remote Mine")
                                                       | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "DY357-LX")
                                                       | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "DY357-LX")
                                                       | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "President Scanner", "DY357-LX"))

            crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
            world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "President Scanner")
                                                       | HasAll("Crash Site - Perfect Agent", "K7 Avenger", "President Scanner")
                                                       | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "President Scanner"))

            crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
            world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                       | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                       | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "President Scanner"))
            
            crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
            world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "Remote Mine")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "Remote Mine")
                                                          | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "President Scanner", "Remote Mine")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "DY357-LX")
                                                          | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "DY357-LX")
                                                          | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "President Scanner", "DY357-LX"))


            # Stage 13 - Pelagic II
            pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
            world.set_rule(pelagic_prf_agent_obj_1, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "X-Ray Scanner")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150", "X-Ray Scanner")
                                                    | HasAll("Pelagic II - Perfect Agent", "Phoenix", "X-Ray Scanner"))

            pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
            world.set_rule(pelagic_prf_agent_obj_2, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "Phoenix", "Research Tape"))

            pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
            world.set_rule(pelagic_prf_agent_obj_3, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150")
                                                    | HasAll("Pelagic II - Perfect Agent", "Phoenix"))

            pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
            world.set_rule(pelagic_prf_agent_obj_4, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun")
                                                    | HasAll("Pelagic II - Perfect Agent", "CMP150")
                                                    | HasAll("Pelagic II - Perfect Agent", "Phoenix"))

            pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
            world.set_rule(pelagic_prf_agent_obj_5, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner", "Research Tape")
                                                    | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))
            
            pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
            world.set_rule(pelagic_prf_agent_complete, HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner", "Research Tape")
                                                       | HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner", "Research Tape")
                                                       | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))


            # Stage 14 - Deep Sea
            deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
            world.set_rule(deep_sea_prf_agent_obj_1, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner"))

            deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
            world.set_rule(deep_sea_prf_agent_obj_2, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
            world.set_rule(deep_sea_prf_agent_obj_3, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner"))

            deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
            world.set_rule(deep_sea_prf_agent_obj_4, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))

            deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
            world.set_rule(deep_sea_prf_agent_obj_5, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                     | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))
            
            deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
            world.set_rule(deep_sea_prf_agent_complete, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                        | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))


            # Stage 15 - Carrington Institute Defense
            institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
            world.set_rule(institute_defense_prf_agent_obj_1, Has("CI Defense - Perfect Agent"))

            institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
            world.set_rule(institute_defense_prf_agent_obj_2, HasAll("CI Defense - Perfect Agent", "AR34"))

            institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
            world.set_rule(institute_defense_prf_agent_obj_3, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120"))

            institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
            world.set_rule(institute_defense_prf_agent_obj_4, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser")
                                                              | HasAll("CI Defense - Perfect Agent", "AR34", "Devastator"))

            institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
            world.set_rule(institute_defense_prf_agent_obj_5, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                              | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))

            institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
            world.set_rule(institute_defense_prf_agent_complete, HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                                 | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))


            # Stage 16 - Attack Ship
            attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
            world.set_rule(attack_ship_prf_agent_obj_1, HasAll("Attack Ship - Perfect Agent", "Mauler"))

            attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
            world.set_rule(attack_ship_prf_agent_obj_2, HasAll("Attack Ship - Perfect Agent", "Mauler"))

            attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
            world.set_rule(attack_ship_prf_agent_obj_3, HasAll("Attack Ship - Perfect Agent", "Mauler"))

            attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
            world.set_rule(attack_ship_prf_agent_obj_4, HasAll("Attack Ship - Perfect Agent", "Mauler"))

            attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
            world.set_rule(attack_ship_prf_agent_obj_5, HasAll("Attack Ship - Perfect Agent", "Mauler"))

            attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
            world.set_rule(attack_ship_prf_agent_complete, HasAll("Attack Ship - Perfect Agent", "Mauler"))      


            # Stage 17 - Skedar Ruins
            skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
            world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"))

            skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
            world.set_rule(skedar_ruins_prf_agent_obj_2, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator"))

            skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
            world.set_rule(skedar_ruins_prf_agent_obj_3, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
            world.set_rule(skedar_ruins_prf_agent_obj_4, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
            world.set_rule(skedar_ruins_prf_agent_obj_5, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"))

            skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
            world.set_rule(skedar_ruins_prf_agent_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            world.set_rule(mbr_prf_agent_obj_1, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Skedar Bomb")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150", "Skedar Bomb"))

            mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            world.set_rule(mbr_prf_agent_obj_2, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CamSpy", "Cloaking Device"))

            mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            world.set_rule(mbr_prf_agent_obj_3, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler")
                                                | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150"))

            mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
            world.set_rule(mbr_prf_agent_complete, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Skedar Bomb")
                                                   | HasAll("Mr. Blonde's Revenge - Perfect Agent", "CMP150", "Skedar Bomb"))


            # Stage 19 - Maian SOS
            maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
            world.set_rule(maian_sos_prf_agent_obj_1, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
            world.set_rule(maian_sos_prf_agent_obj_2, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
            world.set_rule(maian_sos_prf_agent_obj_3, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))

            maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
            world.set_rule(maian_sos_prf_agent_complete, HasAll("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"))


            # Stage 20 - WAR!
            war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
            world.set_rule(war_prf_agent_obj_1, HasAll("WAR! - Perfect Agent", "Phoenix")
                                                | HasAll("WAR! - Perfect Agent", "Callisto NTG")
                                                | HasAll("WAR! - Perfect Agent", "Mauler"))

            war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
            world.set_rule(war_prf_agent_obj_2, HasAll("WAR! - Perfect Agent", "Phoenix")
                                                | HasAll("WAR! - Perfect Agent", "Callisto NTG")
                                                | HasAll("WAR! - Perfect Agent", "Mauler"))

            war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
            world.set_rule(war_prf_agent_obj_3, HasAll("WAR! - Perfect Agent", "Phoenix")
                                                | HasAll("WAR! - Perfect Agent", "Callisto NTG")
                                                | HasAll("WAR! - Perfect Agent", "Mauler"))

            war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
            world.set_rule(war_prf_agent_complete, HasAll("WAR! - Perfect Agent", "Phoenix")
                                                   | HasAll("WAR! - Perfect Agent", "Callisto NTG")
                                                   | HasAll("WAR! - Perfect Agent", "Mauler"))


            # Stage 21 - The Duel
            duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
            world.set_rule(duel_prf_agent_obj_1, Has("The Duel - Perfect Agent"))

            duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
            world.set_rule(duel_prf_agent_obj_2, Has("The Duel - Perfect Agent"))

            duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
            world.set_rule(duel_prf_agent_obj_3, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)")
                                                 | HasAll("The Duel - Perfect Agent", "DY357 Magnum"))
            
            duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
            world.set_rule(duel_prf_agent_complete, HasAll("The Duel - Perfect Agent", "Falcon 2 (Scope)")
                                                    | HasAll("The Duel - Perfect Agent", "DY357 Magnum"))


        if world.options.unlock_cheats:
            # Defection
            cheat_defection_complete = world.get_location("Cheat Unlock: Complete dD Defection")
            world.set_rule(cheat_defection_complete, Has("dD Defection - Agent")
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine", "CMP150") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink", "CMP150") & HAS_DD_KEYS))


            # Investigation
            cheat_investigation_complete = world.get_location("Cheat Unlock: Complete dD Investigation")
            world.set_rule(cheat_investigation_complete, HasAll("dD Investigation - Agent", "CamSpy", "Falcon 2", "Data Uplink")
                                                         | HasAll("dD Investigation - Agent", "CamSpy", "CMP150", "Data Uplink")
                                                         | HasAll("dD Investigation - Special Agent", "CamSpy", "Falcon 2", "Data Uplink")
                                                         | HasAll("dD Investigation - Special Agent", "CamSpy", "CMP150", "Data Uplink")
                                                         | HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                         | HasAll("dD Investigation - Perfect Agent", "CamSpy", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


            # Extraction
            cheat_extraction_complete = world.get_location("Cheat Unlock: Complete dD Extraction")
            world.set_rule(cheat_extraction_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Special Agent", "Night Vision", "CMP150", "Shotgun")
                                                      | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                      | HasAll("dD Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                      | HasAll("dD Extraction - Perfect Agent", "Night Vision", "CMP150", "Shotgun"))


            # Villa
            cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
            world.set_rule(cheat_villa_complete, HasAll("Carrington Villa - Agent", "Sniper Rifle", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Agent", "CMP150", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Special Agent", "CMP150", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card")
                                                 | HasAll("Carrington Villa - Perfect Agent", "CMP150", "Sniper Rifle", "Cellar Key Card"))


            # Chicago
            cheat_chicago_complete = world.get_location("Cheat Unlock: Complete Chicago")
            world.set_rule(cheat_chicago_complete, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "CMP150")
                                                   | HasAll("Chicago - Agent", "Remote Mine", "Data Uplink", "DY357 Magnum")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "CMP150")
                                                   | HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink", "DY357 Magnum")
                                                   | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)")
                                                   | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "CMP150")
                                                   | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "DY357 Magnum"))


            # G5 Building
            cheat_g5_complete = world.get_location("Cheat Unlock: Complete G5 Building")
            world.set_rule(cheat_g5_complete, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Special Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Perfect Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS)
                                              | (HasAll("G5 Building - Perfect Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS))


            # Infiltration
            cheat_infiltration_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration")
            world.set_rule(cheat_infiltration_complete, (HasAll("A51 Infiltration - Agent", "Falcon 2", "MagSec 4", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Agent", "Falcon 2", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Agent", "MagSec 4", "Dragon", "Explosives") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Dragon" "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "MagSec 4", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))


            # Rescue
            cheat_rescue_complete = world.get_location("Cheat Unlock: Complete A51 Rescue")
            world.set_rule(cheat_rescue_complete, (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Agent", "Dragon", "SuperDragon", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "Dragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Falcon 2 (Silencer)", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Special Agent", "Dragon", "SuperDragon", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))


            # Escape
            cheat_escape_complete = world.get_location("Cheat Unlock: Complete A51 Escape")
            world.set_rule(cheat_escape_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Special Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack")
                                                  | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Perfect Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                  | HasAll("A51 Escape - Perfect Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))


            # Air Base
            cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
            world.set_rule(cheat_air_base_complete, HasAll("Air Base - Agent", "Crossbow", "Dragon", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise")
                                                    | HasAll("Air Base - Agent", "CamSpy", "Dragon", "Stewardess Disguise")
                                                    | HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase")
                                                    | HasAll("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                    | HasAll("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                    | HasAll("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"))


            # Air Force One
            cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
            world.set_rule(cheat_air_force_one_complete, HasAll("Air Force One - Agent", "Laptop Gun", "Timed Mine")
                                                         | HasAll("Air Force One - Agent", "Cyclone", "Timed Mine")
                                                         | HasAll("Air Force One - Agent", "K7 Avenger", "Timed Mine")
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))


            # Crash Site
            cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
            world.set_rule(cheat_crash_site_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                      | HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Agent", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Special Agent", "K7 Avenger", "Sniper Rifle", "President Scanner")
                                                      | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "Remote Mine")
                                                      | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "Remote Mine")
                                                      | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "President Scanner", "Remote Mine")
                                                      | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "DY357-LX")
                                                      | HasAll("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "DY357-LX")
                                                      | HasAll("Crash Site - Perfect Agent", "Sniper Rifle", "K7 Avenger", "President Scanner", "DY357-LX"))


            # Pelagic II
            cheat_pelagic_complete = world.get_location("Cheat Unlock: Complete Pelagic II")
            world.set_rule(cheat_pelagic_complete, HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Agent", "Laptop Gun", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Special Agent", "Laptop Gun", "CMP150", "X-Ray Scanner")
                                                   | HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner", "Research Tape")
                                                   | HasAll("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner", "Research Tape")
                                                   | HasAll("Pelagic II - Perfect Agent", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"))


            # Deep Sea
            cheat_deep_sea_complete = world.get_location("Cheat Unlock: Complete Deep Sea")
            world.set_rule(cheat_deep_sea_complete, HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                    | HasAll("Deep Sea - Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Agent", "Shotgun", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Special Agent", "Shotgun", "FarSight XR-20", "IR Scanner")
                                                    | HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                    | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))


            # CI Defense
            cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
            world.set_rule(cheat_institute_defense_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Agent", "Mauler", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Special Agent", "AR34", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Special Agent", "Mauler", "RC-P120", "Data Uplink")
                                                             | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink")
                                                             | HasAll("CI Defense - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"))


            # Attack Ship
            cheat_attack_ship_complete = world.get_location("Cheat Unlock: Complete Attack Ship")
            world.set_rule(cheat_attack_ship_complete, HasAll("Attack Ship - Agent", "Mauler")
                                                       | HasAll("Attack Ship - Special Agent", "Mauler")
                                                       | HasAll("Attack Ship - Perfect Agent", "Mauler"))


            # Skedar Ruins
            cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
            world.set_rule(cheat_skedar_ruins_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                        | HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                        | HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))

            
            if world.options.agent:
                # Extraction
                cheat_extraction_timed_complete = world.get_location("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
                world.set_rule(cheat_extraction_timed_complete, HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150")
                                                                | HasAll("dD Extraction - Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun")
                                                                | HasAll("dD Extraction - Agent", "Night Vision", "CMP150", "Shotgun"))


                # G5 Building
                cheat_g5_timed_complete = world.get_location("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
                world.set_rule(cheat_g5_timed_complete, (HasAll("G5 Building - Agent", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS)
                                                        | (HasAll("G5 Building - Agent", "CMP150", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS))


                # Escape
                cheat_escape_timed_complete = world.get_location("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
                world.set_rule(cheat_escape_timed_complete, HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack")
                                                            | HasAll("A51 Escape - Agent", "Tranquilizer", "SuperDragon", "Alien Medpack")
                                                            | HasAll("A51 Escape - Agent", "Falcon 2 (Scope)", "Tranquilizer", "Alien Medpack"))


                # Crash Site
                cheat_crash_site_timed_complete = world.get_location("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
                world.set_rule(cheat_crash_site_timed_complete, HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner")
                                                                | HasAll("Crash Site - Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner")
                                                                | HasAll("Crash Site - Agent", "K7 Avenger", "Sniper Rifle", "President Scanner"))


                # CI Defense
                cheat_institute_defense_timed_complete = world.get_location("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")
                world.set_rule(cheat_institute_defense_timed_complete, HasAll("CI Defense - Agent", "AR34", "RC-P120", "Data Uplink"))


            if world.options.special_agent:
                # Defection
                cheat_defection_timed_complete = world.get_location("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
                world.set_rule(cheat_defection_timed_complete, (HasAll("dD Defection - Special Agent", "ECM Mine", "Falcon 2 (Silencer)") & HAS_DD_KEYS)
                                                               | (HasAll("dD Defection - Special Agent", "ECM Mine", "CMP150") & HAS_DD_KEYS))


                # Villa
                cheat_villa_timed_complete = world.get_location("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
                world.set_rule(cheat_villa_timed_complete, HasAll("Carrington Villa - Special Agent", "Sniper Rifle", "Cellar Key Card")
                                                           | HasAll("Carrington Villa - Special Agent", "CMP150", "Cellar Key Card"))


                # Infiltration
                cheat_infiltration_timed_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
                world.set_rule(cheat_infiltration_timed_complete, (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                                  | (HasAll("A51 Infiltration - Special Agent", "Falcon 2", "Dragon", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS)
                                                                  | (HasAll("A51 Infiltration - Special Agent", "MagSec 4", "Dragon" "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS))


                # Air Base
                cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase")
                                                              | HasAll("Air Base - Special Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase")
                                                              | HasAll("Air Base - Special Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase"))


                # Pelagic II
                cheat_pelagic_timed_complete = world.get_location("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
                world.set_rule(cheat_pelagic_timed_complete, HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner")
                                                             | HasAll("Pelagic II - Special Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner")
                                                             | HasAll("Pelagic II - Special Agent", "Laptop Gun", "CMP150", "X-Ray Scanner"))


                # Attack Ship
                cheat_attack_ship_timed_complete = world.get_location("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")
                world.set_rule(cheat_attack_ship_timed_complete, HasAll("Attack Ship - Special Agent", "Mauler"))


            if world.options.perfect_agent:
                # Investigation
                cheat_investigation_timed_complete = world.get_location("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
                world.set_rule(cheat_investigation_timed_complete, HasAll("dD Investigation - Perfect Agent", "CamSpy", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                   | HasAll("dD Investigation - Perfect Agent", "CamSpy", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"))


                # Chicago
                cheat_chicago_timed_complete = world.get_location("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
                world.set_rule(cheat_chicago_timed_complete, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)")
                                                             | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "CMP150")
                                                             | HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "DY357 Magnum"))


                # Rescue
                cheat_rescue_timed_complete = world.get_location("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
                world.set_rule(cheat_rescue_timed_complete, (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                            | (HasAll("A51 Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS)
                                                            | (HasAll("A51 Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS))                    


                # Air Force One
                cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                world.set_rule(cheat_air_force_one_timed_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Laptop Gun", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                                   | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Cyclone", "Timed Mine") & HAS_AFO_LIFT_KEY)
                                                                   | (HasAll("Air Force One - Perfect Agent", "Suitcase", "K7 Avenger", "Timed Mine") & HAS_AFO_LIFT_KEY))


                # Deep Sea
                cheat_deep_sea_timed_complete = world.get_location("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
                world.set_rule(cheat_deep_sea_timed_complete, HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "Shotgun", "IR Scanner", "Backup Disk")
                                                              | HasAll("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "FarSight XR-20", "IR Scanner", "Backup Disk")
                                                              | HasAll("Deep Sea - Perfect Agent", "Shotgun", "FarSight XR-20", "IR Scanner", "Backup Disk"))

                # Skedar Ruins
                cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                world.set_rule(cheat_skedar_ruins_timed_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))


    elif world.options.weapon_progression.value > WeaponProgression.option_vanilla:
        if world.options.agent:
            # Stage 1 - Defection
            defection_agent_obj_1 = world.get_location("dD Defection - Agent Objective 1")
            world.set_rule(defection_agent_obj_1, Has("dD Defection - Agent"))

            defection_agent_complete = world.get_location("Complete: dD Defection - Agent")
            world.set_rule(defection_agent_complete, Has("dD Defection - Agent"))


            # Stage 2 - Investigation
            investigation_agent_obj_1 = world.get_location("dD Investigation - Agent Objective 1")
            world.set_rule(investigation_agent_obj_1, HasAll("dD Investigation - Agent", "CamSpy"))

            investigation_agent_obj_2 = world.get_location("dD Investigation - Agent Objective 2")
            world.set_rule(investigation_agent_obj_2, HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_agent_complete = world.get_location("Complete: dD Investigation - Agent")
            world.set_rule(investigation_agent_complete, HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 3 - Extraction
            extraction_agent_obj_1 = world.get_location("dD Extraction - Agent Objective 1")
            world.set_rule(extraction_agent_obj_1, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            extraction_agent_obj_2 = world.get_location("dD Extraction - Agent Objective 2")
            world.set_rule(extraction_agent_obj_2, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_agent_obj_3 = world.get_location("dD Extraction - Agent Objective 3")
            world.set_rule(extraction_agent_obj_3, HasAll("dD Extraction - Agent", "Night Vision")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_agent_complete = world.get_location("Complete: dD Extraction - Agent")
            world.set_rule(extraction_agent_complete, HasAll("dD Extraction - Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 4 - Villa
            villa_agent_obj_1 = world.get_location("Carrington Villa - Agent Objective 1")
            world.set_rule(villa_agent_obj_1, Has("Carrington Villa - Agent")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_agent_obj_2 = world.get_location("Carrington Villa - Agent Objective 2")
            world.set_rule(villa_agent_obj_2, Has("Carrington Villa - Agent")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_agent_obj_3 = world.get_location("Carrington Villa - Agent Objective 3")
            world.set_rule(villa_agent_obj_3, HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_agent_complete = world.get_location("Complete: Carrington Villa - Agent")
            world.set_rule(villa_agent_complete, HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            chicago_agent_obj_1 = world.get_location("Chicago - Agent Objective 1")
            world.set_rule(chicago_agent_obj_1, HasAll("Chicago - Agent", "Remote Mine", "Data Uplink"))

            chicago_agent_obj_2 = world.get_location("Chicago - Agent Objective 2")
            world.set_rule(chicago_agent_obj_2, (HasAll("Chicago - Agent", "Data Uplink")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                | (HasAll("Chicago - Agent", "CamSpy")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

            chicago_agent_obj_3 = world.get_location("Chicago - Agent Objective 3")
            world.set_rule(chicago_agent_obj_3, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                | (HasAll("Chicago - Agent", "Data Uplink") 
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            chicago_agent_complete = world.get_location("Complete: Chicago - Agent")
            world.set_rule(chicago_agent_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_agent_obj_1 = world.get_location("G5 Building - Agent Objective 1")
            world.set_rule(g5_agent_obj_1, HasAll("G5 Building - Agent", "CamSpy") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_obj_2 = world.get_location("G5 Building - Agent Objective 2")
            world.set_rule(g5_agent_obj_2, HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_obj_3 = world.get_location("G5 Building - Agent Objective 3")
            world.set_rule(g5_agent_obj_3, HasAll("G5 Building - Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_agent_complete = world.get_location("Complete: G5 Building - Agent")
            world.set_rule(g5_agent_complete, HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 7 - Infiltration
            infiltration_agent_obj_1 = world.get_location("A51 Infiltration - Agent Objective 1")
            world.set_rule(infiltration_agent_obj_1, HasAll("A51 Infiltration - Agent", "Explosives")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_obj_2 = world.get_location("A51 Infiltration - Agent Objective 2")
            world.set_rule(infiltration_agent_obj_2, HasAll("A51 Infiltration - Agent") & HAS_A51_INFIL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_obj_3 = world.get_location("A51 Infiltration - Agent Objective 3")
            world.set_rule(infiltration_agent_obj_3, HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_agent_complete = world.get_location("Complete: A51 Infiltration - Agent")
            world.set_rule(infiltration_agent_complete, HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_agent_obj_1 = world.get_location("A51 Rescue - Agent Objective 1")
            world.set_rule(rescue_agent_obj_1, HasAll("A51 Rescue - Agent", "Lab Clothes")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_agent_obj_2 = world.get_location("A51 Rescue - Agent Objective 2")
            world.set_rule(rescue_agent_obj_2, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_agent_obj_3 = world.get_location("A51 Rescue - Agent Objective 3")
            world.set_rule(rescue_agent_obj_3, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_agent_complete = world.get_location("Complete: A51 Rescue - Agent")
            world.set_rule(rescue_agent_complete, HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_agent_obj_1 = world.get_location("A51 Escape - Agent Objective 1")
            world.set_rule(escape_agent_obj_1, Has("A51 Escape - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_agent_obj_2 = world.get_location("A51 Escape - Agent Objective 2")
            world.set_rule(escape_agent_obj_2, Has("A51 Escape - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_agent_obj_3 = world.get_location("A51 Escape - Agent Objective 3")
            world.set_rule(escape_agent_obj_3, HasAll("A51 Escape - Agent", "Alien Medpack")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_agent_complete = world.get_location("Complete: A51 Escape - Agent")
            world.set_rule(escape_agent_complete, HasAll("A51 Escape - Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
                world.set_rule(air_base_agent_obj_1, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                     | (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")))

                air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
                world.set_rule(air_base_agent_obj_2, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                     | (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")))

                air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
                world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "Stewardess Disguise")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                
                air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
                world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_agent_obj_1 = world.get_location("Air Base - Agent Objective 1")
                world.set_rule(air_base_agent_obj_1, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

                air_base_agent_obj_2 = world.get_location("Air Base - Agent Objective 2")
                world.set_rule(air_base_agent_obj_2, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise"))

                air_base_agent_obj_3 = world.get_location("Air Base - Agent Objective 3")
                world.set_rule(air_base_agent_obj_3, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

                air_base_agent_complete = world.get_location("Complete: Air Base - Agent")
                world.set_rule(air_base_agent_complete, HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 11 - Air Force One
            air_force_one_agent_obj_1 = world.get_location("Air Force One - Agent Objective 1")
            world.set_rule(air_force_one_agent_obj_1, HasAll("Air Force One - Agent", "Suitcase"))

            air_force_one_agent_obj_2 = world.get_location("Air Force One - Agent Objective 2")
            world.set_rule(air_force_one_agent_obj_2, HasAll("Air Force One - Agent", "Suitcase")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_agent_obj_3 = world.get_location("Air Force One - Agent Objective 3")
            world.set_rule(air_force_one_agent_obj_3, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Air Force One - Agent", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_agent_complete = world.get_location("Complete: Air Force One - Agent")
            world.set_rule(air_force_one_agent_complete, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Agent", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_agent_obj_1 = world.get_location("Crash Site - Agent Objective 1")
            world.set_rule(crash_site_agent_obj_1, Has("Crash Site - Agent"))

            crash_site_agent_obj_2 = world.get_location("Crash Site - Agent Objective 2")
            world.set_rule(crash_site_agent_obj_2, HasAll("Crash Site - Agent", "President Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_agent_obj_3 = world.get_location("Crash Site - Agent Objective 3")
            world.set_rule(crash_site_agent_obj_3, HasAll("Crash Site - Agent", "President Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_agent_complete = world.get_location("Complete: Crash Site - Agent")
            world.set_rule(crash_site_agent_complete, HasAll("Crash Site - Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_agent_obj_1 = world.get_location("Pelagic II - Agent Objective 1")
            world.set_rule(pelagic_agent_obj_1, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_agent_obj_2 = world.get_location("Pelagic II - Agent Objective 2")
            world.set_rule(pelagic_agent_obj_2, Has("Pelagic II - Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_agent_obj_3 = world.get_location("Pelagic II - Agent Objective 3")
            world.set_rule(pelagic_agent_obj_3, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_agent_complete = world.get_location("Complete: Pelagic II - Agent")
            world.set_rule(pelagic_agent_complete, HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_agent_obj_1 = world.get_location("Deep Sea - Agent Objective 1")
            world.set_rule(deep_sea_agent_obj_1, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_obj_2 = world.get_location("Deep Sea - Agent Objective 2")
            world.set_rule(deep_sea_agent_obj_2, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_obj_3 = world.get_location("Deep Sea - Agent Objective 3")
            world.set_rule(deep_sea_agent_obj_3, HasAll("Deep Sea - Agent", "IR Scanner")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_agent_complete = world.get_location("Complete: Deep Sea - Agent")
            world.set_rule(deep_sea_agent_complete, HasAll("Deep Sea - Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 15 - Carrington Institute Defense
            institute_defense_agent_obj_1 = world.get_location("CI Defense - Agent Objective 1")
            world.set_rule(institute_defense_agent_obj_1, Has("CI Defense - Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_agent_obj_2 = world.get_location("CI Defense - Agent Objective 2")
            world.set_rule(institute_defense_agent_obj_2, (HasAll("CI Defense - Agent", "RC-P120")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                          | (Has("CI Defense - Agent")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_agent_obj_3 = world.get_location("CI Defense - Agent Objective 3")
            world.set_rule(institute_defense_agent_obj_3, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                          | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_agent_complete = world.get_location("Complete: CI Defense - Agent")
            world.set_rule(institute_defense_agent_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_agent_obj_1 = world.get_location("Attack Ship - Agent Objective 1")
            world.set_rule(attack_ship_agent_obj_1, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_obj_2 = world.get_location("Attack Ship - Agent Objective 2")
            world.set_rule(attack_ship_agent_obj_2, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_obj_3 = world.get_location("Attack Ship - Agent Objective 3")
            world.set_rule(attack_ship_agent_obj_3, Has("Attack Ship - Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_agent_complete = world.get_location("Complete: Attack Ship - Agent")
            world.set_rule(attack_ship_agent_complete, Has("Attack Ship - Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
                world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
                world.set_rule(skedar_ruins_agent_obj_2, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                         | (HAS_SKEDAR_RUINS_AGENT
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
                world.set_rule(skedar_ruins_agent_obj_3, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                         | (HAS_SKEDAR_RUINS_AGENT & HasAll("IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
                world.set_rule(skedar_ruins_agent_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_agent_obj_1 = world.get_location("Skedar Ruins - Agent Objective 1")
                world.set_rule(skedar_ruins_agent_obj_1, HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_2 = world.get_location("Skedar Ruins - Agent Objective 2")
                world.set_rule(skedar_ruins_agent_obj_2, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_obj_3 = world.get_location("Skedar Ruins - Agent Objective 3")
                world.set_rule(skedar_ruins_agent_obj_3, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "IR Scanner")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_agent_complete = world.get_location("Complete: Skedar Ruins - Agent")
                world.set_rule(skedar_ruins_agent_complete, HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Agent Objective 1")
            world.set_rule(mbr_agent_obj_1, Has("Mr. Blonde's Revenge - Agent")
                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Agent")
            world.set_rule(mbr_agent_complete, Has("Mr. Blonde's Revenge - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_agent_obj_1 = world.get_location("Maian SOS - Agent Objective 1")
            world.set_rule(maian_sos_agent_obj_1, Has("Maian SOS - Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_agent_complete = world.get_location("Complete: Maian SOS - Agent")
            world.set_rule(maian_sos_agent_complete, Has("Maian SOS - Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 20 - WAR!
            war_agent_obj_1 = world.get_location("WAR! - Agent Objective 1")
            world.set_rule(war_agent_obj_1, Has("WAR! - Agent")
                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_agent_complete = world.get_location("Complete: WAR! - Agent")
            world.set_rule(war_agent_complete, Has("WAR! - Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_agent_obj_1 = world.get_location("The Duel - Agent Objective 1")
            world.set_rule(duel_agent_obj_1, Has("The Duel - Agent"))

            duel_agent_complete = world.get_location("Complete: The Duel - Agent")
            world.set_rule(duel_agent_complete, Has("The Duel - Agent"))


        if world.options.special_agent:
            # Stage 1 - Defection
            defection_sp_agent_obj_1 = world.get_location("dD Defection - Special Agent Objective 1")
            world.set_rule(defection_sp_agent_obj_1, HasAll("dD Defection - Special Agent", "ECM Mine"))

            defection_sp_agent_obj_2 = world.get_location("dD Defection - Special Agent Objective 2")
            world.set_rule(defection_sp_agent_obj_2, Has("dD Defection - Special Agent") & HAS_DD_KEYS)

            defection_sp_agent_obj_3 = world.get_location("dD Defection - Special Agent Objective 3")
            world.set_rule(defection_sp_agent_obj_3, HasAll("dD Defection - Special Agent", "ECM Mine")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_sp_agent_obj_4 = world.get_location("dD Defection - Special Agent Objective 4")
            world.set_rule(defection_sp_agent_obj_4, Has("dD Defection - Special Agent") & HAS_DD_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_sp_agent_complete = world.get_location("Complete: dD Defection - Special Agent")
            world.set_rule(defection_sp_agent_complete, HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 2 - Investigation
            investigation_sp_agent_obj_1 = world.get_location("dD Investigation - Special Agent Objective 1")
            world.set_rule(investigation_sp_agent_obj_1, HasAll("dD Investigation - Special Agent", "CamSpy"))

            investigation_sp_agent_obj_2 = world.get_location("dD Investigation - Special Agent Objective 2")
            world.set_rule(investigation_sp_agent_obj_2, Has("dD Investigation - Special Agent"))

            investigation_sp_agent_obj_3 = world.get_location("dD Investigation - Special Agent Objective 3")
            world.set_rule(investigation_sp_agent_obj_3, Has("dD Investigation - Special Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_sp_agent_obj_4 = world.get_location("dD Investigation - Special Agent Objective 4")
            world.set_rule(investigation_sp_agent_obj_4, HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_sp_agent_complete = world.get_location("Complete: dD Investigation - Special Agent")
            world.set_rule(investigation_sp_agent_complete, HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 3 - Extraction
            extraction_sp_agent_obj_1 = world.get_location("dD Extraction - Special Agent Objective 1")
            world.set_rule(extraction_sp_agent_obj_1, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))

            extraction_sp_agent_obj_2 = world.get_location("dD Extraction - Special Agent Objective 2")
            world.set_rule(extraction_sp_agent_obj_2, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_obj_3 = world.get_location("dD Extraction - Special Agent Objective 3")
            world.set_rule(extraction_sp_agent_obj_3, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_obj_4 = world.get_location("dD Extraction - Special Agent Objective 4")
            world.set_rule(extraction_sp_agent_obj_4, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_sp_agent_complete = world.get_location("Complete: dD Extraction - Special Agent")
            world.set_rule(extraction_sp_agent_complete, HasAll("dD Extraction - Special Agent", "Night Vision")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 4 - Villa
            villa_sp_agent_obj_1 = world.get_location("Carrington Villa - Special Agent Objective 1")
            world.set_rule(villa_sp_agent_obj_1, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_obj_2 = world.get_location("Carrington Villa - Special Agent Objective 2")
            world.set_rule(villa_sp_agent_obj_2, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_obj_3 = world.get_location("Carrington Villa - Special Agent Objective 3")
            world.set_rule(villa_sp_agent_obj_3, Has("Carrington Villa - Special Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_sp_agent_obj_4 = world.get_location("Carrington Villa - Special Agent Objective 4")
            world.set_rule(villa_sp_agent_obj_4, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_sp_agent_complete = world.get_location("Complete: Carrington Villa - Special Agent")
            world.set_rule(villa_sp_agent_complete, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            chicago_sp_agent_obj_1 = world.get_location("Chicago - Special Agent Objective 1")
            world.set_rule(chicago_sp_agent_obj_1, HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink"))

            chicago_sp_agent_obj_2 = world.get_location("Chicago - Special Agent Objective 2")
            world.set_rule(chicago_sp_agent_obj_2, (HasAll("Chicago - Special Agent", "Remote Mine")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (Has("Chicago - Special Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_sp_agent_obj_3 = world.get_location("Chicago - Special Agent Objective 3")
            world.set_rule(chicago_sp_agent_obj_3, (HasAll("Chicago - Special Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "CamSpy")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

            chicago_sp_agent_obj_4 = world.get_location("Chicago - Special Agent Objective 4")
            world.set_rule(chicago_sp_agent_obj_4, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            chicago_sp_agent_complete = world.get_location("Complete: Chicago - Special Agent")
            world.set_rule(chicago_sp_agent_complete, (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                      | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 6 - G5 Building
            g5_sp_agent_obj_1 = world.get_location("G5 Building - Special Agent Objective 1")
            world.set_rule(g5_sp_agent_obj_1, Has("G5 Building - Special Agent") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_2 = world.get_location("G5 Building - Special Agent Objective 2")
            world.set_rule(g5_sp_agent_obj_2, HasAll("G5 Building - Special Agent", "CamSpy") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_3 = world.get_location("G5 Building - Special Agent Objective 3")
            world.set_rule(g5_sp_agent_obj_3, HasAll("G5 Building - Special Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            g5_sp_agent_obj_4 = world.get_location("G5 Building - Special Agent Objective 4")
            world.set_rule(g5_sp_agent_obj_4, (HasAll("G5 Building - Special Agent", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (Has("G5 Building - Special Agent") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            g5_sp_agent_complete = world.get_location("Complete: G5 Building - Special Agent")
            world.set_rule(g5_sp_agent_complete, (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                 | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Stage 7 - Infiltration
            infiltration_sp_agent_obj_1 = world.get_location("A51 Infiltration - Special Agent Objective 1")
            world.set_rule(infiltration_sp_agent_obj_1, HasAll("A51 Infiltration - Special Agent", "Explosives")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_2 = world.get_location("A51 Infiltration - Special Agent Objective 2")
            world.set_rule(infiltration_sp_agent_obj_2, HasAll("A51 Infiltration - Special Agent", "Comms Rider")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_3 = world.get_location("A51 Infiltration - Special Agent Objective 3")
            world.set_rule(infiltration_sp_agent_obj_3, HasAll("A51 Infiltration - Special Agent") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_obj_4 = world.get_location("A51 Infiltration - Special Agent Objective 4")
            world.set_rule(infiltration_sp_agent_obj_4, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_sp_agent_complete = world.get_location("Complete: A51 Infiltration - Special Agent")
            world.set_rule(infiltration_sp_agent_complete, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_sp_agent_obj_1 = world.get_location("A51 Rescue - Special Agent Objective 1")
            world.set_rule(rescue_sp_agent_obj_1, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_2 = world.get_location("A51 Rescue - Special Agent Objective 2")
            world.set_rule(rescue_sp_agent_obj_2, HasAll("A51 Rescue - Special Agent", "Lab Clothes")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_3 = world.get_location("A51 Rescue - Special Agent Objective 3")
            world.set_rule(rescue_sp_agent_obj_3, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_sp_agent_obj_4 = world.get_location("A51 Rescue - Special Agent Objective 4")
            world.set_rule(rescue_sp_agent_obj_4, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_sp_agent_complete = world.get_location("Complete: A51 Rescue - Special Agent")
            world.set_rule(rescue_sp_agent_complete, HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_sp_agent_obj_1 = world.get_location("A51 Escape - Special Agent Objective 1")
            world.set_rule(escape_sp_agent_obj_1, Has("A51 Escape - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_sp_agent_obj_2 = world.get_location("A51 Escape - Special Agent Objective 2")
            world.set_rule(escape_sp_agent_obj_2, Has("A51 Escape - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_sp_agent_obj_3 = world.get_location("A51 Escape - Special Agent Objective 3")
            world.set_rule(escape_sp_agent_obj_3, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_sp_agent_obj_4 = world.get_location("A51 Escape - Special Agent Objective 4")
            world.set_rule(escape_sp_agent_obj_4, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_sp_agent_complete = world.get_location("Complete: A51 Escape - Special Agent")
            world.set_rule(escape_sp_agent_complete, HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
                world.set_rule(air_base_sp_agent_obj_1, (HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise")))

                air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
                world.set_rule(air_base_sp_agent_obj_2, (HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")))

                air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
                world.set_rule(air_base_sp_agent_obj_3, (HasAll("Air Base - Special Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise")))

                air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
                world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
                world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_sp_agent_obj_1 = world.get_location("Air Base - Special Agent Objective 1")
                world.set_rule(air_base_sp_agent_obj_1, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

                air_base_sp_agent_obj_2 = world.get_location("Air Base - Special Agent Objective 2")
                world.set_rule(air_base_sp_agent_obj_2, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_sp_agent_obj_3 = world.get_location("Air Base - Special Agent Objective 3")
                world.set_rule(air_base_sp_agent_obj_3, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise"))

                air_base_sp_agent_obj_4 = world.get_location("Air Base - Special Agent Objective 4")
                world.set_rule(air_base_sp_agent_obj_4, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_sp_agent_complete = world.get_location("Complete: Air Base - Special Agent")
                world.set_rule(air_base_sp_agent_complete, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


            # Stage 11 - Air Force One
            air_force_one_sp_agent_obj_1 = world.get_location("Air Force One - Special Agent Objective 1")
            world.set_rule(air_force_one_sp_agent_obj_1, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_2 = world.get_location("Air Force One - Special Agent Objective 2")
            world.set_rule(air_force_one_sp_agent_obj_2, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_sp_agent_obj_3 = world.get_location("Air Force One - Special Agent Objective 3")
            world.set_rule(air_force_one_sp_agent_obj_3, HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_sp_agent_obj_4 = world.get_location("Air Force One - Special Agent Objective 4")
            world.set_rule(air_force_one_sp_agent_obj_4, (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_sp_agent_complete = world.get_location("Complete: Air Force One - Special Agent")
            world.set_rule(air_force_one_sp_agent_complete, (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                            | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_sp_agent_obj_1 = world.get_location("Crash Site - Special Agent Objective 1")
            world.set_rule(crash_site_sp_agent_obj_1, HasAll("Crash Site - Special Agent", "President Scanner"))

            crash_site_sp_agent_obj_2 = world.get_location("Crash Site - Special Agent Objective 2")
            world.set_rule(crash_site_sp_agent_obj_2, Has("Crash Site - Special Agent"))

            crash_site_sp_agent_obj_3 = world.get_location("Crash Site - Special Agent Objective 3")
            world.set_rule(crash_site_sp_agent_obj_3, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_sp_agent_obj_4 = world.get_location("Crash Site - Special Agent Objective 4")
            world.set_rule(crash_site_sp_agent_obj_4, HasAll("Crash Site - Special Agent", "President Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_sp_agent_complete = world.get_location("Complete: Crash Site - Special Agent")
            world.set_rule(crash_site_sp_agent_complete, HasAll("Crash Site - Special Agent", "President Scanner")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_sp_agent_obj_1 = world.get_location("Pelagic II - Special Agent Objective 1")
            world.set_rule(pelagic_sp_agent_obj_1, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_2 = world.get_location("Pelagic II - Special Agent Objective 2")
            world.set_rule(pelagic_sp_agent_obj_2, Has("Pelagic II - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_3 = world.get_location("Pelagic II - Special Agent Objective 3")
            world.set_rule(pelagic_sp_agent_obj_3, Has("Pelagic II - Special Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_sp_agent_obj_4 = world.get_location("Pelagic II - Special Agent Objective 4")
            world.set_rule(pelagic_sp_agent_obj_4, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_sp_agent_complete = world.get_location("Complete: Pelagic II - Special Agent")
            world.set_rule(pelagic_sp_agent_complete, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_sp_agent_obj_1 = world.get_location("Deep Sea - Special Agent Objective 1")
            world.set_rule(deep_sea_sp_agent_obj_1, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_2 = world.get_location("Deep Sea - Special Agent Objective 2")
            world.set_rule(deep_sea_sp_agent_obj_2, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_3 = world.get_location("Deep Sea - Special Agent Objective 3")
            world.set_rule(deep_sea_sp_agent_obj_3, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_sp_agent_obj_4 = world.get_location("Deep Sea - Special Agent Objective 4")
            world.set_rule(deep_sea_sp_agent_obj_4, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            
            deep_sea_sp_agent_complete = world.get_location("Complete: Deep Sea - Special Agent")
            world.set_rule(deep_sea_sp_agent_complete, HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 15 - Carrington Institute Defense
            institute_defense_sp_agent_obj_1 = world.get_location("CI Defense - Special Agent Objective 1")
            world.set_rule(institute_defense_sp_agent_obj_1, Has("CI Defense - Special Agent"))

            institute_defense_sp_agent_obj_2 = world.get_location("CI Defense - Special Agent Objective 2")
            world.set_rule(institute_defense_sp_agent_obj_2, Has("CI Defense - Special Agent")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_sp_agent_obj_3 = world.get_location("CI Defense - Special Agent Objective 3")
            world.set_rule(institute_defense_sp_agent_obj_3, (HasAll("CI Defense - Special Agent", "RC-P120")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (Has("CI Defense - Special Agent")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_sp_agent_obj_4 = world.get_location("CI Defense - Special Agent Objective 4")
            world.set_rule(institute_defense_sp_agent_obj_4, (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_sp_agent_complete = world.get_location("Complete: CI Defense - Special Agent")
            world.set_rule(institute_defense_sp_agent_complete, (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Stage 16 - Attack Ship
            attack_ship_sp_agent_obj_1 = world.get_location("Attack Ship - Special Agent Objective 1")
            world.set_rule(attack_ship_sp_agent_obj_1, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_2 = world.get_location("Attack Ship - Special Agent Objective 2")
            world.set_rule(attack_ship_sp_agent_obj_2, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_3 = world.get_location("Attack Ship - Special Agent Objective 3")
            world.set_rule(attack_ship_sp_agent_obj_3, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_obj_4 = world.get_location("Attack Ship - Special Agent Objective 4")
            world.set_rule(attack_ship_sp_agent_obj_4, Has("Attack Ship - Special Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_sp_agent_complete = world.get_location("Complete: Attack Ship - Special Agent")
            world.set_rule(attack_ship_sp_agent_complete, Has("Attack Ship - Special Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            

            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
                world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
                world.set_rule(skedar_ruins_sp_agent_obj_2, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
                world.set_rule(skedar_ruins_sp_agent_obj_3, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))
                
                skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
                world.set_rule(skedar_ruins_sp_agent_obj_4, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
                world.set_rule(skedar_ruins_sp_agent_complete, (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                               | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))
            
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_sp_agent_obj_1 = world.get_location("Skedar Ruins - Special Agent Objective 1")
                world.set_rule(skedar_ruins_sp_agent_obj_1, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_2 = world.get_location("Skedar Ruins - Special Agent Objective 2")
                world.set_rule(skedar_ruins_sp_agent_obj_2, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_obj_3 = world.get_location("Skedar Ruins - Special Agent Objective 3")
                world.set_rule(skedar_ruins_sp_agent_obj_3, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                
                skedar_ruins_sp_agent_obj_4 = world.get_location("Skedar Ruins - Special Agent Objective 4")
                world.set_rule(skedar_ruins_sp_agent_obj_4, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "IR Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_sp_agent_complete = world.get_location("Complete: Skedar Ruins - Special Agent")
                world.set_rule(skedar_ruins_sp_agent_complete, HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_sp_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 1")
            world.set_rule(mbr_sp_agent_obj_1, HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_sp_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Special Agent Objective 2")
            world.set_rule(mbr_sp_agent_obj_2, Has("Mr. Blonde's Revenge - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_sp_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Special Agent")
            world.set_rule(mbr_sp_agent_complete, HasAll("Mr. Blonde's Revenge - Special Agent", "Skedar Bomb")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_sp_agent_obj_1 = world.get_location("Maian SOS - Special Agent Objective 1")
            world.set_rule(maian_sos_sp_agent_obj_1, Has("Maian SOS - Special Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_sp_agent_obj_2 = world.get_location("Maian SOS - Special Agent Objective 2")
            world.set_rule(maian_sos_sp_agent_obj_2, Has("Maian SOS - Special Agent")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_sp_agent_complete = world.get_location("Complete: Maian SOS - Special Agent")
            world.set_rule(maian_sos_sp_agent_complete, Has("Maian SOS - Special Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 20 - WAR!
            war_sp_agent_obj_1 = world.get_location("WAR! - Special Agent Objective 1")
            world.set_rule(war_sp_agent_obj_1, Has("WAR! - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_sp_agent_obj_2 = world.get_location("WAR! - Special Agent Objective 2")
            world.set_rule(war_sp_agent_obj_2, Has("WAR! - Special Agent")
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_sp_agent_complete = world.get_location("Complete: WAR! - Special Agent")
            world.set_rule(war_sp_agent_complete, Has("WAR! - Special Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_sp_agent_obj_1 = world.get_location("The Duel - Special Agent Objective 1")
            world.set_rule(duel_sp_agent_obj_1, Has("The Duel - Special Agent"))

            duel_sp_agent_obj_2 = world.get_location("The Duel - Special Agent Objective 2")
            world.set_rule(duel_sp_agent_obj_2, Has("The Duel - Special Agent"))

            duel_sp_agent_complete = world.get_location("Complete: The Duel - Special Agent")
            world.set_rule(duel_sp_agent_complete, Has("The Duel - Special Agent"))


        if world.options.perfect_agent:
            # Stage 1 - Defection
            defection_prf_agent_obj_1 = world.get_location("dD Defection - Perfect Agent Objective 1")
            world.set_rule(defection_prf_agent_obj_1, HasAll("dD Defection - Perfect Agent", "ECM Mine"))

            defection_prf_agent_obj_2 = world.get_location("dD Defection - Perfect Agent Objective 2")
            world.set_rule(defection_prf_agent_obj_2, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS)

            defection_prf_agent_obj_3 = world.get_location("dD Defection - Perfect Agent Objective 3")
            world.set_rule(defection_prf_agent_obj_3, HasAll("dD Defection - Perfect Agent", "Data Uplink")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_obj_4 = world.get_location("dD Defection - Perfect Agent Objective 4")
            world.set_rule(defection_prf_agent_obj_4, HasAll("dD Defection - Perfect Agent", "ECM Mine")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_obj_5 = world.get_location("dD Defection - Perfect Agent Objective 5")
            world.set_rule(defection_prf_agent_obj_5, Has("dD Defection - Perfect Agent") & HAS_DD_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            defection_prf_agent_complete = world.get_location("Complete: dD Defection - Perfect Agent")
            world.set_rule(defection_prf_agent_complete, HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink") & HAS_DD_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 2 - Investigation
            investigation_prf_agent_obj_1 = world.get_location("dD Investigation - Perfect Agent Objective 1")
            world.set_rule(investigation_prf_agent_obj_1, HasAll("dD Investigation - Perfect Agent", "CamSpy"))

            investigation_prf_agent_obj_2 = world.get_location("dD Investigation - Perfect Agent Objective 2")
            world.set_rule(investigation_prf_agent_obj_2, Has("dD Investigation - Perfect Agent"))

            investigation_prf_agent_obj_3 = world.get_location("dD Investigation - Perfect Agent Objective 3")
            world.set_rule(investigation_prf_agent_obj_3, Has("dD Investigation - Perfect Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            investigation_prf_agent_obj_4 = world.get_location("dD Investigation - Perfect Agent Objective 4")
            world.set_rule(investigation_prf_agent_obj_4, (HasAll("dD Investigation - Perfect Agent", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | HasAll("dD Investigation - Perfect Agent", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))

            investigation_prf_agent_obj_5 = world.get_location("dD Investigation - Perfect Agent Objective 5")
            world.set_rule(investigation_prf_agent_obj_5, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                          | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))

            investigation_prf_agent_complete = world.get_location("Complete: dD Investigation - Perfect Agent")
            world.set_rule(investigation_prf_agent_complete, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                             | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))  


            # Stage 3 - Extraction
            extraction_prf_agent_obj_1 = world.get_location("dD Extraction - Perfect Agent Objective 1")
            world.set_rule(extraction_prf_agent_obj_1, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_2 = world.get_location("dD Extraction - Perfect Agent Objective 2")
            world.set_rule(extraction_prf_agent_obj_2, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_3 = world.get_location("dD Extraction - Perfect Agent Objective 3")
            world.set_rule(extraction_prf_agent_obj_3, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
            
            extraction_prf_agent_obj_4 = world.get_location("dD Extraction - Perfect Agent Objective 4")
            world.set_rule(extraction_prf_agent_obj_4, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_obj_5 = world.get_location("dD Extraction - Perfect Agent Objective 5")
            world.set_rule(extraction_prf_agent_obj_5, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            extraction_prf_agent_complete = world.get_location("Complete: dD Extraction - Perfect Agent")
            world.set_rule(extraction_prf_agent_complete, HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


            # Stage 4 - Villa
            villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
            world.set_rule(villa_prf_agent_obj_1, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
            
            villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
            world.set_rule(villa_prf_agent_obj_2, Has("Carrington Villa - Perfect Agent")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
            world.set_rule(villa_prf_agent_obj_3, Has("Carrington Villa - Perfect Agent")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))

            villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
            world.set_rule(villa_prf_agent_obj_4, Has("Carrington Villa - Perfect Agent"))

            villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
            world.set_rule(villa_prf_agent_obj_5, HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))

            villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
            world.set_rule(villa_prf_agent_complete, HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


            # Stage 5 - Chicago
            chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
            world.set_rule(chicago_prf_agent_obj_1, HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink"))

            chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
            world.set_rule(chicago_prf_agent_obj_2, HasAll("Chicago - Perfect Agent", "Tracer Bug"))

            chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
            world.set_rule(chicago_prf_agent_obj_3, (HasAll("Chicago - Perfect Agent", "Remote Mine")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (Has("Chicago - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
            world.set_rule(chicago_prf_agent_obj_4, (HasAll("Chicago - Perfect Agent", "Data Uplink")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Perfect Agent", "CamSpy")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))

            chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
            world.set_rule(chicago_prf_agent_obj_5, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                    | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            
            chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
            world.set_rule(chicago_prf_agent_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                       | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))     


            # Stage 6 - G5 Building
            g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
            world.set_rule(g5_prf_agent_obj_1, Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
            world.set_rule(g5_prf_agent_obj_2, Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
            world.set_rule(g5_prf_agent_obj_3, HasAll("G5 Building - Perfect Agent", "CamSpy") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
            world.set_rule(g5_prf_agent_obj_4, HasAll("G5 Building - Perfect Agent", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
            world.set_rule(g5_prf_agent_obj_5, (HasAll("G5 Building - Perfect Agent", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                               | (Has("G5 Building - Perfect Agent") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))

            g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
            world.set_rule(g5_prf_agent_complete, (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))
            

            # Stage 7 - Infiltration
            infiltration_prf_agent_obj_1 = world.get_location("A51 Infiltration - Perfect Agent Objective 1")
            world.set_rule(infiltration_prf_agent_obj_1, HasAll("A51 Infiltration - Perfect Agent", "Explosives")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_2 = world.get_location("A51 Infiltration - Perfect Agent Objective 2")
            world.set_rule(infiltration_prf_agent_obj_2, HasAll("A51 Infiltration - Perfect Agent", "Comms Rider")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_3 = world.get_location("A51 Infiltration - Perfect Agent Objective 3")
            world.set_rule(infiltration_prf_agent_obj_3, Has("A51 Infiltration - Perfect Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_4 = world.get_location("A51 Infiltration - Perfect Agent Objective 4")
            world.set_rule(infiltration_prf_agent_obj_4, HasAll("A51 Infiltration - Perfect Agent") & HAS_A51_INFIL_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_obj_5 = world.get_location("A51 Infiltration - Perfect Agent Objective 5")
            world.set_rule(infiltration_prf_agent_obj_5, HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            infiltration_prf_agent_complete = world.get_location("Complete: A51 Infiltration - Perfect Agent")
            world.set_rule(infiltration_prf_agent_complete, HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 8 - Rescue
            rescue_prf_agent_obj_1 = world.get_location("A51 Rescue - Perfect Agent Objective 1")
            world.set_rule(rescue_prf_agent_obj_1, HasAll("A51 Rescue - Perfect Agent", "Data Uplink")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_2 = world.get_location("A51 Rescue - Perfect Agent Objective 2")
            world.set_rule(rescue_prf_agent_obj_2, HasAll("A51 Rescue - Perfect Agent", "X-Ray Scanner")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_3 = world.get_location("A51 Rescue - Perfect Agent Objective 3")
            world.set_rule(rescue_prf_agent_obj_3, HasAll("A51 Rescue - Perfect Agent", "Lab Clothes")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_4 = world.get_location("A51 Rescue - Perfect Agent Objective 4")
            world.set_rule(rescue_prf_agent_obj_4, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_FIRST_KEY
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            rescue_prf_agent_obj_5 = world.get_location("A51 Rescue - Perfect Agent Objective 5")
            world.set_rule(rescue_prf_agent_obj_5, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            rescue_prf_agent_complete = world.get_location("Complete: A51 Rescue - Perfect Agent")
            world.set_rule(rescue_prf_agent_complete, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 9 - Escape
            escape_prf_agent_obj_1 = world.get_location("A51 Escape - Perfect Agent Objective 1")
            world.set_rule(escape_prf_agent_obj_1, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_2 = world.get_location("A51 Escape - Perfect Agent Objective 2")
            world.set_rule(escape_prf_agent_obj_2, Has("A51 Escape - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_3 = world.get_location("A51 Escape - Perfect Agent Objective 3")
            world.set_rule(escape_prf_agent_obj_3, Has("A51 Escape - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_4 = world.get_location("A51 Escape - Perfect Agent Objective 4")
            world.set_rule(escape_prf_agent_obj_4, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            escape_prf_agent_obj_5 = world.get_location("A51 Escape - Perfect Agent Objective 5")
            world.set_rule(escape_prf_agent_obj_5, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            escape_prf_agent_complete = world.get_location("Complete: A51 Escape - Perfect Agent")
            world.set_rule(escape_prf_agent_complete, HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            

            # Stage 10 - Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1,  (HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                          | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise")))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2,  (HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                          | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase")))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3,  (HasAll("Air Base - Perfect Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
                                                          | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise")))

                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
            
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
                world.set_rule(air_base_prf_agent_obj_1, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))

                air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
                world.set_rule(air_base_prf_agent_obj_2, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"))

                air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
                world.set_rule(air_base_prf_agent_obj_3, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"))
                
                air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
                world.set_rule(air_base_prf_agent_obj_4, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
                world.set_rule(air_base_prf_agent_obj_5, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                
                air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
                world.set_rule(air_base_prf_agent_complete, HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


            # Stage 11 - Air Force One
            air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
            world.set_rule(air_force_one_prf_agent_obj_1, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
            world.set_rule(air_force_one_prf_agent_obj_2, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY)

            air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
            world.set_rule(air_force_one_prf_agent_obj_3, HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
            world.set_rule(air_force_one_prf_agent_obj_4, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
            world.set_rule(air_force_one_prf_agent_obj_5, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                          | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
            world.set_rule(air_force_one_prf_agent_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                             | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Stage 12 - Crash Site
            crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
            world.set_rule(crash_site_prf_agent_obj_1, HasAll("Crash Site - Perfect Agent", "President Scanner"))

            crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
            world.set_rule(crash_site_prf_agent_obj_2, Has("Crash Site - Perfect Agent"))

            crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
            world.set_rule(crash_site_prf_agent_obj_3, Has("Crash Site - Perfect Agent")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
            world.set_rule(crash_site_prf_agent_obj_4, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
            world.set_rule(crash_site_prf_agent_obj_5, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
            world.set_rule(crash_site_prf_agent_complete, HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                          & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 13 - Pelagic II
            pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
            world.set_rule(pelagic_prf_agent_obj_1, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
            world.set_rule(pelagic_prf_agent_obj_2, HasAll("Pelagic II - Perfect Agent", "Research Tape")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
            world.set_rule(pelagic_prf_agent_obj_3, Has("Pelagic II - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
            world.set_rule(pelagic_prf_agent_obj_4, Has("Pelagic II - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
            world.set_rule(pelagic_prf_agent_obj_5, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
            world.set_rule(pelagic_prf_agent_complete, HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                       & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 14 - Deep Sea
            deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
            world.set_rule(deep_sea_prf_agent_obj_1, HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                     & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
            world.set_rule(deep_sea_prf_agent_obj_2, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
            world.set_rule(deep_sea_prf_agent_obj_3, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
            world.set_rule(deep_sea_prf_agent_obj_4, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))

            deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
            world.set_rule(deep_sea_prf_agent_obj_5, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                     | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))
            
            deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
            world.set_rule(deep_sea_prf_agent_complete, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                        | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))
            

            # Stage 15 - Carrington Institute Defense
            institute_defense_prf_agent_obj_1 = world.get_location("CI Defense - Perfect Agent Objective 1")
            world.set_rule(institute_defense_prf_agent_obj_1, Has("CI Defense - Perfect Agent"))

            institute_defense_prf_agent_obj_2 = world.get_location("CI Defense - Perfect Agent Objective 2")
            world.set_rule(institute_defense_prf_agent_obj_2, Has("CI Defense - Perfect Agent")
                                                              & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))

            institute_defense_prf_agent_obj_3 = world.get_location("CI Defense - Perfect Agent Objective 3")
            world.set_rule(institute_defense_prf_agent_obj_3, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                              | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_prf_agent_obj_4 = world.get_location("CI Defense - Perfect Agent Objective 4")
            world.set_rule(institute_defense_prf_agent_obj_4, (HasAll("CI Defense - Perfect Agent", "RC-P120")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                              | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                              | (Has("CI Defense - Perfect Agent")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))

            institute_defense_prf_agent_obj_5 = world.get_location("CI Defense - Perfect Agent Objective 5")
            world.set_rule(institute_defense_prf_agent_obj_5, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                              | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))

            institute_defense_prf_agent_complete = world.get_location("Complete: CI Defense - Perfect Agent")
            world.set_rule(institute_defense_prf_agent_complete, (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                 | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))) 


            # Stage 16 - Attack Ship
            attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
            world.set_rule(attack_ship_prf_agent_obj_1, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
            world.set_rule(attack_ship_prf_agent_obj_2, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
            world.set_rule(attack_ship_prf_agent_obj_3, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
            world.set_rule(attack_ship_prf_agent_obj_4, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
            world.set_rule(attack_ship_prf_agent_obj_5, Has("Attack Ship - Perfect Agent")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
            world.set_rule(attack_ship_prf_agent_complete, Has("Attack Ship - Perfect Agent")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            

            # Stage 17 - Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
                world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
                world.set_rule(skedar_ruins_prf_agent_obj_2, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
                world.set_rule(skedar_ruins_prf_agent_obj_3, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
                world.set_rule(skedar_ruins_prf_agent_obj_4, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
                world.set_rule(skedar_ruins_prf_agent_obj_5, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                             | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
                world.set_rule(skedar_ruins_prf_agent_complete, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                                | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
                world.set_rule(skedar_ruins_prf_agent_obj_1, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
                world.set_rule(skedar_ruins_prf_agent_obj_2, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
                world.set_rule(skedar_ruins_prf_agent_obj_3, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
                world.set_rule(skedar_ruins_prf_agent_obj_4, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
                world.set_rule(skedar_ruins_prf_agent_obj_5, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "IR Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

                skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
                world.set_rule(skedar_ruins_prf_agent_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 18 - Mr. Blonde's Revenge
            mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            world.set_rule(mbr_prf_agent_obj_1, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            world.set_rule(mbr_prf_agent_obj_2, Has("Mr. Blonde's Revenge - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            world.set_rule(mbr_prf_agent_obj_3, Has("Mr. Blonde's Revenge - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
            world.set_rule(mbr_prf_agent_complete, HasAll("Mr. Blonde's Revenge - Perfect Agent", "Skedar Bomb")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


            # Stage 19 - Maian SOS
            maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
            world.set_rule(maian_sos_prf_agent_obj_1, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
            world.set_rule(maian_sos_prf_agent_obj_2, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
            world.set_rule(maian_sos_prf_agent_obj_3, Has("Maian SOS - Perfect Agent")
                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

            maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
            world.set_rule(maian_sos_prf_agent_complete, Has("Maian SOS - Perfect Agent")
                                                         & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
   

            # Stage 20 - WAR!
            war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
            world.set_rule(war_prf_agent_obj_1, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
            world.set_rule(war_prf_agent_obj_2, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
            world.set_rule(war_prf_agent_obj_3, Has("WAR! - Perfect Agent")
                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

            war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
            world.set_rule(war_prf_agent_complete, Has("WAR! - Perfect Agent")
                                                   & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            # Stage 21 - The Duel
            duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
            world.set_rule(duel_prf_agent_obj_1, Has("The Duel - Perfect Agent"))

            duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
            world.set_rule(duel_prf_agent_obj_2, Has("The Duel - Perfect Agent"))

            duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
            world.set_rule(duel_prf_agent_obj_3, Has("The Duel - Perfect Agent")
                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
            
            duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
            world.set_rule(duel_prf_agent_complete, Has("The Duel - Perfect Agent")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


        if world.options.unlock_cheats:
            # Defection
            cheat_defection_complete = world.get_location("Cheat Unlock: Complete dD Defection")
            world.set_rule(cheat_defection_complete, Has("dD Defection - Agent")
                                                     | (HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                     | (HasAll("dD Defection - Perfect Agent", "ECM Mine", "Data Uplink") & HAS_DD_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))


            # Investigation
            cheat_investigation_complete = world.get_location("Cheat Unlock: Complete dD Investigation")
            world.set_rule(cheat_investigation_complete, (HasAll("dD Investigation - Agent", "CamSpy", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Special Agent", "CamSpy", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                         | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))


            # Extraction
            cheat_extraction_complete = world.get_location("Cheat Unlock: Complete dD Extraction")
            world.set_rule(cheat_extraction_complete, (HasAll("dD Extraction - Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                      | (HasAll("dD Extraction - Special Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                      | (HasAll("dD Extraction - Perfect Agent", "Night Vision")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"])))


            # Villa
            cheat_villa_complete = world.get_location("Cheat Unlock: Complete Carrington Villa")
            world.set_rule(cheat_villa_complete, (HasAll("Carrington Villa - Agent", "Cellar Key Card")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
                                                 | (HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
                                                 | (HasAll("Carrington Villa - Perfect Agent", "Cellar Key Card")
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"])))


            # Chicago
            cheat_chicago_complete = world.get_location("Cheat Unlock: Complete Chicago")
            world.set_rule(cheat_chicago_complete, (HasAll("Chicago - Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                   | (HasAll("Chicago - Special Agent", "Remote Mine", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Special Agent", "Data Uplink") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                                   | (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                   | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # G5 Building
            cheat_g5_complete = world.get_location("Cheat Unlock: Complete G5 Building")
            world.set_rule(cheat_g5_complete, (HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                              | (HasAll("G5 Building - Special Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
                                              | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                              | (HasAll("G5 Building - Perfect Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


            # Infiltration
            cheat_infiltration_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration")
            world.set_rule(cheat_infiltration_complete, (HasAll("A51 Infiltration - Agent", "Explosives") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("A51 Infiltration - Perfect Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Rescue
            cheat_rescue_complete = world.get_location("Cheat Unlock: Complete A51 Rescue")
            world.set_rule(cheat_rescue_complete, (HasAll("A51 Rescue - Agent", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Rescue - Special Agent", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Escape
            cheat_escape_complete = world.get_location("Cheat Unlock: Complete A51 Escape")
            world.set_rule(cheat_escape_complete, (HasAll("A51 Escape - Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Escape - Special Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                  | (HasAll("A51 Escape - Perfect Agent", "Alien Medpack")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Air Base
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
                world.set_rule(cheat_air_base_complete, (HasAll("Air Base - Agent", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                                                        | (HasAll("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))
    
            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                cheat_air_base_complete = world.get_location("Cheat Unlock: Complete Air Base")
                world.set_rule(cheat_air_base_complete, (HasAll("Air Base - Agent", "CamSpy", "Stewardess Disguise")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                        | (HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
                                                        | (HasAll("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"])))


            # Air Force One
            cheat_air_force_one_complete = world.get_location("Cheat Unlock: Complete Air Force One")
            world.set_rule(cheat_air_force_one_complete, (HasAll("Air Force One - Agent", "Suitcase", "Timed Mine")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Agent", "Suitcase")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Special Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                         | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


            # Crash Site
            cheat_crash_site_complete = world.get_location("Cheat Unlock: Complete Crash Site")
            world.set_rule(cheat_crash_site_complete, (HasAll("Crash Site - Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Crash Site - Special Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                      | (HasAll("Crash Site - Perfect Agent", "President Scanner")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Pelagic II
            cheat_pelagic_complete = world.get_location("Cheat Unlock: Complete Pelagic II")
            world.set_rule(cheat_pelagic_complete, (HasAll("Pelagic II - Agent", "X-Ray Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                   | (HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                   | (HasAll("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"])))


            # Deep Sea
            cheat_deep_sea_complete = world.get_location("Cheat Unlock: Complete Deep Sea")
            world.set_rule(cheat_deep_sea_complete, (HasAll("Deep Sea - Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Special Agent", "IR Scanner")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                    | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))


            # CI Defense
            cheat_institute_defense_complete = world.get_location("Cheat Unlock: Complete CI Defense")
            world.set_rule(cheat_institute_defense_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                             | (HasAll("CI Defense - Special Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Special Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
                                                             | (HasAll("CI Defense - Perfect Agent", "RC-P120", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                             | (HasAll("CI Defense - Perfect Agent", "Data Uplink")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            # Attack Ship
            cheat_attack_ship_complete = world.get_location("Cheat Unlock: Complete Attack Ship")
            world.set_rule(cheat_attack_ship_complete, (Has("Attack Ship - Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                       | (Has("Attack Ship - Special Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                       | (Has("Attack Ship - Perfect Agent")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])))


            # Skedar Ruins
            if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
                world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                cheat_skedar_ruins_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins")
                world.set_rule(cheat_skedar_ruins_complete, (HAS_SKEDAR_RUINS_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_SP_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                            | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])))


            if world.options.agent:
                # Extraction
                cheat_extraction_timed_complete = world.get_location("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
                world.set_rule(cheat_extraction_timed_complete, HasAll("dD Extraction - Agent", "Night Vision")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # G5 Building
                cheat_g5_timed_complete = world.get_location("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
                world.set_rule(cheat_g5_timed_complete, HasAll("G5 Building - Agent", "CamSpy", "Door Decoder", "Backup Disk") & HAS_G5_KEYS
                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # Escape
                cheat_escape_timed_complete = world.get_location("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
                world.set_rule(cheat_escape_timed_complete, HasAll("A51 Escape - Agent", "Alien Medpack")
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Crash Site
                cheat_crash_site_timed_complete = world.get_location("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
                world.set_rule(cheat_crash_site_timed_complete, HasAll("Crash Site - Agent", "President Scanner")
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # CI Defense
                cheat_institute_defense_timed_complete = world.get_location("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")
                world.set_rule(cheat_institute_defense_timed_complete, (HasAll("CI Defense - Agent", "RC-P120", "Data Uplink")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]))
                                                                       | (HasAll("CI Defense - Agent", "Data Uplink")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"])))


            if world.options.special_agent:
                # Defection
                cheat_defection_timed_complete = world.get_location("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
                world.set_rule(cheat_defection_timed_complete, HasAll("dD Defection - Special Agent", "ECM Mine") & HAS_DD_KEYS
                                                               & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))


                # Villa
                cheat_villa_timed_complete = world.get_location("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
                world.set_rule(cheat_villa_timed_complete, HasAll("Carrington Villa - Special Agent", "Cellar Key Card")
                                                           & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))


                # Infiltration
                cheat_infiltration_timed_complete = world.get_location("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
                world.set_rule(cheat_infiltration_timed_complete, HasAll("A51 Infiltration - Special Agent", "Explosives", "Comms Rider") & HAS_A51_INFIL_KEYS
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Air Base
                if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                    cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                    world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "Stewardess Disguise", "Suitcase")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                    cheat_air_base_timed_complete = world.get_location("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
                    world.set_rule(cheat_air_base_timed_complete, HasAll("Air Base - Special Agent", "CamSpy", "Stewardess Disguise", "Suitcase")
                                                                  & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))


                # Pelagic II
                cheat_pelagic_timed_complete = world.get_location("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
                world.set_rule(cheat_pelagic_timed_complete, HasAll("Pelagic II - Special Agent", "X-Ray Scanner")
                                                             & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Attack Ship
                cheat_attack_ship_timed_complete = world.get_location("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")
                world.set_rule(cheat_attack_ship_timed_complete, Has("Attack Ship - Special Agent")
                                                                 & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


            if world.options.perfect_agent:
                # Investigation
                cheat_investigation_timed_complete = world.get_location("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
                world.set_rule(cheat_investigation_timed_complete, (HasAll("dD Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                                   | (HasAll("dD Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item")
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"])))


                # Chicago
                cheat_chicago_timed_complete = world.get_location("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
                world.set_rule(cheat_chicago_timed_complete, (HasAll("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]))
                                                             | (HasAll("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug") 
                                                                & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"])))


                # Rescue
                cheat_rescue_timed_complete = world.get_location("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
                world.set_rule(cheat_rescue_timed_complete, HasAll("A51 Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes") & HAS_A51_RESCUE_ALL_KEYS
                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))


                # Air Force One
                cheat_air_force_one_timed_complete = world.get_location("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
                world.set_rule(cheat_air_force_one_timed_complete, (HasAll("Air Force One - Perfect Agent", "Suitcase", "Timed Mine") & HAS_AFO_LIFT_KEY
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
                                                                   | (HasAll("Air Force One - Perfect Agent", "Suitcase") & HAS_AFO_LIFT_KEY
                                                                        & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))


                # Deep Sea
                cheat_deep_sea_timed_complete = world.get_location("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
                world.set_rule(cheat_deep_sea_timed_complete, (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                              | (HasAll("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk")
                                                                    & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"])))


                # Skedar Ruins
                if world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                    cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                    world.set_rule(cheat_skedar_ruins_timed_complete, (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
                                                                      | (HAS_SKEDAR_RUINS_PF_AGENT & HasAll("R-Tracker", "Target Amplifier", "IR Scanner")
                                                                            & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"])))

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                    cheat_skedar_ruins_timed_complete = world.get_location("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
                    world.set_rule(cheat_skedar_ruins_timed_complete, HAS_SKEDAR_RUINS_PF_AGENT & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                                                      & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))


def set_all_extra_location_rules(world: PerfectDarkWorld) -> None:                      
    if world.options.weapon_progression.value == WeaponProgression.option_vanilla:
        if world.options.unlock_cheats & world.options.weapon_training:
            cheat_pp9i = world.get_location("Cheat Unlock: Get gold medals for Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)")
            world.set_rule(cheat_pp9i, HasAll("Falcon 2", "Falcon 2 (Silencer)", "Falcon 2 (Scope)"))

            cheat_cc13 = world.get_location("Cheat Unlock: Get gold medals for MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX")
            world.set_rule(cheat_cc13, HasAll("MagSec 4", "Mauler", "Phoenix", "DY357 Magnum", "DY357-LX"))

            cheat_kl01313 = world.get_location("Cheat Unlock: Get gold medals for CMP150, Cyclone, Callisto NTG, and RC-P120")
            world.set_rule(cheat_kl01313, HasAll("CMP150", "Cyclone", "Callisto NTG", "RC-P120"))

            cheat_kf7 = world.get_location("Cheat Unlock: Get gold medals for Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon")
            world.set_rule(cheat_kf7, HasAll("Laptop Gun", "Dragon", "K7 Avenger", "AR34", "SuperDragon"))

            cheat_zzt = world.get_location("Cheat Unlock: Get gold medals for Shotgun, Sniper Rifle, Rocket Launcher, and Slayer")
            world.set_rule(cheat_zzt, HasAll("Shotgun", "Sniper Rifle", "Rocket Launcher", "Slayer"))

            cheat_dmc = world.get_location("Cheat Unlock: Get gold medals for Timed Mine, Proximity Mine, and Remote Mine")
            world.set_rule(cheat_dmc, HasAll("Timed Mine", "Proximity Mine", "Remote Mine"))

            cheat_ar53 = world.get_location("Cheat Unlock: Get gold medals for FarSight XR-20, Crossbow, Combat Knife, and Grenade")
            world.set_rule(cheat_ar53, HasAll("FarSight XR-20", "Crossbow", "Combat Knife", "Grenade"))

            cheat_rcp45 = world.get_location("Cheat Unlock: Get gold medals for Tranquilizer, Reaper, and Devastator")
            world.set_rule(cheat_rcp45, HasAll("Tranquilizer", "Reaper", "Devastator"))

        if world.options.challenges:
            if world.options.challenge_logic.value == ChallengeLogic.option_strict:
                challenge_rules = {
                    "Challenge 1": HasAll("Challenge 1", "Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon"),
                    "Challenge 2": HasAll("Challenge 2", "Combat Knife", "Falcon 2", "Cyclone", "Dragon", "Rocket Launcher"),
                    "Challenge 3": HasAll("Challenge 3", "MagSec 4", "CMP150", "Timed Mine", "Dragon", "AR34"),
                    "Challenge 4": HasAll("Challenge 4", "MagSec 4", "CMP150", "Dragon", "K7 Avenger", "Shield"),
                    "Challenge 5": HasAll("Challenge 5", "Cyclone", "Grenade", "AR34", "FarSight XR-20", "Shield"),
                    "Challenge 6": HasAll("Challenge 6", "Briefcase", "CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger", "Shield"),
                    "Challenge 7": HasAll("Challenge 7", "Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade", "Shield"),
                    "Challenge 8": HasAll("Challenge 8", "Briefcase", "MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon", "Shield"),
                    "Challenge 9": HasAll("Challenge 9", "Falcon 2", "DY357 Magnum", "Timed Mine", "Laptop Gun", "FarSight XR-20"),
                    "Challenge 10": HasAll("Challenge 10", "Data Uplink", "CMP150", "Cyclone", "Remote Mine", "AR34", "Shield"),
                    "Challenge 11": HasAll("Challenge 11", "MagSec 4", "Tranquilizer", "Shotgun", "K7 Avenger", "Shield"),
                    "Challenge 12": HasAll("Challenge 12", "Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon", "Shield"),
                    "Challenge 13": HasAll("Challenge 13", "Falcon 2 (Silencer)", "Tranquilizer", "Laptop Gun", "Grenade", "Reaper"),
                    "Challenge 14": HasAll("Challenge 14", "Briefcase", "Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20", "Cloaking Device"),
                    "Challenge 15": HasAll("Challenge 15", "Briefcase", "MagSec 4", "Dragon", "Shotgun", "Devastator", "Shield"),
                    "Challenge 16": HasAll("Challenge 16", "Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine", "Shield"),
                    "Challenge 17": HasAll("Challenge 17", "DY357 Magnum", "AR34", "Reaper", "Slayer", "Shield"),
                    "Challenge 18": HasAll("Challenge 18", "Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun", "Shield", "Cloaking Device"),
                    "Challenge 19": HasAll("Challenge 19", "CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20", "Shield", "Combat Boost"),
                    "Challenge 20": HasAll("Challenge 20", "Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum", "Shield"),
                    "Challenge 21": HasAll("Challenge 21", "Data Uplink", "Mauler", "Reaper", "Shotgun", "Callisto NTG", "Cloaking Device"),
                    "Challenge 22": HasAll("Challenge 22", "Briefcase", "Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger", "Shield"),
                    "Challenge 23": HasAll("Challenge 23", "MagSec 4", "Grenade", "Laptop Gun", "RC-P120", "Shield", "Combat Boost"),
                    "Challenge 24": HasAll("Challenge 24", "Briefcase", "CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX"),
                    "Challenge 25": HasAll("Challenge 25", "Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20", "Cloaking Device"),
                    "Challenge 26": HasAll("Challenge 26", "Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper"),
                    "Challenge 27": HasAll("Challenge 27", "Data Uplink", "Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher", "Shield"),
                    "Challenge 28": HasAll("Challenge 28", "Briefcase", "Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun"),
                    "Challenge 29": HasAll("Challenge 29", "Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon"),
                    "Challenge 30": HasAll("Challenge 30", "Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum"),
                }

                add_challenge_rules(world, challenge_rules)


            elif world.options.challenge_logic.value == ChallengeLogic.option_normal:
                challenge_rules = {
                    "Challenge 1": Has("Challenge 1") & HasAny("Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon"),
                    "Challenge 2": HasAll("Challenge 2", "Rocket Launcher"),
                    "Challenge 3": HasAll("Challenge 3", "Timed Mine", "Dragon", "AR34"),
                    "Challenge 4": HasAll("Challenge 4", "K7 Avenger", "Shield"),
                    "Challenge 5": HasAll("Challenge 5", "FarSight XR-20"),
                    "Challenge 6": HasAll("Challenge 6", "Briefcase") & HasAny("CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger"),
                    "Challenge 7": Has("Challenge 7") & HasAny("Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade"),
                    "Challenge 8": HasAll("Challenge 8", "Briefcase") & HasAny("MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon"),
                    "Challenge 9": HasAll("Challenge 9", "FarSight XR-20", "Laptop Gun"),
                    "Challenge 10": HasAll("Challenge 10", "Data Uplink") & HasAny("CMP150", "Cyclone", "Remote Mine", "AR34"),
                    "Challenge 11": HasAll("Challenge 11", "Shotgun", "Tranquilizer"),
                    "Challenge 12": Has("Challenge 12") & HasAny("Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon"),
                    "Challenge 13": HasAll("Challenge 13", "Tranquilizer"),
                    "Challenge 14": HasAll("Challenge 14", "Briefcase", "Cloaking Device") & HasAny("Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20"),
                    "Challenge 15": HasAll("Challenge 15", "Briefcase", "Devastator"),
                    "Challenge 16": HasAll("Challenge 16", "Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine", "Shield"),
                    "Challenge 17": HasAll("Challenge 17", "DY357 Magnum", "AR34", "Reaper", "Slayer", "Shield"),
                    "Challenge 18": HasAll("Challenge 18", "Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun", "Shield", "Cloaking Device"),
                    "Challenge 19": HasAll("Challenge 19", "CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20", "Shield"),
                    "Challenge 20": HasAll("Challenge 20", "Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum", "Shield"),
                    "Challenge 21": HasAll("Challenge 21", "Data Uplink", "Mauler", "Reaper", "Shotgun", "Callisto NTG", "Cloaking Device"),
                    "Challenge 22": HasAll("Challenge 22", "Briefcase", "Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger", "Shield"),
                    "Challenge 23": HasAll("Challenge 23", "MagSec 4", "Grenade", "Laptop Gun", "RC-P120", "Shield"),
                    "Challenge 24": HasAll("Challenge 24", "Briefcase", "CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX"),
                    "Challenge 25": HasAll("Challenge 25", "Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20", "Cloaking Device"),
                    "Challenge 26": HasAll("Challenge 26", "Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper"),
                    "Challenge 27": HasAll("Challenge 27", "Data Uplink", "Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher", "Shield"),
                    "Challenge 28": HasAll("Challenge 28", "Briefcase", "Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun"),
                    "Challenge 29": HasAll("Challenge 29", "Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon"),
                    "Challenge 30": HasAll("Challenge 30", "Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum"),
                }

                add_challenge_rules(world, challenge_rules)


            elif world.options.challenge_logic.value == ChallengeLogic.option_hard:
                challenge_rules = {
                    "Challenge 1": Has("Challenge 1") & HasAny("Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon"),
                    "Challenge 2": Has("Challenge 2") & HasAny("Combat Knife", "Falcon 2", "Cyclone", "Dragon", "Rocket Launcher"),
                    "Challenge 3": Has("Challenge 3") & HasAny("MagSec 4", "CMP150", "Timed Mine", "Dragon", "AR34"),
                    "Challenge 4": Has("Challenge 4") & HasAny("MagSec 4", "CMP150", "Dragon", "K7 Avenger"),
                    "Challenge 5": Has("Challenge 5") & HasAny("Cyclone", "Grenade", "AR34", "FarSight XR-20"),
                    "Challenge 6": HasAll("Challenge 6", "Briefcase") & HasAny("CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger"),
                    "Challenge 7": Has("Challenge 7") & HasAny("Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade"),
                    "Challenge 8": HasAll("Challenge 8", "Briefcase") & HasAny("MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon"),
                    "Challenge 9": Has("Challenge 9") & HasAny("Falcon 2", "DY357 Magnum", "Timed Mine", "Laptop Gun", "FarSight XR-20"),
                    "Challenge 10": HasAll("Challenge 10", "Data Uplink") & HasAny("CMP150", "Cyclone", "Remote Mine", "AR34"),
                    "Challenge 11": Has("Challenge 11") & HasAny("MagSec 4", "Tranquilizer", "Shotgun", "K7 Avenger"),
                    "Challenge 12": Has("Challenge 12") & HasAny("Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon"),
                    "Challenge 13": Has("Challenge 13") & HasAny("Falcon 2 (Silencer)", "Tranquilizer", "Laptop Gun", "Grenade", "Reaper"),
                    "Challenge 14": HasAll("Challenge 14", "Briefcase") & HasAny("Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20"),
                    "Challenge 15": HasAll("Challenge 15", "Briefcase") & HasAny("MagSec 4", "Dragon", "Shotgun", "Devastator"),
                    "Challenge 16": Has("Challenge 16") & HasAny("Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine"),
                    "Challenge 17": Has("Challenge 17") & HasAny("DY357 Magnum", "AR34", "Reaper", "Slayer"),
                    "Challenge 18": Has("Challenge 18") & HasAny("Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun"),
                    "Challenge 19": Has("Challenge 19") & HasAny("CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20"),
                    "Challenge 20": Has("Challenge 20") & HasAny("Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum"),
                    "Challenge 21": HasAll("Challenge 21", "Data Uplink") & HasAny("Mauler", "Reaper", "Shotgun", "Callisto NTG"),
                    "Challenge 22": HasAll("Challenge 22", "Briefcase") & HasAny("Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger"),
                    "Challenge 23": Has("Challenge 23") & HasAny("MagSec 4", "Grenade", "Laptop Gun", "RC-P120"),
                    "Challenge 24": HasAll("Challenge 24", "Briefcase") & HasAny("CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX"),
                    "Challenge 25": Has("Challenge 25") & HasAny("Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20"),
                    "Challenge 26": Has("Challenge 26") & HasAny("Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper"),
                    "Challenge 27": HasAll("Challenge 27", "Data Uplink") & HasAny("Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher"),
                    "Challenge 28": HasAll("Challenge 28", "Briefcase") & HasAny("Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun"),
                    "Challenge 29": Has("Challenge 29") & HasAny("Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon"),
                    "Challenge 30": Has("Challenge 30") & HasAny("Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum"),
                }

                add_challenge_rules(world, challenge_rules)


        if world.options.weapon_training:
            falcon2_bronze = world.get_location("Firing Range: Falcon 2 - Bronze")
            world.set_rule(falcon2_bronze, Has("Falcon 2"))
            
            falcon2_silver = world.get_location("Firing Range: Falcon 2 - Silver")
            world.set_rule(falcon2_silver, Has("Falcon 2"))
            
            falcon2_gold = world.get_location("Firing Range: Falcon 2 - Gold")
            world.set_rule(falcon2_gold, Has("Falcon 2"))
            
            falcon2silencer_bronze = world.get_location("Firing Range: Falcon 2 (Silencer) - Bronze")
            world.set_rule(falcon2silencer_bronze, Has("Falcon 2 (Silencer)"))
            
            falcon2silencer_silver = world.get_location("Firing Range: Falcon 2 (Silencer) - Silver")
            world.set_rule(falcon2silencer_silver, Has("Falcon 2 (Silencer)"))
            
            falcon2silencer_gold = world.get_location("Firing Range: Falcon 2 (Silencer) - Gold")
            world.set_rule(falcon2silencer_gold, Has("Falcon 2 (Silencer)"))
            
            falcon2scope_bronze = world.get_location("Firing Range: Falcon 2 (Scope) - Bronze")
            world.set_rule(falcon2scope_bronze, Has("Falcon 2 (Scope)"))
            
            falcon2scope_silver = world.get_location("Firing Range: Falcon 2 (Scope) - Silver")
            world.set_rule(falcon2scope_silver, Has("Falcon 2 (Scope)"))
            
            falcon2scope_gold = world.get_location("Firing Range: Falcon 2 (Scope) - Gold")
            world.set_rule(falcon2scope_gold, Has("Falcon 2 (Scope)"))
            
            magsec4_bronze = world.get_location("Firing Range: MagSec 4 - Bronze")
            world.set_rule(magsec4_bronze, Has("MagSec 4"))
            
            magsec4_silver = world.get_location("Firing Range: MagSec 4 - Silver")
            world.set_rule(magsec4_silver, Has("MagSec 4"))
            
            magsec4_gold = world.get_location("Firing Range: MagSec 4 - Gold")
            world.set_rule(magsec4_gold, Has("MagSec 4"))
            
            mauler_bronze = world.get_location("Firing Range: Mauler - Bronze")
            world.set_rule(mauler_bronze, Has("Mauler"))
            
            mauler_silver = world.get_location("Firing Range: Mauler - Silver")
            world.set_rule(mauler_silver, Has("Mauler"))
            
            mauler_gold = world.get_location("Firing Range: Mauler - Gold")
            world.set_rule(mauler_gold, Has("Mauler"))
            
            phoenix_bronze = world.get_location("Firing Range: Phoenix - Bronze")
            world.set_rule(phoenix_bronze, Has("Phoenix"))
            
            phoenix_silver = world.get_location("Firing Range: Phoenix - Silver")
            world.set_rule(phoenix_silver, Has("Phoenix"))
            
            phoenix_gold = world.get_location("Firing Range: Phoenix - Gold")
            world.set_rule(phoenix_gold, Has("Phoenix"))
            
            dy357magnum_bronze = world.get_location("Firing Range: DY357 Magnum - Bronze")
            world.set_rule(dy357magnum_bronze, Has("DY357 Magnum"))
            
            dy357magnum_silver = world.get_location("Firing Range: DY357 Magnum - Silver")
            world.set_rule(dy357magnum_silver, Has("DY357 Magnum"))
            
            dy357magnum_gold = world.get_location("Firing Range: DY357 Magnum - Gold")
            world.set_rule(dy357magnum_gold, Has("DY357 Magnum"))
            
            dy357lx_bronze = world.get_location("Firing Range: DY357-LX - Bronze")
            world.set_rule(dy357lx_bronze, Has("DY357-LX"))
            
            dy357lx_silver = world.get_location("Firing Range: DY357-LX - Silver")
            world.set_rule(dy357lx_silver, Has("DY357-LX"))
            
            dy357lx_gold = world.get_location("Firing Range: DY357-LX - Gold")
            world.set_rule(dy357lx_gold, Has("DY357-LX"))
            
            cmp150_bronze = world.get_location("Firing Range: CMP150 - Bronze")
            world.set_rule(cmp150_bronze, Has("CMP150"))
            
            cmp150_silver = world.get_location("Firing Range: CMP150 - Silver")
            world.set_rule(cmp150_silver, Has("CMP150"))
            
            cmp150_gold = world.get_location("Firing Range: CMP150 - Gold")
            world.set_rule(cmp150_gold, Has("CMP150"))
            
            cyclone_bronze = world.get_location("Firing Range: Cyclone - Bronze")
            world.set_rule(cyclone_bronze, Has("Cyclone"))
            
            cyclone_silver = world.get_location("Firing Range: Cyclone - Silver")
            world.set_rule(cyclone_silver, Has("Cyclone"))
            
            cyclone_gold = world.get_location("Firing Range: Cyclone - Gold")
            world.set_rule(cyclone_gold, Has("Cyclone"))
            
            callisto_bronze = world.get_location("Firing Range: Callisto NTG - Bronze")
            world.set_rule(callisto_bronze, Has("Callisto NTG"))
            
            callisto_silver = world.get_location("Firing Range: Callisto NTG - Silver")
            world.set_rule(callisto_silver, Has("Callisto NTG"))
            
            callisto_gold = world.get_location("Firing Range: Callisto NTG - Gold")
            world.set_rule(callisto_gold, Has("Callisto NTG"))
            
            rcp120_bronze = world.get_location("Firing Range: RC-P120 - Bronze")
            world.set_rule(rcp120_bronze, Has("RC-P120"))
            
            rcp120_silver = world.get_location("Firing Range: RC-P120 - Silver")
            world.set_rule(rcp120_silver, Has("RC-P120"))
            
            rcp120_gold = world.get_location("Firing Range: RC-P120 - Gold")
            world.set_rule(rcp120_gold, Has("RC-P120"))
            
            laptopgun_bronze = world.get_location("Firing Range: Laptop Gun - Bronze")
            world.set_rule(laptopgun_bronze, Has("Laptop Gun"))
            
            laptopgun_silver = world.get_location("Firing Range: Laptop Gun - Silver")
            world.set_rule(laptopgun_silver, Has("Laptop Gun"))
            
            laptopgun_gold = world.get_location("Firing Range: Laptop Gun - Gold")
            world.set_rule(laptopgun_gold, Has("Laptop Gun"))
            
            dragon_bronze = world.get_location("Firing Range: Dragon - Bronze")
            world.set_rule(dragon_bronze, Has("Dragon"))
            
            dragon_silver = world.get_location("Firing Range: Dragon - Silver")
            world.set_rule(dragon_silver, Has("Dragon"))
            
            dragon_gold = world.get_location("Firing Range: Dragon - Gold")
            world.set_rule(dragon_gold, Has("Dragon"))
            
            k7avenger_bronze = world.get_location("Firing Range: K7 Avenger - Bronze")
            world.set_rule(k7avenger_bronze, Has("K7 Avenger"))
            
            k7avenger_silver = world.get_location("Firing Range: K7 Avenger - Silver")
            world.set_rule(k7avenger_silver, Has("K7 Avenger"))
            
            k7avenger_gold = world.get_location("Firing Range: K7 Avenger - Gold")
            world.set_rule(k7avenger_gold, Has("K7 Avenger"))
            
            ar34_bronze = world.get_location("Firing Range: AR34 - Bronze")
            world.set_rule(ar34_bronze, Has("AR34"))
            
            ar34_silver = world.get_location("Firing Range: AR34 - Silver")
            world.set_rule(ar34_silver, Has("AR34"))
            
            ar34_gold = world.get_location("Firing Range: AR34 - Gold")
            world.set_rule(ar34_gold, Has("AR34"))
            
            superdragon_bronze = world.get_location("Firing Range: SuperDragon - Bronze")
            world.set_rule(superdragon_bronze, Has("SuperDragon"))
            
            superdragon_silver = world.get_location("Firing Range: SuperDragon - Silver")
            world.set_rule(superdragon_silver, Has("SuperDragon"))
            
            superdragon_gold = world.get_location("Firing Range: SuperDragon - Gold")
            world.set_rule(superdragon_gold, Has("SuperDragon"))
            
            shotgun_bronze = world.get_location("Firing Range: Shotgun - Bronze")
            world.set_rule(shotgun_bronze, Has("Shotgun"))
            
            shotgun_silver = world.get_location("Firing Range: Shotgun - Silver")
            world.set_rule(shotgun_silver, Has("Shotgun"))
            
            shotgun_gold = world.get_location("Firing Range: Shotgun - Gold")
            world.set_rule(shotgun_gold, Has("Shotgun"))
            
            reaper_bronze = world.get_location("Firing Range: Reaper - Bronze")
            world.set_rule(reaper_bronze, Has("Reaper"))
            
            reaper_silver = world.get_location("Firing Range: Reaper - Silver")
            world.set_rule(reaper_silver, Has("Reaper"))
            
            reaper_gold = world.get_location("Firing Range: Reaper - Gold")
            world.set_rule(reaper_gold, Has("Reaper"))
            
            sniperrifle_bronze = world.get_location("Firing Range: Sniper Rifle - Bronze")
            world.set_rule(sniperrifle_bronze, Has("Sniper Rifle"))
            
            sniperrifle_silver = world.get_location("Firing Range: Sniper Rifle - Silver")
            world.set_rule(sniperrifle_silver, Has("Sniper Rifle"))
            
            sniperrifle_gold = world.get_location("Firing Range: Sniper Rifle - Gold")
            world.set_rule(sniperrifle_gold, Has("Sniper Rifle"))
            
            farsight_bronze = world.get_location("Firing Range: FarSight XR-20 - Bronze")
            world.set_rule(farsight_bronze, Has("FarSight XR-20"))
            
            farsight_silver = world.get_location("Firing Range: FarSight XR-20 - Silver")
            world.set_rule(farsight_silver, Has("FarSight XR-20"))
            
            farsight_gold = world.get_location("Firing Range: FarSight XR-20 - Gold")
            world.set_rule(farsight_gold, Has("FarSight XR-20"))
            
            devastator_bronze = world.get_location("Firing Range: Devastator - Bronze")
            world.set_rule(devastator_bronze, Has("Devastator"))
            
            devastator_silver = world.get_location("Firing Range: Devastator - Silver")
            world.set_rule(devastator_silver, Has("Devastator"))
            
            devastator_gold = world.get_location("Firing Range: Devastator - Gold")
            world.set_rule(devastator_gold, Has("Devastator"))
            
            rocketlauncher_bronze = world.get_location("Firing Range: Rocket Launcher - Bronze")
            world.set_rule(rocketlauncher_bronze, Has("Rocket Launcher"))
            
            rocketlauncher_silver = world.get_location("Firing Range: Rocket Launcher - Silver")
            world.set_rule(rocketlauncher_silver, Has("Rocket Launcher"))
            
            rocketlauncher_gold = world.get_location("Firing Range: Rocket Launcher - Gold")
            world.set_rule(rocketlauncher_gold, Has("Rocket Launcher"))
            
            slayer_bronze = world.get_location("Firing Range: Slayer - Bronze")
            world.set_rule(slayer_bronze, Has("Slayer"))
            
            slayer_silver = world.get_location("Firing Range: Slayer - Silver")
            world.set_rule(slayer_silver, Has("Slayer"))
            
            slayer_gold = world.get_location("Firing Range: Slayer - Gold")
            world.set_rule(slayer_gold, Has("Slayer"))
            
            knife_bronze = world.get_location("Firing Range: Combat Knife - Bronze")
            world.set_rule(knife_bronze, Has("Combat Knife"))
            
            knife_silver = world.get_location("Firing Range: Combat Knife - Silver")
            world.set_rule(knife_silver, Has("Combat Knife"))
            
            knife_gold = world.get_location("Firing Range: Combat Knife - Gold")
            world.set_rule(knife_gold, Has("Combat Knife"))
            
            crossbow_bronze = world.get_location("Firing Range: Crossbow - Bronze")
            world.set_rule(crossbow_bronze, Has("Crossbow"))
            
            crossbow_silver = world.get_location("Firing Range: Crossbow - Silver")
            world.set_rule(crossbow_silver, Has("Crossbow"))
            
            crossbow_gold = world.get_location("Firing Range: Crossbow - Gold")
            world.set_rule(crossbow_gold, Has("Crossbow"))
            
            tranquilizer_bronze = world.get_location("Firing Range: Tranquilizer - Bronze")
            world.set_rule(tranquilizer_bronze, Has("Tranquilizer"))
            
            tranquilizer_silver = world.get_location("Firing Range: Tranquilizer - Silver")
            world.set_rule(tranquilizer_silver, Has("Tranquilizer"))
            
            tranquilizer_gold = world.get_location("Firing Range: Tranquilizer - Gold")
            world.set_rule(tranquilizer_gold, Has("Tranquilizer"))
            
            laser_bronze = world.get_location("Firing Range: Laser - Bronze")
            world.set_rule(laser_bronze, Has("Laser"))
            
            laser_silver = world.get_location("Firing Range: Laser - Silver")
            world.set_rule(laser_silver, Has("Laser"))
            
            laser_gold = world.get_location("Firing Range: Laser - Gold")
            world.set_rule(laser_gold, Has("Laser"))
            
            grenade_bronze = world.get_location("Firing Range: Grenade - Bronze")
            world.set_rule(grenade_bronze, Has("Grenade"))
            
            grenade_silver = world.get_location("Firing Range: Grenade - Silver")
            world.set_rule(grenade_silver, Has("Grenade"))
            
            grenade_gold = world.get_location("Firing Range: Grenade - Gold")
            world.set_rule(grenade_gold, Has("Grenade"))
            
            timedmine_bronze = world.get_location("Firing Range: Timed Mine - Bronze")
            world.set_rule(timedmine_bronze, Has("Timed Mine"))
            
            timedmine_silver = world.get_location("Firing Range: Timed Mine - Silver")
            world.set_rule(timedmine_silver, Has("Timed Mine"))
            
            timedmine_gold = world.get_location("Firing Range: Timed Mine - Gold")
            world.set_rule(timedmine_gold, Has("Timed Mine"))
            
            proximitymine_bronze = world.get_location("Firing Range: Proximity Mine - Bronze")
            world.set_rule(proximitymine_bronze, Has("Proximity Mine"))
            
            proximitymine_silver = world.get_location("Firing Range: Proximity Mine - Silver")
            world.set_rule(proximitymine_silver, Has("Proximity Mine"))
            
            proximitymine_gold = world.get_location("Firing Range: Proximity Mine - Gold")
            world.set_rule(proximitymine_gold, Has("Proximity Mine"))
            
            remotemine_bronze = world.get_location("Firing Range: Remote Mine - Bronze")
            world.set_rule(remotemine_bronze, Has("Remote Mine"))
            
            remotemine_silver = world.get_location("Firing Range: Remote Mine - Silver")
            world.set_rule(remotemine_silver, Has("Remote Mine"))
            
            remotemine_gold = world.get_location("Firing Range: Remote Mine - Gold")
            world.set_rule(remotemine_gold, Has("Remote Mine"))


        if world.options.holotraining:
            dt_data_uplink = world.get_location("Holotraining 7: Live Combat 2")
            world.set_rule(dt_data_uplink, Has("Falcon 2"))

    elif world.options.weapon_progression.value > WeaponProgression.option_vanilla:
        if world.options.unlock_cheats & world.options.weapon_training:
            cheat_pp9i = world.get_location("Cheat Unlock: Get gold medals for Falcon 2, Falcon 2 (Silencer), & Falcon 2 (Scope)")
            world.set_rule(cheat_pp9i, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"]))

            cheat_cc13 = world.get_location("Cheat Unlock: Get gold medals for MagSec 4, Mauler, Phoenix, DY357 Magnum, & DY357-LX")
            world.set_rule(cheat_cc13, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]))

            cheat_kl01313 = world.get_location("Cheat Unlock: Get gold medals for CMP150, Cyclone, Callisto NTG, & RC-P120")
            world.set_rule(cheat_kl01313, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))

            cheat_kf7 = world.get_location("Cheat Unlock: Get gold medals for Laptop Gun, Dragon, K7 Avenger, AR34, & SuperDragon")
            world.set_rule(cheat_kf7, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]))

            cheat_zzt = world.get_location("Cheat Unlock: Get gold medals for Shotgun, Sniper Rifle, Rocket Launcher, & Slayer")
            world.set_rule(cheat_zzt, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]))

            cheat_dmc = world.get_location("Cheat Unlock: Get gold medals for Timed Mine, Proximity Mine, & Remote Mine")
            world.set_rule(cheat_dmc, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))

            cheat_ar53 = world.get_location("Cheat Unlock: Get gold medals for FarSight XR-20, Crossbow, Combat Knife, & Grenade")
            world.set_rule(cheat_ar53, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))

            cheat_rcp45 = world.get_location("Cheat Unlock: Get gold medals for Tranquilizer, Reaper, & Devastator")
            world.set_rule(cheat_rcp45, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]))

        if world.options.challenges:
            if world.options.challenge_logic.value == ChallengeLogic.option_strict:
                challenge_rules = {
                    "Challenge 1": Has("Challenge 1") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]),
                    "Challenge 2": Has("Challenge 2") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]),
                    "Challenge 3": Has("Challenge 3") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]),
                    "Challenge 4": HasAll("Challenge 4", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 5": HasAll("Challenge 5", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 6": HasAll("Challenge 6", "Briefcase", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 7": HasAll("Challenge 7", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]),
                    "Challenge 8": HasAll("Challenge 8", "Briefcase", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]),
                    "Challenge 9": Has("Challenge 9") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 10": HasAll("Challenge 10", "Data Uplink", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]),
                    "Challenge 11": HasAll("Challenge 11", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 12": HasAll("Challenge 12", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]),
                    "Challenge 13": Has("Challenge 13") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]),
                    "Challenge 14": HasAll("Challenge 14", "Briefcase", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 15": HasAll("Challenge 15", "Briefcase", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]),
                    "Challenge 16": HasAll("Challenge 16", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]),
                    "Challenge 17": HasAll("Challenge 17", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]),
                    "Challenge 18": HasAll("Challenge 18", "Shield", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]),
                    "Challenge 19": HasAll("Challenge 19", "Shield", "Combat Boost") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 20": HasAll("Challenge 20", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                    "Challenge 21": HasAll("Challenge 21", "Data Uplink", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                    "Challenge 22": HasAll("Challenge 22", "Briefcase", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 23": HasAll("Challenge 23", "Shield", "Combat Boost") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]),
                    "Challenge 24": HasAll("Challenge 24", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]),
                    "Challenge 25": HasAll("Challenge 25", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 26": Has("Challenge 26") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                    "Challenge 27": HasAll("Challenge 27", "Data Uplink", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]),
                    "Challenge 28": HasAll("Challenge 28", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]),
                    "Challenge 29": Has("Challenge 29") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]),
                    "Challenge 30": Has("Challenge 30") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                }

                add_challenge_rules(world, challenge_rules)


            elif world.options.challenge_logic.value == ChallengeLogic.option_normal:
                challenge_rules = {
                    "Challenge 1": Has("Challenge 1") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]),
                    "Challenge 2": Has("Challenge 2") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]),
                    "Challenge 3": Has("Challenge 3") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]),
                    "Challenge 4": HasAll("Challenge 4", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 5": Has("Challenge 5") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 6": HasAll("Challenge 6", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 7": Has("Challenge 7") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]),
                    "Challenge 8": HasAll("Challenge 8", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]),
                    "Challenge 9": Has("Challenge 9") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 10": HasAll("Challenge 10", "Data Uplink") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]),
                    "Challenge 11": Has("Challenge 11") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]),
                    "Challenge 12": Has("Challenge 12") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]),
                    "Challenge 13": Has("Challenge 13") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]),
                    "Challenge 14": HasAll("Challenge 14", "Briefcase", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 15": HasAll("Challenge 15", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]),
                    "Challenge 16": HasAll("Challenge 16", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]),
                    "Challenge 17": HasAll("Challenge 17", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]),
                    "Challenge 18": HasAll("Challenge 18", "Shield", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]),
                    "Challenge 19": HasAll("Challenge 19", "Shield", "Combat Boost") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 20": HasAll("Challenge 20", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                    "Challenge 21": HasAll("Challenge 21", "Data Uplink", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                    "Challenge 22": HasAll("Challenge 22", "Briefcase", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]),
                    "Challenge 23": HasAll("Challenge 23", "Shield", "Combat Boost") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]),
                    "Challenge 24": HasAll("Challenge 24", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]),
                    "Challenge 25": HasAll("Challenge 25", "Cloaking Device") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]),
                    "Challenge 26": Has("Challenge 26") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                    "Challenge 27": HasAll("Challenge 27", "Data Uplink", "Shield") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]),
                    "Challenge 28": HasAll("Challenge 28", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]),
                    "Challenge 29": Has("Challenge 29") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]),
                    "Challenge 30": Has("Challenge 30") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]),
                }

                add_challenge_rules(world, challenge_rules)
            

            elif world.options.challenge_logic.value == ChallengeLogic.option_hard:
                challenge_rules = {
                    "Challenge 1": Has("Challenge 1") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]),
                    "Challenge 2": Has("Challenge 2") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]),
                    "Challenge 3": Has("Challenge 3") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]),
                    "Challenge 4": Has("Challenge 4") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]),
                    "Challenge 5": Has("Challenge 5") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]),
                    "Challenge 6": HasAll("Challenge 6", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]),
                    "Challenge 7": Has("Challenge 7") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"]),
                    "Challenge 8": HasAll("Challenge 8", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]),
                    "Challenge 9": Has("Challenge 9") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 10": HasAll("Challenge 10", "Data Uplink") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"]),
                    "Challenge 11": Has("Challenge 11") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]),
                    "Challenge 12": Has("Challenge 12") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]),
                    "Challenge 13": Has("Challenge 13") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]),
                    "Challenge 14": HasAll("Challenge 14", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]),
                    "Challenge 15": HasAll("Challenge 15", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]),
                    "Challenge 16": Has("Challenge 16") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 17": Has("Challenge 17") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]),
                    "Challenge 18": Has("Challenge 18") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]),
                    "Challenge 19": Has("Challenge 19") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]),
                    "Challenge 20": Has("Challenge 20") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 21": HasAll("Challenge 21", "Data Uplink") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]),
                    "Challenge 22": HasAll("Challenge 22", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"]),
                    "Challenge 23": Has("Challenge 23") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]),
                    "Challenge 24": HasAll("Challenge 24", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]),
                    "Challenge 25": Has("Challenge 25") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["N-Bomb"]),
                    "Challenge 26": Has("Challenge 26") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 27": HasAll("Challenge 27", "Data Uplink") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 28": HasAll("Challenge 28", "Briefcase") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 29": Has("Challenge 29") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                    "Challenge 30": Has("Challenge 30") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]),
                }

                add_challenge_rules(world, challenge_rules)

            
        if world.options.weapon_training:
            falcon2_bronze = world.get_location("Firing Range: Falcon 2 - Bronze")
            world.set_rule(falcon2_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            falcon2_silver = world.get_location("Firing Range: Falcon 2 - Silver")
            world.set_rule(falcon2_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            falcon2_gold = world.get_location("Firing Range: Falcon 2 - Gold")
            world.set_rule(falcon2_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))
            
            falcon2silencer_bronze = world.get_location("Firing Range: Falcon 2 (Silencer) - Bronze")
            world.set_rule(falcon2silencer_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"]))
            
            falcon2silencer_silver = world.get_location("Firing Range: Falcon 2 (Silencer) - Silver")
            world.set_rule(falcon2silencer_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"]))
            
            falcon2silencer_gold = world.get_location("Firing Range: Falcon 2 (Silencer) - Gold")
            world.set_rule(falcon2silencer_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"]))
            
            falcon2scope_bronze = world.get_location("Firing Range: Falcon 2 (Scope) - Bronze")
            world.set_rule(falcon2scope_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"]))
            
            falcon2scope_silver = world.get_location("Firing Range: Falcon 2 (Scope) - Silver")
            world.set_rule(falcon2scope_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"]))
            
            falcon2scope_gold = world.get_location("Firing Range: Falcon 2 (Scope) - Gold")
            world.set_rule(falcon2scope_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Scope)"]))
            
            magsec4_bronze = world.get_location("Firing Range: MagSec 4 - Bronze")
            world.set_rule(magsec4_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]))
            
            magsec4_silver = world.get_location("Firing Range: MagSec 4 - Silver")
            world.set_rule(magsec4_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]))
            
            magsec4_gold = world.get_location("Firing Range: MagSec 4 - Gold")
            world.set_rule(magsec4_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]))
            
            mauler_bronze = world.get_location("Firing Range: Mauler - Bronze")
            world.set_rule(mauler_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]))
            
            mauler_silver = world.get_location("Firing Range: Mauler - Silver")
            world.set_rule(mauler_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]))
            
            mauler_gold = world.get_location("Firing Range: Mauler - Gold")
            world.set_rule(mauler_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]))
            
            phoenix_bronze = world.get_location("Firing Range: Phoenix - Bronze")
            world.set_rule(phoenix_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]))
            
            phoenix_silver = world.get_location("Firing Range: Phoenix - Silver")
            world.set_rule(phoenix_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]))
            
            phoenix_gold = world.get_location("Firing Range: Phoenix - Gold")
            world.set_rule(phoenix_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]))
            
            dy357magnum_bronze = world.get_location("Firing Range: DY357 Magnum - Bronze")
            world.set_rule(dy357magnum_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]))
            
            dy357magnum_silver = world.get_location("Firing Range: DY357 Magnum - Silver")
            world.set_rule(dy357magnum_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]))
            
            dy357magnum_gold = world.get_location("Firing Range: DY357 Magnum - Gold")
            world.set_rule(dy357magnum_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]))
            
            dy357lx_bronze = world.get_location("Firing Range: DY357-LX - Bronze")
            world.set_rule(dy357lx_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]))
            
            dy357lx_silver = world.get_location("Firing Range: DY357-LX - Silver")
            world.set_rule(dy357lx_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]))
            
            dy357lx_gold = world.get_location("Firing Range: DY357-LX - Gold")
            world.set_rule(dy357lx_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]))
            
            cmp150_bronze = world.get_location("Firing Range: CMP150 - Bronze")
            world.set_rule(cmp150_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"]))
            
            cmp150_silver = world.get_location("Firing Range: CMP150 - Silver")
            world.set_rule(cmp150_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"]))
            
            cmp150_gold = world.get_location("Firing Range: CMP150 - Gold")
            world.set_rule(cmp150_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"]))
            
            cyclone_bronze = world.get_location("Firing Range: Cyclone - Bronze")
            world.set_rule(cyclone_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]))
            
            cyclone_silver = world.get_location("Firing Range: Cyclone - Silver")
            world.set_rule(cyclone_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]))
            
            cyclone_gold = world.get_location("Firing Range: Cyclone - Gold")
            world.set_rule(cyclone_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]))
            
            callisto_bronze = world.get_location("Firing Range: Callisto NTG - Bronze")
            world.set_rule(callisto_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Callisto NTG"]))
            
            callisto_silver = world.get_location("Firing Range: Callisto NTG - Silver")
            world.set_rule(callisto_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Callisto NTG"]))
            
            callisto_gold = world.get_location("Firing Range: Callisto NTG - Gold")
            world.set_rule(callisto_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Callisto NTG"]))
            
            rcp120_bronze = world.get_location("Firing Range: RC-P120 - Bronze")
            world.set_rule(rcp120_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
            
            rcp120_silver = world.get_location("Firing Range: RC-P120 - Silver")
            world.set_rule(rcp120_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
            
            rcp120_gold = world.get_location("Firing Range: RC-P120 - Gold")
            world.set_rule(rcp120_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]))
            
            laptopgun_bronze = world.get_location("Firing Range: Laptop Gun - Bronze")
            world.set_rule(laptopgun_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"]))
            
            laptopgun_silver = world.get_location("Firing Range: Laptop Gun - Silver")
            world.set_rule(laptopgun_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"]))
            
            laptopgun_gold = world.get_location("Firing Range: Laptop Gun - Gold")
            world.set_rule(laptopgun_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laptop Gun"]))
            
            dragon_bronze = world.get_location("Firing Range: Dragon - Bronze")
            world.set_rule(dragon_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
            
            dragon_silver = world.get_location("Firing Range: Dragon - Silver")
            world.set_rule(dragon_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
            
            dragon_gold = world.get_location("Firing Range: Dragon - Gold")
            world.set_rule(dragon_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]))
            
            k7avenger_bronze = world.get_location("Firing Range: K7 Avenger - Bronze")
            world.set_rule(k7avenger_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
            
            k7avenger_silver = world.get_location("Firing Range: K7 Avenger - Silver")
            world.set_rule(k7avenger_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
            
            k7avenger_gold = world.get_location("Firing Range: K7 Avenger - Gold")
            world.set_rule(k7avenger_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]))
            
            ar34_bronze = world.get_location("Firing Range: AR34 - Bronze")
            world.set_rule(ar34_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]))
            
            ar34_silver = world.get_location("Firing Range: AR34 - Silver")
            world.set_rule(ar34_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]))
            
            ar34_gold = world.get_location("Firing Range: AR34 - Gold")
            world.set_rule(ar34_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]))
            
            superdragon_bronze = world.get_location("Firing Range: SuperDragon - Bronze")
            world.set_rule(superdragon_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]))
            
            superdragon_silver = world.get_location("Firing Range: SuperDragon - Silver")
            world.set_rule(superdragon_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]))
            
            superdragon_gold = world.get_location("Firing Range: SuperDragon - Gold")
            world.set_rule(superdragon_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]))
            
            shotgun_bronze = world.get_location("Firing Range: Shotgun - Bronze")
            world.set_rule(shotgun_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            
            shotgun_silver = world.get_location("Firing Range: Shotgun - Silver")
            world.set_rule(shotgun_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            
            shotgun_gold = world.get_location("Firing Range: Shotgun - Gold")
            world.set_rule(shotgun_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))
            
            reaper_bronze = world.get_location("Firing Range: Reaper - Bronze")
            world.set_rule(reaper_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Reaper"]))
            
            reaper_silver = world.get_location("Firing Range: Reaper - Silver")
            world.set_rule(reaper_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Reaper"]))
            
            reaper_gold = world.get_location("Firing Range: Reaper - Gold")
            world.set_rule(reaper_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Reaper"]))
            
            sniperrifle_bronze = world.get_location("Firing Range: Sniper Rifle - Bronze")
            world.set_rule(sniperrifle_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
            
            sniperrifle_silver = world.get_location("Firing Range: Sniper Rifle - Silver")
            world.set_rule(sniperrifle_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
            
            sniperrifle_gold = world.get_location("Firing Range: Sniper Rifle - Gold")
            world.set_rule(sniperrifle_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]))
            
            farsight_bronze = world.get_location("Firing Range: FarSight XR-20 - Bronze")
            world.set_rule(farsight_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
            
            farsight_silver = world.get_location("Firing Range: FarSight XR-20 - Silver")
            world.set_rule(farsight_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
            
            farsight_gold = world.get_location("Firing Range: FarSight XR-20 - Gold")
            world.set_rule(farsight_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]))
            
            devastator_bronze = world.get_location("Firing Range: Devastator - Bronze")
            world.set_rule(devastator_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]))
            
            devastator_silver = world.get_location("Firing Range: Devastator - Silver")
            world.set_rule(devastator_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]))
            
            devastator_gold = world.get_location("Firing Range: Devastator - Gold")
            world.set_rule(devastator_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]))
            
            rocketlauncher_bronze = world.get_location("Firing Range: Rocket Launcher - Bronze")
            world.set_rule(rocketlauncher_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]))
            
            rocketlauncher_silver = world.get_location("Firing Range: Rocket Launcher - Silver")
            world.set_rule(rocketlauncher_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]))
            
            rocketlauncher_gold = world.get_location("Firing Range: Rocket Launcher - Gold")
            world.set_rule(rocketlauncher_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]))
            
            slayer_bronze = world.get_location("Firing Range: Slayer - Bronze")
            world.set_rule(slayer_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
            
            slayer_silver = world.get_location("Firing Range: Slayer - Silver")
            world.set_rule(slayer_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
            
            slayer_gold = world.get_location("Firing Range: Slayer - Gold")
            world.set_rule(slayer_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]))
            
            knife_bronze = world.get_location("Firing Range: Combat Knife - Bronze")
            world.set_rule(knife_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
            
            knife_silver = world.get_location("Firing Range: Combat Knife - Silver")
            world.set_rule(knife_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
            
            knife_gold = world.get_location("Firing Range: Combat Knife - Gold")
            world.set_rule(knife_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]))
            
            crossbow_bronze = world.get_location("Firing Range: Crossbow - Bronze")
            world.set_rule(crossbow_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"]))
            
            crossbow_silver = world.get_location("Firing Range: Crossbow - Silver")
            world.set_rule(crossbow_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"]))
            
            crossbow_gold = world.get_location("Firing Range: Crossbow - Gold")
            world.set_rule(crossbow_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"]))
            
            tranquilizer_bronze = world.get_location("Firing Range: Tranquilizer - Bronze")
            world.set_rule(tranquilizer_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
            
            tranquilizer_silver = world.get_location("Firing Range: Tranquilizer - Silver")
            world.set_rule(tranquilizer_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
            
            tranquilizer_gold = world.get_location("Firing Range: Tranquilizer - Gold")
            world.set_rule(tranquilizer_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]))
            
            laser_bronze = world.get_location("Firing Range: Laser - Bronze")
            world.set_rule(laser_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"]))
            
            laser_silver = world.get_location("Firing Range: Laser - Silver")
            world.set_rule(laser_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"]))
            
            laser_gold = world.get_location("Firing Range: Laser - Gold")
            world.set_rule(laser_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Laser"]))
            
            grenade_bronze = world.get_location("Firing Range: Grenade - Bronze")
            world.set_rule(grenade_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]))
            
            grenade_silver = world.get_location("Firing Range: Grenade - Silver")
            world.set_rule(grenade_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]))
            
            grenade_gold = world.get_location("Firing Range: Grenade - Gold")
            world.set_rule(grenade_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]))
            
            timedmine_bronze = world.get_location("Firing Range: Timed Mine - Bronze")
            world.set_rule(timedmine_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
            
            timedmine_silver = world.get_location("Firing Range: Timed Mine - Silver")
            world.set_rule(timedmine_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
            
            timedmine_gold = world.get_location("Firing Range: Timed Mine - Gold")
            world.set_rule(timedmine_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
            
            proximitymine_bronze = world.get_location("Firing Range: Proximity Mine - Bronze")
            world.set_rule(proximitymine_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"]))
            
            proximitymine_silver = world.get_location("Firing Range: Proximity Mine - Silver")
            world.set_rule(proximitymine_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"]))
            
            proximitymine_gold = world.get_location("Firing Range: Proximity Mine - Gold")
            world.set_rule(proximitymine_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Proximity Mine"]))
            
            remotemine_bronze = world.get_location("Firing Range: Remote Mine - Bronze")
            world.set_rule(remotemine_bronze, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
            
            remotemine_silver = world.get_location("Firing Range: Remote Mine - Silver")
            world.set_rule(remotemine_silver, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))
            
            remotemine_gold = world.get_location("Firing Range: Remote Mine - Gold")
            world.set_rule(remotemine_gold, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]))

        if world.options.holotraining:
            dt_data_uplink = world.get_location("Holotraining 7: Live Combat 2")
            world.set_rule(dt_data_uplink, Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]))

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
        world.set_rule(dt_cloaking_device, Has("Cloaking Device"))


def set_completion_condition(world: PerfectDarkWorld) -> None:
    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        has_skedar_ruins = Has("Skedar Ruins - Agent") | Has("Skedar Ruins - Special Agent") | Has("Skedar Ruins - Perfect Agent")

        if world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_item:
            if world.options.weapon_progression.value == WeaponProgression.option_vanilla:
                world.set_completion_rule(has_skedar_ruins & HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                world.set_completion_rule(has_skedar_ruins 
                                          & ((HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])) 
                                          | (HasAll("R-Tracker", "Target Amplifier", "IR Scanner") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                world.set_completion_rule(has_skedar_ruins & HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]))

        elif world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_mission_stars:
            required_mission_stars = get_mission_stars(world)
            world.set_completion_rule(Has("Mission Star", count=required_mission_stars))

            if world.options.weapon_progression.value == WeaponProgression.option_vanilla:
                world.set_completion_rule(HasAll("Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner")
                                          & Has("Mission Star", count=required_mission_stars))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon:
                world.set_completion_rule((HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])) 
                                          | (HasAll("R-Tracker", "Target Amplifier", "IR Scanner") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]))
                                          & Has("Mission Star", count=required_mission_stars))

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon_one_gun:
                world.set_completion_rule(HasAll("Devastator", "R-Tracker", "Target Amplifier", "IR Scanner") & Has("Progressive Weapon", count=PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"])
                                          & Has("Mission Star", count=required_mission_stars))

    elif world.options.goal.value == Goal.option_collect_mission_stars:
        required_mission_stars = get_mission_stars(world)
        world.set_completion_rule(Has("Mission Star", count=required_mission_stars))

    # elif world.options.goal.value == Goal.option_collect_challenge_stars:
    #     world.set_completion_rule(Has("Challenge Star", count=world.options.required_challenge_stars.value))


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


def add_challenge_rules(world: PerfectDarkWorld, challenge_rules: dict) -> None:
    for challenge, rule in challenge_rules.items():
        if challenge in world.options.allowed_challenges:
            challenge_location = world.get_location(f"Complete: {challenge}")
            world.set_rule(challenge_location, rule)
