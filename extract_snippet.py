import json

with open("found_snippet.json", "r", encoding="utf-8") as f:
    data = json.load(f)

content = data.get("content", "")
if "tool_calls" in data:
    for tc in data["tool_calls"]:
        print(tc)
else:
    print(content[:500])
