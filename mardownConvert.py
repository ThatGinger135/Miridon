import markdown
import os

# Set the path to the root directory
root_dir = "C:/Users/mikea/Documents/obsidianNotes/Miridon"

# Set the path to the output directory
output_dir = "mdFiles"

# Loop through all files and directories in the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".md"):
            # Construct the paths for the input and output files
            input_path = os.path.join(dirpath, filename)
            rel_input_path = os.path.relpath(input_path, root_dir)
            output_path = os.path.join(output_dir, rel_input_path[:-3] + ".html")
            output_dirname = os.path.dirname(output_path)
            
            # Create the output directory if it doesn't exist
            os.makedirs(output_dirname, exist_ok=True)
            
            # Read in the markdown file
            with open(input_path, "r") as md_file:
                md_content = md_file.read()
            
            # Convert the markdown to HTML
            html_content = markdown.markdown(md_content)
            
            # Write the HTML to the output file
            with open(output_path, "w") as html_file:
                html_file.write(html_content)
