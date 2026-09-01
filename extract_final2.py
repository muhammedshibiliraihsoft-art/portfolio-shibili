with open("candidate_content.txt", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "Value @'\n"
end_marker = "\n'\n\nTask logs"
start_idx = content.find(start_marker)
end_idx = content.rfind(end_marker)

if start_idx != -1 and end_idx != -1:
    page_content = content[start_idx + len(start_marker):end_idx]
    with open("src/app/page.tsx", "w", encoding="utf-8") as outf:
        outf.write(page_content)
    print("Page restored!")
else:
    print("Still no")
