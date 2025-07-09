import json
from collections import defaultdict
import os

def generate_scoped_docs(data_key, json_data, output_dir, output_filename, title, **kwargs):
    """
    Generates documentation for items that are organized by scope (like Effects and Triggers).
    """
    documentation_data = json_data.get(data_key, {})
    if not documentation_data:
        print(f"No '{data_key}' data found in the JSON file.")
        return

    print(f"Organizing {title} by scope...")
    items_by_scope = defaultdict(list)
    scope_key = kwargs.get('scope_key', 'supported_scope') # Allow overriding the key for scopes

    for item_name, details in documentation_data.items():
        scopes = details.get(scope_key, [])
        if not scopes:
            items_by_scope["Uncategorized"].append((item_name, details))
        else:
            # Ensure scopes is a list
            if not isinstance(scopes, list):
                scopes = [scopes]
            for scope in scopes:
                items_by_scope[scope].append((item_name, details))

    output_path = os.path.join(output_dir, output_filename)
    print(f"Generating Markdown file at '{output_path}'...")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write("## Table of Content\n\n")
        
        sorted_scopes = sorted(items_by_scope.keys(), key=lambda s: (s == 'Uncategorized', s.upper()))

        for scope in sorted_scopes:
            f.write(f"* [{scope.upper()}](#{title.lower()}-for-scope-{scope.lower()})\n")
        f.write("\n")

        for scope in sorted_scopes:
            f.write(f"## {title} for scope {scope.upper()}\n\n")
            
            sorted_items = sorted(items_by_scope[scope], key=lambda item: item[0])
            for item_name, _ in sorted_items:
                f.write(f"* [{item_name}](#{item_name.lower()})\n")
            f.write("\n")

            for item_name, details in sorted_items:
                f.write(f"### {item_name}\n\n")
                
                scopes_str = ", ".join(details.get(scope_key, ["none"]))
                targets_str = ", ".join(details.get("supported_target", ["none"]))
                
                f.write(f"* Supported Scopes: {scopes_str}\n")
                if "supported_target" in details:
                    f.write(f"* Supported Targets: {targets_str}\n")
                
                description = details.get("description", "No description available.").strip()
                if description:
                    f.write(f"\n```hoi4\n{description}\n```\n\n")
                else:
                    f.write("\n")


    print(f"Successfully generated '{output_filename}'.")

def generate_simple_kv_docs(data_key, json_data, output_dir, output_filename, title, **kwargs):
    """
    Generates documentation for simple key-value sections (like Script Concepts).
    """
    documentation_data = json_data.get(data_key, {})
    if not documentation_data:
        print(f"No '{data_key}' data found in the JSON file.")
        return

    output_path = os.path.join(output_dir, output_filename)
    print(f"Generating Markdown file at '{output_path}'...")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write("## Table of Content\n\n")
        
        sorted_keys = sorted(documentation_data.keys())
        for key in sorted_keys:
            anchor = key.lower().replace(' ', '-')
            f.write(f"* [{key}](#{anchor})\n")
        f.write("\n")

        for key in sorted_keys:
            f.write(f"## {key}\n")
            content = documentation_data[key]
            if content.startswith("![MD]"):
                content = content[len("![MD]"):].strip()
            f.write(content)
            f.write("\n\n")

    print(f"Successfully generated '{output_filename}'.")

def generate_modifiers_docs(data_key, json_data, output_dir, output_filename, title, **kwargs):
    """
    Generates documentation for the complex 'modifiers' list.
    """
    modifiers_data = json_data.get(data_key, [])
    if not modifiers_data:
        print(f"No '{data_key}' data found in the JSON file.")
        return

    print(f"Organizing {title} by category...")
    modifiers_by_category = defaultdict(list)
    all_modifiers = []

    for mod_info in modifiers_data:
        name = mod_info.get("name") or mod_info.get("groupname")
        if not name:
            continue
        
        all_modifiers.append((name, mod_info))
        categories = mod_info.get("categories", ["Uncategorized"])
        for category in categories:
            modifiers_by_category[category].append(name)

    output_path = os.path.join(output_dir, output_filename)
    print(f"Generating Markdown file at '{output_path}'...")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write("Modifiers listed here are recognized by the game, but not necessarily used in any context.\n\n")
        f.write("The listed decimal places is for display only. All numbers support up to 3 decimal places.\n\n")

        f.write("## Table of Content\n\n")
        sorted_categories = sorted(modifiers_by_category.keys())
        for category in sorted_categories:
            f.write(f"* [{category}](#modifiers-for-scope-{category})\n")
        f.write("\n")

        for category in sorted_categories:
            f.write(f"## Modifiers for scope {category}\n\n")
            unique_mods = sorted(list(set(modifiers_by_category[category])))
            for mod_name in unique_mods:
                anchor = mod_name.replace('<', '').replace('>', '').replace('_', '-')
                f.write(f"* [{mod_name}](#{anchor})\n")
            f.write("\n")

        all_modifiers.sort(key=lambda x: x[0])
        for name, details in all_modifiers:
            anchor = name.replace('<', '').replace('>', '').replace('_', '-')
            f.write(f"## <a id=\"{anchor}\"/>{name}\n\n")
            
            if "desc" in details:
                f.write(f"* **Description**: {details['desc']}\n")
            
            if "type" in details:
                f.write(f"* {details['type'].capitalize()}")
                if "decimal_places" in details:
                    f.write(f" with {details['decimal_places']} decimal places")
                f.write("\n")

            if "categories" in details:
                f.write(f"* **Categories**: {', '.join(details['categories'])}\n")

            if "modifiers" in details:
                 f.write(f"* **Modified types**: {', '.join(details['modifiers'])}\n")
            
            f.write("\n")

    print(f"Successfully generated '{output_filename}'.")

def generate_loc_objects_docs(data_key, json_data, output_dir, output_filename, title, **kwargs):
    """
    Generates documentation for Localization Objects.
    """
    loc_objects_data = json_data.get(data_key, {})
    if not loc_objects_data:
        print(f"No '{data_key}' data found in the JSON file.")
        return

    output_path = os.path.join(output_dir, output_filename)
    print(f"Generating Markdown file at '{output_path}'...")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write("## Table of Content\n\n")
        
        sorted_objects = sorted(loc_objects_data.keys())
        for obj_name in sorted_objects:
            f.write(f"* [{obj_name}](#{obj_name.lower()})\n")
        f.write("\n")

        for obj_name in sorted_objects:
            details = loc_objects_data[obj_name]
            f.write(f"## {obj_name}\n\n")

            if "doc" in details and details["doc"]:
                content = details["doc"]
                if content.startswith("![MD]"):
                    content = content[len("![MD]"):].strip()
                f.write(f"{content}\n\n")

            for section_name in ["promotions", "properties"]:
                f.write(f"### {section_name.capitalize()}\n")
                items = details.get(section_name, [])
                if items:
                    for item in sorted(items, key=lambda p: p['name']):
                        f.write(f"**{item['name']}**\n\n")
                        doc = item.get('doc', 'No description available.')
                        if doc.startswith("![MD]"):
                            doc = doc[len("![MD]"):].strip()
                        f.write(f"{doc}\n\n")
                else:
                    f.write("\n")

    print(f"Successfully generated '{output_filename}'.")

def generate_console_docs(data_key, json_data, output_dir, output_filename, title, **kwargs):
    """
    Generates documentation for Console Commands and Tweakables.
    """
    console_data = json_data.get(data_key, {})
    if not console_data:
        print(f"No '{data_key}' data found in the JSON file.")
        return

    output_path = os.path.join(output_dir, output_filename)
    print(f"Generating Markdown file at '{output_path}'...")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")

        for section_key, section_title in [('commands', 'Commands'), ('tweakables', 'Tweakables')]:
            section_data = console_data.get(section_key, {})
            if not section_data:
                continue

            f.write(f"## {section_title}\n\n")
            sorted_keys = sorted(section_data.keys())

            for key in sorted_keys:
                details = section_data[key]
                f.write(f"### {key}\n\n")
                
                if "description" in details and details["description"]:
                    f.write(f"* **Description**: {details['description']}\n")
                if "aliases" in details:
                    f.write(f"* **Aliases**: {', '.join(details['aliases'])}\n")
                if "arguments" in details:
                    f.write(f"* **Arguments**: `{' '.join(details['arguments'])}`\n")
                if "type" in details:
                    f.write(f"* **Type**: {details['type']}\n")
                f.write("\n")

    print(f"Successfully generated '{output_filename}'.")

if __name__ == '__main__':
    # --- Configuration ---
    json_file_path = 'c:\\Users\\Anwender\\Documents\\GitHub\\hoi4_mod_tw\\bicemodded\\common\\documentation\\script_documentation.json'
    output_directory = '.' # Save the output in the current directory

    # --- List of documentation files to generate ---
    # To add or remove a file, modify this list.
    # The format is: (json_key, output_filename, markdown_title, generator_function, optional_kwargs_dict)
    docs_to_generate = [
        ('effects', 'Effects.md', 'Effects', generate_scoped_docs, {}),
        ('triggers', 'Triggers.md', 'Triggers', generate_scoped_docs, {}),
        ('modifiers', 'Modifiers.md', 'Modifiers', generate_modifiers_docs, {}),
        ('script_concepts', 'Script Concepts.md', 'Script Concepts', generate_simple_kv_docs, {}),
        ('loc_objects', 'Localization Objects.md', 'Localization Objects', generate_loc_objects_docs, {}),
        ('loc_formatter', 'Localization Formatters.md', 'Localization Formatters', generate_simple_kv_docs, {}),
        ('console_commands', 'Console.md', 'Console Commands', generate_console_docs, {}),
        ('dynamic_variables', 'Dynamic Variables.md', 'Dynamic Variables', generate_scoped_docs, {'scope_key': 'scope'}),
    ]

    # --- Execution ---
    print("Loading data from JSON...")
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")
        exit()
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file_path}' is not a valid JSON file.")
        exit()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    for key, filename, title, generator_func, kwargs in docs_to_generate:
        generator_func(key, json_data, output_directory, filename, title, **kwargs)
