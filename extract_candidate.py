import json
import codecs

lines = []
with codecs.open(r"C:\Users\Admin\.gemini\antigravity\brain\10c3d803-d670-4bee-b2fa-3981e6b09cfc\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line)

data = json.loads(lines[722])
content = data.get("content", "")
if "tool_calls" in data:
    print("It's a tool call")
else:
    print(content[:500])
    with open("candidate_content.txt", "w", encoding="utf-8") as outf:
        outf.write(content)
