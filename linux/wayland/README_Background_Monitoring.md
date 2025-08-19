# EIM Text Expansion - Background Monitoring

This guide explains how to set up EIM text expansion to run continuously in the background, automatically expanding abbreviations as you type them.

## 🎯 **What is Background Monitoring?**

Instead of manually running the script each time you want to expand text, the background daemon continuously monitors your system for abbreviations and automatically expands them when detected.

## 🚀 **Quick Start**

### **1. Start the Daemon**
```bash
# Navigate to the linux folder
cd linux

# Start the daemon in the background
./start_eim_daemon_enhanced.sh start
```

### **2. Use Text Expansion**
- **Enhanced Mode**: Type any abbreviation anywhere (e.g., `aomg`, `lainre`, `USca`) and press **Space** or **Enter** to expand
- **Basic Mode**: Type abbreviations, copy them (Ctrl+C), then click where you want expansion
- No need to run commands manually!

### **3. Stop the Daemon**
```bash
./start_eim_daemon_enhanced.sh stop
```

## 📁 **Files Overview**

| File | Purpose |
|------|---------|
| `EIM_autokey_dotool_daemon.py` | Basic background monitoring (clipboard only) |
| `EIM_autokey_dotool_daemon_evdev.py` | **Enhanced monitoring with direct keyboard input** |
| `start_eim_daemon_enhanced.sh` | **Enhanced startup script with auto-detection** |
| `eim_config.json` | **Configuration file for customizing behavior** |
| `scan_keyboard_devices.py` | **Utility to scan and configure keyboard devices** |
| `eim-text-expansion.service` | Systemd service file (optional) |

## 🔧 **Installation & Setup**

### **Prerequisites**
```bash
# Install dotool
sudo apt install dotool  # Ubuntu/Debian
sudo dnf install dotool  # Fedora
sudo pacman -S dotool    # Arch

# Install clipboard tools
sudo apt install wl-clipboard xclip  # Ubuntu/Debian
sudo dnf install wl-clipboard xclip  # Fedora
sudo pacman -S wl-clipboard xclip    # Arch

# Install evdev for enhanced keyboard monitoring (optional but recommended)
pip3 install evdev
```

### **Basic Setup**
1. **Copy files** to your system
2. **Make startup script executable**: `chmod +x start_eim_daemon_enhanced.sh`
3. **Start daemon**: `./start_eim_daemon_enhanced.sh start`

### **Enhanced Setup (Recommended)**
1. **Install evdev**: `./start_eim_daemon_enhanced.sh install-evdev`
2. **Scan devices**: `./start_eim_daemon_enhanced.sh scan`
3. **Start enhanced daemon**: `./start_eim_daemon_enhanced.sh start`

## 🎮 **Usage Methods**

### **Method 1: Direct Keyboard Monitoring (Enhanced)**
The enhanced daemon monitors keyboard input directly:

1. **Type an abbreviation** anywhere (e.g., `aomg`)
2. **Press Space or Enter** to trigger expansion
3. **The daemon automatically expands it** in place

### **Method 2: Clipboard Monitoring (Fallback)**
The daemon monitors your clipboard for abbreviations:

1. **Type an abbreviation** in any text field
2. **Copy it** (Ctrl+C or right-click → Copy)
3. **Click in the target field** where you want the expansion
4. **The daemon automatically expands it**

### **Method 3: Manual Trigger**
You can still use the manual method:
```bash
python3 EIM_autokey_dotool.py aomg
```

## 🛠️ **Management Commands**

### **Start the Daemon**
```bash
./start_eim_daemon_enhanced.sh start
```

### **Check Status**
```bash
./start_eim_daemon_enhanced.sh status
```

### **Stop the Daemon**
```bash
./start_eim_daemon_enhanced.sh stop
```

### **Restart the Daemon**
```bash
./start_eim_daemon_enhanced.sh restart
```

### **Scan Keyboard Devices**
```bash
./start_eim_daemon_enhanced.sh scan
```

### **Show Configuration**
```bash
./start_eim_daemon_enhanced.sh config
```

### **Install Enhanced Monitoring**
```bash
./start_eim_daemon_enhanced.sh install-evdev
```

## 🔍 **Enhanced Keyboard Monitoring**

### **How It Works**
The enhanced daemon uses `evdev` to monitor keyboard input directly:

1. **Device Detection**: Automatically finds and monitors keyboard devices
2. **Real-time Input**: Captures keystrokes as you type
3. **Smart Triggers**: Expands abbreviations when you press Space or Enter
4. **Buffer Management**: Maintains abbreviation buffer with timeout

### **Configuration Options**
Edit `eim_config.json` to customize behavior:

```json
{
  "keyboard_devices": [],
  "auto_detect_keyboards": true,
  "key_timeout": 2.0,
  "buffer_size": 20,
  "clipboard_fallback": true,
  "expansion_triggers": {
    "space_key": true,
    "enter_key": true,
    "tab_key": false
  }
}
```

### **Device Management**
- **Auto-detection**: Automatically finds all keyboard devices
- **Manual configuration**: Specify specific devices in config
- **Permission handling**: Guides you through device access setup

## 🔄 **Auto-Start Options**

### **Option 1: Session Startup (Recommended)**
Add to your desktop environment's startup applications:

1. **GNOME**: Settings → Applications → Startup Applications
2. **KDE**: System Settings → Startup and Shutdown → Autostart
3. **XFCE**: Settings → Session and Startup → Application Autostart

**Command to add:**
```bash
/path/to/linux/start_eim_daemon_enhanced.sh start
```

### **Option 2: Systemd User Service**
1. **Edit the service file**:
   ```bash
   # Copy service file to user directory
   cp eim-text-expansion.service ~/.config/systemd/user/
   
   # Edit the ExecStart path
   nano ~/.config/systemd/user/eim-text-expansion.service
   ```

2. **Enable and start**:
   ```bash
   systemctl --user enable eim-text-expansion.service
   systemctl --user start eim-text-expansion.service
   ```

### **Option 3: Shell Profile**
Add to `~/.bashrc` or `~/.profile`:
```bash
# Start EIM daemon if not already running
if ! pgrep -f "EIM_autokey_dotool_daemon" > /dev/null; then
    /path/to/linux/start_eim_daemon_enhanced.sh start > /dev/null 2>&1 &
fi
```

## 📊 **Monitoring & Logs**

### **View Daemon Status**
```bash
./start_eim_daemon_enhanced.sh status
```

### **View Recent Expansions**
The daemon shows expansion history every 30 seconds when running in foreground.

### **Check System Logs**
```bash
# If using systemd service
journalctl --user -u eim-text-expansion.service -f

# View process output
ps aux | grep 'EIM_autokey_dotool_daemon'
```

## 🔍 **Troubleshooting**

### **Daemon Won't Start**
```bash
# Check prerequisites
./start_eim_daemon_enhanced.sh status

# Check script permissions
ls -la start_eim_daemon_enhanced.sh
chmod +x start_eim_daemon_enhanced.sh

# Run manually to see errors
python3 EIM_autokey_dotool_daemon_evdev.py
```

### **Enhanced Monitoring Not Working**
```bash
# Check evdev installation
./start_eim_daemon_enhanced.sh install-evdev

# Scan for keyboard devices
./start_eim_daemon_enhanced.sh scan

# Check device permissions
sudo usermod -a -G input $USER
# Log out and back in
```

### **Expansions Not Working**
```bash
# Check if daemon is running
./start_eim_daemon_enhanced.sh status

# Check clipboard tools
wl-clipboard read
xclip -o -selection clipboard

# Restart daemon
./start_eim_daemon_enhanced.sh restart
```

### **Permission Issues**
```bash
# Make sure script is executable
chmod +x start_eim_daemon_enhanced.sh

# Check file ownership
ls -la *.py *.sh

# Add user to input group
sudo usermod -a -G input $USER
```

## ⚡ **Performance & Resources**

### **Resource Usage**
- **CPU**: Minimal (keyboard events or clipboard checks every 500ms)
- **Memory**: ~10-20 MB
- **Disk**: Minimal logging

### **Optimization Tips**
- **Use enhanced mode** for better performance and user experience
- **Configure specific devices** instead of auto-detection if needed
- **Adjust timeout values** in configuration
- **Use systemd service** for better process management

## 🔒 **Security Considerations**

### **What the Daemon Can Do**
- **Read keyboard input** (for abbreviation detection)
- **Read clipboard content** (for fallback method)
- **Simulate keyboard input** (for text expansion)
- **Access filesystem** (for logging and data)

### **Security Best Practices**
- **Run as your user** (not root)
- **Use systemd service** for better isolation
- **Monitor logs** for unexpected activity
- **Keep scripts updated** and from trusted sources
- **Review device permissions** regularly

## 🌟 **Advanced Features**

### **Smart Abbreviation Detection**
- **Real-time input monitoring** with evdev
- **Configurable triggers** (Space, Enter, Tab)
- **Timeout-based reset** for incomplete abbreviations
- **Buffer management** for complex input sequences

### **Device Management**
- **Automatic device detection** and categorization
- **Permission handling** and troubleshooting
- **Device-specific configuration** options
- **Fallback to clipboard** if keyboard monitoring fails

### **Configuration Management**
- **JSON-based configuration** with defaults
- **Runtime configuration** updates
- **Device auto-discovery** and persistence
- **Performance tuning** options

### **Custom Expansion History**
The daemon maintains a history of recent expansions (last 100).

### **Category Statistics**
Shows counts of different expansion types:
- Text Abbreviations
- Legal Phrases
- Word Completions
- Geographic Data
- Single Words

### **Graceful Shutdown**
Handles Ctrl+C and system signals properly.

## 📚 **Examples**

### **Typical Workflow (Enhanced)**
1. **Start daemon**: `./start_eim_daemon_enhanced.sh start`
2. **Type abbreviation**: `aomg` anywhere
3. **Press Space**: Triggers expansion
4. **Auto-expansion**: `aomg` becomes "oh my god"

### **Typical Workflow (Basic)**
1. **Start daemon**: `./start_eim_daemon_enhanced.sh start`
2. **Type abbreviation**: `aomg` in any text field
3. **Copy abbreviation**: Ctrl+C
4. **Click target field**: Where you want the expansion
5. **Auto-expansion**: `aomg` becomes "oh my god"

### **Common Abbreviations**
- `aomg` → "oh my god"
- `lainre` → "in reference to the matter of"
- `USca` → "California"
- `ncondi` → "condition"

## 🔮 **Future Enhancements**

### **Planned Features**
- [x] **Direct keyboard monitoring** with evdev
- [x] **Device auto-detection** and configuration
- [x] **Smart trigger keys** (Space, Enter, Tab)
- [x] **Configuration management** with JSON
- [ ] **Custom trigger keys** (e.g., Ctrl+Space)
- [ ] **Expansion statistics** (usage analytics)
- [ ] **Application-specific** expansion rules
- [ ] **Multi-language support**

### **Contributing**
- Report issues with background monitoring
- Suggest performance improvements
- Test on different Wayland compositors
- Help with device compatibility

---

*Enhanced background monitoring provides a seamless text expansion experience similar to AutoHotkey on Windows, with direct keyboard input monitoring and full Wayland compatibility!*
