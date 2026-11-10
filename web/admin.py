from django.contrib import admin

from .models import (
    Agenda, AmalUsaha, Berita, Dokumen, PesanMasuk,
    Pimpinan, ProfilOrganisasi, Ranting, TautanTerkait,
)

admin.site.site_header = "Admin Website PCM BAKI JAUH DARI RUMAH KTA"
admin.site.site_title = "Admin Website PCM"
admin.site.index_title = "Kelola Konten Website"


@admin.register(ProfilOrganisasi)
class ProfilOrganisasiAdmin(admin.ModelAdmin):
    list_display = ("nama", "nama_singkat", "telepon", "email")

    def has_add_permission(self, request):
        return not ProfilOrganisasi.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ("nama", "jabatan", "periode", "urutan")
    list_editable = ("urutan",)
    search_fields = ("nama", "jabatan")


@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
    list_display = ("nama", "ketua", "telepon")
    search_fields = ("nama", "ketua")


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ("nama", "bidang", "alamat")
    list_filter = ("bidang",)
    search_fields = ("nama", "deskripsi")


@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ("judul", "status", "tanggal_terbit")
    list_filter = ("status",)
    search_fields = ("judul", "ringkasan")
    prepopulated_fields = {"slug": ("judul",)}
    date_hierarchy = "tanggal_terbit"


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ("nama_kegiatan", "waktu_mulai", "tempat")
    list_filter = ("waktu_mulai",)
    search_fields = ("nama_kegiatan", "tempat")


@admin.register(Dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ("judul", "tanggal_unggah")
    search_fields = ("judul",)


@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = ("subjek", "nama", "email", "waktu_kirim", "sudah_dibaca")
    list_filter = ("sudah_dibaca", "waktu_kirim")
    search_fields = ("nama", "email", "subjek")
    readonly_fields = ("nama", "email", "subjek", "pesan", "waktu_kirim")

    def has_add_permission(self, request):
        return False


@admin.register(TautanTerkait)
class TautanTerkaitAdmin(admin.ModelAdmin):
    list_display = ("nama", "url", "urutan")
    list_editable = ("urutan",)