## here we are goin to write all the filees name which we need to create

import os
from pathlib import Path
import logging

## creating a list of files

files_list=[
    ".github/workflows/.gitkeep",                   ### ".gitkeep" we use for continous integration and continous deployement
    "src/__init__.py",                              ### "src" folders contains all the source code and "__init__" we use to consider the foldeer as module and call any file into any another folder
    "src/components/__init__.py"                    ### "components" whatever stages we do for from data pipeline to testing, these all are contains multiple cmponents.thus e keep it here
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/pipeline/model_evaluation.py",
    "src/pipeline/model_trainer.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",                          ### this file for devlopment environment
    "setup.py",
    "setup.cfg",
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
        
        