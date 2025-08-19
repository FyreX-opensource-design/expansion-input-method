# EIM Text Expansion - Linux Solutions

This folder contains Linux-compatible text expansion solutions for the EIM system, organized by display server compatibility.

## 📁 **Project Structure**

```
linux/
├── README.md                           # This file - main overview
├── EIM_autokey_corrected.py           # AutoKey script for X11
├── EIM_autokey_simple.py              # Simple AutoKey template
├── create_autokey_scripts.py          # Script generator for AutoKey
├── README_AutoKey.md                  # AutoKey setup guide
└── wayland/                           # Wayland-specific solutions
    ├── EIM_autokey_dotool_daemon_evdev.py  # Enhanced daemon (recommended)
    ├── start_eim_daemon_enhanced.sh         # Enhanced startup script
    ├── eim_config.json                       # Configuration file
    ├── scan_keyboard_devices.py              # Device scanner utility
    ├── eim-text-expansion.service            # Systemd service file
    └── README_Background_Monitoring.md      # Background monitoring guide
```

## 🎯 **Quick Start Guide**

### **For X11 Users (GNOME, KDE, XFCE)**
```bash
cd linux
# Follow README_AutoKey.md for setup
```

### **For Wayland Users (Recommended)**
```bash
cd linux/wayland
# Install enhanced monitoring
./start_eim_daemon_enhanced.sh install-evdev

# Start the daemon
./start_eim_daemon_enhanced.sh start
```

## 🚀 **Recommended Solutions by Use Case**

### **X11 Desktop Environments**
- **File**: `EIM_autokey_corrected.py`
- **Guide**: `README_AutoKey.md`
- **Best for**: Traditional Linux desktops, GNOME on X11

### **Wayland Display Server**
- **File**: `wayland/EIM_autokey_dotool_daemon_evdev.py`
- **Guide**: `wayland/README_Background_Monitoring.md`
- **Best for**: Modern Wayland desktops, GNOME 40+, KDE Plasma 6

## 🔧 **Installation Quick Commands**

### **Ubuntu/Debian**
```bash
sudo apt install dotool wl-clipboard xclip
pip3 install evdev
```

### **Fedora**
```bash
sudo dnf install dotool wl-clipboard xclip
pip3 install evdev
```

### **Arch Linux**
```bash
sudo pacman -S dotool wl-clipboard xclip
pip3 install evdev
```

## 📚 **Documentation**

- **`README_AutoKey.md`** - Complete AutoKey setup for X11
- **`wayland/README_Background_Monitoring.md`** - Enhanced background monitoring for Wayland
- **`README_Expansion_Types.md`** (root) - All expansion types and patterns
- **`README_Region_Abbreviations.md`** (root) - Geographic abbreviations and conflicts

## 🌟 **Key Features**

### **X11 Solutions**
- ✅ **AutoKey integration** with full API support
- ✅ **Phrase triggers** for automatic expansion
- ✅ **Cross-application** compatibility
- ✅ **Professional quality** with error handling

### **Wayland Solutions**
- ✅ **Direct keyboard monitoring** with evdev
- ✅ **Background daemon** for continuous operation
- ✅ **Auto-device detection** and configuration
- ✅ **Clipboard fallback** for compatibility
- ✅ **Systemd service** for production use

## 🔄 **Migration Path**

### **From X11 to Wayland**
1. **Keep existing** AutoKey setup for X11
2. **Add Wayland solution** in `wayland/` folder
3. **Use enhanced daemon** for better performance
4. **Maintain both** for hybrid environments

### **From Windows AutoHotkey**
1. **Use Wayland solution** for closest experience
2. **Background monitoring** matches AHK behavior
3. **Direct keyboard input** for seamless expansion
4. **Same abbreviations** work across platforms

## 🛠️ **Development & Customization**

### **Adding Custom Expansions**
- **X11**: Edit `EIM_expansions_data.py` and restart AutoKey
- **Wayland**: Edit `wayland/eim_config.json` and restart daemon

### **Script Generation**
```bash
cd linux
python3 create_autokey_scripts.py
```

### **Configuration**
- **X11**: AutoKey preferences and phrase triggers
- **Wayland**: JSON configuration with runtime updates

## 🔍 **Troubleshooting**

### **Common Issues**
- **Permissions**: Add user to `input` group for Wayland
- **Dependencies**: Install required packages (see above)
- **Device access**: Use `wayland/scan_keyboard_devices.py`

### **Getting Help**
- Check relevant README files
- Run diagnostic commands in startup scripts
- Verify display server compatibility

## 📊 **Performance Comparison**

| Feature | X11 (AutoKey) | Wayland (Enhanced) |
|---------|---------------|-------------------|
| **Setup Complexity** | Medium | Low |
| **Performance** | Good | Excellent |
| **Resource Usage** | Low | Very Low |
| **User Experience** | Good | Excellent |
| **Compatibility** | X11 Only | Wayland + Fallback |

## 🔮 **Future Development**

- **Enhanced X11 support** with additional features
- **Wayland improvements** for better device management
- **Cross-platform compatibility** improvements
- **Performance optimizations** for all solutions

---

*Choose the solution that best fits your display server and requirements. Wayland users get the most AutoHotkey-like experience with background monitoring!*
