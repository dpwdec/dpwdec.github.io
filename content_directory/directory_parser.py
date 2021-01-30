# script that recursively parses JSON folder structure into an static HTML page
import subprocess, json

# lambda to match only required sub directories
def match_directory(name: str) -> bool:
    return name in {'math', 'note'}

def parse_directory(node: dict, path: str) -> str:
    name = node["name"]

    if node["type"] == "directory":
        path += f"{node['name']}/"
        return f"<br><l>{node['name'].capitalize()}</l><ul>{''.join([parse_directory(x, path) for x in node['contents']])}</ul>"
    else:
        page_title = subprocess\
            .run(f"cat {path.replace('/', '', 1) + node['name']} | grep title: | head | sed 's/title: //'", capture_output=True, shell=True)\
            .stdout\
            .decode('utf-8')
        return f"<l><a href='{path + node['name'].replace('.md', '')}'>{page_title}</a></l><br>"

# generate file structure JSON using tree command
file_structure = json.loads(subprocess.run("tree -J", capture_output=True, shell=True).stdout)

# parse content file nodes recursively into HTML
parsed_nodes = ''.join(
    parse_directory(node, '/') 
    for node in file_structure[0]['contents'] 
    if match_directory(node['name']))

# open notes page template file
base = open("content_directory/directory_base.md").read()

# append HTML to template stub
content = base + f"<ul>{parsed_nodes}</ul>"

# write results to the directory page
with open("_pages/notes.md", "w") as directory_index:
    directory_index.write(content)