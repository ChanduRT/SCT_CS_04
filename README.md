Keylogger Script
This keylogger script captures words typed on the keyboard along with their timestamps. It logs each word with the start and end time in a file named wordlog.txt.

Features
Records each word typed along with the start and end times.
Logs the words to a file with a timestamp.
Pause and resume logging with specific key combinations.
Stop logging with the Esc key.
Requirements
Python 3.x
pynput library
Installation
Ensure you have Python 3.x installed on your system.
Install the pynput library using pip:
bash
Copy code
pip install pynput
Save the script to a file, e.g., keylogger.py.
Usage
Run the script using the command:
bash
Copy code
python keylogger.py
The script will start logging words typed on the keyboard.
Controls
Pause logging: Press Shift key.
Resume logging: Press Alt key.
Stop logging: Press Esc key.
Output
The log will be saved in a file named wordlog.txt in the same directory as the script. Each session will be separated by --- New session ---.

Example Log Entry
less
Copy code
2024-07-05 10:30:45 - example (Start: 0.00s, End: 1.23s)
2024-07-05 10:30:46 - word (Start: 1.24s, End: 2.34s)
Notes
Ensure you have the necessary permissions to create and write to the wordlog.txt file in the script's directory.
Use this script responsibly and ensure you comply with privacy and legal considerations when using a keylogger.
Disclaimer
This script is provided for educational purposes only. The author is not responsible for any misuse of this script.

