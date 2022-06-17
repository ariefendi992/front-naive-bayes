import json
from flask import Blueprint, flash, request, render_template, redirect, url_for
from app.lib.forms.forms_ukt import FormAddUkt
from app.url import base_url
import requests

ukt = Blueprint('ukt', __name__, template_folder='../templates/beasiswa-ukt',
                url_prefix='/beasiswa-ukt')


@ukt.route('/', methods=['GET', 'POST'])
def indexUkt():
    url = base_url+'/beasiswa-ukt/data-record'
    x = request.args.get('page')
    req = requests.get(url + f'?page={x}')

    if req.status_code == 200:
        response = req.json()
        return render_template('get-ukt.html', response=response)
    else:
        return req.json().get('msg')


# tambah record ukt
@ukt.route('/tambah-ukt', methods=['GET', 'POST'])
def tambahDataUkt():
    url_user = base_url+'/auth/user-not-ukt'
    r_user = requests.get(url_user).json()
    resp_user = r_user.get('data')

    select_idUser = [('', '..:: Pilih ::..')]
    for i in resp_user:
        select_idUser.append((i['id'], i['nama'] +' | '+ i['stambuk'] ))

    url_prodi = base_url+'/kategori/jurusan'
    r_prodi = requests.get(url_prodi).json()
    resp_prodi = r_prodi.get('data')

    select_prodi = [('', '..:: Pilih ::..')]
    for i in resp_prodi:
        select_prodi.append((i['id'], i['jurusan']))

    url_sms = base_url+'/kategori/semester'
    r_sms = requests.get(url_sms).json()
    resp_sms = r_sms.get('data')

    select_semester = [('', '..:: Pilih ::..')]
    for i in resp_sms:
        select_semester.append((i['id'], i['semester']))

    select_status_mhs = [('', '..:: Pilih ::..'), ('aktif', 'Aktif'), ('cuti', 'Cuti')]
    
    select_kip = [('', '..:: Pilih ::..'), ('terima', 'Terima'), ('tidak', 'Tidak')]

    url_penghasilan = base_url + '/kategori/penghasilan'
    r_penghasilan = requests.get(url_penghasilan).json()
    resp_penghasilan = r_penghasilan['data']

    select_penghasilan = [('', '..:: Pilih ::..')]
    for i in resp_penghasilan:
        select_penghasilan.append((i['id'], i['keterangan']))

    url_tanggungan = base_url + '/kategori/tanggungan'
    r_tanggungan = requests.get(url_tanggungan).json()
    resp_tanggungan = r_tanggungan['data']

    select_tanggungan = [('', '..:: Pilih ::..')]
    for i in resp_tanggungan:
        select_tanggungan.append((i['id'], i['tanggungan']))

    select_pkh = [('', '..:: Pilih ::..'), ('terima', 'Terima'), ('tidak', 'Tidak')]
    
    select_keputusan = [('', '..:: Pilih ::..'), ('layak', 'Layak'), ('tidak layak', 'Tidak Layak')]
    

    form = FormAddUkt()
    form.idUser.choices = select_idUser
    form.prodi.choices = select_prodi
    form.sms.choices = select_semester
    form.statusMhs.choices = select_status_mhs
    form.kip.choices = select_kip
    form.penghasilan.choices = select_penghasilan
    form.tanggungan.choices = select_tanggungan
    form.pkh.choices = select_pkh
    form.keputusan.choices = select_keputusan

    if form.validate_on_submit() :
        id_user = form.idUser.data
        nik = form.nik.data
        prodi = form.prodi.data
        sms = form.sms.data
        status_mhs = form.statusMhs.data
        kip = form.kip.data
        penghasilan = form.penghasilan.data
        tanggungan = form.tanggungan.data
        pkh = form.pkh.data
        keputusan = form.keputusan.data



        url_ukt = base_url+'/beasiswa-ukt/tambah-data'
        headers = {
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            'id_user': id_user,
            'nik': nik,
            'id_prodi': prodi,
            'id_semester': sms,
            'status_mhs': status_mhs,
            'kip_bm': kip,
            'id_penghasilan': penghasilan,
            'id_tanggungan': tanggungan,
            'pkh_kks': pkh,
            'keputusan': keputusan
        })

        print('json =', payload)
        r = requests.post(url=url_ukt, headers=headers, data=payload)
        # r = requests.request('POST', url_ukt, headers=headers, data=payload)

        if r.status_code == 201:
            flash(message=f'Data beahsil di tambahkan', category='success')
            return redirect(url_for('ukt.indexUkt'))
        else:
            return render_template('tambah-ukt.html', form=form)
    return render_template('tambah-ukt.html', form=form)


# get by id
@ukt.route('/edit-ukt', methods=['POST', 'GET'])
def getByIdUkt():
    # get ukt
    id = request.args.get('id')
    url_ukt = base_url+'/beasiswa-ukt/get-one'
    r_ukt = requests.get(url_ukt+f'?id={id}')
    resp_ukt = r_ukt.json()

    # get user
    url_user = base_url+'/auth/get-all'
    r_user = requests.get(url_user).json()
    resp_user = r_user['data']

    # get prodi
    url_prodi = base_url + '/kategori/jurusan'
    r_prodi = requests.get(url_prodi).json()
    resp_prodi = r_prodi['data']

    # get semester
    url_sms = base_url + '/kategori/semester'
    r_sms = requests.get(url_sms).json()
    resp_sms = r_sms['data']

    # get penghasilan
    url_penghasilan = base_url + '/kategori/penghasilan'
    r_penghasilan = requests.get(url_penghasilan).json()
    resp_penghasilan = r_penghasilan['data']

    return render_template('edit-ukt.html', resp_ukt=resp_ukt, resp_user=resp_user, resp_prodi=resp_prodi, resp_sms=resp_sms, resp_penghasilan=resp_penghasilan)


# update ukt
@ukt.route('/update', methods=['POST', 'PUT'])
def updateUkt():
    nik = request.form.get('nik')
    prodi = request.form.get('prodi')
    sms = request.form.get('semester')
    status_mhs = request.form.get('status_mhs')
    kip = request.form.get('kip')
    penghasilan = request.form.get('penghasilan_orang_tua')
    tanggungan = request.form.get('tanggungan')
    pkh = request.form.get('pkh')
    keputusan = request.form.get('keputusan')

    payload = json.dumps({
        "nik": nik,
        "id_prodi": prodi,
        "id_semester": sms,
        "status_mhs": status_mhs,
        "kip_bm": kip,
        "id_penghasilan": penghasilan,
        "tanggungan": tanggungan,
        "pkh_kks": pkh,
        "keputusan": keputusan
    })

    headers = {
        'Content-Type': 'application/json'
    }
    id = request.args.get('id')
    url = base_url + '/beasiswa-ukt/edit-data'
    r = requests.put(url + f'?id={id}', headers=headers, data=payload)

    if r.status_code == 201:
        return redirect(url_for('ukt.indexUkt'))
    else:
        return redirect(url_for('ukt.getByIdUkt'))


# delete record ukt
@ukt.route('/delete', methods=['POST', 'GET', 'DELETE'])
def deleteUkt():

    url = base_url + '/beasiswa-ukt/delete'

    id = request.args.get('id')
    r = requests.delete(url + f'?id={id}')

    if r.status_code == 204:
        return redirect(url_for('ukt.indexUkt'))
    else:
        return redirect(url_for('ukt.indexUkt'))


# Uji data
@ukt.route('/uji-data', methods=['GET', 'POST'])
def ujiUkt():
    url_user = base_url+'/auth/user-not-ukt'
    r_user = requests.get(url_user).json()
    resp_user = r_user.get('data')

    url_prodi = base_url+'/kategori/jurusan'
    r_prodi = requests.get(url_prodi).json()
    resp_prodi = r_prodi.get('data')

    url_sms = base_url+'/kategori/semester'
    r_sms = requests.get(url_sms).json()
    resp_sms = r_sms.get('data')

    url_penghasilan = base_url + '/kategori/penghasilan'
    r_penghasilan = requests.get(url_penghasilan).json()
    resp_penghasilan = r_penghasilan['data']

    return render_template('uji-data-ukt.html', resp_user=resp_user, resp_prodi=resp_prodi, resp_sms=resp_sms, resp_penghasilan=resp_penghasilan)


# hitung data uji
@ukt.route('/hasil-hitung', methods=['POST', 'GET'])
def prediksi():
    # Request data
    id_user = request.form.get('id_user')
    prodi = request.form.get('prodi')
    sms = request.form.get('semester')
    status_mhs = request.form.get('status_mhs')
    kip = request.form.get('kip')
    penghasilan = request.form.get('penghasilan_orang_tua')
    tanggungan = request.form.get('tanggungan')
    pkh = request.form.get('pkh')

    # url manipulasi
    url_prodi = base_url + '/kategori/jurusan'
    r_prodi = requests.get(url_prodi).json()
    resp_prodi = r_prodi['data']

    url_sms = base_url+'/kategori/semester'
    r_sms = requests.get(url_sms).json()
    resp_sms = r_sms.get('data')

    url_penghasilan = base_url + '/kategori/penghasilan'
    r_penghasilan = requests.get(url_penghasilan).json()
    resp_penghasilan = r_penghasilan['data']

    # to json
    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "id_prodi": int(prodi),
        "id_semester": int(sms),
        "status_mhs": status_mhs,
        "kip_bm": kip,
        "id_penghasilan": int(penghasilan),
        "tanggungan": tanggungan,
        "pkh_kks": pkh
    })
    url = base_url + '/beasiswa-ukt/uji-data'

    r = requests.post(url, headers=headers, data=payload).json()

    response = r
    pay = json.loads(payload)

    print(response)

    return render_template('hasil-uji.html', response=response, resp_prodi=resp_prodi, pay=pay, resp_sms=resp_sms, resp_penghasilan=resp_penghasilan)
