import json
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.lib.forms.forms_login import FormLogin
from app.url import base_url
import requests

auth = Blueprint('auth', __name__, template_folder='../templates/auth/')

@auth.route('/login', methods=['POST','GET'])
def login():

    select_status = [('','..:: Pilih ::..'), ('admin','Admin'), ('user', 'User')]


    form = FormLogin()
    form.status.choices = select_status
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        status = form.status.data

        url = base_url + '/auth/login-pengguna'

        payload = json.dumps({
            'username' : username,
            'password' : password,
            'status' : status
        })

        headers = {
             'Content-Type': 'application/json'
            }

        resp = requests.post(url=url, headers=headers, data=payload)     
        json_resp = resp.json()
       
        if json_resp['status'] == 'admin':
            session['username'] = json_resp['username']
            session['admin'] = json_resp['status']
            session.permanent = True
            flash(message=f'Login Sukses. selamat datang {json_resp["status"]}', category='success')
            return redirect(url_for('admin.adminDashboard'))
    else:
        if 'admin' in session:
            return redirect(url_for('admin.adminDashboard'))
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('auth.login'))