# we are creating this template so that we write entire structure of folder or file such that we don't need to create folders and files manually .DeprecationWarning
 
# importing some libraries
import os 
from pathlib import Path #this a path library
# then we also need python in bit logging4
import logging


# thn frst we need to create our logging stream so 
logging.basicConfig(level= logging.INFO, format = '[%(asctime)s]: %(message)s:')

# specifying the project name
project_name = "text_summarizer" 

# List of files and folder we need to create 
list_of_files = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) 

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the {filename} file")

    if(not os.path.exists(filename)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empthy file : {filepath}")


    else:
        logging.info(f"{filename}is already exist")
       