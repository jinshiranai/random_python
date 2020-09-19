import re

# Load entire text of Alice in Wonderland.
filename = 'data/alice.txt'
with open(filename) as f:
    contents = f.read()

# Extract every sentence that begins with "The".
pulled_lines = re.findall("(The\s.*[.!?']\s?)", contents)

for line in pulled_lines:
    print(line.rstrip())