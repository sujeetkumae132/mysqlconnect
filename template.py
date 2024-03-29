## here we are goin to write all the filees name which we need to create

import os
from pathlib import Path
import logging

python_package="mysql_connect"

## creating a list of files

files_list=[
    ".github/workflows/ci.yaml",                  
    "src/__init__.py",                              
    f"src/{python_package}/__init__.py"                    
    "src/{python_package}/mysql_crud.py",
    "test/__init__.py"
    "tests/unit/__init__.py",
    "test/unit/unit.py"                                 ##here we'll write all the test cases
    "tests/integration/__init__.py",
    "test/integration/int.py",                          ## here we'll write all the test cases for integration purpose
    "init_setup.sh",                                    ## here we'll write all the shell/linux command                      
    "requirements.txt",                                 ## it is for the user environment where test cases not required
    "requirements_dev.txt",                             ## this will be for the devlopment environment only it means for local. because test cases we don't use in user environment    
    "setup.py",
    "setup.cfg",                                        ## this file is used by setuptools to configre the packaging and installation of a python project
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for file in files_list:
    filepath=Path(file)
    filedir,filename=os.path.split(filepath)
    if filedir != "":                               ### "!="" " it means if filedir not exist
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):        ### creating a file or inside a folder there is no file
        with open(filepath,"w") as f:
            pass                                    ### create an empty file
        
        