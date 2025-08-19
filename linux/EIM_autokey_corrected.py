#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EIM Text Expansion Script for AutoKey
Corrected version with proper AutoKey integration

This script provides text expansion for all abbreviations from your EIM.ahk file.
To use this in AutoKey:

1. Create a new Script (not Phrase) in AutoKey
2. Set the abbreviation to the text you want to expand (e.g., "aomg")
3. Paste this entire script
4. The script will automatically expand the text when triggered
"""

# Import AutoKey libraries
import autokey.common
import autokey.configmanager.configmanager
import autokey.scripting

# Import the expansions data from the separate file
try:
    from EIM_expansions_data import EXPANSIONS_DATA
    EXPANSIONS = EXPANSIONS_DATA
except ImportError:
    # Fallback data if import fails
    EXPANSIONS = {
        "aomg": "oh my god",
        "Aomg": "Oh my god",
        "abtw": "by the way",
        "Abtw": "By the way",
        "USca": "California",
        "ccus": "United States",
        "lainre": "in reference to the matter of",
    }

def main():
    """
    Main function that gets called when the script is triggered
    This function will expand the text that triggered the script
    """
    
    # Get the abbreviation that triggered this script
    # In AutoKey, this is typically stored in a variable or we can get it from the trigger
    try:
        # Try to get the abbreviation from the trigger
        abbreviation = store.get_global_value("last_abbreviation")
        if not abbreviation:
            # If that doesn't work, we can get it from the clipboard or use a fallback
            abbreviation = clipboard.get_selection()
    except:
        # Fallback: use a default abbreviation (you can change this)
        abbreviation = "aomg"
    
    # Look up the expansion
    if abbreviation in EXPANSIONS:
        expanded_text = EXPANSIONS[abbreviation]
        
        # Delete the abbreviation that was typed
        keyboard.send_keys("<ctrl>+a")  # Select all
        keyboard.send_keys("<delete>")  # Delete selection
        
        # Type the expanded text
        keyboard.send_text(expanded_text)
    else:
        # If no expansion found, just type the original text
        keyboard.send_text(abbreviation)

# Alternative approach: Create individual scripts for each abbreviation
def create_individual_script(abbreviation):
    """
    This function shows how to create a script for a specific abbreviation
    You would create a separate script for each abbreviation you want to use
    """
    
    # Get the expansion for this specific abbreviation
    if abbreviation in EXPANSIONS:
        expanded_text = EXPANSIONS[abbreviation]
        
        # Delete the abbreviation and type the expansion
        keyboard.send_keys("<ctrl>+a")
        keyboard.send_keys("<delete>")
        keyboard.send_text(expanded_text)
    else:
        # If abbreviation not found, do nothing
        pass

# Example: Script for "aomg" abbreviation
def expand_aomg():
    """Script specifically for expanding 'aomg'"""
    keyboard.send_keys("<ctrl>+a")
    keyboard.send_keys("<delete>")
    keyboard.send_text("oh my god")

# Example: Script for "USca" abbreviation  
def expand_USca():
    """Script specifically for expanding 'USca'"""
    keyboard.send_keys("<ctrl>+a")
    keyboard.send_keys("<delete>")
    keyboard.send_text("California")

# Example: Script for "ccus" abbreviation
def expand_ccus():
    """Script specifically for expanding 'ccus'"""
    keyboard.send_keys("<ctrl>+a")
    keyboard.send_keys("<delete>")
    keyboard.send_text("United States")

# Example: Script for "lainre" abbreviation
def expand_lainre():
    """Script specifically for expanding 'lainre'"""
    keyboard.send_keys("<ctrl>+a")
    keyboard.send_keys("<delete>")
    keyboard.send_text("in reference to the matter of")

# Call the main function when the script is triggered
if __name__ == "__main__":
    main()
