# script that recursively parses JSON folder structure into an static HTML page
import subprocess, json

# lambda to match only required sub directories
def match_directory(node):
    return node['name'] == 'math' or node['name'] == 'note'

def parse_directory(node, path):
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

# append content to base directory file by recursively stepping through JSON
content = open("content_directory/directory_base.md").read() + f"<ul>{''.join([parse_directory(x, '/') for x in filter(match_directory, file_structure[0]['contents'])])}</ul>"

# write results to the directory page
with open("_pages/notes.md", "w") as directory_index:
    directory_index.write(content)