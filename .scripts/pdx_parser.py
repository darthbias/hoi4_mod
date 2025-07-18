# pdx_parser.py
# A robust parser to convert Paradox's scripting language into a Python dictionary.

import re
import yaml # Requires PyYAML: pip install pyyaml
import os

def _tokenize(text):
    """
    Converts a string of Paradox script into a list of tokens.
    This is the lexical analysis stage.
    """
    # Remove comments
    text = re.sub(r'#.*', '', text)
    # Add space around braces and equals signs to ensure they are tokenized correctly
    text = text.replace('{', ' { ')
    text = text.replace('}', ' } ')
    text = text.replace('=', ' = ')
    # Find all tokens (words, quoted strings, operators)
    token_regex = re.compile(r'\"[^"]*\"|\S+')
    tokens = token_regex.findall(text)
    return tokens

class PdxParser:
    """
    A recursive descent parser for Paradox's scripting language.
    It converts a list of tokens into a nested Python dictionary.
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def _peek(self):
        """Return the next token without consuming it."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def _consume(self):
        """Consume and return the current token, then advance."""
        token = self._peek()
        if token is not None:
            self.position += 1
        return token

    def _parse_value(self):
        """Parse a value, which can be a literal or a block."""
        if self._peek() == '{':
            return self._parse_block()
        else:
            token = self._consume()
            try:
                return int(token)
            except (ValueError, TypeError):
                try:
                    return float(token)
                except (ValueError, TypeError):
                    return token.strip('"')

    def _parse_kv_pair(self):
        """Parse a key-value pair."""
        key = self._consume()
        if self._peek() != '=':
            # This handles cases like `item` in `list = { item item }`
            # We treat the key itself as a value in a list.
            return None, key.strip('"')

        self._consume()  # Consume '='
        value = self._parse_value()
        return key, value

    def _parse_block(self):
        """Parse a block enclosed in curly braces."""
        data = {}
        self._consume()  # Consume '{'

        while self._peek() and self._peek() != '}':
            key, value = self._parse_kv_pair()

            if key is None: # This was a list item
                # This is a simple way to handle lists of unkeyed values.
                # A more robust implementation might use a special key like '_values'.
                if '_values' not in data:
                    data['_values'] = []
                data['_values'].append(value)
                continue

            # Handle duplicate keys by turning them into a list
            if key in data:
                if not isinstance(data[key], list):
                    data[key] = [data[key]]
                data[key].append(value)
            else:
                data[key] = value

        self._consume()  # Consume '}'
        return data

    def parse(self):
        """Starts the parsing process for the entire file."""
        data = {}
        while self._peek():
            key, value = self._parse_kv_pair()
            if key in data:
                if not isinstance(data[key], list):
                    data[key] = [data[key]]
                data[key].append(value)
            else:
                data[key] = value
        return data

def main():
    """
    Main function to parse an entire directory of vanilla files and output them as YAML.
    """
    # --- CONFIGURATION ---
    vanilla_root = "c:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV"
    # A list of all top-level directories we want to parse from the vanilla game.
    # We can add more here as needed (e.g., "decisions", "interface").
    target_directories = ["common", "events", "gfx"]
    
    # --- SCRIPT ---
    output_dir_root = os.path.join(os.path.dirname(__file__), '..', 'source_data', 'vanilla_base')

    for target_directory in target_directories:
        input_dir_path = os.path.join(vanilla_root, target_directory)

        if not os.path.exists(input_dir_path):
            print(f"[WARNING] Vanilla directory not found, skipping: {input_dir_path}")
            continue

        print(f"\n==================================================")
        print(f"Starting batch parse of directory: {target_directory}")
        print(f"==================================================")

        for root, _, files in os.walk(input_dir_path):
            for filename in files:
                # We expand this to include other relevant file types
                if not filename.endswith((".txt", ".gfx")):
                    continue

                input_file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_file_path, vanilla_root)
                output_file_path_no_ext, _ = os.path.splitext(os.path.join(output_dir_root, relative_path))
                output_file_path = output_file_path_no_ext + ".yml"

                print(f"\n--- Processing: {relative_path} ---")
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                try:
                    with open(input_file_path, 'r', encoding='utf-8-sig') as f:
                        text = f.read()
                    
                    if not text.strip():
                        print("  -> Skipping empty file.")
                        continue

                    tokens = _tokenize(text)
                    parser = PdxParser(tokens)
                    parsed_data = parser.parse()
                    
                    with open(output_file_path, 'w', encoding='utf-8') as f:
                        yaml.dump(parsed_data, f, default_flow_style=False, sort_keys=False, indent=2)
                    print(f"  -> Successfully parsed to: {os.path.relpath(output_file_path, output_dir_root)}")

                except Exception as e:
                    print(f"  [ERROR] Failed to parse {filename}: {e}")

    print("\n\nBatch parsing complete!")

if __name__ == "__main__":
    main()