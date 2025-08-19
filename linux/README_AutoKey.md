# EIM Text Expansion for AutoKey

This is a conversion of your AutoHotkey script (`EIM.ahk`) to work with AutoKey, a cross-platform text expansion tool.

## Files Included

1. **`EIM_expansions_data.py`** - Contains all the text expansions data
2. **`EIM_autokey_corrected.py`** - Main script with proper AutoKey integration
3. **`EIM_autokey_simple.py`** - Simple template for individual abbreviations
4. **`create_autokey_scripts.py`** - Generator script to create individual AutoKey scripts
5. **`README_AutoKey.md`** - This instruction file

## What's Included

The conversion includes all the text expansions from your original AutoHotkey script:

- **Text abbreviations** (starting with 'a'): `aomg` → "oh my god"
- **Legal phrases** (starting with 'la'): `lainre` → "in reference to the matter of"
- **Word expansions** (starting with '1w'): `1wdh` → "downhill"
- **US states and territories**: `USca` → "California"
- **Canadian provinces**: `CAab` → "Alberta"
- **Australian states**: `AUact` → "Australian Capital Territory"
- **German federal states**: `DEbw` → "Baden-Württemberg"
- **Indian states**: `INan` → "Andhra Pradesh"
- **Brazilian states**: `BRac` → "Acre"
- **Mexican states**: `MXags` → "Aguascalientes"
- **Country codes**: `ccus` → "United States"
- **Nationalities**: `pccus` → "United States"
- And many more geographic and administrative divisions

## Installation Instructions

### Step 1: Install AutoKey

1. **On Windows**: Download from [AutoKey GitHub releases](https://github.com/autokey/autokey/releases)
2. **On Linux**: `sudo apt-get install autokey-gtk` (Ubuntu/Debian)
3. **On macOS**: `brew install autokey` (using Homebrew)

### Step 2: Copy Scripts to AutoKey

1. Open AutoKey
2. Go to **File** → **Open Folder** to see your scripts folder
3. Copy both Python files to this folder:
   - `EIM_expansions_data.py`
   - `EIM_autokey_corrected.py`

### Step 3: Create AutoKey Scripts

#### Option A: Use the Main Script (Advanced)

1. In AutoKey, create a new **Script** (not phrase)
2. Set the abbreviation to one of your triggers (e.g., `aomg`)
3. Paste the content from `EIM_autokey_corrected.py`
4. The script will automatically expand text when triggered

#### Option B: Individual Phrase Triggers (Recommended)

1. In AutoKey, right-click and select **New** → **Phrase**
2. Set the **Abbreviation** to one of your triggers (e.g., `aomg`)
3. In the **Script** tab, paste this code:

```python
from EIM_autokey_corrected import expand_abbreviation

# Get the abbreviation that triggered this script
abbreviation = "aomg"  # Change this for each script
expanded = expand_abbreviation(abbreviation)

# Send the expanded text
keyboard.send_text(expanded)
```

4. Repeat for each abbreviation you want to use

#### Option C: Generate Individual Scripts (Easiest)

1. Run the generator script: `python create_autokey_scripts.py`
2. This creates a folder with individual scripts for each abbreviation
3. Copy each script to AutoKey and set the appropriate abbreviation

## Usage Examples

### Basic Text Expansion

- Type `aomg` → expands to "oh my god"
- Type `abtw` → expands to "by the way"
- Type `aidk` → expands to "i don't know"

### Legal Phrases

- Type `lainre` → expands to "in reference to the matter of"
- Type `lahere` → "subject to the provisions hereof"
- Type `lalaw` → "pursuant to applicable law"

### Geographic Locations

- Type `USca` → expands to "California"
- Type `CAab` → expands to "Alberta"
- Type `AUact` → expands to "Australian Capital Territory"
- Type `DEbw` → expands to "Baden-Württemberg"

### Countries and Nationalities

- Type `ccus` → expands to "United States"
- Type `pccus` → expands to "United States"
- Type `ccgb` → expands to "England"
- Type `pccgb` → expands to "English"

## Customization

### Adding New Expansions

1. Edit `EIM_expansions_data.py`
2. Add new key-value pairs to the `EXPANSIONS_DATA` dictionary
3. Save the file
4. Restart AutoKey or reload the scripts

### Modifying Existing Expansions

1. Edit `EIM_expansions_data.py`
2. Change the value for any existing key
3. Save the file
3. Restart AutoKey or reload the scripts

### Creating Custom Scripts

You can create custom AutoKey scripts that use the expander:

```python
from EIM_autokey_corrected import expander

# Expand text from clipboard
clipboard_content = clipboard.get_selection()
if clipboard_content in expander.expansions:
    expanded = expander.expand_text(clipboard_content)
    keyboard.send_text(expanded)

# Search for expansions
results = expander.search_expansions("california")
for abbrev, expansion in results.items():
    print(f"{abbrev}: {expansion}")
```

## Troubleshooting

### Import Errors

If you get import errors:
1. Make sure both Python files are in the same AutoKey scripts folder
2. Check that the file names match exactly
3. Restart AutoKey after copying the files

### Scripts Not Working

1. Check AutoKey's log for error messages
2. Verify that the abbreviations are set correctly
3. Make sure the script is enabled in AutoKey
4. Test with a simple abbreviation first

### Performance Issues

1. The script loads all expansions into memory on startup
2. For very large numbers of expansions, consider splitting into multiple files
3. Use individual phrase triggers for better performance

## Differences from AutoHotkey

- **Syntax**: Python instead of AHK syntax
- **Setup**: Requires creating individual AutoKey scripts for each abbreviation
- **Cross-platform**: Works on Windows, Linux, and macOS
- **Integration**: Better integration with modern desktop environments
- **Customization**: More flexible scripting capabilities

## Support

If you need help:
1. Check AutoKey's documentation
2. Look at the example scripts in the main file
3. Test with simple expansions first
4. Check AutoKey's log for error messages

## License

This conversion maintains the same functionality as your original AutoHotkey script. Use it as you would the original.
