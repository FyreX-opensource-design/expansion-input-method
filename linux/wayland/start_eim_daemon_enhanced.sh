#!/bin/bash
# EIM Text Expansion Daemon Enhanced Startup Script

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASIC_DAEMON="$SCRIPT_DIR/EIM_autokey_dotool_daemon.py"
ENHANCED_DAEMON="$SCRIPT_DIR/EIM_autokey_dotool_daemon_evdev.py"
CONFIG_FILE="$SCRIPT_DIR/eim_config.json"
DEVICE_SCANNER="$SCRIPT_DIR/scan_keyboard_devices.py"

echo -e "${BLUE}EIM Text Expansion Daemon Enhanced${NC}"
echo "=========================================="

# Function to check prerequisites
check_prerequisites() {
    local missing_deps=()
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        missing_deps+=("python3")
    fi
    
    # Check dotool
    if ! command -v dotool &> /dev/null; then
        missing_deps+=("dotool")
    fi
    
    # Check evdev (optional)
    if ! python3 -c "import evdev" 2>/dev/null; then
        echo -e "${YELLOW}Warning: evdev not available. Install with: pip3 install evdev${NC}"
        echo "Enhanced keyboard monitoring will not be available."
        EVDEV_AVAILABLE=false
    else
        EVDEV_AVAILABLE=true
    fi
    
    # Check clipboard tools
    if ! command -v wl-clipboard &> /dev/null && ! command -v xclip &> /dev/null; then
        missing_deps+=("wl-clipboard or xclip")
    fi
    
    if [ ${#missing_deps[@]} -gt 0 ]; then
        echo -e "${RED}Missing dependencies:${NC}"
        for dep in "${missing_deps[@]}"; do
            echo "  - $dep"
        done
        echo ""
        echo "Install with:"
        echo "  sudo apt install dotool wl-clipboard xclip  # Ubuntu/Debian"
        echo "  sudo dnf install dotool wl-clipboard xclip  # Fedora"
        echo "  sudo pacman -S dotool wl-clipboard xclip    # Arch"
        echo ""
        echo "For evdev (enhanced keyboard monitoring):"
        echo "  pip3 install evdev"
        return 1
    fi
    
    return 0
}

# Function to scan keyboard devices
scan_devices() {
    if [ "$EVDEV_AVAILABLE" = true ] && [ -f "$DEVICE_SCANNER" ]; then
        echo -e "${CYAN}Scanning keyboard devices...${NC}"
        python3 "$DEVICE_SCANNER"
        echo ""
    else
        echo -e "${YELLOW}Device scanner not available${NC}"
    fi
}

# Function to check which daemon to use
select_daemon() {
    if [ "$EVDEV_AVAILABLE" = true ] && [ -f "$ENHANCED_DAEMON" ]; then
        DAEMON_SCRIPT="$ENHANCED_DAEMON"
        DAEMON_TYPE="enhanced (evdev)"
        echo -e "${GREEN}Using enhanced daemon with keyboard monitoring${NC}"
    elif [ -f "$BASIC_DAEMON" ]; then
        DAEMON_SCRIPT="$BASIC_DAEMON"
        DAEMON_TYPE="basic (clipboard only)"
        echo -e "${YELLOW}Using basic daemon (clipboard monitoring only)${NC}"
    else
        echo -e "${RED}Error: No daemon scripts found${NC}"
        exit 1
    fi
}

# Function to check if already running
check_running() {
    if pgrep -f "EIM_autokey_dotool_daemon" > /dev/null; then
        echo -e "${YELLOW}EIM daemon is already running${NC}"
        echo "Process ID: $(pgrep -f 'EIM_autokey_dotool_daemon')"
        echo ""
        echo "To stop the daemon:"
        echo "  $0 stop"
        echo ""
        echo "To restart:"
        echo "  $0 restart"
        return 0
    fi
    return 1
}

# Function to start daemon
start_daemon() {
    echo -e "${GREEN}Starting EIM Text Expansion Daemon ($DAEMON_TYPE)...${NC}"
    
    # Start in background
    nohup python3 "$DAEMON_SCRIPT" --background > /dev/null 2>&1 &
    DAEMON_PID=$!
    
    # Wait a moment to see if it starts successfully
    sleep 2
    
    if kill -0 $DAEMON_PID 2>/dev/null; then
        echo -e "${GREEN}✓ Daemon started successfully!${NC}"
        echo "Process ID: $DAEMON_PID"
        echo ""
        if [ "$DAEMON_TYPE" = "enhanced (evdev)" ]; then
            echo "The enhanced daemon is now monitoring keyboard input directly."
            echo "Type abbreviations and press Space/Enter to expand them!"
        else
            echo "The basic daemon is monitoring clipboard for abbreviations."
            echo "Type abbreviations, copy them, then click where you want expansion!"
        fi
        echo ""
        echo "To stop the daemon:"
        echo "  $0 stop"
        echo ""
        echo "To check status:"
        echo "  $0 status"
    else
        echo -e "${RED}✗ Failed to start daemon${NC}"
        exit 1
    fi
}

# Function to stop daemon
stop_daemon() {
    echo -e "${YELLOW}Stopping EIM Text Expansion Daemon...${NC}"
    
    if pkill -f "EIM_autokey_dotool_daemon"; then
        echo -e "${GREEN}✓ Daemon stopped successfully${NC}"
    else
        echo -e "${RED}✗ No daemon found running${NC}"
    fi
}

# Function to show status
show_status() {
    echo -e "${BLUE}EIM Text Expansion Daemon Status${NC}"
    echo "====================================="
    
    if pgrep -f "EIM_autokey_dotool_daemon" > /dev/null; then
        echo -e "${GREEN}✓ Daemon is running${NC}"
        echo "Process ID: $(pgrep -f 'EIM_autokey_dotool_daemon')"
        echo "Uptime: $(ps -o etime= -p $(pgrep -f 'EIM_autokey_dotool_daemon'))"
        
        # Check which type is running
        if pgrep -f "EIM_autokey_dotool_daemon_evdev" > /dev/null; then
            echo "Type: Enhanced (evdev keyboard monitoring)"
        else
            echo "Type: Basic (clipboard monitoring)"
        fi
    else
        echo -e "${RED}✗ Daemon is not running${NC}"
    fi
    
    echo ""
    echo "Available commands:"
    echo "  $0 start    - Start the daemon"
    echo "  $0 stop     - Stop the daemon"
    echo "  $0 restart  - Restart the daemon"
    echo "  $0 status   - Show current status"
    echo "  $0 scan     - Scan keyboard devices"
    echo "  $0 config   - Show configuration"
}

# Function to show configuration
show_config() {
    echo -e "${BLUE}EIM Configuration${NC}"
    echo "===================="
    
    if [ -f "$CONFIG_FILE" ]; then
        echo "Configuration file: $CONFIG_FILE"
        echo ""
        echo "Current settings:"
        python3 -m json.tool "$CONFIG_FILE" 2>/dev/null || cat "$CONFIG_FILE"
    else
        echo "No configuration file found"
        echo "Create one by running the enhanced daemon once"
    fi
}

# Function to install evdev
install_evdev() {
    echo -e "${CYAN}Installing evdev for enhanced keyboard monitoring...${NC}"
    
    if command -v pip3 &> /dev/null; then
        echo "Installing with pip3..."
        pip3 install evdev
    elif command -v pip &> /dev/null; then
        echo "Installing with pip..."
        pip install evdev
    else
        echo -e "${RED}Error: pip not available${NC}"
        echo "Install pip first, then run: pip3 install evdev"
        return 1
    fi
    
    if python3 -c "import evdev" 2>/dev/null; then
        echo -e "${GREEN}✓ evdev installed successfully${NC}"
        echo "Enhanced keyboard monitoring is now available!"
    else
        echo -e "${RED}✗ Failed to install evdev${NC}"
        return 1
    fi
}

# Main script logic
main() {
    # Check prerequisites first
    if ! check_prerequisites; then
        exit 1
    fi
    
    # Select appropriate daemon
    select_daemon
    
    # Parse command line arguments
    case "${1:-start}" in
        start)
            if check_running; then
                exit 0
            fi
            start_daemon
            ;;
        stop)
            stop_daemon
            ;;
        restart)
            stop_daemon
            sleep 1
            start_daemon
            ;;
        status)
            show_status
            ;;
        scan)
            scan_devices
            ;;
        config)
            show_config
            ;;
        install-evdev)
            install_evdev
            ;;
        *)
            echo "Usage: $0 {start|stop|restart|status|scan|config|install-evdev}"
            echo ""
            echo "Commands:"
            echo "  start         - Start the EIM text expansion daemon"
            echo "  stop          - Stop the daemon"
            echo "  restart       - Restart the daemon"
            echo "  status        - Check if running and show status"
            echo "  scan          - Scan available keyboard devices"
            echo "  config        - Show current configuration"
            echo "  install-evdev - Install evdev for enhanced monitoring"
            echo ""
            echo "Examples:"
            echo "  $0 start      # Start the daemon"
            echo "  $0 stop       # Stop the daemon"
            echo "  $0 scan       # Scan keyboard devices"
            echo "  $0 install-evdev  # Install enhanced monitoring"
            exit 1
            ;;
    esac
}

# Run main function
main "$@"
