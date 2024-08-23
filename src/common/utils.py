
def write_markdown_file(content, filename):
  """Writes the given content as a markdown file to the local directory.

  Args:
    content: The string content to write to the file.
    filename: The filename to save the file as.
  """
  with open(f"{filename}.md", "w") as f:
    f.write(content)


def read_markdown_files(filename):
    with open(filename, 'r') as file:
      content = file.read()
    return content