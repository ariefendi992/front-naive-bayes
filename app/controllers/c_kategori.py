from flask import Blueprint, render_template, session, redirect, url_for
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
        return render_template('semester.html', response=response)
    else:
        return redirect(url_for('auth.login'))


# kategori jurusan
@kategori.route('/kategori-jurusan', methods=['GET', 'POST'])
def kategoriJ():
    if 'admin' in session:
        url = base_url + '/kategori/jurusan'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('jurusan.html', response=response)
    else:
        return redirect(url_for('auth.login'))


# kategori Penghasilan
@kategori.route('/kategori-penghasilan', methods=['GET', 'POST'])
def kategoriPenghasilan():
    if 'admin' in session:
        url = base_url + '/kategori/penghasilan'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('penghasilan.html', response=response)
    else:
        return redirect(url_for('auth.login'))


# kategori Penghasilan
@kategori.route('/kategori-tanggungan', methods=['GET', 'POST'])
def kategoriTanggungan():
    if 'admin' in session:
        url = base_url + '/kategori/tanggungan'
        req = requests.get(url).json()
        response = req.get('data')
        return render_template('tanggungan.html', response=response)
    else:
        return redirect(url_for('auth.login'))

