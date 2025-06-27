import os
import shutil
import nbformat as nbf

# Set your target directory where the Excel files are located
directory = r"custom"


# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith(".xlsx"):
        file_path = os.path.join(directory, filename)

        # Remove file extension to get folder name
        base_name = filename.rsplit(".", 1)[0]
        folder_path = os.path.join(directory, base_name)

        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Move the Excel file into the new folder
        new_file_path = os.path.join(folder_path, filename)
        shutil.move(file_path, new_file_path)

        print(f"Moved '{filename}' to '{folder_path}'")

        # Create a blank notebook with a markdown title cell
        nb = nbf.v4.new_notebook()
        nb.cells.append(nbf.v4.new_markdown_cell(f"# Notebook for {base_name}"))

        notebook_path = os.path.join(folder_path, f"{base_name}.ipynb")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)

        print(f"Created notebook: '{notebook_path}")
