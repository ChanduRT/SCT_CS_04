# Read data from keylogger.txt
with open('keylog.txt', 'r') as keylog_file:
    keylog_data = keylog_file.read()

# Process the data
lines = keylog_data.split('\n')
word_data = []
for line in lines:
    if line.strip():  # Skip empty lines
        timestamp, word = line.split(' - ', 1)
        word_data.append((timestamp, word))

# Create a new text file (e.g., raw_data.txt)
with open('raw_data.txt', 'w') as raw_file:
    for timestamp, word in word_data:
        raw_file.write(f'{timestamp} - {word}\n')

print("Raw data saved to raw_data.txt")
