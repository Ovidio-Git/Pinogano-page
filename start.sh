#!/bin/bash

source ../bin/activate

export FLASK_APP=app.py
export FLASK_DEBUG=1
export FLASK_ENV=development

sudo fuser -k 5000/tcp

flask run
