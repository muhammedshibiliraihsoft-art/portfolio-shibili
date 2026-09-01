import json
import codecs

recovered = False
with codecs.open(r"C:\Users\Admin\.gemini\antigravity\brain\10c3d803-d670-4bee-b2fa-3981e6b09cfc\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            # Check tool output
            if "tool_calls" in data:
                continue
            if data.get("type") == "TOOL_RESPONSE" or data.get("source") == "SYSTEM":
                content = data.get("content", "")
                if "diff --git a/src/app/page.tsx b/src/app/page.tsx" in content:
                    diff_lines = content.split("\n")
                    new_file_lines = []
                    started = False
                    for cl in diff_lines:
                        if cl.startswith("@@"):
                            started = True
                            continue
                        if started:
                            if cl.startswith("+"):
                                new_file_lines.append(cl[1:])
                            elif cl.startswith(" "):
                                new_file_lines.append(cl[1:])
                    
                    with open("src/app/page.tsx", "w", encoding="utf-8") as outf:
                        outf.write("\n".join(new_file_lines))
                    print("Recovered from tool response!")
                    recovered = True
        except Exception as e:
            pass
