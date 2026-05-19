from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal

ITEM_NAME_TO_ID = {
    "NONE": 1,
    "UNARMED": 2,
    "Falcon 2": 3,
    "Falcon 2 (Silencer)": 4,
    "Falcon 2 (Scope)": 5,
    "MagSec 4": 6,
    "Mauler": 7,
    "Phoenix": 8,
    "DY357 Magnum": 9,
    "DY357-LX": 10,
    "CMP150": 11,
    "Cyclone": 12,
    "Callisto NTG": 13,
    "RC-P120": 14,
    "Laptop Gun": 15,
    "Dragon": 16,
    "K7 Avenger": 17,
    "AR34": 18,
    "SuperDragon": 19,
    "Shotgun": 20,
    "Reaper": 21,
    "Sniper Rifle": 22,
    "FarSight XR-20": 23,
    "Devastator": 24,
    "Rocket Launcher": 25,
    "Slayer": 26,
    "Combat Knife": 27,
    "Crossbow": 28,
    "Tranquilizer": 29,
    "Laser": 30,
    "Grenade": 31,
    "N-Bomb": 32,
    "Timed Mine": 33,
    "Proximity Mine": 34,
    "Remote Mine": 35,
    "Combat Boost": 36,
	"PP9i": 37,
	"CC13": 38,
	"KL01313": 39,
	"KF7 Special": 40,
	"ZZT (9mm)": 41,
	"DMC": 42,
	"AR53": 43,
	"RC-P45": 44,
    "Psychosis Gun": 45,
	"Night Vision": 46,
	"CamSpy": 47,
	"X-Ray Scanner": 48,
	"IR Scanner": 49,
	"Cloaking Device": 50,
	"Horizon Scanner": 51,
    "TESTER": 52,
    "ROCKETLAUNCHER_34": 53,
	"ECM Mine": 54,
	"Data Uplink": 55,
	"R-Tracker": 56,
	"President Scanner": 57,
	"Door Decoder": 58,
	"Alien Medpack": 59,
	"Explosives": 60,
	"Skedar Bomb": 61,
	"Comms Rider": 62,
	"Tracer Bug": 63,
	"Target Amplifier": 64,
	"Lab Clothes": 65,
	"Stewardess Disguise": 66,
	"Flight Plans": 67,
	"Research Tape": 68,
	"Backup Disk": 69,
	"G5 Building Level 1 Key Card": 70,
	"G5 Building Level 2 Key Card": 71,
	"Medlab 2 Key Card": 72,
	"Op Room Key Card": 73,
	"Air Force One Key Cards": 74,
	"Cellar Key Card": 75,
	"Area 51 Lift Key Card": 76,
	"Cassandra's Office Key Card": 77,
	"Suitcase": 78,
	"WEAPON_BRIEFCASE": 79,
	"Shield Tech Item": 80,
	"De Vries' Necklace": 81,
    "HAMMER": 82,
    "SCREWDRIVER": 83,
    "ROCKET": 84,
    "HOMINGROCKET": 85,
    "GRENADEROUND": 86,
    "BOLT": 87,
    "Briefcase": 88,
	"SKROCKET": 89,
    "CHOPPERGUN": 90,
    "WATCHLASER": 91,
    "Shield": 92,
	"DISABLED": 93,
    "SUICIDEPILL": 94,
    "Defection - Agent": 95,
    "Investigation - Agent": 96,
    "Extraction - Agent": 97,
    "Carrington Villa - Agent": 98,
    "Chicago - Agent": 99,
    "G5 Building - Agent": 100,
    "Infiltration - Agent": 101,
    "Rescue - Agent": 102,
    "Escape - Agent": 103,
    "Air Base - Agent": 104,
    "Air Force One - Agent": 105,
    "Crash Site - Agent": 106,
    "Pelagic II - Agent": 107,
    "Deep Sea - Agent": 108,
    "Carrington Institute - Agent": 109,
    "Attack Ship - Agent": 110,
    "Skedar Ruins - Agent": 111,
    "Mr. Blonde's Revenge - Agent": 112,
    "Maian SOS - Agent": 113,
    "WAR! - Agent": 114,
    "The Duel - Agent": 115,
    "Defection - Special Agent": 116,
    "Investigation - Special Agent": 117,
    "Extraction - Special Agent": 118,
    "Carrington Villa - Special Agent": 119,
    "Chicago - Special Agent": 120,
    "G5 Building - Special Agent": 121,
    "Infiltration - Special Agent": 122,
    "Rescue - Special Agent": 123,
    "Escape - Special Agent": 124,
    "Air Base - Special Agent": 125,
    "Air Force One - Special Agent": 126,
    "Crash Site - Special Agent": 127,
    "Pelagic II - Special Agent": 128,
    "Deep Sea - Special Agent": 129,
    "Carrington Institute - Special Agent": 130,
    "Attack Ship - Special Agent": 131,
    "Skedar Ruins - Special Agent": 132,
    "Mr. Blonde's Revenge - Special Agent": 133,
    "Maian SOS - Special Agent": 134,
    "WAR! - Special Agent": 135,
    "The Duel - Special Agent": 136,
    "Defection - Perfect Agent": 137,
    "Investigation - Perfect Agent": 138,
    "Extraction - Perfect Agent": 139,
    "Carrington Villa - Perfect Agent": 140,
    "Chicago - Perfect Agent": 141,
    "G5 Building - Perfect Agent": 142,
    "Infiltration - Perfect Agent": 143,
    "Rescue - Perfect Agent": 144,
    "Escape - Perfect Agent": 145,
    "Air Base - Perfect Agent": 146,
    "Air Force One - Perfect Agent": 147,
    "Crash Site - Perfect Agent": 148,
    "Pelagic II - Perfect Agent": 149,
    "Deep Sea - Perfect Agent": 150,
    "Carrington Institute - Perfect Agent": 151,
    "Attack Ship - Perfect Agent": 152,
    "Skedar Ruins - Perfect Agent": 153,
    "Mr. Blonde's Revenge - Perfect Agent": 154,
    "Maian SOS - Perfect Agent": 155,
    "WAR! - Perfect Agent": 156,
    "The Duel - Perfect Agent": 157,
	"Challenge 1": 158,
	"Challenge 2": 159,
	"Challenge 3": 160,
	"Challenge 4": 161,
	"Challenge 5": 162,
	"Challenge 6": 163,
	"Challenge 7": 164,
	"Challenge 8": 165,
	"Challenge 9": 166,
	"Challenge 10": 167,
	"Challenge 11": 168,
	"Challenge 12": 169,
	"Challenge 13": 170,
	"Challenge 14": 171,
	"Challenge 15": 172,
	"Challenge 16": 173,
	"Challenge 17": 174,
	"Challenge 18": 175,
	"Challenge 19": 176,
	"Challenge 20": 177,
	"Challenge 21": 178,
	"Challenge 22": 179,
	"Challenge 23": 180,
	"Challenge 24": 181,
	"Challenge 25": 182,
	"Challenge 26": 183,
	"Challenge 27": 184,
	"Challenge 28": 185,
	"Challenge 29": 186,
	"Challenge 30": 187,
    "Progressive Weapon": 188,
    "Cheese": 189,
    "Trap": 190,
    "Mission Star": 191,
    "Victory": 192,
}

STARTING_MISSION_ID_TO_NAME = {
    1: "Defection - Perfect Agent",
    2: "Investigation - Perfect Agent",
    3: "Extraction - Perfect Agent",
    4: "Carrington Villa - Perfect Agent",
    5: "Chicago - Perfect Agent",
    6: "G5 Building - Perfect Agent",
    7: "Infiltration - Perfect Agent",
    8: "Rescue - Perfect Agent",
    9: "Escape - Perfect Agent",
    10: "Air Base - Perfect Agent",
    11: "Air Force One - Perfect Agent",
    12: "Crash Site - Perfect Agent",
    13: "Pelagic II - Perfect Agent",
    14: "Deep Sea - Perfect Agent",
    15: "Carrington Institute - Perfect Agent",
    16: "Attack Ship - Perfect Agent",
    17: "Mr. Blonde's Revenge - Perfect Agent",
    18: "Maian SOS - Perfect Agent",
    19: "WAR! - Perfect Agent",
    20: "The Duel - Perfect Agent",
    21: "Skedar Ruins - Perfect Agent",
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "NONE": ItemClassification.filler,
    "UNARMED": ItemClassification.progression,
    "Falcon 2": ItemClassification.progression,
    "Falcon 2 (Silencer)": ItemClassification.progression,
    "Falcon 2 (Scope)": ItemClassification.progression,
    "MagSec 4": ItemClassification.progression,
    "Mauler": ItemClassification.progression,
    "Phoenix": ItemClassification.progression,
    "DY357 Magnum": ItemClassification.progression,
    "DY357-LX": ItemClassification.progression,
    "CMP150": ItemClassification.progression,
    "Cyclone": ItemClassification.progression,
    "Callisto NTG": ItemClassification.progression,
    "RC-P120": ItemClassification.progression,
    "Laptop Gun": ItemClassification.progression,
    "Dragon": ItemClassification.progression,
    "K7 Avenger": ItemClassification.progression,
    "AR34": ItemClassification.progression,
    "SuperDragon": ItemClassification.progression,
    "Shotgun": ItemClassification.progression,
    "Reaper": ItemClassification.progression,
    "Sniper Rifle": ItemClassification.progression,
    "FarSight XR-20": ItemClassification.progression,
    "Devastator": ItemClassification.progression,
    "Rocket Launcher": ItemClassification.progression,
    "Slayer": ItemClassification.progression,
    "Combat Knife": ItemClassification.progression,
    "Crossbow": ItemClassification.progression,
    "Tranquilizer": ItemClassification.progression,
    "Laser": ItemClassification.progression,
    "Grenade": ItemClassification.progression,
    "N-Bomb": ItemClassification.progression,
    "Timed Mine": ItemClassification.progression,
    "Proximity Mine": ItemClassification.progression,
    "Remote Mine": ItemClassification.progression,
    "Combat Boost": ItemClassification.filler,
	"PP9i": ItemClassification.filler,
	"CC13": ItemClassification.filler,
	"KL01313": ItemClassification.filler,
	"KF7 Special": ItemClassification.filler,
	"ZZT (9mm)": ItemClassification.filler,
	"DMC": ItemClassification.filler,
	"AR53": ItemClassification.filler,
	"RC-P45": ItemClassification.filler,
    "Psychosis Gun": ItemClassification.filler,
	"Night Vision": ItemClassification.progression | ItemClassification.useful,
	"CamSpy": ItemClassification.progression | ItemClassification.useful,
	"X-Ray Scanner": ItemClassification.progression | ItemClassification.useful,
	"IR Scanner": ItemClassification.progression | ItemClassification.useful,
	"Cloaking Device": ItemClassification.progression | ItemClassification.useful,
	"Horizon Scanner": ItemClassification.filler,
    "TESTER": ItemClassification.filler,
    "ROCKETLAUNCHER_34": ItemClassification.filler,
	"ECM Mine": ItemClassification.progression | ItemClassification.useful,
	"Data Uplink": ItemClassification.progression | ItemClassification.useful,
	"R-Tracker": ItemClassification.progression | ItemClassification.useful,
	"President Scanner": ItemClassification.progression | ItemClassification.useful,
	"Door Decoder": ItemClassification.progression | ItemClassification.useful,
	"Alien Medpack": ItemClassification.progression | ItemClassification.useful,
	"Explosives": ItemClassification.progression | ItemClassification.useful,
	"Skedar Bomb": ItemClassification.progression | ItemClassification.useful,
	"Comms Rider": ItemClassification.progression | ItemClassification.useful,
	"Tracer Bug": ItemClassification.progression | ItemClassification.useful,
	"Target Amplifier": ItemClassification.progression | ItemClassification.useful,
	"Lab Clothes": ItemClassification.progression | ItemClassification.useful,
	"Stewardess Disguise": ItemClassification.progression | ItemClassification.useful,
	"Flight Plans": ItemClassification.progression | ItemClassification.useful,
	"Research Tape": ItemClassification.progression | ItemClassification.useful,
	"Backup Disk": ItemClassification.progression | ItemClassification.useful,
	"G5 Building Level 1 Key Card": ItemClassification.progression | ItemClassification.useful,
	"G5 Building Level 2 Key Card": ItemClassification.progression | ItemClassification.useful,
	"Medlab 2 Key Card": ItemClassification.progression | ItemClassification.useful,
	"Op Room Key Card": ItemClassification.progression | ItemClassification.useful,
	"Air Force One Key Cards": ItemClassification.progression | ItemClassification.useful,
	"Cellar Key Card": ItemClassification.progression | ItemClassification.useful,
	"Area 51 Lift Key Card": ItemClassification.progression | ItemClassification.useful,
	"Cassandra's Office Key Card": ItemClassification.filler,
	"Suitcase": ItemClassification.progression | ItemClassification.useful,
	"WEAPON_BRIEFCASE": ItemClassification.filler,
	"Shield Tech Item": ItemClassification.progression | ItemClassification.useful,
	"De Vries' Necklace": ItemClassification.progression | ItemClassification.useful,
    "HAMMER": ItemClassification.filler,
    "SCREWDRIVER": ItemClassification.filler,
    "ROCKET": ItemClassification.filler,
    "HOMINGROCKET": ItemClassification.filler,
    "GRENADEROUND": ItemClassification.filler,
    "BOLT": ItemClassification.filler,
    "Briefcase": ItemClassification.progression | ItemClassification.useful,
	"SKROCKET": ItemClassification.filler,
    "CHOPPERGUN": ItemClassification.filler,
    "WATCHLASER": ItemClassification.filler,
    "Shield": ItemClassification.progression | ItemClassification.useful,
	"DISABLED": ItemClassification.filler,
    "SUICIDEPILL": ItemClassification.filler,
    "Defection - Agent": ItemClassification.progression | ItemClassification.useful,
    "Defection - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Defection - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Investigation - Agent": ItemClassification.progression | ItemClassification.useful,
    "Investigation - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Investigation - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Extraction - Agent": ItemClassification.progression | ItemClassification.useful,
    "Extraction - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Extraction - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa - Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Chicago - Agent": ItemClassification.progression | ItemClassification.useful,
    "Chicago - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Chicago - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "G5 Building - Agent": ItemClassification.progression | ItemClassification.useful,
    "G5 Building - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "G5 Building - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Infiltration - Agent": ItemClassification.progression | ItemClassification.useful,
    "Infiltration - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Infiltration - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Rescue - Agent": ItemClassification.progression | ItemClassification.useful,
    "Rescue - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Rescue - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Escape - Agent": ItemClassification.progression | ItemClassification.useful,
    "Escape - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Escape - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Air Base - Agent": ItemClassification.progression | ItemClassification.useful,
    "Air Base - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Air Base - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Air Force One - Agent": ItemClassification.progression | ItemClassification.useful,
    "Air Force One - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Air Force One - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Crash Site - Agent": ItemClassification.progression | ItemClassification.useful,
    "Crash Site - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Crash Site - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Pelagic II - Agent": ItemClassification.progression | ItemClassification.useful,
    "Pelagic II - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Pelagic II - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Deep Sea - Agent": ItemClassification.progression | ItemClassification.useful,
    "Deep Sea - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Deep Sea - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Institute - Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Institute - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Institute - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Attack Ship - Agent": ItemClassification.progression | ItemClassification.useful,
    "Attack Ship - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Attack Ship - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Skedar Ruins - Agent": ItemClassification.progression | ItemClassification.useful,
    "Skedar Ruins - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Skedar Ruins - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Mr. Blonde's Revenge - Agent": ItemClassification.progression | ItemClassification.useful,
    "Mr. Blonde's Revenge - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Mr. Blonde's Revenge - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Maian SOS - Agent": ItemClassification.progression | ItemClassification.useful,
    "Maian SOS - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Maian SOS - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "WAR! - Agent": ItemClassification.progression | ItemClassification.useful,
    "WAR! - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "WAR! - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "The Duel - Agent": ItemClassification.progression | ItemClassification.useful,
    "The Duel - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "The Duel - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
	"Challenge 1": ItemClassification.progression | ItemClassification.useful,
	"Challenge 2": ItemClassification.progression | ItemClassification.useful,
	"Challenge 3": ItemClassification.progression | ItemClassification.useful,
	"Challenge 4": ItemClassification.progression | ItemClassification.useful,
	"Challenge 5": ItemClassification.progression | ItemClassification.useful,
	"Challenge 6": ItemClassification.progression | ItemClassification.useful,
	"Challenge 7": ItemClassification.progression | ItemClassification.useful,
	"Challenge 8": ItemClassification.progression | ItemClassification.useful,
	"Challenge 9": ItemClassification.progression | ItemClassification.useful,
	"Challenge 10": ItemClassification.progression | ItemClassification.useful,
	"Challenge 11": ItemClassification.progression | ItemClassification.useful,
	"Challenge 12": ItemClassification.progression | ItemClassification.useful,
	"Challenge 13": ItemClassification.progression | ItemClassification.useful,
	"Challenge 14": ItemClassification.progression | ItemClassification.useful,
	"Challenge 15": ItemClassification.progression | ItemClassification.useful,
	"Challenge 16": ItemClassification.progression | ItemClassification.useful,
	"Challenge 17": ItemClassification.progression | ItemClassification.useful,
	"Challenge 18": ItemClassification.progression | ItemClassification.useful,
	"Challenge 19": ItemClassification.progression | ItemClassification.useful,
	"Challenge 20": ItemClassification.progression | ItemClassification.useful,
	"Challenge 21": ItemClassification.progression | ItemClassification.useful,
	"Challenge 22": ItemClassification.progression | ItemClassification.useful,
	"Challenge 23": ItemClassification.progression | ItemClassification.useful,
	"Challenge 24": ItemClassification.progression | ItemClassification.useful,
	"Challenge 25": ItemClassification.progression | ItemClassification.useful,
	"Challenge 26": ItemClassification.progression | ItemClassification.useful,
	"Challenge 27": ItemClassification.progression | ItemClassification.useful,
	"Challenge 28": ItemClassification.progression | ItemClassification.useful,
	"Challenge 29": ItemClassification.progression | ItemClassification.useful,
	"Challenge 30": ItemClassification.progression | ItemClassification.useful,
    "Progressive Weapon": ItemClassification.progression,
    "Cheese": ItemClassification.filler,
    "Trap": ItemClassification.trap,
    "Mission Star": ItemClassification.progression | ItemClassification.useful,
    "Victory": ItemClassification.progression | ItemClassification.useful,
}


class PerfectDarkItem(Item):
    game = "Perfect Dark"


def get_random_filler_item_name(world: PerfectDarkWorld) -> str:
    # if world.random.randint(0, 99) < world.options.trap_chance:
    #     return "Trap"
    return "Cheese"


def create_item_with_correct_classification(world: PerfectDarkWorld, name: str) -> PerfectDarkItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return PerfectDarkItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world:PerfectDarkWorld) -> None:
    # Create items
    itempool: list[Item] = [
        world.create_item("Combat Boost"),
        world.create_item("Night Vision"),
        world.create_item("CamSpy"),
        world.create_item("X-Ray Scanner"),
        world.create_item("IR Scanner"),
        world.create_item("Cloaking Device"),
        world.create_item("Horizon Scanner"),
        world.create_item("ECM Mine"),
        world.create_item("Data Uplink"),
        world.create_item("R-Tracker"),
        world.create_item("President Scanner"),
        world.create_item("Door Decoder"),
        world.create_item("Alien Medpack"),
        world.create_item("Explosives"),
        world.create_item("Skedar Bomb"),
        world.create_item("Comms Rider"),
        world.create_item("Tracer Bug"),
        world.create_item("Target Amplifier"),
        world.create_item("Lab Clothes"),
        world.create_item("Stewardess Disguise"),
        world.create_item("Flight Plans"),
        world.create_item("Research Tape"),
        world.create_item("Backup Disk"),
        world.create_item("G5 Building Level 1 Key Card"),
        world.create_item("G5 Building Level 2 Key Card"),
        world.create_item("Medlab 2 Key Card"), 
        world.create_item("Op Room Key Card"), 
        world.create_item("Air Force One Key Cards"),
        world.create_item("Cellar Key Card"),
        world.create_item("Area 51 Lift Key Card"),
        world.create_item("Suitcase"),
        world.create_item("Shield Tech Item"),
        world.create_item("De Vries' Necklace"),
        world.create_item("Shield"),
        world.create_item("Defection - Perfect Agent"),
        world.create_item("Investigation - Perfect Agent"),
        world.create_item("Extraction - Perfect Agent"),
        world.create_item("Carrington Villa - Perfect Agent"),
        world.create_item("Chicago - Perfect Agent"),
        world.create_item("G5 Building - Perfect Agent"),
        world.create_item("Infiltration - Perfect Agent"),
        world.create_item("Rescue - Perfect Agent"),
        world.create_item("Escape - Perfect Agent"),
        world.create_item("Air Base - Perfect Agent"),
        world.create_item("Air Force One - Perfect Agent"),
        world.create_item("Crash Site - Perfect Agent"),
        world.create_item("Pelagic II - Perfect Agent"),
        world.create_item("Deep Sea - Perfect Agent"),
        world.create_item("Carrington Institute - Perfect Agent"),
        world.create_item("Attack Ship - Perfect Agent"),
        world.create_item("Skedar Ruins - Perfect Agent"),
        world.create_item("Mr. Blonde's Revenge - Perfect Agent"),
        world.create_item("Maian SOS - Perfect Agent"),
        world.create_item("WAR! - Perfect Agent"),
        world.create_item("The Duel - Perfect Agent"),
    ]

    if world.options.weapon_progression.value == world.options.weapon_progression.option_vanilla:
        itempool.append(world.create_item("Falcon 2"))
        itempool.append(world.create_item("Falcon 2 (Silencer)"))
        itempool.append(world.create_item("Falcon 2 (Scope)"))
        itempool.append(world.create_item("MagSec 4"))
        itempool.append(world.create_item("Mauler"))
        itempool.append(world.create_item("Phoenix"))
        itempool.append(world.create_item("DY357 Magnum"))
        itempool.append(world.create_item("DY357-LX"))
        itempool.append(world.create_item("CMP150"))
        itempool.append(world.create_item("Cyclone"))
        itempool.append(world.create_item("Callisto NTG"))
        itempool.append(world.create_item("RC-P120"))
        itempool.append(world.create_item("Laptop Gun"))
        itempool.append(world.create_item("Dragon"))
        itempool.append(world.create_item("K7 Avenger"))
        itempool.append(world.create_item("AR34"))
        itempool.append(world.create_item("SuperDragon"))
        itempool.append(world.create_item("Shotgun"))
        itempool.append(world.create_item("Reaper"))
        itempool.append(world.create_item("Sniper Rifle"))
        itempool.append(world.create_item("FarSight XR-20"))
        itempool.append(world.create_item("Devastator"))
        itempool.append(world.create_item("Rocket Launcher"))
        itempool.append(world.create_item("Slayer"))
        itempool.append(world.create_item("Combat Knife"))
        itempool.append(world.create_item("Crossbow"))
        itempool.append(world.create_item("Tranquilizer"))
        itempool.append(world.create_item("Laser"))
        itempool.append(world.create_item("Grenade"))
        itempool.append(world.create_item("N-Bomb"))
        itempool.append(world.create_item("Timed Mine"))
        itempool.append(world.create_item("Proximity Mine"))
        itempool.append(world.create_item("Remote Mine"))
        itempool.append(world.create_item("PP9i"))
        itempool.append(world.create_item("CC13"))
        itempool.append(world.create_item("KL01313"))
        itempool.append(world.create_item("KF7 Special"))
        itempool.append(world.create_item("ZZT (9mm)"))
        itempool.append(world.create_item("DMC"))
        itempool.append(world.create_item("AR53"))
        itempool.append(world.create_item("RC-P45"))
        itempool.append(world.create_item("Psychosis Gun"))
    elif world.options.weapon_progression.value > world.options.weapon_progression.option_vanilla:
        itempool.append(world.create_item("RC-P120"))
        itempool.append(world.create_item("K7 Avenger"))
        itempool.append(world.create_item("FarSight XR-20"))
        itempool.append(world.create_item("Devastator"))
        itempool.append(world.create_item("Timed Mine"))
        itempool.append(world.create_item("Remote Mine"))
        for x in range(42):
            itempool.append(world.create_item("Progressive Weapon"))

    if world.options.challenges:
        itempool.append(world.create_item("Briefcase"))
        itempool.append(world.create_item("Challenge 1"))
        itempool.append(world.create_item("Challenge 2"))
        itempool.append(world.create_item("Challenge 3"))
        itempool.append(world.create_item("Challenge 4"))
        itempool.append(world.create_item("Challenge 5"))
        itempool.append(world.create_item("Challenge 6"))
        itempool.append(world.create_item("Challenge 7"))
        itempool.append(world.create_item("Challenge 8"))
        itempool.append(world.create_item("Challenge 9"))
        itempool.append(world.create_item("Challenge 10"))
        itempool.append(world.create_item("Challenge 11"))
        itempool.append(world.create_item("Challenge 12"))
        itempool.append(world.create_item("Challenge 13"))
        itempool.append(world.create_item("Challenge 14"))
        itempool.append(world.create_item("Challenge 15"))
        itempool.append(world.create_item("Challenge 16"))
        itempool.append(world.create_item("Challenge 17"))
        itempool.append(world.create_item("Challenge 18"))
        itempool.append(world.create_item("Challenge 19"))
        itempool.append(world.create_item("Challenge 20"))
        itempool.append(world.create_item("Challenge 21"))
        itempool.append(world.create_item("Challenge 22"))
        itempool.append(world.create_item("Challenge 23"))
        itempool.append(world.create_item("Challenge 24"))
        itempool.append(world.create_item("Challenge 25"))
        itempool.append(world.create_item("Challenge 26"))
        itempool.append(world.create_item("Challenge 27"))
        itempool.append(world.create_item("Challenge 28"))
        itempool.append(world.create_item("Challenge 29"))
        itempool.append(world.create_item("Challenge 30"))
    
        if world.options.start_with_all_challenges:
            remove_starting_item_from_pool(world, "Challenge 1", itempool)
            remove_starting_item_from_pool(world, "Challenge 2", itempool)
            remove_starting_item_from_pool(world, "Challenge 3", itempool)
            remove_starting_item_from_pool(world, "Challenge 4", itempool)
            remove_starting_item_from_pool(world, "Challenge 5", itempool)
            remove_starting_item_from_pool(world, "Challenge 6", itempool)
            remove_starting_item_from_pool(world, "Challenge 7", itempool)
            remove_starting_item_from_pool(world, "Challenge 8", itempool)
            remove_starting_item_from_pool(world, "Challenge 9", itempool)
            remove_starting_item_from_pool(world, "Challenge 10", itempool)
            remove_starting_item_from_pool(world, "Challenge 11", itempool)
            remove_starting_item_from_pool(world, "Challenge 12", itempool)
            remove_starting_item_from_pool(world, "Challenge 13", itempool)
            remove_starting_item_from_pool(world, "Challenge 14", itempool)
            remove_starting_item_from_pool(world, "Challenge 15", itempool)
            remove_starting_item_from_pool(world, "Challenge 16", itempool)
            remove_starting_item_from_pool(world, "Challenge 17", itempool)
            remove_starting_item_from_pool(world, "Challenge 18", itempool)
            remove_starting_item_from_pool(world, "Challenge 19", itempool)
            remove_starting_item_from_pool(world, "Challenge 20", itempool)
            remove_starting_item_from_pool(world, "Challenge 21", itempool)
            remove_starting_item_from_pool(world, "Challenge 22", itempool)
            remove_starting_item_from_pool(world, "Challenge 23", itempool)
            remove_starting_item_from_pool(world, "Challenge 24", itempool)
            remove_starting_item_from_pool(world, "Challenge 25", itempool)
            remove_starting_item_from_pool(world, "Challenge 26", itempool)
            remove_starting_item_from_pool(world, "Challenge 27", itempool)
            remove_starting_item_from_pool(world, "Challenge 28", itempool)
            remove_starting_item_from_pool(world, "Challenge 29", itempool)
            remove_starting_item_from_pool(world, "Challenge 30", itempool)

    if world.options.goal == Goal.option_complete_skedar_ruins:
        world.get_location("Complete: Skedar Ruins - Perfect Agent").place_locked_item(world.create_item("Victory"))
    elif world.options.goal == Goal.option_collect_mission_stars:
        mission_locations = [
            # "Complete: Defection - Agent",
            # "Complete: Defection - Special Agent",
            "Complete: Defection - Perfect Agent",
            # "Complete: Investigation - Agent",
            # "Complete: Investigation - Special Agent",
            "Complete: Investigation - Perfect Agent",
            # "Complete: Extraction - Agent",
            # "Complete: Extraction - Special Agent",
            "Complete: Extraction - Perfect Agent",
            # "Complete: Carrington Villa - Agent",
            # "Complete: Carrington Villa - Special Agent",
            "Complete: Carrington Villa - Perfect Agent",
            # "Complete: Chicago - Agent",
            # "Complete: Chicago - Special Agent",
            "Complete: Chicago - Perfect Agent",
            # "Complete: G5 Building - Agent",
            # "Complete: G5 Building - Special Agent",
            "Complete: G5 Building - Perfect Agent",
            # "Complete: Infiltration - Agent",
            # "Complete: Infiltration - Special Agent",
            "Complete: Infiltration - Perfect Agent",
            # "Complete: Rescue - Agent",
            # "Complete: Rescue - Special Agent",
            "Complete: Rescue - Perfect Agent",
            # "Complete: Escape - Agent",
            # "Complete: Escape - Special Agent",
            "Complete: Escape - Perfect Agent",
            # "Complete: Air Base - Agent",
            # "Complete: Air Base - Special Agent",
            "Complete: Air Base - Perfect Agent",
            # "Complete: Air Force One - Agent",
            # "Complete: Air Force One - Special Agent",
            "Complete: Air Force One - Perfect Agent",
            # "Complete: Crash Site - Agent",
            # "Complete: Crash Site - Special Agent",
            "Complete: Crash Site - Perfect Agent",
            # "Complete: Pelagic II - Agent",
            # "Complete: Pelagic II - Special Agent",
            "Complete: Pelagic II - Perfect Agent",
            # "Complete: Deep Sea - Agent",
            # "Complete: Deep Sea - Special Agent",
            "Complete: Deep Sea - Perfect Agent",
            # "Complete: Carrington Institute - Agent",
            # "Complete: Carrington Institute - Special Agent",
            "Complete: Carrington Institute - Perfect Agent",
            # "Complete: Attack Ship - Agent",
            # "Complete: Attack Ship - Special Agent",
            "Complete: Attack Ship - Perfect Agent",
            # "Complete: Skedar Ruins - Agent",
            # "Complete: Skedar Ruins - Special Agent",
            "Complete: Skedar Ruins - Perfect Agent",
            # "Complete: Mr. Blonde's Revenge - Agent",
            # "Complete: Mr. Blonde's Revenge - Special Agent",
            "Complete: Mr. Blonde's Revenge - Perfect Agent",
            # "Complete: Maian SOS - Agent",
            # "Complete: Maian SOS - Special Agent",
            "Complete: Maian SOS - Perfect Agent",
            # "Complete: WAR! - Agent",
            # "Complete: WAR! - Special Agent",
            "Complete: WAR! - Perfect Agent",
            # "Complete: The Duel - Agent",
            # "Complete: The Duel - Special Agent",
            "Complete: The Duel - Perfect Agent",
        ]
        for location in mission_locations:
            world.get_location(location).place_locked_item(world.create_item("Mission Star"))
    
    # Start with a random mission
    if world.options.start_with_mission:
        if world.options.goal == Goal.option_complete_skedar_ruins:
            itemID = world.random.randint(1, 20)
        else:
            itemID = world.random.randint(1, 21)
        remove_starting_item_from_pool(world, STARTING_MISSION_ID_TO_NAME[itemID], itempool)

    # Start with a random weapon
    if world.options.start_with_weapon:
        if world.options.weapon_progression.value == world.options.weapon_progression.option_vanilla:
            itemID = world.random.randint(3, 35)
            remove_starting_item_from_pool(world, list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(itemID)], itempool)
        elif world.options.weapon_progression.value > world.options.weapon_progression.option_vanilla:
            remove_starting_item_from_pool(world, "Progressive Weapon", itempool)
            

    # Fill with filler items if there is not enough items to locations
    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
    

def remove_starting_item_from_pool(world:PerfectDarkWorld, item:str, itempool:list[Item]) -> None:
    world.push_precollected(world.create_item(item))
    itempool.remove(world.create_item(item))
        