# debug_missing_files.py
# A temporary script to find which files are missing from our vanilla_base.

import os
from _config import VANILLA_ROOT, VANILLA_BASE_DIR, EXCLUSION_LIST

def main():
    """
    Compares a vanilla directory with our generated source directory to find missing files.
    """
    # --- CONFIGURATION ---
    # Configuration is now imported from _config.py
    # The directory we want to check
    target_directory = "map"

    # --- SCRIPT ---
    vanilla_path = os.path.join(VANILLA_ROOT, target_directory)
    our_path = os.path.join(VANILLA_BASE_DIR, target_directory)

    if not os.path.exists(vanilla_path) or not os.path.exists(our_path):
        print("[ERROR] One of the directories to compare does not exist. Please run the main scripts first.")
        return

    # Get all relative file paths from the vanilla directory
    vanilla_files = set()
    for root, _, files in os.walk(vanilla_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, VANILLA_ROOT)
            vanilla_files.add(relative_path.replace('\\', '/'))

    # Get all relative file paths from our generated directory
    our_base_files = set()
    for root, _, files in os.walk(our_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, VANILLA_BASE_DIR)
            our_base_files.add(relative_path.replace('\\', '/'))

    # Create a "normalized" set of what we EXPECT the vanilla files to look like after processing
    expected_files = set()
    PARSABLE_EXTENSIONS = (".txt", ".gfx", ".asset")
    for f in vanilla_files:
        if f in EXCLUSION_LIST:
            expected_files.add(f) # Expect the file to be copied as-is
        elif f.lower().endswith(PARSABLE_EXTENSIONS):
            base, _ = os.path.splitext(f)
            expected_files.add(base + ".yml")
        else:
            expected_files.add(f)

    # Find and print the difference
    missing_files = expected_files - our_base_files
    print(f"Comparing '{vanilla_path}' with '{our_path}'...")
    if not missing_files:
        print("No missing files found! The directories are in sync.")
    else:
        print(f"\nFound {len(missing_files)} missing file(s):")
        for f in sorted(list(missing_files)):
            print(f"  - {f}")

if __name__ == "__main__":
    main()