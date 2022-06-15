from flask import Blueprint
from datetime import datetime
from dateutil import parser

filter = Blueprint('filter', __name__)


@filter.app_template_filter()
def dateTimeIndo(value):
    dt_obj = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    dt_str = datetime.strftime(dt_obj, '%d-%m-%Y %H:%M:%S')
    return dt_str

@filter.app_template_filter()
def dateTimeIndo2(value):
    month = ("Januari", "Februari", "Maret",
             "April", "Mei", "Juni", "Juli",
             "Agustus", "September", "Oktober",
             "November", "Desember")

    dt_object = parser.parse(value)
    dt_str = datetime.isoformat(dt_object)
    tahun = dt_str[:4]
    bulan = dt_str[5:7]
    tanggal = dt_str[8:10]

    jam = dt_str[11:13]
    menit = dt_str[14:16]
    detik = dt_str[17:19]

    

    format = tanggal + '-' + month[int(bulan)-1] + '-' + tahun + ' | ' + jam + '-' + menit + '-' + detik
    return format