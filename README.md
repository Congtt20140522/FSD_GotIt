# FSD_GotIt
## Installation:

#### Install python3.5:
    cd ~
    sudo apt-get update
    sudo apt-get install python3.5
    
#### Install **python3 pip**:

    sudo apt-get install python3-pip

#### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

#### Now create a virtual environment 

    virtualenv TwoFootball 

#### Active your virtual environment:    
    
    source TwoFootball/bin/activate
    
#### To deactivate:

    deactivate

## Install Flask on virtual environment:
    
#### Active virtual enviroment:
    source TwoFootball/bin/activate
    
#### Install Flask:
    sudo pip3 install flask
    
#### Install Flask extensions:
    sudo pip3 install PyMySQL
    sudo pip3 install flask-wtf
    sudo pip3 install flask-sqlalchemy
    sudo pip3 install flask-migrate

### Install MySQL

Link: [Install MySQL on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)

## Run Project:

#### Set flask app:
    export FLASK_ENV=development
    export FLASK_APP=twofootball.py
    
#### Migrate database:
Please change database setting in config.py

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/database_name'

After that, run these commands:

    flask db init
    flask db migrate
    flask db upgrade
    
#### Run application:
    flask run