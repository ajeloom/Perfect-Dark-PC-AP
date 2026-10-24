from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import (
    Goal, 
    SkedarRuinsRequirements, 
    MissionLogic, 
    MissionsInItemPool, 
    WeaponProgression, 
    ChallengeLogic,
)

from .rules import (
    PROGRESSIVE_WEAPON_NAME_TO_ID, 
    PROGRESSIVE_PISTOL_NAME_TO_ID, 
    PROGRESSIVE_SMG_NAME_TO_ID, 
    PROGRESSIVE_RIFLE_NAME_TO_ID, 
    PROGRESSIVE_EXPLOSIVE_NAME_TO_ID,
    PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID,
    has_challenges,
)

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
	# "WEAPON_BRIEFCASE": 79,
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
    # "Trap": 236,
    "Victory": 240,
    "Progressive Pistol": 241,
    "Progressive SMG": 242,
    "Progressive Rifle": 243,
    "Progressive Explosive": 244,
    "Progressive Other Weapon": 245,
    "Carrington": 246,
    "Cassandra": 247,
    "Dr. Caroll": 248,
    "Jonathan": 249,
    "Elvis": 250,
    "President": 251,
    "DK Mode Trap": 252,
    "Small Jo Trap": 253,
    "Small Characters Trap": 254,
    "Slow Motion Trap": 255,
    "Enemy Rockets Trap": 256,
    "Perfect Darkness Trap": 257,
    "Fast Animations Trap": 258,
    "Skedar Trap": 259,
    "N-Bomb Trap": 260,
    "Ammo Refill": 261,
    "Shield Refill": 262,
    "Health Refill": 263,
    "Buddy": 264,
    "dD Defection": 265,
    "dD Investigation": 266,
    "dD Extraction": 267,
    "Carrington Villa": 268,
    "Chicago": 269,
    "G5 Building": 270,
    "A51 Infiltration": 271,
    "A51 Rescue": 272,
    "A51 Escape": 273,
    "Air Base": 274,
    "Air Force One": 275,
    "Crash Site": 276,
    "Pelagic II": 277,
    "Deep Sea": 278,
    "CI Defense": 279,
    "Attack Ship": 280,
    "Skedar Ruins": 281,
    "Mr. Blonde's Revenge": 282,
    "Maian SOS": 283,
    "WAR!": 284,
    "The Duel": 285,
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
	# "WEAPON_BRIEFCASE": ItemClassification.filler,
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
    # "Trap": ItemClassification.trap,
    "Victory": ItemClassification.progression | ItemClassification.useful,
    "Progressive Pistol": ItemClassification.progression | ItemClassification.useful,
    "Progressive SMG": ItemClassification.progression | ItemClassification.useful,
    "Progressive Rifle": ItemClassification.progression | ItemClassification.useful,
    "Progressive Explosive": ItemClassification.progression | ItemClassification.useful,
    "Progressive Other Weapon": ItemClassification.progression | ItemClassification.useful,
    "Carrington": ItemClassification.progression | ItemClassification.useful,
    "Cassandra": ItemClassification.progression | ItemClassification.useful,
    "Dr. Caroll": ItemClassification.progression | ItemClassification.useful,
    "Jonathan": ItemClassification.progression | ItemClassification.useful,
    "Elvis": ItemClassification.progression | ItemClassification.useful,
    "President": ItemClassification.progression | ItemClassification.useful,
    "DK Mode Trap": ItemClassification.trap,
    "Small Jo Trap": ItemClassification.trap,
    "Small Characters Trap": ItemClassification.trap,
    "Slow Motion Trap": ItemClassification.trap,
    "Enemy Rockets Trap": ItemClassification.trap,
    "Perfect Darkness Trap": ItemClassification.trap,
    "Fast Animations Trap": ItemClassification.trap,
    "Skedar Trap": ItemClassification.trap,
    "N-Bomb Trap": ItemClassification.trap,
    "Ammo Refill": ItemClassification.filler | ItemClassification.useful,
    "Shield Refill": ItemClassification.filler | ItemClassification.useful,
    "Health Refill": ItemClassification.filler | ItemClassification.useful,
    "Buddy": ItemClassification.filler | ItemClassification.useful,
    "dD Defection": ItemClassification.progression | ItemClassification.useful,
    "dD Investigation": ItemClassification.progression | ItemClassification.useful,
    "dD Extraction": ItemClassification.progression | ItemClassification.useful,
    "Carrington Villa": ItemClassification.progression | ItemClassification.useful,
    "Chicago": ItemClassification.progression | ItemClassification.useful,
    "G5 Building": ItemClassification.progression | ItemClassification.useful,
    "A51 Infiltration": ItemClassification.progression | ItemClassification.useful,
    "A51 Rescue": ItemClassification.progression | ItemClassification.useful,
    "A51 Escape": ItemClassification.progression | ItemClassification.useful,
    "Air Base": ItemClassification.progression | ItemClassification.useful,
    "Air Force One": ItemClassification.progression | ItemClassification.useful,
    "Crash Site": ItemClassification.progression | ItemClassification.useful,
    "Pelagic II": ItemClassification.progression | ItemClassification.useful,
    "Deep Sea": ItemClassification.progression | ItemClassification.useful,
    "CI Defense": ItemClassification.progression | ItemClassification.useful,
    "Attack Ship": ItemClassification.progression | ItemClassification.useful,
    "Skedar Ruins": ItemClassification.progression | ItemClassification.useful,
    "Mr. Blonde's Revenge": ItemClassification.progression | ItemClassification.useful,
    "Maian SOS": ItemClassification.progression | ItemClassification.useful,
    "WAR!": ItemClassification.progression | ItemClassification.useful,
    "The Duel": ItemClassification.progression | ItemClassification.useful,
}

mission_list = []
challenge_list = []

FIRING_RANGE_LIST = [
    "Falcon 2",
    "Falcon 2 (Silencer)",
    "Falcon 2 (Scope)",
    "MagSec 4",
    "Mauler",
    "Phoenix",
    "DY357 Magnum",
    "DY357-LX",
    "CMP150",
    "Cyclone",
    "Callisto NTG",
    "RC-P120",
    "Laptop Gun",
    "Dragon",
    "K7 Avenger",
    "AR34",
    "SuperDragon",
    "Shotgun",
    "Reaper",
    "Sniper Rifle",
    "FarSight XR-20",
    "Devastator",
    "Rocket Launcher",
    "Slayer",
    "Combat Knife",
    "Crossbow",
    "Tranquilizer",
    "Laser",
    "Grenade",
    "Timed Mine",
    "Proximity Mine",
    "Remote Mine",
]


class PerfectDarkItem(Item):
    game = "Perfect Dark"


def get_random_filler_item_name(world: PerfectDarkWorld) -> str:
    filler = [
        "Ammo Refill",
        "Shield Refill",
        "Health Refill",
        "Buddy",
    ]

    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        filler.append("Cheese")

    if world.random.randint(0, 99) < world.options.trap_chance:
        traps = [
            "DK Mode Trap",
            "Small Jo Trap",
            "Small Characters Trap",
            "Slow Motion Trap",
            "Enemy Rockets Trap",
            "Perfect Darkness Trap",
            "Fast Animations Trap",
            "Skedar Trap",
            "N-Bomb Trap",
        ]

        available_traps = [
            trap for trap in traps
            if trap not in world.options.excluded_traps
        ]

        if available_traps:
            return world.random.choice(available_traps)
        else:
            return world.random.choice(filler)

    return world.random.choice(filler)


def create_item_with_correct_classification(world: PerfectDarkWorld, name: str) -> PerfectDarkItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if world.options.mission_logic >= MissionLogic.option_veteran \
            and world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent \
            and name == "President Scanner":
        classification = ItemClassification.useful

    if world.options.mission_logic >= MissionLogic.option_hard \
            and not world.options.device_training \
            and not world.options.perfect_agent \
            and not world.options.pickupsanity \
            and name == "Night Vision":
        classification = ItemClassification.useful

    if world.options.mission_logic >= MissionLogic.option_hard \
            and not world.options.device_training \
            and name == "IR Scanner":
        classification = ItemClassification.useful

    if (((has_challenges(world) and world.options.challenge_logic.value <= ChallengeLogic.option_normal)
            or world.options.pickupsanity)
            and name == "Shield"):
        classification = ItemClassification.progression | ItemClassification.useful

    if ((world.options.mission_logic.value == MissionLogic.option_veteran 
            or world.options.mission_logic.value == MissionLogic.option_hard)
            and world.options.weapon_progression.value == WeaponProgression.option_normal):
        if name == "Air Force One Left Room Key Card" or name == "Air Force One Right Room Key Card":
            classification = ItemClassification.progression | ItemClassification.useful

    if world.options.pickupsanity \
            and (name == "Air Force One Left Room Key Card" 
            or name == "Air Force One Right Room Key Card" 
            or name == "Cassandra's Office Key Card" 
            or name == "Psychosis Gun"):
        classification = ItemClassification.progression | ItemClassification.useful

    if has_challenges(world) \
            and world.options.challenge_logic.value == ChallengeLogic.option_strict \
            and name == "Combat Boost":
        classification = ItemClassification.progression | ItemClassification.useful

    if (has_challenges(world) and world.options.challenge_logic.value == ChallengeLogic.option_hard) \
            and not (world.options.pickupsanity and world.options.agent) \
            and not world.options.device_training \
            and not world.options.special_agent \
            and not world.options.perfect_agent \
            and world.options.mission_logic.value >= MissionLogic.option_hard \
            and name == "Cloaking Device":
        classification = ItemClassification.useful

    if world.options.goal.value == Goal.option_cheese_hunt \
            and name == "Cheese":
        classification = ItemClassification.progression | ItemClassification.useful

    return PerfectDarkItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world:PerfectDarkWorld) -> None:
    itempool: list[Item] = []
    
    # Create items needed for missions
    if has_any_difficulty(world):
        itempool.append(world.create_item("Horizon Scanner"))
        itempool.append(world.create_item("President Scanner"))
        itempool.append(world.create_item("Alien Medpack"))
        itempool.append(world.create_item("Explosives"))
        itempool.append(world.create_item("Lab Clothes"))
        itempool.append(world.create_item("Backup Disk"))
        itempool.append(world.create_item("Cellar Key Card"))
        itempool.append(world.create_item("Suitcase"))
        
    if has_challenges(world) or has_any_difficulty(world):
        itempool.append(world.create_item("Combat Boost"))

    if has_challenges(world) \
            or world.options.device_training \
            or world.options.pickupsanity \
            or has_any_difficulty(world):
        itempool.append(world.create_item("Cloaking Device"))

    if has_challenges(world) \
            or world.options.device_training \
            or has_any_difficulty(world):
        itempool.append(world.create_item("Data Uplink"))

    if world.options.device_training \
            or world.options.pickupsanity \
            or has_any_difficulty(world):
        itempool.append(world.create_item("Night Vision"))
        itempool.append(world.create_item("CamSpy"))
        itempool.append(world.create_item("Stewardess Disguise"))

    if world.options.device_training \
            or has_any_difficulty(world):
        itempool.append(world.create_item("X-Ray Scanner"))
        itempool.append(world.create_item("Door Decoder"))

    if world.options.perfect_agent:
        itempool.append(world.create_item("Tracer Bug"))
        itempool.append(world.create_item("Flight Plans"))
        itempool.append(world.create_item("Research Tape"))
        itempool.append(world.create_item("Shield Tech Item"))

    # Items in both Special and Perfect Agent
    if world.options.special_agent or world.options.perfect_agent:
        itempool.append(world.create_item("Skedar Bomb"))

    if world.options.pickupsanity \
            or world.options.special_agent \
            or world.options.perfect_agent:
        itempool.append(world.create_item("Comms Rider"))

    # Create ECM Mine
    if world.options.device_training \
            or world.options.special_agent \
            or world.options.perfect_agent:
        itempool.append(world.create_item("ECM Mine"))

    if (has_challenges(world)):
        itempool.append(world.create_item("Briefcase"))

    # Shield
    if world.options.agent \
            or world.options.special_agent \
            or world.options.pickupsanity \
            or has_challenges(world):
        itempool.append(world.create_item("Shield"))

    # Create items needed to beat Skedar Ruins
    if world.options.device_training \
            or world.options.pickupsanity \
            or has_any_difficulty(world) \
            or world.options.goal.value == Goal.option_complete_skedar_ruins:
        itempool.append(world.create_item("IR Scanner"))
        itempool.append(world.create_item("R-Tracker"))

    if world.options.pickupsanity \
            or has_any_difficulty(world) \
            or world.options.goal.value == Goal.option_complete_skedar_ruins:
        itempool.append(world.create_item("Target Amplifier"))


    # Create key cards
    if world.options.master_key:
        if world.options.special_agent \
                or world.options.perfect_agent \
                or world.options.pickupsanity:
            itempool.append(world.create_item("dataDyne Master Key"))

        if has_any_difficulty(world):
            itempool.append(world.create_item("Area 51 Master Key"))

        if has_any_difficulty(world) \
                or world.options.pickupsanity:
            itempool.append(world.create_item("G5 Building Master Key"))
            itempool.append(world.create_item("Air Force One Master Key"))

    else:
        if world.options.pickupsanity:
            itempool.append(world.create_item("Cassandra's Office Key Card"))

        if has_any_difficulty(world):
            itempool.append(world.create_item("Medlab 2 Key Card"))
            itempool.append(world.create_item("Op Room Key Card"))
            itempool.append(world.create_item("Area 51 Lift Key Card"))


        if world.options.pickupsanity \
                or world.options.special_agent \
                or world.options.perfect_agent:
            itempool.append(world.create_item("De Vries' Necklace"))

        if has_any_difficulty(world) \
                or world.options.pickupsanity:
            itempool.append(world.create_item("G5 Building Level 1 Key Card"))
            itempool.append(world.create_item("G5 Building Level 2 Key Card"))
            itempool.append(world.create_item("Air Force One Left Room Key Card"))
            itempool.append(world.create_item("Air Force One Right Room Key Card"))

        if world.options.special_agent \
                or world.options.perfect_agent:
            itempool.append(world.create_item("Air Force One Lift Key Card"))


    # Create NPCs
    if world.options.npcs:
        itempool.append(world.create_item("Carrington"))
        itempool.append(world.create_item("Cassandra"))
        itempool.append(world.create_item("Dr. Caroll"))
        itempool.append(world.create_item("Jonathan"))
        itempool.append(world.create_item("Elvis"))
        itempool.append(world.create_item("President"))


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

    # Missions 
    if world.options.missions_in_item_pool.value == MissionsInItemPool.option_enabled:
        if has_any_difficulty(world) \
                or world.options.pickupsanity:
            add_mission(world, "dD Defection", itempool)
            add_mission(world, "dD Investigation", itempool)
            add_mission(world, "dD Extraction", itempool)
            add_mission(world, "Carrington Villa", itempool)
            add_mission(world, "Chicago", itempool)
            add_mission(world, "G5 Building", itempool)
            add_mission(world, "A51 Infiltration", itempool)
            add_mission(world, "A51 Rescue", itempool)
            add_mission(world, "A51 Escape", itempool)
            add_mission(world, "Air Base", itempool)
            add_mission(world, "Air Force One", itempool)
            add_mission(world, "Crash Site", itempool)
            add_mission(world, "Pelagic II", itempool)
            add_mission(world, "Deep Sea", itempool)
            add_mission(world, "CI Defense", itempool)
            add_mission(world, "Attack Ship", itempool)
            add_mission(world, "Mr. Blonde's Revenge", itempool)
            add_mission(world, "Maian SOS", itempool)

            if has_any_difficulty(world):
                add_mission(world, "WAR!", itempool)
                add_mission(world, "The Duel", itempool)

        if (is_skedar_ruins_in_itempool(world)):
            add_mission(world, "Skedar Ruins", itempool)

    elif world.options.missions_in_item_pool.value == MissionsInItemPool.option_enabled_per_difficulty:
        if world.options.agent \
                or world.options.pickupsanity:
            add_mission(world, "dD Defection - Agent", itempool)
            add_mission(world, "dD Investigation - Agent", itempool)
            add_mission(world, "dD Extraction - Agent", itempool)
            add_mission(world, "Carrington Villa - Agent", itempool)
            add_mission(world, "Chicago - Agent", itempool)
            add_mission(world, "G5 Building - Agent", itempool)
            add_mission(world, "A51 Infiltration - Agent", itempool)
            add_mission(world, "A51 Rescue - Agent", itempool)
            add_mission(world, "A51 Escape - Agent", itempool)
            add_mission(world, "Air Base - Agent", itempool)
            add_mission(world, "Air Force One - Agent", itempool)
            add_mission(world, "Crash Site - Agent", itempool)
            add_mission(world, "Pelagic II - Agent", itempool)
            add_mission(world, "Deep Sea - Agent", itempool)
            add_mission(world, "CI Defense - Agent", itempool)
            add_mission(world, "Attack Ship - Agent", itempool)
            add_mission(world, "Mr. Blonde's Revenge - Agent", itempool)
            add_mission(world, "Maian SOS - Agent", itempool)

            if world.options.agent:
                add_mission(world, "WAR! - Agent", itempool)
                add_mission(world, "The Duel - Agent", itempool)

            if (is_skedar_ruins_in_itempool(world)):
                add_mission(world, "Skedar Ruins - Agent", itempool)

        if world.options.special_agent \
                or world.options.pickupsanity:
            add_mission(world, "dD Defection - Special Agent", itempool)
            add_mission(world, "dD Investigation - Special Agent", itempool)
            add_mission(world, "dD Extraction - Special Agent", itempool)
            add_mission(world, "Carrington Villa - Special Agent", itempool)
            add_mission(world, "Chicago - Special Agent", itempool)
            add_mission(world, "G5 Building - Special Agent", itempool)
            add_mission(world, "A51 Infiltration - Special Agent", itempool)
            add_mission(world, "A51 Rescue - Special Agent", itempool)
            add_mission(world, "A51 Escape - Special Agent", itempool)
            add_mission(world, "Air Base - Special Agent", itempool)
            add_mission(world, "Air Force One - Special Agent", itempool)
            add_mission(world, "Crash Site - Special Agent", itempool)
            add_mission(world, "Pelagic II - Special Agent", itempool)
            add_mission(world, "Deep Sea - Special Agent", itempool)
            add_mission(world, "CI Defense - Special Agent", itempool)
            add_mission(world, "Attack Ship - Special Agent", itempool)
            add_mission(world, "Mr. Blonde's Revenge - Special Agent", itempool)
            add_mission(world, "Maian SOS - Special Agent", itempool)

            if world.options.special_agent:
                add_mission(world, "WAR! - Special Agent", itempool)
                add_mission(world, "The Duel - Special Agent", itempool)
    
            if (is_skedar_ruins_in_itempool(world)):
                add_mission(world, "Skedar Ruins - Special Agent", itempool)

        if world.options.perfect_agent \
                or world.options.pickupsanity:
            add_mission(world, "dD Defection - Perfect Agent", itempool)
            add_mission(world, "dD Investigation - Perfect Agent", itempool)
            add_mission(world, "dD Extraction - Perfect Agent", itempool)
            add_mission(world, "Carrington Villa - Perfect Agent", itempool)
            add_mission(world, "Chicago - Perfect Agent", itempool)
            add_mission(world, "G5 Building - Perfect Agent", itempool)
            add_mission(world, "A51 Infiltration - Perfect Agent", itempool)
            add_mission(world, "A51 Rescue - Perfect Agent", itempool)
            add_mission(world, "A51 Escape - Perfect Agent", itempool)
            add_mission(world, "Air Base - Perfect Agent", itempool)
            add_mission(world, "Air Force One - Perfect Agent", itempool)
            add_mission(world, "Crash Site - Perfect Agent", itempool)
            add_mission(world, "Pelagic II - Perfect Agent", itempool)
            add_mission(world, "Deep Sea - Perfect Agent", itempool)
            add_mission(world, "CI Defense - Perfect Agent", itempool)
            add_mission(world, "Attack Ship - Perfect Agent", itempool)
            add_mission(world, "Mr. Blonde's Revenge - Perfect Agent", itempool)
            add_mission(world, "Maian SOS - Perfect Agent", itempool)

            if world.options.perfect_agent:
                add_mission(world, "WAR! - Perfect Agent", itempool)
                add_mission(world, "The Duel - Perfect Agent", itempool)
    
            if (is_skedar_ruins_in_itempool(world)):
                add_mission(world, "Skedar Ruins - Perfect Agent", itempool)

        if (is_skedar_ruins_in_itempool(world) 
                and not has_any_difficulty(world)
                and not world.options.pickupsanity):
            add_mission(world, "Skedar Ruins - Agent", itempool)
            add_mission(world, "Skedar Ruins - Special Agent", itempool)
            add_mission(world, "Skedar Ruins - Perfect Agent", itempool)


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
    if has_challenges(world):
        for x in range(1, 31):
            challenge_name = f"Challenge {x}"
            if (world.options.excluded_challenges.__contains__(challenge_name) == False):
                challenge_list.append(challenge_name)
                    
                if world.options.challenges_in_item_pool:
                    itempool.append(world.create_item(challenge_name))


    # Place items based on the goal
    if world.options.goal.value == Goal.option_complete_skedar_ruins:
        if world.options.agent:
            world.get_location("Complete: Skedar Ruins - Agent").place_locked_item(world.create_item("Victory"))
        if world.options.special_agent:
            world.get_location("Complete: Skedar Ruins - Special Agent").place_locked_item(world.create_item("Victory"))
        if world.options.perfect_agent:
            world.get_location("Complete: Skedar Ruins - Perfect Agent").place_locked_item(world.create_item("Victory"))

        if not has_any_difficulty(world):
            world.get_location("Complete: Skedar Ruins - Agent").place_locked_item(world.create_item("Victory"))
            world.get_location("Complete: Skedar Ruins - Special Agent").place_locked_item(world.create_item("Victory"))
            world.get_location("Complete: Skedar Ruins - Perfect Agent").place_locked_item(world.create_item("Victory"))

        if world.options.skedar_ruins_requirements.value >= SkedarRuinsRequirements.option_complete_missions:
            world.get_location("Collect All Stars").place_locked_item(world.create_item("Skedar Ruins"))

    elif world.options.goal.value == Goal.option_cheese_hunt:
        for _ in range(world.options.cheese_total.value):
            itempool.append(world.create_item("Cheese"))


    option_list = []
    
    if has_any_difficulty(world) or world.options.pickupsanity:
        option_list.append("Missions")
    
    if world.options.weapon_training:
        option_list.append("Weapon Training")

    if has_challenges(world):
        option_list.append("Challenges")

    if world.options.starting_items and option_list:
        option = world.random.choice(option_list)

        # Mission
        if option == "Missions":
            if world.options.missions_in_item_pool.value == MissionsInItemPool.option_disabled:
                if world.options.weapon_progression.value <= WeaponProgression.option_all_guns:
                    starting_weapons_list = [
                        "Falcon 2",
                        "Falcon 2 (Silencer)",
                        "Falcon 2 (Scope)",
                        "Mauler",
                        "Phoenix",
                        # "Callisto NTG",
                        "Laptop Gun",
                        "AR34",
                        "Shotgun",
                        # "Sniper Rifle",
                        "Crossbow",
                    ]

                    if world.options.agent or world.options.special_agent \
                            or (world.options.pickupsanity and not has_any_difficulty(world)):
                        starting_weapons_list.append("Sniper Rifle")

                    weapon = world.random.choice(starting_weapons_list)
                    remove_starting_item_from_pool(world, weapon, itempool)

                elif (world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon
                        or world.options.weapon_progression.value == WeaponProgression.option_progressive_one_gun):
                    for _ in range(PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]):
                        remove_starting_item_from_pool(world, "Progressive Weapon", itempool)

                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_types:
                    progressive_types_list = [
                        "Progressive Pistol",
                        "Progressive SMG",
                        "Progressive Rifle",
                        "Progressive Explosive",
                        "Progressive Other Weapon"
                    ]

                    selected_types = world.random.sample(progressive_types_list, 2)

                    for weapon in selected_types:
                        if weapon == "Progressive Other Weapon":
                            for _ in range(4):
                                remove_starting_item_from_pool(world, "Progressive Other Weapon", itempool)
                        else:
                            remove_starting_item_from_pool(world, weapon, itempool)

            elif world.options.missions_in_item_pool.value >= MissionsInItemPool.option_enabled:
                mission = world.random.choice(mission_list)
                # print(f"Picked {mission} to start with")
                remove_starting_item_from_pool(world, mission, itempool)

                if world.options.weapon_progression.value <= WeaponProgression.option_all_guns:
                    # Weapon for mission
                    if any(name in mission for name in 
                            ("dD Defection", 
                            "G5 Building",
                            "A51 Rescue")):
                        remove_starting_item_from_pool(world, "Falcon 2 (Silencer)", itempool)

                    elif any(name in mission for name in 
                            ("dD Investigation", 
                            "A51 Infiltration",
                            "Maian SOS")):
                        remove_starting_item_from_pool(world, "Falcon 2", itempool)

                    elif any(name in mission for name in 
                            ("dD Extraction", 
                            "Chicago",
                            "A51 Escape",
                            "Crash Site",
                            "The Duel")):
                        remove_starting_item_from_pool(world, "Falcon 2 (Scope)", itempool)

                    elif any(name in mission for name in 
                            ("Carrington Villa - Agent", 
                            "Carrington Villa - Special Agent")):
                        remove_starting_item_from_pool(world, "Sniper Rifle", itempool)

                    elif any(name in mission for name in 
                            ("Carrington Villa - Perfect Agent",
                            "Air Force One")):
                        remove_starting_item_from_pool(world, "Laptop Gun", itempool)

                    elif "Carrington Villa" in mission:
                        weapons = []

                        if world.options.agent or world.options.special_agent:
                            weapons.append("Sniper Rifle")

                        if world.options.perfect_agent:
                            weapons.append("Laptop Gun")

                        if world.options.pickupsanity and not has_any_difficulty(world):
                            weapons.append("Sniper Rifle")
                            weapons.append("Laptop Gun")

                        item = world.random.choice(weapons)
                        remove_starting_item_from_pool(world, item, itempool)

                    elif "Air Base" in mission:
                        remove_starting_item_from_pool(world, "Crossbow", itempool)

                    elif "Pelagic II" in mission:
                        weapons = [
                            "Falcon 2 (Silencer)",
                            "Laptop Gun"
                        ]

                        item = world.random.choice(weapons)
                        remove_starting_item_from_pool(world, item, itempool)

                    elif "Deep Sea" in mission:
                        weapons = [
                            "Falcon 2 (Scope)",
                            "Shotgun"
                        ]

                        item = world.random.choice(weapons)
                        remove_starting_item_from_pool(world, item, itempool)

                    elif "CI Defense" in mission:
                        remove_starting_item_from_pool(world, "AR34", itempool)

                    elif "Attack Ship" in mission:
                        if world.options.mission_logic.value <= MissionLogic.option_hard:
                            remove_starting_item_from_pool(world, "Combat Knife", itempool)

                        remove_starting_item_from_pool(world, "Mauler", itempool)

                    elif "Skedar Ruins" in mission:
                        weapons = [
                            "Falcon 2 (Scope)",
                            "Callisto NTG"
                        ]

                        item = world.random.choice(weapons)
                        remove_starting_item_from_pool(world, item, itempool)

                    elif "Mr. Blonde's Revenge" in mission:
                        remove_starting_item_from_pool(world, "Mauler", itempool)

                    elif "WAR!" in mission:
                        remove_starting_item_from_pool(world, "Phoenix", itempool)


                elif (world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon
                        or world.options.weapon_progression.value == WeaponProgression.option_progressive_one_gun):
                    count = 0

                    if "Carrington Villa" in mission:
                        count = PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]

                    elif any(name in mission for name in 
                            ("G5 Building",
                            "A51 Infiltration",
                            "A51 Rescue",
                            "A51 Escape",
                            "Air Base",
                            "Air Force One",
                            "Crash Site",
                            "Pelagic II",
                            "Mr. Blonde's Revenge",
                            "Maian SOS")):
                        count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]

                    elif any(name in mission for name in 
                            ("Deep Sea",
                            "Attack Ship",
                            "Skedar Ruins",
                            "WAR!")):
                        count = PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]

                    elif "CI Defense" in mission:
                        count = PROGRESSIVE_WEAPON_NAME_TO_ID["DMC"]

                    else:
                        count = PROGRESSIVE_WEAPON_NAME_TO_ID["KL01313"]

                    for _ in range(count):
                        remove_starting_item_from_pool(world, "Progressive Weapon", itempool)


                elif world.options.weapon_progression.value == WeaponProgression.option_progressive_types:
                    progressive_types_list = [
                        "Progressive Pistol",
                        "Progressive SMG",
                        "Progressive Rifle",
                        "Progressive Explosive",
                        "Progressive Other Weapon"
                    ]

                    selected_types = world.random.sample(progressive_types_list, 2)

                    for weapon in selected_types:
                        if weapon == "Progressive Other Weapon":
                            for _ in range(4):
                                remove_starting_item_from_pool(world, "Progressive Other Weapon", itempool)
                        else:
                            remove_starting_item_from_pool(world, weapon, itempool)


        # Weapon Training
        elif option == "Weapon Training":
            if world.options.weapon_progression.value <= WeaponProgression.option_all_guns:
                weapon1, weapon2 = world.random.sample(FIRING_RANGE_LIST, 2)
                remove_starting_item_from_pool(world, weapon1, itempool)
                remove_starting_item_from_pool(world, weapon2, itempool)

            elif (world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon
                    or world.options.weapon_progression.value == WeaponProgression.option_progressive_one_gun):
                for _ in range(3):
                    remove_starting_item_from_pool(world, "Progressive Weapon", itempool)

            elif world.options.weapon_progression.value == WeaponProgression.option_progressive_types:
                progressive_types_list = [
                    "Progressive Pistol",
                    # "Progressive SMG",
                    "Progressive Rifle",
                    "Progressive Explosive",
                    "Progressive Other Weapon",
                ]
                weapon = world.random.choice(progressive_types_list)

                if weapon in ("Progressive Pistol", "Progressive Rifle"):
                    remove_starting_item_from_pool(world, weapon, itempool)
                    remove_starting_item_from_pool(world, weapon, itempool)
                else:
                    remove_starting_item_from_pool(world, weapon, itempool)


        # Challenges
        elif option == "Challenges":
            challenge = world.random.choice(challenge_list)

            if world.options.challenges_in_item_pool:
                remove_starting_item_from_pool(world, challenge, itempool)

            challenge_weapons_list = {
                "Challenge 1": ["Falcon 2", "CMP150", "Sniper Rifle", "DY357 Magnum", "Dragon"],

                "Challenge 2": ["Combat Knife", "Falcon 2", "Cyclone", "Dragon", "Rocket Launcher"],

                "Challenge 3": ["MagSec 4", "CMP150", "Timed Mine", "Dragon", "AR34"],

                "Challenge 4": ["MagSec 4", "CMP150", "Dragon", "K7 Avenger"],

                "Challenge 5": ["Cyclone", "Grenade", "AR34", "FarSight XR-20"],

                "Challenge 6": ["CMP150", "DY357 Magnum", "Shotgun", "K7 Avenger"],

                "Challenge 7": ["Falcon 2 (Silencer)", "MagSec 4", "Cyclone", "Grenade"],

                "Challenge 8": ["MagSec 4", "K7 Avenger", "Shotgun", "SuperDragon"],

                "Challenge 9": ["Falcon 2", "DY357 Magnum", "Timed Mine", "Laptop Gun", "FarSight XR-20"],

                "Challenge 10": ["CMP150", "Cyclone", "Remote Mine", "AR34"],

                "Challenge 11": ["MagSec 4", "Tranquilizer", "Shotgun", "K7 Avenger"],

                "Challenge 12": ["Falcon 2 (Scope)", "Sniper Rifle", "Shotgun", "SuperDragon"],

                "Challenge 13": ["Falcon 2 (Silencer)", "Tranquilizer", "Laptop Gun", "Grenade", "Reaper"],

                "Challenge 14": ["Cyclone", "SuperDragon", "K7 Avenger", "FarSight XR-20"],

                "Challenge 15": ["MagSec 4", "Dragon", "Shotgun", "Devastator"],

                "Challenge 16": ["Falcon 2", "K7 Avenger", "SuperDragon", "Proximity Mine"],

                "Challenge 17": ["DY357 Magnum", "AR34", "Reaper", "Slayer"],

                "Challenge 18": ["Falcon 2", "Phoenix", "Tranquilizer", "Laptop Gun"],

                "Challenge 19": ["CMP150", "Shotgun", "Rocket Launcher", "FarSight XR-20"],

                "Challenge 20": ["Mauler", "Falcon 2", "MagSec 4", "DY357 Magnum"],

                "Challenge 21": ["Mauler", "Reaper", "Shotgun", "Callisto NTG"],

                "Challenge 22": ["Falcon 2", "Sniper Rifle", "Crossbow", "K7 Avenger"],

                "Challenge 23": ["MagSec 4", "Grenade", "Laptop Gun", "RC-P120"],

                "Challenge 24": ["CMP150", "Tranquilizer", "Devastator", "SuperDragon", "DY357-LX"],

                "Challenge 25": ["Mauler", "N-Bomb", "K7 Avenger", "FarSight XR-20"],

                "Challenge 26": ["Falcon 2", "Mauler", "Cyclone", "Laptop Gun", "Reaper"],

                "Challenge 27": ["Falcon 2", "MagSec 4", "CMP150", "Rocket Launcher"],

                "Challenge 28": ["Falcon 2", "Falcon 2 (Silencer)", "DY357 Magnum", "AR34", "Shotgun"],

                "Challenge 29": ["Falcon 2", "Cyclone", "DY357 Magnum", "CMP150", "Dragon"],

                "Challenge 30": ["Falcon 2", "Falcon 2 (Scope)", "MagSec 4", "Mauler", "DY357 Magnum"]
            }

            if challenge in [f"Challenge {i}" for i in range(1, 31)]:
                get_challenge_items(world, challenge_weapons_list[challenge], itempool, challenge)


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
            or world.options.goal.value == Goal.option_cheese_hunt):
        return True
    else:
        return False


def has_any_difficulty(world: PerfectDarkWorld) -> bool:
    if (world.options.agent or world.options.special_agent or world.options.perfect_agent):
        return True

    return False


def add_mission(world:PerfectDarkWorld, item:str, itempool:list[Item]) -> None:
    itempool.append(world.create_item(item))
    # print(f"Adding mission {item} to mission_list")
    mission_list.append(item)


def get_challenge_items(world:PerfectDarkWorld, weaponlist:list[str], itempool:list[Item], challenge:str) -> None:

    def remove_weaponset_from_pool():
        for weapon in weaponlist:
            remove_starting_item_from_pool(world, weapon, itempool)

    # Briefcase
    briefcase_list = [
        "Challenge 6",
        "Challenge 8",
        "Challenge 14",
        "Challenge 15",
        "Challenge 22",
        "Challenge 24",
        "Challenge 28",
    ]

    if challenge in briefcase_list:
        remove_starting_item_from_pool(world, "Briefcase", itempool)

    # Data Uplink
    data_uplink_list = [
        "Challenge 10",
        "Challenge 21",
        "Challenge 27",
    ]

    if challenge in data_uplink_list:
        remove_starting_item_from_pool(world, "Data Uplink", itempool)

    # Shield, Cloaking Device, Combat Boost
    if world.options.challenge_logic.value <= ChallengeLogic.option_normal:
        shield_list = [
            "Challenge 16",
            "Challenge 17",
            "Challenge 18",
            "Challenge 19",
            "Challenge 20",
            "Challenge 22",
            "Challenge 23",
            "Challenge 27",
        ]

        cloaking_device_list = [
            "Challenge 14",
            "Challenge 18",
            "Challenge 21",
            "Challenge 25",
        ]

        combat_boost_list = [
            "Challenge 19",
            "Challenge 23",
        ]

        if world.options.challenge_logic.value == ChallengeLogic.option_strict:
            shield_list.append("Challenge 4")
            shield_list.append("Challenge 5")
            shield_list.append("Challenge 6")
            shield_list.append("Challenge 7")
            shield_list.append("Challenge 8")
            shield_list.append("Challenge 10")
            shield_list.append("Challenge 11")
            shield_list.append("Challenge 12")
            shield_list.append("Challenge 15")

            if challenge in combat_boost_list:
                remove_starting_item_from_pool(world, "Combat Boost", itempool)

        if challenge in shield_list:
            remove_starting_item_from_pool(world, "Shield", itempool)

        if challenge in cloaking_device_list:
            remove_starting_item_from_pool(world, "Cloaking Device", itempool)

    # Weapons
    if world.options.weapon_progression.value <= WeaponProgression.option_all_guns:
        if world.options.challenge_logic.value == ChallengeLogic.option_strict:
            remove_weaponset_from_pool()
        elif world.options.challenge_logic.value == ChallengeLogic.option_normal:
            if challenge in [
                    "Challenge 1",
                    "Challenge 6",
                    "Challenge 7",
                    "Challenge 8",
                    "Challenge 10",
                    "Challenge 12",
                    "Challenge 14",
                ]:
                weapon = world.random.choice(weaponlist)
                remove_starting_item_from_pool(world, weapon, itempool)
            elif challenge == "Challenge 2":
                remove_starting_item_from_pool(world, "Rocket Launcher", itempool)
            elif challenge == "Challenge 3":
                remove_starting_item_from_pool(world, "Timed Mine", itempool)
                remove_starting_item_from_pool(world, "Dragon", itempool)
                remove_starting_item_from_pool(world, "AR34", itempool)
            elif challenge == "Challenge 4":
                remove_starting_item_from_pool(world, "K7 Avenger", itempool)
            elif challenge == "Challenge 5":
                remove_starting_item_from_pool(world, "FarSight XR-20", itempool)
            elif challenge == "Challenge 9":
                remove_starting_item_from_pool(world, "FarSight XR-20", itempool)
                remove_starting_item_from_pool(world, "Laptop Gun", itempool)
            elif challenge == "Challenge 11":
                remove_starting_item_from_pool(world, "Shotgun", itempool)
                remove_starting_item_from_pool(world, "Tranquilizer", itempool)
            elif challenge == "Challenge 13":
                remove_starting_item_from_pool(world, "Tranquilizer", itempool)
            elif challenge == "Challenge 15":
                remove_starting_item_from_pool(world, "Devastator", itempool)
            elif challenge in [
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
                ]:
                remove_weaponset_from_pool()       
        elif world.options.challenge_logic.value == ChallengeLogic.option_hard:
            weapon = world.random.choice(weaponlist)
            remove_starting_item_from_pool(world, weapon, itempool)
    
    elif (world.options.weapon_progression.value == WeaponProgression.option_progressive_weapon
            or world.options.weapon_progression.value == WeaponProgression.option_progressive_one_gun):
        count = 0

        if world.options.challenge_logic.value == ChallengeLogic.option_strict:
            if challenge == "Challenge 1":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Dragon"]
            elif challenge == "Challenge 2":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]
            elif challenge == "Challenge 3":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]
            elif challenge == "Challenge 4":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]
            elif challenge == "Challenge 5":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 6":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]
            elif challenge == "Challenge 7":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]
            elif challenge == "Challenge 8":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]
            elif challenge == "Challenge 9":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 10":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Remote Mine"]
            elif challenge == "Challenge 11":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]
            elif challenge == "Challenge 12":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]
            elif challenge == "Challenge 13":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Grenade"]
            elif challenge == "Challenge 14":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 15":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]
            elif challenge == "Challenge 16":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]
            elif challenge == "Challenge 17":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]
            elif challenge == "Challenge 18":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]
            elif challenge == "Challenge 19":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 20":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]
            elif challenge == "Challenge 21":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]
            elif challenge == "Challenge 22":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]
            elif challenge == "Challenge 23":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]
            elif challenge == "Challenge 24":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]
            elif challenge == "Challenge 25":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 26":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]
            elif challenge == "Challenge 27":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]
            elif challenge == "Challenge 28":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]
            elif challenge == "Challenge 29":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]
            elif challenge == "Challenge 30":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]

            for _ in range(count):
                remove_starting_item_from_pool(world, "Progressive Weapon", itempool)

        elif world.options.challenge_logic.value == ChallengeLogic.option_normal:
            if challenge == "Challenge 1":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]
            elif challenge == "Challenge 2":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]
            elif challenge == "Challenge 3":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Timed Mine"]
            elif challenge == "Challenge 4":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]
            elif challenge == "Challenge 5":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 6":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]
            elif challenge == "Challenge 7":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"]
            elif challenge == "Challenge 8":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]
            elif challenge == "Challenge 9":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 10":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"]
            elif challenge == "Challenge 11":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]
            elif challenge == "Challenge 12":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]
            elif challenge == "Challenge 13":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]
            elif challenge == "Challenge 14":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]
            elif challenge == "Challenge 15":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Devastator"]
            elif challenge == "Challenge 16":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["SuperDragon"]
            elif challenge == "Challenge 17":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Slayer"]
            elif challenge == "Challenge 18":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Phoenix"]
            elif challenge == "Challenge 19":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 20":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]
            elif challenge == "Challenge 21":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]
            elif challenge == "Challenge 22":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["K7 Avenger"]
            elif challenge == "Challenge 23":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["RC-P120"]
            elif challenge == "Challenge 24":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["DY357-LX"]
            elif challenge == "Challenge 25":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["FarSight XR-20"]
            elif challenge == "Challenge 26":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]
            elif challenge == "Challenge 27":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Rocket Launcher"]
            elif challenge == "Challenge 28":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]
            elif challenge == "Challenge 29":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]
            elif challenge == "Challenge 30":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Mauler"]

            for _ in range(count):
                remove_starting_item_from_pool(world, "Progressive Weapon", itempool)
                
        elif world.options.challenge_logic.value == ChallengeLogic.option_hard:
            if challenge == "Challenge 1":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]
            elif challenge == "Challenge 2":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Combat Knife"]
            elif challenge == "Challenge 3":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]
            elif challenge == "Challenge 4":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]
            elif challenge == "Challenge 5":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["AR34"]
            elif challenge == "Challenge 6":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]
            elif challenge == "Challenge 7":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2 (Silencer)"]
            elif challenge == "Challenge 8":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]
            elif challenge == "Challenge 9":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 10":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["CMP150"]
            elif challenge == "Challenge 11":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]
            elif challenge == "Challenge 12":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Sniper Rifle"]
            elif challenge == "Challenge 13":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]
            elif challenge == "Challenge 14":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Cyclone"]
            elif challenge == "Challenge 15":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]
            elif challenge == "Challenge 16":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 17":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["DY357 Magnum"]
            elif challenge == "Challenge 18":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]
            elif challenge == "Challenge 19":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]
            elif challenge == "Challenge 20":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 21":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Shotgun"]
            elif challenge == "Challenge 22":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Crossbow"]
            elif challenge == "Challenge 23":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["MagSec 4"]
            elif challenge == "Challenge 24":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Tranquilizer"]
            elif challenge == "Challenge 25":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["N-Bomb"]
            elif challenge == "Challenge 26":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 27":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 28":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 29":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]
            elif challenge == "Challenge 30":
                count = PROGRESSIVE_WEAPON_NAME_TO_ID["Falcon 2"]

            for _ in range(count):
                remove_starting_item_from_pool(world, "Progressive Weapon", itempool)
    
    elif world.options.weapon_progression.value == WeaponProgression.option_progressive_types:
        pistol_count = 0
        smg_count = 0
        rifle_count = 0
        explosive_count = 0
        other_weapon_count = 0

        def give_types() -> None:
            for _ in range(pistol_count):
                remove_starting_item_from_pool(world, "Progressive Pistol", itempool)

            for _ in range(smg_count):
                remove_starting_item_from_pool(world, "Progressive SMG", itempool)

            for _ in range(rifle_count):
                remove_starting_item_from_pool(world, "Progressive Rifle", itempool)

            for _ in range(explosive_count):
                remove_starting_item_from_pool(world, "Progressive Explosive", itempool)

            for _ in range(other_weapon_count):
                remove_starting_item_from_pool(world, "Progressive Other Weapon", itempool)

        def select_one_type() -> None:
            weapon_list = []
            
            if pistol_count > 0:
                weapon_list.append("Progressive Pistol")

            if smg_count > 0:
                weapon_list.append("Progressive SMG")

            if rifle_count > 0:
                weapon_list.append("Progressive Rifle")

            if explosive_count > 0:
                weapon_list.append("Progressive Explosive")

            if other_weapon_count > 0:
                weapon_list.append("Progressive Other Weapon")

            weapon = world.random.choice(weapon_list)
            
            count = 0

            if weapon == "Progressive Pistol":
                count = pistol_count
            elif weapon == "Progressive SMG":
                count = smg_count
            elif weapon == "Progressive Rifle":
                count = rifle_count
            elif weapon == "Progressive Explosive":
                count = explosive_count
            elif weapon == "Progressive Other Weapon":
                count = other_weapon_count

            for _ in range(count):
                remove_starting_item_from_pool(world, weapon, itempool)
        
        if world.options.challenge_logic.value == ChallengeLogic.option_strict:
            if challenge == "Challenge 1":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]

            elif challenge == "Challenge 2":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Combat Knife"]

            elif challenge == "Challenge 3":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]

            elif challenge == "Challenge 4":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]

            elif challenge == "Challenge 5":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 6":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 7":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]

            elif challenge == "Challenge 8":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 9":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 10":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]

            elif challenge == "Challenge 11":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 12":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 13":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]

            elif challenge == "Challenge 14":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 15":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 16":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]

            elif challenge == "Challenge 17":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]

            elif challenge == "Challenge 18":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]

            elif challenge == "Challenge 19":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 20":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]

            elif challenge == "Challenge 21":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Callisto NTG"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]

            elif challenge == "Challenge 22":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]

            elif challenge == "Challenge 23":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]

            elif challenge == "Challenge 24":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]

            elif challenge == "Challenge 25":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["N-Bomb"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 26":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]

            elif challenge == "Challenge 27":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]

            elif challenge == "Challenge 28":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 29":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]

            elif challenge == "Challenge 30":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]

            give_types()

        elif world.options.challenge_logic.value == ChallengeLogic.option_normal:
            if challenge == "Challenge 1":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]
                select_one_type()

            elif challenge == "Challenge 2":
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                give_types()

            elif challenge == "Challenge 3":
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]
                give_types()

            elif challenge == "Challenge 4":
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                give_types()

            elif challenge == "Challenge 5":
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]
                give_types()

            elif challenge == "Challenge 6":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]
                select_one_type()

            elif challenge == "Challenge 7":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]
                select_one_type()

            elif challenge == "Challenge 8":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]
                select_one_type()

            elif challenge == "Challenge 9":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]
                give_types()

            elif challenge == "Challenge 10":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]
                select_one_type()

            elif challenge == "Challenge 11":
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]
                give_types()

            elif challenge == "Challenge 12":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                select_one_type()

            elif challenge == "Challenge 13":
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]
                give_types()

            elif challenge == "Challenge 14":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]
                select_one_type()

            elif challenge == "Challenge 15":
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]
                give_types()

            elif challenge == "Challenge 16":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]
                give_types()

            elif challenge == "Challenge 17":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]
                give_types()

            elif challenge == "Challenge 18":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Phoenix"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]
                give_types()

            elif challenge == "Challenge 19":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]
                give_types()

            elif challenge == "Challenge 20":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                give_types()

            elif challenge == "Challenge 21":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Callisto NTG"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]
                give_types()

            elif challenge == "Challenge 22":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]
                give_types()

            elif challenge == "Challenge 23":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["RC-P120"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]
                give_types()

            elif challenge == "Challenge 24":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]
                give_types()

            elif challenge == "Challenge 25":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["N-Bomb"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]
                give_types()

            elif challenge == "Challenge 26":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]
                give_types()

            elif challenge == "Challenge 27":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                give_types()

            elif challenge == "Challenge 28":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]
                give_types()

            elif challenge == "Challenge 29":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                give_types()

            elif challenge == "Challenge 30":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                give_types()

        elif world.options.challenge_logic.value == ChallengeLogic.option_hard:
            if challenge == "Challenge 1":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]

            elif challenge == "Challenge 2":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Combat Knife"]

            elif challenge == "Challenge 3":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]

            elif challenge == "Challenge 4":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]

            elif challenge == "Challenge 5":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 6":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 7":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]

            elif challenge == "Challenge 8":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 9":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Timed Mine"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 10":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Remote Mine"]

            elif challenge == "Challenge 11":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]

            elif challenge == "Challenge 12":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Scope)"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Sniper Rifle"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]

            elif challenge == "Challenge 13":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2 (Silencer)"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]

            elif challenge == "Challenge 14":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 15":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 16":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Proximity Mine"]

            elif challenge == "Challenge 17":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357 Magnum"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Slayer"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]

            elif challenge == "Challenge 18":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]

            elif challenge == "Challenge 19":
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 20":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]

            elif challenge == "Challenge 21":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Callisto NTG"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 22":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Crossbow"]

            elif challenge == "Challenge 23":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["MagSec 4"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Laptop Gun"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Grenade"]

            elif challenge == "Challenge 24":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["DY357-LX"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["SuperDragon"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Devastator"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Tranquilizer"]

            elif challenge == "Challenge 25":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Mauler"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["K7 Avenger"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["N-Bomb"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["FarSight XR-20"]

            elif challenge == "Challenge 26":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["Cyclone"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Reaper"]

            elif challenge == "Challenge 27":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                explosive_count = PROGRESSIVE_EXPLOSIVE_NAME_TO_ID["Rocket Launcher"]

            elif challenge == "Challenge 28":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["AR34"]
                other_weapon_count = PROGRESSIVE_OTHER_WEAPON_NAME_TO_ID["Shotgun"]

            elif challenge == "Challenge 29":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]
                smg_count = PROGRESSIVE_SMG_NAME_TO_ID["CMP150"]
                rifle_count = PROGRESSIVE_RIFLE_NAME_TO_ID["Dragon"]

            elif challenge == "Challenge 30":
                pistol_count = PROGRESSIVE_PISTOL_NAME_TO_ID["Falcon 2"]

            select_one_type()
    