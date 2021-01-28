const fs = require('fs');

const parseDirectory = (dir, path) => {
  path += `${dir.name}/`

  // TODO: dumb conditionals to catch titles, remove
  if (dir.name == 'math') { dir.name = 'Math' }
  if (dir.name == 'note') { dir.name = 'Notes'}

  html += `<br><l>${dir.name}</l><ul>`

  dir.contents.forEach(content => {
    if(content.type == "directory") {
      parseDirectory(content, path)
    }
    if(content.type == "file") {
      parseFile(content, path)
    }
  })
  html += "</ul>"
}

const parseFile = (file, path) => {
  let pathName = file
    .name
    .replace('.md', '');
  path += `${pathName}`

  titleName = pathName.match(/[A-Z][a-z0-9]+/g);
  if(titleName == null) { 
    titleName = pathName 
  } else { 
    // TODO: Join consecutive capital letters
    titleName = titleName.join(' ') 
  }
  html += `<l><a href="${path}">${titleName}</a></l><br>`
}


let html = fs.readFileSync('content_directory/directory_base.md');
html += "<ul>";

JSON.parse(process.argv[2])[0]
  .contents
  .filter(x => x.name == 'math' || x.name == 'note')
  .forEach(x => parseDirectory(x, `/`));

html += "</ul>"

fs.writeFileSync("_pages/notes.md", html)