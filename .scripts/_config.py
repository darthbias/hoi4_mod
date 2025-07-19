# _config.py
# A centralized configuration file for all scripts in the toolchain.

import os

# --- Core Paths ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
VANILLA_ROOT = "c:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV"
VANILLA_BASE_DIR = os.path.join(PROJECT_ROOT, 'source_data', 'vanilla_base')
MOD_SOURCE_DIR = os.path.join(PROJECT_ROOT, 'source_data', 'total_war_mod')
BUILD_DIR = os.path.join(PROJECT_ROOT, 'build', 'total_war_mod')

# --- Script Settings ---

# Directories to scan for parsable script files (.txt, .gfx, .asset)
PARSER_TARGET_DIRS = ["common", "events", "gfx", "history", "interface", "map", "music"]

# Directories to scan for any other assets (.dds, .gui, .lua, .ogg, etc.)
ASSET_TARGET_DIRS = ["common", "events", "gfx", "history", "interface", "localisation", "map", "music"]

# A list of specific files to EXCLUDE from parsing and copy directly instead.
# These are typically files that use a .txt extension but are not in standard Paradox script format.
EXCLUSION_LIST = [
    "map/adjacencies.txt",
    "map/airports.txt",
    "map/buildings.txt",
    "map/railways.txt",
    "map/rocketsites.txt",
    "map/unit_icons.txt"
]