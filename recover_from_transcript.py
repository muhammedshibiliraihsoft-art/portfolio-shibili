import json
import codecs

lines = []
with codecs.open(r"C:\Users\Admin\.gemini\antigravity\brain\10c3d803-d670-4bee-b2fa-3981e6b09cfc\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line)

found = []
# Search backward
for i in range(len(lines)-1, -1, -1):
    if "Festival Manager" in lines[i] and "export default function" in lines[i]:
        found.append(i)

if found:
    print(f"Found in lines {found}")
    with open("found_snippet.json", "w", encoding="utf-8") as outf:
        outf.write(lines[found[-1]]) # write the earliest one or latest? Let's just write the last found (which is the earliest in the file since we search backwards)
else:
    print("Not found in same line. Looking for any output that has the full file...")
    for i in range(len(lines)-1, -1, -1):
        if "Festival Manager" in lines[i] and "flex items-center justify-center" in lines[i]:
            print(f"Found candidate in line {i}")
            with open("found_snippet.json", "w", encoding="utf-8") as outf:
                outf.write(lines[i])
            break
