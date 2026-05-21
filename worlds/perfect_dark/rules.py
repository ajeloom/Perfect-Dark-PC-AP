from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, RequiredMissionStars

def set_all_rules(world: PerfectDarkWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: PerfectDarkWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
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

    set_rule(ci_to_defection, lambda state: state.has("Defection - Perfect Agent", world.player))
    set_rule(ci_to_investigation, lambda state: state.has("Investigation - Perfect Agent", world.player))
    set_rule(ci_to_extraction, lambda state: state.has("Extraction - Perfect Agent", world.player))
    set_rule(ci_to_villa, lambda state: state.has("Carrington Villa - Perfect Agent", world.player))
    set_rule(ci_to_chicago, lambda state: state.has("Chicago - Perfect Agent", world.player))
    set_rule(ci_to_g5_building, lambda state: state.has("G5 Building - Perfect Agent", world.player))
    set_rule(ci_to_infiltration, lambda state: state.has("Infiltration - Perfect Agent", world.player))
    set_rule(ci_to_rescue, lambda state: state.has("Rescue - Perfect Agent", world.player))
    set_rule(ci_to_escape, lambda state: state.has("Escape - Perfect Agent", world.player))
    set_rule(ci_to_air_base, lambda state: state.has("Air Base - Perfect Agent", world.player))
    set_rule(ci_to_air_force_one, lambda state: state.has("Air Force One - Perfect Agent", world.player))
    set_rule(ci_to_crash_site, lambda state: state.has("Crash Site - Perfect Agent", world.player))
    set_rule(ci_to_pelagic, lambda state: state.has("Pelagic II - Perfect Agent", world.player))
    set_rule(ci_to_deep_sea, lambda state: state.has("Deep Sea - Perfect Agent", world.player))
    set_rule(ci_to_defense, lambda state: state.has("Carrington Institute - Perfect Agent", world.player))
    set_rule(ci_to_attack_ship, lambda state: state.has("Attack Ship - Perfect Agent", world.player))
    set_rule(ci_to_skedar_ruins, lambda state: state.has("Skedar Ruins - Perfect Agent", world.player))
    set_rule(ci_to_mbr, lambda state: state.has("Mr. Blonde's Revenge - Perfect Agent", world.player))
    set_rule(ci_to_maian_sos, lambda state: state.has("Maian SOS - Perfect Agent", world.player))
    set_rule(ci_to_war, lambda state: state.has("WAR! - Perfect Agent", world.player))
    set_rule(ci_to_duel, lambda state: state.has("The Duel - Perfect Agent", world.player))


def set_all_location_rules(world: PerfectDarkWorld) -> None:
    if world.options.weapon_progression.value == world.options.weapon_progression.option_vanilla:
        # Stage 1 - Defection
        defection_prf_agent_obj_1 = world.get_location("Defection - Perfect Agent Objective 1")
        add_rule(defection_prf_agent_obj_1, lambda state: state.has_all(("Defection - Perfect Agent", "ECM Mine"), world.player))

        defection_prf_agent_obj_2 = world.get_location("Defection - Perfect Agent Objective 2")
        add_rule(defection_prf_agent_obj_2, lambda state: state.has_all(("Defection - Perfect Agent", "De Vries' Necklace"), world.player))

        defection_prf_agent_obj_3 = world.get_location("Defection - Perfect Agent Objective 3")
        add_rule(defection_prf_agent_obj_3, lambda state: state.has_all(("Defection - Perfect Agent", "Data Uplink", "Falcon 2 (Silencer)"), world.player)
                                                        or state.has_all(("Defection - Perfect Agent", "Data Uplink", "CMP150"), world.player))

        defection_prf_agent_obj_4 = world.get_location("Defection - Perfect Agent Objective 4")
        add_rule(defection_prf_agent_obj_4, lambda state: state.has_all(("Defection - Perfect Agent", "ECM Mine", "Falcon 2 (Silencer)"), world.player)
                                                        or state.has_all(("Defection - Perfect Agent", "ECM Mine", "CMP150"), world.player))

        defection_prf_agent_obj_5 = world.get_location("Defection - Perfect Agent Objective 5")
        add_rule(defection_prf_agent_obj_5, lambda state: state.has_all(("Defection - Perfect Agent", "De Vries' Necklace", "Falcon 2 (Silencer)"), world.player)
                                                        or state.has_all(("Defection - Perfect Agent", "De Vries' Necklace", "CMP150"), world.player))

        defection_prf_agent_complete = world.get_location("Complete: Defection - Perfect Agent")
        add_rule(defection_prf_agent_complete, lambda state: state.has_all(("Defection - Perfect Agent", "ECM Mine", "De Vries' Necklace", "Data Uplink", "Falcon 2 (Silencer)"), world.player)
                                                            or state.has_all(("Defection - Perfect Agent", "ECM Mine", "De Vries' Necklace", "Data Uplink", "CMP150"), world.player))


        # Stage 2 - Investigation
        investigation_prf_agent_obj_1 = world.get_location("Investigation - Perfect Agent Objective 1")
        add_rule(investigation_prf_agent_obj_1, lambda state: state.has_all(("Investigation - Perfect Agent", "CamSpy"), world.player))

        investigation_prf_agent_obj_2 = world.get_location("Investigation - Perfect Agent Objective 2")
        add_rule(investigation_prf_agent_obj_2, lambda state: state.has("Investigation - Perfect Agent", world.player))

        investigation_prf_agent_obj_3 = world.get_location("Investigation - Perfect Agent Objective 3")
        add_rule(investigation_prf_agent_obj_3, lambda state: state.has_all(("Investigation - Perfect Agent", "Falcon 2"), world.player)
                                                            or state.has_all(("Investigation - Perfect Agent", "CMP150"), world.player))

        investigation_prf_agent_obj_4 = world.get_location("Investigation - Perfect Agent Objective 4")
        add_rule(investigation_prf_agent_obj_4, lambda state: state.has_all(("Investigation - Perfect Agent", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                            or state.has_all(("Investigation - Perfect Agent", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player))

        investigation_prf_agent_obj_5 = world.get_location("Investigation - Perfect Agent Objective 5")
        add_rule(investigation_prf_agent_obj_5, lambda state: state.has_all(("Investigation - Perfect Agent", "CamSpy", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                            or state.has_all(("Investigation - Perfect Agent", "CamSpy", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player))

        investigation_prf_agent_complete = world.get_location("Complete: Investigation - Perfect Agent")
        add_rule(investigation_prf_agent_complete, lambda state: state.has_all(("Investigation - Perfect Agent", "CamSpy", "Falcon 2", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                or state.has_all(("Investigation - Perfect Agent", "CamSpy", "CMP150", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player))
        

        # Stage 3 - Extraction
        extraction_prf_agent_obj_1 = world.get_location("Extraction - Perfect Agent Objective 1")
        add_rule(extraction_prf_agent_obj_1, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)"), world.player))

        extraction_prf_agent_obj_2 = world.get_location("Extraction - Perfect Agent Objective 2")
        add_rule(extraction_prf_agent_obj_2, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)"), world.player))

        extraction_prf_agent_obj_3 = world.get_location("Extraction - Perfect Agent Objective 3")
        add_rule(extraction_prf_agent_obj_3, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Rocket Launcher"), world.player))

        extraction_prf_agent_obj_4 = world.get_location("Extraction - Perfect Agent Objective 4")
        add_rule(extraction_prf_agent_obj_4, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150"), world.player)
                                                        or state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun"), world.player))

        extraction_prf_agent_obj_5 = world.get_location("Extraction - Perfect Agent Objective 5")
        add_rule(extraction_prf_agent_obj_5, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150"), world.player)
                                                        or state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun"), world.player))

        extraction_prf_agent_complete = world.get_location("Complete: Extraction - Perfect Agent")
        add_rule(extraction_prf_agent_complete, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "CMP150", "Rocket Launcher"), world.player)
                                                            or state.has_all(("Extraction - Perfect Agent", "Night Vision", "Falcon 2 (Scope)", "Shotgun", "Rocket Launcher"), world.player))


        # Stage 4 - Villa
        villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
        add_rule(villa_prf_agent_obj_1, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "CMP150"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "Sniper Rifle"), world.player))

        villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
        add_rule(villa_prf_agent_obj_2, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "CMP150"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "Sniper Rifle"), world.player))

        villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
        add_rule(villa_prf_agent_obj_3, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "CMP150"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "Sniper Rifle"), world.player))

        villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
        add_rule(villa_prf_agent_obj_4, lambda state: state.has("Carrington Villa - Perfect Agent", world.player))

        villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
        add_rule(villa_prf_agent_obj_5, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card"), world.player)
                                                    or state.has_all(("Carrington Villa - Perfect Agent", "CMP150", "Sniper Rifle", "Cellar Key Card"), world.player))

        villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
        add_rule(villa_prf_agent_complete, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun", "CMP150", "Cellar Key Card"), world.player)
                                                        or state.has_all(("Carrington Villa - Perfect Agent", "Laptop Gun", "Sniper Rifle", "Cellar Key Card"), world.player)
                                                        or state.has_all(("Carrington Villa - Perfect Agent", "CMP150", "Sniper Rifle", "Cellar Key Card"), world.player))


        # Stage 5 - Chicago
        chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
        add_rule(chicago_prf_agent_obj_1, lambda state: state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink"), world.player))

        chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
        add_rule(chicago_prf_agent_obj_2, lambda state: state.has_all(("Chicago - Perfect Agent", "Tracer Bug"), world.player))

        chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
        add_rule(chicago_prf_agent_obj_3, lambda state: state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Falcon 2 (Scope)"), world.player)
                                                        or state.has_all(("Chicago - Perfect Agent", "Remote Mine", "CMP150"), world.player))

        chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
        add_rule(chicago_prf_agent_obj_4, lambda state: state.has_all(("Chicago - Perfect Agent", "Data Uplink", "Falcon 2 (Scope)"), world.player)
                                                        or state.has_all(("Chicago - Perfect Agent", "Data Uplink", "CMP150"), world.player) 
                                                        or state.has_all(("Chicago - Perfect Agent", "CamSpy", "Falcon 2 (Scope)"), world.player)
                                                        or state.has_all(("Chicago - Perfect Agent", "CamSpy", "CMP150"), world.player))

        chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
        add_rule(chicago_prf_agent_obj_5, lambda state: state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)"), world.player) 
                                                        or state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "CMP150"), world.player))
        
        chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
        add_rule(chicago_prf_agent_complete, lambda state: state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "Falcon 2 (Scope)"), world.player)
                                                        or state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug", "CMP150"), world.player))


        # Stage 6 - G5 Building
        g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
        add_rule(g5_prf_agent_obj_1, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Falcon 2 (Silencer)"), world.player)
                                                or state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CMP150"), world.player))

        g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
        add_rule(g5_prf_agent_obj_2, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Falcon 2 (Silencer)"), world.player)
                                                or state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CMP150"), world.player))

        g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
        add_rule(g5_prf_agent_obj_3, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Falcon 2 (Silencer)", "CamSpy"), world.player)
                                                or state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CMP150", "CamSpy"), world.player))

        g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
        add_rule(g5_prf_agent_obj_4, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Falcon 2 (Silencer)", "Door Decoder", "Backup Disk"), world.player)
                                                or state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CMP150", "Door Decoder", "Backup Disk"), world.player))

        g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
        add_rule(g5_prf_agent_obj_5, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Falcon 2 (Silencer)", "Remote Mine"), world.player)
                                                or state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CMP150", "Remote Mine"), world.player))

        g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
        add_rule(g5_prf_agent_complete, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Falcon 2 (Silencer)", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine"), world.player)
                                                    or state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CMP150", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine"), world.player))


        # Stage 7 - Infiltration
        infiltration_prf_agent_obj_1 = world.get_location("Infiltration - Perfect Agent Objective 1")
        add_rule(infiltration_prf_agent_obj_1, lambda state: state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Explosives"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "MagSec 4", "Explosives"), world.player))

        infiltration_prf_agent_obj_2 = world.get_location("Infiltration - Perfect Agent Objective 2")
        add_rule(infiltration_prf_agent_obj_2, lambda state: state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Comms Rider"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "MagSec 4", "Comms Rider"), world.player))

        infiltration_prf_agent_obj_3 = world.get_location("Infiltration - Perfect Agent Objective 3")
        add_rule(infiltration_prf_agent_obj_3, lambda state: state.has_all(("Infiltration - Perfect Agent", "Falcon 2"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "MagSec 4"), world.player))

        infiltration_prf_agent_obj_4 = world.get_location("Infiltration - Perfect Agent Objective 4")
        add_rule(infiltration_prf_agent_obj_4, lambda state: state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Area 51 Lift Key Card"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "MagSec 4", "Area 51 Lift Key Card"), world.player))

        infiltration_prf_agent_obj_5 = world.get_location("Infiltration - Perfect Agent Objective 5")
        add_rule(infiltration_prf_agent_obj_5, lambda state: state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Rocket Launcher", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Grenade", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                            or state.has_all(("Infiltration - Perfect Agent", "MagSec 4", "Dragon", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player))

        infiltration_prf_agent_complete = world.get_location("Complete: Infiltration - Perfect Agent")
        add_rule(infiltration_prf_agent_complete, lambda state: state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "MagSec 4", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                                or state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Rocket Launcher", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                                or state.has_all(("Infiltration - Perfect Agent", "Falcon 2", "Dragon", "Grenade", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                                or state.has_all(("Infiltration - Perfect Agent", "MagSec 4", "Dragon", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player))


        # Stage 8 - Rescue
        rescue_prf_agent_obj_1 = world.get_location("Rescue - Perfect Agent Objective 1")
        add_rule(rescue_prf_agent_obj_1, lambda state: state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Data Uplink"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Dragon", "Data Uplink"), world.player))

        rescue_prf_agent_obj_2 = world.get_location("Rescue - Perfect Agent Objective 2")
        add_rule(rescue_prf_agent_obj_2, lambda state: state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Dragon", "X-Ray Scanner"), world.player))

        rescue_prf_agent_obj_3 = world.get_location("Rescue - Perfect Agent Objective 3")
        add_rule(rescue_prf_agent_obj_3, lambda state: state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Lab Clothes"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Lab Clothes"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Dragon", "SuperDragon", "Lab Clothes"), world.player))

        rescue_prf_agent_obj_4 = world.get_location("Rescue - Perfect Agent Objective 4")
        add_rule(rescue_prf_agent_obj_4, lambda state: state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card"), world.player))

        rescue_prf_agent_obj_5 = world.get_location("Rescue - Perfect Agent Objective 5")
        add_rule(rescue_prf_agent_obj_5, lambda state: state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                    or state.has_all(("Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player))
        
        rescue_prf_agent_complete = world.get_location("Complete: Rescue - Perfect Agent")
        add_rule(rescue_prf_agent_complete, lambda state: state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "Dragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                        or state.has_all(("Rescue - Perfect Agent", "Falcon 2 (Silencer)", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                        or state.has_all(("Rescue - Perfect Agent", "Dragon", "SuperDragon", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player))


        # Stage 9 - Escape
        escape_prf_agent_obj_1 = world.get_location("Escape - Perfect Agent Objective 1")
        add_rule(escape_prf_agent_obj_1, lambda state: state.has_all(("Escape - Perfect Agent", "Falcon 2 (Scope)", "Alien Medpack"), world.player))

        escape_prf_agent_obj_2 = world.get_location("Escape - Perfect Agent Objective 2")
        add_rule(escape_prf_agent_obj_2, lambda state: state.has_all(("Escape - Perfect Agent", "Falcon 2 (Scope)"), world.player))

        escape_prf_agent_obj_3 = world.get_location("Escape - Perfect Agent Objective 3")
        add_rule(escape_prf_agent_obj_3, lambda state: state.has_all(("Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon"), world.player))

        escape_prf_agent_obj_4 = world.get_location("Escape - Perfect Agent Objective 4")
        add_rule(escape_prf_agent_obj_4, lambda state: state.has_all(("Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"), world.player))

        escape_prf_agent_obj_5 = world.get_location("Escape - Perfect Agent Objective 5")
        add_rule(escape_prf_agent_obj_5, lambda state: state.has_all(("Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"), world.player))
        
        escape_prf_agent_complete = world.get_location("Complete: Escape - Perfect Agent")
        add_rule(escape_prf_agent_complete, lambda state: state.has_all(("Escape - Perfect Agent", "Falcon 2 (Scope)", "SuperDragon", "Alien Medpack"), world.player))


        # Stage 10 - Air Base
        air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
        add_rule(air_base_prf_agent_obj_1, lambda state: state.has_all(("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise"), world.player)
                                                or state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"), world.player))

        air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
        add_rule(air_base_prf_agent_obj_2, lambda state: state.has_all(("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise", "Suitcase"), world.player)
                                                or state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"), world.player))

        air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
        add_rule(air_base_prf_agent_obj_3, lambda state: state.has_all(("Air Base - Perfect Agent", "Crossbow", "Stewardess Disguise"), world.player)
                                                or state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"), world.player))

        air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
        add_rule(air_base_prf_agent_obj_4, lambda state: state.has_all(("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Flight Plans"), world.player)
                                                or state.has_all(("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Flight Plans"), world.player)
                                                or state.has_all(("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Flight Plans"), world.player)
                                                or state.has_all(("Air Base - Perfect Agent", "CamSpy", "K7 Avenger", "Stewardess Disguise", "Flight Plans"), world.player))

        air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
        add_rule(air_base_prf_agent_obj_5, lambda state: state.has_all(("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                        or state.has_all(("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                        or state.has_all(("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                        or state.has_all(("Air Base - Perfect Agent", "CamSpy", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player))
        
        air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
        add_rule(air_base_prf_agent_complete, lambda state: state.has_all(("Air Base - Perfect Agent", "Crossbow", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                            or state.has_all(("Air Base - Perfect Agent", "Crossbow", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                            or state.has_all(("Air Base - Perfect Agent", "CamSpy", "Dragon", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                            or state.has_all(("Air Base - Perfect Agent", "CamSpy", "K7 Avenger", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player))


        # Stage 11 - Air Force One
        air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
        add_rule(air_force_one_prf_agent_obj_1, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player))

        air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
        add_rule(air_force_one_prf_agent_obj_2, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player))

        air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
        add_rule(air_force_one_prf_agent_obj_3, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Laptop Gun"), world.player)
                                                            or state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Cyclone"), world.player))

        air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
        add_rule(air_force_one_prf_agent_obj_4, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Laptop Gun", "Timed Mine"), world.player)
                                                            or state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Cyclone", "Timed Mine"), world.player))

        air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
        add_rule(air_force_one_prf_agent_obj_5, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Laptop Gun", "Timed Mine"), world.player)
                                                            or state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Cyclone", "Timed Mine"), world.player))

        air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
        add_rule(air_force_one_prf_agent_complete, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Laptop Gun", "Timed Mine"), world.player)
                                                                or state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Cyclone", "Timed Mine"), world.player))


        # Stage 12 - Crash Site
        crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
        add_rule(crash_site_prf_agent_obj_1, lambda state: state.has_all(("Crash Site - Perfect Agent", "President Scanner"), world.player))

        crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
        add_rule(crash_site_prf_agent_obj_2, lambda state: state.has("Crash Site - Perfect Agent", world.player))

        crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
        add_rule(crash_site_prf_agent_obj_3, lambda state: state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "Remote Mine"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "Remote Mine"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "K7 Avenger", "Sniper Rifle", "Remote Mine"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "DY357-LX", "President Scanner"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "DY357-LX", "President Scanner"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "K7 Avenger", "Sniper Rifle", "DY357-LX", "President Scanner"), world.player))

        crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
        add_rule(crash_site_prf_agent_obj_4, lambda state: state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "President Scanner"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "K7 Avenger", "President Scanner"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "Sniper Rifle", "President Scanner"), world.player))

        crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
        add_rule(crash_site_prf_agent_obj_5, lambda state: state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner"), world.player)
                                                        or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner"), world.player))
        
        crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
        add_rule(crash_site_prf_agent_complete, lambda state: state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "Remote Mine"), world.player)
                                                            or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "Remote Mine"), world.player)
                                                            or state.has_all(("Crash Site - Perfect Agent", "K7 Avenger", "Sniper Rifle", "President Scanner", "Remote Mine"), world.player)
                                                            or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "K7 Avenger", "President Scanner", "DY357-LX"), world.player)
                                                            or state.has_all(("Crash Site - Perfect Agent", "Falcon 2 (Scope)", "Sniper Rifle", "President Scanner", "DY357-LX"), world.player)
                                                            or state.has_all(("Crash Site - Perfect Agent", "K7 Avenger", "Sniper Rifle", "President Scanner", "DY357-LX"), world.player))


        # Stage 13 - Pelagic II
        pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
        add_rule(pelagic_prf_agent_obj_1, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "X-Ray Scanner"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Laptop Gun", "X-Ray Scanner"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "CMP150", "X-Ray Scanner"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Phoenix", "X-Ray Scanner"), world.player))

        pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
        add_rule(pelagic_prf_agent_obj_2, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Laptop Gun", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "CMP150", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Phoenix", "Research Tape"), world.player))

        pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
        add_rule(pelagic_prf_agent_obj_3, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Laptop Gun"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "CMP150"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Phoenix"), world.player))

        pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
        add_rule(pelagic_prf_agent_obj_4, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Laptop Gun"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "CMP150"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Phoenix"), world.player))

        pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
        add_rule(pelagic_prf_agent_obj_5, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"), world.player))
        
        pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
        add_rule(pelagic_prf_agent_complete, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "Laptop Gun", "X-Ray Scanner", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Falcon 2 (Silencer)", "CMP150", "X-Ray Scanner", "Research Tape"), world.player)
                                                        or state.has_all(("Pelagic II - Perfect Agent", "Laptop Gun", "CMP150", "X-Ray Scanner", "Research Tape"), world.player))


        # Stage 14 - Deep Sea
        deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
        add_rule(deep_sea_prf_agent_obj_1, lambda state: state.has_all(("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner"), world.player)
                                                        or state.has_all(("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner"), world.player))

        deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
        add_rule(deep_sea_prf_agent_obj_2, lambda state: state.has_all(("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20"), world.player)
                                                        or state.has_all(("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20"), world.player))

        deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
        add_rule(deep_sea_prf_agent_obj_3, lambda state: state.has_all(("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20"), world.player)
                                                        or state.has_all(("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20"), world.player))

        deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
        add_rule(deep_sea_prf_agent_obj_4, lambda state: state.has_all(("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player)
                                                        or state.has_all(("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player))

        deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
        add_rule(deep_sea_prf_agent_obj_5, lambda state: state.has_all(("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player)
                                                        or state.has_all(("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player))
        
        deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
        add_rule(deep_sea_prf_agent_complete, lambda state: state.has_all(("Deep Sea - Perfect Agent", "Falcon 2 (Scope)", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player)
                                                        or state.has_all(("Deep Sea - Perfect Agent", "Shotgun", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player))


        # Stage 15 - Carrington Institute Defense
        institute_defense_prf_agent_obj_1 = world.get_location("Carrington Institute - Perfect Agent Objective 1")
        add_rule(institute_defense_prf_agent_obj_1, lambda state: state.has("Carrington Institute - Perfect Agent", world.player))

        institute_defense_prf_agent_obj_2 = world.get_location("Carrington Institute - Perfect Agent Objective 2")
        add_rule(institute_defense_prf_agent_obj_2, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "AR34"), world.player))

        institute_defense_prf_agent_obj_3 = world.get_location("Carrington Institute - Perfect Agent Objective 3")
        add_rule(institute_defense_prf_agent_obj_3, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "AR34", "RC-P120"), world.player))

        institute_defense_prf_agent_obj_4 = world.get_location("Carrington Institute - Perfect Agent Objective 4")
        add_rule(institute_defense_prf_agent_obj_4, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "AR34", "RC-P120", "Laser"), world.player)
                                                                or state.has_all(("Carrington Institute - Perfect Agent", "AR34", "Devastator"), world.player))

        institute_defense_prf_agent_obj_5 = world.get_location("Carrington Institute - Perfect Agent Objective 5")
        add_rule(institute_defense_prf_agent_obj_5, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink"), world.player)
                                                                or state.has_all(("Carrington Institute - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"), world.player))

        institute_defense_prf_agent_complete = world.get_location("Complete: Carrington Institute - Perfect Agent")
        add_rule(institute_defense_prf_agent_complete, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "AR34", "RC-P120", "Laser", "Data Uplink"), world.player)
                                                                    or state.has_all(("Carrington Institute - Perfect Agent", "AR34", "RC-P120", "Devastator", "Data Uplink"), world.player))


        # Stage 16 - Attack Ship
        attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
        add_rule(attack_ship_prf_agent_obj_1, lambda state: state.has_all(("Attack Ship - Perfect Agent", "Combat Knife", "Mauler"), world.player))

        attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
        add_rule(attack_ship_prf_agent_obj_2, lambda state: state.has_all(("Attack Ship - Perfect Agent", "Combat Knife", "Mauler"), world.player))

        attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
        add_rule(attack_ship_prf_agent_obj_3, lambda state: state.has_all(("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"), world.player))

        attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
        add_rule(attack_ship_prf_agent_obj_4, lambda state: state.has_all(("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"), world.player))

        attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
        add_rule(attack_ship_prf_agent_obj_5, lambda state: state.has_all(("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"), world.player))

        attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
        add_rule(attack_ship_prf_agent_complete, lambda state: state.has_all(("Attack Ship - Perfect Agent", "Combat Knife", "Mauler", "AR34"), world.player))


        # Stage 17 - Skedar Ruins
        skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
        add_rule(skedar_ruins_prf_agent_obj_1, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "R-Tracker", "Target Amplifier"), world.player))

        skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
        add_rule(skedar_ruins_prf_agent_obj_2, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "Devastator"), world.player))

        skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
        add_rule(skedar_ruins_prf_agent_obj_3, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"), world.player))

        skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
        add_rule(skedar_ruins_prf_agent_obj_4, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"), world.player))

        skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
        add_rule(skedar_ruins_prf_agent_obj_5, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "Devastator", "IR Scanner"), world.player))

        skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
        add_rule(skedar_ruins_prf_agent_complete, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player))


        # Stage 18 - Mr. Blonde's Revenge
        mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
        add_rule(mbr_prf_agent_obj_1, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb"), world.player))

        mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
        add_rule(mbr_prf_agent_obj_2, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device"), world.player)
                                                    or state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "CamSpy", "Cloaking Device"), world.player))

        mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
        add_rule(mbr_prf_agent_obj_3, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device"), world.player))

        mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
        add_rule(mbr_prf_agent_complete, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Mauler", "Cloaking Device", "Skedar Bomb"), world.player))


        # Stage 19 - Maian SOS
        maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
        add_rule(maian_sos_prf_agent_obj_1, lambda state: state.has_all(("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"), world.player))

        maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
        add_rule(maian_sos_prf_agent_obj_2, lambda state: state.has_all(("Maian SOS - Perfect Agent", "Falcon 2", "Dragon", "DY357-LX"), world.player))

        maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
        add_rule(maian_sos_prf_agent_obj_3, lambda state: state.has_all(("Maian SOS - Perfect Agent", "Falcon 2", "Dragon"), world.player))

        maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
        add_rule(maian_sos_prf_agent_complete, lambda state: state.has_all(("Maian SOS - Perfect Agent", "Falcon 2", "Dragon", "DY357-LX"), world.player))


        # Stage 20 - WAR!
        war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
        add_rule(war_prf_agent_obj_1, lambda state: state.has_all(("WAR! - Perfect Agent", "Phoenix"), world.player))

        war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
        add_rule(war_prf_agent_obj_2, lambda state: state.has_all(("WAR! - Perfect Agent", "Phoenix"), world.player))

        war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
        add_rule(war_prf_agent_obj_3, lambda state: state.has_all(("WAR! - Perfect Agent", "Phoenix"), world.player))

        war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
        add_rule(war_prf_agent_complete, lambda state: state.has_all(("WAR! - Perfect Agent", "Phoenix"), world.player))


        # Stage 21 - The Duel
        duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
        add_rule(duel_prf_agent_obj_1, lambda state: state.has_all(("The Duel - Perfect Agent", "Falcon 2 (Scope)"), world.player))

        duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
        add_rule(duel_prf_agent_obj_2, lambda state: state.has_all(("The Duel - Perfect Agent", "Falcon 2 (Scope)"), world.player))

        duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
        add_rule(duel_prf_agent_obj_3, lambda state: state.has_all(("The Duel - Perfect Agent", "Falcon 2 (Scope)"), world.player))
        
        duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
        add_rule(duel_prf_agent_complete, lambda state: state.has_all(("The Duel - Perfect Agent", "Falcon 2 (Scope)"), world.player))


        if world.options.challenges:
            challenge_1 = world.get_location("Complete: Challenge 1")
            add_rule(challenge_1, lambda state: state.has_all(("Challenge 1", "Falcon 2"), world.player)
                                                or state.has_all(("Challenge 1", "CMP150"), world.player)
                                                or state.has_all(("Challenge 1", "Sniper Rifle"), world.player)
                                                or state.has_all(("Challenge 1", "DY357 Magnum"), world.player)
                                                or state.has_all(("Challenge 1", "Dragon"), world.player))

            challenge_2 = world.get_location("Complete: Challenge 2")
            add_rule(challenge_2, lambda state: state.has_all(("Challenge 2", "Rocket Launcher"), world.player))

            challenge_3 = world.get_location("Complete: Challenge 3")
            add_rule(challenge_3, lambda state: state.has_all(("Challenge 3", "Timed Mine"), world.player))

            challenge_4 = world.get_location("Complete: Challenge 4")
            add_rule(challenge_4, lambda state: state.has_all(("Challenge 4", "K7 Avenger"), world.player))

            challenge_5 = world.get_location("Complete: Challenge 5")
            add_rule(challenge_5, lambda state: state.has_all(("Challenge 5", "FarSight XR-20"), world.player))

            challenge_6 = world.get_location("Complete: Challenge 6")
            add_rule(challenge_6, lambda state: state.has_all(("Challenge 6", "Briefcase", "CMP150"), world.player)
                                                or state.has_all(("Challenge 6", "Briefcase", "DY357 Magnum"), world.player)
                                                or state.has_all(("Challenge 6", "Briefcase", "Shotgun"), world.player)
                                                or state.has_all(("Challenge 6", "Briefcase", "K7 Avenger"), world.player))

            challenge_7 = world.get_location("Complete: Challenge 7")
            add_rule(challenge_7, lambda state: state.has_all(("Challenge 7", "Falcon 2 (Silencer)"), world.player)
                                                or state.has_all(("Challenge 7", "MagSec 4"), world.player)
                                                or state.has_all(("Challenge 7", "Cyclone"), world.player)
                                                or state.has_all(("Challenge 7", "Grenade"), world.player))

            challenge_8 = world.get_location("Complete: Challenge 8")
            add_rule(challenge_8, lambda state: state.has_all(("Challenge 8", "Briefcase", "MagSec 4"), world.player)
                                                or state.has_all(("Challenge 8", "Briefcase", "K7 Avenger"), world.player)
                                                or state.has_all(("Challenge 8", "Briefcase", "Shotgun"), world.player)
                                                or state.has_all(("Challenge 8", "Briefcase", "SuperDragon"), world.player))

            challenge_9 = world.get_location("Complete: Challenge 9")
            add_rule(challenge_9, lambda state: state.has_all(("Challenge 9", "FarSight XR-20"), world.player)
                                                or state.has_all(("Challenge 9", "Laptop Gun"), world.player))

            challenge_10 = world.get_location("Complete: Challenge 10")
            add_rule(challenge_10, lambda state: state.has_all(("Challenge 10", "Data Uplink", "CMP150"), world.player)
                                                or state.has_all(("Challenge 10", "Data Uplink", "Cyclone"), world.player)
                                                or state.has_all(("Challenge 10", "Data Uplink", "Remote Mine"), world.player)
                                                or state.has_all(("Challenge 10", "Data Uplink", "AR34"), world.player))

            challenge_11 = world.get_location("Complete: Challenge 11")
            add_rule(challenge_11, lambda state: state.has_all(("Challenge 11", "Shotgun", "Tranquilizer"), world.player))

            challenge_12 = world.get_location("Complete: Challenge 12")
            add_rule(challenge_12, lambda state: state.has_all(("Challenge 12", "SuperDragon"), world.player))

            challenge_13 = world.get_location("Complete: Challenge 13")
            add_rule(challenge_13, lambda state: state.has_all(("Challenge 13", "Tranquilizer", "Falcon 2 (Silencer)"), world.player)
                                                or state.has_all(("Challenge 13", "Tranquilizer", "Laptop Gun"), world.player)
                                                or state.has_all(("Challenge 13", "Tranquilizer", "Grenade"), world.player)
                                                or state.has_all(("Challenge 13", "Tranquilizer", "Reaper"), world.player))

            challenge_14 = world.get_location("Complete: Challenge 14")
            add_rule(challenge_14, lambda state: state.has_all(("Challenge 14", "Briefcase", "Cloaking Device", "Cyclone"), world.player)
                                                or state.has_all(("Challenge 14", "Briefcase", "Cloaking Device", "SuperDragon"), world.player)
                                                or state.has_all(("Challenge 14", "Briefcase", "Cloaking Device", "K7 Avenger"), world.player)
                                                or state.has_all(("Challenge 14", "Briefcase", "Cloaking Device", "FarSight XR-20"), world.player))

            challenge_15 = world.get_location("Complete: Challenge 15")
            add_rule(challenge_15, lambda state: state.has_all(("Challenge 15", "Briefcase", "Devastator", "MagSec 4"), world.player)
                                                or state.has_all(("Challenge 15", "Briefcase", "Devastator", "Dragon"), world.player)
                                                or state.has_all(("Challenge 15", "Briefcase", "Devastator", "Shotgun"), world.player))

            challenge_16 = world.get_location("Complete: Challenge 16")
            add_rule(challenge_16, lambda state: state.has_all(("Challenge 16", "Proximity Mine", "SuperDragon"), world.player))

            challenge_17 = world.get_location("Complete: Challenge 17")
            add_rule(challenge_17, lambda state: state.has_all(("Challenge 17", "Slayer", "AR34", "Reaper"), world.player))

            challenge_18 = world.get_location("Complete: Challenge 18")
            add_rule(challenge_18, lambda state: state.has_all(("Challenge 18", "Cloaking Device", "Laptop Gun", "Tranquilizer"), world.player))

            challenge_19 = world.get_location("Complete: Challenge 19")
            add_rule(challenge_19, lambda state: state.has_all(("Challenge 19", "Rocket Launcher", "FarSight XR-20", "CMP150", "Shotgun"), world.player))

            challenge_20 = world.get_location("Complete: Challenge 20")
            add_rule(challenge_20, lambda state: state.has_all(("Challenge 20", "MagSec 4", "Mauler"), world.player))

            challenge_21 = world.get_location("Complete: Challenge 21")
            add_rule(challenge_21, lambda state: state.has_all(("Challenge 21", "Data Uplink", "Cloaking Device", "Callisto NTG", "Reaper", "Shotgun"), world.player)
                                                or state.has_all(("Challenge 21", "Data Uplink", "Cloaking Device", "Callisto NTG", "Reaper", "Mauler"), world.player))

            challenge_22 = world.get_location("Complete: Challenge 22")
            add_rule(challenge_22, lambda state: state.has_all(("Challenge 22", "Briefcase", "Crossbow", "Sniper Rifle", "K7 Avenger", "Falcon 2"), world.player))

            challenge_23 = world.get_location("Complete: Challenge 23")
            add_rule(challenge_23, lambda state: state.has_all(("Challenge 23", "RC-P120", "Laptop Gun", "MagSec 4", "Grenade"), world.player))

            challenge_24 = world.get_location("Complete: Challenge 24")
            add_rule(challenge_24, lambda state: state.has_all(("Challenge 24", "Briefcase", "DY357-LX", "Tranquilizer", "Devastator", "SuperDragon", "CMP150"), world.player))

            challenge_25 = world.get_location("Complete: Challenge 25")
            add_rule(challenge_25, lambda state: state.has_all(("Challenge 25", "Cloaking Device", "N-Bomb", "FarSight XR-20", "Mauler"), world.player)
                                                or state.has_all(("Challenge 25", "Cloaking Device", "N-Bomb", "FarSight XR-20", "K7 Avenger"), world.player))

            challenge_26 = world.get_location("Complete: Challenge 26")
            add_rule(challenge_26, lambda state: state.has_all(("Challenge 26", "Mauler", "Cyclone", "Laptop Gun", "Reaper"), world.player))

            challenge_27 = world.get_location("Complete: Challenge 27")
            add_rule(challenge_27, lambda state: state.has_all(("Challenge 27", "Data Uplink", "Rocket Launcher", "CMP150", "MagSec 4", "Falcon 2"), world.player))

            challenge_28 = world.get_location("Complete: Challenge 28")
            add_rule(challenge_28, lambda state: state.has_all(("Challenge 28", "Briefcase", "Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun"), world.player))

            challenge_29 = world.get_location("Complete: Challenge 29")
            add_rule(challenge_29, lambda state: state.has_all(("Challenge 29", "DY357 Magnum", "Dragon", "CMP150", "Cyclone", "Falcon 2"), world.player))

            challenge_30 = world.get_location("Complete: Challenge 30")
            add_rule(challenge_30, lambda state: state.has_all(("Challenge 30", "Mauler", "MagSec 4", "Falcon 2", "Falcon 2 (Scope)", "DY357 Magnum"), world.player))

        if world.options.weapon_training:
            falcon2_bronze = world.get_location("Firing Range: Falcon 2 - Bronze")
            add_rule(falcon2_bronze, lambda state: state.has("Falcon 2", world.player))
            
            falcon2_silver = world.get_location("Firing Range: Falcon 2 - Silver")
            add_rule(falcon2_silver, lambda state: state.has("Falcon 2", world.player))
            
            falcon2_gold = world.get_location("Firing Range: Falcon 2 - Gold")
            add_rule(falcon2_gold, lambda state: state.has("Falcon 2", world.player))
            
            falcon2silencer_bronze = world.get_location("Firing Range: Falcon 2 (Silencer) - Bronze")
            add_rule(falcon2silencer_bronze, lambda state: state.has("Falcon 2 (Silencer)", world.player))
            
            falcon2silencer_silver = world.get_location("Firing Range: Falcon 2 (Silencer) - Silver")
            add_rule(falcon2silencer_silver, lambda state: state.has("Falcon 2 (Silencer)", world.player))
            
            falcon2silencer_gold = world.get_location("Firing Range: Falcon 2 (Silencer) - Gold")
            add_rule(falcon2silencer_gold, lambda state: state.has("Falcon 2 (Silencer)", world.player))
            
            falcon2scope_bronze = world.get_location("Firing Range: Falcon 2 (Scope) - Bronze")
            add_rule(falcon2scope_bronze, lambda state: state.has("Falcon 2 (Scope)", world.player))
            
            falcon2scope_silver = world.get_location("Firing Range: Falcon 2 (Scope) - Silver")
            add_rule(falcon2scope_silver, lambda state: state.has("Falcon 2 (Scope)", world.player))
            
            falcon2scope_gold = world.get_location("Firing Range: Falcon 2 (Scope) - Gold")
            add_rule(falcon2scope_gold, lambda state: state.has("Falcon 2 (Scope)", world.player))
            
            magsec4_bronze = world.get_location("Firing Range: MagSec 4 - Bronze")
            add_rule(magsec4_bronze, lambda state: state.has("MagSec 4", world.player))
            
            magsec4_silver = world.get_location("Firing Range: MagSec 4 - Silver")
            add_rule(magsec4_silver, lambda state: state.has("MagSec 4", world.player))
            
            magsec4_gold = world.get_location("Firing Range: MagSec 4 - Gold")
            add_rule(magsec4_gold, lambda state: state.has("MagSec 4", world.player))
            
            mauler_bronze = world.get_location("Firing Range: Mauler - Bronze")
            add_rule(mauler_bronze, lambda state: state.has("Mauler", world.player))
            
            mauler_silver = world.get_location("Firing Range: Mauler - Silver")
            add_rule(mauler_silver, lambda state: state.has("Mauler", world.player))
            
            mauler_gold = world.get_location("Firing Range: Mauler - Gold")
            add_rule(mauler_gold, lambda state: state.has("Mauler", world.player))
            
            phoenix_bronze = world.get_location("Firing Range: Phoenix - Bronze")
            add_rule(phoenix_bronze, lambda state: state.has("Phoenix", world.player))
            
            phoenix_silver = world.get_location("Firing Range: Phoenix - Silver")
            add_rule(phoenix_silver, lambda state: state.has("Phoenix", world.player))
            
            phoenix_gold = world.get_location("Firing Range: Phoenix - Gold")
            add_rule(phoenix_gold, lambda state: state.has("Phoenix", world.player))
            
            dy357magnum_bronze = world.get_location("Firing Range: DY357 Magnum - Bronze")
            add_rule(dy357magnum_bronze, lambda state: state.has("DY357 Magnum", world.player))
            
            dy357magnum_silver = world.get_location("Firing Range: DY357 Magnum - Silver")
            add_rule(dy357magnum_silver, lambda state: state.has("DY357 Magnum", world.player))
            
            dy357magnum_gold = world.get_location("Firing Range: DY357 Magnum - Gold")
            add_rule(dy357magnum_gold, lambda state: state.has("DY357 Magnum", world.player))
            
            dy357lx_bronze = world.get_location("Firing Range: DY357-LX - Bronze")
            add_rule(dy357lx_bronze, lambda state: state.has("DY357-LX", world.player))
            
            dy357lx_silver = world.get_location("Firing Range: DY357-LX - Silver")
            add_rule(dy357lx_silver, lambda state: state.has("DY357-LX", world.player))
            
            dy357lx_gold = world.get_location("Firing Range: DY357-LX - Gold")
            add_rule(dy357lx_gold, lambda state: state.has("DY357-LX", world.player))
            
            cmp150_bronze = world.get_location("Firing Range: CMP150 - Bronze")
            add_rule(cmp150_bronze, lambda state: state.has("CMP150", world.player))
            
            cmp150_silver = world.get_location("Firing Range: CMP150 - Silver")
            add_rule(cmp150_silver, lambda state: state.has("CMP150", world.player))
            
            cmp150_gold = world.get_location("Firing Range: CMP150 - Gold")
            add_rule(cmp150_gold, lambda state: state.has("CMP150", world.player))
            
            cyclone_bronze = world.get_location("Firing Range: Cyclone - Bronze")
            add_rule(cyclone_bronze, lambda state: state.has("Cyclone", world.player))
            
            cyclone_silver = world.get_location("Firing Range: Cyclone - Silver")
            add_rule(cyclone_silver, lambda state: state.has("Cyclone", world.player))
            
            cyclone_gold = world.get_location("Firing Range: Cyclone - Gold")
            add_rule(cyclone_gold, lambda state: state.has("Cyclone", world.player))
            
            callisto_bronze = world.get_location("Firing Range: Callisto NTG - Bronze")
            add_rule(callisto_bronze, lambda state: state.has("Callisto NTG", world.player))
            
            callisto_silver = world.get_location("Firing Range: Callisto NTG - Silver")
            add_rule(callisto_silver, lambda state: state.has("Callisto NTG", world.player))
            
            callisto_gold = world.get_location("Firing Range: Callisto NTG - Gold")
            add_rule(callisto_gold, lambda state: state.has("Callisto NTG", world.player))
            
            rcp120_bronze = world.get_location("Firing Range: RC-P120 - Bronze")
            add_rule(rcp120_bronze, lambda state: state.has("RC-P120", world.player))
            
            rcp120_silver = world.get_location("Firing Range: RC-P120 - Silver")
            add_rule(rcp120_silver, lambda state: state.has("RC-P120", world.player))
            
            rcp120_gold = world.get_location("Firing Range: RC-P120 - Gold")
            add_rule(rcp120_gold, lambda state: state.has("RC-P120", world.player))
            
            laptopgun_bronze = world.get_location("Firing Range: Laptop Gun - Bronze")
            add_rule(laptopgun_bronze, lambda state: state.has("Laptop Gun", world.player))
            
            laptopgun_silver = world.get_location("Firing Range: Laptop Gun - Silver")
            add_rule(laptopgun_silver, lambda state: state.has("Laptop Gun", world.player))
            
            laptopgun_gold = world.get_location("Firing Range: Laptop Gun - Gold")
            add_rule(laptopgun_gold, lambda state: state.has("Laptop Gun", world.player))
            
            dragon_bronze = world.get_location("Firing Range: Dragon - Bronze")
            add_rule(dragon_bronze, lambda state: state.has("Dragon", world.player))
            
            dragon_silver = world.get_location("Firing Range: Dragon - Silver")
            add_rule(dragon_silver, lambda state: state.has("Dragon", world.player))
            
            dragon_gold = world.get_location("Firing Range: Dragon - Gold")
            add_rule(dragon_gold, lambda state: state.has("Dragon", world.player))
            
            k7avenger_bronze = world.get_location("Firing Range: K7 Avenger - Bronze")
            add_rule(k7avenger_bronze, lambda state: state.has("K7 Avenger", world.player))
            
            k7avenger_silver = world.get_location("Firing Range: K7 Avenger - Silver")
            add_rule(k7avenger_silver, lambda state: state.has("K7 Avenger", world.player))
            
            k7avenger_gold = world.get_location("Firing Range: K7 Avenger - Gold")
            add_rule(k7avenger_gold, lambda state: state.has("K7 Avenger", world.player))
            
            ar34_bronze = world.get_location("Firing Range: AR34 - Bronze")
            add_rule(ar34_bronze, lambda state: state.has("AR34", world.player))
            
            ar34_silver = world.get_location("Firing Range: AR34 - Silver")
            add_rule(ar34_silver, lambda state: state.has("AR34", world.player))
            
            ar34_gold = world.get_location("Firing Range: AR34 - Gold")
            add_rule(ar34_gold, lambda state: state.has("AR34", world.player))
            
            superdragon_bronze = world.get_location("Firing Range: SuperDragon - Bronze")
            add_rule(superdragon_bronze, lambda state: state.has("SuperDragon", world.player))
            
            superdragon_silver = world.get_location("Firing Range: SuperDragon - Silver")
            add_rule(superdragon_silver, lambda state: state.has("SuperDragon", world.player))
            
            superdragon_gold = world.get_location("Firing Range: SuperDragon - Gold")
            add_rule(superdragon_gold, lambda state: state.has("SuperDragon", world.player))
            
            shotgun_bronze = world.get_location("Firing Range: Shotgun - Bronze")
            add_rule(shotgun_bronze, lambda state: state.has("Shotgun", world.player))
            
            shotgun_silver = world.get_location("Firing Range: Shotgun - Silver")
            add_rule(shotgun_silver, lambda state: state.has("Shotgun", world.player))
            
            shotgun_gold = world.get_location("Firing Range: Shotgun - Gold")
            add_rule(shotgun_gold, lambda state: state.has("Shotgun", world.player))
            
            reaper_bronze = world.get_location("Firing Range: Reaper - Bronze")
            add_rule(reaper_bronze, lambda state: state.has("Reaper", world.player))
            
            reaper_silver = world.get_location("Firing Range: Reaper - Silver")
            add_rule(reaper_silver, lambda state: state.has("Reaper", world.player))
            
            reaper_gold = world.get_location("Firing Range: Reaper - Gold")
            add_rule(reaper_gold, lambda state: state.has("Reaper", world.player))
            
            sniperrifle_bronze = world.get_location("Firing Range: Sniper Rifle - Bronze")
            add_rule(sniperrifle_bronze, lambda state: state.has("Sniper Rifle", world.player))
            
            sniperrifle_silver = world.get_location("Firing Range: Sniper Rifle - Silver")
            add_rule(sniperrifle_silver, lambda state: state.has("Sniper Rifle", world.player))
            
            sniperrifle_gold = world.get_location("Firing Range: Sniper Rifle - Gold")
            add_rule(sniperrifle_gold, lambda state: state.has("Sniper Rifle", world.player))
            
            farsight_bronze = world.get_location("Firing Range: FarSight XR-20 - Bronze")
            add_rule(farsight_bronze, lambda state: state.has("FarSight XR-20", world.player))
            
            farsight_silver = world.get_location("Firing Range: FarSight XR-20 - Silver")
            add_rule(farsight_silver, lambda state: state.has("FarSight XR-20", world.player))
            
            farsight_gold = world.get_location("Firing Range: FarSight XR-20 - Gold")
            add_rule(farsight_gold, lambda state: state.has("FarSight XR-20", world.player))
            
            devastator_bronze = world.get_location("Firing Range: Devastator - Bronze")
            add_rule(devastator_bronze, lambda state: state.has("Devastator", world.player))
            
            devastator_silver = world.get_location("Firing Range: Devastator - Silver")
            add_rule(devastator_silver, lambda state: state.has("Devastator", world.player))
            
            devastator_gold = world.get_location("Firing Range: Devastator - Gold")
            add_rule(devastator_gold, lambda state: state.has("Devastator", world.player))
            
            rocketlauncher_bronze = world.get_location("Firing Range: Rocket Launcher - Bronze")
            add_rule(rocketlauncher_bronze, lambda state: state.has("Rocket Launcher", world.player))
            
            rocketlauncher_silver = world.get_location("Firing Range: Rocket Launcher - Silver")
            add_rule(rocketlauncher_silver, lambda state: state.has("Rocket Launcher", world.player))
            
            rocketlauncher_gold = world.get_location("Firing Range: Rocket Launcher - Gold")
            add_rule(rocketlauncher_gold, lambda state: state.has("Rocket Launcher", world.player))
            
            slayer_bronze = world.get_location("Firing Range: Slayer - Bronze")
            add_rule(slayer_bronze, lambda state: state.has("Slayer", world.player))
            
            slayer_silver = world.get_location("Firing Range: Slayer - Silver")
            add_rule(slayer_silver, lambda state: state.has("Slayer", world.player))
            
            slayer_gold = world.get_location("Firing Range: Slayer - Gold")
            add_rule(slayer_gold, lambda state: state.has("Slayer", world.player))
            
            knife_bronze = world.get_location("Firing Range: Combat Knife - Bronze")
            add_rule(knife_bronze, lambda state: state.has("Combat Knife", world.player))
            
            knife_silver = world.get_location("Firing Range: Combat Knife - Silver")
            add_rule(knife_silver, lambda state: state.has("Combat Knife", world.player))
            
            knife_gold = world.get_location("Firing Range: Combat Knife - Gold")
            add_rule(knife_gold, lambda state: state.has("Combat Knife", world.player))
            
            crossbow_bronze = world.get_location("Firing Range: Crossbow - Bronze")
            add_rule(crossbow_bronze, lambda state: state.has("Crossbow", world.player))
            
            crossbow_silver = world.get_location("Firing Range: Crossbow - Silver")
            add_rule(crossbow_silver, lambda state: state.has("Crossbow", world.player))
            
            crossbow_gold = world.get_location("Firing Range: Crossbow - Gold")
            add_rule(crossbow_gold, lambda state: state.has("Crossbow", world.player))
            
            tranquilizer_bronze = world.get_location("Firing Range: Tranquilizer - Bronze")
            add_rule(tranquilizer_bronze, lambda state: state.has("Tranquilizer", world.player))
            
            tranquilizer_silver = world.get_location("Firing Range: Tranquilizer - Silver")
            add_rule(tranquilizer_silver, lambda state: state.has("Tranquilizer", world.player))
            
            tranquilizer_gold = world.get_location("Firing Range: Tranquilizer - Gold")
            add_rule(tranquilizer_gold, lambda state: state.has("Tranquilizer", world.player))
            
            laser_bronze = world.get_location("Firing Range: Laser - Bronze")
            add_rule(laser_bronze, lambda state: state.has("Laser", world.player))
            
            laser_silver = world.get_location("Firing Range: Laser - Silver")
            add_rule(laser_silver, lambda state: state.has("Laser", world.player))
            
            laser_gold = world.get_location("Firing Range: Laser - Gold")
            add_rule(laser_gold, lambda state: state.has("Laser", world.player))
            
            grenade_bronze = world.get_location("Firing Range: Grenade - Bronze")
            add_rule(grenade_bronze, lambda state: state.has("Grenade", world.player))
            
            grenade_silver = world.get_location("Firing Range: Grenade - Silver")
            add_rule(grenade_silver, lambda state: state.has("Grenade", world.player))
            
            grenade_gold = world.get_location("Firing Range: Grenade - Gold")
            add_rule(grenade_gold, lambda state: state.has("Grenade", world.player))
            
            timedmine_bronze = world.get_location("Firing Range: Timed Mine - Bronze")
            add_rule(timedmine_bronze, lambda state: state.has("Timed Mine", world.player))
            
            timedmine_silver = world.get_location("Firing Range: Timed Mine - Silver")
            add_rule(timedmine_silver, lambda state: state.has("Timed Mine", world.player))
            
            timedmine_gold = world.get_location("Firing Range: Timed Mine - Gold")
            add_rule(timedmine_gold, lambda state: state.has("Timed Mine", world.player))
            
            proximitymine_bronze = world.get_location("Firing Range: Proximity Mine - Bronze")
            add_rule(proximitymine_bronze, lambda state: state.has("Proximity Mine", world.player))
            
            proximitymine_silver = world.get_location("Firing Range: Proximity Mine - Silver")
            add_rule(proximitymine_silver, lambda state: state.has("Proximity Mine", world.player))
            
            proximitymine_gold = world.get_location("Firing Range: Proximity Mine - Gold")
            add_rule(proximitymine_gold, lambda state: state.has("Proximity Mine", world.player))
            
            remotemine_bronze = world.get_location("Firing Range: Remote Mine - Bronze")
            add_rule(remotemine_bronze, lambda state: state.has("Remote Mine", world.player))
            
            remotemine_silver = world.get_location("Firing Range: Remote Mine - Silver")
            add_rule(remotemine_silver, lambda state: state.has("Remote Mine", world.player))
            
            remotemine_gold = world.get_location("Firing Range: Remote Mine - Gold")
            add_rule(remotemine_gold, lambda state: state.has("Remote Mine", world.player))

        if world.options.holotraining:
            dt_data_uplink = world.get_location("Holotraining 7: Live Combat 2")
            add_rule(dt_data_uplink, lambda state: state.has("Falcon 2", world.player))


    elif world.options.weapon_progression.value > world.options.weapon_progression.option_vanilla:
        # Stage 1 - Defection
        defection_prf_agent_obj_1 = world.get_location("Defection - Perfect Agent Objective 1")
        add_rule(defection_prf_agent_obj_1, lambda state: state.has_all(("Defection - Perfect Agent", "ECM Mine"), world.player))

        defection_prf_agent_obj_2 = world.get_location("Defection - Perfect Agent Objective 2")
        add_rule(defection_prf_agent_obj_2, lambda state: state.has_all(("Defection - Perfect Agent", "De Vries' Necklace"), world.player))

        defection_prf_agent_obj_3 = world.get_location("Defection - Perfect Agent Objective 3")
        add_rule(defection_prf_agent_obj_3, lambda state: state.has_all(("Defection - Perfect Agent", "Data Uplink"), world.player)
                                                          and state.has("Progressive Weapon", world.player, 1))

        defection_prf_agent_obj_4 = world.get_location("Defection - Perfect Agent Objective 4")
        add_rule(defection_prf_agent_obj_4, lambda state: state.has_all(("Defection - Perfect Agent", "ECM Mine"), world.player)
                                                          and state.has("Progressive Weapon", world.player, 1))

        defection_prf_agent_obj_5 = world.get_location("Defection - Perfect Agent Objective 5")
        add_rule(defection_prf_agent_obj_5, lambda state: state.has_all(("Defection - Perfect Agent", "De Vries' Necklace"), world.player)
                                                          and state.has("Progressive Weapon", world.player, 1))

        defection_prf_agent_complete = world.get_location("Complete: Defection - Perfect Agent")
        add_rule(defection_prf_agent_complete, lambda state: state.has_all(("Defection - Perfect Agent", "ECM Mine", "De Vries' Necklace", "Data Uplink"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 1))


        # Stage 2 - Investigation
        investigation_prf_agent_obj_1 = world.get_location("Investigation - Perfect Agent Objective 1")
        add_rule(investigation_prf_agent_obj_1, lambda state: state.has_all(("Investigation - Perfect Agent", "CamSpy"), world.player))

        investigation_prf_agent_obj_2 = world.get_location("Investigation - Perfect Agent Objective 2")
        add_rule(investigation_prf_agent_obj_2, lambda state: state.has("Investigation - Perfect Agent", world.player))

        investigation_prf_agent_obj_3 = world.get_location("Investigation - Perfect Agent Objective 3")
        add_rule(investigation_prf_agent_obj_3, lambda state: state.has("Investigation - Perfect Agent", world.player)
                                                              and state.has("Progressive Weapon", world.player, 1))

        investigation_prf_agent_obj_4 = world.get_location("Investigation - Perfect Agent Objective 4")
        add_rule(investigation_prf_agent_obj_4, lambda state: (state.has_all(("Investigation - Perfect Agent", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                              or state.has_all(("Investigation - Perfect Agent", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 29))

        investigation_prf_agent_obj_5 = world.get_location("Investigation - Perfect Agent Objective 5")
        add_rule(investigation_prf_agent_obj_5, lambda state: (state.has_all(("Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                              or (state.has_all(("Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 29)))

        investigation_prf_agent_complete = world.get_location("Complete: Investigation - Perfect Agent")
        add_rule(investigation_prf_agent_complete, lambda state: (state.has_all(("Investigation - Perfect Agent", "CamSpy", "K7 Avenger", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 1))
                                                                 or (state.has_all(("Investigation - Perfect Agent", "CamSpy", "Night Vision", "Data Uplink", "Shield Tech Item"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 29)))
        

        # Stage 3 - Extraction
        extraction_prf_agent_obj_1 = world.get_location("Extraction - Perfect Agent Objective 1")
        add_rule(extraction_prf_agent_obj_1, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

        extraction_prf_agent_obj_2 = world.get_location("Extraction - Perfect Agent Objective 2")
        add_rule(extraction_prf_agent_obj_2, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

        extraction_prf_agent_obj_3 = world.get_location("Extraction - Perfect Agent Objective 3")
        add_rule(extraction_prf_agent_obj_3, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 3))
        
        extraction_prf_agent_obj_4 = world.get_location("Extraction - Perfect Agent Objective 4")
        add_rule(extraction_prf_agent_obj_4, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

        extraction_prf_agent_obj_5 = world.get_location("Extraction - Perfect Agent Objective 5")
        add_rule(extraction_prf_agent_obj_5, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

        extraction_prf_agent_complete = world.get_location("Complete: Extraction - Perfect Agent")
        add_rule(extraction_prf_agent_complete, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            # Given laser for certain weapons to prevent softlock
            add_rule(extraction_prf_agent_obj_3, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                               and state.has("Progressive Weapon", world.player, 1))
            
            add_rule(extraction_prf_agent_complete, lambda state: state.has_all(("Extraction - Perfect Agent", "Night Vision"), world.player)
                                                                  and state.has("Progressive Weapon", world.player, 1))


        # Stage 4 - Villa
        villa_prf_agent_obj_1 = world.get_location("Carrington Villa - Perfect Agent Objective 1")
        add_rule(villa_prf_agent_obj_1, lambda state: state.has("Carrington Villa - Perfect Agent", world.player)
                                                      and state.has("Progressive Weapon", world.player, 3))
        
        villa_prf_agent_obj_2 = world.get_location("Carrington Villa - Perfect Agent Objective 2")
        add_rule(villa_prf_agent_obj_2, lambda state: state.has("Carrington Villa - Perfect Agent", world.player)
                                                      and state.has("Progressive Weapon", world.player, 1))

        villa_prf_agent_obj_3 = world.get_location("Carrington Villa - Perfect Agent Objective 3")
        add_rule(villa_prf_agent_obj_3, lambda state: state.has("Carrington Villa - Perfect Agent", world.player)
                                                      and state.has("Progressive Weapon", world.player, 1))

        villa_prf_agent_obj_4 = world.get_location("Carrington Villa - Perfect Agent Objective 4")
        add_rule(villa_prf_agent_obj_4, lambda state: state.has("Carrington Villa - Perfect Agent", world.player))

        villa_prf_agent_obj_5 = world.get_location("Carrington Villa - Perfect Agent Objective 5")
        add_rule(villa_prf_agent_obj_5, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Cellar Key Card"), world.player)
                                                      and state.has("Progressive Weapon", world.player, 3))

        villa_prf_agent_complete = world.get_location("Complete: Carrington Villa - Perfect Agent")
        add_rule(villa_prf_agent_complete, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Cellar Key Card"), world.player)
                                                         and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            # Given laser for certain weapons to prevent softlock
            add_rule(villa_prf_agent_obj_1, lambda state: state.has("Carrington Villa - Perfect Agent", world.player)
                                                          and state.has("Progressive Weapon", world.player, 1))

            add_rule(villa_prf_agent_obj_5, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Cellar Key Card"), world.player)
                                                      and state.has("Progressive Weapon", world.player, 1))

            add_rule(villa_prf_agent_complete, lambda state: state.has_all(("Carrington Villa - Perfect Agent", "Cellar Key Card"), world.player)
                                                         and state.has("Progressive Weapon", world.player, 1))

        # Stage 5 - Chicago
        chicago_prf_agent_obj_1 = world.get_location("Chicago - Perfect Agent Objective 1")
        add_rule(chicago_prf_agent_obj_1, lambda state: (state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink"), world.player))
                                                        or (state.has_all(("Chicago - Perfect Agent", "Data Uplink"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 27)))

        chicago_prf_agent_obj_2 = world.get_location("Chicago - Perfect Agent Objective 2")
        add_rule(chicago_prf_agent_obj_2, lambda state: state.has_all(("Chicago - Perfect Agent", "Tracer Bug"), world.player))

        chicago_prf_agent_obj_3 = world.get_location("Chicago - Perfect Agent Objective 3")
        add_rule(chicago_prf_agent_obj_3, lambda state: (state.has_all(("Chicago - Perfect Agent", "Remote Mine"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                        or (state.has("Chicago - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 27)))

        chicago_prf_agent_obj_4 = world.get_location("Chicago - Perfect Agent Objective 4")
        add_rule(chicago_prf_agent_obj_4, lambda state: (state.has_all(("Chicago - Perfect Agent", "Data Uplink"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                        or (state.has_all(("Chicago - Perfect Agent", "CamSpy"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 2)))

        chicago_prf_agent_obj_5 = world.get_location("Chicago - Perfect Agent Objective 5")
        add_rule(chicago_prf_agent_obj_5, lambda state: (state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug"), world.player) 
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                        or (state.has_all(("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug"), world.player) 
                                                            and state.has("Progressive Weapon", world.player, 27)))
        
        chicago_prf_agent_complete = world.get_location("Complete: Chicago - Perfect Agent")
        add_rule(chicago_prf_agent_complete, lambda state: (state.has_all(("Chicago - Perfect Agent", "Remote Mine", "Data Uplink", "Tracer Bug"), world.player) 
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                           or (state.has_all(("Chicago - Perfect Agent", "Data Uplink", "Tracer Bug"), world.player) 
                                                                and state.has("Progressive Weapon", world.player, 27)))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            # Given laser
            add_rule(chicago_prf_agent_obj_4, lambda state: (state.has_all(("Chicago - Perfect Agent", "Data Uplink"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                            or (state.has_all(("Chicago - Perfect Agent", "CamSpy"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1)))


        # Stage 6 - G5 Building
        g5_prf_agent_obj_1 = world.get_location("G5 Building - Perfect Agent Objective 1")
        add_rule(g5_prf_agent_obj_1, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card"), world.player)
                                                   and state.has("Progressive Weapon", world.player, 1))

        g5_prf_agent_obj_2 = world.get_location("G5 Building - Perfect Agent Objective 2")
        add_rule(g5_prf_agent_obj_2, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card"), world.player)
                                                   and state.has("Progressive Weapon", world.player, 1))

        g5_prf_agent_obj_3 = world.get_location("G5 Building - Perfect Agent Objective 3")
        add_rule(g5_prf_agent_obj_3, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CamSpy"), world.player)
                                                   and state.has("Progressive Weapon", world.player, 1))

        g5_prf_agent_obj_4 = world.get_location("G5 Building - Perfect Agent Objective 4")
        add_rule(g5_prf_agent_obj_4, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Door Decoder", "Backup Disk"), world.player)
                                                   and state.has("Progressive Weapon", world.player, 1))

        g5_prf_agent_obj_5 = world.get_location("G5 Building - Perfect Agent Objective 5")
        add_rule(g5_prf_agent_obj_5, lambda state: (state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Remote Mine"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))
                                                   or (state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 27)))

        g5_prf_agent_complete = world.get_location("Complete: G5 Building - Perfect Agent")
        add_rule(g5_prf_agent_complete, lambda state: (state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))
                                                      or (state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CamSpy", "Door Decoder", "Backup Disk"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 27)))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(g5_prf_agent_obj_5, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "Remote Mine"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 1))

            add_rule(g5_prf_agent_complete, lambda state: state.has_all(("G5 Building - Perfect Agent", "G5 Building Level 1 Key Card", "G5 Building Level 2 Key Card", "CamSpy", "Door Decoder", "Backup Disk", "Remote Mine"), world.player)
                                                          and state.has("Progressive Weapon", world.player, 1))


        # Stage 7 - Infiltration
        infiltration_prf_agent_obj_1 = world.get_location("Infiltration - Perfect Agent Objective 1")
        add_rule(infiltration_prf_agent_obj_1, lambda state: state.has_all(("Infiltration - Perfect Agent", "Explosives"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 1))

        infiltration_prf_agent_obj_2 = world.get_location("Infiltration - Perfect Agent Objective 2")
        add_rule(infiltration_prf_agent_obj_2, lambda state: state.has_all(("Infiltration - Perfect Agent", "Comms Rider"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 1))

        infiltration_prf_agent_obj_3 = world.get_location("Infiltration - Perfect Agent Objective 3")
        add_rule(infiltration_prf_agent_obj_3, lambda state: state.has("Infiltration - Perfect Agent", world.player)
                                                             and state.has("Progressive Weapon", world.player, 3))

        infiltration_prf_agent_obj_4 = world.get_location("Infiltration - Perfect Agent Objective 4")
        add_rule(infiltration_prf_agent_obj_4, lambda state: state.has_all(("Infiltration - Perfect Agent", "Area 51 Lift Key Card"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 1))

        infiltration_prf_agent_obj_5 = world.get_location("Infiltration - Perfect Agent Objective 5")
        add_rule(infiltration_prf_agent_obj_5, lambda state: state.has_all(("Infiltration - Perfect Agent", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 3))

        infiltration_prf_agent_complete = world.get_location("Complete: Infiltration - Perfect Agent")
        add_rule(infiltration_prf_agent_complete, lambda state: state.has_all(("Infiltration - Perfect Agent", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 3))

        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(infiltration_prf_agent_obj_3, lambda state: state.has("Infiltration - Perfect Agent", world.player)
                                                                 and state.has("Progressive Weapon", world.player, 1))

            add_rule(infiltration_prf_agent_obj_5, lambda state: state.has_all(("Infiltration - Perfect Agent", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))

            add_rule(infiltration_prf_agent_complete, lambda state: state.has_all(("Infiltration - Perfect Agent", "Explosives", "Comms Rider", "Area 51 Lift Key Card"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 1))


        # Stage 8 - Rescue
        rescue_prf_agent_obj_1 = world.get_location("Rescue - Perfect Agent Objective 1")
        add_rule(rescue_prf_agent_obj_1, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        rescue_prf_agent_obj_2 = world.get_location("Rescue - Perfect Agent Objective 2")
        add_rule(rescue_prf_agent_obj_2, lambda state: state.has_all(("Rescue - Perfect Agent", "X-Ray Scanner"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        rescue_prf_agent_obj_3 = world.get_location("Rescue - Perfect Agent Objective 3")
        add_rule(rescue_prf_agent_obj_3, lambda state: state.has_all(("Rescue - Perfect Agent", "Lab Clothes"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        rescue_prf_agent_obj_4 = world.get_location("Rescue - Perfect Agent Objective 4")
        add_rule(rescue_prf_agent_obj_4, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        rescue_prf_agent_obj_5 = world.get_location("Rescue - Perfect Agent Objective 5")
        add_rule(rescue_prf_agent_obj_5, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))
        
        rescue_prf_agent_complete = world.get_location("Complete: Rescue - Perfect Agent")
        add_rule(rescue_prf_agent_complete, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(rescue_prf_agent_obj_1, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 1))

            add_rule(rescue_prf_agent_obj_2, lambda state: state.has_all(("Rescue - Perfect Agent", "X-Ray Scanner"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

            add_rule(rescue_prf_agent_obj_3, lambda state: state.has_all(("Rescue - Perfect Agent", "Lab Clothes"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

            add_rule(rescue_prf_agent_obj_4, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

            add_rule(rescue_prf_agent_obj_5, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))
            
            add_rule(rescue_prf_agent_complete, lambda state: state.has_all(("Rescue - Perfect Agent", "Data Uplink", "X-Ray Scanner", "Lab Clothes", "Medlab 2 Key Card", "Op Room Key Card"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

        # Stage 9 - Escape
        escape_prf_agent_obj_1 = world.get_location("Escape - Perfect Agent Objective 1")
        add_rule(escape_prf_agent_obj_1, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        escape_prf_agent_obj_2 = world.get_location("Escape - Perfect Agent Objective 2")
        add_rule(escape_prf_agent_obj_2, lambda state: state.has("Escape - Perfect Agent", world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        escape_prf_agent_obj_3 = world.get_location("Escape - Perfect Agent Objective 3")
        add_rule(escape_prf_agent_obj_3, lambda state: state.has("Escape - Perfect Agent", world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        escape_prf_agent_obj_4 = world.get_location("Escape - Perfect Agent Objective 4")
        add_rule(escape_prf_agent_obj_4, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))

        escape_prf_agent_obj_5 = world.get_location("Escape - Perfect Agent Objective 5")
        add_rule(escape_prf_agent_obj_5, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))
        
        escape_prf_agent_complete = world.get_location("Complete: Escape - Perfect Agent")
        add_rule(escape_prf_agent_complete, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                          and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(escape_prf_agent_obj_1, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

            add_rule(escape_prf_agent_obj_2, lambda state: state.has("Escape - Perfect Agent", world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

            add_rule(escape_prf_agent_obj_3, lambda state: state.has("Escape - Perfect Agent", world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

            add_rule(escape_prf_agent_obj_4, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

            add_rule(escape_prf_agent_obj_5, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))
            
            add_rule(escape_prf_agent_complete, lambda state: state.has_all(("Escape - Perfect Agent", "Alien Medpack"), world.player)
                                                              and state.has("Progressive Weapon", world.player, 1))


        # Stage 10 - Air Base
        air_base_prf_agent_obj_1 = world.get_location("Air Base - Perfect Agent Objective 1")
        add_rule(air_base_prf_agent_obj_1, lambda state: (state.has_all(("Air Base - Perfect Agent", "Stewardess Disguise"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 2))
                                                         or (state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"), world.player)))

        air_base_prf_agent_obj_2 = world.get_location("Air Base - Perfect Agent Objective 2")
        add_rule(air_base_prf_agent_obj_2, lambda state: (state.has_all(("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 2))
                                                         or (state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"), world.player)))

        air_base_prf_agent_obj_3 = world.get_location("Air Base - Perfect Agent Objective 3")
        add_rule(air_base_prf_agent_obj_3, lambda state: (state.has_all(("Air Base - Perfect Agent", "Stewardess Disguise"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 2))
                                                         or (state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"), world.player)))

        air_base_prf_agent_obj_4 = world.get_location("Air Base - Perfect Agent Objective 4")
        add_rule(air_base_prf_agent_obj_4, lambda state: state.has_all(("Air Base - Perfect Agent", "Stewardess Disguise", "Flight Plans"), world.player)
                                                         and state.has("Progressive Weapon", world.player, 18))

        air_base_prf_agent_obj_5 = world.get_location("Air Base - Perfect Agent Objective 5")
        add_rule(air_base_prf_agent_obj_5, lambda state: state.has_all(("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                         and state.has("Progressive Weapon", world.player, 18))
        
        air_base_prf_agent_complete = world.get_location("Complete: Air Base - Perfect Agent")
        add_rule(air_base_prf_agent_complete, lambda state: state.has_all(("Air Base - Perfect Agent", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 18))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(air_base_prf_agent_obj_1, lambda state: state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"), world.player))

            add_rule(air_base_prf_agent_obj_2, lambda state: state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase"), world.player))

            add_rule(air_base_prf_agent_obj_3, lambda state: state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise"), world.player))
            
            # Given your weapon back
            add_rule(air_base_prf_agent_obj_4, lambda state: state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Flight Plans"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 2))

            add_rule(air_base_prf_agent_obj_5, lambda state: state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 2))
            
            add_rule(air_base_prf_agent_complete, lambda state: state.has_all(("Air Base - Perfect Agent", "CamSpy", "Stewardess Disguise", "Suitcase", "Flight Plans"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 2))


        # Stage 11 - Air Force One
        air_force_one_prf_agent_obj_1 = world.get_location("Air Force One - Perfect Agent Objective 1")
        add_rule(air_force_one_prf_agent_obj_1, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player))

        air_force_one_prf_agent_obj_2 = world.get_location("Air Force One - Perfect Agent Objective 2")
        add_rule(air_force_one_prf_agent_obj_2, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player))

        air_force_one_prf_agent_obj_3 = world.get_location("Air Force One - Perfect Agent Objective 3")
        add_rule(air_force_one_prf_agent_obj_3, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player)
                                                              and state.has("Progressive Weapon", world.player, 1))

        air_force_one_prf_agent_obj_4 = world.get_location("Air Force One - Perfect Agent Objective 4")
        add_rule(air_force_one_prf_agent_obj_4, lambda state: (state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Timed Mine"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                              or (state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 24)))

        air_force_one_prf_agent_obj_5 = world.get_location("Air Force One - Perfect Agent Objective 5")
        add_rule(air_force_one_prf_agent_obj_5, lambda state: (state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Timed Mine"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                              or (state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 24)))

        air_force_one_prf_agent_complete = world.get_location("Complete: Air Force One - Perfect Agent")
        add_rule(air_force_one_prf_agent_complete, lambda state: (state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Timed Mine"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 1))
                                                                 or (state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 24)))

        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(air_force_one_prf_agent_obj_4, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Timed Mine"), world.player)
                                                                  and state.has("Progressive Weapon", world.player, 1))

            add_rule(air_force_one_prf_agent_obj_5, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Timed Mine"), world.player)
                                                                  and state.has("Progressive Weapon", world.player, 1))

            add_rule(air_force_one_prf_agent_complete, lambda state: state.has_all(("Air Force One - Perfect Agent", "Air Force One Key Cards", "Suitcase", "Timed Mine"), world.player)
                                                                     and state.has("Progressive Weapon", world.player, 1))


        # Stage 12 - Crash Site
        crash_site_prf_agent_obj_1 = world.get_location("Crash Site - Perfect Agent Objective 1")
        add_rule(crash_site_prf_agent_obj_1, lambda state: state.has_all(("Crash Site - Perfect Agent", "President Scanner"), world.player))

        crash_site_prf_agent_obj_2 = world.get_location("Crash Site - Perfect Agent Objective 2")
        add_rule(crash_site_prf_agent_obj_2, lambda state: state.has("Crash Site - Perfect Agent", world.player))

        crash_site_prf_agent_obj_3 = world.get_location("Crash Site - Perfect Agent Objective 3")
        add_rule(crash_site_prf_agent_obj_3, lambda state: state.has("Crash Site - Perfect Agent", world.player)
                                                           and state.has("Progressive Weapon", world.player, 3))

        crash_site_prf_agent_obj_4 = world.get_location("Crash Site - Perfect Agent Objective 4")
        add_rule(crash_site_prf_agent_obj_4, lambda state: state.has_all(("Crash Site - Perfect Agent", "President Scanner"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 1))

        crash_site_prf_agent_obj_5 = world.get_location("Crash Site - Perfect Agent Objective 5")
        add_rule(crash_site_prf_agent_obj_5, lambda state: state.has_all(("Crash Site - Perfect Agent", "President Scanner"), world.player)
                                                           and state.has("Progressive Weapon", world.player, 3))
        
        crash_site_prf_agent_complete = world.get_location("Complete: Crash Site - Perfect Agent")
        add_rule(crash_site_prf_agent_complete, lambda state: state.has_all(("Crash Site - Perfect Agent", "President Scanner"), world.player)
                                                              and state.has("Progressive Weapon", world.player, 3))

        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(crash_site_prf_agent_obj_3, lambda state: state.has("Crash Site - Perfect Agent", world.player)
                                                               and state.has("Progressive Weapon", world.player, 1))


        # Stage 13 - Pelagic II
        pelagic_prf_agent_obj_1 = world.get_location("Pelagic II - Perfect Agent Objective 1")
        add_rule(pelagic_prf_agent_obj_1, lambda state: state.has_all(("Pelagic II - Perfect Agent", "X-Ray Scanner"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

        pelagic_prf_agent_obj_2 = world.get_location("Pelagic II - Perfect Agent Objective 2")
        add_rule(pelagic_prf_agent_obj_2, lambda state: state.has_all(("Pelagic II - Perfect Agent", "Research Tape"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

        pelagic_prf_agent_obj_3 = world.get_location("Pelagic II - Perfect Agent Objective 3")
        add_rule(pelagic_prf_agent_obj_3, lambda state: state.has("Pelagic II - Perfect Agent", world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

        pelagic_prf_agent_obj_4 = world.get_location("Pelagic II - Perfect Agent Objective 4")
        add_rule(pelagic_prf_agent_obj_4, lambda state: state.has("Pelagic II - Perfect Agent", world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))

        pelagic_prf_agent_obj_5 = world.get_location("Pelagic II - Perfect Agent Objective 5")
        add_rule(pelagic_prf_agent_obj_5, lambda state: state.has_all(("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))
        
        pelagic_prf_agent_complete = world.get_location("Complete: Pelagic II - Perfect Agent")
        add_rule(pelagic_prf_agent_complete, lambda state: state.has_all(("Pelagic II - Perfect Agent", "X-Ray Scanner", "Research Tape"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))


        # Stage 14 - Deep Sea
        deep_sea_prf_agent_obj_1 = world.get_location("Deep Sea - Perfect Agent Objective 1")
        add_rule(deep_sea_prf_agent_obj_1, lambda state: state.has_all(("Deep Sea - Perfect Agent", "IR Scanner"), world.player)
                                                         and state.has("Progressive Weapon", world.player, 2))

        deep_sea_prf_agent_obj_2 = world.get_location("Deep Sea - Perfect Agent Objective 2")
        add_rule(deep_sea_prf_agent_obj_2, lambda state: (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                         or (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 42)))

        deep_sea_prf_agent_obj_3 = world.get_location("Deep Sea - Perfect Agent Objective 3")
        add_rule(deep_sea_prf_agent_obj_3, lambda state: (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                         or (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 42)))

        deep_sea_prf_agent_obj_4 = world.get_location("Deep Sea - Perfect Agent Objective 4")
        add_rule(deep_sea_prf_agent_obj_4, lambda state: (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                         or (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 42)))

        deep_sea_prf_agent_obj_5 = world.get_location("Deep Sea - Perfect Agent Objective 5")
        add_rule(deep_sea_prf_agent_obj_5, lambda state: (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))
                                                         or (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk"), world.player)
                                                            and state.has("Progressive Weapon", world.player, 42)))
        
        deep_sea_prf_agent_complete = world.get_location("Complete: Deep Sea - Perfect Agent")
        add_rule(deep_sea_prf_agent_complete, lambda state: (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "FarSight XR-20", "Backup Disk"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))
                                                            or (state.has_all(("Deep Sea - Perfect Agent", "IR Scanner", "Backup Disk"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 42)))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(deep_sea_prf_agent_obj_1, lambda state: state.has_all(("Deep Sea - Perfect Agent", "IR Scanner"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 1))


        # Stage 15 - Carrington Institute Defense
        institute_defense_prf_agent_obj_1 = world.get_location("Carrington Institute - Perfect Agent Objective 1")
        add_rule(institute_defense_prf_agent_obj_1, lambda state: state.has("Carrington Institute - Perfect Agent", world.player))

        institute_defense_prf_agent_obj_2 = world.get_location("Carrington Institute - Perfect Agent Objective 2")
        add_rule(institute_defense_prf_agent_obj_2, lambda state: state.has("Carrington Institute - Perfect Agent", world.player)
                                                                  and state.has("Progressive Weapon", world.player, 15))

        institute_defense_prf_agent_obj_3 = world.get_location("Carrington Institute - Perfect Agent Objective 3")
        add_rule(institute_defense_prf_agent_obj_3, lambda state: (state.has_all(("Carrington Institute - Perfect Agent", "RC-P120"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 15))
                                                                  or (state.has("Carrington Institute - Perfect Agent", world.player)
                                                                    and state.has("Progressive Weapon", world.player, 40)))

        institute_defense_prf_agent_obj_4 = world.get_location("Carrington Institute - Perfect Agent Objective 4")
        add_rule(institute_defense_prf_agent_obj_4, lambda state: (state.has("Carrington Institute - Perfect Agent", world.player)
                                                                        and state.has("Progressive Weapon", world.player, 18))
                                                                  or (state.has_all(("Carrington Institute - Perfect Agent", "RC-P120"), world.player)
                                                                        and state.has("Progressive Weapon", world.player, 15)))

        institute_defense_prf_agent_obj_5 = world.get_location("Carrington Institute - Perfect Agent Objective 5")
        add_rule(institute_defense_prf_agent_obj_5, lambda state: (state.has_all(("Carrington Institute - Perfect Agent", "Data Uplink"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 40))
                                                                  or (state.has_all(("Carrington Institute - Perfect Agent", "RC-P120", "Data Uplink"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 15)))

        institute_defense_prf_agent_complete = world.get_location("Complete: Carrington Institute - Perfect Agent")
        add_rule(institute_defense_prf_agent_complete, lambda state: (state.has_all(("Carrington Institute - Perfect Agent", "Data Uplink"), world.player)
                                                                        and state.has("Progressive Weapon", world.player, 40))
                                                                    or (state.has_all(("Carrington Institute - Perfect Agent", "RC-P120", "Data Uplink"), world.player)
                                                                        and state.has("Progressive Weapon", world.player, 15)))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(institute_defense_prf_agent_obj_3, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "RC-P120"), world.player)
                                                                      and state.has("Progressive Weapon", world.player, 15))

            add_rule(institute_defense_prf_agent_obj_4, lambda state: (state.has_all(("Carrington Institute - Perfect Agent", "RC-P120"), world.player)
                                                                            and state.has("Progressive Weapon", world.player, 15))
                                                                      or (state.has_all(("Carrington Institute - Perfect Agent", "Devastator"), world.player)))

            add_rule(institute_defense_prf_agent_obj_5, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "RC-P120", "Data Uplink"), world.player)
                                                                      and state.has("Progressive Weapon", world.player, 15))

            add_rule(institute_defense_prf_agent_complete, lambda state: state.has_all(("Carrington Institute - Perfect Agent", "RC-P120", "Data Uplink"), world.player)
                                                                         and state.has("Progressive Weapon", world.player, 15))


        # Stage 16 - Attack Ship
        attack_ship_prf_agent_obj_1 = world.get_location("Attack Ship - Perfect Agent Objective 1")
        add_rule(attack_ship_prf_agent_obj_1, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 3))

        attack_ship_prf_agent_obj_2 = world.get_location("Attack Ship - Perfect Agent Objective 2")
        add_rule(attack_ship_prf_agent_obj_2, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 3))

        attack_ship_prf_agent_obj_3 = world.get_location("Attack Ship - Perfect Agent Objective 3")
        add_rule(attack_ship_prf_agent_obj_3, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 3))

        attack_ship_prf_agent_obj_4 = world.get_location("Attack Ship - Perfect Agent Objective 4")
        add_rule(attack_ship_prf_agent_obj_4, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 3))

        attack_ship_prf_agent_obj_5 = world.get_location("Attack Ship - Perfect Agent Objective 5")
        add_rule(attack_ship_prf_agent_obj_5, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 3))

        attack_ship_prf_agent_complete = world.get_location("Complete: Attack Ship - Perfect Agent")
        add_rule(attack_ship_prf_agent_complete, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                               and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(attack_ship_prf_agent_obj_1, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))

            add_rule(attack_ship_prf_agent_obj_2, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))

            add_rule(attack_ship_prf_agent_obj_3, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))

            add_rule(attack_ship_prf_agent_obj_4, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))

            add_rule(attack_ship_prf_agent_obj_5, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))

            add_rule(attack_ship_prf_agent_complete, lambda state: state.has("Attack Ship - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))


        # Stage 17 - Skedar Ruins
        skedar_ruins_prf_agent_obj_1 = world.get_location("Skedar Ruins - Perfect Agent Objective 1")
        add_rule(skedar_ruins_prf_agent_obj_1, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "R-Tracker", "Target Amplifier"), world.player)
                                                             and state.has("Progressive Weapon", world.player, 3))

        skedar_ruins_prf_agent_obj_2 = world.get_location("Skedar Ruins - Perfect Agent Objective 2")
        add_rule(skedar_ruins_prf_agent_obj_2, lambda state: (state.has_all(("Skedar Ruins - Perfect Agent", "Devastator"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 3))
                                                             or (state.has("Skedar Ruins - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 24)))

        skedar_ruins_prf_agent_obj_3 = world.get_location("Skedar Ruins - Perfect Agent Objective 3")
        add_rule(skedar_ruins_prf_agent_obj_3, lambda state: (state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "IR Scanner"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 3))
                                                             or (state.has_all(("Skedar Ruins - Perfect Agent", "IR Scanner"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 24)))

        skedar_ruins_prf_agent_obj_4 = world.get_location("Skedar Ruins - Perfect Agent Objective 4")
        add_rule(skedar_ruins_prf_agent_obj_4, lambda state: (state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "IR Scanner"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 4))
                                                             or (state.has_all(("Skedar Ruins - Perfect Agent", "IR Scanner"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 24)))

        skedar_ruins_prf_agent_obj_5 = world.get_location("Skedar Ruins - Perfect Agent Objective 5")
        add_rule(skedar_ruins_prf_agent_obj_5, lambda state: (state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "IR Scanner"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 4))
                                                             or (state.has_all(("Skedar Ruins - Perfect Agent", "IR Scanner"), world.player)
                                                                and state.has("Progressive Weapon", world.player, 24)))

        skedar_ruins_prf_agent_complete = world.get_location("Complete: Skedar Ruins - Perfect Agent")
        add_rule(skedar_ruins_prf_agent_complete, lambda state: (state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 4))
                                                                or (state.has_all(("Skedar Ruins - Perfect Agent", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
                                                                    and state.has("Progressive Weapon", world.player, 24)))

        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(skedar_ruins_prf_agent_obj_1, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "R-Tracker", "Target Amplifier"), world.player)
                                                                 and state.has("Progressive Weapon", world.player, 3))

            add_rule(skedar_ruins_prf_agent_obj_2, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Devastator"), world.player)
                                                                 and state.has("Progressive Weapon", world.player, 3))

            add_rule(skedar_ruins_prf_agent_obj_3, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "IR Scanner"), world.player)
                                                                 and state.has("Progressive Weapon", world.player, 3))

            add_rule(skedar_ruins_prf_agent_obj_4, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "IR Scanner"), world.player)
                                                                 and state.has("Progressive Weapon", world.player, 3))

            add_rule(skedar_ruins_prf_agent_obj_5, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "IR Scanner"), world.player)
                                                                 and state.has("Progressive Weapon", world.player, 3))

            add_rule(skedar_ruins_prf_agent_complete, lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
                                                                        and state.has("Progressive Weapon", world.player, 3))


        # Stage 18 - Mr. Blonde's Revenge
        mbr_prf_agent_obj_1 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 1")
        add_rule(mbr_prf_agent_obj_1, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb"), world.player))

        mbr_prf_agent_obj_2 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 2")
        add_rule(mbr_prf_agent_obj_2, lambda state: (state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1))
                                                    or (state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "CamSpy", "Cloaking Device"), world.player)))

        mbr_prf_agent_obj_3 = world.get_location("Mr. Blonde's Revenge - Perfect Agent Objective 3")
        add_rule(mbr_prf_agent_obj_3, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 1))

        mbr_prf_agent_complete = world.get_location("Complete: Mr. Blonde's Revenge - Perfect Agent")
        add_rule(mbr_prf_agent_complete, lambda state: state.has_all(("Mr. Blonde's Revenge - Perfect Agent", "Cloaking Device", "Skedar Bomb"), world.player)
                                                       and state.has("Progressive Weapon", world.player, 1))


        # Stage 19 - Maian SOS
        maian_sos_prf_agent_obj_1 = world.get_location("Maian SOS - Perfect Agent Objective 1")
        add_rule(maian_sos_prf_agent_obj_1, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                          and state.has("Progressive Weapon", world.player, 3))

        maian_sos_prf_agent_obj_2 = world.get_location("Maian SOS - Perfect Agent Objective 2")
        add_rule(maian_sos_prf_agent_obj_2, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                          and state.has("Progressive Weapon", world.player, 3))

        maian_sos_prf_agent_obj_3 = world.get_location("Maian SOS - Perfect Agent Objective 3")
        add_rule(maian_sos_prf_agent_obj_3, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                          and state.has("Progressive Weapon", world.player, 3))

        maian_sos_prf_agent_complete = world.get_location("Complete: Maian SOS - Perfect Agent")
        add_rule(maian_sos_prf_agent_complete, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                             and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(maian_sos_prf_agent_obj_1, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))

            add_rule(maian_sos_prf_agent_obj_2, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))

            add_rule(maian_sos_prf_agent_obj_3, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                            and state.has("Progressive Weapon", world.player, 1))

            add_rule(maian_sos_prf_agent_complete, lambda state: state.has("Maian SOS - Perfect Agent", world.player)
                                                                and state.has("Progressive Weapon", world.player, 1))


        # Stage 20 - WAR!
        war_prf_agent_obj_1 = world.get_location("WAR! - Perfect Agent Objective 1")
        add_rule(war_prf_agent_obj_1, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                    and state.has("Progressive Weapon", world.player, 3))

        war_prf_agent_obj_2 = world.get_location("WAR! - Perfect Agent Objective 2")
        add_rule(war_prf_agent_obj_2, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                    and state.has("Progressive Weapon", world.player, 3))

        war_prf_agent_obj_3 = world.get_location("WAR! - Perfect Agent Objective 3")
        add_rule(war_prf_agent_obj_3, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                    and state.has("Progressive Weapon", world.player, 3))

        war_prf_agent_complete = world.get_location("Complete: WAR! - Perfect Agent")
        add_rule(war_prf_agent_complete, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                       and state.has("Progressive Weapon", world.player, 3))
        
        if world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            add_rule(war_prf_agent_obj_1, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                        and state.has("Progressive Weapon", world.player, 2))

            add_rule(war_prf_agent_obj_2, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                        and state.has("Progressive Weapon", world.player, 2))

            add_rule(war_prf_agent_obj_3, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                        and state.has("Progressive Weapon", world.player, 2))

            add_rule(war_prf_agent_complete, lambda state: state.has("WAR! - Perfect Agent", world.player)
                                                        and state.has("Progressive Weapon", world.player, 2))

        # Stage 21 - The Duel
        duel_prf_agent_obj_1 = world.get_location("The Duel - Perfect Agent Objective 1")
        add_rule(duel_prf_agent_obj_1, lambda state: state.has("The Duel - Perfect Agent", world.player)
                                                     and state.has("Progressive Weapon", world.player, 1))

        duel_prf_agent_obj_2 = world.get_location("The Duel - Perfect Agent Objective 2")
        add_rule(duel_prf_agent_obj_2, lambda state: state.has("The Duel - Perfect Agent", world.player)
                                                     and state.has("Progressive Weapon", world.player, 1))

        duel_prf_agent_obj_3 = world.get_location("The Duel - Perfect Agent Objective 3")
        add_rule(duel_prf_agent_obj_3, lambda state: state.has("The Duel - Perfect Agent", world.player)
                                                     and state.has("Progressive Weapon", world.player, 1))
        
        duel_prf_agent_complete = world.get_location("Complete: The Duel - Perfect Agent")
        add_rule(duel_prf_agent_complete, lambda state: state.has("The Duel - Perfect Agent", world.player)
                                                     and state.has("Progressive Weapon", world.player, 1))
        
        if world.options.challenges:
            challenge_1 = world.get_location("Complete: Challenge 1")
            add_rule(challenge_1, lambda state: state.has("Challenge 1", world.player)
                                                and state.has("Progressive Weapon", world.player, 18))

            challenge_2 = world.get_location("Complete: Challenge 2")
            add_rule(challenge_2, lambda state: state.has("Challenge 2", world.player)
                                                and state.has("Progressive Weapon", world.player, 34))

            challenge_3 = world.get_location("Complete: Challenge 3")
            add_rule(challenge_3, lambda state: (state.has_all(("Challenge 3", "Timed Mine"), world.player))
                                                or (state.has("Challenge 3", world.player)
                                                    and state.has("Progressive Weapon", world.player, 24)))

            challenge_4 = world.get_location("Complete: Challenge 4")
            add_rule(challenge_4, lambda state: (state.has_all(("Challenge 4", "K7 Avenger"), world.player))
                                                or (state.has("Challenge 4", world.player)
                                                    and state.has("Progressive Weapon", world.player, 29)))

            challenge_5 = world.get_location("Complete: Challenge 5")
            add_rule(challenge_5, lambda state: (state.has_all(("Challenge 5", "FarSight XR-20"), world.player))
                                                or (state.has("Challenge 5", world.player)
                                                    and state.has("Progressive Weapon", world.player, 42)))

            challenge_6 = world.get_location("Complete: Challenge 6")
            add_rule(challenge_6, lambda state: (state.has_all(("Challenge 6", "Briefcase", "K7 Avenger"), world.player))
                                                or (state.has_all(("Challenge 6", "Briefcase"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 29)))

            challenge_7 = world.get_location("Complete: Challenge 7")
            add_rule(challenge_7, lambda state: state.has("Challenge 7", world.player)
                                                and state.has("Progressive Weapon", world.player, 25))

            challenge_8 = world.get_location("Complete: Challenge 8")
            add_rule(challenge_8, lambda state: state.has_all(("Challenge 8", "Briefcase"), world.player)
                                                and state.has("Progressive Weapon", world.player, 32))

            challenge_9 = world.get_location("Complete: Challenge 9")
            add_rule(challenge_9, lambda state: (state.has_all(("Challenge 9", "FarSight XR-20"), world.player))
                                                or (state.has("Challenge 9", world.player)
                                                    and state.has("Progressive Weapon", world.player, 42)))

            challenge_10 = world.get_location("Complete: Challenge 10")
            add_rule(challenge_10, lambda state: (state.has_all(("Challenge 10", "Data Uplink", "Remote Mine"), world.player))
                                                 or (state.has_all(("Challenge 10", "Data Uplink"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 27)))

            challenge_11 = world.get_location("Complete: Challenge 11")
            add_rule(challenge_11, lambda state: state.has("Challenge 11", world.player)
                                                 and state.has("Progressive Weapon", world.player, 13))

            challenge_12 = world.get_location("Complete: Challenge 12")
            add_rule(challenge_12, lambda state: state.has("Challenge 12", world.player)
                                                 and state.has("Progressive Weapon", world.player, 32))

            challenge_13 = world.get_location("Complete: Challenge 13")
            add_rule(challenge_13, lambda state: state.has("Challenge 13", world.player)
                                                 and state.has("Progressive Weapon", world.player, 25))

            challenge_14 = world.get_location("Complete: Challenge 14")
            add_rule(challenge_14, lambda state: (state.has_all(("Challenge 14", "Briefcase", "Cloaking Device", "FarSight XR-20"), world.player))
                                                 or (state.has_all(("Challenge 14", "Briefcase", "Cloaking Device"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 42)))

            challenge_15 = world.get_location("Complete: Challenge 15")
            add_rule(challenge_15, lambda state: state.has_all(("Challenge 15", "Briefcase"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 35))

            challenge_16 = world.get_location("Complete: Challenge 16")
            add_rule(challenge_16, lambda state: state.has("Challenge 16", world.player)
                                                 and state.has("Progressive Weapon", world.player, 32))

            challenge_17 = world.get_location("Complete: Challenge 17")
            add_rule(challenge_17, lambda state: state.has("Challenge 17", world.player)
                                                 and state.has("Progressive Weapon", world.player, 33))

            challenge_18 = world.get_location("Complete: Challenge 18")
            add_rule(challenge_18, lambda state: state.has_all(("Challenge 18", "Cloaking Device"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 22))

            challenge_19 = world.get_location("Complete: Challenge 19")
            add_rule(challenge_19, lambda state: (state.has_all(("Challenge 19", "FarSight XR-20"), world.player))
                                                 or (state.has("Challenge 19", world.player)
                                                    and state.has("Progressive Weapon", world.player, 42)))

            challenge_20 = world.get_location("Complete: Challenge 20")
            add_rule(challenge_20, lambda state: state.has("Challenge 20", world.player)
                                                 and state.has("Progressive Weapon", world.player, 37))

            challenge_21 = world.get_location("Complete: Challenge 21")
            add_rule(challenge_21, lambda state: state.has_all(("Challenge 21", "Data Uplink", "Cloaking Device"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 37))

            challenge_22 = world.get_location("Complete: Challenge 22")
            add_rule(challenge_22, lambda state: state.has_all(("Challenge 22", "Briefcase"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 36))

            challenge_23 = world.get_location("Complete: Challenge 23")
            add_rule(challenge_23, lambda state: state.has("Challenge 23", world.player)
                                                 and state.has("Progressive Weapon", world.player, 40))

            challenge_24 = world.get_location("Complete: Challenge 24")
            add_rule(challenge_24, lambda state: state.has_all(("Challenge 24", "Briefcase"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 41))

            challenge_25 = world.get_location("Complete: Challenge 25")
            add_rule(challenge_25, lambda state: (state.has_all(("Challenge 25", "Cloaking Device"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 42)))

            challenge_26 = world.get_location("Complete: Challenge 26")
            add_rule(challenge_26, lambda state: state.has("Challenge 26", world.player)
                                                 and state.has("Progressive Weapon", world.player, 37))

            challenge_27 = world.get_location("Complete: Challenge 27")
            add_rule(challenge_27, lambda state: state.has_all(("Challenge 27", "Data Uplink"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 34))

            challenge_28 = world.get_location("Complete: Challenge 28")
            add_rule(challenge_28, lambda state: state.has_all(("Challenge 28", "Briefcase"), world.player)
                                                 and state.has("Progressive Weapon", world.player, 21))

            challenge_29 = world.get_location("Complete: Challenge 29")
            add_rule(challenge_29, lambda state: state.has("Challenge 29", world.player)
                                                 and state.has("Progressive Weapon", world.player, 19))

            challenge_30 = world.get_location("Complete: Challenge 30")
            add_rule(challenge_30, lambda state: state.has("Challenge 30", world.player)
                                                 and state.has("Progressive Weapon", world.player, 37))
            
            if world.options.prog_weapon_in_challenges and world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon:
                add_rule(challenge_1, lambda state: state.has("Challenge 1", world.player)
                                                    and state.has("Progressive Weapon", world.player, 1))

                add_rule(challenge_2, lambda state: state.has("Challenge 2", world.player)
                                                    and state.has("Progressive Weapon", world.player, 1))

                add_rule(challenge_3, lambda state: (state.has_all(("Challenge 3", "Timed Mine"), world.player))
                                                    or (state.has("Challenge 3", world.player)
                                                        and state.has("Progressive Weapon", world.player, 1)))

                add_rule(challenge_4, lambda state: (state.has_all(("Challenge 4", "K7 Avenger"), world.player))
                                                    or (state.has("Challenge 4", world.player)
                                                        and state.has("Progressive Weapon", world.player, 2)))

                add_rule(challenge_5, lambda state: (state.has_all(("Challenge 5", "FarSight XR-20"), world.player))
                                                    or (state.has("Challenge 5", world.player)
                                                        and state.has("Progressive Weapon", world.player, 1)))

                add_rule(challenge_6, lambda state: (state.has_all(("Challenge 6", "Briefcase", "K7 Avenger"), world.player))
                                                    or (state.has_all(("Challenge 6", "Briefcase"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 1)))

                add_rule(challenge_7, lambda state: state.has("Challenge 7", world.player)
                                                    and state.has("Progressive Weapon", world.player, 2))

                add_rule(challenge_8, lambda state: state.has_all(("Challenge 8", "Briefcase"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 2))

                add_rule(challenge_9, lambda state: (state.has_all(("Challenge 9", "FarSight XR-20"), world.player))
                                                    or (state.has("Challenge 9", world.player)
                                                        and state.has("Progressive Weapon", world.player, 2)))

                add_rule(challenge_10, lambda state: (state.has_all(("Challenge 10", "Data Uplink", "Remote Mine"), world.player))
                                                    or (state.has_all(("Challenge 10", "Data Uplink"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 2)))

                add_rule(challenge_11, lambda state: state.has("Challenge 11", world.player)
                                                    and state.has("Progressive Weapon", world.player, 2))

                add_rule(challenge_12, lambda state: state.has("Challenge 12", world.player)
                                                    and state.has("Progressive Weapon", world.player, 2))

                add_rule(challenge_13, lambda state: state.has("Challenge 13", world.player)
                                                    and state.has("Progressive Weapon", world.player, 2))

                add_rule(challenge_14, lambda state: (state.has_all(("Challenge 14", "Briefcase", "Cloaking Device", "FarSight XR-20"), world.player))
                                                    or (state.has_all(("Challenge 14", "Briefcase", "Cloaking Device"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 2)))

                add_rule(challenge_15, lambda state: state.has_all(("Challenge 15", "Briefcase"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 2))

                add_rule(challenge_16, lambda state: state.has("Challenge 16", world.player)
                                                    and state.has("Progressive Weapon", world.player, 12))

                add_rule(challenge_17, lambda state: state.has("Challenge 17", world.player)
                                                    and state.has("Progressive Weapon", world.player, 14))

                add_rule(challenge_18, lambda state: state.has_all(("Challenge 18", "Cloaking Device"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 14))

                add_rule(challenge_19, lambda state: (state.has_all(("Challenge 19", "FarSight XR-20"), world.player))
                                                    or (state.has("Challenge 19", world.player)
                                                        and state.has("Progressive Weapon", world.player, 14)))

                add_rule(challenge_20, lambda state: state.has("Challenge 20", world.player)
                                                    and state.has("Progressive Weapon", world.player, 10))

                add_rule(challenge_21, lambda state: state.has_all(("Challenge 21", "Data Uplink", "Cloaking Device"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 14))

                add_rule(challenge_22, lambda state: state.has_all(("Challenge 22", "Briefcase"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 14))

                add_rule(challenge_23, lambda state: state.has("Challenge 23", world.player)
                                                    and state.has("Progressive Weapon", world.player, 14))

                add_rule(challenge_24, lambda state: state.has_all(("Challenge 24", "Briefcase"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 14))

                add_rule(challenge_25, lambda state: (state.has_all(("Challenge 25", "Cloaking Device"), world.player)
                                                        and state.has("Progressive Weapon", world.player, 14)))

                add_rule(challenge_26, lambda state: state.has("Challenge 26", world.player)
                                                    and state.has("Progressive Weapon", world.player, 22))

                add_rule(challenge_27, lambda state: state.has_all(("Challenge 27", "Data Uplink"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 22))

                add_rule(challenge_28, lambda state: state.has_all(("Challenge 28", "Briefcase"), world.player)
                                                    and state.has("Progressive Weapon", world.player, 22))

                add_rule(challenge_29, lambda state: state.has("Challenge 29", world.player)
                                                    and state.has("Progressive Weapon", world.player, 22))

                add_rule(challenge_30, lambda state: state.has("Challenge 30", world.player)
                                                    and state.has("Progressive Weapon", world.player, 22))
        
        if world.options.weapon_training:
            falcon2_bronze = world.get_location("Firing Range: Falcon 2 - Bronze")
            add_rule(falcon2_bronze, lambda state: state.has("Progressive Weapon", world.player, 5))
            
            falcon2_silver = world.get_location("Firing Range: Falcon 2 - Silver")
            add_rule(falcon2_silver, lambda state: state.has("Progressive Weapon", world.player, 5))
            
            falcon2_gold = world.get_location("Firing Range: Falcon 2 - Gold")
            add_rule(falcon2_gold, lambda state: state.has("Progressive Weapon", world.player, 5))
            
            falcon2silencer_bronze = world.get_location("Firing Range: Falcon 2 (Silencer) - Bronze")
            add_rule(falcon2silencer_bronze, lambda state: state.has("Progressive Weapon", world.player, 6))
            
            falcon2silencer_silver = world.get_location("Firing Range: Falcon 2 (Silencer) - Silver")
            add_rule(falcon2silencer_silver, lambda state: state.has("Progressive Weapon", world.player, 6))
            
            falcon2silencer_gold = world.get_location("Firing Range: Falcon 2 (Silencer) - Gold")
            add_rule(falcon2silencer_gold, lambda state: state.has("Progressive Weapon", world.player, 6))
            
            falcon2scope_bronze = world.get_location("Firing Range: Falcon 2 (Scope) - Bronze")
            add_rule(falcon2scope_bronze, lambda state: state.has("Progressive Weapon", world.player, 7))
            
            falcon2scope_silver = world.get_location("Firing Range: Falcon 2 (Scope) - Silver")
            add_rule(falcon2scope_silver, lambda state: state.has("Progressive Weapon", world.player, 7))
            
            falcon2scope_gold = world.get_location("Firing Range: Falcon 2 (Scope) - Gold")
            add_rule(falcon2scope_gold, lambda state: state.has("Progressive Weapon", world.player, 7))
            
            magsec4_bronze = world.get_location("Firing Range: MagSec 4 - Bronze")
            add_rule(magsec4_bronze, lambda state: state.has("Progressive Weapon", world.player, 10))
            
            magsec4_silver = world.get_location("Firing Range: MagSec 4 - Silver")
            add_rule(magsec4_silver, lambda state: state.has("Progressive Weapon", world.player, 10))
            
            magsec4_gold = world.get_location("Firing Range: MagSec 4 - Gold")
            add_rule(magsec4_gold, lambda state: state.has("Progressive Weapon", world.player, 10))
            
            mauler_bronze = world.get_location("Firing Range: Mauler - Bronze")
            add_rule(mauler_bronze, lambda state: state.has("Progressive Weapon", world.player, 37))
            
            mauler_silver = world.get_location("Firing Range: Mauler - Silver")
            add_rule(mauler_silver, lambda state: state.has("Progressive Weapon", world.player, 37))
            
            mauler_gold = world.get_location("Firing Range: Mauler - Gold")
            add_rule(mauler_gold, lambda state: state.has("Progressive Weapon", world.player, 37))
            
            phoenix_bronze = world.get_location("Firing Range: Phoenix - Bronze")
            add_rule(phoenix_bronze, lambda state: state.has("Progressive Weapon", world.player, 38))
            
            phoenix_silver = world.get_location("Firing Range: Phoenix - Silver")
            add_rule(phoenix_silver, lambda state: state.has("Progressive Weapon", world.player, 38))
            
            phoenix_gold = world.get_location("Firing Range: Phoenix - Gold")
            add_rule(phoenix_gold, lambda state: state.has("Progressive Weapon", world.player, 38))
            
            dy357magnum_bronze = world.get_location("Firing Range: DY357 Magnum - Bronze")
            add_rule(dy357magnum_bronze, lambda state: state.has("Progressive Weapon", world.player, 12))
            
            dy357magnum_silver = world.get_location("Firing Range: DY357 Magnum - Silver")
            add_rule(dy357magnum_silver, lambda state: state.has("Progressive Weapon", world.player, 12))
            
            dy357magnum_gold = world.get_location("Firing Range: DY357 Magnum - Gold")
            add_rule(dy357magnum_gold, lambda state: state.has("Progressive Weapon", world.player, 12))
            
            dy357lx_bronze = world.get_location("Firing Range: DY357-LX - Bronze")
            add_rule(dy357lx_bronze, lambda state: state.has("Progressive Weapon", world.player, 41))
            
            dy357lx_silver = world.get_location("Firing Range: DY357-LX - Silver")
            add_rule(dy357lx_silver, lambda state: state.has("Progressive Weapon", world.player, 41))
            
            dy357lx_gold = world.get_location("Firing Range: DY357-LX - Gold")
            add_rule(dy357lx_gold, lambda state: state.has("Progressive Weapon", world.player, 41))
            
            cmp150_bronze = world.get_location("Firing Range: CMP150 - Bronze")
            add_rule(cmp150_bronze, lambda state: state.has("Progressive Weapon", world.player, 17))
            
            cmp150_silver = world.get_location("Firing Range: CMP150 - Silver")
            add_rule(cmp150_silver, lambda state: state.has("Progressive Weapon", world.player, 17))
            
            cmp150_gold = world.get_location("Firing Range: CMP150 - Gold")
            add_rule(cmp150_gold, lambda state: state.has("Progressive Weapon", world.player, 17))
            
            cyclone_bronze = world.get_location("Firing Range: Cyclone - Bronze")
            add_rule(cyclone_bronze, lambda state: state.has("Progressive Weapon", world.player, 19))
            
            cyclone_silver = world.get_location("Firing Range: Cyclone - Silver")
            add_rule(cyclone_silver, lambda state: state.has("Progressive Weapon", world.player, 19))
            
            cyclone_gold = world.get_location("Firing Range: Cyclone - Gold")
            add_rule(cyclone_gold, lambda state: state.has("Progressive Weapon", world.player, 19))
            
            callisto_bronze = world.get_location("Firing Range: Callisto NTG - Bronze")
            add_rule(callisto_bronze, lambda state: state.has("Progressive Weapon", world.player, 30))
            
            callisto_silver = world.get_location("Firing Range: Callisto NTG - Silver")
            add_rule(callisto_silver, lambda state: state.has("Progressive Weapon", world.player, 30))
            
            callisto_gold = world.get_location("Firing Range: Callisto NTG - Gold")
            add_rule(callisto_gold, lambda state: state.has("Progressive Weapon", world.player, 30))
            
            rcp120_bronze = world.get_location("Firing Range: RC-P120 - Bronze")
            add_rule(rcp120_bronze, lambda state: state.has("Progressive Weapon", world.player, 40))
            
            rcp120_silver = world.get_location("Firing Range: RC-P120 - Silver")
            add_rule(rcp120_silver, lambda state: state.has("Progressive Weapon", world.player, 40))
            
            rcp120_gold = world.get_location("Firing Range: RC-P120 - Gold")
            add_rule(rcp120_gold, lambda state: state.has("Progressive Weapon", world.player, 40))
            
            laptopgun_bronze = world.get_location("Firing Range: Laptop Gun - Bronze")
            add_rule(laptopgun_bronze, lambda state: state.has("Progressive Weapon", world.player, 22))
            
            laptopgun_silver = world.get_location("Firing Range: Laptop Gun - Silver")
            add_rule(laptopgun_silver, lambda state: state.has("Progressive Weapon", world.player, 22))
            
            laptopgun_gold = world.get_location("Firing Range: Laptop Gun - Gold")
            add_rule(laptopgun_gold, lambda state: state.has("Progressive Weapon", world.player, 22))
            
            dragon_bronze = world.get_location("Firing Range: Dragon - Bronze")
            add_rule(dragon_bronze, lambda state: state.has("Progressive Weapon", world.player, 18))
            
            dragon_silver = world.get_location("Firing Range: Dragon - Silver")
            add_rule(dragon_silver, lambda state: state.has("Progressive Weapon", world.player, 18))
            
            dragon_gold = world.get_location("Firing Range: Dragon - Gold")
            add_rule(dragon_gold, lambda state: state.has("Progressive Weapon", world.player, 18))
            
            k7avenger_bronze = world.get_location("Firing Range: K7 Avenger - Bronze")
            add_rule(k7avenger_bronze, lambda state: state.has("Progressive Weapon", world.player, 29))
            
            k7avenger_silver = world.get_location("Firing Range: K7 Avenger - Silver")
            add_rule(k7avenger_silver, lambda state: state.has("Progressive Weapon", world.player, 29))
            
            k7avenger_gold = world.get_location("Firing Range: K7 Avenger - Gold")
            add_rule(k7avenger_gold, lambda state: state.has("Progressive Weapon", world.player, 29))
            
            ar34_bronze = world.get_location("Firing Range: AR34 - Bronze")
            add_rule(ar34_bronze, lambda state: state.has("Progressive Weapon", world.player, 21))
            
            ar34_silver = world.get_location("Firing Range: AR34 - Silver")
            add_rule(ar34_silver, lambda state: state.has("Progressive Weapon", world.player, 21))
            
            ar34_gold = world.get_location("Firing Range: AR34 - Gold")
            add_rule(ar34_gold, lambda state: state.has("Progressive Weapon", world.player, 21))
            
            superdragon_bronze = world.get_location("Firing Range: SuperDragon - Bronze")
            add_rule(superdragon_bronze, lambda state: state.has("Progressive Weapon", world.player, 32))
            
            superdragon_silver = world.get_location("Firing Range: SuperDragon - Silver")
            add_rule(superdragon_silver, lambda state: state.has("Progressive Weapon", world.player, 32))
            
            superdragon_gold = world.get_location("Firing Range: SuperDragon - Gold")
            add_rule(superdragon_gold, lambda state: state.has("Progressive Weapon", world.player, 32))
            
            shotgun_bronze = world.get_location("Firing Range: Shotgun - Bronze")
            add_rule(shotgun_bronze, lambda state: state.has("Progressive Weapon", world.player, 13))
            
            shotgun_silver = world.get_location("Firing Range: Shotgun - Silver")
            add_rule(shotgun_silver, lambda state: state.has("Progressive Weapon", world.player, 13))
            
            shotgun_gold = world.get_location("Firing Range: Shotgun - Gold")
            add_rule(shotgun_gold, lambda state: state.has("Progressive Weapon", world.player, 13))
            
            reaper_bronze = world.get_location("Firing Range: Reaper - Bronze")
            add_rule(reaper_bronze, lambda state: state.has("Progressive Weapon", world.player, 20))
            
            reaper_silver = world.get_location("Firing Range: Reaper - Silver")
            add_rule(reaper_silver, lambda state: state.has("Progressive Weapon", world.player, 20))
            
            reaper_gold = world.get_location("Firing Range: Reaper - Gold")
            add_rule(reaper_gold, lambda state: state.has("Progressive Weapon", world.player, 20))
            
            sniperrifle_bronze = world.get_location("Firing Range: Sniper Rifle - Bronze")
            add_rule(sniperrifle_bronze, lambda state: state.has("Progressive Weapon", world.player, 11))
            
            sniperrifle_silver = world.get_location("Firing Range: Sniper Rifle - Silver")
            add_rule(sniperrifle_silver, lambda state: state.has("Progressive Weapon", world.player, 11))
            
            sniperrifle_gold = world.get_location("Firing Range: Sniper Rifle - Gold")
            add_rule(sniperrifle_gold, lambda state: state.has("Progressive Weapon", world.player, 11))
            
            farsight_bronze = world.get_location("Firing Range: FarSight XR-20 - Bronze")
            add_rule(farsight_bronze, lambda state: state.has("Progressive Weapon", world.player, 42))
            
            farsight_silver = world.get_location("Firing Range: FarSight XR-20 - Silver")
            add_rule(farsight_silver, lambda state: state.has("Progressive Weapon", world.player, 42))
            
            farsight_gold = world.get_location("Firing Range: FarSight XR-20 - Gold")
            add_rule(farsight_gold, lambda state: state.has("Progressive Weapon", world.player, 42))
            
            devastator_bronze = world.get_location("Firing Range: Devastator - Bronze")
            add_rule(devastator_bronze, lambda state: state.has("Progressive Weapon", world.player, 35))
            
            devastator_silver = world.get_location("Firing Range: Devastator - Silver")
            add_rule(devastator_silver, lambda state: state.has("Progressive Weapon", world.player, 35))
            
            devastator_gold = world.get_location("Firing Range: Devastator - Gold")
            add_rule(devastator_gold, lambda state: state.has("Progressive Weapon", world.player, 35))
            
            rocketlauncher_bronze = world.get_location("Firing Range: Rocket Launcher - Bronze")
            add_rule(rocketlauncher_bronze, lambda state: state.has("Progressive Weapon", world.player, 34))
            
            rocketlauncher_silver = world.get_location("Firing Range: Rocket Launcher - Silver")
            add_rule(rocketlauncher_silver, lambda state: state.has("Progressive Weapon", world.player, 34))
            
            rocketlauncher_gold = world.get_location("Firing Range: Rocket Launcher - Gold")
            add_rule(rocketlauncher_gold, lambda state: state.has("Progressive Weapon", world.player, 34))
            
            slayer_bronze = world.get_location("Firing Range: Slayer - Bronze")
            add_rule(slayer_bronze, lambda state: state.has("Progressive Weapon", world.player, 33))
            
            slayer_silver = world.get_location("Firing Range: Slayer - Silver")
            add_rule(slayer_silver, lambda state: state.has("Progressive Weapon", world.player, 33))
            
            slayer_gold = world.get_location("Firing Range: Slayer - Gold")
            add_rule(slayer_gold, lambda state: state.has("Progressive Weapon", world.player, 33))
            
            knife_bronze = world.get_location("Firing Range: Combat Knife - Bronze")
            add_rule(knife_bronze, lambda state: state.has("Progressive Weapon", world.player, 1))
            
            knife_silver = world.get_location("Firing Range: Combat Knife - Silver")
            add_rule(knife_silver, lambda state: state.has("Progressive Weapon", world.player, 1))
            
            knife_gold = world.get_location("Firing Range: Combat Knife - Gold")
            add_rule(knife_gold, lambda state: state.has("Progressive Weapon", world.player, 1))
            
            crossbow_bronze = world.get_location("Firing Range: Crossbow - Bronze")
            add_rule(crossbow_bronze, lambda state: state.has("Progressive Weapon", world.player, 36))
            
            crossbow_silver = world.get_location("Firing Range: Crossbow - Silver")
            add_rule(crossbow_silver, lambda state: state.has("Progressive Weapon", world.player, 36))
            
            crossbow_gold = world.get_location("Firing Range: Crossbow - Gold")
            add_rule(crossbow_gold, lambda state: state.has("Progressive Weapon", world.player, 36))
            
            tranquilizer_bronze = world.get_location("Firing Range: Tranquilizer - Bronze")
            add_rule(tranquilizer_bronze, lambda state: state.has("Progressive Weapon", world.player, 2))
            
            tranquilizer_silver = world.get_location("Firing Range: Tranquilizer - Silver")
            add_rule(tranquilizer_silver, lambda state: state.has("Progressive Weapon", world.player, 2))
            
            tranquilizer_gold = world.get_location("Firing Range: Tranquilizer - Gold")
            add_rule(tranquilizer_gold, lambda state: state.has("Progressive Weapon", world.player, 2))
            
            laser_bronze = world.get_location("Firing Range: Laser - Bronze")
            add_rule(laser_bronze, lambda state: state.has("Progressive Weapon", world.player, 4))
            
            laser_silver = world.get_location("Firing Range: Laser - Silver")
            add_rule(laser_silver, lambda state: state.has("Progressive Weapon", world.player, 4))
            
            laser_gold = world.get_location("Firing Range: Laser - Gold")
            add_rule(laser_gold, lambda state: state.has("Progressive Weapon", world.player, 4))
            
            grenade_bronze = world.get_location("Firing Range: Grenade - Bronze")
            add_rule(grenade_bronze, lambda state: state.has("Progressive Weapon", world.player, 25))
            
            grenade_silver = world.get_location("Firing Range: Grenade - Silver")
            add_rule(grenade_silver, lambda state: state.has("Progressive Weapon", world.player, 25))
            
            grenade_gold = world.get_location("Firing Range: Grenade - Gold")
            add_rule(grenade_gold, lambda state: state.has("Progressive Weapon", world.player, 25))
            
            timedmine_bronze = world.get_location("Firing Range: Timed Mine - Bronze")
            add_rule(timedmine_bronze, lambda state: state.has("Progressive Weapon", world.player, 24))
            
            timedmine_silver = world.get_location("Firing Range: Timed Mine - Silver")
            add_rule(timedmine_silver, lambda state: state.has("Progressive Weapon", world.player, 24))
            
            timedmine_gold = world.get_location("Firing Range: Timed Mine - Gold")
            add_rule(timedmine_gold, lambda state: state.has("Progressive Weapon", world.player, 24))
            
            proximitymine_bronze = world.get_location("Firing Range: Proximity Mine - Bronze")
            add_rule(proximitymine_bronze, lambda state: state.has("Progressive Weapon", world.player, 26))
            
            proximitymine_silver = world.get_location("Firing Range: Proximity Mine - Silver")
            add_rule(proximitymine_silver, lambda state: state.has("Progressive Weapon", world.player, 26))
            
            proximitymine_gold = world.get_location("Firing Range: Proximity Mine - Gold")
            add_rule(proximitymine_gold, lambda state: state.has("Progressive Weapon", world.player, 26))
            
            remotemine_bronze = world.get_location("Firing Range: Remote Mine - Bronze")
            add_rule(remotemine_bronze, lambda state: state.has("Progressive Weapon", world.player, 27))
            
            remotemine_silver = world.get_location("Firing Range: Remote Mine - Silver")
            add_rule(remotemine_silver, lambda state: state.has("Progressive Weapon", world.player, 27))
            
            remotemine_gold = world.get_location("Firing Range: Remote Mine - Gold")
            add_rule(remotemine_gold, lambda state: state.has("Progressive Weapon", world.player, 27))

        if world.options.holotraining:
            dt_data_uplink = world.get_location("Holotraining 7: Live Combat 2")
            add_rule(dt_data_uplink, lambda state: state.has("Progressive Weapon", world.player, 5))

    if world.options.device_training:
        dt_data_uplink = world.get_location("Device Training: Data Uplink")
        add_rule(dt_data_uplink, lambda state: state.has("Data Uplink", world.player))

        dt_ecm_mine = world.get_location("Device Training: ECM Mine")
        add_rule(dt_ecm_mine, lambda state: state.has_all(("Data Uplink", "ECM Mine"), world.player))

        dt_camspy = world.get_location("Device Training: CamSpy")
        add_rule(dt_camspy, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy"), world.player))

        dt_night_vision = world.get_location("Device Training: Night Vision")
        add_rule(dt_night_vision, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision"), world.player))

        dt_door_decoder = world.get_location("Device Training: Door Decoder")
        add_rule(dt_door_decoder, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision", "Door Decoder"), world.player))

        dt_rtracker = world.get_location("Device Training: R-Tracker")
        add_rule(dt_rtracker, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision", "Door Decoder", "R-Tracker", "IR Scanner"), world.player))

        dt_ir_scanner = world.get_location("Device Training: IR Scanner")
        add_rule(dt_ir_scanner, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision", "Door Decoder", "R-Tracker", "IR Scanner"), world.player))

        dt_xray_scanner = world.get_location("Device Training: X-Ray Scanner")
        add_rule(dt_xray_scanner, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision", "Door Decoder", "R-Tracker", "IR Scanner", "X-Ray Scanner"), world.player))

        dt_disguise = world.get_location("Device Training: Disguise")
        add_rule(dt_disguise, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision", "Door Decoder", "R-Tracker", "IR Scanner", "X-Ray Scanner", "Stewardess Disguise"), world.player))

        dt_cloaking_device = world.get_location("Device Training: Cloaking Device")
        add_rule(dt_cloaking_device, lambda state: state.has_all(("Data Uplink", "ECM Mine", "CamSpy", "Night Vision", "Door Decoder", "R-Tracker", "IR Scanner", "X-Ray Scanner", "Stewardess Disguise", "Cloaking Device"), world.player))


def set_completion_condition(world: PerfectDarkWorld) -> None:
    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        if world.options.weapon_progression.value == world.options.weapon_progression.option_vanilla:
            # world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
            world.multiworld.completion_condition[world.player] = lambda state: state.has_all(("Skedar Ruins - Perfect Agent", "Falcon 2 (Scope)", "Callisto NTG", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
        elif world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon:
            world.multiworld.completion_condition[world.player] = lambda state: ((state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
                                                                                    and state.has("Progressive Weapon", world.player, 4))
                                                                                or (state.has_all(("Skedar Ruins - Perfect Agent", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
                                                                                    and state.has("Progressive Weapon", world.player, 24)))
        elif world.options.weapon_progression.value == world.options.weapon_progression.option_progressive_weapon_one_gun:
            world.multiworld.completion_condition[world.player] = lambda state: (state.has_all(("Skedar Ruins - Perfect Agent", "Devastator", "R-Tracker", "Target Amplifier", "IR Scanner"), world.player)
                                                                                and state.has("Progressive Weapon", world.player, 3))
    elif world.options.goal.value == Goal.option_collect_mission_stars:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Mission Star", world.player, world.options.required_mission_stars.value)
