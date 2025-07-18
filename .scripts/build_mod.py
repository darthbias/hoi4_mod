# build_mod.py
# The generator script that reads our YAML source data and builds the final mod files.

import yaml
import os

def dict_to_pdx_string(data, indent=0):
    """
    Recursively converts a Python dictionary back into a Paradox-formatted string.
    This is the core of the generator.
    """
    s = ""
    tabs = "\t" * indent
    for key, value in data.items():
        # Handle special case for unkeyed lists (like in categories)
        if key == '_values':
            for item in value:
                s += f"{tabs}{item}\n"
            continue

        if isinstance(value, dict):
            s += f"{tabs}{key} = {{\n"
            s += dict_to_pdx_string(value, indent + 1)
            s += f"{tabs}}}\n"
        elif isinstance(value, list):
            # Handle lists of items. This is the crucial change.
            for item in value:
                if isinstance(item, dict):
                    # This is a list of complex blocks, like focuses or ideas.
                    # Each one gets its own `key = { ... }` block.
                    s += f"{tabs}{key} = {{\n"
                    s += dict_to_pdx_string(item, indent + 1)
                    s += f"{tabs}}}\n"
                else:
                    # This is a list of simple values, like prerequisites.
                    # Each one gets its own `key = value` line.
                    s += f"{tabs}{key} = {item}\n"
        else:
            # Handle simple key-value pairs
            # Add quotes around values that are strings but not simple yes/no/numbers
            if isinstance(value, str) and value not in ['yes', 'no'] and not str(value).replace('.','',1).isdigit():
                 s += f'{tabs}{key} = "{value}"\n'
            else:
                 s += f"{tabs}{key} = {value}\n"
    return s

def main():
    """
    Main function to build the mod. It reads all YAML files from a source
    directory and generates the final Paradox-formatted text files.
    """
    # --- CONFIGURATION ---
    # The source of our parsed vanilla data
    script_dir = os.path.dirname(__file__)
    vanilla_source_dir = os.path.join(script_dir, '..', 'source_data', 'vanilla_base')
    mod_source_dir = os.path.join(script_dir, '..', 'source_data', 'total_war_mod')
    # The final output directory for the playable mod
    build_dir = os.path.join(script_dir, '..', 'build', 'total_war_mod')

    # --- SCRIPT ---
    print(f"Starting mod build process...")

    # 1. Gather all files, with mod files overriding vanilla files.
    files_to_build = {}
    # First, add all vanilla files to the build list.
    if os.path.exists(vanilla_source_dir):
        for root, _, files in os.walk(vanilla_source_dir):
            for filename in files:
                if filename.endswith(".yml"):
                    full_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(full_path, vanilla_source_dir)
                    files_to_build[relative_path] = full_path
    else:
        print(f"[WARNING] Vanilla source directory not found: {vanilla_source_dir}")
        print("Please ensure the parser has run successfully.")

    # Second, walk through the mod directory and add/overwrite files.
    if os.path.exists(mod_source_dir):
        for root, _, files in os.walk(mod_source_dir):
            for filename in files:
                if filename.endswith(".yml"):
                    full_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(full_path, mod_source_dir)
                    files_to_build[relative_path] = full_path # This adds new files and overwrites vanilla ones

    # 2. Build all files in the final list.
    print(f"Found {len(files_to_build)} files to build.")
    for relative_path, input_file_path in files_to_build.items():
        # Change the extension from .yml to .txt for the output
        output_file_path_no_ext, _ = os.path.splitext(os.path.join(build_dir, relative_path))
        output_file_path = output_file_path_no_ext + ".txt"

        print(f"\n--- Building: {relative_path} ---")
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        try:
            with open(input_file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            pdx_content = dict_to_pdx_string(data)
            
            with open(output_file_path, 'w', encoding='utf-8-sig') as f:
                f.write(pdx_content)
            print(f"  -> Successfully built to: {os.path.relpath(output_file_path, build_dir)}")
        except Exception as e:
            print(f"  [ERROR] Failed to build {relative_path}: {e}")

    print("\n\nFull build process complete!")

if __name__ == "__main__":
    main()