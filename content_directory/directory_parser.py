import subprocess, json

def parse_directory(node, path):
    name = node["name"]

    if node["type"] == "directory":
        path += f"{node['name']}/"
        return f"<br><l>{node['name']}</l><ul>{''.join([parse_directory(x, path) for x in node['contents']])}</ul>"
    else:
        return f"<l><a href='{path + node['name'].replace('.md', '')}'>{name}</a></l><br>"


html = open("content_directory/directory_base.md").read()

html += "<ul>"

file_structure = json.loads(subprocess.run("tree -J", capture_output = True, shell = True).stdout)

# print(list(filter(lambda x: x["name"] == "math" or x["name"] == "note", file_structure[0]["contents"])))

for x in filter(lambda x: x["name"] == "math" or x["name"] == "note", file_structure[0]["contents"]):
    html += parse_directory(x, "/")

html += "</ul>"

with open("_pages/notes.md", "w") as directory_index:
    directory_index.write(html)