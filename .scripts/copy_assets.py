# copy_assets.py
# A script to copy non-parsable but necessary files (like .lua) into our source tree.

import os
from _config import VANILLA_ROOT, VANILLA_BASE_DIR, ASSET_TARGET_DIRS, EXCLUSION_LIST
import shutil

def main():
    """
    Main function to copy asset files from the vanilla game directory.
    """
    # --- CONFIGURATION ---
    # Configuration is now imported from _config.py
    # Define file extensions that are handled by the PARSER. We will copy everything else.
    PARSABLE_EXTENSIONS = (".txt", ".gfx", ".asset")

    # --- SCRIPT ---
    print("Starting asset copy process...")
    for target_dir in ASSET_TARGET_DIRS:
        input_dir_path = os.path.join(VANILLA_ROOT, target_dir)
        if not os.path.exists(input_dir_path):
            print(f"[WARNING] Directory not found, skipping: {input_dir_path}")
            continue

        for root, _, files in os.walk(input_dir_path):
            for filename in files:
                input_file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_file_path, VANILLA_ROOT).replace('\\', '/')

                # We copy a file if it's on the exclusion list OR if it's not a parsable type.
                if relative_path in EXCLUSION_LIST or not filename.lower().endswith(PARSABLE_EXTENSIONS):
                    # Use the os-specific separator for the output path
                    output_file_path = os.path.join(VANILLA_BASE_DIR, relative_path.replace('/', os.sep))
                    
                    print(f"  -> Copying: {relative_path}")
                    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                    shutil.copy2(input_file_path, output_file_path)

    print("\nAsset copy complete!")

if __name__ == "__main__":
    main()