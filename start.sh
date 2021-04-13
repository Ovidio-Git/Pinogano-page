#!/bin/bash



export FLASK_APP=main.py
export FLASK_DEBUG=0
export FLASK_ENV=production

sudo fuser -k 5000/tcp

flask run 
