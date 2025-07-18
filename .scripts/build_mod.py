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
            # Handle lists of complex items (e.g., list of focuses)
            for item in value:
                s += f"{tabs}{key} = {{\n"
                s += dict_to_pdx_string(item, indent + 1)
                s += f"{tabs}}}\n"
        else:
            # Handle simple key-value pairs
            # Add quotes around values that are strings but not simple yes/no/numbers
            if isinstance(value, str) and value not in ['yes', 'no'] and not value.replace('.','',1).isdigit():
                 s += f'{tabs}{key} = "{value}"\n'
            else:
                 s += f"{tabs}{key} = {value}\n"
    return s

def main():
    """
    Main function to build the mod.
    As a first test, we will just "rebuild" one of the vanilla files we parsed
    to prove that our parser and generator can work together.
    """
    # --- CONFIGURATION ---
    # The source of our parsed vanilla data
    vanilla_source_dir = os.path.join(os.path.dirname(__file__), '..', 'source_data', 'vanilla_base')
    # The final output directory for the playable mod
    build_dir = os.path.join(os.path.dirname(__file__), '..', 'build', 'total_war_mod')

    # --- SCRIPT ---
    # Let's use a simple file for our first test.
    test_input_filename = "common/ideologies/00_ideologies.yml"
    test_output_filename = "common/ideologies/00_ideologies.txt"

    input_file_path = os.path.join(vanilla_source_dir, test_input_filename)
    output_file_path = os.path.join(build_dir, test_output_filename)

    if not os.path.exists(input_file_path):
        print(f"[ERROR] Test input file not found: {input_file_path}")
        print("Please ensure the parser has run successfully and the file exists.")
        return

    print(f"--- Rebuilding Test File: {test_input_filename} ---")

    # 1. Read the YAML data
    print("  -> Reading YAML source...")
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 2. Convert data to Paradox Script string
    print("  -> Generating Paradox script...")
    pdx_content = dict_to_pdx_string(data)

    # 3. Write the final .txt file
    print(f"  -> Writing to build directory: {os.path.relpath(output_file_path, build_dir)}")
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8-sig') as f:
        f.write(pdx_content)

    print("\nTest build complete! Check the 'build' folder.")

if __name__ == "__main__":
    main()