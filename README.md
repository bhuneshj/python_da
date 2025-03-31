# Create virtual environment

> A virtual environment is a Python environment such that the Python interpreter, libraries, and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.

- Install a Virtual Environment using Venv  
    `pip install virtualenv`  
- Create Virtual Environment  
    `python -m venv pyenv`  
    `ls`  
- Activate  
    - Linux: `source pyenv/bin/activate`  
    - Windows: 
        `pyenv/Scripts/Activate.ps1` 
        `<pyenv/Scripts/activate`  
- List python libraries  
    `pip list`  
- Create Requirements.txt (You can name this requirements.txt file whatever you want.)  
    `pip freeze > requirements.txt`  
- Install from requirements.txt  
    `pip install -r requirements.txt`  
- Deactivate  
    `deactivate`

## Jupyter Labs
Install JupyterLab with pip

`pip install jupyterlab`

Once installed, launch JupyterLab with:

`jupyter notebook`

##  Working with Pandas
