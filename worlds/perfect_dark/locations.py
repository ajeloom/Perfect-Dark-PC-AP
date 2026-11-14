from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, LocationProgressType

from . import items

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements, MissionLogic, WeaponProgression, AlternateExits
from .rules import has_challenges

FIRING_RANGE_WEAPONS = [
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
    "Remote Mine"
]

LOCATION_NAME_TO_ID = {
    "dD Defection - Agent Objective 1": 1,
    "dD Investigation - Agent Objective 1": 4,
	"dD Investigation - Agent Objective 2": 5,
    "dD Extraction - Agent Objective 1": 7,
	"dD Extraction - Agent Objective 2": 8,
	"dD Extraction - Agent Objective 3": 9,
    "Carrington Villa - Agent Objective 1": 10,
	"Carrington Villa - Agent Objective 2": 11,
	"Carrington Villa - Agent Objective 3": 12,
    "Chicago - Agent Objective 1": 13,
	"Chicago - Agent Objective 2": 14,
	"Chicago - Agent Objective 3": 15,
    "G5 Building - Agent Objective 1": 16,
	"G5 Building - Agent Objective 2": 17,
	"G5 Building - Agent Objective 3": 18,
    "A51 Infiltration - Agent Objective 1": 19,
	"A51 Infiltration - Agent Objective 2": 20,
	"A51 Infiltration - Agent Objective 3": 21,
    "A51 Rescue - Agent Objective 1": 22,
	"A51 Rescue - Agent Objective 2": 23,
	"A51 Rescue - Agent Objective 3": 24,
    "A51 Escape - Agent Objective 1": 25,
	"A51 Escape - Agent Objective 2": 26,
	"A51 Escape - Agent Objective 3": 27,
    "Air Base - Agent Objective 1": 28,
	"Air Base - Agent Objective 2": 29,
	"Air Base - Agent Objective 3": 30,
    "Air Force One - Agent Objective 1": 31,
	"Air Force One - Agent Objective 2": 32,
	"Air Force One - Agent Objective 3": 33,
    "Crash Site - Agent Objective 1": 34,
	"Crash Site - Agent Objective 2": 35,
	"Crash Site - Agent Objective 3": 36,
    "Pelagic II - Agent Objective 1": 37,
	"Pelagic II - Agent Objective 2": 38,
	"Pelagic II - Agent Objective 3": 39,
    "Deep Sea - Agent Objective 1": 40,
	"Deep Sea - Agent Objective 2": 41,
	"Deep Sea - Agent Objective 3": 42,
    "CI Defense - Agent Objective 1": 43,
	"CI Defense - Agent Objective 2": 44,
	"CI Defense - Agent Objective 3": 45,
    "Attack Ship - Agent Objective 1": 46,
	"Attack Ship - Agent Objective 2": 47,
	"Attack Ship - Agent Objective 3": 48,
    "Skedar Ruins - Agent Objective 1": 49,
	"Skedar Ruins - Agent Objective 2": 50,
	"Skedar Ruins - Agent Objective 3": 51,
    "Mr. Blonde's Revenge - Agent Objective 1": 52,
    "Maian SOS - Agent Objective 1": 55,
    "WAR! - Agent Objective 1": 58,
    "The Duel - Agent Objective 1": 61,
	"dD Defection - Special Agent Objective 1": 62,
	"dD Defection - Special Agent Objective 2": 63,
	"dD Defection - Special Agent Objective 3": 64,
	"dD Defection - Special Agent Objective 4": 65,
    "dD Investigation - Special Agent Objective 1": 66,
	"dD Investigation - Special Agent Objective 2": 67,
	"dD Investigation - Special Agent Objective 3": 68,
	"dD Investigation - Special Agent Objective 4": 69,
    "dD Extraction - Special Agent Objective 1": 70,
	"dD Extraction - Special Agent Objective 2": 71,
	"dD Extraction - Special Agent Objective 3": 72,
	"dD Extraction - Special Agent Objective 4": 73,
    "Carrington Villa - Special Agent Objective 1": 74,
	"Carrington Villa - Special Agent Objective 2": 75,
	"Carrington Villa - Special Agent Objective 3": 76,
	"Carrington Villa - Special Agent Objective 4": 77,
    "Chicago - Special Agent Objective 1": 78,
	"Chicago - Special Agent Objective 2": 79,
	"Chicago - Special Agent Objective 3": 80,
	"Chicago - Special Agent Objective 4": 81,
    "G5 Building - Special Agent Objective 1": 82,
	"G5 Building - Special Agent Objective 2": 83,
	"G5 Building - Special Agent Objective 3": 84,
	"G5 Building - Special Agent Objective 4": 85,
    "A51 Infiltration - Special Agent Objective 1": 86,
	"A51 Infiltration - Special Agent Objective 2": 87,
	"A51 Infiltration - Special Agent Objective 3": 88,
	"A51 Infiltration - Special Agent Objective 4": 89,
    "A51 Rescue - Special Agent Objective 1": 90,
	"A51 Rescue - Special Agent Objective 2": 91,
	"A51 Rescue - Special Agent Objective 3": 92,
	"A51 Rescue - Special Agent Objective 4": 93,
    "A51 Escape - Special Agent Objective 1": 94,
	"A51 Escape - Special Agent Objective 2": 95,
	"A51 Escape - Special Agent Objective 3": 96,
	"A51 Escape - Special Agent Objective 4": 97,
    "Air Base - Special Agent Objective 1": 98,
	"Air Base - Special Agent Objective 2": 99,
	"Air Base - Special Agent Objective 3": 100,
	"Air Base - Special Agent Objective 4": 101,
    "Air Force One - Special Agent Objective 1": 102,
	"Air Force One - Special Agent Objective 2": 103,
	"Air Force One - Special Agent Objective 3": 104,
	"Air Force One - Special Agent Objective 4": 105,
    "Crash Site - Special Agent Objective 1": 106,
	"Crash Site - Special Agent Objective 2": 107,
	"Crash Site - Special Agent Objective 3": 108,
	"Crash Site - Special Agent Objective 4": 109,
    "Pelagic II - Special Agent Objective 1": 110,
	"Pelagic II - Special Agent Objective 2": 111,
	"Pelagic II - Special Agent Objective 3": 112,
	"Pelagic II - Special Agent Objective 4": 113,
    "Deep Sea - Special Agent Objective 1": 114,
	"Deep Sea - Special Agent Objective 2": 115,
	"Deep Sea - Special Agent Objective 3": 116,
	"Deep Sea - Special Agent Objective 4": 117,
    "CI Defense - Special Agent Objective 1": 118,
	"CI Defense - Special Agent Objective 2": 119,
	"CI Defense - Special Agent Objective 3": 120,
	"CI Defense - Special Agent Objective 4": 121,
    "Attack Ship - Special Agent Objective 1": 122,
	"Attack Ship - Special Agent Objective 2": 123,
	"Attack Ship - Special Agent Objective 3": 124,
	"Attack Ship - Special Agent Objective 4": 125,
    "Skedar Ruins - Special Agent Objective 1": 126,
	"Skedar Ruins - Special Agent Objective 2": 127,
	"Skedar Ruins - Special Agent Objective 3": 128,
	"Skedar Ruins - Special Agent Objective 4": 129,
    "Mr. Blonde's Revenge - Special Agent Objective 1": 130,
	"Mr. Blonde's Revenge - Special Agent Objective 2": 131,
    "Maian SOS - Special Agent Objective 1": 134,
	"Maian SOS - Special Agent Objective 2": 135,
    "WAR! - Special Agent Objective 1": 138,
	"WAR! - Special Agent Objective 2": 139,
    "The Duel - Special Agent Objective 1": 142,
	"The Duel - Special Agent Objective 2": 143,
	"dD Defection - Perfect Agent Objective 1": 144,
	"dD Defection - Perfect Agent Objective 2": 145,
	"dD Defection - Perfect Agent Objective 3": 146,
	"dD Defection - Perfect Agent Objective 4": 147,
	"dD Defection - Perfect Agent Objective 5": 148,
	"dD Investigation - Perfect Agent Objective 1": 149,
	"dD Investigation - Perfect Agent Objective 2": 150,
	"dD Investigation - Perfect Agent Objective 3": 151,
	"dD Investigation - Perfect Agent Objective 4": 152,
	"dD Investigation - Perfect Agent Objective 5": 153,
	"dD Extraction - Perfect Agent Objective 1": 154,
	"dD Extraction - Perfect Agent Objective 2": 155,
	"dD Extraction - Perfect Agent Objective 3": 156,
	"dD Extraction - Perfect Agent Objective 4": 157,
	"dD Extraction - Perfect Agent Objective 5": 158,
	"Carrington Villa - Perfect Agent Objective 1": 159,
	"Carrington Villa - Perfect Agent Objective 2": 160,
	"Carrington Villa - Perfect Agent Objective 3": 161,
	"Carrington Villa - Perfect Agent Objective 4": 162,
	"Carrington Villa - Perfect Agent Objective 5": 163,
	"Chicago - Perfect Agent Objective 1": 164,
	"Chicago - Perfect Agent Objective 2": 165,
	"Chicago - Perfect Agent Objective 3": 166,
	"Chicago - Perfect Agent Objective 4": 167,
	"Chicago - Perfect Agent Objective 5": 168,
	"G5 Building - Perfect Agent Objective 1": 169,
	"G5 Building - Perfect Agent Objective 2": 170,
	"G5 Building - Perfect Agent Objective 3": 171,
	"G5 Building - Perfect Agent Objective 4": 172,
	"G5 Building - Perfect Agent Objective 5": 173,
	"A51 Infiltration - Perfect Agent Objective 1": 174,
	"A51 Infiltration - Perfect Agent Objective 2": 175,
	"A51 Infiltration - Perfect Agent Objective 3": 176,
	"A51 Infiltration - Perfect Agent Objective 4": 177,
	"A51 Infiltration - Perfect Agent Objective 5": 178,
	"A51 Rescue - Perfect Agent Objective 1": 179,
	"A51 Rescue - Perfect Agent Objective 2": 180,
	"A51 Rescue - Perfect Agent Objective 3": 181,
	"A51 Rescue - Perfect Agent Objective 4": 182,
	"A51 Rescue - Perfect Agent Objective 5": 183,
	"A51 Escape - Perfect Agent Objective 1": 184,
	"A51 Escape - Perfect Agent Objective 2": 185,
	"A51 Escape - Perfect Agent Objective 3": 186,
	"A51 Escape - Perfect Agent Objective 4": 187,
	"A51 Escape - Perfect Agent Objective 5": 188,
	"Air Base - Perfect Agent Objective 1": 189,
	"Air Base - Perfect Agent Objective 2": 190,
	"Air Base - Perfect Agent Objective 3": 191,
	"Air Base - Perfect Agent Objective 4": 192,
	"Air Base - Perfect Agent Objective 5": 193,
	"Air Force One - Perfect Agent Objective 1": 194,
	"Air Force One - Perfect Agent Objective 2": 195,
	"Air Force One - Perfect Agent Objective 3": 196,
	"Air Force One - Perfect Agent Objective 4": 197,
	"Air Force One - Perfect Agent Objective 5": 198,
	"Crash Site - Perfect Agent Objective 1": 199,
	"Crash Site - Perfect Agent Objective 2": 200,
	"Crash Site - Perfect Agent Objective 3": 201,
	"Crash Site - Perfect Agent Objective 4": 202,
	"Crash Site - Perfect Agent Objective 5": 203,
	"Pelagic II - Perfect Agent Objective 1": 204,
	"Pelagic II - Perfect Agent Objective 2": 205,
	"Pelagic II - Perfect Agent Objective 3": 206,
	"Pelagic II - Perfect Agent Objective 4": 207,
	"Pelagic II - Perfect Agent Objective 5": 208,
	"Deep Sea - Perfect Agent Objective 1": 209,
	"Deep Sea - Perfect Agent Objective 2": 210,
	"Deep Sea - Perfect Agent Objective 3": 211,
	"Deep Sea - Perfect Agent Objective 4": 212,
	"Deep Sea - Perfect Agent Objective 5": 213,
	"CI Defense - Perfect Agent Objective 1": 214,
	"CI Defense - Perfect Agent Objective 2": 215,
	"CI Defense - Perfect Agent Objective 3": 216,
	"CI Defense - Perfect Agent Objective 4": 217,
	"CI Defense - Perfect Agent Objective 5": 218,
	"Attack Ship - Perfect Agent Objective 1": 219,
	"Attack Ship - Perfect Agent Objective 2": 220,
	"Attack Ship - Perfect Agent Objective 3": 221,
	"Attack Ship - Perfect Agent Objective 4": 222,
	"Attack Ship - Perfect Agent Objective 5": 223,
	"Skedar Ruins - Perfect Agent Objective 1": 224,
	"Skedar Ruins - Perfect Agent Objective 2": 225,
	"Skedar Ruins - Perfect Agent Objective 3": 226,
	"Skedar Ruins - Perfect Agent Objective 4": 227,
	"Skedar Ruins - Perfect Agent Objective 5": 228,
	"Mr. Blonde's Revenge - Perfect Agent Objective 1": 229,
	"Mr. Blonde's Revenge - Perfect Agent Objective 2": 230,
	"Mr. Blonde's Revenge - Perfect Agent Objective 3": 231,
	"Maian SOS - Perfect Agent Objective 1": 234,
	"Maian SOS - Perfect Agent Objective 2": 235,
	"Maian SOS - Perfect Agent Objective 3": 236,
	"WAR! - Perfect Agent Objective 1": 239,
	"WAR! - Perfect Agent Objective 2": 240,
	"WAR! - Perfect Agent Objective 3": 241,	
	"The Duel - Perfect Agent Objective 1": 244,
	"The Duel - Perfect Agent Objective 2": 245,
	"The Duel - Perfect Agent Objective 3": 246,
    "Complete: dD Defection - Agent": 247,
    "Complete: dD Defection - Special Agent": 248,
    "Complete: dD Defection - Perfect Agent": 249,
    "Complete: dD Investigation - Agent": 250,
    "Complete: dD Investigation - Special Agent": 251,
    "Complete: dD Investigation - Perfect Agent": 252,
    "Complete: dD Extraction - Agent": 253,
    "Complete: dD Extraction - Special Agent": 254,
    "Complete: dD Extraction - Perfect Agent": 255,
    "Complete: Carrington Villa - Agent": 256,
    "Complete: Carrington Villa - Special Agent": 257,
    "Complete: Carrington Villa - Perfect Agent": 258,
    "Complete: Chicago - Agent": 259,
    "Complete: Chicago - Special Agent": 260,
    "Complete: Chicago - Perfect Agent": 261,
    "Complete: G5 Building - Agent": 262,
    "Complete: G5 Building - Special Agent": 263,
    "Complete: G5 Building - Perfect Agent": 264,
    "Complete: A51 Infiltration - Agent": 265,
    "Complete: A51 Infiltration - Special Agent": 266,
    "Complete: A51 Infiltration - Perfect Agent": 267,
    "Complete: A51 Rescue - Agent": 268,
    "Complete: A51 Rescue - Special Agent": 269,
    "Complete: A51 Rescue - Perfect Agent": 270,
    "Complete: A51 Escape - Agent": 271,
    "Complete: A51 Escape - Special Agent": 272,
    "Complete: A51 Escape - Perfect Agent": 273,
    "Complete: Air Base - Agent": 274,
    "Complete: Air Base - Special Agent": 275,
    "Complete: Air Base - Perfect Agent": 276,
    "Complete: Air Force One - Agent": 277,
    "Complete: Air Force One - Special Agent": 278,
    "Complete: Air Force One - Perfect Agent": 279,
    "Complete: Crash Site - Agent": 280,
    "Complete: Crash Site - Special Agent": 281,
    "Complete: Crash Site - Perfect Agent": 282,
    "Complete: Pelagic II - Agent": 283,
    "Complete: Pelagic II - Special Agent": 284,
    "Complete: Pelagic II - Perfect Agent": 285,
    "Complete: Deep Sea - Agent": 286,
    "Complete: Deep Sea - Special Agent": 287,
    "Complete: Deep Sea - Perfect Agent": 288,
    "Complete: CI Defense - Agent": 289,
    "Complete: CI Defense - Special Agent": 290,
    "Complete: CI Defense - Perfect Agent": 291,
    "Complete: Attack Ship - Agent": 292,
    "Complete: Attack Ship - Special Agent": 293,
    "Complete: Attack Ship - Perfect Agent": 294,
    "Complete: Skedar Ruins - Agent": 295,
    "Complete: Skedar Ruins - Special Agent": 296,
    "Complete: Skedar Ruins - Perfect Agent": 297,
    "Complete: Mr. Blonde's Revenge - Agent": 298,
    "Complete: Mr. Blonde's Revenge - Special Agent": 299,
    "Complete: Mr. Blonde's Revenge - Perfect Agent": 300,
    "Complete: Maian SOS - Agent": 301,
    "Complete: Maian SOS - Special Agent": 302,
    "Complete: Maian SOS - Perfect Agent": 303,
    "Complete: WAR! - Agent": 304,
    "Complete: WAR! - Special Agent": 305,
    "Complete: WAR! - Perfect Agent": 306,
    "Complete: The Duel - Agent": 307,
    "Complete: The Duel - Special Agent": 308,
    "Complete: The Duel - Perfect Agent": 309,
	"Complete: Challenge 1": 310,
	"Complete: Challenge 2": 311,
	"Complete: Challenge 3": 312,
	"Complete: Challenge 4": 313,
	"Complete: Challenge 5": 314,
	"Complete: Challenge 6": 315,
	"Complete: Challenge 7": 316,
	"Complete: Challenge 8": 317,
	"Complete: Challenge 9": 318,
	"Complete: Challenge 10": 319,
	"Complete: Challenge 11": 320,
	"Complete: Challenge 12": 321,
	"Complete: Challenge 13": 322,
	"Complete: Challenge 14": 323,
	"Complete: Challenge 15": 324,
	"Complete: Challenge 16": 325,
	"Complete: Challenge 17": 326,
	"Complete: Challenge 18": 327,
	"Complete: Challenge 19": 328,
	"Complete: Challenge 20": 329,
	"Complete: Challenge 21": 330,
	"Complete: Challenge 22": 331,
	"Complete: Challenge 23": 332,
	"Complete: Challenge 24": 333,
	"Complete: Challenge 25": 334,
	"Complete: Challenge 26": 335,
	"Complete: Challenge 27": 336,
	"Complete: Challenge 28": 337,
	"Complete: Challenge 29": 338,
	"Complete: Challenge 30": 339,
    "Firing Range: Falcon 2 - Bronze": 340,
    "Firing Range: Falcon 2 - Silver": 341,
    "Firing Range: Falcon 2 - Gold": 342,
    "Firing Range: Falcon 2 (Silencer) - Bronze": 343,
    "Firing Range: Falcon 2 (Silencer) - Silver": 344,
    "Firing Range: Falcon 2 (Silencer) - Gold": 345,
    "Firing Range: Falcon 2 (Scope) - Bronze": 346,
    "Firing Range: Falcon 2 (Scope) - Silver": 347,
    "Firing Range: Falcon 2 (Scope) - Gold": 348,
    "Firing Range: MagSec 4 - Bronze": 349,
    "Firing Range: MagSec 4 - Silver": 350,
    "Firing Range: MagSec 4 - Gold": 351,
    "Firing Range: Mauler - Bronze": 352,
    "Firing Range: Mauler - Silver": 353,
    "Firing Range: Mauler - Gold": 354,
    "Firing Range: Phoenix - Bronze": 355,
    "Firing Range: Phoenix - Silver": 356,
    "Firing Range: Phoenix - Gold": 357,
    "Firing Range: DY357 Magnum - Bronze": 358,
    "Firing Range: DY357 Magnum - Silver": 359,
    "Firing Range: DY357 Magnum - Gold": 360,
    "Firing Range: DY357-LX - Bronze": 361,
    "Firing Range: DY357-LX - Silver": 362,
    "Firing Range: DY357-LX - Gold": 363,
    "Firing Range: CMP150 - Bronze": 364,
    "Firing Range: CMP150 - Silver": 365,
    "Firing Range: CMP150 - Gold": 366,
    "Firing Range: Cyclone - Bronze": 367,
    "Firing Range: Cyclone - Silver": 368,
    "Firing Range: Cyclone - Gold": 369,
    "Firing Range: Callisto NTG - Bronze": 370,
    "Firing Range: Callisto NTG - Silver": 371,
    "Firing Range: Callisto NTG - Gold": 372,
    "Firing Range: RC-P120 - Bronze": 373,
    "Firing Range: RC-P120 - Silver": 374,
    "Firing Range: RC-P120 - Gold": 375,
    "Firing Range: Laptop Gun - Bronze": 376,
    "Firing Range: Laptop Gun - Silver": 377,
    "Firing Range: Laptop Gun - Gold": 378,
    "Firing Range: Dragon - Bronze": 379,
    "Firing Range: Dragon - Silver": 380,
    "Firing Range: Dragon - Gold": 381,
    "Firing Range: K7 Avenger - Bronze": 382,
    "Firing Range: K7 Avenger - Silver": 383,
    "Firing Range: K7 Avenger - Gold": 384,
    "Firing Range: AR34 - Bronze": 385,
    "Firing Range: AR34 - Silver": 386,
    "Firing Range: AR34 - Gold": 387,
    "Firing Range: SuperDragon - Bronze": 388,
    "Firing Range: SuperDragon - Silver": 389,
    "Firing Range: SuperDragon - Gold": 390,
    "Firing Range: Shotgun - Bronze": 391,
    "Firing Range: Shotgun - Silver": 392,
    "Firing Range: Shotgun - Gold": 393,
    "Firing Range: Reaper - Bronze": 394,
    "Firing Range: Reaper - Silver": 395,
    "Firing Range: Reaper - Gold": 396,
    "Firing Range: Sniper Rifle - Bronze": 397,
    "Firing Range: Sniper Rifle - Silver": 398,
    "Firing Range: Sniper Rifle - Gold": 399,
    "Firing Range: FarSight XR-20 - Bronze": 400,
    "Firing Range: FarSight XR-20 - Silver": 401,
    "Firing Range: FarSight XR-20 - Gold": 402,
    "Firing Range: Devastator - Bronze": 403,
    "Firing Range: Devastator - Silver": 404,
    "Firing Range: Devastator - Gold": 405,
    "Firing Range: Rocket Launcher - Bronze": 406,
    "Firing Range: Rocket Launcher - Silver": 407,
    "Firing Range: Rocket Launcher - Gold": 408,
    "Firing Range: Slayer - Bronze": 409,
    "Firing Range: Slayer - Silver": 410,
    "Firing Range: Slayer - Gold": 411,
    "Firing Range: Combat Knife - Bronze": 412,
    "Firing Range: Combat Knife - Silver": 413,
    "Firing Range: Combat Knife - Gold": 414,
    "Firing Range: Crossbow - Bronze": 415,
    "Firing Range: Crossbow - Silver": 416,
    "Firing Range: Crossbow - Gold": 417,
    "Firing Range: Tranquilizer - Bronze": 418,
    "Firing Range: Tranquilizer - Silver": 419,
    "Firing Range: Tranquilizer - Gold": 420,
    "Firing Range: Laser - Bronze": 421,
    "Firing Range: Laser - Silver": 422,
    "Firing Range: Laser - Gold": 423,
    "Firing Range: Grenade - Bronze": 424,
    "Firing Range: Grenade - Silver": 425,
    "Firing Range: Grenade - Gold": 426,
    # "Firing Range: N-Bomb - Bronze": 427,
    # "Firing Range: N-Bomb - Silver": 428,
    # "Firing Range: N-Bomb - Gold": 429,
    "Firing Range: Timed Mine - Bronze": 430,
    "Firing Range: Timed Mine - Silver": 431,
    "Firing Range: Timed Mine - Gold": 432,
    "Firing Range: Proximity Mine - Bronze": 433,
    "Firing Range: Proximity Mine - Silver": 434,
    "Firing Range: Proximity Mine - Gold": 435,
    "Firing Range: Remote Mine - Bronze": 436,
    "Firing Range: Remote Mine - Silver": 437,
    "Firing Range: Remote Mine - Gold": 438,
    "Device Training: Data Uplink": 439,
    "Device Training: ECM Mine": 440,
    "Device Training: CamSpy": 441,
    "Device Training: Night Vision": 442,
    "Device Training: Door Decoder": 443,
    "Device Training: R-Tracker": 444,
    "Device Training: IR Scanner": 445,
    "Device Training: X-Ray Scanner": 446,
    "Device Training: Disguise": 447,
    "Device Training: Cloaking Device": 448,
    "Holotraining 1: Looking Around": 449,
    "Holotraining 2: Movement 1": 450,
    "Holotraining 3: Movement 2": 451,
    "Holotraining 4: Unarmed Combat 1": 452,
    "Holotraining 5: Unarmed Combat 2": 453,
    "Holotraining 6: Live Combat 1": 454,
    "Holotraining 7: Live Combat 2": 455,
    "Cheat Unlock: Complete dD Defection": 456,
    "Cheat Unlock: Complete dD Investigation": 457,
    "Cheat Unlock: Complete dD Extraction": 458,
    "Cheat Unlock: Complete Carrington Villa": 459,
    "Cheat Unlock: Complete Chicago": 460,
    "Cheat Unlock: Complete G5 Building": 461,
    "Cheat Unlock: Complete A51 Infiltration": 462,
    "Cheat Unlock: Complete A51 Rescue": 463,
    "Cheat Unlock: Complete A51 Escape": 464,
    "Cheat Unlock: Complete Air Base": 465,
    "Cheat Unlock: Complete Air Force One": 466,
    "Cheat Unlock: Complete Crash Site": 467,
    "Cheat Unlock: Complete Pelagic II" : 468,
    "Cheat Unlock: Complete Deep Sea": 469,
    "Cheat Unlock: Complete CI Defense": 470,
    "Cheat Unlock: Complete Attack Ship": 471,
    "Cheat Unlock: Complete Skedar Ruins": 472,
    "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30": 473,
    "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30": 474,
    "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03": 475,
    "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30": 476,
    "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00": 477,
    "Cheat Unlock: Complete G5 Building (Agent) in under 1:40": 478,
    "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00": 479,
    "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59": 480,
    "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50": 481,
    "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11": 482,
    "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55": 483,
    "Cheat Unlock: Complete Crash Site (Agent) in under 2:50": 484,
    "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07": 485,
    "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27": 486,
    "Cheat Unlock: Complete CI Defense (Agent) in under 1:45": 487,
    "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17": 488,
    "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31": 489,
    "Cheat Unlock: Get gold on Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)": 490,
    "Cheat Unlock: Get gold on MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX": 491,
    "Cheat Unlock: Get gold on CMP150, Cyclone, Callisto NTG, and RC-P120": 492,
    "Cheat Unlock: Get gold on Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon": 493,
    "Cheat Unlock: Get gold on Shotgun, Sniper Rifle, Rocket Launcher, and Slayer": 494,
    "Cheat Unlock: Get gold on Timed Mine, Proximity Mine, and Remote Mine": 495,
    "Cheat Unlock: Get gold on FarSight XR-20, Crossbow, Combat Knife, and Grenade": 496,
    "Cheat Unlock: Get gold on Tranquilizer, Reaper, and Devastator": 497,
    "Collect All Stars": 498,
    # "Complete Challenges: Unused First Unlock": 499,
    "Complete 1 Challenge: FarSight XR-20 Unlock": 500,
    "Complete 7 Challenges: Tranquilizer Unlock": 501,
    "Complete 4 Challenges: SuperDragon Unlock": 502,
    "Complete 13 Challenges: Slayer Unlock": 503,
    "Complete 3 Challenges: Falcon 2 (Silencer) Unlock": 504,
    "Complete 8 Challenges: Falcon 2 (Scope) Unlock": 505,
    "Complete 16 Challenges: Mauler Unlock": 506,
    "Complete 14 Challenges: Phoenix Unlock": 507,
    "Complete 20 Challenges: DY357-LX Unlock": 508,
    "Complete 17 Challenges: Callisto NTG Unlock": 509,
    "Complete 5 Challenges: Laptop Gun Unlock": 510,
    # "Complete Challenges: K7 Avenger Unlock": 511,
    "Complete 19 Challenges: RC-P120 Unlock": 512,
    "Complete 2 Challenges: Shotgun Unlock": 513,
    "Complete 9 Challenges: Reaper Unlock": 514,
    "Complete 11 Challenges: Devastator Unlock": 515,
    "Complete 18 Challenges: Crossbow Unlock": 516,
    "Complete 21 Challenges: N-Bomb Unlock": 517,
    "Complete 12 Challenges: Proximity Mine Unlock": 518,
    "Complete 6 Challenges: Remote Mine Unlock": 519,
    # "Complete Challenges: X-Ray Scanner Unlock": 520,
    # "Complete Challenges: Shield Unlock": 521,
    "Complete 10 Challenges: Cloaking Device Unlock": 522,
    "Complete 15 Challenges: Combat Boost Unlock": 523,
    "Complete 7 Challenges: Hard Bot Difficulty Unlock": 524,
    "Complete 12 Challenges: Perfect Bot Difficulty Unlock": 525,
    # "Complete Challenges: Unused 1B Unlock": 526,
    "Complete 22 Challenges: Dark Bot Difficulty Unlock": 527,
    "Complete 8 Challenges: Slow Motion Unlock": 528,
    "Complete 3 Challenges: One-Hit Kills Unlock": 529,
    # "Complete Challenges: King of the Hill Unlock": 530,
    "Complete 2 Challenges: Hold the Briefcase Unlock": 531,
    "Complete 4 Challenges: Capture the Case Unlock": 532,
    # "Complete Challenges: Unused 22 Unlock": 533,
    "Complete 17 Challenges: Car Park Unlock": 534,
    "Complete 1 Challenge: Complex Unlock": 535,
    "Complete 3 Challenges: Warehouse Unlock": 536,
    "Complete 5 Challenges: Ravine Unlock": 537,
    "Complete 6 Challenges: Temple Unlock": 538,
    "Complete 9 Challenges: G5 Building Unlock": 539,
    "Complete 11 Challenges: Grid Unlock": 540,
    "Complete 12 Challenges: Felicity Unlock": 541,
    "Complete 14 Challenges: Villa Unlock": 542,
    "Complete 16 Challenges: Sewers Unlock": 543,
    "Complete 22 Challenges: Ruins Unlock": 544,
    "Complete 18 Challenges: Base Unlock": 545,
    # "Complete Challenges: Unused 2F Unlock": 546,
    "Complete 20 Challenges: Fortress Unlock": 547,
    # "Complete Challenges: Unused 31 Unlock": 548,
    "Complete 1 Challenge: dataDyne Female Guard Unlock": 549,
    "Complete 2 Challenges: Office Suit and Office Casual Unlock": 550,
    "Complete 4 Challenges: Carrington Villa Outfits Unlock": 551,
    "Complete 5 Challenges: Trent Unlock": 552,
    "Complete 5 Challenges: NSA Lackey Unlock": 553,
    "Complete 6 Challenges: G5 Building Outfits Unlock": 554,
    "Complete 7 Challenges: Mr. Blonde Unlock": 555,
    "Complete 9 Challenges: CIA Agent and FBI Agent Unlock": 556,
    "Complete 10 Challenges: A51 Infiltration Outfits Unlock": 557,
    "Complete 11 Challenges: Lab Technician Outfits Unlock": 558,
    "Complete 12 Challenges: Biotechnician Unlock": 559,
    "Complete 14 Challenges: Elvis and Maian Soldier Unlock": 560,
    "Complete 17 Challenges: Alaskan Guard Unlock": 561,
    "Complete 16 Challenges: Air Force One Outfits Unlock": 562,
    "Complete 7 Challenges: 8 Bots and Dinner Jacket Outfits Unlock": 563,
    "Complete 18 Challenges: Formal Outfits and President Unlock": 564,
    "Complete 19 Challenges: President's Clone Unlock": 565,
    "Complete 18 Challenges: Presidential Security Unlock": 566,
    "Complete 19 Challenges: NSA Bodyguard Unlock": 567,
    "Complete 24 Challenges: Pelagic II Outfits Unlock": 568,
    "Complete 8 Challenges: Joanna Trench Unlock": 569,
    # "Complete Challenges: Unused Jo Snow Unlock": 570,
    # "Complete Challenges: Unused 48 Unlock": 571,
    # "Complete Challenges: Unused 49 Unlock": 572,
    "Complete 17 Challenges: Joanna Arctic Unlock": 573,
    # "Complete Challenges: Unused 4B Unlock": 574,
    # "Complete Challenges: Jonathan Unlock": 575,
    "Complete 12 Challenges: Pop a Cap Unlock": 576,
    "Complete 6 Challenges: Hacker Central Unlock": 577,
    # "Complete Challenges: Laser Unlock": 578,
    "Complete G5 Building (Agent): Bottom Exit": 579,
    "Complete G5 Building (Agent): Upper Exit": 580,
    "Complete G5 Building (Special Agent): Bottom Exit": 581,
    "Complete G5 Building (Special Agent): Upper Exit": 582,
    "Complete G5 Building (Perfect Agent): Bottom Exit": 583,
    "Complete G5 Building (Perfect Agent): Upper Exit": 584,
    "Complete A51 Escape (Agent): UFO Escape": 585,
    "Complete A51 Escape (Agent): Alternate Escape": 586,
    "Complete A51 Escape (Special Agent): UFO Escape": 587,
    "Complete A51 Escape (Special Agent): Alternate Escape": 588,
    "Complete A51 Escape (Perfect Agent): UFO Escape": 589,
    "Complete A51 Escape (Perfect Agent): Alternate Escape": 590,
    "Complete Air Base (Agent): Shuttle Exit": 591,
    "Complete Air Base (Agent): Ladder Exit": 592,
    "Complete Air Base (Special Agent): Shuttle Exit": 593,
    "Complete Air Base (Special Agent): Ladder Exit": 594,
    "Complete Air Base (Perfect Agent): Shuttle Exit": 595,
    "Complete Air Base (Perfect Agent): Ladder Exit": 596,
    "dD Defection (Agent/Special): 3F Shield": 2010,
    "dD Defection: 2F double Falcon 2 (silencer)": 2033,
    "dD Defection: 2F Laptop Gun": 2466,
    "dD Defection: 2F Falcon 2 (silencer) (on right)": 2468,
    "dD Defection: 2F Falcon 2 (silencer) (on left)": 2469,
    "dD Defection: 3F tiny ammo box (on corner desk)": 2470,
    "dD Defection: 3F tiny ammo box (on table near couch)": 2471,
    "dD Defection: 2F tiny ammo box (on desk across the stairs)": 2472,
    "dD Defection: 2F tiny ammo box (on desk across the elevator)": 2473,
    "dD Defection: 2F Falcon 2 (silencer) (on desk)": 2474,
    "dD Defection: 2F tiny ammo box (under stairs)": 2475,
    "dD Defection: 1F CMP150 (on right of front desk)": 2605,
    "dD Defection: 1F CMP150 (on left of front desk)": 2606,
    "dD Defection (Agent): 1F Shield": 2607,
    "dD Investigation: ammo box (front of room above the K7 Avenger)": 4625,
    "dD Investigation: ammo box (back of room above the K7 Avenger)": 4626,
    "dD Investigation: ammo box (front of room with one scientist)": 4627,
    "dD Investigation: ammo box (back of room with one scientist)": 4628,
    "dD Investigation: ammo box (front of Night Vision room)": 4629,
    "dD Investigation: ammo box (back of Night Vision room)": 4630,
    "dD Investigation: ammo box (front of room near two scientists)": 4631,
    "dD Investigation: ammo box (back of room near two scientists)": 4632,
    "dD Investigation: CMP150 (on front of table)": 4633,
    "dD Investigation: CMP150 (on back of table)": 4634,
    "dD Investigation: CMP150 (left of secret weapons compartment)": 4635,
    "dD Investigation: CMP150 (right of secret weapons compartment)": 4636,
    "dD Investigation: Proximity Mine (in radioactive room)": 4637,
    "dD Investigation (Agent): Shield (on crate)": 4638,
    "dD Investigation (Agent/Special): Shield (behind the glass)": 4639,
    "dD Extraction: 1F DY357 Magnum (from fifth guard)": 6005,
    "dD Extraction (Agent): 2F Shield": 6120,
    "dD Extraction: 4F Rocket Launcher": 6452,
    "dD Extraction: 4F Grenade (on Cassandra's desk)": 6466,
    "dD Extraction: 4F Dragon (in hidden room in Cassandra's office)": 6467,
    "dD Extraction: Rocket ammo box (on left)": 6516,
    "dD Extraction: Rocket ammo box (on right)": 6519,
    "Carrington Villa: Devastator (in helipad crate)": 8000,
    "Carrington Villa: 1st ammo box (in crate on observatory path)": 8001,
    "Carrington Villa: 2nd ammo box (in crate on observatory path)": 8002,
    "Carrington Villa: 3rd ammo box (in crate on observatory path)": 8003,
    "Carrington Villa: 4th ammo box (in crate on observatory path)": 8004,
    "Carrington Villa: 5th ammo box (in crate on observatory path)": 8005,
    "Carrington Villa: 6th ammo box (in crate on observatory path)": 8006,
    "Carrington Villa: 7th ammo box (in crate on observatory path)": 8007,
    "Carrington Villa: 8th ammo box (in crate on observatory path)": 8008,
    "Carrington Villa: 9th ammo box (in crate on observatory path)": 8009,
    "Carrington Villa (Perfect Agent): Sniper Rifle (in the bathroom)": 8085,
    "Carrington Villa: double CMP150 (from sniper near the helipad)": 8410,
    "Carrington Villa (Agent): Shield (on helipad crate)": 8568,
    "Carrington Villa (Agent): Shield (in the bathroom)": 8569,
    "Chicago: BombSpy (in the dumpster)": 10000,
    "Chicago: double Falcon 2 (scope) (in the Pond Punk)": 10287,
    "Chicago (Agent): Shield (near the taxi)": 10289,
    "Chicago (Agent/Special): Shield (under stairs near Pond Punk)": 10290,
    "G5 Building: Crossbow (after knocking out the second guard)": 12000,
    "G5 Building (Agent/Special): Shield (on stairs to the upper exit)": 12086,
    "G5 Building: N-Bomb (near the upper exit)": 12149,
    "G5 Building (Agent): Shield (in room before the laser grids)": 12150,
    "A51 Infiltration: Rocket Launcher (in mine field)": 14052,
    "A51 Infiltration: double MagSec 4 (after placing comms rider)": 14053,
    "A51 Infiltration (Agent): Shield (near hoverbike)": 14150,
    "A51 Infiltration (Agent/Special): Shield (in the crawl space)": 15381,
    "A51 Rescue (Agent): Shield (guard past first elevator)": 16004,
    "A51 Rescue: Phoenix (past locked hangar door)": 16905,
    "A51 Rescue: double Falcon 2 (silencer) (hidden in barrel)": 16987,
    "A51 Rescue (Agent/Special): Shield (on desk near computer)": 17140,
    "A51 Escape: double Falcon 2 (scope) (behind you at the start)": 18036,
    "A51 Escape (Agent): Shield (dropped by biotechnician)": 18040,
    "A51 Escape (Agent/Special): Shield (behind locked medical containment doors)": 18895,
    "A51 Escape: Remote Mine (in first room with guards)": 19383,
    "Air Base (Agent): Shield (dropped by NSA Lackey)": 20017,
    "Air Base: double DY357 Magnum (after knocking out all NSA Lackeys)": 20018,
    "Air Base: Proximity Mine (past the cave)": 20181,
    "Air Base (Agent/Special): Shield (in the safe)": 20214,
    "Air Force One: Cyclone (in room right of stairs)": 22203,
    "Air Force One: Cyclone (in room left of stairs)": 22204,
    "Air Force One (Agent/Special): Shield (in piano room)": 22363,
    "Air Force One (Agent): Shield (in small kitchen)": 22364,
    "Crash Site: DY357-LX (from disarming Trent)": 24001,
    "Crash Site (Agent/Special): Shield (behind President's clone)": 24144,
    "Crash Site (Agent): Shield (near the crashed UFO)": 24262, 
    "Crash Site: Proximity Mine (from Elvis before doing any objective)": 24263, # Shares same pad as Shield (need to add one for the location)
    "Pelagic II: double Falcon 2 (silencer) (without triggering the alarm)": 26052,
    "Pelagic II (Agent): Shield (on the helipad)": 26541,
    "Pelagic II (Agent/Special): Shield (on the sub hangar crate)": 26542,
    "Deep Sea: Proximity Mine (from guard in 2nd room with cloaked guards)": 28008,
    "Deep Sea (Agent/Special): Shield (on the left path)": 28018,
    # "Deep Sea (Agent): Shield (dropped from guard)": 28026,
    # "Deep Sea: Shotgun (near Shield on the left path)": 28063,
    "CI Defense: Devastator (dropped after saving most of the hostages)": 30000,
    "CI Defense (Agent/Special): Basement Shield": 30146,
    "CI Defense (Agent): 2F Shield": 30648,
    "Attack Ship: double Mauler (dropped from Skedar in final room)": 32045,
    "Attack Ship (Perfect Agent): De Vries' Necklace": 32051,
    "Attack Ship: Slayer (in the room past green chambers)": 32466,
    "Attack Ship (Agent/Special): Shield (on table)": 32499,
    "Skedar Ruins: double Phoenix (near the gap)": 34050,
    "Skedar Ruins (Agent/Special): Shield (area past the gap to the right)": 34186,
    "Skedar Ruins (Agent): Shield (behind the fallen pillar)": 34337,
    "Mr. Blonde's Revenge (Agent/Special): 3F Shield": 36010,
    "Mr. Blonde's Revenge: 1F double CMP150 (from guard near bottom elevator)": 36015,
    "Mr. Blonde's Revenge: 2F Laptop Gun": 36466,
    "Mr. Blonde's Revenge: 2F Falcon 2 (on right)": 36468,
    "Mr. Blonde's Revenge: 2F Falcon 2 (on left)": 36469,
    "Mr. Blonde's Revenge: 3F tiny ammo box (on corner desk)": 36470,
    "Mr. Blonde's Revenge: 3F tiny ammo box (on table near couch)": 36471,
    "Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the stairs)": 36472,
    "Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the elevator)": 36473,
    "Mr. Blonde's Revenge: 2F Falcon 2 (on desk)": 36474,
    "Mr. Blonde's Revenge: 2F tiny ammo box (under stairs)": 36475,
    "Mr. Blonde's Revenge: 1F CMP150 (on right of front desk)": 36605,
    "Mr. Blonde's Revenge: 1F CMP150 (on left of front desk)": 36606,
    "Mr. Blonde's Revenge (Agent): 1F Shield": 36607,
    "Maian SOS: double DY357-LX (from dual-wielding guard)": 38011,
    "Maian SOS: Psychosis Gun (on desk near the start)": 38919,
    "dD Central: Top Glass Railing (stairs between roof and 4F)": 40291, # 273
    "dD Central: Bottom Glass Railing (stairs between roof and 4F)": 40292, # 274
    "dD Central: Top Window (stairs between roof and 4F)": 40284, # 272
    "dD Central: Middle Window (stairs between roof and 4F)": 40283, # 271
    "dD Central: Bottom Window (stairs between roof and 4F)": 40257, # 244
    "dD Central: 4F Window 1": 40256, # 243
    "dD Central: 4F Window 2": 40240, # 227
    "dD Central: 4F Window 3": 40235, # 222
    "dD Central: 4F Window 4": 40231, # 218
    "dD Central: 4F Window 5": 40232, # 219
    "dD Central: 4F Window 6": 40226, # 213
    "dD Central: 4F Window 7": 40225, # 212
    "dD Central: 4F Window 8": 40247, # 234
    "dD Central: 4F Window 9": 40255, # 242
    "dD Central: 4F Glass Railing 1": 40297, # 279
    "dD Central: 4F Glass Railing 2": 40295, # 282
    "dD Central: 4F Glass Railing 3": 40296, # 281
    "dD Central: 4F Glass Railing 4": 40298, # 280
    "dD Central: Cassandra's Office Window (left)": 40280, # 268
    "dD Central: Cassandra's Office Window (middle)": 40281, # 269
    "dD Central: Cassandra's Office Window (right)": 40279, # 267
    "dD Central: Cassandra's Office Window (top)": 40282, # 270
    "dD Central: Top Glass Railing (stairs between 4F and 2F)": 40293, # 275
    "dD Central: Bottom Glass Railing (stairs between 4F and 2F)": 40294, # 276
    "dD Central: Top Window (stairs between 4F and 2F)": 40260, # 247
    "dD Central: Middle Window (stairs between 4F and 2F)": 40258, # 246
    "dD Central: Bottom Window (stairs between 4F and 2F)": 40259, # 245
    "dD Central: 3F Glass 1 (near elevator)": 40274, # 261
    "dD Central: 3F Glass 2 (near elevator)": 40276, # 263
    "dD Central: 3F Glass 3 (near elevator)": 40275, # 262
    "dD Central: 3F Window 1": 40254, # 241
    "dD Central: 3F Window 2": 40248, # 235
    "dD Central: 3F Window 3": 40224, # 211
    "dD Central: 3F Window 4": 40227, # 214
    "dD Central: 3F Window 5": 40233, # 220
    "dD Central: 3F Window 6": 40230, # 217
    "dD Central: 3F Window 7": 40236, # 223
    "dD Central: 3F Window 8": 40239, # 226
    "dD Central: 3F Window 9": 40241, # 228
    "dD Central: 3F Window 10": 40245, # 232
    "dD Central: 3F Window 11": 40244, # 231
    "dD Central: 3F Window 12": 40269, # 256
    "dD Central: 3F Window 13": 40270, # 257
    "dD Central: 3F Window 14": 40267, # 254
    "dD Central: 3F Window 15": 40268, # 255
    "dD Central: 3F Window 16": 40262, # Unreachable on Extraction
    "dD Central: 3F Window 17": 40251, # Unreachable on Extraction
    "dD Central: 3F Window 18": 40252, # Unreachable on Extraction
    "dD Central: 2F Glass 1 (near elevator)": 40273, # 260
    "dD Central: 2F Glass 2 (near elevator)": 40271, # 258
    "dD Central: 2F Glass 3 (near elevator)": 40272, # 259
    "dD Central: 2F Window 1": 40249, # 236
    "dD Central: 2F Window 2": 40223, # 210
    "dD Central: 2F Window 3": 40228, # 215
    "dD Central: 2F Window 4": 40234, # Unreachable on Extraction
    "dD Central: 2F Window 5": 40229, # Unreachable on Extraction
    "dD Central: 2F Window 6": 40237, # 224
    "dD Central: 2F Window 7": 40238, # 225
    "dD Central: 2F Window 8": 40242, # 229
    "dD Central: 2F Window 9": 40246, # 233
    "dD Central: 2F Window 10": 40243, # 230
    "dD Central: 2F Window 11": 40261, # 248
    "dD Central: 2F Window 12": 40263, # 250
    "dD Central: 2F Window 13": 40264, # 251
    "dD Central: 2F Window 14": 40265, # 252
    "dD Central: 2F Window 15": 40266, # 253
    "dD Central: 2F Window 16": 40250, # 237
    "dD Central: 2F Window 17": 40253, # 240
    "dD Central: Left Elevator Glass 1": 40287, # 208 # Left when facing door of elevator 
    "dD Central: Left Elevator Glass 2": 40288, # 209 # Right when facing door of elevator 
    "dD Central: Right Elevator Glass 1": 40289, # 207 # Left when facing door of elevator
    "dD Central: Right Elevator Glass 2": 40290, # 206 # Right when facing door of elevator
    "dD Central: 1F Left Elevator Glass 1": 40584, # 597
    "dD Central: 1F Left Elevator Glass 2": 40589, # 592
    "dD Central: 1F Left Elevator Glass 3": 40591, # 590
    "dD Central: 1F Right Elevator Glass 1": 40588, # 593
    "dD Central: 1F Right Elevator Glass 2": 40590, # 591
    "dD Central: 1F Right Elevator Glass 3": 40592, # 589
    "dD Central: 1F Glass Railing 1": 40585, # 596
    "dD Central: 1F Glass Railing 2": 40586, # 595
    "dD Central: 1F Glass Railing 3": 40587, # 594
    "dD Central: 1F Glass Railing 4": 40593, # 588 # Left from top of stairs 
    "dD Central: 1F Glass Railing 5": 40594, # 587 # Right from top of stairs 
    "dD Investigation: Glass Railing (near cleaning bot)": 42440,
    "dD Investigation: Glass on door (near cleaning bot)": 42350,
    "dD Investigation: Glass 1 (near computer)": 42435,
    "dD Investigation: Glass 2 (near computer)": 42436,
    "dD Investigation: Glass 1 (room with one scientist)": 42448,
    "dD Investigation: Glass 2 (room with one scientist)": 42449,
    "dD Investigation: Glass 3 (room with one scientist)": 42450,
    "dD Investigation: Glass 4 (room with one scientist)": 42451,
    "dD Investigation: Glass 5 (room with one scientist)": 42452,
    "dD Investigation: Glass 6 (room with one scientist)": 42453,
    "dD Investigation: Glass 7 (room with one scientist)": 42454,
    "dD Investigation: Glass 8 (room with one scientist)": 42455,
    "dD Investigation: Glass 1 (room with night vision)": 42461,
    "dD Investigation: Glass 2 (room with night vision)": 42462,
    "dD Investigation: Glass 3 (room with night vision)": 42463,
    "dD Investigation: Glass 4 (room with night vision)": 42464,
    "dD Investigation: Glass 5 (room with night vision)": 42465,
    "dD Investigation: Glass 6 (room with night vision)": 42466,
    "dD Investigation: Glass 7 (room with night vision)": 42467,
    "dD Investigation: Glass 8 (room with night vision)": 42468,
    "dD Investigation: Glass 1 (room near two scientists)": 42456,
    "dD Investigation: Glass 2 (room near two scientists)": 42457,
    "dD Investigation: Glass 3 (room near two scientists)": 42458,
    "dD Investigation: Glass 4 (room near two scientists)": 42459,
    "dD Investigation: Glass 1 (room with glass enclosure)": 42447,
    "dD Investigation: Glass 2 (room with glass enclosure)": 42446,
    "dD Investigation: Glass 3 (room with glass enclosure)": 42445,
    "dD Investigation: Glass on door 1 (sector 3 door)": 42391,
    "dD Investigation: Glass on door 2 (sector 3 door)": 42392,
    "dD Investigation: Glass 1 (big room near the end)": 42441,
    "dD Investigation: Glass 2 (big room near the end)": 42442,
    "dD Investigation: Glass 3 (big room near the end)": 42443,
    "dD Investigation: Glass 4 (big room near the end)": 42444,
    "dD Investigation: Glass 1 (right glass pillar of big room)": 42469,
    "dD Investigation: Glass 2 (right glass pillar of big room)": 42470,
    "dD Investigation: Glass 3 (right glass pillar of big room)": 42471,
    "dD Investigation: Glass 4 (right glass pillar of big room)": 42472,
    "dD Investigation: Glass 5 (right glass pillar of big room)": 42473,
    "dD Investigation: Glass 6 (right glass pillar of big room)": 42474,
    "dD Investigation: Glass 7 (right glass pillar of big room)": 42475,
    "dD Investigation: Glass 8 (right glass pillar of big room)": 42476,
    "dD Investigation: Glass 1 (front left glass pillar of big room)": 42485,
    "dD Investigation: Glass 2 (front left glass pillar of big room)": 42486,
    "dD Investigation: Glass 3 (front left glass pillar of big room)": 42487,
    "dD Investigation: Glass 4 (front left glass pillar of big room)": 42488,
    "dD Investigation: Glass 5 (front left glass pillar of big room)": 42489,
    "dD Investigation: Glass 6 (front left glass pillar of big room)": 42490,
    "dD Investigation: Glass 7 (front left glass pillar of big room)": 42491,
    "dD Investigation: Glass 8 (front left glass pillar of big room)": 42492,
    "dD Investigation: Glass 1 (back left glass pillar of big room)": 42477,
    "dD Investigation: Glass 2 (back left glass pillar of big room)": 42478,
    "dD Investigation: Glass 3 (back left glass pillar of big room)": 42479,
    "dD Investigation: Glass 4 (back left glass pillar of big room)": 42480,
    "dD Investigation: Glass 5 (back left glass pillar of big room)": 42481,
    "dD Investigation: Glass 6 (back left glass pillar of big room)": 42482,
    "dD Investigation: Glass 7 (back left glass pillar of big room)": 42483,
    "dD Investigation: Glass 8 (back left glass pillar of big room)": 42484,
    "Carrington Villa: Glass Bottle 1": 44240,
    "Carrington Villa: Glass Bottle 2": 44239,
    "Carrington Villa: Glass Bottle 3": 44238,
    "Carrington Villa: Glass Bottle 4": 44233,
    "Carrington Villa: Glass Bottle 5": 44234,
    "Carrington Villa: Glass Bottle 6": 44232,
    "Carrington Villa: Glass Bottle 7": 44230,
    "Carrington Villa: Glass Bottle 8": 44235,
    "Carrington Villa: Glass Bottle 9": 44229,
    "Carrington Villa: Glass Bottle 10": 44231,
    "Carrington Villa: Glass Bottle 11": 44236,
    "Carrington Villa: Glass Bottle 12": 44237,
    "Carrington Villa: Glass Bottle 13": 44244,
    "Carrington Villa: Glass Bottle 14": 44241,
    "Carrington Villa: Glass Bottle 15": 44242,
    "Carrington Villa: Glass Bottle 16": 44243,
    "Carrington Villa: Glass Bottle 17": 44245,
    "Carrington Villa: Glass Bottle 18": 44246,
    "Carrington Villa: Glass Bottle 19": 44247,
    "Carrington Villa: Glass Bottle 20": 44248,
    "Carrington Villa: Glass Bottle 21": 44250,
    "Carrington Villa: Glass Bottle 22": 44249,
    "Carrington Villa: Glass Bottle 23": 44251,
    "Carrington Villa: Glass Bottle 24": 44252,
    "Carrington Villa: Glass Bottle 25": 44253,
    "Carrington Villa: Glass Bottle 26": 44254,
    "Carrington Villa: Glass Bottle 27": 44255,
    "Carrington Villa: Glass Bottle 28": 44256,
    "Carrington Villa: Glass Bottle 29": 44257,
    "Carrington Villa: Glass Bottle 30": 44258,
    "Carrington Villa: Glass Bottle 31": 44259,
    "Carrington Villa: Glass Bottle 32": 44260,
    "Carrington Villa: Glass Bottle 33": 44261,
    "Carrington Villa: Glass Bottle 34": 44262,
    "Carrington Villa: Glass Bottle 35": 44263,
    "Carrington Villa: Glass Bottle 36": 44264,
    "Carrington Villa: Glass Bottle 37": 44276,
    "Carrington Villa: Glass Bottle 38": 44275,
    "Carrington Villa: Glass Bottle 39": 44274,
    "Carrington Villa: Glass Bottle 40": 44269,
    "Carrington Villa: Glass Bottle 41": 44270,
    "Carrington Villa: Glass Bottle 42": 44268,
    "Carrington Villa: Glass Bottle 43": 44266,
    "Carrington Villa: Glass Bottle 44": 44271,
    "Carrington Villa: Glass Bottle 45": 44265,
    "Carrington Villa: Glass Bottle 46": 44267,
    "Carrington Villa: Glass Bottle 47": 44272,
    "Carrington Villa: Glass Bottle 48": 44273,
    "Carrington Villa: Glass Bottle 49": 44280,
    "Carrington Villa: Glass Bottle 50": 44277,
    "Carrington Villa: Glass Bottle 51": 44278,
    "Carrington Villa: Glass Bottle 52": 44279,
    "Carrington Villa: Glass Bottle 53": 44281,
    "Carrington Villa: Glass Bottle 54": 44282,
    "Carrington Villa: Glass Bottle 55": 44297,
    "Carrington Villa: Glass Bottle 56": 44291,
    "Carrington Villa: Glass Bottle 57": 44296,
    "Carrington Villa: Glass Bottle 58": 44289,
    "Carrington Villa: Glass Bottle 59": 44290,
    "Carrington Villa: Glass Bottle 60": 44295,
    "Carrington Villa: Glass Bottle 61": 44292,
    "Carrington Villa: Glass Bottle 62": 44294,
    "Carrington Villa: Glass Bottle 63": 44293,
    "Carrington Villa: Glass Bottle 64": 44298,
    "Carrington Villa: Glass Bottle 65": 44299,
    "Carrington Villa: Glass Bottle 66": 44300,
    "Carrington Villa: Glass Bottle 67": 44288,
    "Carrington Villa: Glass Bottle 68": 44287,
    "Carrington Villa: Glass Bottle 69": 44285,
    "Carrington Villa: Glass Bottle 70": 44284,
    "Carrington Villa: Glass Bottle 71": 44283,
    "Carrington Villa: Glass Bottle 72": 44286,
    "Carrington Villa: Glass Bottle 73": 44325,
    "Carrington Villa: Glass Bottle 74": 44326,
    "Carrington Villa: Glass Bottle 75": 44327,
    "Carrington Villa: Glass Bottle 76": 44328,
    "Carrington Villa: Glass Bottle 77": 44329,
    "Carrington Villa: Glass Bottle 78": 44330,
    "Carrington Villa: Glass Bottle 79": 44331,
    "Carrington Villa: Glass Bottle 80": 44332,
    "Carrington Villa: Glass Bottle 81": 44333,
    "Carrington Villa: Glass Bottle 82": 44334,
    "Carrington Villa: Glass Bottle 83": 44335,
    "Carrington Villa: Glass Bottle 84": 44319,
    "Carrington Villa: Glass Bottle 85": 44320,
    "Carrington Villa: Glass Bottle 86": 44321,
    "Carrington Villa: Glass Bottle 87": 44322,
    "Carrington Villa: Glass Bottle 88": 44323,
    "Carrington Villa: Glass Bottle 89": 44324,
    "Carrington Villa: Glass Bottle 90": 44318,
    "Carrington Villa: Glass Bottle 91": 44317,
    "Carrington Villa: Glass Bottle 92": 44316,
    "Carrington Villa: Glass Bottle 93": 44311,
    "Carrington Villa: Glass Bottle 94": 44312,
    "Carrington Villa: Glass Bottle 95": 44310,
    "Carrington Villa: Glass Bottle 96": 44313,
    "Carrington Villa: Glass Bottle 97": 44308,
    "Carrington Villa: Glass Bottle 98": 44307,
    "Carrington Villa: Glass Bottle 99": 44314,
    "Carrington Villa: Glass Bottle 100": 44309,
    "Carrington Villa: Glass Bottle 101": 44315,
    "Carrington Villa: Glass Bottle 102": 44304,
    "Carrington Villa: Glass Bottle 103": 44301,
    "Carrington Villa: Glass Bottle 104": 44302,
    "Carrington Villa: Glass Bottle 105": 44303,
    "Carrington Villa: Glass Bottle 106": 44305,
    "Carrington Villa: Glass Bottle 107": 44306,
    "Chicago: Glass 1 (above stacked barrels)": 46291,
    "Chicago: Glass 2 (above stacked barrels)": 46292,
    "Chicago: Glass 3 (above stacked barrels)": 46293,
    "G5 Building: Glass (first room)": 48190,
    "G5 Building: Glass 1 (2nd cloak guards room)": 48192,
    "G5 Building: Glass 2 (2nd cloak guards room)": 48193,
    "G5 Building: Door Glass 1 (1st door with glass)": 48156,
    "G5 Building: Door Glass 2 (1st door with glass)": 48157,
    "G5 Building: Door Glass 1 (2nd door with glass)": 48164,
    "G5 Building: Door Glass 2 (2nd door with glass)": 48165,
    "G5 Building: Door Glass 1 (3rd door with glass)": 48162,
    "G5 Building: Door Glass 2 (3rd door with glass)": 48163,
    "G5 Building: Door Glass 1 (4th door with glass)": 48166,
    "G5 Building: Door Glass 2 (4th door with glass)": 48167,
    "G5 Building: Door Glass 1 (5th door with glass)": 48170,
    "G5 Building: Door Glass 2 (5th door with glass)": 48171,
    "G5 Building: Door Glass 1 (6th door with glass)": 48172,
    "G5 Building: Door Glass 2 (6th door with glass)": 48173,
    "G5 Building: Door Glass 1 (7th door with glass)": 48168,
    "G5 Building: Door Glass 2 (7th door with glass)": 48169,
    "G5 Building: Door Glass 1 (8th door with glass)": 48179,
    "G5 Building: Door Glass 2 (8th door with glass)": 48180,
    "Rescue/Escape/Maian SOS: Glass on door 1": 50646,
    "Rescue/Escape/Maian SOS: Glass on door 2": 50649,
    "Rescue/Escape/Maian SOS: Glass on medlab door": 50680,
    "Rescue/Maian SOS: Glass 1 (in medlab)": 51078,
    "Rescue/Maian SOS: Glass 2 (in medlab)": 51079,
    "Rescue/Maian SOS: Glass 3 (in medlab)": 51080,
    "Maian SOS: Glass 1 (first room)": 51081,
    "Maian SOS: Glass 2 (first room)": 51082,
    "Maian SOS: Glass 3 (first room)": 51083,
    "A51 Escape: Glass (near locked medical containment door)": 51084,
    "A51 Escape: Glass on door (locked medical containment door)": 50612,
    "Air Base: Window (suitcase room)": 52491,
    "Air Base: Window (near security monitor)": 52494,
    "Air Base: Window (near escalator)": 52500,
    "Air Base: Window 1 (next to flight plans room)": 52495,
    "Air Base: Window 2 (next to flight plans room)": 52498,
    "Air Base: Window (in front of plane)": 52501,
    "Air Base: Window 1 (near flight plans)": 52496,
    "Air Base: Window 2 (near flight plans)": 52497,
    "Pelagic II: Glass on Door (1st door)": 54244,
    "Pelagic II: Glass on Door (2nd door)": 54271,
    "Pelagic II: Glass on Door (3rd door)": 54243,
    "Pelagic II: Glass on Door (4th door)": 54272,
    "Pelagic II: Glass on Door (5th door)": 54273,
    "Pelagic II: Glass on Door (6th door)": 54270,
    "Pelagic II: Glass on Door (7th door)": 54268,
    "Pelagic II: Glass on Door (8th door)": 54267,
    "Pelagic II: Glass on Door (9th door)": 54269,
    "Pelagic II: Glass on Door (10th door)": 54248,
    "Pelagic II: Glass on Door (15th door)": 54276,
    "Pelagic II: Glass on Door (16th door)": 54275,
    "Pelagic II: Glass on Door (17th door)": 54277,
    "Pelagic II: Glass on Door (18th door)": 54280,
    "Pelagic II: Glass on Door (19th door)": 54281,
    "Pelagic II: Glass on Door (20th door)": 54284,
    "Pelagic II: Glass on Door (21th door)": 54283,
    "Pelagic II: Glass on Door (22nd door)": 54282,
    "Pelagic II: Glass on Door (23rd door)": 54279,
    "Pelagic II: Glass on Door (24th door)": 54247,
    "Pelagic II: Glass on Door (25th door)": 54278,
    "Pelagic II: Glass on Door (near the end)": 54255,
    "Pelagic II: Glass on Door (11th door)": 54253,
    "Pelagic II: Glass on Door (12th door)": 54260,
    "Pelagic II: Glass on Door (13th door)": 54261,
    "Pelagic II: Glass on Door (14th door)": 54254,
    "Pelagic II: Glass on Door 1 (lower floors)": 54242,
    "Pelagic II: Glass on Door 2 (lower floors)": 54265,
    "Pelagic II: Glass on Door 3 (lower floors)": 54264,
    "Pelagic II: Glass on Door 4 (lower floors)": 54262,
    "Pelagic II: Glass on Door 5 (lower floors)": 54263,
    "Pelagic II: Glass on Door 6 (lower floors)": 54241,
    "Pelagic II: Glass on Door 7 (lower floors)": 54240,
    "Pelagic II: Glass on Door 1 (near research tapes)": 54249,
    "Pelagic II: Glass on Door 2 (near research tapes)": 54250,
    "Deep Sea: Glass 1 (1st power node)": 56515,
    "Deep Sea: Glass 2 (1st power node)": 56516,
    "Deep Sea: Glass 3 (1st power node)": 56517,
    "Deep Sea: Glass 1 (2nd power node)": 56518,
    "Deep Sea: Glass 2 (2nd power node)": 56519,
    "Deep Sea: Glass 3 (2nd power node)": 56520,
    "Deep Sea: Glass 1 (3rd power node)": 56521,
    "Deep Sea: Glass 2 (3rd power node)": 56522,
    "Deep Sea: Glass 3 (3rd power node)": 56523,
    "Deep Sea: Glass 1 (4th power node)": 56524,
    "Deep Sea: Glass 2 (4th power node)": 56525,
    "Deep Sea: Glass 3 (4th power node)": 56526,
    "Deep Sea: Glass 1 (5th power node)": 56527,
    "Deep Sea: Glass 2 (5th power node)": 56528,
    "Deep Sea: Glass 3 (5th power node)": 56529,
    "Deep Sea: Glass 1 (6th power node)": 56530,
    "Deep Sea: Glass 2 (6th power node)": 56531,
    "Deep Sea: Glass 3 (6th power node)": 56532,
    "Deep Sea: Glass 4 (6th power node)": 56533,
    "Deep Sea: Glass 5 (6th power node)": 56534,
    "Deep Sea: Glass 6 (6th power node)": 56535,
    "Deep Sea: Glass 7 (6th power node)": 56536,
    "Deep Sea: Glass 8 (6th power node)": 56537,
    "Deep Sea: Glass 9 (6th power node)": 56538,
    "Deep Sea: Glass 10 (6th power node)": 56539,
    "Deep Sea: Glass 11 (6th power node)": 56540,
    "Deep Sea: Glass 12 (6th power node)": 56541,
    "Deep Sea: Glass 1 (7th power node)": 56542,
    "Deep Sea: Glass 2 (7th power node)": 56543,
    "Deep Sea: Glass 3 (7th power node)": 56544,
    "Deep Sea: Glass 4 (7th power node)": 56545,
    "Deep Sea: Glass 5 (7th power node)": 56546,
    "Deep Sea: Glass 6 (7th power node)": 56547,
    "Deep Sea: Glass 7 (7th power node)": 56548,
    "Deep Sea: Glass 8 (7th power node)": 56549,
    "Deep Sea: Glass 9 (7th power node)": 56550,
    "Deep Sea: Glass 10 (7th power node)": 56551,
    "Deep Sea: Glass 11 (7th power node)": 56552,
    "Deep Sea: Glass 12 (7th power node)": 56553,
    "Deep Sea: Glass 1 (8th power node)": 56554,
    "Deep Sea: Glass 2 (8th power node)": 56555,
    "Deep Sea: Glass 3 (8th power node)": 56556,
    "Deep Sea: Glass 4 (8th power node)": 56557,
    "Deep Sea: Glass 5 (8th power node)": 56558,
    "Deep Sea: Glass 6 (8th power node)": 56559,
    "Deep Sea: Glass 7 (8th power node)": 56560,
    "Deep Sea: Glass 8 (8th power node)": 56561,
    "Deep Sea: Glass 9 (8th power node)": 56562,
    "Deep Sea: Glass 10 (8th power node)": 56563,
    "Deep Sea: Glass 11 (8th power node)": 56564,
    "Deep Sea: Glass 12 (8th power node)": 56565,
    "Deep Sea: Glass 1 (9th power node)": 56566,
    "Deep Sea: Glass 2 (9th power node)": 56567,
    "Deep Sea: Glass 3 (9th power node)": 56568,
    "Deep Sea: Glass 4 (9th power node)": 56569,
    "Deep Sea: Glass 5 (9th power node)": 56570,
    "Deep Sea: Glass 6 (9th power node)": 56571,
    "Deep Sea: Glass 7 (9th power node)": 56572,
    "Deep Sea: Glass 8 (9th power node)": 56573,
    "Deep Sea: Glass 9 (9th power node)": 56574,
    "Deep Sea: Glass 10 (9th power node)": 56575,
    "Deep Sea: Glass 11 (9th power node)": 56576,
    "Deep Sea: Glass 12 (9th power node)": 56577,
    "Deep Sea: Glass 1 (10th power node)": 56578,
    "Deep Sea: Glass 2 (10th power node)": 56579,
    "Deep Sea: Glass 3 (10th power node)": 56580,
    "Deep Sea: Glass 4 (10th power node)": 56581,
    "Deep Sea: Glass 5 (10th power node)": 56582,
    "Deep Sea: Glass 6 (10th power node)": 56583,
    "Deep Sea: Glass 7 (10th power node)": 56584,
    "Deep Sea: Glass 8 (10th power node)": 56585,
    "Deep Sea: Glass 9 (10th power node)": 56586,
    "Deep Sea: Glass 10 (10th power node)": 56587,
    "Deep Sea: Glass 11 (10th power node)": 56588,
    "Deep Sea: Glass 12 (10th power node)": 56589,
    "Deep Sea: Glass 1 (11th power node)": 56590,
    "Deep Sea: Glass 2 (11th power node)": 56591,
    "Deep Sea: Glass 3 (11th power node)": 56592,
    "Deep Sea: Glass 4 (11th power node)": 56593,
    "Deep Sea: Glass 5 (11th power node)": 56594,
    "Deep Sea: Glass 6 (11th power node)": 56595,
    "Deep Sea: Glass 7 (11th power node)": 56596,
    "Deep Sea: Glass 8 (11th power node)": 56597,
    "Deep Sea: Glass 9 (11th power node)": 56598,
    "Deep Sea: Glass 10 (11th power node)": 56599,
    "Deep Sea: Glass 11 (11th power node)": 56600,
    "Deep Sea: Glass 12 (11th power node)": 56601,
    "Deep Sea: Glass 1 (12th power node)": 56602,
    "Deep Sea: Glass 2 (12th power node)": 56603,
    "Deep Sea: Glass 3 (12th power node)": 56604,
    "Deep Sea: Glass 4 (12th power node)": 56605,
    "Deep Sea: Glass 5 (12th power node)": 56606,
    "Deep Sea: Glass 6 (12th power node)": 56607,
    "Deep Sea: Glass 7 (12th power node)": 56608,
    "Deep Sea: Glass 8 (12th power node)": 56609,
    "Deep Sea: Glass 9 (12th power node)": 56610,
    "Deep Sea: Glass 10 (12th power node)": 56611,
    "Deep Sea: Glass 11 (12th power node)": 56612,
    "Deep Sea: Glass 12 (12th power node)": 56613,
    "CI Defense: 1F Glass Railing": 58465,
    "CI Defense: Basement Glass on Door 1": 58387,
    "CI Defense: Basement Glass on Door 2": 58388,
    "CI Defense: Basement Glass Railing 1": 58451,
    "CI Defense: Basement Glass Railing 2": 58439,
    "CI Defense: Basement Glass Railing 3": 58441,
    "CI Defense: Basement Glass Railing 4": 58440,
    "CI Defense: Basement Glass Railing 5": 58442,
    "CI Defense: Basement Glass Railing 6": 58443,
    "CI Defense: Basement Glass Railing 7": 58444,
    "CI Defense: Basement Glass Railing 8": 58447,
    "CI Defense: Basement Glass Railing 9": 58445,
    "CI Defense: Basement Glass Railing 10": 58446,
    "CI Defense: Basement Glass on Door 1 (2nd door)": 58360,
    "CI Defense: Basement Glass on Door 2 (2nd door)": 58361,
    "CI Defense: Basement Glass on Door 1 (3rd door)": 58362,
    "CI Defense: Basement Glass on Door 2 (3rd door)": 58363,
    "CI Defense: Basement Glass on Door 1 (4th door)": 58364,
    "CI Defense: Basement Glass on Door 2 (4th door)": 58365,
    "CI Defense: Basement Glass on Door 1 (5th door)": 58366,
    "CI Defense: Basement Glass on Door 2 (5th door)": 58367,
    "CI Defense: Basement Glass on Door 1 (6th door)": 58368,
    "CI Defense: Basement Glass on Door 2 (6th door)": 58369,
    "CI Defense: Basement Glass on Door 1 (7th door)": 58370,
    "CI Defense: Basement Glass on Door 2 (7th door)": 58371,
    "CI Defense: Basement Glass on Door 1 (8th door)": 58372,
    "CI Defense: Basement Glass on Door 2 (8th door)": 58373,
    "CI Defense: Basement Glass on Door 1 (9th door)": 58381,
    "CI Defense: Basement Glass on Door 2 (9th door)": 58382,
    "CI Defense: Basement Glass on Door 1 (10th door)": 58383,
    "CI Defense: Basement Glass on Door 2 (10th door)": 58384,
    "CI Defense: Basement Glass on Door 1 (11th door)": 58376,
    "CI Defense: Basement Glass on Door 2 (11th door)": 58377,
    "CI Defense: Basement Glass on Door 1 (12th door)": 58374,
    "CI Defense: Basement Glass on Door 2 (12th door)": 58375,
    "CI Defense: Basement Glass on Door 1 (13th door)": 58379,
    "CI Defense: Basement Glass on Door 2 (13th door)": 58380,
    "CI Defense: Firing Range Glass 1": 58464,
    "CI Defense: Firing Range Glass 2": 58463,
    "CI Defense: Firing Range Glass 3": 58458,
    "CI Defense: Firing Range Glass 4": 58457,
    "CI Defense: Firing Range Glass 5": 58456,
    "CI Defense: Firing Range Glass 6": 58460,
    "CI Defense: Firing Range Glass 7": 58461,
    "CI Defense: Firing Range Glass 8": 58459,
    "CI Defense: Firing Range RC-P120 Glass": 58462,
    "CI Defense: Firing Range Ceiling Glass 1": 58420,
    "CI Defense: Firing Range Ceiling Glass 2": 58421,
    "CI Defense: Firing Range Ceiling Glass 3": 58423,
    "CI Defense: Firing Range Ceiling Glass 4": 58422,
    "CI Defense: Device Lab Glass 1": 58418,
    "CI Defense: Device Lab Glass 2": 58419,
    "CI Defense: Info Room Glass 1": 58416,
    "CI Defense: Info Room Glass 2": 58417,
    "CI Defense: Joanna's Office Glass 1": 58412,
    "CI Defense: Joanna's Office Glass 2": 58413,
    "CI Defense: Carrington's Office Glass 1": 58414,
    "CI Defense: Carrington's Office Glass 2": 58415,
    "Attack Ship: Engine System Glass 1": 60413,
    "Attack Ship: Engine System Glass 2": 60414,
    "Attack Ship: Engine System Glass 3": 60415,
    "Attack Ship: Engine System Glass 4": 60416,
    "Attack Ship: Engine System Glass 5": 60417,
    "Attack Ship: Engine System Glass 6": 60418,
}

class PerfectDarkLocation(Location):
    game = "Perfect Dark"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: PerfectDarkWorld) -> None:
    create_regular_locations(world)


def create_regular_locations(world: PerfectDarkWorld) -> None:
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
    dd_central = world.get_region("dataDyne Central")
    inner_a51 = world.get_region("Inner Area 51")

    institute_locations_list = []
    defection_locations_list = []
    investigation_locations_list = []
    extraction_locations_list = []
    villa_locations_list = []
    chicago_locations_list = []
    g5_locations_list = []
    infiltration_locations_list = []
    rescue_locations_list = []
    escape_locations_list = []
    airbase_locations_list = []
    afo_locations_list = []
    crashsite_locations_list = []
    pelagic_locations_list = []
    deepsea_locations_list = []
    defense_locations_list = []
    attackship_locations_list = []
    skedarruins_locations_list = []
    mbr_locations_list = []
    maiansos_locations_list = []
    war_locations_list = []
    duel_locations_list = []
    dd_central_locations_list = []
    inner_a51_locations_list = []
    

    # Missions
    if world.options.agent:
        if "dD Defection" not in world.options.excluded_missions:
            defection_locations_list.append("dD Defection - Agent Objective 1")
            defection_locations_list.append("Complete: dD Defection - Agent")

        if "dD Investigation" not in world.options.excluded_missions:
            investigation_locations_list.append("dD Investigation - Agent Objective 1")
            investigation_locations_list.append("dD Investigation - Agent Objective 2")
            investigation_locations_list.append("Complete: dD Investigation - Agent")

        if "dD Extraction" not in world.options.excluded_missions:
            extraction_locations_list.append("dD Extraction - Agent Objective 1")
            extraction_locations_list.append("dD Extraction - Agent Objective 2")
            extraction_locations_list.append("dD Extraction - Agent Objective 3")
            extraction_locations_list.append("Complete: dD Extraction - Agent")

        if "Carrington Villa" not in world.options.excluded_missions:
            villa_locations_list.append("Carrington Villa - Agent Objective 1")
            villa_locations_list.append("Carrington Villa - Agent Objective 2")
            villa_locations_list.append("Carrington Villa - Agent Objective 3")
            villa_locations_list.append("Complete: Carrington Villa - Agent")

        if "Chicago" not in world.options.excluded_missions:
            chicago_locations_list.append("Chicago - Agent Objective 1")
            chicago_locations_list.append("Chicago - Agent Objective 2")
            chicago_locations_list.append("Chicago - Agent Objective 3")
            chicago_locations_list.append("Complete: Chicago - Agent")

        if "G5 Building" not in world.options.excluded_missions:
            g5_locations_list.append("G5 Building - Agent Objective 1")
            g5_locations_list.append("G5 Building - Agent Objective 2")
            g5_locations_list.append("G5 Building - Agent Objective 3")
            g5_locations_list.append("Complete: G5 Building - Agent")

        if "A51 Infiltration" not in world.options.excluded_missions:
            infiltration_locations_list.append("A51 Infiltration - Agent Objective 1")
            infiltration_locations_list.append("A51 Infiltration - Agent Objective 2")
            infiltration_locations_list.append("A51 Infiltration - Agent Objective 3")
            infiltration_locations_list.append("Complete: A51 Infiltration - Agent")

        if "A51 Rescue" not in world.options.excluded_missions:
            rescue_locations_list.append("A51 Rescue - Agent Objective 1")
            rescue_locations_list.append("A51 Rescue - Agent Objective 2")
            rescue_locations_list.append("A51 Rescue - Agent Objective 3")
            rescue_locations_list.append("Complete: A51 Rescue - Agent")

        if "A51 Escape" not in world.options.excluded_missions:
            escape_locations_list.append("A51 Escape - Agent Objective 1")
            escape_locations_list.append("A51 Escape - Agent Objective 2")
            escape_locations_list.append("A51 Escape - Agent Objective 3")
            escape_locations_list.append("Complete: A51 Escape - Agent")

        if "Air Base" not in world.options.excluded_missions:
            airbase_locations_list.append("Air Base - Agent Objective 1")
            airbase_locations_list.append("Air Base - Agent Objective 2")
            airbase_locations_list.append("Air Base - Agent Objective 3")
            airbase_locations_list.append("Complete: Air Base - Agent")

        if "Air Force One" not in world.options.excluded_missions:
            afo_locations_list.append("Air Force One - Agent Objective 1")
            afo_locations_list.append("Air Force One - Agent Objective 2")
            afo_locations_list.append("Air Force One - Agent Objective 3")
            afo_locations_list.append("Complete: Air Force One - Agent")

        if "Crash Site" not in world.options.excluded_missions:
            crashsite_locations_list.append("Crash Site - Agent Objective 1")
            crashsite_locations_list.append("Crash Site - Agent Objective 2")
            crashsite_locations_list.append("Crash Site - Agent Objective 3")
            crashsite_locations_list.append("Complete: Crash Site - Agent")

        if "Pelagic II" not in world.options.excluded_missions:
            pelagic_locations_list.append("Pelagic II - Agent Objective 1")
            pelagic_locations_list.append("Pelagic II - Agent Objective 2")
            pelagic_locations_list.append("Pelagic II - Agent Objective 3")
            pelagic_locations_list.append("Complete: Pelagic II - Agent")

        if "Deep Sea" not in world.options.excluded_missions:
            deepsea_locations_list.append("Deep Sea - Agent Objective 1")
            deepsea_locations_list.append("Deep Sea - Agent Objective 2")
            deepsea_locations_list.append("Deep Sea - Agent Objective 3")
            deepsea_locations_list.append("Complete: Deep Sea - Agent")

        if "CI Defense" not in world.options.excluded_missions:
            defense_locations_list.append("CI Defense - Agent Objective 1")
            defense_locations_list.append("CI Defense - Agent Objective 2")
            defense_locations_list.append("CI Defense - Agent Objective 3")
            defense_locations_list.append("Complete: CI Defense - Agent")

        if "Attack Ship" not in world.options.excluded_missions:
            attackship_locations_list.append("Attack Ship - Agent Objective 1")
            attackship_locations_list.append("Attack Ship - Agent Objective 2")
            attackship_locations_list.append("Attack Ship - Agent Objective 3")
            attackship_locations_list.append("Complete: Attack Ship - Agent")

        if ("Skedar Ruins" not in world.options.excluded_missions
                or world.options.goal.value == Goal.option_complete_skedar_ruins):
            skedarruins_locations_list.append("Skedar Ruins - Agent Objective 1")
            skedarruins_locations_list.append("Skedar Ruins - Agent Objective 2")
            skedarruins_locations_list.append("Skedar Ruins - Agent Objective 3")
            skedarruins_locations_list.append("Complete: Skedar Ruins - Agent")

        if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
            mbr_locations_list.append("Mr. Blonde's Revenge - Agent Objective 1")
            mbr_locations_list.append("Complete: Mr. Blonde's Revenge - Agent")

        if "Maian SOS" not in world.options.excluded_missions:
            maiansos_locations_list.append("Maian SOS - Agent Objective 1")
            maiansos_locations_list.append("Complete: Maian SOS - Agent")
        
        if "WAR!" not in world.options.excluded_missions:
            war_locations_list.append("WAR! - Agent Objective 1")
            war_locations_list.append("Complete: WAR! - Agent")
        
        if "The Duel" not in world.options.excluded_missions:
            duel_locations_list.append("The Duel - Agent Objective 1")
            duel_locations_list.append("Complete: The Duel - Agent")

        if world.options.alternate_exits.value == AlternateExits.option_one:
            g5_building_exits = [
                "Complete G5 Building (Agent): Bottom Exit",
                "Complete G5 Building (Agent): Upper Exit"
            ]

            escape_exits = [
                "Complete A51 Escape (Agent): UFO Escape",
                "Complete A51 Escape (Agent): Alternate Escape"
            ]

            air_base_exits = [
                "Complete Air Base (Agent): Shuttle Exit",
                "Complete Air Base (Agent): Ladder Exit"
            ]

            if (((world.options.special_agent or world.options.perfect_agent) and "Chicago" not in world.options.excluded_missions)
                    or world.options.weapon_progression.value >= WeaponProgression.option_all_guns) \
                    and "G5 Building" not in world.options.excluded_missions:
                g5_item = world.random.choice(g5_building_exits)
                g5_locations_list.append(g5_item)

            if "A51 Escape" not in world.options.excluded_missions:
                escape_item = world.random.choice(escape_exits)
                escape_locations_list.append(escape_item)

            if "Air Base" not in world.options.excluded_missions:
                air_base_item = world.random.choice(air_base_exits)
                airbase_locations_list.append(air_base_item)
            
        elif world.options.alternate_exits.value == AlternateExits.option_all:
            if (((world.options.special_agent or world.options.perfect_agent) and "Chicago" not in world.options.excluded_missions)
                    or world.options.weapon_progression.value >= WeaponProgression.option_all_guns) \
                    and "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("Complete G5 Building (Agent): Bottom Exit")
                g5_locations_list.append("Complete G5 Building (Agent): Upper Exit")

            if "A51 Escape" not in world.options.excluded_missions:
                escape_locations_list.append("Complete A51 Escape (Agent): UFO Escape")
                escape_locations_list.append("Complete A51 Escape (Agent): Alternate Escape")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Complete Air Base (Agent): Shuttle Exit")
                airbase_locations_list.append("Complete Air Base (Agent): Ladder Exit")


    if world.options.special_agent:
        if "dD Defection" not in world.options.excluded_missions:
            defection_locations_list.append("dD Defection - Special Agent Objective 1")
            defection_locations_list.append("dD Defection - Special Agent Objective 2")
            defection_locations_list.append("dD Defection - Special Agent Objective 3")
            defection_locations_list.append("dD Defection - Special Agent Objective 4")
            defection_locations_list.append("Complete: dD Defection - Special Agent")

        if "dD Investigation" not in world.options.excluded_missions:
            investigation_locations_list.append("dD Investigation - Special Agent Objective 1")
            investigation_locations_list.append("dD Investigation - Special Agent Objective 2")
            investigation_locations_list.append("dD Investigation - Special Agent Objective 3")
            investigation_locations_list.append("dD Investigation - Special Agent Objective 4")
            investigation_locations_list.append("Complete: dD Investigation - Special Agent")

        if "dD Extraction" not in world.options.excluded_missions:
            extraction_locations_list.append("dD Extraction - Special Agent Objective 1")
            extraction_locations_list.append("dD Extraction - Special Agent Objective 2")
            extraction_locations_list.append("dD Extraction - Special Agent Objective 3")
            extraction_locations_list.append("dD Extraction - Special Agent Objective 4")
            extraction_locations_list.append("Complete: dD Extraction - Special Agent")

        if "Carrington Villa" not in world.options.excluded_missions:
            villa_locations_list.append("Carrington Villa - Special Agent Objective 1")
            villa_locations_list.append("Carrington Villa - Special Agent Objective 2")
            villa_locations_list.append("Carrington Villa - Special Agent Objective 3")
            villa_locations_list.append("Carrington Villa - Special Agent Objective 4")
            villa_locations_list.append("Complete: Carrington Villa - Special Agent")

        if "Chicago" not in world.options.excluded_missions:
            chicago_locations_list.append("Chicago - Special Agent Objective 1")
            chicago_locations_list.append("Chicago - Special Agent Objective 2")
            chicago_locations_list.append("Chicago - Special Agent Objective 3")
            chicago_locations_list.append("Chicago - Special Agent Objective 4")
            chicago_locations_list.append("Complete: Chicago - Special Agent")

        if "G5 Building" not in world.options.excluded_missions:
            g5_locations_list.append("G5 Building - Special Agent Objective 1")
            g5_locations_list.append("G5 Building - Special Agent Objective 2")
            g5_locations_list.append("G5 Building - Special Agent Objective 3")
            g5_locations_list.append("G5 Building - Special Agent Objective 4")
            g5_locations_list.append("Complete: G5 Building - Special Agent")

        if "A51 Infiltration" not in world.options.excluded_missions:
            infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 1")
            infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 2")
            infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 3")
            infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 4")
            infiltration_locations_list.append("Complete: A51 Infiltration - Special Agent")

        if "A51 Rescue" not in world.options.excluded_missions:
            rescue_locations_list.append("A51 Rescue - Special Agent Objective 1")
            rescue_locations_list.append("A51 Rescue - Special Agent Objective 2")
            rescue_locations_list.append("A51 Rescue - Special Agent Objective 3")
            rescue_locations_list.append("A51 Rescue - Special Agent Objective 4")
            rescue_locations_list.append("Complete: A51 Rescue - Special Agent")

        if "A51 Escape" not in world.options.excluded_missions:
            escape_locations_list.append("A51 Escape - Special Agent Objective 1")
            escape_locations_list.append("A51 Escape - Special Agent Objective 2")
            escape_locations_list.append("A51 Escape - Special Agent Objective 3")
            escape_locations_list.append("A51 Escape - Special Agent Objective 4")
            escape_locations_list.append("Complete: A51 Escape - Special Agent")

        if "Air Base" not in world.options.excluded_missions:
            airbase_locations_list.append("Air Base - Special Agent Objective 1")
            airbase_locations_list.append("Air Base - Special Agent Objective 2")
            airbase_locations_list.append("Air Base - Special Agent Objective 3")
            airbase_locations_list.append("Air Base - Special Agent Objective 4")
            airbase_locations_list.append("Complete: Air Base - Special Agent")

        if "Air Force One" not in world.options.excluded_missions:
            afo_locations_list.append("Air Force One - Special Agent Objective 1")
            afo_locations_list.append("Air Force One - Special Agent Objective 2")
            afo_locations_list.append("Air Force One - Special Agent Objective 3")
            afo_locations_list.append("Air Force One - Special Agent Objective 4")
            afo_locations_list.append("Complete: Air Force One - Special Agent")

        if "Crash Site" not in world.options.excluded_missions:
            crashsite_locations_list.append("Crash Site - Special Agent Objective 1")
            crashsite_locations_list.append("Crash Site - Special Agent Objective 2")
            crashsite_locations_list.append("Crash Site - Special Agent Objective 3")
            crashsite_locations_list.append("Crash Site - Special Agent Objective 4")
            crashsite_locations_list.append("Complete: Crash Site - Special Agent")

        if "Pelagic II" not in world.options.excluded_missions:
            pelagic_locations_list.append("Pelagic II - Special Agent Objective 1")
            pelagic_locations_list.append("Pelagic II - Special Agent Objective 2")
            pelagic_locations_list.append("Pelagic II - Special Agent Objective 3")
            pelagic_locations_list.append("Pelagic II - Special Agent Objective 4")
            pelagic_locations_list.append("Complete: Pelagic II - Special Agent")

        if "Deep Sea" not in world.options.excluded_missions:
            deepsea_locations_list.append("Deep Sea - Special Agent Objective 1")
            deepsea_locations_list.append("Deep Sea - Special Agent Objective 2")
            deepsea_locations_list.append("Deep Sea - Special Agent Objective 3")
            deepsea_locations_list.append("Deep Sea - Special Agent Objective 4")
            deepsea_locations_list.append("Complete: Deep Sea - Special Agent")

        if "CI Defense" not in world.options.excluded_missions:
            defense_locations_list.append("CI Defense - Special Agent Objective 1")
            defense_locations_list.append("CI Defense - Special Agent Objective 2")
            defense_locations_list.append("CI Defense - Special Agent Objective 3")
            defense_locations_list.append("CI Defense - Special Agent Objective 4")
            defense_locations_list.append("Complete: CI Defense - Special Agent")

        if "Attack Ship" not in world.options.excluded_missions:
            attackship_locations_list.append("Attack Ship - Special Agent Objective 1")
            attackship_locations_list.append("Attack Ship - Special Agent Objective 2")
            attackship_locations_list.append("Attack Ship - Special Agent Objective 3")
            attackship_locations_list.append("Attack Ship - Special Agent Objective 4")
            attackship_locations_list.append("Complete: Attack Ship - Special Agent")

        if ("Skedar Ruins" not in world.options.excluded_missions
                or world.options.goal.value == Goal.option_complete_skedar_ruins):
            skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 1")
            skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 2")
            skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 3")
            skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 4")
            skedarruins_locations_list.append("Complete: Skedar Ruins - Special Agent")

        if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
            mbr_locations_list.append("Mr. Blonde's Revenge - Special Agent Objective 1")
            mbr_locations_list.append("Mr. Blonde's Revenge - Special Agent Objective 2")
            mbr_locations_list.append("Complete: Mr. Blonde's Revenge - Special Agent")

        if "Maian SOS" not in world.options.excluded_missions:
            maiansos_locations_list.append("Maian SOS - Special Agent Objective 1")
            maiansos_locations_list.append("Maian SOS - Special Agent Objective 2")
            maiansos_locations_list.append("Complete: Maian SOS - Special Agent")

        if "WAR!" not in world.options.excluded_missions:
            war_locations_list.append("WAR! - Special Agent Objective 1")
            war_locations_list.append("WAR! - Special Agent Objective 2")
            war_locations_list.append("Complete: WAR! - Special Agent")

        if "The Duel" not in world.options.excluded_missions:
            duel_locations_list.append("The Duel - Special Agent Objective 1")
            duel_locations_list.append("The Duel - Special Agent Objective 2")
            duel_locations_list.append("Complete: The Duel - Special Agent")

        if world.options.alternate_exits.value == AlternateExits.option_one:
            g5_building_exits = [
                "Complete G5 Building (Special Agent): Bottom Exit",
                "Complete G5 Building (Special Agent): Upper Exit"
            ]

            escape_exits = [
                "Complete A51 Escape (Special Agent): UFO Escape",
                "Complete A51 Escape (Special Agent): Alternate Escape"
            ]

            air_base_exits = [
                "Complete Air Base (Special Agent): Shuttle Exit",
                "Complete Air Base (Special Agent): Ladder Exit"
            ]

            if "G5 Building" not in world.options.excluded_missions:
                g5_item = world.random.choice(g5_building_exits)
                g5_locations_list.append(g5_item)

            if "A51 Escape" not in world.options.excluded_missions:
                escape_item = world.random.choice(escape_exits)
                escape_locations_list.append(escape_item)

            if "Air Base" not in world.options.excluded_missions:
                air_base_item = world.random.choice(air_base_exits)
                airbase_locations_list.append(air_base_item)
            
        elif world.options.alternate_exits.value == AlternateExits.option_all:
            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("Complete G5 Building (Special Agent): Bottom Exit")
                g5_locations_list.append("Complete G5 Building (Special Agent): Upper Exit")

            if "A51 Escape" not in world.options.excluded_missions:
                escape_locations_list.append("Complete A51 Escape (Special Agent): UFO Escape")
                escape_locations_list.append("Complete A51 Escape (Special Agent): Alternate Escape")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Complete Air Base (Special Agent): Shuttle Exit")
                airbase_locations_list.append("Complete Air Base (Special Agent): Ladder Exit")


    if world.options.perfect_agent:
        if "dD Defection" not in world.options.excluded_missions:
            defection_locations_list.append("dD Defection - Perfect Agent Objective 1")
            defection_locations_list.append("dD Defection - Perfect Agent Objective 2")
            defection_locations_list.append("dD Defection - Perfect Agent Objective 3")
            defection_locations_list.append("dD Defection - Perfect Agent Objective 4")
            defection_locations_list.append("dD Defection - Perfect Agent Objective 5")
            defection_locations_list.append("Complete: dD Defection - Perfect Agent")

        if "dD Investigation" not in world.options.excluded_missions:
            investigation_locations_list.append("dD Investigation - Perfect Agent Objective 1")
            investigation_locations_list.append("dD Investigation - Perfect Agent Objective 2")
            investigation_locations_list.append("dD Investigation - Perfect Agent Objective 3")
            investigation_locations_list.append("dD Investigation - Perfect Agent Objective 4")
            investigation_locations_list.append("dD Investigation - Perfect Agent Objective 5")
            investigation_locations_list.append("Complete: dD Investigation - Perfect Agent")

        if "dD Extraction" not in world.options.excluded_missions:
            extraction_locations_list.append("dD Extraction - Perfect Agent Objective 1")
            extraction_locations_list.append("dD Extraction - Perfect Agent Objective 2")
            extraction_locations_list.append("dD Extraction - Perfect Agent Objective 3")
            extraction_locations_list.append("dD Extraction - Perfect Agent Objective 4")
            extraction_locations_list.append("dD Extraction - Perfect Agent Objective 5")
            extraction_locations_list.append("Complete: dD Extraction - Perfect Agent")

        if "Carrington Villa" not in world.options.excluded_missions:
            villa_locations_list.append("Carrington Villa - Perfect Agent Objective 1")
            villa_locations_list.append("Carrington Villa - Perfect Agent Objective 2")
            villa_locations_list.append("Carrington Villa - Perfect Agent Objective 3")
            villa_locations_list.append("Carrington Villa - Perfect Agent Objective 4")
            villa_locations_list.append("Carrington Villa - Perfect Agent Objective 5")
            villa_locations_list.append("Complete: Carrington Villa - Perfect Agent")

        if "Chicago" not in world.options.excluded_missions:
            chicago_locations_list.append("Chicago - Perfect Agent Objective 1")
            chicago_locations_list.append("Chicago - Perfect Agent Objective 2")
            chicago_locations_list.append("Chicago - Perfect Agent Objective 3")
            chicago_locations_list.append("Chicago - Perfect Agent Objective 4")
            chicago_locations_list.append("Chicago - Perfect Agent Objective 5")
            chicago_locations_list.append("Complete: Chicago - Perfect Agent")

        if "G5 Building" not in world.options.excluded_missions:
            g5_locations_list.append("G5 Building - Perfect Agent Objective 1")
            g5_locations_list.append("G5 Building - Perfect Agent Objective 2")
            g5_locations_list.append("G5 Building - Perfect Agent Objective 3")
            g5_locations_list.append("G5 Building - Perfect Agent Objective 4")
            g5_locations_list.append("G5 Building - Perfect Agent Objective 5")
            g5_locations_list.append("Complete: G5 Building - Perfect Agent")

        if "A51 Infiltration" not in world.options.excluded_missions:
            infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 1")
            infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 2")
            infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 3")
            infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 4")
            infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 5")
            infiltration_locations_list.append("Complete: A51 Infiltration - Perfect Agent")

        if "A51 Rescue" not in world.options.excluded_missions:
            rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 1")
            rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 2")
            rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 3")
            rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 4")
            rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 5")
            rescue_locations_list.append("Complete: A51 Rescue - Perfect Agent")

        if "A51 Escape" not in world.options.excluded_missions:
            escape_locations_list.append("A51 Escape - Perfect Agent Objective 1")
            escape_locations_list.append("A51 Escape - Perfect Agent Objective 2")
            escape_locations_list.append("A51 Escape - Perfect Agent Objective 3")
            escape_locations_list.append("A51 Escape - Perfect Agent Objective 4")
            escape_locations_list.append("A51 Escape - Perfect Agent Objective 5")
            escape_locations_list.append("Complete: A51 Escape - Perfect Agent")

        if "Air Base" not in world.options.excluded_missions:
            airbase_locations_list.append("Air Base - Perfect Agent Objective 1")
            airbase_locations_list.append("Air Base - Perfect Agent Objective 2")
            airbase_locations_list.append("Air Base - Perfect Agent Objective 3")
            airbase_locations_list.append("Air Base - Perfect Agent Objective 4")
            airbase_locations_list.append("Air Base - Perfect Agent Objective 5")
            airbase_locations_list.append("Complete: Air Base - Perfect Agent")

        if "Air Force One" not in world.options.excluded_missions:
            afo_locations_list.append("Air Force One - Perfect Agent Objective 1")
            afo_locations_list.append("Air Force One - Perfect Agent Objective 2")
            afo_locations_list.append("Air Force One - Perfect Agent Objective 3")
            afo_locations_list.append("Air Force One - Perfect Agent Objective 4")
            afo_locations_list.append("Air Force One - Perfect Agent Objective 5")
            afo_locations_list.append("Complete: Air Force One - Perfect Agent")

        if "Crash Site" not in world.options.excluded_missions:
            crashsite_locations_list.append("Crash Site - Perfect Agent Objective 1")
            crashsite_locations_list.append("Crash Site - Perfect Agent Objective 2")
            crashsite_locations_list.append("Crash Site - Perfect Agent Objective 3")
            crashsite_locations_list.append("Crash Site - Perfect Agent Objective 4")
            crashsite_locations_list.append("Crash Site - Perfect Agent Objective 5")
            crashsite_locations_list.append("Complete: Crash Site - Perfect Agent")

        if "Pelagic II" not in world.options.excluded_missions:
            pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 1")
            pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 2")
            pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 3")
            pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 4")
            pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 5")
            pelagic_locations_list.append("Complete: Pelagic II - Perfect Agent")

        if "Deep Sea" not in world.options.excluded_missions:
            deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 1")
            deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 2")
            deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 3")
            deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 4")
            deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 5")
            deepsea_locations_list.append("Complete: Deep Sea - Perfect Agent")

        if "CI Defense" not in world.options.excluded_missions:
            defense_locations_list.append("CI Defense - Perfect Agent Objective 1")
            defense_locations_list.append("CI Defense - Perfect Agent Objective 2")
            defense_locations_list.append("CI Defense - Perfect Agent Objective 3")
            defense_locations_list.append("CI Defense - Perfect Agent Objective 4")
            defense_locations_list.append("CI Defense - Perfect Agent Objective 5")
            defense_locations_list.append("Complete: CI Defense - Perfect Agent")

        if "Attack Ship" not in world.options.excluded_missions:
            attackship_locations_list.append("Attack Ship - Perfect Agent Objective 1")
            attackship_locations_list.append("Attack Ship - Perfect Agent Objective 2")
            attackship_locations_list.append("Attack Ship - Perfect Agent Objective 3")
            attackship_locations_list.append("Attack Ship - Perfect Agent Objective 4")
            attackship_locations_list.append("Attack Ship - Perfect Agent Objective 5")
            attackship_locations_list.append("Complete: Attack Ship - Perfect Agent")

        if ("Skedar Ruins" not in world.options.excluded_missions
                or world.options.goal.value == Goal.option_complete_skedar_ruins):
            skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 1")
            skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 2")
            skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 3")
            skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 4")
            skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 5")
            skedarruins_locations_list.append("Complete: Skedar Ruins - Perfect Agent")

        if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
            mbr_locations_list.append("Mr. Blonde's Revenge - Perfect Agent Objective 1")
            mbr_locations_list.append("Mr. Blonde's Revenge - Perfect Agent Objective 2")
            mbr_locations_list.append("Mr. Blonde's Revenge - Perfect Agent Objective 3")
            mbr_locations_list.append("Complete: Mr. Blonde's Revenge - Perfect Agent")

        if "Maian SOS" not in world.options.excluded_missions:
            maiansos_locations_list.append("Maian SOS - Perfect Agent Objective 1")
            maiansos_locations_list.append("Maian SOS - Perfect Agent Objective 2")
            maiansos_locations_list.append("Maian SOS - Perfect Agent Objective 3")
            maiansos_locations_list.append("Complete: Maian SOS - Perfect Agent")

        if "WAR!" not in world.options.excluded_missions:
            war_locations_list.append("WAR! - Perfect Agent Objective 1")
            war_locations_list.append("WAR! - Perfect Agent Objective 2")
            war_locations_list.append("WAR! - Perfect Agent Objective 3")
            war_locations_list.append("Complete: WAR! - Perfect Agent")

        if "The Duel" not in world.options.excluded_missions:
            duel_locations_list.append("The Duel - Perfect Agent Objective 1")
            duel_locations_list.append("The Duel - Perfect Agent Objective 2")
            duel_locations_list.append("The Duel - Perfect Agent Objective 3")
            duel_locations_list.append("Complete: The Duel - Perfect Agent")

        if world.options.alternate_exits.value == AlternateExits.option_one:
            g5_building_exits = [
                "Complete G5 Building (Perfect Agent): Bottom Exit",
                "Complete G5 Building (Perfect Agent): Upper Exit"
            ]

            escape_exits = [
                "Complete A51 Escape (Perfect Agent): UFO Escape",
                "Complete A51 Escape (Perfect Agent): Alternate Escape"
            ]

            air_base_exits = [
                "Complete Air Base (Perfect Agent): Shuttle Exit",
                "Complete Air Base (Perfect Agent): Ladder Exit"
            ]

            if "G5 Building" not in world.options.excluded_missions:
                g5_item = world.random.choice(g5_building_exits)
                g5_locations_list.append(g5_item)

            if "A51 Escape" not in world.options.excluded_missions:
                escape_item = world.random.choice(escape_exits)
                escape_locations_list.append(escape_item)

            if "Air Base" not in world.options.excluded_missions:
                air_base_item = world.random.choice(air_base_exits)
                airbase_locations_list.append(air_base_item)
            
        elif world.options.alternate_exits.value == AlternateExits.option_all:
            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("Complete G5 Building (Perfect Agent): Bottom Exit")
                g5_locations_list.append("Complete G5 Building (Perfect Agent): Upper Exit")

            if "A51 Escape" not in world.options.excluded_missions:
                escape_locations_list.append("Complete A51 Escape (Perfect Agent): UFO Escape")
                escape_locations_list.append("Complete A51 Escape (Perfect Agent): Alternate Escape")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Complete Air Base (Perfect Agent): Shuttle Exit")
                airbase_locations_list.append("Complete Air Base (Perfect Agent): Ladder Exit")


    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not (world.options.agent or world.options.special_agent or world.options.perfect_agent):
        skedarruins_locations_list.append("Skedar Ruins - Agent Objective 1")
        skedarruins_locations_list.append("Skedar Ruins - Agent Objective 2")
        skedarruins_locations_list.append("Skedar Ruins - Agent Objective 3")
        skedarruins_locations_list.append("Complete: Skedar Ruins - Agent")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 1")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 2")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 3")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 4")
        skedarruins_locations_list.append("Complete: Skedar Ruins - Special Agent")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 1")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 2")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 3")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 4")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 5")
        skedarruins_locations_list.append("Complete: Skedar Ruins - Perfect Agent")

        if world.options.completion_cheats:
            skedarruins_locations_list.append("Cheat Unlock: Complete Skedar Ruins")
            skedar_cheat = PerfectDarkLocation(world.player, "Cheat Unlock: Complete Skedar Ruins")
            skedar_cheat.progress_type = LocationProgressType.EXCLUDED

        if world.options.timed_cheats:
            skedarruins_locations_list.append("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
            skedar_cheat_timed = PerfectDarkLocation(world.player, "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
            skedar_cheat_timed.progress_type = LocationProgressType.EXCLUDED


    if (world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value >= SkedarRuinsRequirements.option_complete_missions):
        institute_locations_list.append("Collect All Stars")


    if has_challenges(world):
        challenge_total = 0

        for x in range(1, 31):
            challenge_name = f"Challenge {x}"
            if (world.options.excluded_challenges.__contains__(challenge_name) == False):
                challenge_total += 1
                challenge_location = f"Complete: Challenge {x}"
                institute_locations_list.append(challenge_location)

        if world.options.multiplayer_unlocks:
            if challenge_total >= 1:
                institute_locations_list.append("Complete 1 Challenge: FarSight XR-20 Unlock")
                institute_locations_list.append("Complete 1 Challenge: Complex Unlock")
                institute_locations_list.append("Complete 1 Challenge: dataDyne Female Guard Unlock")

            if challenge_total >= 2:
                institute_locations_list.append("Complete 2 Challenges: Shotgun Unlock")
                institute_locations_list.append("Complete 2 Challenges: Hold the Briefcase Unlock")
                institute_locations_list.append("Complete 2 Challenges: Office Suit and Office Casual Unlock")

            if challenge_total >= 3:
                institute_locations_list.append("Complete 3 Challenges: Falcon 2 (Silencer) Unlock")
                institute_locations_list.append("Complete 3 Challenges: One-Hit Kills Unlock")
                institute_locations_list.append("Complete 3 Challenges: Warehouse Unlock")
            
            if challenge_total >= 4:
                institute_locations_list.append("Complete 4 Challenges: SuperDragon Unlock")
                institute_locations_list.append("Complete 4 Challenges: Capture the Case Unlock")
                institute_locations_list.append("Complete 4 Challenges: Carrington Villa Outfits Unlock")

            if challenge_total >= 5:
                institute_locations_list.append("Complete 5 Challenges: Laptop Gun Unlock")
                institute_locations_list.append("Complete 5 Challenges: Ravine Unlock")
                institute_locations_list.append("Complete 5 Challenges: Trent Unlock")
                institute_locations_list.append("Complete 5 Challenges: NSA Lackey Unlock")

            if challenge_total >= 6:
                institute_locations_list.append("Complete 6 Challenges: Remote Mine Unlock")
                institute_locations_list.append("Complete 6 Challenges: Temple Unlock")
                institute_locations_list.append("Complete 6 Challenges: G5 Building Outfits Unlock")
                institute_locations_list.append("Complete 6 Challenges: Hacker Central Unlock")
            
            if challenge_total >= 7:
                institute_locations_list.append("Complete 7 Challenges: Tranquilizer Unlock")
                institute_locations_list.append("Complete 7 Challenges: Hard Bot Difficulty Unlock")
                institute_locations_list.append("Complete 7 Challenges: Mr. Blonde Unlock")
                institute_locations_list.append("Complete 7 Challenges: 8 Bots and Dinner Jacket Outfits Unlock")

            if challenge_total >= 8:
                institute_locations_list.append("Complete 8 Challenges: Falcon 2 (Scope) Unlock")
                institute_locations_list.append("Complete 8 Challenges: Slow Motion Unlock")
                institute_locations_list.append("Complete 8 Challenges: Joanna Trench Unlock")

            if challenge_total >= 9:
                institute_locations_list.append("Complete 9 Challenges: Reaper Unlock")
                institute_locations_list.append("Complete 9 Challenges: G5 Building Unlock")
                institute_locations_list.append("Complete 9 Challenges: CIA Agent and FBI Agent Unlock")


            if challenge_total >= 10:
                institute_locations_list.append("Complete 10 Challenges: Cloaking Device Unlock")
                institute_locations_list.append("Complete 10 Challenges: A51 Infiltration Outfits Unlock")


            if challenge_total >= 11:
                institute_locations_list.append("Complete 11 Challenges: Devastator Unlock")
                institute_locations_list.append("Complete 11 Challenges: Grid Unlock")
                institute_locations_list.append("Complete 11 Challenges: Lab Technician Outfits Unlock")

            if challenge_total >= 12:
                institute_locations_list.append("Complete 12 Challenges: Proximity Mine Unlock")
                institute_locations_list.append("Complete 12 Challenges: Perfect Bot Difficulty Unlock")
                institute_locations_list.append("Complete 12 Challenges: Felicity Unlock")
                institute_locations_list.append("Complete 12 Challenges: Biotechnician Unlock")
                institute_locations_list.append("Complete 12 Challenges: Pop a Cap Unlock")

            if challenge_total >= 13:
                institute_locations_list.append("Complete 13 Challenges: Slayer Unlock")

            if challenge_total >= 14:
                institute_locations_list.append("Complete 14 Challenges: Phoenix Unlock")
                institute_locations_list.append("Complete 14 Challenges: Villa Unlock")
                institute_locations_list.append("Complete 14 Challenges: Elvis and Maian Soldier Unlock")

            if challenge_total >= 15:
                institute_locations_list.append("Complete 15 Challenges: Combat Boost Unlock")

            if challenge_total >= 16:
                institute_locations_list.append("Complete 16 Challenges: Mauler Unlock")
                institute_locations_list.append("Complete 16 Challenges: Sewers Unlock")
                institute_locations_list.append("Complete 16 Challenges: Air Force One Outfits Unlock")

            if challenge_total >= 17:
                institute_locations_list.append("Complete 17 Challenges: Callisto NTG Unlock")
                institute_locations_list.append("Complete 17 Challenges: Car Park Unlock")
                institute_locations_list.append("Complete 17 Challenges: Alaskan Guard Unlock")
                institute_locations_list.append("Complete 17 Challenges: Joanna Arctic Unlock")

            if challenge_total >= 18:
                institute_locations_list.append("Complete 18 Challenges: Crossbow Unlock")
                institute_locations_list.append("Complete 18 Challenges: Base Unlock")
                institute_locations_list.append("Complete 18 Challenges: Formal Outfits and President Unlock")
                institute_locations_list.append("Complete 18 Challenges: Presidential Security Unlock")

            if challenge_total >= 19:
                institute_locations_list.append("Complete 19 Challenges: RC-P120 Unlock")
                institute_locations_list.append("Complete 19 Challenges: President's Clone Unlock")
                institute_locations_list.append("Complete 19 Challenges: NSA Bodyguard Unlock")

            if challenge_total >= 20:
                institute_locations_list.append("Complete 20 Challenges: DY357-LX Unlock")
                institute_locations_list.append("Complete 20 Challenges: Fortress Unlock")

            if challenge_total >= 21:
                institute_locations_list.append("Complete 21 Challenges: N-Bomb Unlock")

            if challenge_total >= 22:
                institute_locations_list.append("Complete 22 Challenges: Dark Bot Difficulty Unlock")
                institute_locations_list.append("Complete 22 Challenges: Ruins Unlock")

            if challenge_total >= 24:
                institute_locations_list.append("Complete 24 Challenges: Pelagic II Outfits Unlock")

            # institute_locations_list.append("Complete Challenges: Unused First Unlock")
            # institute_locations_list.append("Complete Challenges: K7 Avenger Unlock")
            # institute_locations_list.append("Complete Challenges: X-Ray Scanner Unlock")
            # institute_locations_list.append("Complete Challenges: Shield Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 1B Unlock")
            # institute_locations_list.append("Complete Challenges: King of the Hill Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 22 Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 2F Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 31 Unlock")
            # institute_locations_list.append("Complete Challenges: Unused Jo Snow Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 48 Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 49 Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 4B Unlock")
            # institute_locations_list.append("Complete Challenges: Jonathan Unlock")
            # institute_locations_list.append("Complete Challenges: Laser Unlock")


    if world.options.weapon_training:
        for weapon in FIRING_RANGE_WEAPONS:
            if weapon not in world.options.excluded_fr_weapons:
                institute_locations_list.append(f"Firing Range: {weapon} - Bronze")
                institute_locations_list.append(f"Firing Range: {weapon} - Silver")
                institute_locations_list.append(f"Firing Range: {weapon} - Gold")


    if world.options.device_training:
        institute_locations_list.append("Device Training: Data Uplink")
        institute_locations_list.append("Device Training: ECM Mine")
        institute_locations_list.append("Device Training: CamSpy")
        institute_locations_list.append("Device Training: Night Vision")
        institute_locations_list.append("Device Training: Door Decoder")
        institute_locations_list.append("Device Training: R-Tracker")
        institute_locations_list.append("Device Training: IR Scanner")
        institute_locations_list.append("Device Training: X-Ray Scanner")
        institute_locations_list.append("Device Training: Disguise")
        institute_locations_list.append("Device Training: Cloaking Device")


    if world.options.holotraining:
        institute_locations_list.append("Holotraining 1: Looking Around")
        institute_locations_list.append("Holotraining 2: Movement 1")
        institute_locations_list.append("Holotraining 3: Movement 2")
        institute_locations_list.append("Holotraining 4: Unarmed Combat 1")
        institute_locations_list.append("Holotraining 5: Unarmed Combat 2")
        institute_locations_list.append("Holotraining 6: Live Combat 1")
        institute_locations_list.append("Holotraining 7: Live Combat 2")


    if world.options.completion_cheats \
            and (world.options.agent or world.options.special_agent or world.options.perfect_agent):
        if "dD Defection" not in world.options.excluded_missions:
            defection_locations_list.append("Cheat Unlock: Complete dD Defection")

        if "dD Investigation" not in world.options.excluded_missions:
            investigation_locations_list.append("Cheat Unlock: Complete dD Investigation")

        if "dD Extraction" not in world.options.excluded_missions:
            extraction_locations_list.append("Cheat Unlock: Complete dD Extraction")

        if "Carrington Villa" not in world.options.excluded_missions:
            villa_locations_list.append("Cheat Unlock: Complete Carrington Villa")

        if "Chicago" not in world.options.excluded_missions:
            chicago_locations_list.append("Cheat Unlock: Complete Chicago")

        if "G5 Building" not in world.options.excluded_missions:
            g5_locations_list.append("Cheat Unlock: Complete G5 Building")

        if "A51 Infiltration" not in world.options.excluded_missions:
            infiltration_locations_list.append("Cheat Unlock: Complete A51 Infiltration")

        if "A51 Rescue" not in world.options.excluded_missions:
            rescue_locations_list.append("Cheat Unlock: Complete A51 Rescue")

        if "A51 Escape" not in world.options.excluded_missions:
            escape_locations_list.append("Cheat Unlock: Complete A51 Escape")

        if "Air Base" not in world.options.excluded_missions:
            airbase_locations_list.append("Cheat Unlock: Complete Air Base")

        if "Air Force One" not in world.options.excluded_missions:
            afo_locations_list.append("Cheat Unlock: Complete Air Force One")

        if "Crash Site" not in world.options.excluded_missions:
            crashsite_locations_list.append("Cheat Unlock: Complete Crash Site")

        if "Pelagic II" not in world.options.excluded_missions:
            pelagic_locations_list.append("Cheat Unlock: Complete Pelagic II")

        if "Deep Sea" not in world.options.excluded_missions:
            deepsea_locations_list.append("Cheat Unlock: Complete Deep Sea")

        if "CI Defense" not in world.options.excluded_missions:
            defense_locations_list.append("Cheat Unlock: Complete CI Defense")

        if "Attack Ship" not in world.options.excluded_missions:
            attackship_locations_list.append("Cheat Unlock: Complete Attack Ship")

        if "Skedar Ruins" not in world.options.excluded_missions:
            skedarruins_locations_list.append("Cheat Unlock: Complete Skedar Ruins")


    if world.options.timed_cheats:
        if world.options.agent:
            if "dD Extraction" not in world.options.excluded_missions:
                extraction_locations_list.append("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")

            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")

            if "A51 Escape" not in world.options.excluded_missions:
                escape_locations_list.append("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")

            if "Crash Site" not in world.options.excluded_missions:
                crashsite_locations_list.append("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")

            if "CI Defense" not in world.options.excluded_missions:
                defense_locations_list.append("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")

        if world.options.special_agent:
            if "dD Defection" not in world.options.excluded_missions:
                defection_locations_list.append("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")

            if "Carrington Villa" not in world.options.excluded_missions:
                villa_locations_list.append("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")

            if "A51 Infiltration" not in world.options.excluded_missions:
                infiltration_locations_list.append("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")

            if "Pelagic II" not in world.options.excluded_missions:
                pelagic_locations_list.append("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")

            if "Attack Ship" not in world.options.excluded_missions:
                attackship_locations_list.append("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")

        if world.options.perfect_agent:
            if "dD Investigation" not in world.options.excluded_missions:
                investigation_locations_list.append("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")

            if "Chicago" not in world.options.excluded_missions:
                chicago_locations_list.append("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")

            if "A51 Rescue" not in world.options.excluded_missions:
                rescue_locations_list.append("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")

            if "Air Force One" not in world.options.excluded_missions:
                afo_locations_list.append("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")

            if "Deep Sea" not in world.options.excluded_missions:
                deepsea_locations_list.append("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")

            if "Skedar Ruins" not in world.options.excluded_missions:
                skedarruins_locations_list.append("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")


    if world.options.weapon_cheats:
        if ("Falcon 2" not in world.options.excluded_fr_weapons
                and "Falcon 2 (Silencer)" not in world.options.excluded_fr_weapons
                and "Falcon 2 (Scope)" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)")

        if ("MagSec 4" not in world.options.excluded_fr_weapons
                and "Mauler" not in world.options.excluded_fr_weapons
                and "Phoenix" not in world.options.excluded_fr_weapons
                and "DY357 Magnum" not in world.options.excluded_fr_weapons
                and "DY357-LX" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX")

        if ("CMP150" not in world.options.excluded_fr_weapons
                and "Cyclone" not in world.options.excluded_fr_weapons
                and "Callisto NTG" not in world.options.excluded_fr_weapons
                and "RC-P120" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on CMP150, Cyclone, Callisto NTG, and RC-P120")

        if ("Laptop Gun" not in world.options.excluded_fr_weapons
                and "Dragon" not in world.options.excluded_fr_weapons
                and "K7 Avenger" not in world.options.excluded_fr_weapons
                and "AR34" not in world.options.excluded_fr_weapons
                and "SuperDragon" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon")

        if ("Shotgun" not in world.options.excluded_fr_weapons
                and "Sniper Rifle" not in world.options.excluded_fr_weapons
                and "Rocket Launcher" not in world.options.excluded_fr_weapons
                and "Slayer" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on Shotgun, Sniper Rifle, Rocket Launcher, and Slayer")

        if ("Timed Mine" not in world.options.excluded_fr_weapons
                and "Proximity Mine" not in world.options.excluded_fr_weapons
                and "Remote Mine" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on Timed Mine, Proximity Mine, and Remote Mine")

        if ("FarSight XR-20" not in world.options.excluded_fr_weapons
                and "Crossbow" not in world.options.excluded_fr_weapons
                and "Combat Knife" not in world.options.excluded_fr_weapons
                and "Grenade" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on FarSight XR-20, Crossbow, Combat Knife, and Grenade")

        if ("Tranquilizer" not in world.options.excluded_fr_weapons
                and "Reaper" not in world.options.excluded_fr_weapons
                and "Devastator" not in world.options.excluded_fr_weapons):
            institute_locations_list.append("Cheat Unlock: Get gold on Tranquilizer, Reaper, and Devastator")


    if world.options.pickupsanity \
            and (world.options.agent or world.options.special_agent or world.options.perfect_agent):
        if "dD Defection" not in world.options.excluded_missions:
            defection_locations_list.append("dD Defection: 2F double Falcon 2 (silencer)")
            defection_locations_list.append("dD Defection: 3F tiny ammo box (on corner desk)")
            defection_locations_list.append("dD Defection: 3F tiny ammo box (on table near couch)")
            defection_locations_list.append("dD Defection: 2F tiny ammo box (on desk across the stairs)")
            defection_locations_list.append("dD Defection: 2F tiny ammo box (on desk across the elevator)")
            defection_locations_list.append("dD Defection: 2F Falcon 2 (silencer) (on desk)")
            defection_locations_list.append("dD Defection: 2F tiny ammo box (under stairs)")
            defection_locations_list.append("dD Defection: 1F CMP150 (on right of front desk)")
            defection_locations_list.append("dD Defection: 1F CMP150 (on left of front desk)")

        if "dD Investigation" not in world.options.excluded_missions:
            investigation_locations_list.append("dD Investigation: ammo box (front of room above the K7 Avenger)")
            investigation_locations_list.append("dD Investigation: ammo box (back of room above the K7 Avenger)")
            investigation_locations_list.append("dD Investigation: ammo box (front of Night Vision room)")
            investigation_locations_list.append("dD Investigation: ammo box (back of Night Vision room)")
            investigation_locations_list.append("dD Investigation: CMP150 (on front of table)")
            investigation_locations_list.append("dD Investigation: CMP150 (on back of table)")
            investigation_locations_list.append("dD Investigation: CMP150 (left of secret weapons compartment)")
            investigation_locations_list.append("dD Investigation: CMP150 (right of secret weapons compartment)")
            investigation_locations_list.append("dD Investigation: Proximity Mine (in radioactive room)")

        if "dD Extraction" not in world.options.excluded_missions:
            extraction_locations_list.append("dD Extraction: 1F DY357 Magnum (from fifth guard)")
            extraction_locations_list.append("dD Extraction: 4F Rocket Launcher")
            extraction_locations_list.append("dD Extraction: 4F Grenade (on Cassandra's desk)")
            extraction_locations_list.append("dD Extraction: 4F Dragon (in hidden room in Cassandra's office)")
            extraction_locations_list.append("dD Extraction: Rocket ammo box (on left)")
            extraction_locations_list.append("dD Extraction: Rocket ammo box (on right)")

        if "Carrington Villa" not in world.options.excluded_missions:
            villa_locations_list.append("Carrington Villa: Devastator (in helipad crate)")
            villa_locations_list.append("Carrington Villa: 1st ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 2nd ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 3rd ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 4th ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 5th ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 6th ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 7th ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 8th ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: 9th ammo box (in crate on observatory path)")
            villa_locations_list.append("Carrington Villa: double CMP150 (from sniper near the helipad)")

        if "Chicago" not in world.options.excluded_missions:
            chicago_locations_list.append("Chicago: BombSpy (in the dumpster)")
            chicago_locations_list.append("Chicago: double Falcon 2 (scope) (in the Pond Punk)")

        if "G5 Building" not in world.options.excluded_missions:
            g5_locations_list.append("G5 Building: Crossbow (after knocking out the second guard)")

        if "A51 Infiltration" not in world.options.excluded_missions:
            infiltration_locations_list.append("A51 Infiltration: Rocket Launcher (in mine field)")

        if "A51 Rescue" not in world.options.excluded_missions:
            rescue_locations_list.append("A51 Rescue: Phoenix (past locked hangar door)")
            rescue_locations_list.append("A51 Rescue: double Falcon 2 (silencer) (hidden in barrel)")

        if "A51 Escape" not in world.options.excluded_missions:
            escape_locations_list.append("A51 Escape: double Falcon 2 (scope) (behind you at the start)")
            escape_locations_list.append("A51 Escape: Remote Mine (in first room with guards)")

        if "Air Base" not in world.options.excluded_missions:
            airbase_locations_list.append("Air Base: double DY357 Magnum (after knocking out all NSA Lackeys)")
            airbase_locations_list.append("Air Base: Proximity Mine (past the cave)")

        if "Air Force One" not in world.options.excluded_missions:
            afo_locations_list.append("Air Force One: Cyclone (in room right of stairs)")
            afo_locations_list.append("Air Force One: Cyclone (in room left of stairs)")

        if "Crash Site" not in world.options.excluded_missions:
            crashsite_locations_list.append("Crash Site: DY357-LX (from disarming Trent)")
            crashsite_locations_list.append("Crash Site: Proximity Mine (from Elvis before doing any objective)")

        if "Pelagic II" not in world.options.excluded_missions:
            pelagic_locations_list.append("Pelagic II: double Falcon 2 (silencer) (without triggering the alarm)")

        if "Deep Sea" not in world.options.excluded_missions:
            deepsea_locations_list.append("Deep Sea: Proximity Mine (from guard in 2nd room with cloaked guards)")
            # deepsea_locations_list.append("Deep Sea: Shotgun (near Shield on the left path)")

        if "CI Defense" not in world.options.excluded_missions:
            defense_locations_list.append("CI Defense: Devastator (dropped after saving most of the hostages)")

        if "Attack Ship" not in world.options.excluded_missions:
            attackship_locations_list.append("Attack Ship: double Mauler (dropped from Skedar in final room)")
            attackship_locations_list.append("Attack Ship: Slayer (in the room past green chambers)")

        if "Skedar Ruins" not in world.options.excluded_missions:
            skedarruins_locations_list.append("Skedar Ruins: double Phoenix (near the gap)")

        if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
            mbr_locations_list.append("Mr. Blonde's Revenge: 1F double CMP150 (from guard near bottom elevator)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 3F tiny ammo box (on corner desk)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 3F tiny ammo box (on table near couch)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the stairs)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the elevator)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F Falcon 2 (on desk)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F tiny ammo box (under stairs)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 1F CMP150 (on right of front desk)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 1F CMP150 (on left of front desk)")

        if "Maian SOS" not in world.options.excluded_missions:
            maiansos_locations_list.append("Maian SOS: double DY357-LX (from dual-wielding guard)")
            maiansos_locations_list.append("Maian SOS: Psychosis Gun (on desk near the start)")

        if world.options.agent:
            if "dD Defection" not in world.options.excluded_missions:
                defection_locations_list.append("dD Defection (Agent): 1F Shield")

            if "dD Investigation" not in world.options.excluded_missions:
                investigation_locations_list.append("dD Investigation (Agent): Shield (on crate)")

            if "dD Extraction" not in world.options.excluded_missions:
                extraction_locations_list.append("dD Extraction (Agent): 2F Shield")

            if "Carrington Villa" not in world.options.excluded_missions:
                villa_locations_list.append("Carrington Villa (Agent): Shield (on helipad crate)")
                villa_locations_list.append("Carrington Villa (Agent): Shield (in the bathroom)")

            if "Chicago" not in world.options.excluded_missions:
                chicago_locations_list.append("Chicago (Agent): Shield (near the taxi)")

            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("G5 Building (Agent): Shield (in room before the laser grids)")

            if "A51 Infiltration" not in world.options.excluded_missions:
                infiltration_locations_list.append("A51 Infiltration (Agent): Shield (near hoverbike)")

            if "A51 Rescue" not in world.options.excluded_missions:
                rescue_locations_list.append("A51 Rescue (Agent): Shield (guard past first elevator)")

            if "A51 Escape" not in world.options.excluded_missions:
                escape_locations_list.append("A51 Escape (Agent): Shield (dropped by biotechnician)")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Air Base (Agent): Shield (dropped by NSA Lackey)")

            if "Air Force One" not in world.options.excluded_missions:
                afo_locations_list.append("Air Force One (Agent): Shield (in small kitchen)")

            if "Crash Site" not in world.options.excluded_missions:
                crashsite_locations_list.append("Crash Site (Agent): Shield (near the crashed UFO)")

            if "Pelagic II" not in world.options.excluded_missions:
                pelagic_locations_list.append("Pelagic II (Agent): Shield (on the helipad)")

            # if "Deep Sea" not in world.options.excluded_missions:
            #     deepsea_locations_list.append("Deep Sea (Agent): Pick up Shield dropped from Sniper guard")

            if "CI Defense" not in world.options.excluded_missions:
                defense_locations_list.append("CI Defense (Agent): 2F Shield")

            if "Skedar Ruins" not in world.options.excluded_missions:
                skedarruins_locations_list.append("Skedar Ruins (Agent): Shield (behind the fallen pillar)")

            if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
                mbr_locations_list.append("Mr. Blonde's Revenge (Agent): 1F Shield")


        if world.options.agent or world.options.special_agent:
            if "dD Defection" not in world.options.excluded_missions:
                defection_locations_list.append("dD Defection (Agent/Special): 3F Shield")

            if "dD Investigation" not in world.options.excluded_missions:
                investigation_locations_list.append("dD Investigation (Agent/Special): Shield (behind the glass)")

            if "Chicago" not in world.options.excluded_missions:
                chicago_locations_list.append("Chicago (Agent/Special): Shield (under stairs near Pond Punk)")

            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("G5 Building (Agent/Special): Shield (on stairs to the upper exit)")

            if "A51 Infiltration" not in world.options.excluded_missions:
                infiltration_locations_list.append("A51 Infiltration (Agent/Special): Shield (in the crawl space)")

            if "A51 Rescue" not in world.options.excluded_missions:
                rescue_locations_list.append("A51 Rescue (Agent/Special): Shield (on desk near computer)")

            if "A51 Escape" not in world.options.excluded_missions:
                escape_locations_list.append("A51 Escape (Agent/Special): Shield (behind locked medical containment doors)")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Air Base (Agent/Special): Shield (in the safe)")

            if "Air Force One" not in world.options.excluded_missions:
                afo_locations_list.append("Air Force One (Agent/Special): Shield (in piano room)")

            if "Crash Site" not in world.options.excluded_missions:
                crashsite_locations_list.append("Crash Site (Agent/Special): Shield (behind President's clone)")

            if "Pelagic II" not in world.options.excluded_missions:
                pelagic_locations_list.append("Pelagic II (Agent/Special): Shield (on the sub hangar crate)")

            if "Deep Sea" not in world.options.excluded_missions:
                deepsea_locations_list.append("Deep Sea (Agent/Special): Shield (on the left path)")

            if "CI Defense" not in world.options.excluded_missions:
                defense_locations_list.append("CI Defense (Agent/Special): Basement Shield")

            if "Attack Ship" not in world.options.excluded_missions:
                attackship_locations_list.append("Attack Ship (Agent/Special): Shield (on table)")

            if "Skedar Ruins" not in world.options.excluded_missions:
                skedarruins_locations_list.append("Skedar Ruins (Agent/Special): Shield (area past the gap to the right)")

            if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
                mbr_locations_list.append("Mr. Blonde's Revenge (Agent/Special): 3F Shield")


        if world.options.special_agent or world.options.perfect_agent:
            if "dD Investigation" not in world.options.excluded_missions:
                investigation_locations_list.append("dD Investigation: ammo box (front of room with one scientist)")
                investigation_locations_list.append("dD Investigation: ammo box (back of room with one scientist)")
                investigation_locations_list.append("dD Investigation: ammo box (front of room near two scientists)")
                investigation_locations_list.append("dD Investigation: ammo box (back of room near two scientists)")

            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("G5 Building: N-Bomb (near the upper exit)")

            if "A51 Infiltration" not in world.options.excluded_missions:
                infiltration_locations_list.append("A51 Infiltration: double MagSec 4 (after placing comms rider)")


        if world.options.perfect_agent:
            if "Carrington Villa" not in world.options.excluded_missions:
                villa_locations_list.append("Carrington Villa (Perfect Agent): Sniper Rifle (in the bathroom)")

            if "Attack Ship" not in world.options.excluded_missions:
                attackship_locations_list.append("Attack Ship (Perfect Agent): De Vries' Necklace")


        if world.options.mission_logic.value == MissionLogic.option_perfect:
            if "Mr. Blonde's Revenge" not in world.options.excluded_missions:
                mbr_locations_list.append("Mr. Blonde's Revenge: 2F Laptop Gun")
                mbr_locations_list.append("Mr. Blonde's Revenge: 2F Falcon 2 (on right)")
                mbr_locations_list.append("Mr. Blonde's Revenge: 2F Falcon 2 (on left)")


        if world.options.perfect_agent \
                or world.options.mission_logic.value == MissionLogic.option_perfect:
            if "dD Defection" not in world.options.excluded_missions:
                defection_locations_list.append("dD Defection: 2F Laptop Gun")
                defection_locations_list.append("dD Defection: 2F Falcon 2 (silencer) (on right)")
                defection_locations_list.append("dD Defection: 2F Falcon 2 (silencer) (on left)")

    if world.options.glassanity:
        if ("dD Defection" not in world.options.excluded_missions
                or "dD Extraction" not in world.options.excluded_missions
                or "Mr. Blonde's Revenge" not in world.options.excluded_missions):
            dd_central_locations_list.append("dD Central: Top Glass Railing (stairs between roof and 4F)")
            dd_central_locations_list.append("dD Central: Bottom Glass Railing (stairs between roof and 4F)")
            dd_central_locations_list.append("dD Central: Top Window (stairs between roof and 4F)")
            dd_central_locations_list.append("dD Central: Middle Window (stairs between roof and 4F)")
            dd_central_locations_list.append("dD Central: Bottom Window (stairs between roof and 4F)")
            dd_central_locations_list.append("dD Central: 4F Window 1")
            dd_central_locations_list.append("dD Central: 4F Window 2")
            dd_central_locations_list.append("dD Central: 4F Window 3")
            dd_central_locations_list.append("dD Central: 4F Window 4")
            dd_central_locations_list.append("dD Central: 4F Window 5")
            dd_central_locations_list.append("dD Central: 4F Window 6")
            dd_central_locations_list.append("dD Central: 4F Window 7")
            dd_central_locations_list.append("dD Central: 4F Window 8")
            dd_central_locations_list.append("dD Central: 4F Window 9")
            dd_central_locations_list.append("dD Central: 4F Glass Railing 1")
            dd_central_locations_list.append("dD Central: 4F Glass Railing 2")
            dd_central_locations_list.append("dD Central: 4F Glass Railing 3")
            dd_central_locations_list.append("dD Central: 4F Glass Railing 4")
            dd_central_locations_list.append("dD Central: Cassandra's Office Window (left)")
            dd_central_locations_list.append("dD Central: Cassandra's Office Window (middle)")
            dd_central_locations_list.append("dD Central: Cassandra's Office Window (right)")
            dd_central_locations_list.append("dD Central: Cassandra's Office Window (top)")
            dd_central_locations_list.append("dD Central: Top Glass Railing (stairs between 4F and 2F)")
            dd_central_locations_list.append("dD Central: Bottom Glass Railing (stairs between 4F and 2F)")
            dd_central_locations_list.append("dD Central: Top Window (stairs between 4F and 2F)")
            dd_central_locations_list.append("dD Central: Middle Window (stairs between 4F and 2F)")
            dd_central_locations_list.append("dD Central: Bottom Window (stairs between 4F and 2F)")
            dd_central_locations_list.append("dD Central: 3F Glass 1 (near elevator)")
            dd_central_locations_list.append("dD Central: 3F Glass 2 (near elevator)")
            dd_central_locations_list.append("dD Central: 3F Glass 3 (near elevator)")
            dd_central_locations_list.append("dD Central: 3F Window 1")
            dd_central_locations_list.append("dD Central: 3F Window 2")
            dd_central_locations_list.append("dD Central: 3F Window 3")
            dd_central_locations_list.append("dD Central: 3F Window 4")
            dd_central_locations_list.append("dD Central: 3F Window 5")
            dd_central_locations_list.append("dD Central: 3F Window 6")
            dd_central_locations_list.append("dD Central: 3F Window 7")
            dd_central_locations_list.append("dD Central: 3F Window 8")
            dd_central_locations_list.append("dD Central: 3F Window 9")
            dd_central_locations_list.append("dD Central: 3F Window 10")
            dd_central_locations_list.append("dD Central: 3F Window 11")
            dd_central_locations_list.append("dD Central: 3F Window 12")
            dd_central_locations_list.append("dD Central: 3F Window 13")
            dd_central_locations_list.append("dD Central: 3F Window 14")
            dd_central_locations_list.append("dD Central: 3F Window 15")
            dd_central_locations_list.append("dD Central: 3F Window 16")
            dd_central_locations_list.append("dD Central: 3F Window 17")
            dd_central_locations_list.append("dD Central: 3F Window 18")
            dd_central_locations_list.append("dD Central: 2F Glass 1 (near elevator)")
            dd_central_locations_list.append("dD Central: 2F Glass 2 (near elevator)")
            dd_central_locations_list.append("dD Central: 2F Glass 3 (near elevator)")
            dd_central_locations_list.append("dD Central: 2F Window 1")
            dd_central_locations_list.append("dD Central: 2F Window 2")
            dd_central_locations_list.append("dD Central: 2F Window 3")
            dd_central_locations_list.append("dD Central: 2F Window 4")
            dd_central_locations_list.append("dD Central: 2F Window 5")
            dd_central_locations_list.append("dD Central: 2F Window 6")
            dd_central_locations_list.append("dD Central: 2F Window 7")
            dd_central_locations_list.append("dD Central: 2F Window 8")
            dd_central_locations_list.append("dD Central: 2F Window 9")
            dd_central_locations_list.append("dD Central: 2F Window 10")
            dd_central_locations_list.append("dD Central: 2F Window 11")
            dd_central_locations_list.append("dD Central: 2F Window 12")
            dd_central_locations_list.append("dD Central: 2F Window 13")
            dd_central_locations_list.append("dD Central: 2F Window 14")
            dd_central_locations_list.append("dD Central: 2F Window 15")
            dd_central_locations_list.append("dD Central: 2F Window 16")
            dd_central_locations_list.append("dD Central: 2F Window 17")
            dd_central_locations_list.append("dD Central: Left Elevator Glass 1")
            dd_central_locations_list.append("dD Central: Left Elevator Glass 2")
            dd_central_locations_list.append("dD Central: Right Elevator Glass 1")
            dd_central_locations_list.append("dD Central: Right Elevator Glass 2")
            dd_central_locations_list.append("dD Central: 1F Left Elevator Glass 1")
            dd_central_locations_list.append("dD Central: 1F Left Elevator Glass 2")
            dd_central_locations_list.append("dD Central: 1F Left Elevator Glass 3")
            dd_central_locations_list.append("dD Central: 1F Right Elevator Glass 1")
            dd_central_locations_list.append("dD Central: 1F Right Elevator Glass 2")
            dd_central_locations_list.append("dD Central: 1F Right Elevator Glass 3")
            dd_central_locations_list.append("dD Central: 1F Glass Railing 1")
            dd_central_locations_list.append("dD Central: 1F Glass Railing 2")
            dd_central_locations_list.append("dD Central: 1F Glass Railing 3")
            dd_central_locations_list.append("dD Central: 1F Glass Railing 4")
            dd_central_locations_list.append("dD Central: 1F Glass Railing 5")

        if "dD Investigation" not in world.options.excluded_missions:
            investigation_locations_list.append("dD Investigation: Glass Railing (near cleaning bot)")
            investigation_locations_list.append("dD Investigation: Glass on door (near cleaning bot)")
            investigation_locations_list.append("dD Investigation: Glass 1 (near computer)")
            investigation_locations_list.append("dD Investigation: Glass 2 (near computer)")
            investigation_locations_list.append("dD Investigation: Glass 1 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 2 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 3 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 4 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 5 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 6 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 7 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 8 (room with night vision)")
            investigation_locations_list.append("dD Investigation: Glass 1 (room with glass enclosure)")
            
            investigation_locations_list.append("dD Investigation: Glass on door 1 (sector 3 door)")
            investigation_locations_list.append("dD Investigation: Glass on door 2 (sector 3 door)")
            investigation_locations_list.append("dD Investigation: Glass 1 (big room near the end)")
            investigation_locations_list.append("dD Investigation: Glass 2 (big room near the end)")
            investigation_locations_list.append("dD Investigation: Glass 3 (big room near the end)")
            investigation_locations_list.append("dD Investigation: Glass 4 (big room near the end)")
            investigation_locations_list.append("dD Investigation: Glass 1 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 2 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 3 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 4 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 5 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 6 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 7 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 8 (right glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 1 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 2 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 3 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 4 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 5 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 6 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 7 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 8 (front left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 1 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 2 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 3 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 4 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 5 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 6 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 7 (back left glass pillar of big room)")
            investigation_locations_list.append("dD Investigation: Glass 8 (back left glass pillar of big room)")

        if "Carrington Villa" not in world.options.excluded_missions:
            villa_locations_list.append("Carrington Villa: Glass Bottle 1")
            villa_locations_list.append("Carrington Villa: Glass Bottle 2")
            villa_locations_list.append("Carrington Villa: Glass Bottle 3")
            villa_locations_list.append("Carrington Villa: Glass Bottle 4")
            villa_locations_list.append("Carrington Villa: Glass Bottle 5")
            villa_locations_list.append("Carrington Villa: Glass Bottle 6")
            villa_locations_list.append("Carrington Villa: Glass Bottle 7")
            villa_locations_list.append("Carrington Villa: Glass Bottle 8")
            villa_locations_list.append("Carrington Villa: Glass Bottle 9")
            villa_locations_list.append("Carrington Villa: Glass Bottle 10")
            villa_locations_list.append("Carrington Villa: Glass Bottle 11")
            villa_locations_list.append("Carrington Villa: Glass Bottle 12")
            villa_locations_list.append("Carrington Villa: Glass Bottle 13")
            villa_locations_list.append("Carrington Villa: Glass Bottle 14")
            villa_locations_list.append("Carrington Villa: Glass Bottle 15")
            villa_locations_list.append("Carrington Villa: Glass Bottle 16")
            villa_locations_list.append("Carrington Villa: Glass Bottle 17")
            villa_locations_list.append("Carrington Villa: Glass Bottle 18")
            villa_locations_list.append("Carrington Villa: Glass Bottle 19")
            villa_locations_list.append("Carrington Villa: Glass Bottle 20")
            villa_locations_list.append("Carrington Villa: Glass Bottle 21")
            villa_locations_list.append("Carrington Villa: Glass Bottle 22")
            villa_locations_list.append("Carrington Villa: Glass Bottle 23")
            villa_locations_list.append("Carrington Villa: Glass Bottle 24")
            villa_locations_list.append("Carrington Villa: Glass Bottle 25")
            villa_locations_list.append("Carrington Villa: Glass Bottle 26")
            villa_locations_list.append("Carrington Villa: Glass Bottle 27")
            villa_locations_list.append("Carrington Villa: Glass Bottle 28")
            villa_locations_list.append("Carrington Villa: Glass Bottle 29")
            villa_locations_list.append("Carrington Villa: Glass Bottle 30")
            villa_locations_list.append("Carrington Villa: Glass Bottle 31")
            villa_locations_list.append("Carrington Villa: Glass Bottle 32")
            villa_locations_list.append("Carrington Villa: Glass Bottle 33")
            villa_locations_list.append("Carrington Villa: Glass Bottle 34")
            villa_locations_list.append("Carrington Villa: Glass Bottle 35")
            villa_locations_list.append("Carrington Villa: Glass Bottle 36")
            villa_locations_list.append("Carrington Villa: Glass Bottle 37")
            villa_locations_list.append("Carrington Villa: Glass Bottle 38")
            villa_locations_list.append("Carrington Villa: Glass Bottle 39")
            villa_locations_list.append("Carrington Villa: Glass Bottle 40")
            villa_locations_list.append("Carrington Villa: Glass Bottle 41")
            villa_locations_list.append("Carrington Villa: Glass Bottle 42")
            villa_locations_list.append("Carrington Villa: Glass Bottle 43")
            villa_locations_list.append("Carrington Villa: Glass Bottle 44")
            villa_locations_list.append("Carrington Villa: Glass Bottle 45")
            villa_locations_list.append("Carrington Villa: Glass Bottle 46")
            villa_locations_list.append("Carrington Villa: Glass Bottle 47")
            villa_locations_list.append("Carrington Villa: Glass Bottle 48")
            villa_locations_list.append("Carrington Villa: Glass Bottle 49")
            villa_locations_list.append("Carrington Villa: Glass Bottle 50")
            villa_locations_list.append("Carrington Villa: Glass Bottle 51")
            villa_locations_list.append("Carrington Villa: Glass Bottle 52")
            villa_locations_list.append("Carrington Villa: Glass Bottle 53")
            villa_locations_list.append("Carrington Villa: Glass Bottle 54")
            villa_locations_list.append("Carrington Villa: Glass Bottle 55")
            villa_locations_list.append("Carrington Villa: Glass Bottle 56")
            villa_locations_list.append("Carrington Villa: Glass Bottle 57")
            villa_locations_list.append("Carrington Villa: Glass Bottle 58")
            villa_locations_list.append("Carrington Villa: Glass Bottle 59")
            villa_locations_list.append("Carrington Villa: Glass Bottle 60")
            villa_locations_list.append("Carrington Villa: Glass Bottle 61")
            villa_locations_list.append("Carrington Villa: Glass Bottle 62")
            villa_locations_list.append("Carrington Villa: Glass Bottle 63")
            villa_locations_list.append("Carrington Villa: Glass Bottle 64")
            villa_locations_list.append("Carrington Villa: Glass Bottle 65")
            villa_locations_list.append("Carrington Villa: Glass Bottle 66")
            villa_locations_list.append("Carrington Villa: Glass Bottle 67")
            villa_locations_list.append("Carrington Villa: Glass Bottle 68")
            villa_locations_list.append("Carrington Villa: Glass Bottle 69")
            villa_locations_list.append("Carrington Villa: Glass Bottle 70")
            villa_locations_list.append("Carrington Villa: Glass Bottle 71")
            villa_locations_list.append("Carrington Villa: Glass Bottle 72")
            villa_locations_list.append("Carrington Villa: Glass Bottle 73")
            villa_locations_list.append("Carrington Villa: Glass Bottle 74")
            villa_locations_list.append("Carrington Villa: Glass Bottle 75")
            villa_locations_list.append("Carrington Villa: Glass Bottle 76")
            villa_locations_list.append("Carrington Villa: Glass Bottle 77")
            villa_locations_list.append("Carrington Villa: Glass Bottle 78")
            villa_locations_list.append("Carrington Villa: Glass Bottle 79")
            villa_locations_list.append("Carrington Villa: Glass Bottle 80")
            villa_locations_list.append("Carrington Villa: Glass Bottle 81")
            villa_locations_list.append("Carrington Villa: Glass Bottle 82")
            villa_locations_list.append("Carrington Villa: Glass Bottle 83")
            villa_locations_list.append("Carrington Villa: Glass Bottle 84")
            villa_locations_list.append("Carrington Villa: Glass Bottle 85")
            villa_locations_list.append("Carrington Villa: Glass Bottle 86")
            villa_locations_list.append("Carrington Villa: Glass Bottle 87")
            villa_locations_list.append("Carrington Villa: Glass Bottle 88")
            villa_locations_list.append("Carrington Villa: Glass Bottle 89")
            villa_locations_list.append("Carrington Villa: Glass Bottle 90")
            villa_locations_list.append("Carrington Villa: Glass Bottle 91")
            villa_locations_list.append("Carrington Villa: Glass Bottle 92")
            villa_locations_list.append("Carrington Villa: Glass Bottle 93")
            villa_locations_list.append("Carrington Villa: Glass Bottle 94")
            villa_locations_list.append("Carrington Villa: Glass Bottle 95")
            villa_locations_list.append("Carrington Villa: Glass Bottle 96")
            villa_locations_list.append("Carrington Villa: Glass Bottle 97")
            villa_locations_list.append("Carrington Villa: Glass Bottle 98")
            villa_locations_list.append("Carrington Villa: Glass Bottle 99")
            villa_locations_list.append("Carrington Villa: Glass Bottle 100")
            villa_locations_list.append("Carrington Villa: Glass Bottle 101")
            villa_locations_list.append("Carrington Villa: Glass Bottle 102")
            villa_locations_list.append("Carrington Villa: Glass Bottle 103")
            villa_locations_list.append("Carrington Villa: Glass Bottle 104")
            villa_locations_list.append("Carrington Villa: Glass Bottle 105")
            villa_locations_list.append("Carrington Villa: Glass Bottle 106")
            villa_locations_list.append("Carrington Villa: Glass Bottle 107")

        if "Chicago" not in world.options.excluded_missions:
            chicago_locations_list.append("Chicago: Glass 1 (above stacked barrels)")
            chicago_locations_list.append("Chicago: Glass 2 (above stacked barrels)")
            chicago_locations_list.append("Chicago: Glass 3 (above stacked barrels)")

        if "G5 Building" not in world.options.excluded_missions:
            g5_locations_list.append("G5 Building: Glass 1 (2nd cloak guards room)")
            g5_locations_list.append("G5 Building: Glass 2 (2nd cloak guards room)")
            g5_locations_list.append("G5 Building: Door Glass 1 (1st door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (1st door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (2nd door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (2nd door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (3rd door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (3rd door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (4th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (4th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (5th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (5th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (6th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (6th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (7th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (7th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 1 (8th door with glass)")
            g5_locations_list.append("G5 Building: Door Glass 2 (8th door with glass)")

        if ("A51 Rescue" not in world.options.excluded_missions
                or "A51 Escape" not in world.options.excluded_missions
                or "Maian SOS" not in world.options.excluded_missions):
            inner_a51_locations_list.append("Rescue/Escape/Maian SOS: Glass on door 1")
            inner_a51_locations_list.append("Rescue/Escape/Maian SOS: Glass on door 2")
            inner_a51_locations_list.append("Rescue/Escape/Maian SOS: Glass on medlab door")

        if ("A51 Rescue" not in world.options.excluded_missions
                or "Maian SOS" not in world.options.excluded_missions):
            inner_a51_locations_list.append("Rescue/Maian SOS: Glass 1 (in medlab)")
            inner_a51_locations_list.append("Rescue/Maian SOS: Glass 2 (in medlab)")
            inner_a51_locations_list.append("Rescue/Maian SOS: Glass 3 (in medlab)")

        if "A51 Escape" not in world.options.excluded_missions:
            escape_locations_list.append("A51 Escape: Glass (near locked medical containment door)")
            escape_locations_list.append("A51 Escape: Glass on door (locked medical containment door)")

        if "Maian SOS" not in world.options.excluded_missions:
            maiansos_locations_list.append("Maian SOS: Glass 1 (first room)")
            maiansos_locations_list.append("Maian SOS: Glass 2 (first room)")
            maiansos_locations_list.append("Maian SOS: Glass 3 (first room)")

        if "Air Base" not in world.options.excluded_missions:
            airbase_locations_list.append("Air Base: Window (suitcase room)")
            airbase_locations_list.append("Air Base: Window (near security monitor)")
            airbase_locations_list.append("Air Base: Window 1 (next to flight plans room)")
            airbase_locations_list.append("Air Base: Window 2 (next to flight plans room)")
            airbase_locations_list.append("Air Base: Window 1 (near flight plans)")
            airbase_locations_list.append("Air Base: Window 2 (near flight plans)")

        if "Pelagic II" not in world.options.excluded_missions:
            pelagic_locations_list.append("Pelagic II: Glass on Door (1st door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (2nd door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (3rd door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (4th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (5th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (6th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (7th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (8th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (9th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (10th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (15th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (16th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (17th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (18th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (19th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (20th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (21th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (22nd door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (23rd door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (24th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (25th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (near the end)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (11th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (12th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (13th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door (14th door)")
            pelagic_locations_list.append("Pelagic II: Glass on Door 1 (lower floors)")
            pelagic_locations_list.append("Pelagic II: Glass on Door 2 (lower floors)")
            pelagic_locations_list.append("Pelagic II: Glass on Door 3 (lower floors)")

        if "CI Defense" not in world.options.excluded_missions:
            defense_locations_list.append("CI Defense: 1F Glass Railing")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2")
            defense_locations_list.append("CI Defense: Basement Glass Railing 1")
            defense_locations_list.append("CI Defense: Basement Glass Railing 2")
            defense_locations_list.append("CI Defense: Basement Glass Railing 3")
            defense_locations_list.append("CI Defense: Basement Glass Railing 4")
            defense_locations_list.append("CI Defense: Basement Glass Railing 5")
            defense_locations_list.append("CI Defense: Basement Glass Railing 6")
            defense_locations_list.append("CI Defense: Basement Glass Railing 7")
            defense_locations_list.append("CI Defense: Basement Glass Railing 8")
            defense_locations_list.append("CI Defense: Basement Glass Railing 9")
            defense_locations_list.append("CI Defense: Basement Glass Railing 10")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (2nd door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (2nd door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (3rd door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (3rd door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (4th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (4th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (5th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (5th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (6th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (6th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (7th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (7th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (8th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (8th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (9th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (9th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (10th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (10th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (11th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (11th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (12th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (12th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 1 (13th door)")
            defense_locations_list.append("CI Defense: Basement Glass on Door 2 (13th door)")
            defense_locations_list.append("CI Defense: Firing Range Glass 1")
            defense_locations_list.append("CI Defense: Firing Range RC-P120 Glass")
            defense_locations_list.append("CI Defense: Firing Range Ceiling Glass 1")
            defense_locations_list.append("CI Defense: Firing Range Ceiling Glass 2")
            defense_locations_list.append("CI Defense: Firing Range Ceiling Glass 3")
            defense_locations_list.append("CI Defense: Firing Range Ceiling Glass 4")
            defense_locations_list.append("CI Defense: Device Lab Glass 1")
            defense_locations_list.append("CI Defense: Device Lab Glass 2")
            defense_locations_list.append("CI Defense: Info Room Glass 1")
            defense_locations_list.append("CI Defense: Info Room Glass 2")
            defense_locations_list.append("CI Defense: Joanna's Office Glass 1")
            defense_locations_list.append("CI Defense: Joanna's Office Glass 2")
            defense_locations_list.append("CI Defense: Carrington's Office Glass 1")
            defense_locations_list.append("CI Defense: Carrington's Office Glass 2")

        if world.options.special_agent or world.options.perfect_agent:
            if "dD Investigation" not in world.options.excluded_missions:
                investigation_locations_list.append("dD Investigation: Glass 1 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 2 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 3 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 4 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 5 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 6 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 7 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 8 (room with one scientist)")
                investigation_locations_list.append("dD Investigation: Glass 1 (room near two scientists)")
                investigation_locations_list.append("dD Investigation: Glass 2 (room near two scientists)")
                investigation_locations_list.append("dD Investigation: Glass 3 (room near two scientists)")
                investigation_locations_list.append("dD Investigation: Glass 4 (room near two scientists)")

            if "Pelagic II" not in world.options.excluded_missions:
                pelagic_locations_list.append("Pelagic II: Glass on Door 4 (lower floors)")
                pelagic_locations_list.append("Pelagic II: Glass on Door 5 (lower floors)")
                pelagic_locations_list.append("Pelagic II: Glass on Door 6 (lower floors)")
                pelagic_locations_list.append("Pelagic II: Glass on Door 7 (lower floors)")

            if "Attack Ship" not in world.options.excluded_missions:
                attackship_locations_list.append("Attack Ship: Engine System Glass 1")
                attackship_locations_list.append("Attack Ship: Engine System Glass 2")
                attackship_locations_list.append("Attack Ship: Engine System Glass 3")
                attackship_locations_list.append("Attack Ship: Engine System Glass 4")
                attackship_locations_list.append("Attack Ship: Engine System Glass 5")
                attackship_locations_list.append("Attack Ship: Engine System Glass 6")

        if world.options.perfect_agent:
            if "Pelagic II" not in world.options.excluded_missions:
                pelagic_locations_list.append("Pelagic II: Glass on Door 1 (near research tapes)")
                pelagic_locations_list.append("Pelagic II: Glass on Door 2 (near research tapes)")

            if "Deep Sea" not in world.options.excluded_missions:
                deepsea_locations_list.append("Deep Sea: Glass 1 (1st power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (1st power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (1st power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (2nd power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (2nd power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (2nd power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (3rd power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (3rd power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (3rd power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (4th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (4th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (4th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (5th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (5th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (5th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (6th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (7th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (8th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (9th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (10th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (11th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 1 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 2 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 3 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 4 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 5 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 6 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 7 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 8 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 9 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 10 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 11 (12th power node)")
                deepsea_locations_list.append("Deep Sea: Glass 12 (12th power node)")

        if world.options.weapon_progression.value >= WeaponProgression.option_all_guns:
            if "dD Investigation" not in world.options.excluded_missions:
                investigation_locations_list.append("dD Investigation: Glass 2 (room with glass enclosure)")
                investigation_locations_list.append("dD Investigation: Glass 3 (room with glass enclosure)")

            if "G5 Building" not in world.options.excluded_missions:
                g5_locations_list.append("G5 Building: Glass (first room)")

            if "Air Base" not in world.options.excluded_missions:
                airbase_locations_list.append("Air Base: Window (near escalator)")
                airbase_locations_list.append("Air Base: Window (in front of plane)")

            if "CI Defense" not in world.options.excluded_missions:
                defense_locations_list.append("CI Defense: Firing Range Glass 2")
                defense_locations_list.append("CI Defense: Firing Range Glass 3")
                defense_locations_list.append("CI Defense: Firing Range Glass 4")
                defense_locations_list.append("CI Defense: Firing Range Glass 5")
                defense_locations_list.append("CI Defense: Firing Range Glass 6")
                defense_locations_list.append("CI Defense: Firing Range Glass 7")
                defense_locations_list.append("CI Defense: Firing Range Glass 8")


    institute_locations = get_location_names_with_ids(institute_locations_list)
    carrington_institute.add_locations(institute_locations, PerfectDarkLocation)

    defection_locations = get_location_names_with_ids(defection_locations_list)
    defection.add_locations(defection_locations, PerfectDarkLocation)

    investigation_locations = get_location_names_with_ids(investigation_locations_list)
    investigation.add_locations(investigation_locations, PerfectDarkLocation)

    extraction_locations = get_location_names_with_ids(extraction_locations_list)
    extraction.add_locations(extraction_locations, PerfectDarkLocation)

    villa_locations = get_location_names_with_ids(villa_locations_list)
    villa.add_locations(villa_locations, PerfectDarkLocation)

    chicago_locations = get_location_names_with_ids(chicago_locations_list)
    chicago.add_locations(chicago_locations, PerfectDarkLocation)

    g5_building_locations = get_location_names_with_ids(g5_locations_list)
    g5_building.add_locations(g5_building_locations, PerfectDarkLocation)

    infiltration_locations = get_location_names_with_ids(infiltration_locations_list)
    infiltration.add_locations(infiltration_locations, PerfectDarkLocation)

    rescue_locations = get_location_names_with_ids(rescue_locations_list)
    rescue.add_locations(rescue_locations, PerfectDarkLocation)

    escape_locations = get_location_names_with_ids(escape_locations_list)
    escape.add_locations(escape_locations, PerfectDarkLocation)

    air_base_locations = get_location_names_with_ids(airbase_locations_list)
    air_base.add_locations(air_base_locations, PerfectDarkLocation)

    air_force_one_locations = get_location_names_with_ids(afo_locations_list)
    air_force_one.add_locations(air_force_one_locations, PerfectDarkLocation)

    crash_site_locations = get_location_names_with_ids(crashsite_locations_list)
    crash_site.add_locations(crash_site_locations, PerfectDarkLocation)

    pelagic_locations = get_location_names_with_ids(pelagic_locations_list)
    pelagic.add_locations(pelagic_locations, PerfectDarkLocation)

    deep_sea_locations = get_location_names_with_ids(deepsea_locations_list)
    deep_sea.add_locations(deep_sea_locations, PerfectDarkLocation)

    institute_defense_locations = get_location_names_with_ids(defense_locations_list)
    institute_defense.add_locations(institute_defense_locations, PerfectDarkLocation)

    attack_ship_locations = get_location_names_with_ids(attackship_locations_list)
    attack_ship.add_locations(attack_ship_locations, PerfectDarkLocation)

    skedar_ruins_locations = get_location_names_with_ids(skedarruins_locations_list)
    skedar_ruins.add_locations(skedar_ruins_locations, PerfectDarkLocation)

    mbr_locations = get_location_names_with_ids(mbr_locations_list)
    mbr.add_locations(mbr_locations, PerfectDarkLocation)

    maian_sos_locations = get_location_names_with_ids(maiansos_locations_list)
    maian_sos.add_locations(maian_sos_locations, PerfectDarkLocation)

    war_locations = get_location_names_with_ids(war_locations_list)
    war.add_locations(war_locations, PerfectDarkLocation)

    duel_locations = get_location_names_with_ids(duel_locations_list)
    duel.add_locations(duel_locations, PerfectDarkLocation)

    dd_central_locations = get_location_names_with_ids(dd_central_locations_list)
    dd_central.add_locations(dd_central_locations, PerfectDarkLocation)

    inner_a51_locations = get_location_names_with_ids(inner_a51_locations_list)
    inner_a51.add_locations(inner_a51_locations, PerfectDarkLocation)
