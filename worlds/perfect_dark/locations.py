from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, LocationProgressType

from . import items

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements, MissionLogic, AlternateExits
from .items import has_challenges

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
    "dD Defection: 3F Shield - (Agent/Special)": 2010,
    "dD Defection: 2F double Falcon 2 (silencer)": 2033,
    "dD Defection: 2F Laptop Gun": 2466,
    "dD Defection: 2F Falcon 2 (silencer) (right side)": 2468,
    "dD Defection: 2F Falcon 2 (silencer) (left side)": 2469,
    "dD Defection: 3F tiny ammo box (on corner desk)": 2470,
    "dD Defection: 3F tiny ammo box (on table near couch)": 2471,
    "dD Defection: 2F tiny ammo box (on desk across the stairs)": 2472,
    "dD Defection: 2F tiny ammo box (on desk across the elevator)": 2473,
    "dD Defection: 2F Falcon 2 (silencer) (on desk)": 2474,
    "dD Defection: 2F tiny ammo box (under stairs)": 2475,
    "dD Defection: 1F CMP150 (on right of front desk)": 2605,
    "dD Defection: 1F CMP150 (on left of front desk)": 2606,
    "dD Defection: 1F Shield - (Agent)": 2607,
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
    "dD Investigation: Shield (on crate) - (Agent)": 4638,
    "dD Investigation: Shield (behind the glass) - (Agent/Special)": 4639,
    "dD Extraction: 1F DY357 Magnum (from fifth guard)": 6005,
    "dD Extraction: 2F Shield - (Agent)": 6120,
    "dD Extraction: 4F Rocket Launcher": 6452,
    "dD Extraction: 4F Grenade (on Cassandra's desk)": 6466,
    "dD Extraction: 4F Dragon (in hidden room in Cassandra's office)": 6467,
    "dD Extraction: Roof ammo box (on left) - (Agent)": 6516,
    "dD Extraction: Roof ammo box (on right) - (Agent)": 6519,
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
    "Carrington Villa: Sniper Rifle (in the bathroom) - (Perfect Agent)": 8085,
    "Carrington Villa: double CMP150 (from sniper near the helipad)": 8410,
    "Carrington Villa: Shield (on helipad crate) - (Agent)": 8568,
    "Carrington Villa: Shield (in the bathroom) - (Agent)": 8569,
    "Chicago: BombSpy (in the dumpster)": 10000,
    "Chicago: double Falcon 2 (scope) (in the Pond Punk)": 10287,
    "Chicago: Shield (near the taxi) - (Agent)": 10289,
    "Chicago: Shield (under stairs near Pond Punk) - (Agent/Special)": 10290,
    "G5 Building: Crossbow (after knocking out first two guards)": 12000,
    "G5 Building: Shield (on stairs to the upper exit) - (Agent/Special)": 12086,
    "G5 Building: N-Bomb (near the upper exit)": 12149,
    "G5 Building: Shield (in room before the laser grids) - (Agent)": 12150,
    "A51 Infiltration: Rocket Launcher (in mine field)": 14052,
    "A51 Infiltration: double MagSec 4 (after placing comms rider)": 14053,
    "A51 Infiltration: Shield (near hoverbike) - (Agent)": 14150,
    "A51 Infiltration: Shield (in the crawl space) - (Agent/Special)": 15381,
    "A51 Rescue: Shield (guard past first elevator) - (Agent)": 16004,
    "A51 Rescue: Phoenix (past locked hangar door)": 16905,
    "A51 Rescue: double Falcon 2 (silencer) (hidden in barrel)": 16987,
    "A51 Rescue: Shield (on desk near computer) - (Agent/Special)": 17140,
    "A51 Escape: double Falcon 2 (scope) (behind you at the start)": 18036,
    "A51 Escape: Shield (dropped by biotechnician) - (Agent)": 18040,
    "A51 Escape: Shield (behind locked medical containment doors) - (Agent/Special)": 18895,
    "A51 Escape: Remote Mine (in first room with guards)": 19383,
    "Air Base: Shield (dropped by NSA Lackey) - (Agent)": 20017,
    "Air Base: double DY357 Magnum (after knocking out all NSA Lackeys)": 20018,
    "Air Base: Proximity Mine (past the cave)": 20181,
    "Air Base: Shield (in the safe) - (Agent/Special)": 20214,
    "Air Force One: Cyclone (in room right of stairs)": 22203,
    "Air Force One: Cyclone (in room left of stairs)": 22204,
    "Air Force One: Shield (in piano room) - (Agent/Special)": 22363,
    "Air Force One: Shield (in small kitchen) - (Agent)": 22364,
    "Crash Site: DY357-LX (from disarming Trent)": 24001,
    "Crash Site: Shield (behind President's clone) - (Agent/Special)": 24144,
    "Crash Site: Shield (near the crashed UFO) - (Agent)": 24262, 
    "Crash Site: Proximity Mine (from Elvis before doing any objective)": 24263, # Shares same pad as Shield (need to add one for the location)
    "Pelagic II: double Falcon 2 (silencer) (from guard and no alarm)": 26052,
    "Pelagic II: Shield (on the helipad) - (Agent)": 26541,
    "Pelagic II: Shield (on the sub hangar crate) - (Agent/Special)": 26542,
    "Deep Sea: Proximity Mine (from guard in 2nd room with cloaked guards)": 28008,
    "Deep Sea: Shield (on the left path) - (Agent/Special)": 28018,
    # "Deep Sea: Shield (dropped from guard) - (Agent)": 28026,
    # "Deep Sea: Shotgun (near Shield on the left path)": 28063,
    "CI Defense: Devastator (dropped after saving most of the hostages)": 30000,
    "CI Defense: Basement Shield - (Agent/Special)": 30146,
    "CI Defense: 2F Shield - (Agent)": 30648,
    "Attack Ship: double Mauler (dropped from Skedar in final room)": 32045,
    "Attack Ship: De Vries' necklace - (Perfect Agent)": 32051,
    "Attack Ship: Slayer (in the room past green chambers)": 32466,
    "Attack Ship: Shield (on table) - (Agent/Special)": 32499,
    "Skedar Ruins: double Phoenix (near the gap)": 34050,
    "Skedar Ruins: Shield (area past the gap to the right) - (Agent/Special)": 34186,
    "Skedar Ruins: Shield (behind the fallen pillar) - (Agent)": 34337,
    "Mr. Blonde's Revenge: 3F Shield - (Agent/Special)": 36010,
    "Mr. Blonde's Revenge: 1F double CMP150 (from guard near bottom elevator)": 36015,
    "Mr. Blonde's Revenge: 2F Laptop Gun": 36466,
    "Mr. Blonde's Revenge: 2F Falcon 2 (right side)": 36468,
    "Mr. Blonde's Revenge: 2F Falcon 2 (left side)": 36469,
    "Mr. Blonde's Revenge: 3F tiny ammo box (on corner desk)": 36470,
    "Mr. Blonde's Revenge: 3F tiny ammo box (on table near couch)": 36471,
    "Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the stairs)": 36472,
    "Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the elevator)": 36473,
    "Mr. Blonde's Revenge: 2F Falcon 2 (on desk)": 36474,
    "Mr. Blonde's Revenge: 2F tiny ammo box (under stairs)": 36475,
    "Mr. Blonde's Revenge: 1F CMP150 (on right of front desk)": 36605,
    "Mr. Blonde's Revenge: 1F CMP150 (on left of front desk)": 36606,
    "Mr. Blonde's Revenge: 1F Shield - (Agent)": 36607,
    "Maian SOS: double DY357-LX (from dual-wielding guard)": 38011,
    "Maian SOS: Psychosis Gun (on desk near the start)": 38919,
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
    

    # Missions
    if world.options.agent:
        defection_locations_list.append("dD Defection - Agent Objective 1")
        defection_locations_list.append("Complete: dD Defection - Agent")
        investigation_locations_list.append("dD Investigation - Agent Objective 1")
        investigation_locations_list.append("dD Investigation - Agent Objective 2")
        investigation_locations_list.append("Complete: dD Investigation - Agent")
        extraction_locations_list.append("dD Extraction - Agent Objective 1")
        extraction_locations_list.append("dD Extraction - Agent Objective 2")
        extraction_locations_list.append("dD Extraction - Agent Objective 3")
        extraction_locations_list.append("Complete: dD Extraction - Agent")
        villa_locations_list.append("Carrington Villa - Agent Objective 1")
        villa_locations_list.append("Carrington Villa - Agent Objective 2")
        villa_locations_list.append("Carrington Villa - Agent Objective 3")
        villa_locations_list.append("Complete: Carrington Villa - Agent")
        chicago_locations_list.append("Chicago - Agent Objective 1")
        chicago_locations_list.append("Chicago - Agent Objective 2")
        chicago_locations_list.append("Chicago - Agent Objective 3")
        chicago_locations_list.append("Complete: Chicago - Agent")
        g5_locations_list.append("G5 Building - Agent Objective 1")
        g5_locations_list.append("G5 Building - Agent Objective 2")
        g5_locations_list.append("G5 Building - Agent Objective 3")
        g5_locations_list.append("Complete: G5 Building - Agent")
        infiltration_locations_list.append("A51 Infiltration - Agent Objective 1")
        infiltration_locations_list.append("A51 Infiltration - Agent Objective 2")
        infiltration_locations_list.append("A51 Infiltration - Agent Objective 3")
        infiltration_locations_list.append("Complete: A51 Infiltration - Agent")
        rescue_locations_list.append("A51 Rescue - Agent Objective 1")
        rescue_locations_list.append("A51 Rescue - Agent Objective 2")
        rescue_locations_list.append("A51 Rescue - Agent Objective 3")
        rescue_locations_list.append("Complete: A51 Rescue - Agent")
        escape_locations_list.append("A51 Escape - Agent Objective 1")
        escape_locations_list.append("A51 Escape - Agent Objective 2")
        escape_locations_list.append("A51 Escape - Agent Objective 3")
        escape_locations_list.append("Complete: A51 Escape - Agent")
        airbase_locations_list.append("Air Base - Agent Objective 1")
        airbase_locations_list.append("Air Base - Agent Objective 2")
        airbase_locations_list.append("Air Base - Agent Objective 3")
        airbase_locations_list.append("Complete: Air Base - Agent")
        afo_locations_list.append("Air Force One - Agent Objective 1")
        afo_locations_list.append("Air Force One - Agent Objective 2")
        afo_locations_list.append("Air Force One - Agent Objective 3")
        afo_locations_list.append("Complete: Air Force One - Agent")
        crashsite_locations_list.append("Crash Site - Agent Objective 1")
        crashsite_locations_list.append("Crash Site - Agent Objective 2")
        crashsite_locations_list.append("Crash Site - Agent Objective 3")
        crashsite_locations_list.append("Complete: Crash Site - Agent")
        pelagic_locations_list.append("Pelagic II - Agent Objective 1")
        pelagic_locations_list.append("Pelagic II - Agent Objective 2")
        pelagic_locations_list.append("Pelagic II - Agent Objective 3")
        pelagic_locations_list.append("Complete: Pelagic II - Agent")
        deepsea_locations_list.append("Deep Sea - Agent Objective 1")
        deepsea_locations_list.append("Deep Sea - Agent Objective 2")
        deepsea_locations_list.append("Deep Sea - Agent Objective 3")
        deepsea_locations_list.append("Complete: Deep Sea - Agent")
        defense_locations_list.append("CI Defense - Agent Objective 1")
        defense_locations_list.append("CI Defense - Agent Objective 2")
        defense_locations_list.append("CI Defense - Agent Objective 3")
        defense_locations_list.append("Complete: CI Defense - Agent")
        attackship_locations_list.append("Attack Ship - Agent Objective 1")
        attackship_locations_list.append("Attack Ship - Agent Objective 2")
        attackship_locations_list.append("Attack Ship - Agent Objective 3")
        attackship_locations_list.append("Complete: Attack Ship - Agent")
        skedarruins_locations_list.append("Skedar Ruins - Agent Objective 1")
        skedarruins_locations_list.append("Skedar Ruins - Agent Objective 2")
        skedarruins_locations_list.append("Skedar Ruins - Agent Objective 3")
        skedarruins_locations_list.append("Complete: Skedar Ruins - Agent")
        mbr_locations_list.append("Mr. Blonde's Revenge - Agent Objective 1")
        mbr_locations_list.append("Complete: Mr. Blonde's Revenge - Agent")
        maiansos_locations_list.append("Maian SOS - Agent Objective 1")
        maiansos_locations_list.append("Complete: Maian SOS - Agent")
        war_locations_list.append("WAR! - Agent Objective 1")
        war_locations_list.append("Complete: WAR! - Agent")
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

            g5_item = world.random.choice(g5_building_exits)
            escape_item = world.random.choice(escape_exits)
            air_base_item = world.random.choice(air_base_exits)

            g5_locations_list.append(g5_item)
            escape_locations_list.append(escape_item)
            airbase_locations_list.append(air_base_item)
            
        elif world.options.alternate_exits.value == AlternateExits.option_all:
            g5_locations_list.append("Complete G5 Building (Agent): Bottom Exit")
            g5_locations_list.append("Complete G5 Building (Agent): Upper Exit")
            escape_locations_list.append("Complete A51 Escape (Agent): UFO Escape")
            escape_locations_list.append("Complete A51 Escape (Agent): Alternate Escape")
            airbase_locations_list.append("Complete Air Base (Agent): Shuttle Exit")
            airbase_locations_list.append("Complete Air Base (Agent): Ladder Exit")


    if world.options.special_agent:
        defection_locations_list.append("dD Defection - Special Agent Objective 1")
        defection_locations_list.append("dD Defection - Special Agent Objective 2")
        defection_locations_list.append("dD Defection - Special Agent Objective 3")
        defection_locations_list.append("dD Defection - Special Agent Objective 4")
        defection_locations_list.append("Complete: dD Defection - Special Agent")
        investigation_locations_list.append("dD Investigation - Special Agent Objective 1")
        investigation_locations_list.append("dD Investigation - Special Agent Objective 2")
        investigation_locations_list.append("dD Investigation - Special Agent Objective 3")
        investigation_locations_list.append("dD Investigation - Special Agent Objective 4")
        investigation_locations_list.append("Complete: dD Investigation - Special Agent")
        extraction_locations_list.append("dD Extraction - Special Agent Objective 1")
        extraction_locations_list.append("dD Extraction - Special Agent Objective 2")
        extraction_locations_list.append("dD Extraction - Special Agent Objective 3")
        extraction_locations_list.append("dD Extraction - Special Agent Objective 4")
        extraction_locations_list.append("Complete: dD Extraction - Special Agent")
        villa_locations_list.append("Carrington Villa - Special Agent Objective 1")
        villa_locations_list.append("Carrington Villa - Special Agent Objective 2")
        villa_locations_list.append("Carrington Villa - Special Agent Objective 3")
        villa_locations_list.append("Carrington Villa - Special Agent Objective 4")
        villa_locations_list.append("Complete: Carrington Villa - Special Agent")
        chicago_locations_list.append("Chicago - Special Agent Objective 1")
        chicago_locations_list.append("Chicago - Special Agent Objective 2")
        chicago_locations_list.append("Chicago - Special Agent Objective 3")
        chicago_locations_list.append("Chicago - Special Agent Objective 4")
        chicago_locations_list.append("Complete: Chicago - Special Agent")
        g5_locations_list.append("G5 Building - Special Agent Objective 1")
        g5_locations_list.append("G5 Building - Special Agent Objective 2")
        g5_locations_list.append("G5 Building - Special Agent Objective 3")
        g5_locations_list.append("G5 Building - Special Agent Objective 4")
        g5_locations_list.append("Complete: G5 Building - Special Agent")
        infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 1")
        infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 2")
        infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 3")
        infiltration_locations_list.append("A51 Infiltration - Special Agent Objective 4")
        infiltration_locations_list.append("Complete: A51 Infiltration - Special Agent")
        rescue_locations_list.append("A51 Rescue - Special Agent Objective 1")
        rescue_locations_list.append("A51 Rescue - Special Agent Objective 2")
        rescue_locations_list.append("A51 Rescue - Special Agent Objective 3")
        rescue_locations_list.append("A51 Rescue - Special Agent Objective 4")
        rescue_locations_list.append("Complete: A51 Rescue - Special Agent")
        escape_locations_list.append("A51 Escape - Special Agent Objective 1")
        escape_locations_list.append("A51 Escape - Special Agent Objective 2")
        escape_locations_list.append("A51 Escape - Special Agent Objective 3")
        escape_locations_list.append("A51 Escape - Special Agent Objective 4")
        escape_locations_list.append("Complete: A51 Escape - Special Agent")
        airbase_locations_list.append("Air Base - Special Agent Objective 1")
        airbase_locations_list.append("Air Base - Special Agent Objective 2")
        airbase_locations_list.append("Air Base - Special Agent Objective 3")
        airbase_locations_list.append("Air Base - Special Agent Objective 4")
        airbase_locations_list.append("Complete: Air Base - Special Agent")
        afo_locations_list.append("Air Force One - Special Agent Objective 1")
        afo_locations_list.append("Air Force One - Special Agent Objective 2")
        afo_locations_list.append("Air Force One - Special Agent Objective 3")
        afo_locations_list.append("Air Force One - Special Agent Objective 4")
        afo_locations_list.append("Complete: Air Force One - Special Agent")
        crashsite_locations_list.append("Crash Site - Special Agent Objective 1")
        crashsite_locations_list.append("Crash Site - Special Agent Objective 2")
        crashsite_locations_list.append("Crash Site - Special Agent Objective 3")
        crashsite_locations_list.append("Crash Site - Special Agent Objective 4")
        crashsite_locations_list.append("Complete: Crash Site - Special Agent")
        pelagic_locations_list.append("Pelagic II - Special Agent Objective 1")
        pelagic_locations_list.append("Pelagic II - Special Agent Objective 2")
        pelagic_locations_list.append("Pelagic II - Special Agent Objective 3")
        pelagic_locations_list.append("Pelagic II - Special Agent Objective 4")
        pelagic_locations_list.append("Complete: Pelagic II - Special Agent")
        deepsea_locations_list.append("Deep Sea - Special Agent Objective 1")
        deepsea_locations_list.append("Deep Sea - Special Agent Objective 2")
        deepsea_locations_list.append("Deep Sea - Special Agent Objective 3")
        deepsea_locations_list.append("Deep Sea - Special Agent Objective 4")
        deepsea_locations_list.append("Complete: Deep Sea - Special Agent")
        defense_locations_list.append("CI Defense - Special Agent Objective 1")
        defense_locations_list.append("CI Defense - Special Agent Objective 2")
        defense_locations_list.append("CI Defense - Special Agent Objective 3")
        defense_locations_list.append("CI Defense - Special Agent Objective 4")
        defense_locations_list.append("Complete: CI Defense - Special Agent")
        attackship_locations_list.append("Attack Ship - Special Agent Objective 1")
        attackship_locations_list.append("Attack Ship - Special Agent Objective 2")
        attackship_locations_list.append("Attack Ship - Special Agent Objective 3")
        attackship_locations_list.append("Attack Ship - Special Agent Objective 4")
        attackship_locations_list.append("Complete: Attack Ship - Special Agent")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 1")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 2")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 3")
        skedarruins_locations_list.append("Skedar Ruins - Special Agent Objective 4")
        skedarruins_locations_list.append("Complete: Skedar Ruins - Special Agent")
        mbr_locations_list.append("Mr. Blonde's Revenge - Special Agent Objective 1")
        mbr_locations_list.append("Mr. Blonde's Revenge - Special Agent Objective 2")
        mbr_locations_list.append("Complete: Mr. Blonde's Revenge - Special Agent")
        maiansos_locations_list.append("Maian SOS - Special Agent Objective 1")
        maiansos_locations_list.append("Maian SOS - Special Agent Objective 2")
        maiansos_locations_list.append("Complete: Maian SOS - Special Agent")
        war_locations_list.append("WAR! - Special Agent Objective 1")
        war_locations_list.append("WAR! - Special Agent Objective 2")
        war_locations_list.append("Complete: WAR! - Special Agent")
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

            g5_item = world.random.choice(g5_building_exits)
            escape_item = world.random.choice(escape_exits)
            air_base_item = world.random.choice(air_base_exits)

            g5_locations_list.append(g5_item)
            escape_locations_list.append(escape_item)
            airbase_locations_list.append(air_base_item)
            
        elif world.options.alternate_exits.value == AlternateExits.option_all:
            g5_locations_list.append("Complete G5 Building (Special Agent): Bottom Exit")
            g5_locations_list.append("Complete G5 Building (Special Agent): Upper Exit")
            escape_locations_list.append("Complete A51 Escape (Special Agent): UFO Escape")
            escape_locations_list.append("Complete A51 Escape (Special Agent): Alternate Escape")
            airbase_locations_list.append("Complete Air Base (Special Agent): Shuttle Exit")
            airbase_locations_list.append("Complete Air Base (Special Agent): Ladder Exit")


    if world.options.perfect_agent:
        defection_locations_list.append("dD Defection - Perfect Agent Objective 1")
        defection_locations_list.append("dD Defection - Perfect Agent Objective 2")
        defection_locations_list.append("dD Defection - Perfect Agent Objective 3")
        defection_locations_list.append("dD Defection - Perfect Agent Objective 4")
        defection_locations_list.append("dD Defection - Perfect Agent Objective 5")
        defection_locations_list.append("Complete: dD Defection - Perfect Agent")
        investigation_locations_list.append("dD Investigation - Perfect Agent Objective 1")
        investigation_locations_list.append("dD Investigation - Perfect Agent Objective 2")
        investigation_locations_list.append("dD Investigation - Perfect Agent Objective 3")
        investigation_locations_list.append("dD Investigation - Perfect Agent Objective 4")
        investigation_locations_list.append("dD Investigation - Perfect Agent Objective 5")
        investigation_locations_list.append("Complete: dD Investigation - Perfect Agent")
        extraction_locations_list.append("dD Extraction - Perfect Agent Objective 1")
        extraction_locations_list.append("dD Extraction - Perfect Agent Objective 2")
        extraction_locations_list.append("dD Extraction - Perfect Agent Objective 3")
        extraction_locations_list.append("dD Extraction - Perfect Agent Objective 4")
        extraction_locations_list.append("dD Extraction - Perfect Agent Objective 5")
        extraction_locations_list.append("Complete: dD Extraction - Perfect Agent")
        villa_locations_list.append("Carrington Villa - Perfect Agent Objective 1")
        villa_locations_list.append("Carrington Villa - Perfect Agent Objective 2")
        villa_locations_list.append("Carrington Villa - Perfect Agent Objective 3")
        villa_locations_list.append("Carrington Villa - Perfect Agent Objective 4")
        villa_locations_list.append("Carrington Villa - Perfect Agent Objective 5")
        villa_locations_list.append("Complete: Carrington Villa - Perfect Agent")
        chicago_locations_list.append("Chicago - Perfect Agent Objective 1")
        chicago_locations_list.append("Chicago - Perfect Agent Objective 2")
        chicago_locations_list.append("Chicago - Perfect Agent Objective 3")
        chicago_locations_list.append("Chicago - Perfect Agent Objective 4")
        chicago_locations_list.append("Chicago - Perfect Agent Objective 5")
        chicago_locations_list.append("Complete: Chicago - Perfect Agent")
        g5_locations_list.append("G5 Building - Perfect Agent Objective 1")
        g5_locations_list.append("G5 Building - Perfect Agent Objective 2")
        g5_locations_list.append("G5 Building - Perfect Agent Objective 3")
        g5_locations_list.append("G5 Building - Perfect Agent Objective 4")
        g5_locations_list.append("G5 Building - Perfect Agent Objective 5")
        g5_locations_list.append("Complete: G5 Building - Perfect Agent")
        infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 1")
        infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 2")
        infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 3")
        infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 4")
        infiltration_locations_list.append("A51 Infiltration - Perfect Agent Objective 5")
        infiltration_locations_list.append("Complete: A51 Infiltration - Perfect Agent")
        rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 1")
        rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 2")
        rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 3")
        rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 4")
        rescue_locations_list.append("A51 Rescue - Perfect Agent Objective 5")
        rescue_locations_list.append("Complete: A51 Rescue - Perfect Agent")
        escape_locations_list.append("A51 Escape - Perfect Agent Objective 1")
        escape_locations_list.append("A51 Escape - Perfect Agent Objective 2")
        escape_locations_list.append("A51 Escape - Perfect Agent Objective 3")
        escape_locations_list.append("A51 Escape - Perfect Agent Objective 4")
        escape_locations_list.append("A51 Escape - Perfect Agent Objective 5")
        escape_locations_list.append("Complete: A51 Escape - Perfect Agent")
        airbase_locations_list.append("Air Base - Perfect Agent Objective 1")
        airbase_locations_list.append("Air Base - Perfect Agent Objective 2")
        airbase_locations_list.append("Air Base - Perfect Agent Objective 3")
        airbase_locations_list.append("Air Base - Perfect Agent Objective 4")
        airbase_locations_list.append("Air Base - Perfect Agent Objective 5")
        airbase_locations_list.append("Complete: Air Base - Perfect Agent")
        afo_locations_list.append("Air Force One - Perfect Agent Objective 1")
        afo_locations_list.append("Air Force One - Perfect Agent Objective 2")
        afo_locations_list.append("Air Force One - Perfect Agent Objective 3")
        afo_locations_list.append("Air Force One - Perfect Agent Objective 4")
        afo_locations_list.append("Air Force One - Perfect Agent Objective 5")
        afo_locations_list.append("Complete: Air Force One - Perfect Agent")
        crashsite_locations_list.append("Crash Site - Perfect Agent Objective 1")
        crashsite_locations_list.append("Crash Site - Perfect Agent Objective 2")
        crashsite_locations_list.append("Crash Site - Perfect Agent Objective 3")
        crashsite_locations_list.append("Crash Site - Perfect Agent Objective 4")
        crashsite_locations_list.append("Crash Site - Perfect Agent Objective 5")
        crashsite_locations_list.append("Complete: Crash Site - Perfect Agent")
        pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 1")
        pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 2")
        pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 3")
        pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 4")
        pelagic_locations_list.append("Pelagic II - Perfect Agent Objective 5")
        pelagic_locations_list.append("Complete: Pelagic II - Perfect Agent")
        deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 1")
        deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 2")
        deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 3")
        deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 4")
        deepsea_locations_list.append("Deep Sea - Perfect Agent Objective 5")
        deepsea_locations_list.append("Complete: Deep Sea - Perfect Agent")
        defense_locations_list.append("CI Defense - Perfect Agent Objective 1")
        defense_locations_list.append("CI Defense - Perfect Agent Objective 2")
        defense_locations_list.append("CI Defense - Perfect Agent Objective 3")
        defense_locations_list.append("CI Defense - Perfect Agent Objective 4")
        defense_locations_list.append("CI Defense - Perfect Agent Objective 5")
        defense_locations_list.append("Complete: CI Defense - Perfect Agent")
        attackship_locations_list.append("Attack Ship - Perfect Agent Objective 1")
        attackship_locations_list.append("Attack Ship - Perfect Agent Objective 2")
        attackship_locations_list.append("Attack Ship - Perfect Agent Objective 3")
        attackship_locations_list.append("Attack Ship - Perfect Agent Objective 4")
        attackship_locations_list.append("Attack Ship - Perfect Agent Objective 5")
        attackship_locations_list.append("Complete: Attack Ship - Perfect Agent")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 1")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 2")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 3")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 4")
        skedarruins_locations_list.append("Skedar Ruins - Perfect Agent Objective 5")
        skedarruins_locations_list.append("Complete: Skedar Ruins - Perfect Agent")
        mbr_locations_list.append("Mr. Blonde's Revenge - Perfect Agent Objective 1")
        mbr_locations_list.append("Mr. Blonde's Revenge - Perfect Agent Objective 2")
        mbr_locations_list.append("Mr. Blonde's Revenge - Perfect Agent Objective 3")
        mbr_locations_list.append("Complete: Mr. Blonde's Revenge - Perfect Agent")
        maiansos_locations_list.append("Maian SOS - Perfect Agent Objective 1")
        maiansos_locations_list.append("Maian SOS - Perfect Agent Objective 2")
        maiansos_locations_list.append("Maian SOS - Perfect Agent Objective 3")
        maiansos_locations_list.append("Complete: Maian SOS - Perfect Agent")
        war_locations_list.append("WAR! - Perfect Agent Objective 1")
        war_locations_list.append("WAR! - Perfect Agent Objective 2")
        war_locations_list.append("WAR! - Perfect Agent Objective 3")
        war_locations_list.append("Complete: WAR! - Perfect Agent")
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

            g5_item = world.random.choice(g5_building_exits)
            escape_item = world.random.choice(escape_exits)
            air_base_item = world.random.choice(air_base_exits)

            g5_locations_list.append(g5_item)
            escape_locations_list.append(escape_item)
            airbase_locations_list.append(air_base_item)
            
        elif world.options.alternate_exits.value == AlternateExits.option_all:
            g5_locations_list.append("Complete G5 Building (Perfect Agent): Bottom Exit")
            g5_locations_list.append("Complete G5 Building (Perfect Agent): Upper Exit")
            escape_locations_list.append("Complete A51 Escape (Perfect Agent): UFO Escape")
            escape_locations_list.append("Complete A51 Escape (Perfect Agent): Alternate Escape")
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


    if ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value >= SkedarRuinsRequirements.option_collect_mission_stars)
            or world.options.goal.value >= Goal.option_complete_missions):
        institute_locations_list.append("Collect All Stars")


    if has_challenges(world):
        for x in range(1, 31):
            challenge_name = f"Challenge {x}"
            if (world.options.excluded_challenges.__contains__(challenge_name) == False):
                challenge_location = f"Complete: Challenge {x}"
                institute_locations_list.append(challenge_location)

        if world.options.multiplayer_unlocks:
            # institute_locations_list.append("Complete Challenges: Unused First Unlock")
            institute_locations_list.append("Complete 1 Challenge: FarSight XR-20 Unlock")
            institute_locations_list.append("Complete 7 Challenges: Tranquilizer Unlock")
            institute_locations_list.append("Complete 4 Challenges: SuperDragon Unlock")
            institute_locations_list.append("Complete 13 Challenges: Slayer Unlock")
            institute_locations_list.append("Complete 3 Challenges: Falcon 2 (Silencer) Unlock")
            institute_locations_list.append("Complete 8 Challenges: Falcon 2 (Scope) Unlock")
            institute_locations_list.append("Complete 16 Challenges: Mauler Unlock")
            institute_locations_list.append("Complete 14 Challenges: Phoenix Unlock")
            institute_locations_list.append("Complete 20 Challenges: DY357-LX Unlock")
            institute_locations_list.append("Complete 17 Challenges: Callisto NTG Unlock")
            institute_locations_list.append("Complete 5 Challenges: Laptop Gun Unlock")
            # institute_locations_list.append("Complete Challenges: K7 Avenger Unlock")
            institute_locations_list.append("Complete 19 Challenges: RC-P120 Unlock")
            institute_locations_list.append("Complete 2 Challenges: Shotgun Unlock")
            institute_locations_list.append("Complete 9 Challenges: Reaper Unlock")
            institute_locations_list.append("Complete 11 Challenges: Devastator Unlock")
            institute_locations_list.append("Complete 18 Challenges: Crossbow Unlock")
            institute_locations_list.append("Complete 21 Challenges: N-Bomb Unlock")
            institute_locations_list.append("Complete 12 Challenges: Proximity Mine Unlock")
            institute_locations_list.append("Complete 6 Challenges: Remote Mine Unlock")
            # institute_locations_list.append("Complete Challenges: X-Ray Scanner Unlock")
            # institute_locations_list.append("Complete Challenges: Shield Unlock")
            institute_locations_list.append("Complete 10 Challenges: Cloaking Device Unlock")
            institute_locations_list.append("Complete 15 Challenges: Combat Boost Unlock")
            institute_locations_list.append("Complete 7 Challenges: Hard Bot Difficulty Unlock")
            institute_locations_list.append("Complete 12 Challenges: Perfect Bot Difficulty Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 1B Unlock")
            institute_locations_list.append("Complete 22 Challenges: Dark Bot Difficulty Unlock")
            institute_locations_list.append("Complete 8 Challenges: Slow Motion Unlock")
            institute_locations_list.append("Complete 3 Challenges: One-Hit Kills Unlock")
            # institute_locations_list.append("Complete Challenges: King of the Hill Unlock")
            institute_locations_list.append("Complete 2 Challenges: Hold the Briefcase Unlock")
            institute_locations_list.append("Complete 4 Challenges: Capture the Case Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 22 Unlock")
            institute_locations_list.append("Complete 17 Challenges: Car Park Unlock")
            institute_locations_list.append("Complete 1 Challenge: Complex Unlock")
            institute_locations_list.append("Complete 3 Challenges: Warehouse Unlock")
            institute_locations_list.append("Complete 5 Challenges: Ravine Unlock")
            institute_locations_list.append("Complete 6 Challenges: Temple Unlock")
            institute_locations_list.append("Complete 9 Challenges: G5 Building Unlock")
            institute_locations_list.append("Complete 11 Challenges: Grid Unlock")
            institute_locations_list.append("Complete 12 Challenges: Felicity Unlock")
            institute_locations_list.append("Complete 14 Challenges: Villa Unlock")
            institute_locations_list.append("Complete 16 Challenges: Sewers Unlock")
            institute_locations_list.append("Complete 22 Challenges: Ruins Unlock")
            institute_locations_list.append("Complete 18 Challenges: Base Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 2F Unlock")
            institute_locations_list.append("Complete 20 Challenges: Fortress Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 31 Unlock")
            institute_locations_list.append("Complete 1 Challenge: dataDyne Female Guard Unlock")
            institute_locations_list.append("Complete 2 Challenges: Office Suit and Office Casual Unlock")
            institute_locations_list.append("Complete 4 Challenges: Carrington Villa Outfits Unlock")
            institute_locations_list.append("Complete 5 Challenges: Trent Unlock")
            institute_locations_list.append("Complete 5 Challenges: NSA Lackey Unlock")
            institute_locations_list.append("Complete 6 Challenges: G5 Building Outfits Unlock")
            institute_locations_list.append("Complete 7 Challenges: Mr. Blonde Unlock")
            institute_locations_list.append("Complete 9 Challenges: CIA Agent and FBI Agent Unlock")
            institute_locations_list.append("Complete 10 Challenges: A51 Infiltration Outfits Unlock")
            institute_locations_list.append("Complete 11 Challenges: Lab Technician Outfits Unlock")
            institute_locations_list.append("Complete 12 Challenges: Biotechnician Unlock")
            institute_locations_list.append("Complete 14 Challenges: Elvis and Maian Soldier Unlock")
            institute_locations_list.append("Complete 17 Challenges: Alaskan Guard Unlock")
            institute_locations_list.append("Complete 16 Challenges: Air Force One Outfits Unlock")
            institute_locations_list.append("Complete 7 Challenges: 8 Bots and Dinner Jacket Outfits Unlock")
            institute_locations_list.append("Complete 18 Challenges: Formal Outfits and President Unlock")
            institute_locations_list.append("Complete 19 Challenges: President's Clone Unlock")
            institute_locations_list.append("Complete 18 Challenges: Presidential Security Unlock")
            institute_locations_list.append("Complete 19 Challenges: NSA Bodyguard Unlock")
            institute_locations_list.append("Complete 24 Challenges: Pelagic II Outfits Unlock")
            institute_locations_list.append("Complete 8 Challenges: Joanna Trench Unlock")
            # institute_locations_list.append("Complete Challenges: Unused Jo Snow Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 48 Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 49 Unlock")
            institute_locations_list.append("Complete 17 Challenges: Joanna Arctic Unlock")
            # institute_locations_list.append("Complete Challenges: Unused 4B Unlock")
            # institute_locations_list.append("Complete Challenges: Jonathan Unlock")
            institute_locations_list.append("Complete 12 Challenges: Pop a Cap Unlock")
            institute_locations_list.append("Complete 6 Challenges: Hacker Central Unlock")
            # institute_locations_list.append("Complete Challenges: Laser Unlock")


    if world.options.weapon_training:
        institute_locations_list.append("Firing Range: Falcon 2 - Bronze")
        institute_locations_list.append("Firing Range: Falcon 2 - Silver")
        institute_locations_list.append("Firing Range: Falcon 2 - Gold")
        institute_locations_list.append("Firing Range: Falcon 2 (Silencer) - Bronze")
        institute_locations_list.append("Firing Range: Falcon 2 (Silencer) - Silver")
        institute_locations_list.append("Firing Range: Falcon 2 (Silencer) - Gold")
        institute_locations_list.append("Firing Range: Falcon 2 (Scope) - Bronze")
        institute_locations_list.append("Firing Range: Falcon 2 (Scope) - Silver")
        institute_locations_list.append("Firing Range: Falcon 2 (Scope) - Gold")
        institute_locations_list.append("Firing Range: MagSec 4 - Bronze")
        institute_locations_list.append("Firing Range: MagSec 4 - Silver")
        institute_locations_list.append("Firing Range: MagSec 4 - Gold")
        institute_locations_list.append("Firing Range: Mauler - Bronze")
        institute_locations_list.append("Firing Range: Mauler - Silver")
        institute_locations_list.append("Firing Range: Mauler - Gold")
        institute_locations_list.append("Firing Range: Phoenix - Bronze")
        institute_locations_list.append("Firing Range: Phoenix - Silver")
        institute_locations_list.append("Firing Range: Phoenix - Gold")
        institute_locations_list.append("Firing Range: DY357 Magnum - Bronze")
        institute_locations_list.append("Firing Range: DY357 Magnum - Silver")
        institute_locations_list.append("Firing Range: DY357 Magnum - Gold")
        institute_locations_list.append("Firing Range: DY357-LX - Bronze")
        institute_locations_list.append("Firing Range: DY357-LX - Silver")
        institute_locations_list.append("Firing Range: DY357-LX - Gold")
        institute_locations_list.append("Firing Range: CMP150 - Bronze")
        institute_locations_list.append("Firing Range: CMP150 - Silver")
        institute_locations_list.append("Firing Range: CMP150 - Gold")
        institute_locations_list.append("Firing Range: Cyclone - Bronze")
        institute_locations_list.append("Firing Range: Cyclone - Silver")
        institute_locations_list.append("Firing Range: Cyclone - Gold")
        institute_locations_list.append("Firing Range: Callisto NTG - Bronze")
        institute_locations_list.append("Firing Range: Callisto NTG - Silver")
        institute_locations_list.append("Firing Range: Callisto NTG - Gold")
        institute_locations_list.append("Firing Range: RC-P120 - Bronze")
        institute_locations_list.append("Firing Range: RC-P120 - Silver")
        institute_locations_list.append("Firing Range: RC-P120 - Gold")
        institute_locations_list.append("Firing Range: Laptop Gun - Bronze")
        institute_locations_list.append("Firing Range: Laptop Gun - Silver")
        institute_locations_list.append("Firing Range: Laptop Gun - Gold")
        institute_locations_list.append("Firing Range: Dragon - Bronze")
        institute_locations_list.append("Firing Range: Dragon - Silver")
        institute_locations_list.append("Firing Range: Dragon - Gold")
        institute_locations_list.append("Firing Range: K7 Avenger - Bronze")
        institute_locations_list.append("Firing Range: K7 Avenger - Silver")
        institute_locations_list.append("Firing Range: K7 Avenger - Gold")
        institute_locations_list.append("Firing Range: AR34 - Bronze")
        institute_locations_list.append("Firing Range: AR34 - Silver")
        institute_locations_list.append("Firing Range: AR34 - Gold")
        institute_locations_list.append("Firing Range: SuperDragon - Bronze")
        institute_locations_list.append("Firing Range: SuperDragon - Silver")
        institute_locations_list.append("Firing Range: SuperDragon - Gold")
        institute_locations_list.append("Firing Range: Shotgun - Bronze")
        institute_locations_list.append("Firing Range: Shotgun - Silver")
        institute_locations_list.append("Firing Range: Shotgun - Gold")
        institute_locations_list.append("Firing Range: Reaper - Bronze")
        institute_locations_list.append("Firing Range: Reaper - Silver")
        institute_locations_list.append("Firing Range: Reaper - Gold")
        institute_locations_list.append("Firing Range: Sniper Rifle - Bronze")
        institute_locations_list.append("Firing Range: Sniper Rifle - Silver")
        institute_locations_list.append("Firing Range: Sniper Rifle - Gold")
        institute_locations_list.append("Firing Range: FarSight XR-20 - Bronze")
        institute_locations_list.append("Firing Range: FarSight XR-20 - Silver")
        institute_locations_list.append("Firing Range: FarSight XR-20 - Gold")
        institute_locations_list.append("Firing Range: Devastator - Bronze")
        institute_locations_list.append("Firing Range: Devastator - Silver")
        institute_locations_list.append("Firing Range: Devastator - Gold")
        institute_locations_list.append("Firing Range: Rocket Launcher - Bronze")
        institute_locations_list.append("Firing Range: Rocket Launcher - Silver")
        institute_locations_list.append("Firing Range: Rocket Launcher - Gold")
        institute_locations_list.append("Firing Range: Slayer - Bronze")
        institute_locations_list.append("Firing Range: Slayer - Silver")
        institute_locations_list.append("Firing Range: Slayer - Gold")
        institute_locations_list.append("Firing Range: Combat Knife - Bronze")
        institute_locations_list.append("Firing Range: Combat Knife - Silver")
        institute_locations_list.append("Firing Range: Combat Knife - Gold")
        institute_locations_list.append("Firing Range: Crossbow - Bronze")
        institute_locations_list.append("Firing Range: Crossbow - Silver")
        institute_locations_list.append("Firing Range: Crossbow - Gold")
        institute_locations_list.append("Firing Range: Tranquilizer - Bronze")
        institute_locations_list.append("Firing Range: Tranquilizer - Silver")
        institute_locations_list.append("Firing Range: Tranquilizer - Gold")
        institute_locations_list.append("Firing Range: Laser - Bronze")
        institute_locations_list.append("Firing Range: Laser - Silver")
        institute_locations_list.append("Firing Range: Laser - Gold")
        institute_locations_list.append("Firing Range: Grenade - Bronze")
        institute_locations_list.append("Firing Range: Grenade - Silver")
        institute_locations_list.append("Firing Range: Grenade - Gold")
        institute_locations_list.append("Firing Range: Timed Mine - Bronze")
        institute_locations_list.append("Firing Range: Timed Mine - Silver")
        institute_locations_list.append("Firing Range: Timed Mine - Gold")
        institute_locations_list.append("Firing Range: Proximity Mine - Bronze")
        institute_locations_list.append("Firing Range: Proximity Mine - Silver")
        institute_locations_list.append("Firing Range: Proximity Mine - Gold")
        institute_locations_list.append("Firing Range: Remote Mine - Bronze")
        institute_locations_list.append("Firing Range: Remote Mine - Silver")
        institute_locations_list.append("Firing Range: Remote Mine - Gold")


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
        defection_locations_list.append("Cheat Unlock: Complete dD Defection")
        investigation_locations_list.append("Cheat Unlock: Complete dD Investigation")
        extraction_locations_list.append("Cheat Unlock: Complete dD Extraction")
        villa_locations_list.append("Cheat Unlock: Complete Carrington Villa")
        chicago_locations_list.append("Cheat Unlock: Complete Chicago")
        g5_locations_list.append("Cheat Unlock: Complete G5 Building")
        infiltration_locations_list.append("Cheat Unlock: Complete A51 Infiltration")
        rescue_locations_list.append("Cheat Unlock: Complete A51 Rescue")
        escape_locations_list.append("Cheat Unlock: Complete A51 Escape")
        airbase_locations_list.append("Cheat Unlock: Complete Air Base")
        afo_locations_list.append("Cheat Unlock: Complete Air Force One")
        crashsite_locations_list.append("Cheat Unlock: Complete Crash Site")
        pelagic_locations_list.append("Cheat Unlock: Complete Pelagic II")
        deepsea_locations_list.append("Cheat Unlock: Complete Deep Sea")
        defense_locations_list.append("Cheat Unlock: Complete CI Defense")
        attackship_locations_list.append("Cheat Unlock: Complete Attack Ship")
        skedarruins_locations_list.append("Cheat Unlock: Complete Skedar Ruins")


    if world.options.timed_cheats:
        if world.options.agent:
            extraction_locations_list.append("Cheat Unlock: Complete dD Extraction (Agent) in under 2:03")
            g5_locations_list.append("Cheat Unlock: Complete G5 Building (Agent) in under 1:40")
            escape_locations_list.append("Cheat Unlock: Complete A51 Escape (Agent) in under 3:50")
            crashsite_locations_list.append("Cheat Unlock: Complete Crash Site (Agent) in under 2:50")
            defense_locations_list.append("Cheat Unlock: Complete CI Defense (Agent) in under 1:45")

        if world.options.special_agent:
            defection_locations_list.append("Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30")
            villa_locations_list.append("Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30")
            infiltration_locations_list.append("Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00")
            airbase_locations_list.append("Cheat Unlock: Complete Air Base (Special Agent) in under 3:11")
            pelagic_locations_list.append("Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07")
            attackship_locations_list.append("Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17")

        if world.options.perfect_agent:
            investigation_locations_list.append("Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30")
            chicago_locations_list.append("Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00")
            rescue_locations_list.append("Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59")
            afo_locations_list.append("Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55")
            deepsea_locations_list.append("Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27")
            skedarruins_locations_list.append("Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")


    if world.options.weapon_cheats:
        institute_locations_list.append("Cheat Unlock: Get gold on Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)")
        institute_locations_list.append("Cheat Unlock: Get gold on MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX")
        institute_locations_list.append("Cheat Unlock: Get gold on CMP150, Cyclone, Callisto NTG, and RC-P120")
        institute_locations_list.append("Cheat Unlock: Get gold on Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon")
        institute_locations_list.append("Cheat Unlock: Get gold on Shotgun, Sniper Rifle, Rocket Launcher, and Slayer")
        institute_locations_list.append("Cheat Unlock: Get gold on Timed Mine, Proximity Mine, and Remote Mine")
        institute_locations_list.append("Cheat Unlock: Get gold on FarSight XR-20, Crossbow, Combat Knife, and Grenade")
        institute_locations_list.append("Cheat Unlock: Get gold on Tranquilizer, Reaper, and Devastator")


    if world.options.pickupsanity \
            and (world.options.agent or world.options.special_agent or world.options.perfect_agent):
        defection_locations_list.append("dD Defection: 2F double Falcon 2 (silencer)")
        defection_locations_list.append("dD Defection: 3F tiny ammo box (on corner desk)")
        defection_locations_list.append("dD Defection: 3F tiny ammo box (on table near couch)")
        defection_locations_list.append("dD Defection: 2F tiny ammo box (on desk across the stairs)")
        defection_locations_list.append("dD Defection: 2F tiny ammo box (on desk across the elevator)")
        defection_locations_list.append("dD Defection: 2F Falcon 2 (silencer) (on desk)")
        defection_locations_list.append("dD Defection: 2F tiny ammo box (under stairs)")
        defection_locations_list.append("dD Defection: 1F CMP150 (on right of front desk)")
        defection_locations_list.append("dD Defection: 1F CMP150 (on left of front desk)")

        investigation_locations_list.append("dD Investigation: ammo box (front of room above the K7 Avenger)")
        investigation_locations_list.append("dD Investigation: ammo box (back of room above the K7 Avenger)")
        investigation_locations_list.append("dD Investigation: ammo box (front of Night Vision room)")
        investigation_locations_list.append("dD Investigation: ammo box (back of Night Vision room)")
        investigation_locations_list.append("dD Investigation: CMP150 (on front of table)")
        investigation_locations_list.append("dD Investigation: CMP150 (on back of table)")
        investigation_locations_list.append("dD Investigation: CMP150 (left of secret weapons compartment)")
        investigation_locations_list.append("dD Investigation: CMP150 (right of secret weapons compartment)")
        investigation_locations_list.append("dD Investigation: Proximity Mine (in radioactive room)")

        extraction_locations_list.append("dD Extraction: 1F DY357 Magnum (from fifth guard)")
        extraction_locations_list.append("dD Extraction: 4F Rocket Launcher")
        extraction_locations_list.append("dD Extraction: 4F Grenade (on Cassandra's desk)")
        extraction_locations_list.append("dD Extraction: 4F Dragon (in hidden room in Cassandra's office)")

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

        chicago_locations_list.append("Chicago: BombSpy (in the dumpster)")
        chicago_locations_list.append("Chicago: double Falcon 2 (scope) (in the Pond Punk)")

        g5_locations_list.append("G5 Building: Crossbow (after knocking out first two guards)")
        g5_locations_list.append("G5 Building: N-Bomb (near the upper exit)")

        infiltration_locations_list.append("A51 Infiltration: Rocket Launcher (in mine field)")

        rescue_locations_list.append("A51 Rescue: Phoenix (past locked hangar door)")
        rescue_locations_list.append("A51 Rescue: double Falcon 2 (silencer) (hidden in barrel)")

        escape_locations_list.append("A51 Escape: double Falcon 2 (scope) (behind you at the start)")
        escape_locations_list.append("A51 Escape: Remote Mine (in first room with guards)")

        airbase_locations_list.append("Air Base: double DY357 Magnum (after knocking out all NSA Lackeys)")
        airbase_locations_list.append("Air Base: Proximity Mine (past the cave)")

        afo_locations_list.append("Air Force One: Cyclone (in room right of stairs)")
        afo_locations_list.append("Air Force One: Cyclone (in room left of stairs)")

        crashsite_locations_list.append("Crash Site: DY357-LX (from disarming Trent)")
        crashsite_locations_list.append("Crash Site: Proximity Mine (from Elvis before doing any objective)")

        pelagic_locations_list.append("Pelagic II: double Falcon 2 (silencer) (from guard and no alarm)")

        deepsea_locations_list.append("Deep Sea: Proximity Mine (from guard in 2nd room with cloaked guards)")
        # deepsea_locations_list.append("Deep Sea: Shotgun (near Shield on the left path)")

        defense_locations_list.append("CI Defense: Devastator (dropped after saving most of the hostages)")

        attackship_locations_list.append("Attack Ship: double Mauler (dropped from Skedar in final room)")
        attackship_locations_list.append("Attack Ship: Slayer (in the room past green chambers)")

        skedarruins_locations_list.append("Skedar Ruins: double Phoenix (near the gap)")

        mbr_locations_list.append("Mr. Blonde's Revenge: 1F double CMP150 (from guard near bottom elevator)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 3F tiny ammo box (on corner desk)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 3F tiny ammo box (on table near couch)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the stairs)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 2F tiny ammo box (on desk across the elevator)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 2F Falcon 2 (on desk)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 2F tiny ammo box (under stairs)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 1F CMP150 (on right of front desk)")
        mbr_locations_list.append("Mr. Blonde's Revenge: 1F CMP150 (on left of front desk)")

        maiansos_locations_list.append("Maian SOS: double DY357-LX (from dual-wielding guard)")
        maiansos_locations_list.append("Maian SOS: Psychosis Gun (on desk near the start)")

        if world.options.agent:
            defection_locations_list.append("dD Defection: 1F Shield - (Agent)")

            investigation_locations_list.append("dD Investigation: Shield (on crate) - (Agent)")

            extraction_locations_list.append("dD Extraction: 2F Shield - (Agent)")
            extraction_locations_list.append("dD Extraction: Roof ammo box (on left) - (Agent)")
            extraction_locations_list.append("dD Extraction: Roof ammo box (on right) - (Agent)")

            villa_locations_list.append("Carrington Villa: Shield (on helipad crate) - (Agent)")
            villa_locations_list.append("Carrington Villa: Shield (in the bathroom) - (Agent)")

            chicago_locations_list.append("Chicago: Shield (near the taxi) - (Agent)")

            g5_locations_list.append("G5 Building: Shield (in room before the laser grids) - (Agent)")

            infiltration_locations_list.append("A51 Infiltration: Shield (near hoverbike) - (Agent)")

            rescue_locations_list.append("A51 Rescue: Shield (guard past first elevator) - (Agent)")

            escape_locations_list.append("A51 Escape: Shield (dropped by biotechnician) - (Agent)")

            airbase_locations_list.append("Air Base: Shield (dropped by NSA Lackey) - (Agent)")

            afo_locations_list.append("Air Force One: Shield (in small kitchen) - (Agent)")

            crashsite_locations_list.append("Crash Site: Shield (near the crashed UFO) - (Agent)")

            pelagic_locations_list.append("Pelagic II: Shield (on the helipad) - (Agent)")

            # deepsea_locations_list.append("Deep Sea (Agent): Pick up Shield dropped from Sniper guard")

            defense_locations_list.append("CI Defense: 2F Shield - (Agent)")

            skedarruins_locations_list.append("Skedar Ruins: Shield (behind the fallen pillar) - (Agent)")

            mbr_locations_list.append("Mr. Blonde's Revenge: 1F Shield - (Agent)")


        if world.options.agent or world.options.special_agent:
            defection_locations_list.append("dD Defection: 3F Shield - (Agent/Special)")

            investigation_locations_list.append("dD Investigation: Shield (behind the glass) - (Agent/Special)")

            chicago_locations_list.append("Chicago: Shield (under stairs near Pond Punk) - (Agent/Special)")

            g5_locations_list.append("G5 Building: Shield (on stairs to the upper exit) - (Agent/Special)")

            infiltration_locations_list.append("A51 Infiltration: Shield (in the crawl space) - (Agent/Special)")

            rescue_locations_list.append("A51 Rescue: Shield (on desk near computer) - (Agent/Special)")

            escape_locations_list.append("A51 Escape: Shield (behind locked medical containment doors) - (Agent/Special)")

            airbase_locations_list.append("Air Base: Shield (in the safe) - (Agent/Special)")

            afo_locations_list.append("Air Force One: Shield (in piano room) - (Agent/Special)")

            crashsite_locations_list.append("Crash Site: Shield (behind President's clone) - (Agent/Special)")

            pelagic_locations_list.append("Pelagic II: Shield (on the sub hangar crate) - (Agent/Special)")

            deepsea_locations_list.append("Deep Sea: Shield (on the left path) - (Agent/Special)")

            defense_locations_list.append("CI Defense: Basement Shield - (Agent/Special)")

            attackship_locations_list.append("Attack Ship: Shield (on table) - (Agent/Special)")

            skedarruins_locations_list.append("Skedar Ruins: Shield (area past the gap to the right) - (Agent/Special)")

            mbr_locations_list.append("Mr. Blonde's Revenge: 3F Shield - (Agent/Special)")


        if world.options.special_agent or world.options.perfect_agent:
            investigation_locations_list.append("dD Investigation: ammo box (front of room with one scientist)")
            investigation_locations_list.append("dD Investigation: ammo box (back of room with one scientist)")
            investigation_locations_list.append("dD Investigation: ammo box (front of room near two scientists)")
            investigation_locations_list.append("dD Investigation: ammo box (back of room near two scientists)")

            infiltration_locations_list.append("A51 Infiltration: double MagSec 4 (after placing comms rider)")


        if world.options.perfect_agent:
            villa_locations_list.append("Carrington Villa: Sniper Rifle (in the bathroom) - (Perfect Agent)")

            attackship_locations_list.append("Attack Ship: De Vries' necklace - (Perfect Agent)")


        if world.options.mission_logic.value == MissionLogic.option_perfect:
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F Laptop Gun")
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F Falcon 2 (right side)")
            mbr_locations_list.append("Mr. Blonde's Revenge: 2F Falcon 2 (left side)")


        if world.options.perfect_agent \
                or world.options.mission_logic.value == MissionLogic.option_perfect:
            defection_locations_list.append("dD Defection: 2F Laptop Gun")
            defection_locations_list.append("dD Defection: 2F Falcon 2 (silencer) (right side)")
            defection_locations_list.append("dD Defection: 2F Falcon 2 (silencer) (left side)")


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
