# copy_assets.py
# A script to copy non-parsable but necessary files (like .lua) into our source tree.

import os
import shutil

def main():
    """
    Main function to copy asset files from the vanilla game directory.
    """
    # --- CONFIGURATION ---
    vanilla_root = "c:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV"
    output_dir_root = os.path.join(os.path.dirname(__file__), '..', 'source_data', 'vanilla_base')
    
    # Define file extensions to copy directly
    asset_extensions = (".lua", ".dds", ".tga", ".shader", ".cur", ".bmp", ".font") # We can add more here later if needed
    
    # Define directories to scan
    target_directories = ["common", "events", "gfx", "interface"]

    # --- SCRIPT ---
    print("Starting asset copy process...")
    for target_dir in target_directories:
        input_dir_path = os.path.join(vanilla_root, target_dir)
        if not os.path.exists(input_dir_path):
            print(f"[WARNING] Directory not found, skipping: {input_dir_path}")
            continue

        for root, _, files in os.walk(input_dir_path):
            for filename in files:
                if filename.endswith(asset_extensions):
                    input_file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(input_file_path, vanilla_root)
                    output_file_path = os.path.join(output_dir_root, relative_path)
                    
                    print(f"  -> Copying: {relative_path}")
                    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                    shutil.copy2(input_file_path, output_file_path)

    print("\nAsset copy complete!")

if __name__ == "__main__":
    main()