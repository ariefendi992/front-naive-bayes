from app.controllers.c_users import admin
from app.controllers.c_beasiswa_ukt import ukt
from app.lib.custom_filter import filter
from app.controllers.c_kategori import kategori


def registerApp(app):
    app.register_blueprint(admin)
    app.register_blueprint(ukt)
    app.register_blueprint(kategori)


def registerLib(app):
    app.register_blueprint(filter)
