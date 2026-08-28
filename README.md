# WINDOWS-MONITOR FOR Productivity 
A simple Python productivity tracker for Windows designed to help reduce distractions while working.

The program runs in the background and regularly checks the user's active window. If the window title contains a distracting keyword, such as Instagram, Netflix, TikTok, or Food, a warning message is displayed, telling you to get back to work.

It also tracks how long the computer has been inactive. If there has been no keyboard or mouse input for more than 5 minutes, the program displays an inactivity warning.

Getting Started:
Requirements
Windows 10 or 11
Python 3.x

Installation:
Clone the repository and install the required package:

git clone https://github.com/yourusername/productivity-tracker.git
cd productivity-tracker
pip install pywin32

Running the Program
Start the tracker with:

python productivity_tracker.py

Once running, it will automatically monitor the active window and user activity, checking every 50 seconds.

To stop the tracker, press Ctrl+C in the terminal.

Configuration
The list of distracting websites/applications and the inactivity time can be changed in the program's configuration. By default, the inactivity limit is 5 minutes.

License
This project was created for educational purposes.
