# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:41:22 2019

@author: BSDU ADMIN
"""

import flask

from flask import Flask

app=Flask(__name__)

@app.route("/ashwani")

def welcome():
    return "Welcome to my first Flask App"

app.run()

#or same as above
"""
if __name=="__main__":
    app.run()
"""















"""
#############################################################################################
"""






import flask

from flask import Flask

app=Flask(__name__)

@app.route("/ashwani")

def welcome():
    return "Welcome to my first Flask App"

app.run(host='0.0.0.0',port=81)


