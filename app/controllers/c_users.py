import json
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.controllers.c_auth import login_dulu
from app.url import *
from app.lib.forms.forms_user import FormRegisterUser
import requests

admin = Blueprint('admin', __name__, url_prefix='/',
                  template_folder='../templates/admin/')

url = base_url + '/kategori/jurusan'
req = requests.get(url).json()
response = req.get('data')
select_prodi = [('', '..:: Pilih ::..')]
for i in response:
    select_prodi.append((i['jurusan'], i['jurusan']))


# dashboard
@admin.route('/', methods=['GET', 'POST'])
@login_dulu
def adminDashboard():
    # if 'admin' in session:
        url = base_url + '/total-data'
        r = requests.get(url).json()
        data = r.get('data')
        ukt = data[0].get('total_penerima').get('beasiswa_ukt')
        print(ukt)
        user = data[0].get('total_user')
        user_login = data[0].get('total_user_login')
        data_uji = data[0].get('total_data_uji')

        print('session ==', session )

        return render_template('dashboard.html', admin=session, ukt=ukt, user=user, user_login=user_login, data_uji=data_uji)
    # else:
        # return redirect(url_for('auth.login'))

# User all data
@admin.route('/users', methods=['GET', 'POST'])
def userData():
    if 'admin' in session:

        url = base_url+'/auth/get-all'
        x = request.args.get('page')
        r = requests.get(url + f'?page={x}')

        if r.status_code == 200:
            response = r.json()
            return render_template('user-data.html', admin=session, response=response)
        else:
            return r.json().get('msg')
    else:
        return redirect(url_for('auth.login'))

# user login data
@admin.get('/users-login')
def userLogin():
    if 'admin' in session:

        url = base_url+'/auth/user-login'

        r = requests.get(url).json()
        resp = r.get('data')

        return render_template('user-login.html', admin=session, response=resp)
    else:
        return redirect(url_for('auth.login'))



# user add
@admin.route('/user-add', methods=['GET', 'POST'])
def userAdd(): 
    if 'admin' in session:  
        select_gender = [("","..:: Pilih ::.."),("laki-laki","Laki-Laki"),("perempuan","Perempuan")]

        form = FormRegisterUser()
        form.prodi.choices = select_prodi
        form.gender.choices = select_gender
        
        if form.validate_on_submit() :
            stambuk = form.stambuk.data
            nama = form.nama.data
            gender = form.gender.data
            prodi = form.prodi.data
            email = form.email.data
            password = form.password.data

            url = base_url + '/auth/register'
            header = {
                'Content-Type': 'application/json'
            }
                        
            payload = json.dumps({
                'stambuk': stambuk,
                'nama' : nama,
                'gender': gender,
                'prodi' : prodi,
                'email': email,
                'password': password
            })

            r = requests.post(url=url, headers=header, data=payload)
            print('status code = ', r.status_code)

            if r.status_code == 201:
                print('status error 201 =', r.json().get('error'))
                flash(message=f'Data {form.nama.data} berhasil di tambahkan.', category='success')
                return redirect(url_for('admin.userData'))
            else:
                return render_template('user-add.html', form=form, prodi=response)

        return render_template('user-add.html', admin=session, form=form)
    else:
        return redirect(url_for('auth.login'))



# get user by id
@admin.route('/edit-user', methods=['POST', 'GET'])
def userById():
    if 'admin' in session:
        id = request.args.get('id')
        url = base_url + ('/auth/get-uid')

        r = requests.get(url + f'?id={id}')

        resp = r.json()

        return render_template('user-edit.html',admin=session, response=resp)
    else:
        return redirect(url_for('auth.login'))



# edit user
@admin.route('/update', methods=['PUT', 'PATCH', 'POST'])
def userEdit():
    if 'admin' in session:
        stambuk = request.form.get('nim')
        nama = request.form.get('name')
        gender = request.form.get('jk')
        email = request.form.get('mail')
        password = request.form.get('pswd')

        headers = {
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            'stambuk': stambuk,
            'nama': nama,
            'gender': gender,
            'email': email,
            'password': password
        })

        id = request.args.get('id')
        url = base_url + '/auth/edit-user'
        r = requests.put(url + f'?id={id}', headers=headers, data=payload)

        if r.status_code == 201:
            return redirect(url_for('admin.userData'))
        else:
            return redirect(url_for('admin.userById'))
    else:
        return redirect(url_for('auth.login'))



# delete user
@admin.route('/delete-user', methods=['POST', 'GET', 'DELETE'])
def userDelete():
    if 'admin' in session:
        id = request.args.get('id')
        url = base_url + ('/auth/delete-user')
        r = requests.delete(url + f'?id={id}')
        if r.status_code == 204:
            flash(message=f'Data telah di hapus.', category="danger")
            return redirect(url_for('admin.userData'))
    else:
        return redirect(url_for('auth.login'))



