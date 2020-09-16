# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:29:50 2020

@author: Dell
"""

from flask import Flask, render_template, url_for, flash, redirect, request
import sqlite3

# app initialisation
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    return render_template('registration.html')


# Checking if the user exist for login
@app.route("/valid_user", methods=['POST'])
def valid_user():
    # taking username and password from the form
    username = request.form['lg_username']
    password = request.form['lg_password']
    with sqlite3.connect('credentials.db') as conn:
        cur = conn.cursor()

        # retrieving the role of the concerned user
        row = cur.execute('''SELECT role FROM Credentials WHERE username = ? AND password = ?''',
                          (username, password)).fetchone()

    if row is None:
        return 'You need to register first'
    elif row[0] == 'Employee':
        return render_template('employee.html')
    elif row[0] == 'Employer':
        return render_template('employer.html')
    else:
        return 'An Error has occurred, please try again'


# adding a new user
@app.route("/new_user", methods=['POST'])
def new_user():
    if request.method == 'POST':
        # taking the information of the registering user
        username = request.form['reg_username']
        password = request.form['reg_password']
        password_confirm = request.form['reg_password_confirm']
        email = request.form['reg_email']
        full_name = request.form['reg_fullname']
        gender = request.form.get('reg_gender')
        role = request.form.get('reg_role')

        if password == password_confirm:
            with sqlite3.connect('credentials.db') as conn:
                cur = conn.cursor()

                cur.execute('''SELECT * FROM Credentials WHERE username = ? AND password = ?''',
                            (username, password))
                row = cur.fetchone()
                if row is None:

                    # inserting the records of new user in database
                    cur.execute('''INSERT INTO Credentials (username, password, email, fullname, gender, role) 
                        VALUES ( ?, ?, ?, ?, ?, ? )''', (username, password, email, full_name, gender, role))
                    conn.commit()

                else:
                    return 'You are already registered'

            return render_template('register_success.html')

        else:
            return render_template('register_fail.html')


# Main loop
if __name__ == '__main__':
    app.run(debug=True)
