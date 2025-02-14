import os
import nbformat
import re

# Function to sanitize folder names by removing invalid characters
def sanitize_folder_name(folder_name):
    # Regular expression pattern to match invalid characters
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized_name = re.sub(invalid_chars, '_', folder_name)  # Replace invalid chars with underscore '_'
    return sanitized_name

# Function to extract all the code cells, where we are passing the file path as parameter and are returning a list of code cell contents as strings.
def extract_code_cells(notebook_file_path):
    try:
        # Open and read the notebook file
        with open(notebook_file_path, 'r', encoding='utf-8') as notebook_file:
            notebook_content = nbformat.read(notebook_file, as_version=4)

        # Extract code cells
        code_cells = []
        for cell in notebook_content.cells:
            if cell.cell_type == 'code':
                code_cells.append(cell.source)

        return code_cells

    except FileNotFoundError:
        print(f"Error: The file at {notebook_file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error reading the notebook: {str(e)}")
        return None


# Function to save each code cell to a separate .py file in the specified output folder
def save_code_cells_to_files(code_cells, output_folder):
    if not code_cells:
        print("No code cells to save.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save each code cell as a .py file
    for index, code in enumerate(code_cells, start=1):
        file_path = os.path.join(output_folder, f"code_cell_{index}.py")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        print(f"Saved code cell {index} to {file_path}")

    # Display no. of total files saved to user after all process ends.
    print(f"\nProcess complete! {len(code_cells)} code cells were extracted and saved.")

def main():
    # Taking user input for notebook file path
    notebook_file_path = input("Enter path of notebook: ").strip()
    print() # To add a newline

    # Check if the path is relative or absolute
    if not os.path.isabs(notebook_file_path):
        notebook_file_path = os.path.abspath(notebook_file_path)  # Convert relative path to absolute path

    # Check if the notebook file exists
    if not os.path.exists(notebook_file_path):
        print(f"Error: The file at {notebook_file_path} does not exist.")
        return

    # Generating output folder name
    base_filename = os.path.splitext(os.path.basename(notebook_file_path))[0]
    sanitized_folder_name = sanitize_folder_name(base_filename)  # Sanitize the folder name
    output_folder = os.path.join("Outputs", sanitized_folder_name)  # Outputs/<sanitized_notebook_name>/ 

    # Calling function to extract code cells
    code_cells = extract_code_cells(notebook_file_path)

    if code_cells is not None:
        # Calling function to save code cells to files
        save_code_cells_to_files(code_cells, output_folder)


# Add dunder main to prevent unintended execution of the program
if __name__ == "__main__":
    main()
