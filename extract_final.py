with open("candidate_content.txt", "r", encoding="utf-8") as f:
    content = f.read()

# The content is a Task output that shows the Set-Content command.
# It looks like:
# Task Description: Set-Content -Path src/app/page.tsx -Value @'
# "use client";
# ...
# '@

start_idx = content.find("@'\n")
end_idx = content.rfind("\n'@")

if start_idx != -1 and end_idx != -1:
    page_content = content[start_idx+3:end_idx]
    with open("src/app/page.tsx", "w", encoding="utf-8") as outf:
        outf.write(page_content)
    print("Page restored to previous version!")
else:
    print("Could not find boundaries")
