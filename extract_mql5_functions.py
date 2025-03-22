import os
import re
import chardet  # Install this module using `pip install chardet`

# Path to the folder containing the MQL5 include files
INCLUDE_FOLDER = "mql5-includes"

# Path to the JSON file where we'll update function highlighting
SYNTAX_FILE = "syntaxes/mql5.tmLanguage.json"

# Regular expression to match function definitions
FUNCTION_REGEX = re.compile(r"\b(?:bool|int|double|void|string|float|datetime|char)\s+([a-zA-Z0-9_]+)\s*\(")

# Collect all function names
function_names = set()

# Function to detect encoding
def detect_encoding(filepath):
    with open(filepath, "rb") as file:
        raw_data = file.read(1024)  # Read first 1KB for encoding detection
        encoding = chardet.detect(raw_data)['encoding']
    return encoding or "utf-8"  # Default to UTF-8 if detection fails

# Read all .mqh files in the include folder
for filename in os.listdir(INCLUDE_FOLDER):
    if filename.endswith(".mqh"):
        filepath = os.path.join(INCLUDE_FOLDER, filename)

        # Detect encoding and read file
        encoding = detect_encoding(filepath)
        try:
            with open(filepath, "r", encoding=encoding) as file:
                content = file.read()
                matches = FUNCTION_REGEX.findall(content)
                function_names.update(matches)
        except UnicodeDecodeError:
            print(f"⚠️ Warning: Could not decode {filename} with encoding {encoding}. Skipping file.")

# Convert to sorted list for consistency
function_names = sorted(function_names)

# Update the syntax file
if os.path.exists(SYNTAX_FILE):
    with open(SYNTAX_FILE, "r", encoding="utf-8") as file:
        syntax_data = file.read()

    # Replace the support.function.mql5 section
    new_functions = f"\\b({'|'.join(function_names)})\\b"
    syntax_data = re.sub(
        r'"name": "support\.function\.mql5",\s*"match": ".*?"',
        f'"name": "support.function.mql5", "match": "{new_functions}"',
        syntax_data,
        flags=re.DOTALL
    )

    # Write back to the file
    with open(SYNTAX_FILE, "w", encoding="utf-8") as file:
        file.write(syntax_data)

    print(f"✅ Extracted {len(function_names)} functions and updated {SYNTAX_FILE}")
else:
    print(f"❌ Syntax file {SYNTAX_FILE} not found!")
