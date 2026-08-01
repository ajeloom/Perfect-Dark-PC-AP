from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, LocationProgressType

from . import items

if TYPE_CHECKING:
    from .world import PerfectDarkWorld

from .options import Goal, SkedarRuinsRequirements
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
    "Cheat Unlock: Get gold medals for Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)": 490,
    "Cheat Unlock: Get gold medals for MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX": 491,
    "Cheat Unlock: Get gold medals for CMP150, Cyclone, Callisto NTG, and RC-P120": 492,
    "Cheat Unlock: Get gold medals for Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon": 493,
    "Cheat Unlock: Get gold medals for Shotgun, Sniper Rifle, Rocket Launcher, and Slayer": 494,
    "Cheat Unlock: Get gold medals for Timed Mine, Proximity Mine, and Remote Mine": 495,
    "Cheat Unlock: Get gold medals for FarSight XR-20, Crossbow, Combat Knife, and Grenade": 496,
    "Cheat Unlock: Get gold medals for Tranquilizer, Reaper, and Devastator": 497,
    "Collect All Stars": 498,
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

    if world.options.agent:
        defection_locations = get_location_names_with_ids(
            [
                "dD Defection - Agent Objective 1",
                "Complete: dD Defection - Agent"
            ]
        )
        defection.add_locations(defection_locations, PerfectDarkLocation)

        investigation_locations = get_location_names_with_ids(
            [
                "dD Investigation - Agent Objective 1",
                "dD Investigation - Agent Objective 2",
                "Complete: dD Investigation - Agent"
            ]
        )
        investigation.add_locations(investigation_locations, PerfectDarkLocation)

        extraction_locations = get_location_names_with_ids(
            [
                "dD Extraction - Agent Objective 1",
                "dD Extraction - Agent Objective 2",
                "dD Extraction - Agent Objective 3",
                "Complete: dD Extraction - Agent"
            ]
        )
        extraction.add_locations(extraction_locations, PerfectDarkLocation)

        villa_locations = get_location_names_with_ids(
            [
                "Carrington Villa - Agent Objective 1",
                "Carrington Villa - Agent Objective 2",
                "Carrington Villa - Agent Objective 3",
                "Complete: Carrington Villa - Agent"
            ]
        )
        villa.add_locations(villa_locations, PerfectDarkLocation)

        chicago_locations = get_location_names_with_ids(
            [
                "Chicago - Agent Objective 1",
                "Chicago - Agent Objective 2",
                "Chicago - Agent Objective 3",
                "Complete: Chicago - Agent"
            ]
        )
        chicago.add_locations(chicago_locations, PerfectDarkLocation)

        g5_building_locations = get_location_names_with_ids(
            [
                "G5 Building - Agent Objective 1",
                "G5 Building - Agent Objective 2",
                "G5 Building - Agent Objective 3",
                "Complete: G5 Building - Agent"
            ]
        )
        g5_building.add_locations(g5_building_locations, PerfectDarkLocation)

        infiltration_locations = get_location_names_with_ids(
            [
                "A51 Infiltration - Agent Objective 1",
                "A51 Infiltration - Agent Objective 2",
                "A51 Infiltration - Agent Objective 3",
                "Complete: A51 Infiltration - Agent"
            ]
        )
        infiltration.add_locations(infiltration_locations, PerfectDarkLocation)

        rescue_locations = get_location_names_with_ids(
            [
                "A51 Rescue - Agent Objective 1",
                "A51 Rescue - Agent Objective 2",
                "A51 Rescue - Agent Objective 3",
                "Complete: A51 Rescue - Agent"
            ]
        )
        rescue.add_locations(rescue_locations, PerfectDarkLocation)

        escape_locations = get_location_names_with_ids(
            [
                "A51 Escape - Agent Objective 1",
                "A51 Escape - Agent Objective 2",
                "A51 Escape - Agent Objective 3",
                "Complete: A51 Escape - Agent"
            ]
        )
        escape.add_locations(escape_locations, PerfectDarkLocation)

        air_base_locations = get_location_names_with_ids(
            [
                "Air Base - Agent Objective 1",
                "Air Base - Agent Objective 2",
                "Air Base - Agent Objective 3",
                "Complete: Air Base - Agent"
            ]
        )
        air_base.add_locations(air_base_locations, PerfectDarkLocation)

        air_force_one_locations = get_location_names_with_ids(
            [
                "Air Force One - Agent Objective 1",
                "Air Force One - Agent Objective 2",
                "Air Force One - Agent Objective 3",
                "Complete: Air Force One - Agent"
            ]
        )
        air_force_one.add_locations(air_force_one_locations, PerfectDarkLocation)

        crash_site_locations = get_location_names_with_ids(
            [
                "Crash Site - Agent Objective 1",
                "Crash Site - Agent Objective 2",
                "Crash Site - Agent Objective 3",
                "Complete: Crash Site - Agent"
            ]
        )
        crash_site.add_locations(crash_site_locations, PerfectDarkLocation)

        pelagic_locations = get_location_names_with_ids(
            [
                "Pelagic II - Agent Objective 1",
                "Pelagic II - Agent Objective 2",
                "Pelagic II - Agent Objective 3",
                "Complete: Pelagic II - Agent"
            ]
        )
        pelagic.add_locations(pelagic_locations, PerfectDarkLocation)

        deep_sea_locations = get_location_names_with_ids(
            [
                "Deep Sea - Agent Objective 1",
                "Deep Sea - Agent Objective 2",
                "Deep Sea - Agent Objective 3",
                "Complete: Deep Sea - Agent"
            ]
        )
        deep_sea.add_locations(deep_sea_locations, PerfectDarkLocation)

        institute_defense_locations = get_location_names_with_ids(
            [
                "CI Defense - Agent Objective 1",
                "CI Defense - Agent Objective 2",
                "CI Defense - Agent Objective 3",
                "Complete: CI Defense - Agent"
            ]
        )
        institute_defense.add_locations(institute_defense_locations, PerfectDarkLocation)

        attack_ship_locations = get_location_names_with_ids(
            [
                "Attack Ship - Agent Objective 1",
                "Attack Ship - Agent Objective 2",
                "Attack Ship - Agent Objective 3",
                "Complete: Attack Ship - Agent"
            ]
        )
        attack_ship.add_locations(attack_ship_locations, PerfectDarkLocation)

        skedar_ruins_locations = get_location_names_with_ids(
            [
                "Skedar Ruins - Agent Objective 1",
                "Skedar Ruins - Agent Objective 2",
                "Skedar Ruins - Agent Objective 3",
                "Complete: Skedar Ruins - Agent"
            ]
        )
        skedar_ruins.add_locations(skedar_ruins_locations, PerfectDarkLocation)

        mbr_locations = get_location_names_with_ids(
            [
                "Mr. Blonde's Revenge - Agent Objective 1",
                "Complete: Mr. Blonde's Revenge - Agent"
            ]
        )
        mbr.add_locations(mbr_locations, PerfectDarkLocation)

        maian_sos_locations = get_location_names_with_ids(
            [
                "Maian SOS - Agent Objective 1",
                "Complete: Maian SOS - Agent"
            ]
        )
        maian_sos.add_locations(maian_sos_locations, PerfectDarkLocation)

        war_locations = get_location_names_with_ids(
            [
                "WAR! - Agent Objective 1",
                "Complete: WAR! - Agent"
            ]
        )
        war.add_locations(war_locations, PerfectDarkLocation)

        duel_locations = get_location_names_with_ids(
            [
                "The Duel - Agent Objective 1",
                "Complete: The Duel - Agent"
            ]
        )
        duel.add_locations(duel_locations, PerfectDarkLocation)

    if world.options.special_agent:
        defection_locations = get_location_names_with_ids(
            [
                "dD Defection - Special Agent Objective 1",
                "dD Defection - Special Agent Objective 2",
                "dD Defection - Special Agent Objective 3",
                "dD Defection - Special Agent Objective 4",
                "Complete: dD Defection - Special Agent"
            ]
        )
        defection.add_locations(defection_locations, PerfectDarkLocation)

        investigation_locations = get_location_names_with_ids(
            [
                "dD Investigation - Special Agent Objective 1",
                "dD Investigation - Special Agent Objective 2",
                "dD Investigation - Special Agent Objective 3",
                "dD Investigation - Special Agent Objective 4",
                "Complete: dD Investigation - Special Agent"
            ]
        )
        investigation.add_locations(investigation_locations, PerfectDarkLocation)

        extraction_locations = get_location_names_with_ids(
            [
                "dD Extraction - Special Agent Objective 1",
                "dD Extraction - Special Agent Objective 2",
                "dD Extraction - Special Agent Objective 3",
                "dD Extraction - Special Agent Objective 4",
                "Complete: dD Extraction - Special Agent"
            ]
        )
        extraction.add_locations(extraction_locations, PerfectDarkLocation)

        villa_locations = get_location_names_with_ids(
            [
                "Carrington Villa - Special Agent Objective 1",
                "Carrington Villa - Special Agent Objective 2",
                "Carrington Villa - Special Agent Objective 3",
                "Carrington Villa - Special Agent Objective 4",
                "Complete: Carrington Villa - Special Agent"
            ]
        )
        villa.add_locations(villa_locations, PerfectDarkLocation)

        chicago_locations = get_location_names_with_ids(
            [
                "Chicago - Special Agent Objective 1",
                "Chicago - Special Agent Objective 2",
                "Chicago - Special Agent Objective 3",
                "Chicago - Special Agent Objective 4",
                "Complete: Chicago - Special Agent"
            ]
        )
        chicago.add_locations(chicago_locations, PerfectDarkLocation)

        g5_building_locations = get_location_names_with_ids(
            [
                "G5 Building - Special Agent Objective 1",
                "G5 Building - Special Agent Objective 2",
                "G5 Building - Special Agent Objective 3",
                "G5 Building - Special Agent Objective 4",
                "Complete: G5 Building - Special Agent"
            ]
        )
        g5_building.add_locations(g5_building_locations, PerfectDarkLocation)

        infiltration_locations = get_location_names_with_ids(
            [
                "A51 Infiltration - Special Agent Objective 1",
                "A51 Infiltration - Special Agent Objective 2",
                "A51 Infiltration - Special Agent Objective 3",
                "A51 Infiltration - Special Agent Objective 4",
                "Complete: A51 Infiltration - Special Agent"
            ]
        )
        infiltration.add_locations(infiltration_locations, PerfectDarkLocation)

        rescue_locations = get_location_names_with_ids(
            [
                "A51 Rescue - Special Agent Objective 1",
                "A51 Rescue - Special Agent Objective 2",
                "A51 Rescue - Special Agent Objective 3",
                "A51 Rescue - Special Agent Objective 4",
                "Complete: A51 Rescue - Special Agent"
            ]
        )
        rescue.add_locations(rescue_locations, PerfectDarkLocation)

        escape_locations = get_location_names_with_ids(
            [
                "A51 Escape - Special Agent Objective 1",
                "A51 Escape - Special Agent Objective 2",
                "A51 Escape - Special Agent Objective 3",
                "A51 Escape - Special Agent Objective 4",
                "Complete: A51 Escape - Special Agent"
            ]
        )
        escape.add_locations(escape_locations, PerfectDarkLocation)

        air_base_locations = get_location_names_with_ids(
            [
                "Air Base - Special Agent Objective 1",
                "Air Base - Special Agent Objective 2",
                "Air Base - Special Agent Objective 3",
                "Air Base - Special Agent Objective 4",
                "Complete: Air Base - Special Agent"
            ]
        )
        air_base.add_locations(air_base_locations, PerfectDarkLocation)

        air_force_one_locations = get_location_names_with_ids(
            [
                "Air Force One - Special Agent Objective 1",
                "Air Force One - Special Agent Objective 2",
                "Air Force One - Special Agent Objective 3",
                "Air Force One - Special Agent Objective 4",
                "Complete: Air Force One - Special Agent"
            ]
        )
        air_force_one.add_locations(air_force_one_locations, PerfectDarkLocation)

        crash_site_locations = get_location_names_with_ids(
            [
                "Crash Site - Special Agent Objective 1",
                "Crash Site - Special Agent Objective 2",
                "Crash Site - Special Agent Objective 3",
                "Crash Site - Special Agent Objective 4",
                "Complete: Crash Site - Special Agent"
            ]
        )
        crash_site.add_locations(crash_site_locations, PerfectDarkLocation)

        pelagic_locations = get_location_names_with_ids(
            [
                "Pelagic II - Special Agent Objective 1",
                "Pelagic II - Special Agent Objective 2",
                "Pelagic II - Special Agent Objective 3",
                "Pelagic II - Special Agent Objective 4",
                "Complete: Pelagic II - Special Agent"
            ]
        )
        pelagic.add_locations(pelagic_locations, PerfectDarkLocation)

        deep_sea_locations = get_location_names_with_ids(
            [
                "Deep Sea - Special Agent Objective 1",
                "Deep Sea - Special Agent Objective 2",
                "Deep Sea - Special Agent Objective 3",
                "Deep Sea - Special Agent Objective 4",
                "Complete: Deep Sea - Special Agent"
            ]
        )
        deep_sea.add_locations(deep_sea_locations, PerfectDarkLocation)

        institute_defense_locations = get_location_names_with_ids(
            [
                "CI Defense - Special Agent Objective 1",
                "CI Defense - Special Agent Objective 2",
                "CI Defense - Special Agent Objective 3",
                "CI Defense - Special Agent Objective 4",
                "Complete: CI Defense - Special Agent"
            ]
        )
        institute_defense.add_locations(institute_defense_locations, PerfectDarkLocation)

        attack_ship_locations = get_location_names_with_ids(
            [
                "Attack Ship - Special Agent Objective 1",
                "Attack Ship - Special Agent Objective 2",
                "Attack Ship - Special Agent Objective 3",
                "Attack Ship - Special Agent Objective 4",
                "Complete: Attack Ship - Special Agent"
            ]
        )
        attack_ship.add_locations(attack_ship_locations, PerfectDarkLocation)

        skedar_ruins_locations = get_location_names_with_ids(
            [
                "Skedar Ruins - Special Agent Objective 1",
                "Skedar Ruins - Special Agent Objective 2",
                "Skedar Ruins - Special Agent Objective 3",
                "Skedar Ruins - Special Agent Objective 4",
                "Complete: Skedar Ruins - Special Agent"
            ]
        )
        skedar_ruins.add_locations(skedar_ruins_locations, PerfectDarkLocation)

        mbr_locations = get_location_names_with_ids(
            [
                "Mr. Blonde's Revenge - Special Agent Objective 1",
                "Mr. Blonde's Revenge - Special Agent Objective 2",
                "Complete: Mr. Blonde's Revenge - Special Agent"
            ]
        )
        mbr.add_locations(mbr_locations, PerfectDarkLocation)

        maian_sos_locations = get_location_names_with_ids(
            [
                "Maian SOS - Special Agent Objective 1",
                "Maian SOS - Special Agent Objective 2",
                "Complete: Maian SOS - Special Agent"
            ]
        )
        maian_sos.add_locations(maian_sos_locations, PerfectDarkLocation)

        war_locations = get_location_names_with_ids(
            [
                "WAR! - Special Agent Objective 1",
                "WAR! - Special Agent Objective 2",
                "Complete: WAR! - Special Agent"
            ]
        )
        war.add_locations(war_locations, PerfectDarkLocation)

        duel_locations = get_location_names_with_ids(
            [
                "The Duel - Special Agent Objective 1",
                "The Duel - Special Agent Objective 2",
                "Complete: The Duel - Special Agent"
            ]
        )
        duel.add_locations(duel_locations, PerfectDarkLocation)


    if world.options.perfect_agent:
        defection_locations = get_location_names_with_ids(
            [
                "dD Defection - Perfect Agent Objective 1",
                "dD Defection - Perfect Agent Objective 2",
                "dD Defection - Perfect Agent Objective 3",
                "dD Defection - Perfect Agent Objective 4",
                "dD Defection - Perfect Agent Objective 5",
                "Complete: dD Defection - Perfect Agent"
            ]
        )
        defection.add_locations(defection_locations, PerfectDarkLocation)

        investigation_locations = get_location_names_with_ids(
            [
                "dD Investigation - Perfect Agent Objective 1",
                "dD Investigation - Perfect Agent Objective 2",
                "dD Investigation - Perfect Agent Objective 3",
                "dD Investigation - Perfect Agent Objective 4",
                "dD Investigation - Perfect Agent Objective 5",
                "Complete: dD Investigation - Perfect Agent"
            ]
        )
        investigation.add_locations(investigation_locations, PerfectDarkLocation)

        extraction_locations = get_location_names_with_ids(
            [
                "dD Extraction - Perfect Agent Objective 1",
                "dD Extraction - Perfect Agent Objective 2",
                "dD Extraction - Perfect Agent Objective 3",
                "dD Extraction - Perfect Agent Objective 4",
                "dD Extraction - Perfect Agent Objective 5",
                "Complete: dD Extraction - Perfect Agent"
            ]
        )
        extraction.add_locations(extraction_locations, PerfectDarkLocation)

        villa_locations = get_location_names_with_ids(
            [
                "Carrington Villa - Perfect Agent Objective 1",
                "Carrington Villa - Perfect Agent Objective 2",
                "Carrington Villa - Perfect Agent Objective 3",
                "Carrington Villa - Perfect Agent Objective 4",
                "Carrington Villa - Perfect Agent Objective 5",
                "Complete: Carrington Villa - Perfect Agent"
            ]
        )
        villa.add_locations(villa_locations, PerfectDarkLocation)

        chicago_locations = get_location_names_with_ids(
            [
                "Chicago - Perfect Agent Objective 1",
                "Chicago - Perfect Agent Objective 2",
                "Chicago - Perfect Agent Objective 3",
                "Chicago - Perfect Agent Objective 4",
                "Chicago - Perfect Agent Objective 5",
                "Complete: Chicago - Perfect Agent"
            ]
        )
        chicago.add_locations(chicago_locations, PerfectDarkLocation)

        g5_building_locations = get_location_names_with_ids(
            [
                "G5 Building - Perfect Agent Objective 1",
                "G5 Building - Perfect Agent Objective 2",
                "G5 Building - Perfect Agent Objective 3",
                "G5 Building - Perfect Agent Objective 4",
                "G5 Building - Perfect Agent Objective 5",
                "Complete: G5 Building - Perfect Agent"
            ]
        )
        g5_building.add_locations(g5_building_locations, PerfectDarkLocation)

        infiltration_locations = get_location_names_with_ids(
            [
                "A51 Infiltration - Perfect Agent Objective 1",
                "A51 Infiltration - Perfect Agent Objective 2",
                "A51 Infiltration - Perfect Agent Objective 3",
                "A51 Infiltration - Perfect Agent Objective 4",
                "A51 Infiltration - Perfect Agent Objective 5",
                "Complete: A51 Infiltration - Perfect Agent"
            ]
        )
        infiltration.add_locations(infiltration_locations, PerfectDarkLocation)

        rescue_locations = get_location_names_with_ids(
            [
                "A51 Rescue - Perfect Agent Objective 1",
                "A51 Rescue - Perfect Agent Objective 2",
                "A51 Rescue - Perfect Agent Objective 3",
                "A51 Rescue - Perfect Agent Objective 4",
                "A51 Rescue - Perfect Agent Objective 5",
                "Complete: A51 Rescue - Perfect Agent"
            ]
        )
        rescue.add_locations(rescue_locations, PerfectDarkLocation)

        escape_locations = get_location_names_with_ids(
            [
                "A51 Escape - Perfect Agent Objective 1",
                "A51 Escape - Perfect Agent Objective 2",
                "A51 Escape - Perfect Agent Objective 3",
                "A51 Escape - Perfect Agent Objective 4",
                "A51 Escape - Perfect Agent Objective 5",
                "Complete: A51 Escape - Perfect Agent"
            ]
        )
        escape.add_locations(escape_locations, PerfectDarkLocation)

        air_base_locations = get_location_names_with_ids(
            [
                "Air Base - Perfect Agent Objective 1",
                "Air Base - Perfect Agent Objective 2",
                "Air Base - Perfect Agent Objective 3",
                "Air Base - Perfect Agent Objective 4",
                "Air Base - Perfect Agent Objective 5",
                "Complete: Air Base - Perfect Agent"
            ]
        )
        air_base.add_locations(air_base_locations, PerfectDarkLocation)

        air_force_one_locations = get_location_names_with_ids(
            [
                "Air Force One - Perfect Agent Objective 1",
                "Air Force One - Perfect Agent Objective 2",
                "Air Force One - Perfect Agent Objective 3",
                "Air Force One - Perfect Agent Objective 4",
                "Air Force One - Perfect Agent Objective 5",
                "Complete: Air Force One - Perfect Agent"
            ]
        )
        air_force_one.add_locations(air_force_one_locations, PerfectDarkLocation)

        crash_site_locations = get_location_names_with_ids(
            [
                "Crash Site - Perfect Agent Objective 1",
                "Crash Site - Perfect Agent Objective 2",
                "Crash Site - Perfect Agent Objective 3",
                "Crash Site - Perfect Agent Objective 4",
                "Crash Site - Perfect Agent Objective 5",
                "Complete: Crash Site - Perfect Agent"
            ]
        )
        crash_site.add_locations(crash_site_locations, PerfectDarkLocation)

        pelagic_locations = get_location_names_with_ids(
            [
                "Pelagic II - Perfect Agent Objective 1",
                "Pelagic II - Perfect Agent Objective 2",
                "Pelagic II - Perfect Agent Objective 3",
                "Pelagic II - Perfect Agent Objective 4",
                "Pelagic II - Perfect Agent Objective 5",
                "Complete: Pelagic II - Perfect Agent"
            ]
        )
        pelagic.add_locations(pelagic_locations, PerfectDarkLocation)

        deep_sea_locations = get_location_names_with_ids(
            [
                "Deep Sea - Perfect Agent Objective 1",
                "Deep Sea - Perfect Agent Objective 2",
                "Deep Sea - Perfect Agent Objective 3",
                "Deep Sea - Perfect Agent Objective 4",
                "Deep Sea - Perfect Agent Objective 5",
                "Complete: Deep Sea - Perfect Agent"
            ]
        )
        deep_sea.add_locations(deep_sea_locations, PerfectDarkLocation)

        institute_defense_locations = get_location_names_with_ids(
            [
                "CI Defense - Perfect Agent Objective 1",
                "CI Defense - Perfect Agent Objective 2",
                "CI Defense - Perfect Agent Objective 3",
                "CI Defense - Perfect Agent Objective 4",
                "CI Defense - Perfect Agent Objective 5",
                "Complete: CI Defense - Perfect Agent"
            ]
        )
        institute_defense.add_locations(institute_defense_locations, PerfectDarkLocation)

        attack_ship_locations = get_location_names_with_ids(
            [
                "Attack Ship - Perfect Agent Objective 1",
                "Attack Ship - Perfect Agent Objective 2",
                "Attack Ship - Perfect Agent Objective 3",
                "Attack Ship - Perfect Agent Objective 4",
                "Attack Ship - Perfect Agent Objective 5",
                "Complete: Attack Ship - Perfect Agent"
            ]
        )
        attack_ship.add_locations(attack_ship_locations, PerfectDarkLocation)

        skedar_ruins_locations = get_location_names_with_ids(
            [
                "Skedar Ruins - Perfect Agent Objective 1",
                "Skedar Ruins - Perfect Agent Objective 2",
                "Skedar Ruins - Perfect Agent Objective 3",
                "Skedar Ruins - Perfect Agent Objective 4",
                "Skedar Ruins - Perfect Agent Objective 5",
                "Complete: Skedar Ruins - Perfect Agent"
            ]
        )
        skedar_ruins.add_locations(skedar_ruins_locations, PerfectDarkLocation)

        mbr_locations = get_location_names_with_ids(
            [
                "Mr. Blonde's Revenge - Perfect Agent Objective 1",
                "Mr. Blonde's Revenge - Perfect Agent Objective 2",
                "Mr. Blonde's Revenge - Perfect Agent Objective 3",
                "Complete: Mr. Blonde's Revenge - Perfect Agent"
            ]
        )
        mbr.add_locations(mbr_locations, PerfectDarkLocation)

        maian_sos_locations = get_location_names_with_ids(
            [
                "Maian SOS - Perfect Agent Objective 1",
                "Maian SOS - Perfect Agent Objective 2",
                "Maian SOS - Perfect Agent Objective 3",
                "Complete: Maian SOS - Perfect Agent"
            ]
        )
        maian_sos.add_locations(maian_sos_locations, PerfectDarkLocation)

        war_locations = get_location_names_with_ids(
            [
                "WAR! - Perfect Agent Objective 1",
                "WAR! - Perfect Agent Objective 2",
                "WAR! - Perfect Agent Objective 3",
                "Complete: WAR! - Perfect Agent"
            ]
        )
        war.add_locations(war_locations, PerfectDarkLocation)

        duel_locations = get_location_names_with_ids(
            [
                "The Duel - Perfect Agent Objective 1",
                "The Duel - Perfect Agent Objective 2",
                "The Duel - Perfect Agent Objective 3",
                "Complete: The Duel - Perfect Agent"
            ]
        )
        duel.add_locations(duel_locations, PerfectDarkLocation)


    if world.options.goal.value == Goal.option_complete_skedar_ruins \
            and not world.options.agent \
            and not world.options.special_agent \
            and not world.options.perfect_agent:
        skedar_ruins_locations = get_location_names_with_ids(
            [
                "Skedar Ruins - Agent Objective 1",
                "Skedar Ruins - Agent Objective 2",
                "Skedar Ruins - Agent Objective 3",
                "Complete: Skedar Ruins - Agent",
                "Skedar Ruins - Special Agent Objective 1",
                "Skedar Ruins - Special Agent Objective 2",
                "Skedar Ruins - Special Agent Objective 3",
                "Skedar Ruins - Special Agent Objective 4",
                "Complete: Skedar Ruins - Special Agent",
                "Skedar Ruins - Perfect Agent Objective 1",
                "Skedar Ruins - Perfect Agent Objective 2",
                "Skedar Ruins - Perfect Agent Objective 3",
                "Skedar Ruins - Perfect Agent Objective 4",
                "Skedar Ruins - Perfect Agent Objective 5",
                "Complete: Skedar Ruins - Perfect Agent"
            ]
        )
        skedar_ruins.add_locations(skedar_ruins_locations, PerfectDarkLocation)

        if world.options.unlock_cheats:
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Skedar Ruins",
                    "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"
                ]
            )
            skedar_ruins.add_locations(cheat_locations, PerfectDarkLocation)

            skedar_cheat = PerfectDarkLocation(world.player, "Cheat Unlock: Complete Skedar Ruins")
            skedar_cheat_timed = PerfectDarkLocation(world.player, "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31")
            skedar_cheat.progress_type = LocationProgressType.EXCLUDED
            skedar_cheat_timed.progress_type = LocationProgressType.EXCLUDED


    if ((world.options.goal.value == Goal.option_complete_skedar_ruins
            and world.options.skedar_ruins_requirements.value >= SkedarRuinsRequirements.option_collect_mission_stars)
            or world.options.goal.value >= Goal.option_complete_missions):
        mission_stars = get_location_names_with_ids(
            [
                "Collect All Stars"
            ]
        )
        carrington_institute.add_locations(mission_stars, PerfectDarkLocation)


    if has_challenges(world):
        challenges = []
        
        for x in range(1, 31):
            challenge_name = f"Challenge {x}"
            if (world.options.excluded_challenges.__contains__(challenge_name) == False):
                challenge_location = f"Complete: Challenge {x}"
                challenges.append(challenge_location)

        challenges_locations = get_location_names_with_ids(challenges)
        carrington_institute.add_locations(challenges_locations, PerfectDarkLocation)


    if world.options.weapon_training:
        training_locations = get_location_names_with_ids(
            [
                "Firing Range: Falcon 2 - Bronze",
                "Firing Range: Falcon 2 - Silver",
                "Firing Range: Falcon 2 - Gold",
                "Firing Range: Falcon 2 (Silencer) - Bronze",
                "Firing Range: Falcon 2 (Silencer) - Silver",
                "Firing Range: Falcon 2 (Silencer) - Gold",
                "Firing Range: Falcon 2 (Scope) - Bronze",
                "Firing Range: Falcon 2 (Scope) - Silver",
                "Firing Range: Falcon 2 (Scope) - Gold",
                "Firing Range: MagSec 4 - Bronze",
                "Firing Range: MagSec 4 - Silver",
                "Firing Range: MagSec 4 - Gold",
                "Firing Range: Mauler - Bronze",
                "Firing Range: Mauler - Silver",
                "Firing Range: Mauler - Gold",
                "Firing Range: Phoenix - Bronze",
                "Firing Range: Phoenix - Silver",
                "Firing Range: Phoenix - Gold",
                "Firing Range: DY357 Magnum - Bronze",
                "Firing Range: DY357 Magnum - Silver",
                "Firing Range: DY357 Magnum - Gold",
                "Firing Range: DY357-LX - Bronze",
                "Firing Range: DY357-LX - Silver",
                "Firing Range: DY357-LX - Gold",
                "Firing Range: CMP150 - Bronze",
                "Firing Range: CMP150 - Silver",
                "Firing Range: CMP150 - Gold",
                "Firing Range: Cyclone - Bronze",
                "Firing Range: Cyclone - Silver",
                "Firing Range: Cyclone - Gold",
                "Firing Range: Callisto NTG - Bronze",
                "Firing Range: Callisto NTG - Silver",
                "Firing Range: Callisto NTG - Gold",
                "Firing Range: RC-P120 - Bronze",
                "Firing Range: RC-P120 - Silver",
                "Firing Range: RC-P120 - Gold",
                "Firing Range: Laptop Gun - Bronze",
                "Firing Range: Laptop Gun - Silver",
                "Firing Range: Laptop Gun - Gold",
                "Firing Range: Dragon - Bronze",
                "Firing Range: Dragon - Silver",
                "Firing Range: Dragon - Gold",
                "Firing Range: K7 Avenger - Bronze",
                "Firing Range: K7 Avenger - Silver",
                "Firing Range: K7 Avenger - Gold",
                "Firing Range: AR34 - Bronze",
                "Firing Range: AR34 - Silver",
                "Firing Range: AR34 - Gold",
                "Firing Range: SuperDragon - Bronze",
                "Firing Range: SuperDragon - Silver",
                "Firing Range: SuperDragon - Gold",
                "Firing Range: Shotgun - Bronze",
                "Firing Range: Shotgun - Silver",
                "Firing Range: Shotgun - Gold",
                "Firing Range: Reaper - Bronze",
                "Firing Range: Reaper - Silver",
                "Firing Range: Reaper - Gold",
                "Firing Range: Sniper Rifle - Bronze",
                "Firing Range: Sniper Rifle - Silver",
                "Firing Range: Sniper Rifle - Gold",
                "Firing Range: FarSight XR-20 - Bronze",
                "Firing Range: FarSight XR-20 - Silver",
                "Firing Range: FarSight XR-20 - Gold",
                "Firing Range: Devastator - Bronze",
                "Firing Range: Devastator - Silver",
                "Firing Range: Devastator - Gold",
                "Firing Range: Rocket Launcher - Bronze",
                "Firing Range: Rocket Launcher - Silver",
                "Firing Range: Rocket Launcher - Gold",
                "Firing Range: Slayer - Bronze",
                "Firing Range: Slayer - Silver",
                "Firing Range: Slayer - Gold",
                "Firing Range: Combat Knife - Bronze",
                "Firing Range: Combat Knife - Silver",
                "Firing Range: Combat Knife - Gold",
                "Firing Range: Crossbow - Bronze",
                "Firing Range: Crossbow - Silver",
                "Firing Range: Crossbow - Gold",
                "Firing Range: Tranquilizer - Bronze",
                "Firing Range: Tranquilizer - Silver",
                "Firing Range: Tranquilizer - Gold",
                "Firing Range: Laser - Bronze",
                "Firing Range: Laser - Silver",
                "Firing Range: Laser - Gold",
                "Firing Range: Grenade - Bronze",
                "Firing Range: Grenade - Silver",
                "Firing Range: Grenade - Gold",
                "Firing Range: Timed Mine - Bronze",
                "Firing Range: Timed Mine - Silver",
                "Firing Range: Timed Mine - Gold",
                "Firing Range: Proximity Mine - Bronze",
                "Firing Range: Proximity Mine - Silver",
                "Firing Range: Proximity Mine - Gold",
                "Firing Range: Remote Mine - Bronze",
                "Firing Range: Remote Mine - Silver",
                "Firing Range: Remote Mine - Gold"
            ]
        )
        carrington_institute.add_locations(training_locations, PerfectDarkLocation)

    if world.options.device_training:
        device_training_locations = get_location_names_with_ids(
            [
                "Device Training: Data Uplink",
                "Device Training: ECM Mine",
                "Device Training: CamSpy",
                "Device Training: Night Vision",
                "Device Training: Door Decoder",
                "Device Training: R-Tracker",
                "Device Training: IR Scanner",
                "Device Training: X-Ray Scanner",
                "Device Training: Disguise",
                "Device Training: Cloaking Device"
            ]
        )
        carrington_institute.add_locations(device_training_locations, PerfectDarkLocation)

    if world.options.holotraining:
        holotraining_locations = get_location_names_with_ids(
            [
                "Holotraining 1: Looking Around",
                "Holotraining 2: Movement 1",
                "Holotraining 3: Movement 2",
                "Holotraining 4: Unarmed Combat 1",
                "Holotraining 5: Unarmed Combat 2",
                "Holotraining 6: Live Combat 1",
                "Holotraining 7: Live Combat 2"
            ]
        )
        carrington_institute.add_locations(holotraining_locations, PerfectDarkLocation)

    if world.options.unlock_cheats:
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete dD Defection"
            ]
        )
        defection.add_locations(cheat_locations, PerfectDarkLocation)

        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete dD Investigation"
            ]
        )
        investigation.add_locations(cheat_locations, PerfectDarkLocation)

        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete dD Extraction"
            ]
        )
        extraction.add_locations(cheat_locations, PerfectDarkLocation)

        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Carrington Villa"
            ]
        )
        villa.add_locations(cheat_locations, PerfectDarkLocation)

        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Chicago"
            ]
        )
        chicago.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete G5 Building"
            ]
        )
        g5_building.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete A51 Infiltration"
            ]
        )
        infiltration.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete A51 Rescue"
            ]
        )
        rescue.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete A51 Escape"
            ]
        )
        escape.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Air Base"
            ]
        )
        air_base.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Air Force One"
            ]
        )
        air_force_one.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Crash Site"
            ]
        )
        crash_site.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Pelagic II"
            ]
        )
        pelagic.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Deep Sea"
            ]
        )
        deep_sea.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete CI Defense"
            ]
        )
        institute_defense.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Attack Ship"
            ]
        )
        attack_ship.add_locations(cheat_locations, PerfectDarkLocation)
        
        cheat_locations = get_location_names_with_ids(
            [
                "Cheat Unlock: Complete Skedar Ruins"
            ]
        )
        skedar_ruins.add_locations(cheat_locations, PerfectDarkLocation)

        if world.options.agent:
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete dD Extraction (Agent) in under 2:03"
                ]
            )
            extraction.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete G5 Building (Agent) in under 1:40"
                ]
            )
            g5_building.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete A51 Escape (Agent) in under 3:50"
                ]
            )
            escape.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Crash Site (Agent) in under 2:50"
                ]
            )
            crash_site.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete CI Defense (Agent) in under 1:45"
                ]
            )
            institute_defense.add_locations(cheat_locations, PerfectDarkLocation)

        if world.options.special_agent:
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete dD Defection (Special Agent) in under 1:30"
                ]
            )
            defection.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Carrington Villa (Special Agent) in under 2:30"
                ]
            )
            villa.add_locations(cheat_locations, PerfectDarkLocation)
            
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete A51 Infiltration (Special Agent) in under 5:00"
                ]
            )
            infiltration.add_locations(cheat_locations, PerfectDarkLocation)
            
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Air Base (Special Agent) in under 3:11"
                ]
            )
            air_base.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Pelagic II (Special Agent) in under 7:07"
                ]
            )
            pelagic.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Attack Ship (Special Agent) in under 5:17"
                ]
            )
            attack_ship.add_locations(cheat_locations, PerfectDarkLocation)

        if world.options.perfect_agent:
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete dD Investigation (Perfect Agent) in under 6:30"
                ]
            )
            investigation.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Chicago (Perfect Agent) in under 2:00"
                ]
            )
            chicago.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete A51 Rescue (Perfect Agent) in under 7:59"
                ]
            )
            rescue.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Air Force One (Perfect Agent) in under 3:55"
                ]
            )
            air_force_one.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Deep Sea (Perfect Agent) in under 7:27"
                ]
            )
            deep_sea.add_locations(cheat_locations, PerfectDarkLocation)

            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Complete Skedar Ruins (Perfect Agent) in under 5:31"
                ]
            )
            skedar_ruins.add_locations(cheat_locations, PerfectDarkLocation)

        if world.options.weapon_training:
            cheat_locations = get_location_names_with_ids(
                [
                    "Cheat Unlock: Get gold medals for Falcon 2, Falcon 2 (Silencer), and Falcon 2 (Scope)",
                    "Cheat Unlock: Get gold medals for MagSec 4, Mauler, Phoenix, DY357 Magnum, and DY357-LX",
                    "Cheat Unlock: Get gold medals for CMP150, Cyclone, Callisto NTG, and RC-P120",
                    "Cheat Unlock: Get gold medals for Laptop Gun, Dragon, K7 Avenger, AR34, and SuperDragon",
                    "Cheat Unlock: Get gold medals for Shotgun, Sniper Rifle, Rocket Launcher, and Slayer",
                    "Cheat Unlock: Get gold medals for Timed Mine, Proximity Mine, and Remote Mine",
                    "Cheat Unlock: Get gold medals for FarSight XR-20, Crossbow, Combat Knife, and Grenade",
                    "Cheat Unlock: Get gold medals for Tranquilizer, Reaper, and Devastator",
                ]
            )            
            carrington_institute.add_locations(cheat_locations, PerfectDarkLocation)
