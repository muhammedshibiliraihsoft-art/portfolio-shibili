with open("diff_clean.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_file_lines = []
started = False
for line in lines:
    line = line.rstrip("\n")
    if line.startswith("@@"):
        started = True
        continue
    if started:
        if line.startswith("+"):
            new_file_lines.append(line[1:])
        elif line.startswith(" ") and not line.startswith(" +"):
            new_file_lines.append(line[1:])

if new_file_lines:
    with open("src/app/page.tsx", "w", encoding="utf-8") as outf:
        outf.write("\n".join(new_file_lines))
    print("Recovered!")
else:
    print("Not found.")
