from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.beranda, name="beranda"),
    path("profil/", views.profil, name="profil"),
    path("ranting/", views.get_ranting, name="ranting"),
    path("amal-usaha/", views.get_amal_usaha, name="amal_usaha"),
    path("berita/", views.berita, name="berita"),
    path("berita/<slug:slug>/", views.berita_detail, name="berita_detail"),
    path("unduhan/", views.unduhan, name="unduhan"),
    path("agenda-kegiatan/", views.get_agenda_kegiatan, name="agenda_kegiatan"),
    path("pimpinan/", views.get_pimpinan, name="pimpinan"),
    path("kontak/", views.kontak, name="kontak"),
    path("pesan-sukses/", views.pesan_sukses, name="pesan_sukses"),
]