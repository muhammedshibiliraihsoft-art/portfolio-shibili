import json

with open("diff_output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# The diff is inside the JSON log output for that command.
# We'll just read the transcript directly.
with open(r"C:\Users\Admin\.gemini\antigravity\brain\10c3d803-d670-4bee-b2fa-3981e6b09cfc\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if "git diff HEAD src/app/page.tsx" in line and "diff --git" in line:
            data = json.loads(line)
            content = data.get("content", "")
            if "diff --git" in content:
                # Extract the + lines from the diff
                new_file_lines = []
                for cl in content.split("\n"):
                    if cl.startswith("+") and not cl.startswith("+++"):
                        new_file_lines.append(cl[1:])
                    elif cl.startswith(" ") and not cl.startswith(" +"):
                        new_file_lines.append(cl[1:])
                
                with open("src/app/page.tsx", "w", encoding="utf-8") as outf:
                    outf.write("\n".join(new_file_lines))
                print("Recovered!")
                break
