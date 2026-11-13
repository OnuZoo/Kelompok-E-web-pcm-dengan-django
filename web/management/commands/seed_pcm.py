from datetime import datetime
from pathlib import Path
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from web.models import (
    ProfilOrganisasi,
    Pimpinan,
    Ranting,
    AmalUsaha,
    Berita,
    Agenda,
    TautanTerkait,
)

SEED_MEDIA = Path(__file__).resolve().parents[2] / "seed_media"


def lampirkan(objek, field, nama_file):
    """Salin gambar seed ke ImageField lewat storage; lewati jika file tidak ada."""
    sumber = SEED_MEDIA / nama_file
    if not nama_file or not sumber.exists():
        return
    with sumber.open("rb") as f:
        getattr(objek, field).save(sumber.name, File(f), save=True)


def wib(*args):
    """datetime dengan zona waktu (Asia/Jakarta dari settings)."""
    return timezone.make_aware(datetime(*args))

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
    "nama": "PIMPINAN CABANG MUHAMMADIYAH KECAMATAN BAKI ",
    "nama_singkat": "PCM BAKI",
    "tagline": "",
    "tentang": "",
    "sejarah": """
        I.	Masa Rintisan 1928 – 1940
        Pendiriaan Amal Usaha Pendidikan oleh Bapak Guru Parto Atmojo dari Kampung Sewu Surakarta bersama Bapak Lurah Waru Bapak Hadi Wardoyo

        II.	Berdirinya Group Muhammadiyah 1940 – 1945
        Berdiri Group Muhammadiyah Waru, yang menggabung dengan Ranting Muhammadiyah Kartasura.
        Kegiatan :
        1.	Rintisan Pendidikan Diniyah
        2.	Rintisan Kepanduan Hizbul wathon

        III.	Rintisan Ranting Muhammadiyah Waru 1945 – 1950
        Dirintis oleh bapak Carik Mulyadi dan bapak Lurah Hadi Wardoyo. Amal Usaha : 1. Diniyah Sore
        2. Kepanduan Hizbul wathon

        IV.	Berdirinya Ranting Muhammadiyah Waru 1950 – 1955
        Kegiatan dipimpin oleh bapak Carik Mulyadi Amal Usaha : 1. Diniyah
        2. Kepanduan Hizbul wathon dipimpin oleh bapak M. Iskandar dari Klaten

        V.	Ranting Muhammadiyah waru 1955 – 1960
        Amal Usaha :
        1.	Madrasah Diniyah sore
        2.	Pemuda-pemudi malam hari

        VI.	Berdirinya Cabang Muhammadiyah Waru 1960 – 1965
        Berdiri Cabang Muhammadiyah Waru Amal Usaha :
        1.	Madrasash Diniyah Muhammadiyah berkembang menjadi Madrasah Wajib Belajar Muhammadiyah Waru.
        Dana di dukung dari perusahaan Batik Sukowati Bekonang.
        2.	Gerakan kepanduan Hizbul Wathon
        
        VII.	Perubahan Cabang Muhammadiyah Waru menjadi Cabang Muhamadiyah Baki 1966 – 1970
        Berdirinya Cabang Muhammadiyah Baki di pimpin oleh :
        1.	Bapak Carik Mulyadi
        2.	Bapak Suciman Amal Usaha :
        1.	Madrasah Ibtidaiyah Muhammadiyah
        2.	PGA Muhammadiyah
        3.	Kepanduan Hizbul Wathon
        4.	Ranting Muhammadiyah

        VIII.	Periode Pimpinan Cabang Muhammadiyah Kecamatan Baki 1970 – 1975 : Bapak Mulyadi
        1975 – 1980 : Bapak Mulyadi
        1980 – 1985 : Bapak H. Hadi Suwito 1985 – 1990 : Bapak H. Hadi Suwito 1990 – 1995 : Bapak H. Umar Suwito 1995 – 2000 : Bapak H. Djumali
        2000 – 2005 : Bapak Drs. H. Amir Hasan
        2005 – 2010 : Bapak Drs. M. Syaiun, M.M / H. Harsono Amri, BA 2010 – 2015 : Bapak H. Harsono Amri, BA
        2015 – 2020 : Bapak Drs. H. Ahyar Anas, S.H, M.M 2023- sekarang : H. Muhammad Mahmudi, S.Pd

        IX.	Kantoran Cabang Muhammadiyah Kecamatan Baki
        1.	Di rintis mulai tahuin 1966
        2.	Bapak H. Harsono Amri, BA mulai ikut, pada bulan Maret 1970 dengan tugas mencatat
        3.	Kantoran dilaksanakan :
        1.	Setiap malam rabu
        2.	Tempat dari rumah ke rumah
        3.	Jam 20.00 – 22.00 (Bakda Isya’)
        4.	Daftar Anggota Kantoran PCM. Baki
        1.	Bapak Lurah Hadi Wardoyo
        2.	Bapak Carik Mulyadi
        3.	Bapak Bayan M. Iskandar
        4.	Bapak Mursidi Afandi
        5.	Bapak H. Mardani
        6.	Bapak H. Djumali
        7.	Bapak Pringgo Puspito
        8.	Bapak H. Hadi Suwito
        9.	Bapak H. Umar Suwito
        10.	Bapak Badrun Fatnanto
        11.	Bapak Marhaban Fuadi
        12.	Bapak Abdullah Daim Sukendro
        13.	Bapak Drs. H. Al Fajri
        14.	Bapak H. Jamaludin
        15.	Bapak Wardani
        
        16.	Bapak Drs. H. Amir Hasan
        17.	Bapak H. Jaenuri
        18.	Bapak H. Hasyim Asngari, S.Ag
        19.	Bapak H. Harsono Amri, BA
        """,
    "visi": "",
    "misi": "",
    "alamat_sekretariat": "Jagan RT 01 RW 07 Waru Baki Sukoharjo",
    "telepon": "08179476737",
    "email": "",
    "jumlah_anggota_ktam": 29,
    "gambar_hero": "gambar_hero.jpeg",
}

PIMPINAN = [
    {
        "nama": "H. MUHAMMAD MAHMUDI, S.Pd",
        "jabatan": "Ketua",
        "periode": "2022-2027",
        "foto": "ketua.jpeg",
        "urutan": 1
    },
    
    {
        "nama": "MUHAMMAD NURHASAN ALFATHONI, S.S, M.Pd",
        "jabatan": "Wakil Ketua",
        "periode": "2022-2027",
        "foto": "wakil-ketua1.jpeg",
        "urutan": 2
    },
    
    {
        "nama": "Dr. H. MUCHAMMAD IKSAN, SH",
        "jabatan": "Wakil Ketua",
        "periode": "2022-2027",
        "foto": "wakil-ketua2.jpeg",
        "urutan": 3
    },
    
    {
        "nama": "Drs. H. SAHONO, M.Pd",
        "jabatan": "Wakil Ketua",
        "periode": "2022-2027",
        "foto": "wakil-ketua3.jpeg",
        "urutan": 4
    },
    
]

RANTING = [
    {
        "nama": "Ranting 1",
        "ketua": "Ketua Ranting 1",
        "alamat": "Alamat Ranting 1",
        "telepon": "08123456789"
    }
]

AMAL_USAHA = [
    {
        "nama": "Amal Usaha 1",
        "bidang": "pendidikan",
        "deskripsi": "Deskripsi Amal Usaha 1",
        "alamat": "Alamat Amal Usaha 1",
        "gambar": "amal_usaha_1.jpeg"
    }
]

BERITA = [
    #harus mengisi minimal 6
    {
        "judul": "Berita 1",
        "slug": "berita-1",
        "ringkasan": "Ringkasan Berita 1",
        "isi": "Isi Berita 1",
        "gambar_sampul": "berita_1.jpeg",
        "tanggal_terbit": wib(2026, 10, 5, 9, 0),
        "status": "terbit"
    }
]

AGENDA = [
    {
        "nama_kegiatan": "Agenda 1",
        "waktu_mulai": wib(2026, 12, 1, 10, 0),
        "tempat": "Tempat Agenda 1",
        "keterangan": "Keterangan Agenda 1"
    }
]

TAUTAN_TERKAIT = [
    {"nama": "PDM Sukoharjo", "url": "https://pdmsukoharjo.or.id/", "urutan": 1},
    {"nama": "PWM Jawa Tengah", "url": "https://muhammadiyahjateng.or.id/", "urutan": 2},
    {"nama": "PP Muhammadiyah", "url": "https://muhammadiyah.or.id", "urutan": 3},
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
            isi = {k: v for k, v in PROFIL.items() if k != "gambar_hero"}
            profil, created = ProfilOrganisasi.objects.get_or_create(
                pk=1,
                defaults=isi,
            )
            if created:
                lampirkan(profil, "gambar_hero", PROFIL["gambar_hero"])
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
            obj, created = Pimpinan.objects.get_or_create(
                nama=data["nama"],
                jabatan=data["jabatan"],
                periode=data.get("periode", "2022-2027"),
                defaults={"urutan": data.get("urutan", 0)},
            )
            if created:
                lampirkan(obj, "foto", data.get("foto", ""))
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
            obj, created = AmalUsaha.objects.get_or_create(
                nama=data["nama"],
                defaults={
                    "bidang": data["bidang"],
                    "deskripsi": data.get("deskripsi", ""),
                    "alamat": data.get("alamat", ""),
                },
            )
            if created:
                lampirkan(obj, "gambar", data.get("gambar", ""))
            dibuat["amal_usaha"] += int(created)

        # --------------------------------------------------
        # 5. Berita
        # --------------------------------------------------
        for data in BERITA:
            obj, created = Berita.objects.get_or_create(
                slug=data["slug"],
                defaults={
                    "judul": data["judul"],
                    "ringkasan": data["ringkasan"],
                    "isi": data["isi"],
                    "tanggal_terbit": data.get("tanggal_terbit"),
                    "status": data.get("status", "draf"),
                },
            )
            if created:
                lampirkan(obj, "gambar_sampul", data.get("gambar_sampul", ""))
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
