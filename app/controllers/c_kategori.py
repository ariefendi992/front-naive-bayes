import json
from flask import Blueprint, flash, render_template, request, session, redirect, url_for
from app.lib.forms.forms_kategori import PenghasilanOrtuForm, ProdiForm, SemesterForm, TanggunganForm
from app.url import base_url
import requests

kategori = Blueprint('kategori', __name__, url_prefix='/', template_folder='../templates/kategori/')

# kategori Semester
@kategori.route('/kategori-semester', methods=['GET', 'POST'])
def kategoriS():
    if 'admin' in session:
        url = base_url + '/kategori/semester'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('semester.html', admin=session, response=response)
    else:
        return redirect(url_for('auth.login'))

# add kategori semester
@kategori.route('add-semester', methods=['POST', 'GET'])
def add_semester():
    if 'admin' in session:
        form = SemesterForm()
        if form.validate_on_submit():
            semester = form.semester.data

            url = base_url+'/kategori/semester'
            headers = {
                'Content-Type': 'application/json'
                }
            payload = json.dumps({
                'semester' : semester
            })

            req = requests.post(url, headers=headers, data=payload)

            if req.status_code == 201:
                flash(message=f'Data telah di tambahkan.', category='success')
                return redirect(url_for('kategori.kategoriS'))
            else:
                return render_template('add_semeste.html', form=form, admin=session)
        return render_template('add_semester.html', form=form,  admin=session)
    else:
        return redirect(url_for('auth.login'))

# delete semester
@kategori.route('/semester', methods=['delete','GET'])
def delete_semester():
    if 'admin' in session:
        id = request.args.get('id')
        url = base_url+f'/kategori/semester/{id}'
        print(url)
        req = requests.delete(url)
        if req.status_code == 204:
            flash(message=f'Data telah di hapus.', category="danger")
            return redirect(url_for('kategori.kategoriS'))
    else:
        return redirect(url_for('auth.login'))
    


# kategori jurusan
@kategori.route('/kategori-jurusan', methods=['GET', 'POST'])
def kategoriJ():
    if 'admin' in session:
        url = base_url + '/kategori/jurusan'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('jurusan.html', admin=session, response=response)
    else:
        return redirect(url_for('auth.login'))

# add jurusan
@kategori.post('/add-prodi')
@kategori.get('/add-prodi')
def add_prodi():
    if 'admin' in session:
        form = ProdiForm()
        if form.validate_on_submit():
            jurusan = form.prodi.data

            url = base_url+'/kategori/jurusan'

            payload = json.dumps({
                "jurusan": jurusan
                })
            
            headers = {
                'Content-Type': 'application/json'
                }
            req = requests.post(url, headers=headers, data=payload)

            if req.status_code == 201:
                flash(message=f'Data telah di tambahkan.', category='success')
                return redirect(url_for('kategori.kategoriJ'))
            else:
                return render_template('add_jurusan.html', admin=session, form=form)
        return render_template('add_jurusan.html', admin=session, form=form)
    else:
        return redirect(url_for('auth.login'))


# delete kategori jurusan
@kategori.delete('/jurusan')
@kategori.get('/jurusan')
def delete_jurusan():
    if 'admin' in session:
        id = request.args.get('id')
        url = base_url+f'/kategori/jurusan/{id}'
        print(url)
        req = requests.delete(url)
        if req.status_code == 204:
            flash(message=f'Data telah di hapus.', category="danger")
            return redirect(url_for('kategori.kategoriJ'))
    else:
        return redirect(url_for('auth.login'))

# kategori Penghasilan
@kategori.route('/kategori-penghasilan', methods=['GET', 'POST'])
def kategoriPenghasilan():
    if 'admin' in session:
        url = base_url + '/kategori/penghasilan'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('penghasilan.html', admin=session, response=response)
    else:
        return redirect(url_for('auth.login'))


# add kategori penghasilan
@kategori.route('/add-penghasilan', methods=['POST', 'GET'])
def add_penghasilan():
    if 'admin' in session:
        form = PenghasilanOrtuForm()
        if form.validate_on_submit():
          penghasilan = form.penghasilan.data 
          keterangan = form.keterangan.data 

          url = base_url+'/kategori/penghasilan'
          headers = {
            'Content-type' : 'application/json'
          }  
          payload = json.dumps({
            'penghasilan' : penghasilan,
            'keterangan' : keterangan,
          })
          req = requests.post(url, headers=headers, data=payload)

          if req.status_code == 201:
            flash(message=f'Data telah di tambahkan.', category='success')
            return redirect(url_for('kategori.kategoriPenghasilan'))
        else:
            return render_template('add_penghasilan.html', form=form, admin=session)
        return render_template('add_penghasilan.html', form=form, admin=session)
    
    else:
        return redirect(url_for('auth.login'))

# delete kategori penghasilan
@kategori.delete('/penghasilan')
@kategori.get('/penghasilan')
def delete_penghasilan():
    if 'admin' in session:
        id = request.args.get('id')
        url = base_url+f'/kategori/penghasilan/{id}'
        print(url)
        req = requests.delete(url)
        if req.status_code == 204:
            flash(message=f'Data telah di hapus.', category="danger")
            return redirect(url_for('kategori.kategoriPenghasilan'))
    else:
        return redirect(url_for('auth.login'))


# kategori Penghasilan
@kategori.route('/kategori-tanggungan', methods=['GET', 'POST'])
def kategoriTanggungan():
    if 'admin' in session:
        url = base_url + '/kategori/tanggungan'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('tanggungan.html', admin=session, response=response)
    else:
        return redirect(url_for('auth.login'))
# kategori tanggungan
@kategori.route('/add-tanggungan', methods=['POST','GET'])
def add_tanggungan():
    if 'admin' in session:
        form = TanggunganForm()
        if form.validate_on_submit():
            tanggungan = form.tanggungan.data

            url = base_url+'/kategori/tanggungan'
            headers = {
                'Content-type' : 'application/json'
            }
            payload = json.dumps({
                'tanggungan' : tanggungan
            })

            req = requests.post(url, headers=headers, data=payload)

            if req.status_code == 201:
                flash(message=f'Data telah di tambahkan.', category='success')
                return redirect(url_for('kategori.kategoriTanggungan'))
            else:
                return render_template('add_tanggungan.html', form=form, admin=session)
        return render_template('add_tanggungan.html', form=form, admin=session)
    else:
        return redirect(url_for('auth.login'))

# delete tanggungan
@kategori.delete('/tanggungan')
@kategori.get('/tanggungan')
def delete_tanggungan():
    if 'admin' in session:
        id = request.args.get('id')
        url = base_url+f'/kategori/tanggungan/{id}'
        print(url)
        req = requests.delete(url)
        if req.status_code == 204:
            flash(message=f'Data telah di hapus.', category="danger")
            return redirect(url_for('kategori.kategoriTanggungan'))
    else:
        return redirect(url_for('auth.login'))
