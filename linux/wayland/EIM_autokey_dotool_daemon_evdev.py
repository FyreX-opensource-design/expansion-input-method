#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EIM AutoKey Script for Wayland (dotool + evdev daemon version)
Enhanced background monitoring with direct keyboard input detection

Requirements:
- Python 3.6+
- dotool (Wayland keyboard simulation tool)
- evdev (Linux input device monitoring)
- EIM_expansions_data.py (data file)

Installation:
1. Install dotool: sudo apt install dotool (Ubuntu/Debian)
2. Install evdev: pip3 install evdev
3. Run this script in the background
4. Type abbreviations anywhere and they'll auto-expand

Usage:
python3 EIM_autokey_dotool_daemon_evdev.py &
# or
nohup python3 EIM_autokey_dotool_daemon_evdev.py > /dev/null 2>&1 &
"""

import subprocess
import sys
import time
import threading
import signal
import os
import json
from pathlib import Path
from datetime import datetime
from collections import deque

# Try to import evdev, fall back to clipboard monitoring if not available
try:
    import evdev
    EVDEV_AVAILABLE = True
except ImportError:
    EVDEV_AVAILABLE = False
    print("Warning: evdev not available. Install with: pip3 install evdev")
    print("Falling back to clipboard monitoring only.")

# Import the expansions data
try:
    from EIM_expansions_data import EXPANSIONS_DATA
except ImportError:
    print("Error: EIM_expansions_data.py not found in the same directory")
    print("Please ensure the data file is present")
    sys.exit(1)

class EIMDaemonEnhanced:
    def __init__(self, config_file="eim_config.json"):
        self.running = True
        self.last_clipboard = ""
        self.expansion_history = []
        self.max_history = 100
        self.config_file = config_file
        self.config = self.load_config()
        
        # Keyboard monitoring
        self.keyboard_devices = []
        self.current_abbreviation = ""
        self.abbreviation_buffer = deque(maxlen=20)  # Store last 20 keystrokes
        self.last_key_time = 0
        self.key_timeout = 2.0  # Reset abbreviation after 2 seconds of no input
        
        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
        # Check dotool availability
        if not self.check_dotool():
            print("Error: dotool not available. Please install it first.")
            sys.exit(1)
        
        # Initialize keyboard devices
        if EVDEV_AVAILABLE:
            self.initialize_keyboard_devices()
    
    def load_config(self):
        """Load configuration from file or create default"""
        default_config = {
            "keyboard_devices": [],
            "auto_detect_keyboards": True,
            "key_timeout": 2.0,
            "buffer_size": 20,
            "clipboard_fallback": True,
            "log_level": "INFO"
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    # Merge with defaults
                    for key, value in default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            else:
                # Create default config file
                self.save_config(default_config)
                return default_config
        except Exception as e:
            print(f"Warning: Could not load config file: {e}")
            return default_config
    
    def save_config(self, config):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config file: {e}")
    
    def initialize_keyboard_devices(self):
        """Initialize keyboard devices for monitoring"""
        if not EVDEV_AVAILABLE:
            return
        
        try:
            # Get all input devices
            devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
            
            # Filter for keyboard devices
            keyboard_devices = []
            for device in devices:
                if evdev.ecodes.EV_KEY in device.capabilities():
                    keyboard_devices.append(device)
                    print(f"Found keyboard device: {device.name} ({device.path})")
            
            # Use configured devices or auto-detect
            if self.config["keyboard_devices"]:
                # Use specific devices from config
                for device_path in self.config["keyboard_devices"]:
                    try:
                        device = evdev.InputDevice(device_path)
                        if evdev.ecodes.EV_KEY in device.capabilities():
                            self.keyboard_devices.append(device)
                            print(f"Using configured keyboard: {device.name}")
                    except Exception as e:
                        print(f"Warning: Could not open configured device {device_path}: {e}")
            elif self.config["auto_detect_keyboards"]:
                # Auto-detect and use all keyboard devices
                self.keyboard_devices = keyboard_devices
                # Save detected devices to config
                self.config["keyboard_devices"] = [d.path for d in keyboard_devices]
                self.save_config(self.config)
            
            if self.keyboard_devices:
                print(f"Monitoring {len(self.keyboard_devices)} keyboard device(s)")
            else:
                print("No keyboard devices found for monitoring")
                
        except Exception as e:
            print(f"Error initializing keyboard devices: {e}")
            self.keyboard_devices = []
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print(f"\nReceived signal {signum}, shutting down gracefully...")
        self.running = False
        
        # Close keyboard devices
        for device in self.keyboard_devices:
            try:
                device.close()
            except:
                pass
    
    def check_dotool(self):
        """Check if dotool is available"""
        try:
            result = subprocess.run(['which', 'dotool'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def get_clipboard_content(self):
        """Get current clipboard content using xclip or wl-clipboard"""
        try:
            # Try wl-clipboard first (Wayland)
            result = subprocess.run(['wl-clipboard', 'read'], 
                                  capture_output=True, text=True, timeout=1)
            if result.returncode == 0:
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        try:
            # Try xclip as fallback
            result = subprocess.run(['xclip', '-o', '-selection', 'clipboard'], 
                                  capture_output=True, text=True, timeout=1)
            if result.returncode == 0:
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        return ""
    
    def simulate_keyboard_input(self, text):
        """Simulate keyboard input using dotool"""
        try:
            result = subprocess.run(['dotool', 'type', text], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except Exception as e:
            print(f"Error typing text: {e}")
            return False
    
    def delete_previous_text(self, abbreviation_length):
        """Delete the previously typed abbreviation"""
        try:
            for _ in range(abbreviation_length):
                subprocess.run(['dotool', 'key', 'BackSpace'], 
                             capture_output=True, timeout=5)
            return True
        except Exception as e:
            print(f"Error deleting previous text: {e}")
            return False
    
    def expand_abbreviation(self, abbreviation):
        """Expand an abbreviation to its full text"""
        if abbreviation in EXPANSIONS_DATA:
            return EXPANSIONS_DATA[abbreviation]
        return None
    
    def log_expansion(self, abbreviation, expansion, method="keyboard"):
        """Log expansion to history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {abbreviation} → {expansion} ({method})"
        self.expansion_history.append(log_entry)
        
        # Keep history manageable
        if len(self.expansion_history) > self.max_history:
            self.expansion_history.pop(0)
        
        print(log_entry)
    
    def process_key_event(self, event):
        """Process individual key events for abbreviation detection"""
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == evdev.KeyEvent.key_down:
                # Get the key name
                key_name = evdev.ecodes.KEY[event.code]
                
                # Handle special keys
                if key_name == 'KEY_SPACE':
                    # Space key - check if we have an abbreviation
                    self.check_abbreviation()
                    self.current_abbreviation = ""
                    self.abbreviation_buffer.clear()
                elif key_name == 'KEY_ENTER':
                    # Enter key - check abbreviation and clear
                    self.check_abbreviation()
                    self.current_abbreviation = ""
                    self.abbreviation_buffer.clear()
                elif key_name == 'KEY_BACKSPACE':
                    # Backspace - remove last character
                    if self.current_abbreviation:
                        self.current_abbreviation = self.current_abbreviation[:-1]
                elif key_name.startswith('KEY_'):
                    # Regular key - add to abbreviation
                    if len(key_name) == 4:  # Single character key
                        char = key_name[3].lower()
                        self.current_abbreviation += char
                        self.abbreviation_buffer.append(char)
                        self.last_key_time = time.time()
                
                # Check for timeout
                if time.time() - self.last_key_time > self.config["key_timeout"]:
                    self.current_abbreviation = ""
                    self.abbreviation_buffer.clear()
    
    def check_abbreviation(self):
        """Check if current abbreviation should be expanded"""
        if not self.current_abbreviation:
            return
        
        # Check if it's a valid abbreviation
        expansion = self.expand_abbreviation(self.current_abbreviation)
        if expansion:
            print(f"\nDetected abbreviation: {self.current_abbreviation}")
            print(f"Expanding to: {expansion}")
            
            # Wait a moment for user to focus on text field
            print("Please click in a text field within 3 seconds...")
            time.sleep(3)
            
            # Delete the abbreviation and type expansion
            if self.delete_previous_text(len(self.current_abbreviation)):
                if self.simulate_keyboard_input(expansion):
                    self.log_expansion(self.current_abbreviation, expansion, "keyboard")
                    print("✓ Expansion completed successfully!")
                else:
                    print("✗ Failed to type expansion")
            else:
                print("✗ Failed to delete abbreviation")
    
    def monitor_keyboard_devices(self):
        """Monitor keyboard devices for input"""
        if not self.keyboard_devices:
            print("No keyboard devices available for monitoring")
            return
        
        print("Starting keyboard device monitoring...")
        print(f"Monitoring {len(self.keyboard_devices)} device(s)")
        
        # Create a thread for each keyboard device
        keyboard_threads = []
        for device in self.keyboard_devices:
            thread = threading.Thread(
                target=self._monitor_single_device,
                args=(device,),
                daemon=True
            )
            thread.start()
            keyboard_threads.append(thread)
        
        # Wait for threads to complete
        for thread in keyboard_threads:
            thread.join()
    
    def _monitor_single_device(self, device):
        """Monitor a single keyboard device"""
        try:
            print(f"Monitoring device: {device.name}")
            for event in device.read_loop():
                if not self.running:
                    break
                self.process_key_event(event)
        except Exception as e:
            print(f"Error monitoring device {device.name}: {e}")
        finally:
            try:
                device.close()
            except:
                pass
    
    def monitor_clipboard(self):
        """Monitor clipboard for abbreviations (fallback method)"""
        if not self.config["clipboard_fallback"]:
            return
        
        print("Starting clipboard monitoring (fallback)...")
        print("Type abbreviations anywhere and copy them to auto-expand!")
        
        while self.running:
            try:
                current_clipboard = self.get_clipboard_content()
                
                # Check if clipboard content changed and contains an abbreviation
                if (current_clipboard != self.last_clipboard and 
                    current_clipboard and 
                    current_clipboard in EXPANSIONS_DATA):
                    
                    abbreviation = current_clipboard
                    expansion = self.expand_abbreviation(abbreviation)
                    
                    if expansion:
                        print(f"\nDetected abbreviation: {abbreviation}")
                        print(f"Expanding to: {expansion}")
                        
                        # Wait a moment for user to focus on text field
                        print("Please click in a text field within 3 seconds...")
                        time.sleep(3)
                        
                        # Delete the abbreviation and type expansion
                        if self.delete_previous_text(len(abbreviation)):
                            if self.simulate_keyboard_input(expansion):
                                self.log_expansion(abbreviation, expansion, "clipboard")
                                print("✓ Expansion completed successfully!")
                            else:
                                print("✗ Failed to type expansion")
                        else:
                            print("✗ Failed to delete abbreviation")
                
                self.last_clipboard = current_clipboard
                time.sleep(0.5)  # Check every 500ms
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error in clipboard monitoring: {e}")
                time.sleep(1)
    
    def show_status(self):
        """Show current status and recent expansions"""
        print("\n" + "="*50)
        print("EIM Text Expansion Daemon Status (Enhanced)")
        print("="*50)
        print(f"Running: {self.running}")
        print(f"Total expansions: {len(EXPANSIONS_DATA)}")
        print(f"Recent expansions: {len(self.expansion_history)}")
        print(f"Keyboard devices: {len(self.keyboard_devices)}")
        print(f"Current abbreviation: '{self.current_abbreviation}'")
        
        if self.expansion_history:
            print("\nRecent expansions:")
            for entry in self.expansion_history[-10:]:  # Show last 10
                print(f"  {entry}")
        
        print("\nAvailable abbreviation categories:")
        categories = {}
        for abbr in EXPANSIONS_DATA.keys():
            if abbr.startswith('a') or abbr.startswith('A'):
                categories['Text Abbreviations'] = categories.get('Text Abbreviations', 0) + 1
            elif abbr.startswith('la') or abbr.startswith('LA'):
                categories['Legal Phrases'] = categories.get('Legal Phrases', 0) + 1
            elif abbr.startswith('n') or abbr.startswith('t'):
                categories['Word Completions'] = categories.get('Word Completions', 0) + 1
            elif abbr.startswith('US') or abbr.startswith('CA') or abbr.startswith('cc'):
                categories['Geographic'] = categories.get('Geographic', 0) + 1
            elif abbr.startswith('1w'):
                categories['Single Words'] = categories.get('Single Words', 0) + 1
            else:
                categories['Other'] = categories.get('Other', 0) + 1
        
        for category, count in categories.items():
            print(f"  {category}: {count}")
    
    def run(self):
        """Main daemon loop"""
        try:
            # Start keyboard monitoring if available
            if EVDEV_AVAILABLE and self.keyboard_devices:
                keyboard_thread = threading.Thread(target=self.monitor_keyboard_devices, daemon=True)
                keyboard_thread.start()
                print("✓ Keyboard monitoring started")
            else:
                print("⚠ Keyboard monitoring not available")
            
            # Start clipboard monitoring as fallback
            if self.config["clipboard_fallback"]:
                clipboard_thread = threading.Thread(target=self.monitor_clipboard, daemon=True)
                clipboard_thread.start()
                print("✓ Clipboard monitoring started")
            
            # Main loop for status updates and user interaction
            while self.running:
                try:
                    # Show status every 30 seconds
                    time.sleep(30)
                    if self.running:
                        self.show_status()
                        
                except KeyboardInterrupt:
                    break
                    
        except Exception as e:
            print(f"Error in main daemon loop: {e}")
        finally:
            print("\nShutting down EIM enhanced daemon...")
            self.show_status()

def main():
    """Main function"""
    print("EIM AutoKey Enhanced Daemon for Wayland (dotool + evdev)")
    print("=" * 60)
    
    # Check if running in background
    if len(sys.argv) > 1 and sys.argv[1] == '--background':
        print("Starting in background mode...")
        # Redirect output if running in background
        sys.stdout = open('/dev/null', 'w')
        sys.stderr = open('/dev/null', 'w')
    
    daemon = EIMDaemonEnhanced()
    daemon.run()

if __name__ == "__main__":
    main()
