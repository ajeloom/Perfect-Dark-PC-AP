from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements, MissionLogic, WeaponProgression, ChallengeLogic

ITEM_NAME_TO_ID = {
    # "NONE": 1,
    # "UNARMED": 2,
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
    # "TESTER": 52,
    # "ROCKETLAUNCHER_34": 53,
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
	"Air Force One Lift Key Card": 74,
	"Cellar Key Card": 75,
	"Area 51 Lift Key Card": 76,
	"Cassandra's Office Key Card": 77,
	"Suitcase": 78,
	"WEAPON_BRIEFCASE": 79,
	"Shield Tech Item": 80,
	"De Vries' Necklace": 81,
    "Air Force One Left Room Key Card": 82,     # "HAMMER": 82,
    "Air Force One Right Room Key Card": 83,    # "SCREWDRIVER": 83,
    # "ROCKET": 84,
    # "HOMINGROCKET": 85,
    # "GRENADEROUND": 86,
    # "BOLT": 87,
    "Briefcase": 88,
	# "SKROCKET": 89,
    # "CHOPPERGUN": 90,
    # "WATCHLASER": 91,
    "Shield": 92,
	# "DISABLED": 93,
    # "SUICIDEPILL": 94,
    "dD Defection - Agent": 95,
    "dD Investigation - Agent": 96,
    "dD Extraction - Agent": 97,
    "Carrington Villa - Agent": 98,
    "Chicago - Agent": 99,
    "G5 Building - Agent": 100,
    "A51 Infiltration - Agent": 101,
    "A51 Rescue - Agent": 102,
    "A51 Escape - Agent": 103,
    "Air Base - Agent": 104,
    "Air Force One - Agent": 105,
    "Crash Site - Agent": 106,
    "Pelagic II - Agent": 107,
    "Deep Sea - Agent": 108,
    "CI Defense - Agent": 109,
    "Attack Ship - Agent": 110,
    "Skedar Ruins - Agent": 111,
    "Mr. Blonde's Revenge - Agent": 112,
    "Maian SOS - Agent": 113,
    "WAR! - Agent": 114,
    "The Duel - Agent": 115,
    "dD Defection - Special Agent": 116,
    "dD Investigation - Special Agent": 117,
    "dD Extraction - Special Agent": 118,
    "Carrington Villa - Special Agent": 119,
    "Chicago - Special Agent": 120,
    "G5 Building - Special Agent": 121,
    "A51 Infiltration - Special Agent": 122,
    "A51 Rescue - Special Agent": 123,
    "A51 Escape - Special Agent": 124,
    "Air Base - Special Agent": 125,
    "Air Force One - Special Agent": 126,
    "Crash Site - Special Agent": 127,
    "Pelagic II - Special Agent": 128,
    "Deep Sea - Special Agent": 129,
    "CI Defense - Special Agent": 130,
    "Attack Ship - Special Agent": 131,
    "Skedar Ruins - Special Agent": 132,
    "Mr. Blonde's Revenge - Special Agent": 133,
    "Maian SOS - Special Agent": 134,
    "WAR! - Special Agent": 135,
    "The Duel - Special Agent": 136,
    "dD Defection - Perfect Agent": 137,
    "dD Investigation - Perfect Agent": 138,
    "dD Extraction - Perfect Agent": 139,
    "Carrington Villa - Perfect Agent": 140,
    "Chicago - Perfect Agent": 141,
    "G5 Building - Perfect Agent": 142,
    "A51 Infiltration - Perfect Agent": 143,
    "A51 Rescue - Perfect Agent": 144,
    "A51 Escape - Perfect Agent": 145,
    "Air Base - Perfect Agent": 146,
    "Air Force One - Perfect Agent": 147,
    "Crash Site - Perfect Agent": 148,
    "Pelagic II - Perfect Agent": 149,
    "Deep Sea - Perfect Agent": 150,
    "CI Defense - Perfect Agent": 151,
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
    "Cheat: Hurricane Fists": 189,
    "Cheat: Cloaking Device": 190,
    "Cheat: Invincible": 191,
    "Cheat: All Guns in Solo": 192,
    "Cheat: Unlimited Ammo": 193,
    "Cheat: Unlimited Ammo, No Reloads": 194,
    "Cheat: Slo-mo Single Player": 195,
    "Cheat: DK Mode": 196,
    "Cheat: Trent's Magnum": 197,
    "Cheat: FarSight": 198,
    "Cheat: Small Jo": 199,
    "Cheat: Small Characters": 200,
    "Cheat: Enemy Shields": 201,
    "Cheat: Jo Shield": 202,
    "Cheat: Super Shield": 203,
    "Cheat: Classic Sight": 204,
    "Cheat: Team Heads Only": 205,
    "Cheat: Play as Elvis": 206,
    "Cheat: Enemy Rockets": 207,
    "Cheat: Unlimited Ammo - Laptop Sentry Gun": 208,
    "Cheat: Marquis of Queensbury Rules": 209,
    "Cheat: Perfect Darkness": 210,
    "Cheat: Pugilist": 211,
    "Cheat: Hotshot": 212,
    "Cheat: Hit and Run": 213,
    "Cheat: Alien": 214,
    "Cheat: R-Tracker/Weapon Cache Locations": 215,
    "Cheat: Rocket Launcher": 216,
    "Cheat: Sniper Rifle": 217,
    "Cheat: X-Ray Scanner": 218,
    "Cheat: SuperDragon": 219,
    "Cheat: Laptop Gun": 220,
    "Cheat: Phoenix": 221,
    "Cheat: Psychosis Gun": 222,
    "Cheat: PP9i": 223,
    "Cheat: CC13": 224,
    "Cheat: KL01313": 225,
    "Cheat: KF7 Special": 226,
    "Cheat: ZZT (9mm)": 227,
    "Cheat: DMC": 228,
    "Cheat: AR53": 229,
    "Cheat: RC-P45": 230,
    "dataDyne Master Key": 231,
    "G5 Building Master Key": 232,
    "Area 51 Master Key": 233,
    "Air Force One Master Key": 234,
    "Cheese": 235,
    "Trap": 236,
    "Mission Star": 237,
    "Challenge Star": 238,
    "Skedar Ruins": 239,
    "Victory": 240,
    "Progressive Pistol": 241,
    "Progressive SMG": 242,
    "Progressive Rifle": 243,
    "Progressive Explosive": 244,
    "Progressive Other Weapon": 245,
}


DEFAULT_ITEM_CLASSIFICATIONS = {
    # "NONE": ItemClassification.filler,
    # "UNARMED": ItemClassification.progression,
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
    "Combat Boost": ItemClassification.useful,
	"PP9i": ItemClassification.progression,
	"CC13": ItemClassification.progression,
	"KL01313": ItemClassification.progression,
	"KF7 Special": ItemClassification.progression,
	"ZZT (9mm)": ItemClassification.progression,
	"DMC": ItemClassification.progression,
	"AR53": ItemClassification.progression,
	"RC-P45": ItemClassification.progression,
    "Psychosis Gun": ItemClassification.filler,
	"Night Vision": ItemClassification.progression | ItemClassification.useful,
	"CamSpy": ItemClassification.progression | ItemClassification.useful,
	"X-Ray Scanner": ItemClassification.progression | ItemClassification.useful,
	"IR Scanner": ItemClassification.progression | ItemClassification.useful,
	"Cloaking Device": ItemClassification.progression | ItemClassification.useful,
	"Horizon Scanner": ItemClassification.filler,
    # "TESTER": ItemClassification.filler,
    # "ROCKETLAUNCHER_34": ItemClassification.filler,
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
	"Air Force One Lift Key Card": ItemClassification.progression | ItemClassification.useful,
	"Cellar Key Card": ItemClassification.progression | ItemClassification.useful,
	"Area 51 Lift Key Card": ItemClassification.progression | ItemClassification.useful,
	"Cassandra's Office Key Card": ItemClassification.filler,
	"Suitcase": ItemClassification.progression | ItemClassification.useful,
	"WEAPON_BRIEFCASE": ItemClassification.filler,
	"Shield Tech Item": ItemClassification.progression | ItemClassification.useful,
	"De Vries' Necklace": ItemClassification.progression | ItemClassification.useful,
    "Air Force One Left Room Key Card": ItemClassification.filler,                      # "HAMMER": ItemClassification.filler,
    "Air Force One Right Room Key Card": ItemClassification.filler,                     # "SCREWDRIVER": ItemClassification.filler,
    # "ROCKET": ItemClassification.filler,
    # "HOMINGROCKET": ItemClassification.filler,
    # "GRENADEROUND": ItemClassification.filler,
    # "BOLT": ItemClassification.filler,
    "Briefcase": ItemClassification.progression | ItemClassification.useful,
	# "SKROCKET": ItemClassification.filler,
    # "CHOPPERGUN": ItemClassification.filler,
    # "WATCHLASER": ItemClassification.filler,
    "Shield": ItemClassification.useful,
	# "DISABLED": ItemClassification.filler,
    # "SUICIDEPILL": ItemClassification.filler,
    "dD Defection - Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Defection - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Defection - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Investigation - Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Investigation - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Investigation - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Extraction - Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Extraction - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "dD Extraction - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa - Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "Chicago - Agent": ItemClassification.progression | ItemClassification.useful,
    "Chicago - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "Chicago - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "G5 Building - Agent": ItemClassification.progression | ItemClassification.useful,
    "G5 Building - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "G5 Building - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Infiltration - Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Infiltration - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Infiltration - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Rescue - Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Rescue - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Rescue - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Escape - Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Escape - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "A51 Escape - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
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
    "CI Defense - Agent": ItemClassification.progression | ItemClassification.useful,
    "CI Defense - Special Agent": ItemClassification.progression | ItemClassification.useful,
    "CI Defense - Perfect Agent": ItemClassification.progression | ItemClassification.useful,
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
    "Cheat: DK Mode": ItemClassification.useful,
    "Cheat: Small Jo": ItemClassification.filler,
    "Cheat: Small Characters": ItemClassification.filler,
    "Cheat: Team Heads Only": ItemClassification.filler,
    "Cheat: Play as Elvis": ItemClassification.filler,
    "Cheat: Slo-mo Single Player": ItemClassification.filler,
    "Cheat: Invincible": ItemClassification.useful,
    "Cheat: Cloaking Device": ItemClassification.useful,
    "Cheat: Marquis of Queensbury Rules": ItemClassification.useful,
    "Cheat: Jo Shield": ItemClassification.useful,
    "Cheat: Super Shield": ItemClassification.useful,
    "Cheat: Enemy Shields": ItemClassification.filler,
    "Cheat: Enemy Rockets": ItemClassification.filler,
    "Cheat: Perfect Darkness": ItemClassification.filler,
    "Cheat: Rocket Launcher": ItemClassification.useful,
    "Cheat: Sniper Rifle": ItemClassification.useful,
    "Cheat: SuperDragon": ItemClassification.useful,
    "Cheat: Laptop Gun": ItemClassification.useful,
    "Cheat: Phoenix": ItemClassification.useful,
    "Cheat: Psychosis Gun": ItemClassification.useful,
    "Cheat: Trent's Magnum": ItemClassification.useful,
    "Cheat: FarSight": ItemClassification.useful,
    "Cheat: PP9i": ItemClassification.useful,
    "Cheat: CC13": ItemClassification.useful,
    "Cheat: KL01313": ItemClassification.useful,
    "Cheat: KF7 Special": ItemClassification.useful,
    "Cheat: ZZT (9mm)": ItemClassification.useful,
    "Cheat: DMC": ItemClassification.useful,
    "Cheat: AR53": ItemClassification.useful,
    "Cheat: RC-P45": ItemClassification.useful,
    "Cheat: Classic Sight": ItemClassification.filler,
    "Cheat: Unlimited Ammo - Laptop Sentry Gun": ItemClassification.useful,
    "Cheat: Hurricane Fists": ItemClassification.filler,
    "Cheat: Unlimited Ammo": ItemClassification.useful,
    "Cheat: Unlimited Ammo, No Reloads": ItemClassification.useful,
    "Cheat: X-Ray Scanner": ItemClassification.useful,
    "Cheat: R-Tracker/Weapon Cache Locations": ItemClassification.useful,
    "Cheat: All Guns in Solo": ItemClassification.useful,
    "Cheat: Pugilist": ItemClassification.filler,
    "Cheat: Hotshot": ItemClassification.useful,
    "Cheat: Hit and Run": ItemClassification.useful,
    "Cheat: Alien": ItemClassification.useful,
    "dataDyne Master Key": ItemClassification.progression | ItemClassification.useful,
    "G5 Building Master Key": ItemClassification.progression | ItemClassification.useful,
    "Area 51 Master Key": ItemClassification.progression | ItemClassification.useful,
    "Air Force One Master Key": ItemClassification.progression | ItemClassification.useful,
    "Cheese": ItemClassification.filler,
    "Trap": ItemClassification.trap,
    "Mission Star": ItemClassification.progression | ItemClassification.useful,
    "Challenge Star": ItemClassification.progression | ItemClassification.useful,
    "Skedar Ruins": ItemClassification.progression | ItemClassification.useful,
    "Victory": ItemClassification.progression | ItemClassification.useful,
    "Progressive Pistol": ItemClassification.progression | ItemClassification.useful,
    "Progressive SMG": ItemClassification.progression | ItemClassification.useful,
    "Progressive Rifle": ItemClassification.progression | ItemClassification.useful,
    "Progressive Explosive": ItemClassification.progression | ItemClassification.useful,
    "Progressive Other Weapon": ItemClassification.progression | ItemClassification.useful,
}


class PerfectDarkItem(Item):
    game = "Perfect Dark"


def get_random_filler_item_name(world: PerfectDarkWorld) -> str:
    # if world.random.randint(0, 99) < world.options.trap_chance:
    #     return "Trap"
    return "Cheese"


def create_item_with_correct_classification(world: PerfectDarkWorld, name: str) -> PerfectDarkItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if (world.options.challenge_logic.value == ChallengeLogic.option_strict
            and has_challenges(world)
            and (name == "Combat Boost" or name == "Shield")):
        classification = ItemClassification.progression | ItemClassification.useful

    if (world.options.challenge_logic.value == ChallengeLogic.option_normal
            and has_challenges(world)
            and name == "Shield"):
        classification = ItemClassification.progression | ItemClassification.useful

    if ((world.options.mission_logic.value == MissionLogic.option_veteran 
            or world.options.mission_logic.value == MissionLogic.option_hard)
            and world.options.weapon_progression.value == WeaponProgression.option_normal):
        if name == "Air Force One Left Room Key Card" or name == "Air Force One Right Room Key Card":
            classification = ItemClassification.progression | ItemClassification.useful

    return PerfectDarkItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world:PerfectDarkWorld) -> None:
    itempool: list[Item] = []
    
    # Create items found in any difficulty
    if world.options.agent \
            or world.options.special_agent \
            or world.options.perfect_agent:
        itempool.append(world.create_item("Combat Boost"))
        itempool.append(world.create_item("Night Vision"))
        itempool.append(world.create_item("CamSpy"))
        itempool.append(world.create_item("X-Ray Scanner"))
        itempool.append(world.create_item("IR Scanner"))
        itempool.append(world.create_item("Cloaking Device"))
        itempool.append(world.create_item("Horizon Scanner"))
        itempool.append(world.create_item("Data Uplink"))
        itempool.append(world.create_item("R-Tracker"))
        itempool.append(world.create_item("President Scanner"))
        itempool.append(world.create_item("Door Decoder"))
        itempool.append(world.create_item("Alien Medpack"))
        itempool.append(world.create_item("Explosives"))
        itempool.append(world.create_item("Target Amplifier"))
        itempool.append(world.create_item("Lab Clothes"))
        itempool.append(world.create_item("Stewardess Disguise"))
        itempool.append(world.create_item("Backup Disk"))
        itempool.append(world.create_item("Cellar Key Card"))
        itempool.append(world.create_item("Suitcase"))

    # Create ECM Mine
    if world.options.special_agent \
            or world.options.perfect_agent \
            or world.options.device_training:
        itempool.append(world.create_item("ECM Mine"))

    # Device Training only items
    if world.options.device_training \
            and not world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent:
        itempool.append(world.create_item("Data Uplink"))
        itempool.append(world.create_item("CamSpy"))
        itempool.append(world.create_item("Night Vision"))
        itempool.append(world.create_item("Door Decoder"))
        itempool.append(world.create_item("R-Tracker"))
        itempool.append(world.create_item("IR Scanner"))
        itempool.append(world.create_item("X-Ray Scanner"))
        itempool.append(world.create_item("Stewardess Disguise"))
        itempool.append(world.create_item("Cloaking Device"))

    # Create items needed for Skedar Ruins
    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        if not world.options.device_training:
            itempool.append(world.create_item("IR Scanner"))
            itempool.append(world.create_item("R-Tracker"))

        if not world.options.agent \
                and not world.options.special_agent \
                and not world.options.perfect_agent:
            itempool.append(world.create_item("Target Amplifier"))

    # Cheats
    if world.options.include_cheats_in_item_pool:
        itempool.append(world.create_item("Cheat: DK Mode"))
        itempool.append(world.create_item("Cheat: Small Jo"))
        itempool.append(world.create_item("Cheat: Small Characters"))
        itempool.append(world.create_item("Cheat: Team Heads Only"))
        itempool.append(world.create_item("Cheat: Play as Elvis"))
        itempool.append(world.create_item("Cheat: Slo-mo Single Player"))
        itempool.append(world.create_item("Cheat: Invincible"))
        itempool.append(world.create_item("Cheat: Cloaking Device"))
        itempool.append(world.create_item("Cheat: Marquis of Queensbury Rules"))
        itempool.append(world.create_item("Cheat: Jo Shield"))
        itempool.append(world.create_item("Cheat: Super Shield"))
        itempool.append(world.create_item("Cheat: Enemy Shields"))
        itempool.append(world.create_item("Cheat: Enemy Rockets"))
        itempool.append(world.create_item("Cheat: Perfect Darkness"))
        itempool.append(world.create_item("Cheat: Rocket Launcher"))
        itempool.append(world.create_item("Cheat: Sniper Rifle"))
        itempool.append(world.create_item("Cheat: SuperDragon"))
        itempool.append(world.create_item("Cheat: Laptop Gun"))
        itempool.append(world.create_item("Cheat: Phoenix"))
        itempool.append(world.create_item("Cheat: Psychosis Gun"))
        itempool.append(world.create_item("Cheat: Trent's Magnum"))
        itempool.append(world.create_item("Cheat: FarSight"))
        itempool.append(world.create_item("Cheat: PP9i"))
        itempool.append(world.create_item("Cheat: CC13"))
        itempool.append(world.create_item("Cheat: KL01313"))
        itempool.append(world.create_item("Cheat: KF7 Special"))
        itempool.append(world.create_item("Cheat: ZZT (9mm)"))
        itempool.append(world.create_item("Cheat: DMC"))
        itempool.append(world.create_item("Cheat: AR53"))
        itempool.append(world.create_item("Cheat: RC-P45"))
        itempool.append(world.create_item("Cheat: Classic Sight"))
        itempool.append(world.create_item("Cheat: Unlimited Ammo - Laptop Sentry Gun"))
        itempool.append(world.create_item("Cheat: Hurricane Fists"))
        itempool.append(world.create_item("Cheat: Unlimited Ammo"))
        itempool.append(world.create_item("Cheat: Unlimited Ammo, No Reloads"))
        itempool.append(world.create_item("Cheat: X-Ray Scanner"))
        itempool.append(world.create_item("Cheat: R-Tracker/Weapon Cache Locations"))
        itempool.append(world.create_item("Cheat: All Guns in Solo"))
        itempool.append(world.create_item("Cheat: Pugilist"))
        itempool.append(world.create_item("Cheat: Hotshot"))
        itempool.append(world.create_item("Cheat: Hit and Run"))
        itempool.append(world.create_item("Cheat: Alien"))

    # Key Cards
    if world.options.agent or world.options.special_agent or world.options.perfect_agent:
        if world.options.master_key:
            itempool.append(world.create_item("G5 Building Master Key"))
            itempool.append(world.create_item("Area 51 Master Key"))

            if world.options.special_agent or world.options.perfect_agent:
                itempool.append(world.create_item("dataDyne Master Key"))

            if (world.options.mission_logic.value == MissionLogic.option_veteran
                    or world.options.mission_logic.value == MissionLogic.option_hard
                    or world.options.special_agent
                    or world.options.perfect_agent):
                itempool.append(world.create_item("Air Force One Master Key"))

        else:
            itempool.append(world.create_item("G5 Building Level 1 Key Card"))
            itempool.append(world.create_item("G5 Building Level 2 Key Card"))
            itempool.append(world.create_item("Medlab 2 Key Card"))
            itempool.append(world.create_item("Op Room Key Card"))
            itempool.append(world.create_item("Area 51 Lift Key Card"))
            itempool.append(world.create_item("Cassandra's Office Key Card"))
            itempool.append(world.create_item("Air Force One Left Room Key Card"))
            itempool.append(world.create_item("Air Force One Right Room Key Card"))

            if world.options.special_agent or world.options.perfect_agent:
                itempool.append(world.create_item("Air Force One Lift Key Card"))
                itempool.append(world.create_item("De Vries' Necklace"))


    # Shield
    if world.options.agent or world.options.special_agent or has_challenges(world):
        itempool.append(world.create_item("Shield"))


    # Items only in Agent
    if world.options.agent:
        itempool.append(world.create_item("dD Defection - Agent"))
        itempool.append(world.create_item("dD Investigation - Agent"))
        itempool.append(world.create_item("dD Extraction - Agent"))
        itempool.append(world.create_item("Carrington Villa - Agent"))
        itempool.append(world.create_item("Chicago - Agent"))
        itempool.append(world.create_item("G5 Building - Agent"))
        itempool.append(world.create_item("A51 Infiltration - Agent"))
        itempool.append(world.create_item("A51 Rescue - Agent"))
        itempool.append(world.create_item("A51 Escape - Agent"))
        itempool.append(world.create_item("Air Base - Agent"))
        itempool.append(world.create_item("Air Force One - Agent"))
        itempool.append(world.create_item("Crash Site - Agent"))
        itempool.append(world.create_item("Pelagic II - Agent"))
        itempool.append(world.create_item("Deep Sea - Agent"))
        itempool.append(world.create_item("CI Defense - Agent"))
        itempool.append(world.create_item("Attack Ship - Agent"))
        itempool.append(world.create_item("Mr. Blonde's Revenge - Agent"))
        itempool.append(world.create_item("Maian SOS - Agent"))
        itempool.append(world.create_item("WAR! - Agent"))
        itempool.append(world.create_item("The Duel - Agent"))

        if (is_skedar_ruins_in_itempool(world)):
            itempool.append(world.create_item("Skedar Ruins - Agent"))


    # Items in both Special and Perfect Agent
    if world.options.special_agent or world.options.perfect_agent:
        itempool.append(world.create_item("Skedar Bomb"))
        itempool.append(world.create_item("Comms Rider"))


    # Items only in Special Agent
    if world.options.special_agent:
        itempool.append(world.create_item("dD Defection - Special Agent"))
        itempool.append(world.create_item("dD Investigation - Special Agent"))
        itempool.append(world.create_item("dD Extraction - Special Agent"))
        itempool.append(world.create_item("Carrington Villa - Special Agent"))
        itempool.append(world.create_item("Chicago - Special Agent"))
        itempool.append(world.create_item("G5 Building - Special Agent"))
        itempool.append(world.create_item("A51 Infiltration - Special Agent"))
        itempool.append(world.create_item("A51 Rescue - Special Agent"))
        itempool.append(world.create_item("A51 Escape - Special Agent"))
        itempool.append(world.create_item("Air Base - Special Agent"))
        itempool.append(world.create_item("Air Force One - Special Agent"))
        itempool.append(world.create_item("Crash Site - Special Agent"))
        itempool.append(world.create_item("Pelagic II - Special Agent"))
        itempool.append(world.create_item("Deep Sea - Special Agent"))
        itempool.append(world.create_item("CI Defense - Special Agent"))
        itempool.append(world.create_item("Attack Ship - Special Agent"))
        itempool.append(world.create_item("Mr. Blonde's Revenge - Special Agent"))
        itempool.append(world.create_item("Maian SOS - Special Agent"))
        itempool.append(world.create_item("WAR! - Special Agent"))
        itempool.append(world.create_item("The Duel - Special Agent"))

        if (is_skedar_ruins_in_itempool(world)):
            itempool.append(world.create_item("Skedar Ruins - Special Agent"))


    # Items only in Perfect Agent
    if world.options.perfect_agent:
        itempool.append(world.create_item("Tracer Bug"))
        itempool.append(world.create_item("Flight Plans"))
        itempool.append(world.create_item("Research Tape"))
        itempool.append(world.create_item("Shield Tech Item"))
        itempool.append(world.create_item("dD Defection - Perfect Agent"))
        itempool.append(world.create_item("dD Investigation - Perfect Agent"))
        itempool.append(world.create_item("dD Extraction - Perfect Agent"))
        itempool.append(world.create_item("Carrington Villa - Perfect Agent"))
        itempool.append(world.create_item("Chicago - Perfect Agent"))
        itempool.append(world.create_item("G5 Building - Perfect Agent"))
        itempool.append(world.create_item("A51 Infiltration - Perfect Agent"))
        itempool.append(world.create_item("A51 Rescue - Perfect Agent"))
        itempool.append(world.create_item("A51 Escape - Perfect Agent"))
        itempool.append(world.create_item("Air Base - Perfect Agent"))
        itempool.append(world.create_item("Air Force One - Perfect Agent"))
        itempool.append(world.create_item("Crash Site - Perfect Agent"))
        itempool.append(world.create_item("Pelagic II - Perfect Agent"))
        itempool.append(world.create_item("Deep Sea - Perfect Agent"))
        itempool.append(world.create_item("CI Defense - Perfect Agent"))
        itempool.append(world.create_item("Attack Ship - Perfect Agent"))
        itempool.append(world.create_item("Mr. Blonde's Revenge - Perfect Agent"))
        itempool.append(world.create_item("Maian SOS - Perfect Agent"))
        itempool.append(world.create_item("WAR! - Perfect Agent"))
        itempool.append(world.create_item("The Duel - Perfect Agent"))

        if (is_skedar_ruins_in_itempool(world)):
            itempool.append(world.create_item("Skedar Ruins - Perfect Agent"))


    # Weapons
    if (world.options.weapon_progression.value == WeaponProgression.option_normal
            or world.options.weapon_progression.value == WeaponProgression.option_all_guns):
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
        itempool.append(world.create_item("Psychosis Gun"))

        if world.options.weapon_progression.value == WeaponProgression.option_all_guns:
            itempool.append(world.create_item("PP9i"))
            itempool.append(world.create_item("CC13"))
            itempool.append(world.create_item("KL01313"))
            itempool.append(world.create_item("KF7 Special"))
            itempool.append(world.create_item("ZZT (9mm)"))
            itempool.append(world.create_item("DMC"))
            itempool.append(world.create_item("AR53"))
            itempool.append(world.create_item("RC-P45"))

    elif (world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon
            or world.options.weapon_progression.value == WeaponProgression.option_progressive_one_gun):
        itempool.append(world.create_item("RC-P120"))
        itempool.append(world.create_item("Devastator"))
        itempool.append(world.create_item("Timed Mine"))
        itempool.append(world.create_item("Remote Mine"))
        if world.options.perfect_agent:
            itempool.append(world.create_item("K7 Avenger"))
            itempool.append(world.create_item("FarSight XR-20"))

        for x in range(42):
            itempool.append(world.create_item("Progressive Weapon"))
    elif world.options.weapon_progression.value == WeaponProgression.option_progressive_types:
        for x in range(10):
            itempool.append(world.create_item("Progressive Pistol"))
        for x in range(9):
            itempool.append(world.create_item("Progressive SMG"))
        for x in range(6):
            itempool.append(world.create_item("Progressive Rifle"))
        for x in range(8):
            itempool.append(world.create_item("Progressive Explosive"))
        for x in range(9):
            itempool.append(world.create_item("Progressive Other Weapon"))


    # Challenges
    if (has_challenges(world)):
        itempool.append(world.create_item("Briefcase"))

        if not world.options.device_training \
                and not world.options.agent \
                and not world.options.special_agent \
                and not world.options.perfect_agent:
            itempool.append(world.create_item("Data Uplink"))

        if world.options.challenge_logic.value == ChallengeLogic.option_strict \
                and not world.options.agent \
                and not world.options.special_agent \
                and not world.options.perfect_agent:
            itempool.append(world.create_item("Combat Boost"))

        if world.options.challenge_logic.value < ChallengeLogic.option_hard \
                and not world.options.device_training \
                and not world.options.agent \
                and not world.options.special_agent \
                and not world.options.perfect_agent:
            itempool.append(world.create_item("Cloaking Device"))

        for x in range(1, 31):
            challenge_name = f"Challenge {x}"
            if (world.options.excluded_challenges.__contains__(challenge_name) == False):
                itempool.append(world.create_item(challenge_name))
    
                if world.options.start_with_all_challenges:
                    remove_starting_item_from_pool(world, challenge_name, itempool)


    # Place items based on the goal
    if world.options.goal == Goal.option_complete_skedar_ruins:
        if world.options.agent:
            world.get_location("Complete: Skedar Ruins - Agent").place_locked_item(world.create_item("Victory"))
        if world.options.special_agent:
            world.get_location("Complete: Skedar Ruins - Special Agent").place_locked_item(world.create_item("Victory"))
        if world.options.perfect_agent:
            world.get_location("Complete: Skedar Ruins - Perfect Agent").place_locked_item(world.create_item("Victory"))

        if not world.options.agent \
                and not world.options.special_agent \
                and not world.options.perfect_agent:
            world.get_location("Complete: Skedar Ruins - Agent").place_locked_item(world.create_item("Victory"))
            world.get_location("Complete: Skedar Ruins - Special Agent").place_locked_item(world.create_item("Victory"))
            world.get_location("Complete: Skedar Ruins - Perfect Agent").place_locked_item(world.create_item("Victory"))

        if (world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_mission_stars
                or world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_both_stars):
            mission_locations = []

            if world.options.agent:
                mission_locations.append("Complete: dD Defection - Agent")
                mission_locations.append("Complete: dD Investigation - Agent")
                mission_locations.append("Complete: dD Extraction - Agent")
                mission_locations.append("Complete: Carrington Villa - Agent")
                mission_locations.append("Complete: Chicago - Agent")
                mission_locations.append("Complete: G5 Building - Agent")
                mission_locations.append("Complete: A51 Infiltration - Agent")
                mission_locations.append("Complete: A51 Rescue - Agent")
                mission_locations.append("Complete: A51 Escape - Agent")
                mission_locations.append("Complete: Air Base - Agent")
                mission_locations.append("Complete: Air Force One - Agent")
                mission_locations.append("Complete: Crash Site - Agent")
                mission_locations.append("Complete: Pelagic II - Agent")
                mission_locations.append("Complete: Deep Sea - Agent")
                mission_locations.append("Complete: CI Defense - Agent")
                mission_locations.append("Complete: Attack Ship - Agent")
                mission_locations.append("Complete: Mr. Blonde's Revenge - Agent")
                mission_locations.append("Complete: Maian SOS - Agent")
                mission_locations.append("Complete: WAR! - Agent")
                mission_locations.append("Complete: The Duel - Agent")

            if world.options.special_agent:
                mission_locations.append("Complete: dD Defection - Special Agent")
                mission_locations.append("Complete: dD Investigation - Special Agent")
                mission_locations.append("Complete: dD Extraction - Special Agent")
                mission_locations.append("Complete: Carrington Villa - Special Agent")
                mission_locations.append("Complete: Chicago - Special Agent")
                mission_locations.append("Complete: G5 Building - Special Agent")
                mission_locations.append("Complete: A51 Infiltration - Special Agent")
                mission_locations.append("Complete: A51 Rescue - Special Agent")
                mission_locations.append("Complete: A51 Escape - Special Agent")
                mission_locations.append("Complete: Air Base - Special Agent")
                mission_locations.append("Complete: Air Force One - Special Agent")
                mission_locations.append("Complete: Crash Site - Special Agent")
                mission_locations.append("Complete: Pelagic II - Special Agent")
                mission_locations.append("Complete: Deep Sea - Special Agent")
                mission_locations.append("Complete: CI Defense - Special Agent")
                mission_locations.append("Complete: Attack Ship - Special Agent")
                mission_locations.append("Complete: Mr. Blonde's Revenge - Special Agent")
                mission_locations.append("Complete: Maian SOS - Special Agent")
                mission_locations.append("Complete: WAR! - Special Agent")
                mission_locations.append("Complete: The Duel - Special Agent")

            if world.options.perfect_agent:
                mission_locations.append("Complete: dD Defection - Perfect Agent")
                mission_locations.append("Complete: dD Investigation - Perfect Agent")
                mission_locations.append("Complete: dD Extraction - Perfect Agent")
                mission_locations.append("Complete: Carrington Villa - Perfect Agent")
                mission_locations.append("Complete: Chicago - Perfect Agent")
                mission_locations.append("Complete: G5 Building - Perfect Agent")
                mission_locations.append("Complete: A51 Infiltration - Perfect Agent")
                mission_locations.append("Complete: A51 Rescue - Perfect Agent")
                mission_locations.append("Complete: A51 Escape - Perfect Agent")
                mission_locations.append("Complete: Air Base - Perfect Agent")
                mission_locations.append("Complete: Air Force One - Perfect Agent")
                mission_locations.append("Complete: Crash Site - Perfect Agent")
                mission_locations.append("Complete: Pelagic II - Perfect Agent")
                mission_locations.append("Complete: Deep Sea - Perfect Agent")
                mission_locations.append("Complete: CI Defense - Perfect Agent")
                mission_locations.append("Complete: Attack Ship - Perfect Agent")
                mission_locations.append("Complete: Mr. Blonde's Revenge - Perfect Agent")
                mission_locations.append("Complete: Maian SOS - Perfect Agent")
                mission_locations.append("Complete: WAR! - Perfect Agent")
                mission_locations.append("Complete: The Duel - Perfect Agent")

            for location in mission_locations:
                world.get_location(location).place_locked_item(world.create_item("Mission Star"))

        if (world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_challenge_stars
                or world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_collect_both_stars):
            set_challenge_stars(world)

        if world.options.skedar_ruins_requirements.value >= SkedarRuinsRequirements.option_collect_mission_stars:
            world.get_location("Collect All Stars").place_locked_item(world.create_item("Skedar Ruins"))

    elif world.options.goal == Goal.option_complete_missions:
        set_mission_stars(world)

        world.get_location("Collect All Stars").place_locked_item(world.create_item("Victory"))

    elif world.options.goal == Goal.option_complete_challenges:
        set_challenge_stars(world)

        world.get_location("Collect All Stars").place_locked_item(world.create_item("Victory"))

    elif world.options.goal == Goal.option_complete_both:
        set_mission_stars(world)
        set_challenge_stars(world)

        world.get_location("Collect All Stars").place_locked_item(world.create_item("Victory"))


    # Start with a random mission
    if world.options.start_with_mission:
        missions = []

        if world.options.agent:
            missions.append("dD Defection - Agent")
            missions.append("dD Investigation - Agent")
            missions.append("dD Extraction - Agent")
            missions.append("Carrington Villa - Agent")
            missions.append("Chicago - Agent")
            missions.append("G5 Building - Agent")
            missions.append("A51 Infiltration - Agent")
            missions.append("A51 Rescue - Agent")
            missions.append("A51 Escape - Agent")
            missions.append("Air Base - Agent")
            missions.append("Air Force One - Agent")
            missions.append("Crash Site - Agent")
            missions.append("Pelagic II - Agent")
            missions.append("Deep Sea - Agent")
            missions.append("CI Defense - Agent")
            missions.append("Attack Ship - Agent")
            missions.append("Mr. Blonde's Revenge - Agent")
            missions.append("Maian SOS - Agent")
            missions.append("WAR! - Agent")
            missions.append("The Duel - Agent")

        if world.options.special_agent:
            missions.append("dD Defection - Special Agent")
            missions.append("dD Investigation - Special Agent")
            missions.append("dD Extraction - Special Agent")
            missions.append("Carrington Villa - Special Agent")
            missions.append("Chicago - Special Agent")
            missions.append("G5 Building - Special Agent")
            missions.append("A51 Infiltration - Special Agent")
            missions.append("A51 Rescue - Special Agent")
            missions.append("A51 Escape - Special Agent")
            missions.append("Air Base - Special Agent")
            missions.append("Air Force One - Special Agent")
            missions.append("Crash Site - Special Agent")
            missions.append("Pelagic II - Special Agent")
            missions.append("Deep Sea - Special Agent")
            missions.append("CI Defense - Special Agent")
            missions.append("Attack Ship - Special Agent")
            missions.append("Mr. Blonde's Revenge - Special Agent")
            missions.append("Maian SOS - Special Agent")
            missions.append("WAR! - Special Agent")
            missions.append("The Duel - Special Agent")

        if world.options.perfect_agent:
            missions.append("dD Defection - Perfect Agent")
            missions.append("dD Investigation - Perfect Agent")
            missions.append("dD Extraction - Perfect Agent")
            missions.append("Carrington Villa - Perfect Agent")
            missions.append("Chicago - Perfect Agent")
            missions.append("G5 Building - Perfect Agent")
            missions.append("A51 Infiltration - Perfect Agent")
            missions.append("A51 Rescue - Perfect Agent")
            missions.append("A51 Escape - Perfect Agent")
            missions.append("Air Base - Perfect Agent")
            missions.append("Air Force One - Perfect Agent")
            missions.append("Crash Site - Perfect Agent")
            missions.append("Pelagic II - Perfect Agent")
            missions.append("Deep Sea - Perfect Agent")
            missions.append("CI Defense - Perfect Agent")
            missions.append("Attack Ship - Perfect Agent")
            missions.append("Mr. Blonde's Revenge - Perfect Agent")
            missions.append("Maian SOS - Perfect Agent")
            missions.append("WAR! - Perfect Agent")
            missions.append("The Duel - Perfect Agent")

        if (is_skedar_ruins_in_itempool(world)):
            if world.options.agent:
                missions.append("Skedar Ruins - Agent")
            if world.options.special_agent:
                missions.append("Skedar Ruins - Special Agent")
            if world.options.perfect_agent:
                missions.append("Skedar Ruins - Perfect Agent")

        item = world.random.choice(missions)
        remove_starting_item_from_pool(world, item, itempool)


    # Start with a random weapon
    if world.options.start_with_weapon:
        if world.options.weapon_progression.value == WeaponProgression.option_normal:
            itemID = world.random.randint(3, 35)
            remove_starting_item_from_pool(world, list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(itemID)], itempool)
        elif world.options.weapon_progression.value == WeaponProgression.option_all_guns:
            itemID = world.random.randint(3, 44)
            while itemID == 36:
                itemID = world.random.randint(3, 44)
            remove_starting_item_from_pool(world, list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(itemID)], itempool)
        elif (world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon
                or world.options.weapon_progression.value == WeaponProgression.option_progressive_one_gun):
            remove_starting_item_from_pool(world, "Progressive Weapon", itempool)
        elif world.options.weapon_progression.value == WeaponProgression.option_progressive_types:
            itemID = world.random.randint(241, 245)
            remove_starting_item_from_pool(world, list(ITEM_NAME_TO_ID.keys())[list(ITEM_NAME_TO_ID.values()).index(itemID)], itempool)


    # Fill with filler items if there is not enough items to locations
    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
    

def remove_starting_item_from_pool(world:PerfectDarkWorld, item:str, itempool:list[Item]) -> None:
    world.push_precollected(world.create_item(item))
    itempool.remove(world.create_item(item))


def is_skedar_ruins_in_itempool(world: PerfectDarkWorld) -> bool:
    if ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value == SkedarRuinsRequirements.option_item)
            or world.options.goal.value >= Goal.option_complete_missions):
        return True
    else:
        return False

def set_mission_stars(world: PerfectDarkWorld) -> None:
    mission_locations = []

    if world.options.agent:
        mission_locations.append("Complete: dD Defection - Agent")
        mission_locations.append("Complete: dD Investigation - Agent")
        mission_locations.append("Complete: dD Extraction - Agent")
        mission_locations.append("Complete: Carrington Villa - Agent")
        mission_locations.append("Complete: Chicago - Agent")
        mission_locations.append("Complete: G5 Building - Agent")
        mission_locations.append("Complete: A51 Infiltration - Agent")
        mission_locations.append("Complete: A51 Rescue - Agent")
        mission_locations.append("Complete: A51 Escape - Agent")
        mission_locations.append("Complete: Air Base - Agent")
        mission_locations.append("Complete: Air Force One - Agent")
        mission_locations.append("Complete: Crash Site - Agent")
        mission_locations.append("Complete: Pelagic II - Agent")
        mission_locations.append("Complete: Deep Sea - Agent")
        mission_locations.append("Complete: CI Defense - Agent")
        mission_locations.append("Complete: Attack Ship - Agent")
        mission_locations.append("Complete: Skedar Ruins - Agent")
        mission_locations.append("Complete: Mr. Blonde's Revenge - Agent")
        mission_locations.append("Complete: Maian SOS - Agent")
        mission_locations.append("Complete: WAR! - Agent")
        mission_locations.append("Complete: The Duel - Agent")

    if world.options.special_agent:
        mission_locations.append("Complete: dD Defection - Special Agent")
        mission_locations.append("Complete: dD Investigation - Special Agent")
        mission_locations.append("Complete: dD Extraction - Special Agent")
        mission_locations.append("Complete: Carrington Villa - Special Agent")
        mission_locations.append("Complete: Chicago - Special Agent")
        mission_locations.append("Complete: G5 Building - Special Agent")
        mission_locations.append("Complete: A51 Infiltration - Special Agent")
        mission_locations.append("Complete: A51 Rescue - Special Agent")
        mission_locations.append("Complete: A51 Escape - Special Agent")
        mission_locations.append("Complete: Air Base - Special Agent")
        mission_locations.append("Complete: Air Force One - Special Agent")
        mission_locations.append("Complete: Crash Site - Special Agent")
        mission_locations.append("Complete: Pelagic II - Special Agent")
        mission_locations.append("Complete: Deep Sea - Special Agent")
        mission_locations.append("Complete: CI Defense - Special Agent")
        mission_locations.append("Complete: Attack Ship - Special Agent")
        mission_locations.append("Complete: Skedar Ruins - Special Agent")
        mission_locations.append("Complete: Mr. Blonde's Revenge - Special Agent")
        mission_locations.append("Complete: Maian SOS - Special Agent")
        mission_locations.append("Complete: WAR! - Special Agent")
        mission_locations.append("Complete: The Duel - Special Agent")

    if world.options.perfect_agent:
        mission_locations.append("Complete: dD Defection - Perfect Agent")
        mission_locations.append("Complete: dD Investigation - Perfect Agent")
        mission_locations.append("Complete: dD Extraction - Perfect Agent")
        mission_locations.append("Complete: Carrington Villa - Perfect Agent")
        mission_locations.append("Complete: Chicago - Perfect Agent")
        mission_locations.append("Complete: G5 Building - Perfect Agent")
        mission_locations.append("Complete: A51 Infiltration - Perfect Agent")
        mission_locations.append("Complete: A51 Rescue - Perfect Agent")
        mission_locations.append("Complete: A51 Escape - Perfect Agent")
        mission_locations.append("Complete: Air Base - Perfect Agent")
        mission_locations.append("Complete: Air Force One - Perfect Agent")
        mission_locations.append("Complete: Crash Site - Perfect Agent")
        mission_locations.append("Complete: Pelagic II - Perfect Agent")
        mission_locations.append("Complete: Deep Sea - Perfect Agent")
        mission_locations.append("Complete: CI Defense - Perfect Agent")
        mission_locations.append("Complete: Attack Ship - Perfect Agent")
        mission_locations.append("Complete: Skedar Ruins - Perfect Agent")
        mission_locations.append("Complete: Mr. Blonde's Revenge - Perfect Agent")
        mission_locations.append("Complete: Maian SOS - Perfect Agent")
        mission_locations.append("Complete: WAR! - Perfect Agent")
        mission_locations.append("Complete: The Duel - Perfect Agent")

    for location in mission_locations:
        world.get_location(location).place_locked_item(world.create_item("Mission Star"))

def set_challenge_stars(world: PerfectDarkWorld) -> None:
    for x in range(1, 31):
        challenge_name = f"Challenge {x}"
        if (world.options.excluded_challenges.__contains__(challenge_name) == False):
            challenge_location = f"Complete: Challenge {x}"
            world.get_location(challenge_location).place_locked_item(world.create_item("Challenge Star"))

def has_challenges(world: PerfectDarkWorld) -> bool:
    if (world.options.challenges
        or (world.options.goal >= Goal.option_complete_challenges)
        or (world.options.goal == Goal.option_complete_skedar_ruins
            and (world.options.skedar_ruins_requirements.value >= SkedarRuinsRequirements.option_collect_challenge_stars))):
        return True
    else:
        return False