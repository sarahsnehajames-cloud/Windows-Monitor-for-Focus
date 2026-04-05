import time
import ctypes
from ctypes import wintypes
import win32gui

# Configuration
INACTIVE_THRESHOLD = 300  # seconds (5 minutes)
FORBIDDEN_KEYWORDS = [ 'Instagram', 'Netflix', 'TikTok','Food']

# Global variables
work_mode = True  # Set to True to enable monitoring

# Windows API setup for input tracking
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', wintypes.UINT),
        ('dwTime', wintypes.DWORD),
    ]

def get_idle_time():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    user32.GetLastInputInfo(ctypes.byref(lii))
    current = kernel32.GetTickCount()
    return (current - lii.dwTime) / 1000.0  # in seconds

def get_active_window_title():
    hwnd = user32.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd)

def send_notification(message):
    user32.MessageBoxW(0, message, "Productivity Tracker", 0x40)  # MB_ICONINFORMATION

# Main monitoring loop
print("Productivity tracker started in work mode.")
print("Press Ctrl+C to exit.")

try:
    while True:
        if work_mode:
            title = get_active_window_title()
            if any(kw.lower() in title.lower() for kw in FORBIDDEN_KEYWORDS):
                send_notification("Warning: Get off this website!")

            idle = get_idle_time()
            if idle > INACTIVE_THRESHOLD:
                send_notification("Warning: Computer inactive for too long!")

        time.sleep(50)  # Check every 50 seconds
except KeyboardInterrupt:
    print("Exiting...")