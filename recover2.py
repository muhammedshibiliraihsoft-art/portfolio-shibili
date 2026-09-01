import json
import codecs

with codecs.open(r"C:\Users\Admin\.gemini\antigravity\brain\10c3d803-d670-4bee-b2fa-3981e6b09cfc\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if "git diff HEAD src/app/page.tsx" in line and "diff --git" in line:
            data = json.loads(line)
            content = data.get("content", "")
            if "diff --git" in content:
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
                print("Recovered!")
                break
