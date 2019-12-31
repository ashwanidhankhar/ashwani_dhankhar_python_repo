# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:26:48 2019

@author: BSDU ADMIN
"""


from flask import Flask

app=Flask(__name__)

@app.route("/ashwani")

def BSDU():
    return "<h1>BSDU</h1><br>Welcome to Bhartiya Skill Development University,Jaipur"

if __name__=="__main__":
    app.run()