# script that recursively parses JSON folder structure into an static HTML page
import subprocess, json, random, string
from typing import List

root_dirs = {'math', 'programming'}

# configuration kwargs for subprocess
sp_config = { "shell": True, "capture_output": True }

# recursively join file word lists that contain single character acronyms
# folders must have acronyms separated by underscores, For example:
# To get the output "API" the corresponding directory is called "a_p_i"
def join_with_acronyms(words: List[str]) -> str:
    current_word, *tail = words
    if len(tail) > 0:
        next_word = tail[0]
        insert = "" if len(current_word) == 1 and len(next_word) == 1 else " "
        return current_word + insert + join_with_acronyms(tail)
    else:
        return current_word

# used for deduping directory names
def random_string() -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(10))


# function to match only required sub directories
def match_directory(name: str) -> bool:
    return name in root_dirs

def parse_directory(node: dict, path: str) -> str:
    if node["type"] == "directory":
        path += f"{node['name']}/"
        # Separate and capitalize folder titles based on _
        directory_name = join_with_acronyms(
            word.capitalize()
            for word in node['name'].split('_'))
        directory_content = ''.join(
            parse_directory(child, path)
            for child in node['contents'])
        # checked if else opens root level directories by default

        # use a id to dedup CSS properties
        directory_id = random_string()

        # template the content
        return f"""
        <l>
        <input type="checkbox" id="{directory_id}" {"checked" if match_directory(node['name']) else ""}>
        <label for="{directory_id}">{directory_name}</label>
        <ul>{directory_content}</ul>
        </l>
        """
    else:
        # gather meta data from file about its title to display on the contents page
        # this is because file names are not enough to give the correct title for the contents page
        # instead each file contains a "title" metadata markdown field which is used
        command = f"cat {path.replace('/', '', 1) + node['name']} | grep title: | head | sed 's/title: //'"
        page_title = subprocess.run(command, **sp_config).stdout.decode('utf-8').strip('\n')
        return f"<l class=\"file_content\"><a href='{path + node['name'].replace('.md', '')}'>{page_title}</a></l><br>"

# generate file structure JSON using tree command
# the -J flag generates JSON and the --dirsfirst command lists directories over files first in ordering
# this is mirrored in the display of the file structure on the final page
file_structure = json.loads(subprocess.run("tree -J --dirsfirst", **sp_config).stdout)

# parse content file nodes recursively into HTML
# contained in div tags to fix accordion styling issues
parsed_nodes = f"""
    <div name="contents-index">
    {
        ''.join(
        parse_directory(node, '/') 
        for node in file_structure[0]['contents'] 
        if match_directory(node['name']))
    }
    </div>
    """

# open notes page template file
base = open("content_directory/directory_base.md").read()

# append HTML to template stub
content = base + f"<ul>{parsed_nodes}</ul>"

# write results to the directory page
with open("_pages/notes.md", "w") as directory_index:
    directory_index.write(content)

# TODO: Update to edit file in place with bash script
tidy_content = subprocess.run("html-beautify _pages/notes.md", **sp_config).stdout.decode('utf-8')

with open("_pages/notes.md", "w") as directory_index:
    directory_index.write(tidy_content)
