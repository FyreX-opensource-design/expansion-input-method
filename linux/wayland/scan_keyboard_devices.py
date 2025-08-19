#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EIM Keyboard Device Scanner
Utility to scan and list available keyboard devices for configuration

Requirements:
- Python 3.6+
- evdev (Linux input device monitoring)

Installation:
pip3 install evdev

Usage:
python3 scan_keyboard_devices.py
"""

import sys
import os
from pathlib import Path

# Try to import evdev
try:
    import evdev
except ImportError:
    print("Error: evdev not available")
    print("Install with: pip3 install evdev")
    sys.exit(1)

def scan_input_devices():
    """Scan all available input devices"""
    try:
        devices = []
        for path in evdev.list_devices():
            try:
                device = evdev.InputDevice(path)
                devices.append(device)
            except Exception as e:
                print(f"Warning: Could not open device {path}: {e}")
        
        return devices
    except Exception as e:
        print(f"Error scanning devices: {e}")
        return []

def categorize_devices(devices):
    """Categorize devices by type"""
    categories = {
        'keyboards': [],
        'mice': [],
        'touchpads': [],
        'gamepads': [],
        'other': []
    }
    
    for device in devices:
        try:
            capabilities = device.capabilities()
            
            if evdev.ecodes.EV_KEY in capabilities:
                # Check if it's primarily a keyboard
                key_codes = capabilities[evdev.ecodes.EV_KEY]
                if any(code in key_codes for code in [
                    evdev.ecodes.KEY_A, evdev.ecodes.KEY_SPACE, 
                    evdev.ecodes.KEY_ENTER, evdev.ecodes.KEY_BACKSPACE
                ]):
                    categories['keyboards'].append(device)
                else:
                    categories['other'].append(device)
            
            if evdev.ecodes.EV_REL in capabilities:
                if evdev.ecodes.REL_X in capabilities[evdev.ecodes.EV_REL]:
                    if evdev.ecodes.REL_Y in capabilities[evdev.ecodes.EV_REL]:
                        categories['mice'].append(device)
                    else:
                        categories['touchpads'].append(device)
            
            if evdev.ecodes.EV_ABS in capabilities:
                if evdev.ecodes.ABS_X in capabilities[evdev.ecodes.EV_ABS]:
                    categories['gamepads'].append(device)
            
        except Exception as e:
            print(f"Warning: Could not categorize device {device.name}: {e}")
            categories['other'].append(device)
    
    return categories

def print_device_info(device, category):
    """Print detailed information about a device"""
    try:
        print(f"  📱 {device.name}")
        print(f"     Path: {device.path}")
        print(f"     Phys: {device.phys}")
        print(f"     Uniq: {device.uniq}")
        print(f"     Bus: {device.info.bustype}")
        print(f"     Vendor: {device.info.vendor:04x}")
        print(f"     Product: {device.info.product:04x}")
        
        # Show capabilities
        capabilities = device.capabilities()
        if evdev.ecodes.EV_KEY in capabilities:
            key_count = len(capabilities[evdev.ecodes.EV_KEY])
            print(f"     Keys: {key_count} supported")
        
        if evdev.ecodes.EV_REL in capabilities:
            rel_count = len(capabilities[evdev.ecodes.EV_REL])
            print(f"     Relative axes: {rel_count}")
        
        if evdev.ecodes.EV_ABS in capabilities:
            abs_count = len(capabilities[evdev.ecodes.EV_ABS])
            print(f"     Absolute axes: {abs_count}")
        
        print()
        
    except Exception as e:
        print(f"  Error getting device info: {e}")

def generate_config_snippet(devices, category):
    """Generate configuration snippet for devices"""
    if not devices:
        return ""
    
    paths = [f'"{device.path}"' for device in devices]
    return f'  "keyboard_devices": [{", ".join(paths)}],'

def main():
    """Main function"""
    print("🔍 EIM Keyboard Device Scanner")
    print("=" * 50)
    print()
    
    # Scan devices
    print("Scanning input devices...")
    devices = scan_input_devices()
    
    if not devices:
        print("No input devices found!")
        return
    
    print(f"Found {len(devices)} input device(s)")
    print()
    
    # Categorize devices
    categories = categorize_devices(devices)
    
    # Display results
    for category_name, category_devices in categories.items():
        if category_devices:
            print(f"🎯 {category_name.upper()} ({len(category_devices)} device(s))")
            print("-" * 40)
            
            for device in category_devices:
                print_device_info(device, category_name)
    
    # Generate configuration
    print("⚙️  CONFIGURATION")
    print("=" * 50)
    print("Add this to your eim_config.json file:")
    print()
    
    if categories['keyboards']:
        config_snippet = generate_config_snippet(categories['keyboards'], 'keyboards')
        print(config_snippet)
        print()
        print("Or set auto_detect_keyboards to true for automatic detection.")
    else:
        print('  "auto_detect_keyboards": true,')
        print()
        print("No keyboard devices found. Check device permissions.")
    
    # Permission information
    print("🔐 PERMISSIONS")
    print("=" * 50)
    print("If devices show permission errors, you may need to:")
    print("1. Add your user to the 'input' group:")
    print("   sudo usermod -a -G input $USER")
    print("2. Create udev rules for persistent access")
    print("3. Log out and back in for group changes to take effect")
    print()
    
    # Test device access
    print("🧪 TESTING DEVICE ACCESS")
    print("=" * 50)
    testable_devices = categories['keyboards'][:3]  # Test first 3 keyboards
    
    for device in testable_devices:
        try:
            # Try to open the device
            test_device = evdev.InputDevice(device.path)
            print(f"✓ {device.name}: Accessible")
            test_device.close()
        except Exception as e:
            print(f"✗ {device.name}: {e}")
    
    print()
    print("Scan complete! Use the configuration above in your eim_config.json file.")

if __name__ == "__main__":
    main()
