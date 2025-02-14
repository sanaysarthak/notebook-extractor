import os
import nbformat

# Function to extract all the code cells, where we are passing the file path as parameter and are returning a list of code cell contents as strings.
def extract_code_cells(notebook_file_path):

    # Open and read the notebook file
    with open(notebook_file_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Extract code cells
    code_cells = []
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            code_cells.append(cell.source)

    return code_cells


# Function to save each code cell to a seperate .py file in the specified output folder
def save_code_cells_to_files(code_cells, output_folder):

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save each code cell as a .py file
    for index, code in enumerate(code_cells, start=1):
        file_path = os.path.join(output_folder, f"code_cell_{index}.py")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        print(f"Saved code cell {index} to {file_path}")


# Taking user input for notebook file path
notebook_file_path = input("Enter path of notebook: ")

# Generating output folder name
base_filename = os.path.splitext(os.path.basename(notebook_file_path))[0]
output_folder = f"output - {base_filename}"

# Calling function to extract code cells
code_cells = extract_code_cells(notebook_file_path)

# Calling function to save code cells to files
save_code_cells_to_files(code_cells, output_folder)
