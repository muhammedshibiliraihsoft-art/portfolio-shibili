import json
import codecs

lines = []
with codecs.open(r"C:\Users\Admin\.gemini\antigravity\brain\10c3d803-d670-4bee-b2fa-3981e6b09cfc\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line)

for i in range(710, 730):
    try:
        data = json.loads(lines[i])
        if "tool_calls" not in data and "Festival Manager" in data.get("content", ""):
            print(f"Line {i} is a hit!")
            with open("candidate_content.txt", "w", encoding="utf-8") as outf:
                outf.write(data["content"])
    except:
        pass
