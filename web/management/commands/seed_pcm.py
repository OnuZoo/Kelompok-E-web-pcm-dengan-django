from django.core.management.base import BaseCommand
from django.db import transaction

from web.models import (
    ProfilOrganisasi,
    Pimpinan,
    Ranting,
    AmalUsaha,
    Berita,
    Agenda,
    TautanTerkait,
)


# ==========================================================
# DATA SEED
# Isi bagian ini menggunakan data PCM yang sudah diverifikasi.
# Jangan mengisi dengan data perkiraan atau data fiktif.
# ==========================================================

PROFIL = {
    "nama": "",
    "nama_singkat": "",
    "tagline": "",
    "tentang": "",
    "sejarah": "",
    "visi": "",
    "misi": "",
    "alamat_sekretariat": "",
    "telepon": "",
    "email": "",
    "jumlah_anggota_ktam": 0,
}

PIMPINAN = [
    # Contoh struktur:
    # {
    #     "nama": "Nama sesuai sumber resmi",
    #     "jabatan": "Jabatan",
    #     "periode": "2022-2027",
    #     "urutan": 1,
    # },
]

RANTING = [
    # {
    #     "nama": "Nama ranting",
    #     "ketua": "Nama ketua",
    #     "alamat": "Alamat ranting",
    #     "telepon": "",
    # },
]

AMAL_USAHA = [
    # bidang harus salah satu dari:
    # "pendidikan", "kesehatan", "sosial", "ekonomi"
    #
    # {
    #     "nama": "Nama amal usaha",
    #     "bidang": "pendidikan",
    #     "deskripsi": "Deskripsi",
    #     "alamat": "Alamat",
    # },
]

BERITA = [
    # Gunakan slug yang unik.
    # Status awal sebaiknya DRAF sampai konten diperiksa.
    #
    # {
    #     "judul": "Judul berita",
    #     "slug": "judul-berita",
    #     "ringkasan": "Ringkasan berita",
    #     "isi": "Isi berita",
    #     "status": "DRAF",
    # },
]

AGENDA = [
    # waktu_mulai harus berupa objek datetime Python.
    #
    # {
    #     "nama_kegiatan": "Nama kegiatan",
    #     "waktu_mulai": datetime(...),
    #     "tempat": "Lokasi kegiatan",
    #     "keterangan": "Keterangan kegiatan",
    # },
]

TAUTAN_TERKAIT = [
    # {
    #     "nama": "Nama organisasi",
    #     "url": "https://contoh.org",
    #     "urutan": 1,
    # },
]


class Command(BaseCommand):
    help = "Mengisi data awal website PCM secara aman dan idempotent."

    @transaction.atomic
    def handle(self, *args, **options):
        dibuat = {
            "profil": 0,
            "pimpinan": 0,
            "ranting": 0,
            "amal_usaha": 0,
            "berita": 0,
            "agenda": 0,
            "tautan": 0,
        }

        # --------------------------------------------------
        # 1. Profil Organisasi
        # ProfilOrganisasi menggunakan primary key = 1.
        # --------------------------------------------------
        if PROFIL["nama"] and PROFIL["nama_singkat"]:
            _, created = ProfilOrganisasi.objects.get_or_create(
                pk=1,
                defaults=PROFIL,
            )
            dibuat["profil"] += int(created)
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Profil dilewati: nama dan nama_singkat belum diisi."
                )
            )

        # --------------------------------------------------
        # 2. Pimpinan
        # --------------------------------------------------
        for data in PIMPINAN:
            _, created = Pimpinan.objects.get_or_create(
                nama=data["nama"],
                jabatan=data["jabatan"],
                periode=data.get("periode", "2022-2027"),
                defaults={
                    "foto": data.get("foto", ""),
                    "urutan": data.get("urutan", 0),
                },
            )
            dibuat["pimpinan"] += int(created)

        # --------------------------------------------------
        # 3. Ranting
        # --------------------------------------------------
        for data in RANTING:
            _, created = Ranting.objects.get_or_create(
                nama=data["nama"],
                defaults={
                    "ketua": data.get("ketua", ""),
                    "alamat": data.get("alamat", ""),
                    "telepon": data.get("telepon", ""),
                },
            )
            dibuat["ranting"] += int(created)

        # --------------------------------------------------
        # 4. Amal Usaha
        # --------------------------------------------------
        for data in AMAL_USAHA:
            _, created = AmalUsaha.objects.get_or_create(
                nama=data["nama"],
                defaults={
                    "bidang": data["bidang"],
                    "deskripsi": data.get("deskripsi", ""),
                    "alamat": data.get("alamat", ""),
                    "gambar": data.get("gambar", ""),
                },
            )
            dibuat["amal_usaha"] += int(created)

        # --------------------------------------------------
        # 5. Berita
        # --------------------------------------------------
        for data in BERITA:
            _, created = Berita.objects.get_or_create(
                slug=data["slug"],
                defaults={
                    "judul": data["judul"],
                    "ringkasan": data["ringkasan"],
                    "isi": data["isi"],
                    "status": data.get("status", "DRAF"),
                },
            )
            dibuat["berita"] += int(created)

        # --------------------------------------------------
        # 6. Agenda
        # --------------------------------------------------
        for data in AGENDA:
            _, created = Agenda.objects.get_or_create(
                nama_kegiatan=data["nama_kegiatan"],
                waktu_mulai=data["waktu_mulai"],
                defaults={
                    "tempat": data["tempat"],
                    "keterangan": data.get("keterangan", ""),
                },
            )
            dibuat["agenda"] += int(created)

        # --------------------------------------------------
        # 7. Tautan Terkait
        # --------------------------------------------------
        for data in TAUTAN_TERKAIT:
            _, created = TautanTerkait.objects.get_or_create(
                nama=data["nama"],
                defaults={
                    "url": data["url"],
                    "urutan": data.get("urutan", 0),
                },
            )
            dibuat["tautan"] += int(created)

        # --------------------------------------------------
        # Ringkasan hasil
        # --------------------------------------------------
        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS("Proses seed_pcm selesai.")
        )

        for nama, jumlah in dibuat.items():
            self.stdout.write(f"- {nama}: {jumlah} data baru")

        self.stdout.write(
            self.style.WARNING(
                "Dokumen dan PesanMasuk tidak diisi otomatis. "
                "Dokumen membutuhkan file asli, sedangkan PesanMasuk "
                "sebaiknya berasal dari formulir kontak pengunjung."
            )
        )
