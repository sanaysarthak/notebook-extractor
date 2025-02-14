<a id="readme-top"></a>

<br />
  <h1 align="center">Jupyter Notebook Code Extractor</h1>

  <p align="center">
    A Python automation script to extract all code cells from a Jupyter Notebook and save each one as an individual .py file.
   </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
     </li>
      </ul>
    </li>
    <li>
      <a href="#setup">Setup</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#how-to-use">How to Use</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#example">Example</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#libraries-used">Libraries Used</a>
      <ul>
      </ul>
    </li>
  </ol>
</details>



<!--OVERVIEW --> 
<a id="overview"></a>
## Overview :-

This project allows users to easily extract all code cells from a Jupyter notebook and save each code cell as a separate Python script (```.py```). The code cells are stored in an organized folder structure under a root "Outputs" directory. The folder names are sanitized to ensure compatibility across different operating systems by removing invalid characters (e.g., ```<```, ```>```, ```:```, etc.).

Key features include:
- Input of notebook path (relative or absolute).
- Automatic creation of a sanitized output folder.
- Extraction and saving of each code cell as a separate ```.py``` file.
- Informative messages indicating progress and completion.



<!--SETUP -->
<a id="setup"></a>
## Setup :-

#### Prerequisites
- Python 3.x installed on your machine.
- ```pip``` for installing dependencies

#### Installing Dependencies
1. Clone or download this repository to your local machine.
  ```sh
   git clone https://github.com/sanaysarthak/notebook-extractor.git
  ```
2. Navigate to the project directory.
  ```sh
   cd notebook-extractor
  ```
3. Install the required dependencies by running the following command in your terminal.
  ```sh
  pip install -r requirements.txt
  ```



<!-- HOW TO USE -->
<a id="how-to-use"></a>
## How to Use :-

#### Step 1: Place your Jupyter notebook
Put your Jupyter notebook (e.g., ```.ipynb``` file) in the Test Input/ directory or provide the full/relative path to the notebook when prompted.

#### Step 2: Run the Script
In the project folder, run the ```notebook-extractor.py``` script by executing the following command:
```sh
python notebook-extractor.py
```
#### Step 3: Enter the Notebook File Path
You will be prompted to enter the file path of the notebook. You can either provide an **absolute path** or a **relative path** to your notebook file.

#### Step 4: View the Results
After running the script, the extracted Python code cells will be saved as individual ```.py``` files inside an ```Outputs/``` folder, which will be named after your notebook file (sanitized to remove any invalid characters). \
For example, if your notebook is named ```basic_datatypes.ipynb```, the extracted code cells will be saved in ```Outputs/basic_datatypes/```. \
The script will also inform you how many code cells were successfully extracted and saved.



<!--EXAMPLE -->
<a id="example"></a>
## Example :-

#### Input
Let’s say we have a Jupyter notebook named ```basic_datatypes.ipynb``` that contains 16 code cells.

#### Command to Run the Script
```sh
python notebook-extractor.py
```

#### Output
The script will create the following directory structure inside the ```Outputs/``` folder:
```sh
Outputs/
└── basic_datatypes/
    ├── code_cell_1.py
    ├── code_cell_2.py
    ├── code_cell_3.py
    ├── code_cell_4.py
    ├── code_cell_5.py
    ├── code_cell_6.py
    ├── code_cell_7.py
    ├── code_cell_8.py
    ├── code_cell_9.py
    ├── code_cell_10.py
    ├── code_cell_11.py
    ├── code_cell_12.py
    ├── code_cell_13.py
    ├── code_cell_14.py
    ├── code_cell_15.py
    └── code_cell_16.py
```

The script will print the following message after the extraction:
```sh
Process complete! 16 code cells were extracted and saved.
```



<!--LIBRARIES-USED -->
<a id="libraries-used"></a>
## Libraries Used :-

This project requires the following Python dependencies:

- ```nbformat``` - To read and process Jupyter notebook files.
- ```re``` - For sanitizing folder names (standard Python library).
  
