﻿# fastapi-blog-project
 ##installing virtual env and runnning it
pip install virtualenv
python3 -m venv app
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
.\app\Scripts\Activate.ps1
##Installing required libraries
pip install -r /path/to/requirements.txt
##Running the app
uvicorn main:app --reload
