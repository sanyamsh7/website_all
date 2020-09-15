# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:29:50 2020

@author: Dell
"""

from flask import Flask, render_template, url_for, flash, redirect


#app initialisation
app = Flask(__name__)


@app.route("/")
@app.route("/login")
@app.route("/home")
def home():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('registration.html')

##Main loop
if __name__ == '__main__':
    print("Application is running")
    app.run(debug = True)
