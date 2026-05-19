from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import PerfectDarkWorld


def create_and_connect_regions(world: PerfectDarkWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: PerfectDarkWorld) -> None:
    carrington_institute = Region("Carrington Institute", world.player, world.multiworld)
    defection = Region("Defection", world.player, world.multiworld)
    investigation = Region("Investigation", world.player, world.multiworld)
    extraction = Region("Extraction", world.player, world.multiworld)
    villa = Region("Carrington Villa", world.player, world.multiworld)
    chicago = Region("Chicago", world.player, world.multiworld)
    g5_building = Region("G5 Building", world.player, world.multiworld)
    infiltration = Region("Infiltration", world.player, world.multiworld)
    rescue = Region("Rescue", world.player, world.multiworld)
    escape = Region("Escape", world.player, world.multiworld)
    air_base = Region("Air Base", world.player, world.multiworld)
    air_force_one = Region("Air Force One", world.player, world.multiworld)
    crash_site = Region("Crash Site", world.player, world.multiworld)
    pelagic = Region("Pelagic II", world.player, world.multiworld)
    deep_sea = Region("Deep Sea", world.player, world.multiworld)
    institute_defense = Region("Carrington Institute Defense", world.player, world.multiworld)
    attack_ship = Region("Attack Ship", world.player, world.multiworld)
    skedar_ruins = Region("Skedar Ruins", world.player, world.multiworld)
    mbr = Region("Mr. Blonde's Revenge", world.player, world.multiworld)
    maian_sos = Region("Maian SOS", world.player, world.multiworld)
    war = Region("War!", world.player, world.multiworld)
    duel = Region("The Duel", world.player, world.multiworld)

    regions = [
        carrington_institute,
        defection,
        investigation,
        extraction,
        villa,
        chicago,
        g5_building,
        infiltration,
        rescue,
        escape,
        air_base,
        air_force_one,
        crash_site,
        pelagic,
        deep_sea,
        institute_defense,
        attack_ship,
        skedar_ruins,
        mbr,
        maian_sos,
        war,
        duel
    ]

    world.multiworld.regions += regions


def connect_regions(world: PerfectDarkWorld) -> None:
    carrington_institute = world.get_region("Carrington Institute")
    defection = world.get_region("Defection")
    investigation = world.get_region("Investigation")
    extraction = world.get_region("Extraction")
    villa = world.get_region("Carrington Villa")
    chicago = world.get_region("Chicago")
    g5_building = world.get_region("G5 Building")
    infiltration = world.get_region("Infiltration")
    rescue = world.get_region("Rescue")
    escape = world.get_region("Escape")
    air_base = world.get_region("Air Base")
    air_force_one = world.get_region("Air Force One")
    crash_site = world.get_region("Crash Site")
    pelagic = world.get_region("Pelagic II")
    deep_sea = world.get_region("Deep Sea")
    institute_defense = world.get_region("Carrington Institute Defense")
    attack_ship = world.get_region("Attack Ship")
    skedar_ruins = world.get_region("Skedar Ruins")
    mbr = world.get_region("Mr. Blonde's Revenge")
    maian_sos = world.get_region("Maian SOS")
    war = world.get_region("War!")
    duel = world.get_region("The Duel")

    carrington_institute.connect(defection, "Carrington Institute to Defection")
    carrington_institute.connect(investigation, "Carrington Institute to Investigation")
    carrington_institute.connect(extraction, "Carrington Institute to Extraction")
    carrington_institute.connect(villa, "Carrington Institute to Carrington Villa")
    carrington_institute.connect(chicago, "Carrington Institute to Chicago")
    carrington_institute.connect(g5_building, "Carrington Institute to G5 Building")
    carrington_institute.connect(infiltration, "Carrington Institute to Infiltration")
    carrington_institute.connect(rescue, "Carrington Institute to Rescue")
    carrington_institute.connect(escape, "Carrington Institute to Escape")
    carrington_institute.connect(air_base, "Carrington Institute to Air Base")
    carrington_institute.connect(air_force_one, "Carrington Institute to Air Force One")
    carrington_institute.connect(crash_site, "Carrington Institute to Crash Site")
    carrington_institute.connect(pelagic, "Carrington Institute to Pelagic II")
    carrington_institute.connect(deep_sea, "Carrington Institute to Deep Sea")
    carrington_institute.connect(institute_defense, "Carrington Institute to Defense")
    carrington_institute.connect(attack_ship, "Carrington Institute to Attack Ship")
    carrington_institute.connect(skedar_ruins, "Carrington Institute to Skedar Ruins")
    carrington_institute.connect(mbr, "Carrington Institute to Mr. Blonde's Revenge")
    carrington_institute.connect(maian_sos, "Carrington Institute to Maian SOS")
    carrington_institute.connect(war, "Carrington Institute to War!")
    carrington_institute.connect(duel, "Carrington Institute to The Duel")
