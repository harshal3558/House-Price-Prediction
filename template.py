import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="House-price-prediction"

list_of_files=[
    f"data/raw/",
    f"data/processed/",
    f"notebooks/exploratory_analysis/",
    f"/notebooks/model_building/",
    f"src/__init__.py",
    f"src/data_preprocessing.py",
    f"src/feature_engineering.py",
    f"src/models.py",
    f"src/evaluation.py",
    f"src/deployment.py",
    f"exception.py",
    f"logger.py",
    f"utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")