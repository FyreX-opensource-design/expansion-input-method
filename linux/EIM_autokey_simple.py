#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EIM Text Expansion for AutoKey - Simple Version

This is a template script for AutoKey. To use this:

1. In AutoKey, create a NEW SCRIPT (not phrase)
2. Set the abbreviation to the text you want to expand (e.g., "aomg")
3. Replace the content below with the expansion you want
4. Save and enable the script

Example: For "aomg" abbreviation, replace the keyboard.send_text line with:
keyboard.send_text("oh my god")
"""

# This script will be triggered when you type the abbreviation
# The abbreviation is set in the AutoKey script settings

# Delete the abbreviation that was typed
keyboard.send_keys("<ctrl>+a")  # Select all text
keyboard.send_keys("<delete>")  # Delete the selection

# Type the expanded text - CHANGE THIS TO YOUR DESIRED EXPANSION
keyboard.send_text("REPLACE_WITH_YOUR_EXPANSION")

# Example expansions you can use:
# keyboard.send_text("oh my god")           # for "aomg"
# keyboard.send_text("by the way")          # for "abtw"  
# keyboard.send_text("California")          # for "USca"
# keyboard.send_text("United States")       # for "ccus"
# keyboard.send_text("in reference to the matter of")  # for "lainre"
