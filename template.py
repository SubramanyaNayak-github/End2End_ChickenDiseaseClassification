import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = 'ChickenDiseaseClassification'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]

for file in list_of_files:
    file = os.path.abspath(file)
    filedir,filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info('Creating directory :{} for the file {}'.format(filedir, filename))

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file,'w') as f:
            pass
            logging.info('Creating empty file :{}'.format(file))

    else:
        logging.info('File already exists :{}'.format(file))