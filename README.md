# Web Calculator API

Live enviroment: https://directed-mender-261200.uc.r.appspot.com

# Prerequisites
1. Having postresql installed on your machine
2. If you dont want to use a local postgres db, you can create one for free [here](https://elephantsql.com)

# Steps to run locally

1. Create and actiavte vitual enviroment
    - `python3 -m venv venv `
    - `. ./venv/bin/activate`
2. Install requirements
    - pip install -r requirements.txt
3. Create `.env` file with the following variables
    - DATABSE_URI=CHANGE_VALUE
    - SECRET_KEY='CHANGE_VALUE'
    - JWT_SECRET_KEY='CHANGE_VALUE'
    - FLASK_APP=main.py
    - FLASK_DEBUG=1
    - RANDOM_API_KEY=CHANGE_VALUE

*NOTE:* DATABSE_URI shuould start with `postgresql`

4. Migrate database
    - `flask db upgrade head`
5. Run flask app
    - `flask run`