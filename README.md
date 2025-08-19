# EIM Text Expansion System

A comprehensive text expansion system that works across Windows (AutoHotkey) and Linux (AutoKey + Wayland solutions).

## 📁 **Project Structure**

```
AutoHotkey/
├── README.md                           # This file - project overview
├── EIM.ahk                            # Windows AutoHotkey script
├── EIM_expansions_data.py             # Shared expansion data
├── README_Expansion_Types.md          # Complete expansion type guide
├── README_Region_Abbreviations.md     # Geographic abbreviations guide
└── linux/                             # Linux solutions
    ├── README.md                      # Linux overview and X11 solutions
    ├── EIM_autokey_corrected.py      # AutoKey script for X11
    ├── README_AutoKey.md              # AutoKey setup guide
    └── wayland/                       # Wayland-specific solutions
        ├── README.md                  # Wayland overview
        ├── EIM_autokey_dotool_daemon_evdev.py  # Enhanced daemon
        ├── start_eim_daemon_enhanced.sh         # Startup script
        └── README_Background_Monitoring.md      # Complete guide
```

## 🚀 **Quick Start**

### **Windows Users**
1. Install [AutoHotkey](https://www.autohotkey.com/)
2. Run `EIM.ahk`
3. Type abbreviations anywhere - they expand automatically!

### **Linux Users**
- **X11 (GNOME, KDE, XFCE)**: See `linux/README_AutoKey.md`
- **Wayland (Modern Linux)**: See `linux/wayland/README_Background_Monitoring.md`

## 🎯 **What is EIM?**

EIM (Enhanced Input Method) is a text expansion system that automatically converts abbreviations into full phrases, legal text, geographic locations, and more. It's designed to work seamlessly across different platforms and display servers.

## 🌟 **Key Features**

- **800+ Built-in Expansions** - Text, legal, geographic, word completions
- **Cross-Platform** - Windows, Linux X11, Linux Wayland
- **Smart Abbreviations** - Prefix-based system for easy memorization
- **Background Operation** - Always running, always ready (Linux Wayland)
- **Professional Quality** - Production-ready with error handling

## 📚 **Documentation**

- **[README_Expansion_Types.md](README_Expansion_Types.md)** - Complete guide to all expansion types and patterns
- **[README_Region_Abbreviations.md](README_Region_Abbreviations.md)** - Geographic abbreviations and conflict resolution
- **[linux/README.md](linux/README.md)** - Linux solutions overview
- **[linux/wayland/README_Background_Monitoring.md](linux/wayland/README_Background_Monitoring.md)** - Wayland background monitoring

## 🔤 **Expansion Types**

### **Text Abbreviations** (`a`/`A` prefix)
- `aomg` → "oh my god"
- `Aomg` → "Oh my god"

### **Legal Phrases** (`la`/`LA` prefix)
- `lainre` → "in reference to the matter of"
- `LAinre` → "In reference to the matter of"

### **Word Completions** (`n`/`t` prefix)
- `ncondi` → "condition"
- `tdefen` → "defensive"

### **Geographic** (`US`, `CA`, `cc`, `ID` prefixes)
- `USca` → "California"
- `ccus` → "United States"

### **Single Words** (`1w` prefix)
- `1wdh` → "downhill"

## 🛠️ **Data Management**

All expansions are stored in `EIM_expansions_data.py` and shared across platforms. To add custom expansions:

1. **Edit** `EIM_expansions_data.py`
2. **Add entries** to `EXPANSIONS_DATA` dictionary
3. **Restart scripts** or reload applications

## 🔄 **Platform Migration**

### **Windows to Linux**
- **X11**: Use AutoKey with `linux/EIM_autokey_corrected.py`
- **Wayland**: Use enhanced daemon in `linux/wayland/`

### **Linux to Windows**
- Copy `EIM.ahk` to Windows machine
- Install AutoHotkey
- Run the script

## 🌍 **Supported Platforms**

| Platform | Display Server | Solution | Experience |
|----------|----------------|----------|------------|
| **Windows** | N/A | AutoHotkey | Native, seamless |
| **Linux** | X11 | AutoKey | Full integration |
| **Linux** | Wayland | Enhanced Daemon | **Best experience** |

## 🔧 **Installation**

### **Windows**
```bash
# Download and run EIM.ahk
# Requires AutoHotkey v1.1+
```

### **Linux X11**
```bash
cd linux
# Follow README_AutoKey.md
```

### **Linux Wayland**
```bash
cd linux/wayland
./start_eim_daemon_enhanced.sh install-evdev
./start_eim_daemon_enhanced.sh start
```

## 🚀 **Why Choose EIM?**

- **Professional Quality** - Built for business and productivity use
- **Cross-Platform** - Same abbreviations work everywhere
- **Smart Design** - Prefix system prevents conflicts
- **Active Development** - Regular updates and improvements
- **Community Support** - Clear documentation and troubleshooting

## 🔮 **Future Development**

- **Mobile Support** - Android/iOS text expansion
- **Cloud Sync** - Cross-device abbreviation sharing
- **AI Integration** - Smart abbreviation suggestions
- **Advanced Triggers** - Custom keyboard shortcuts
- **Multi-Language** - International expansion support

## 🤝 **Contributing**

- Report issues with specific platforms
- Suggest new expansion categories
- Test on different Linux distributions
- Improve documentation and examples

---

*EIM provides the most seamless text expansion experience across platforms, with Wayland users getting the closest AutoHotkey-like functionality on Linux!*
