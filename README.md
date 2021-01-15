# streamlit-demo

Mini-project for demonstration of Streamlit and Heroku deployment. Contains simple plots
of Titanic dataset and simple Streamlit widgets.

## Local installation

- download repository and install dependencies via
> pip install -r requirements.txt
- start Streamlit server from terminal via
> streamlit run main.py
- local url will be shown in terminal

## Heroku deployment

- in Heroku deployment options, select "GitHub" and connect to repository
- in Heroku, select ``Deploy Branch``
- Following files are required for Heroku deployment
    - ``requirements.txt``: used by Heroku to install requirements. 
      Here ``pywin32`` or other windows packages cannot be used.
    -  ``Procfile``: contains script to be executed for server startup
    - ``runtime.txt``: specifies python version to be used on Heroku
    - ``setup.sh``: creates Streamlit server config. This file executed by Procfile
