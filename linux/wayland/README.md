# EIM Text Expansion - Wayland Solutions

This folder contains Wayland-specific text expansion solutions that provide the closest experience to AutoHotkey on Windows.

## 🎯 **What's Here**

- **`EIM_autokey_dotool_daemon_evdev.py`** - Enhanced background daemon with direct keyboard monitoring
- **`start_eim_daemon_enhanced.sh`** - Easy startup script with auto-detection
- **`eim_config.json`** - Configuration file for customizing behavior
- **`scan_keyboard_devices.py`** - Utility to scan and configure keyboard devices
- **`eim-text-expansion.service`** - Systemd service file for production use
- **`README_Background_Monitoring.md`** - Complete setup and usage guide

## 🚀 **Quick Start**

```bash
# Install enhanced monitoring
./start_eim_daemon_enhanced.sh install-evdev

# Start the daemon
./start_eim_daemon_enhanced.sh start
```

## 🌟 **Why This Solution?**

- **Direct keyboard monitoring** - No need to copy/paste
- **Background operation** - Always running, always ready
- **Auto-device detection** - Works with any keyboard
- **Fallback support** - Clipboard monitoring if needed
- **Production ready** - Systemd service and configuration

## 📚 **Documentation**

- **`README_Background_Monitoring.md`** - Complete setup guide
- **Main linux README** - Overview of all solutions
- **Root README** - Project overview and expansion types

---

*This is the recommended solution for Wayland users who want AutoHotkey-like functionality!*
