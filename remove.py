# Remove the <br> at the end of each line in the file
# Usage: python remove.py <filename>
# Example: python remove.py test.txt
#
# This script is licensed under GNU GPL version 3 or above
with open("sbsj.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()

with open("sbsj.txt", "w", encoding='utf-8') as f:
    for line in lines:
        if line.strip().endswith("<br>"):
            line = line.strip()[:-4] + "\n"
        f.write(line)