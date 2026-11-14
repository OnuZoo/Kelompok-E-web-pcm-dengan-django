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
    Dokumen,
)

SEED_MEDIA = Path(__file__).resolve().parents[2] / "seed_media"
JAM_AGENDA = (20, 0)


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

# ==========================================================
# DATA SEED
# Isi bagian ini menggunakan data PCM yang sudah diverifikasi.
# Jangan mengisi dengan data perkiraan atau data fiktif.
# ==========================================================

PROFIL = {
    "nama": "PIMPINAN CABANG MUHAMMADIYAH KECAMATAN BAKI ",
    "nama_singkat": "PCM BAKI",
    "tagline": "Bersama Satukan Bangsa",
    "tentang": (
        "Pimpinan Cabang Muhammadiyah (PCM) Baki merupakan organisasi tingkat "
        "kecamatan di bawah naungan Pimpinan Daerah Muhammadiyah (PDM) Kabupaten "
        "Sukoharjo yang berfokus pada gerakan dakwah Islam amar ma'ruf nahi munkar "
        "dan tajdid. Berkedudukan di Desa Waru, Kecamatan Baki, PCM Baki hadir "
        "untuk mengoordinasikan berbagai Pimpinan Ranting Muhammadiyah (PRM) di "
        "tingkat desa serta mengelola Amal Usaha Muhammadiyah (AUM) di bidang "
        "pendidikan, kesehatan, dan sosial kemasyarakatan. Dengan semangat "
        "mencerahkan dan memajukan umat, PCM Baki berkomitmen memberikan kontribusi "
        "nyata bagi kesejahteraan masyarakat di wilayah Kecamatan Baki dan sekitarnya."
    ),
    "sejarah": """
I. Masa Rintisan (1928–1940)
Pendirian amal usaha pendidikan oleh Bapak Guru Parto Atmojo dari Kampung Sewu, Surakarta, bersama Bapak Lurah Waru, Bapak Hadi Wardoyo.

II. Berdirinya Group Muhammadiyah (1940–1945)
Berdiri Group Muhammadiyah Waru, yang bergabung dengan Ranting Muhammadiyah Kartasura.
Kegiatan:
- Rintisan Pendidikan Diniyah
- Rintisan Kepanduan Hizbul Wathan

III. Rintisan Ranting Muhammadiyah Waru (1945–1950)
Dirintis oleh Bapak Carik Mulyadi dan Bapak Lurah Hadi Wardoyo.
Amal usaha:
- Diniyah Sore
- Kepanduan Hizbul Wathan

IV. Berdirinya Ranting Muhammadiyah Waru (1950–1955)
Kegiatan dipimpin oleh Bapak Carik Mulyadi.
Amal usaha:
- Diniyah
- Kepanduan Hizbul Wathan, dipimpin oleh Bapak M. Iskandar dari Klaten

V. Ranting Muhammadiyah Waru (1955–1960)
Amal usaha:
- Madrasah Diniyah Sore
- Pemuda-pemudi malam hari

VI. Berdirinya Cabang Muhammadiyah Waru (1960–1965)
Berdiri Cabang Muhammadiyah Waru.
Amal usaha:
- Madrasah Diniyah Muhammadiyah berkembang menjadi Madrasah Wajib Belajar Muhammadiyah Waru, didukung dana dari perusahaan Batik Sukowati Bekonang
- Gerakan Kepanduan Hizbul Wathan

VII. Cabang Muhammadiyah Waru Menjadi Cabang Muhammadiyah Baki (1966–1970)
Berdiri Cabang Muhammadiyah Baki, dipimpin oleh:
- Bapak Carik Mulyadi
- Bapak Suciman
Amal usaha:
- Madrasah Ibtidaiyah Muhammadiyah
- PGA Muhammadiyah
- Kepanduan Hizbul Wathan
- Ranting Muhammadiyah

VIII. Periode Pimpinan Cabang Muhammadiyah Kecamatan Baki
- 1970–1975: Bapak Mulyadi
- 1975–1980: Bapak Mulyadi
- 1980–1985: Bapak H. Hadi Suwito
- 1985–1990: Bapak H. Hadi Suwito
- 1990–1995: Bapak H. Umar Suwito
- 1995–2000: Bapak H. Djumali
- 2000–2005: Bapak Drs. H. Amir Hasan
- 2005–2010: Bapak Drs. M. Syaiun, M.M / H. Harsono Amri, BA
- 2010–2015: Bapak H. Harsono Amri, BA
- 2015–2020: Bapak Drs. H. Ahyar Anas, S.H, M.M
- 2023–sekarang: H. Muhammad Mahmudi, S.Pd

IX. Kantoran Cabang Muhammadiyah Kecamatan Baki
- Dirintis mulai tahun 1966
- Bapak H. Harsono Amri, BA mulai ikut pada Maret 1970 dengan tugas mencatat
Kantoran dilaksanakan:
- Setiap malam Rabu
- Tempat: dari rumah ke rumah
- Pukul 20.00–22.00 (bakda Isya)
Daftar anggota kantoran PCM Baki:
- Bapak Lurah Hadi Wardoyo
- Bapak Carik Mulyadi
- Bapak Bayan M. Iskandar
- Bapak Mursidi Afandi
- Bapak H. Mardani
- Bapak H. Djumali
- Bapak Pringgo Puspito
- Bapak H. Hadi Suwito
- Bapak H. Umar Suwito
- Bapak Badrun Fatnanto
- Bapak Marhaban Fuadi
- Bapak Abdullah Daim Sukendro
- Bapak Drs. H. Al Fajri
- Bapak H. Jamaludin
- Bapak Wardani
- Bapak Drs. H. Amir Hasan
- Bapak H. Jaenuri
- Bapak H. Hasyim Asngari, S.Ag
- Bapak H. Harsono Amri, BA
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
        "foto": "ketua.jpg",
        "urutan": 1
    },
    
    {
        "nama": "MUHAMMAD NURHASAN ALFATHONI, S.S, M.Pd",
        "jabatan": "Wakil Ketua 1",
        "periode": "2022-2027",
        "foto": "wakil_ketua1.jpg",
        "urutan": 2
    },
    
    {
        "nama": "Dr. H. MUCHAMMAD IKSAN, SH",
        "jabatan": "Wakil Ketua 2",
        "periode": "2022-2027",
        "foto": "wakil_ketua2.jpg",
        "urutan": 3
    },
    
    {
        "nama": "Drs. H. SAHONO, M.Pd",
        "jabatan": "Wakil Ketua 3",
        "periode": "2022-2027",
        "foto": "wakil_ketua3.jpg",
        "urutan": 4
    },
    
    {
        "nama": "HARI YUDANTO, SE",
        "jabatan": "Wakil Ketua 4",
        "periode": "2022-2027",
        "foto": "wakil_ketua4.jpg",
        "urutan": 5
    },
    
    {
        "nama": "H. SARTONO, S. Ag. M.Si",
        "jabatan": "Wakil Ketua 5",
        "periode": "2022-2027",
        "foto": "wakil_ketua5.jpg",
        "urutan": 6
    },
    
    {
        "nama": "SUMIATUN, S.Pd",
        "jabatan": "Wakil Ketua 6",
        "periode": "2022-2027",
        "foto": "wakil_ketua6.jpg",
        "urutan": 7
    },
    
    {
        "nama": "IBNU HAMBALI, S.Pd., M.Si",
        "jabatan": "Sekretaris",
        "periode": "2022-2027",
        "foto": "sekretaris.jpg",
        "urutan": 8
    },
    
    {
        "nama": "MUCHAMMAD RIDUWAN",
        "jabatan": "Wakil Sekretaris",
        "periode": "2022-2027",
        "foto": "wakil_sekretaris.jpg",
        "urutan": 9
    },
    
    {
        "nama": "Drs. SARTONO",
        "jabatan": "Bendahara",
        "periode": "2022-2027",
        "foto": "bendahara.jpg",
        "urutan": 10
    },
    
    {
        "nama": "FUAD HAMDAN, S.PdI",
        "jabatan": "Wakil Bendahara",
        "periode": "2022-2027",
        "foto": "wakil_bendahara.jpg",
        "urutan": 11
    },
]

RANTING = [
    {
        "nama": "Ranting Muhammadiyah Waru 2",
        "ketua": "H. Husnan Arifin, B.A.",
        "alamat": "Waru, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Waru 3",
        "ketua": "Supriyanto",
        "alamat": "Waru, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Waru 4",
        "ketua": "H. Nur Sabiyanto, M.Pd.",
        "alamat": "Waru, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Waru 5",
        "ketua": "Suryanto",
        "alamat": "Waru, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Purbayan",
        "ketua": "Dr. MUCHAMMAD IKSAN",
        "alamat": "Purbayan, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Gentan",
        "ketua": "H. Zaenal Abidin Ahmad, S.E.",
        "alamat": "Gentan, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Jetis",
        "ketua": "Iwan Junaidi",
        "alamat": "Jetis, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    },
    
    {
        "nama": "Ranting Muhammadiyah Duwet",
        "ketua": "Eko Sri Atmaja",
        "alamat": "Duwet, Baki, Sukoharjo, Jawa Tengah 57556",
        "telepon": "Belum tersedia"
    }
]

AMAL_USAHA = [
    {
        "nama": "MTs Muhammadiyah Waru",
        "bidang": "pendidikan",
        "deskripsi": """
        MTs Muhammadiyah Waru Baki merupakan lembaga pendidikan Islam tingkat menengah pertama yang berkomitmen
        menyelenggarakan pendidikan dengan mengintegrasikan ilmu pengetahuan umum dan nilai-nilai keislaman.
        Lembaga ini berperan dalam membentuk peserta didik yang berpengetahuan, berakhlak mulia, dan memiliki landasan keagamaan yang kuat.
        """,
        "alamat": "CQ79+45H, Jl. Waru-Gentan, Dusun III, Waru, Kec. Baki, Kabupaten Sukoharjo, Jawa Tengah 57556",
        "gambar": "mts_muhammadiyah_waru.png"
    },
    
    {
        "nama": "MI Muhammadiyah Waru",
        "bidang": "pendidikan",
        "deskripsi": """
        MI Muhammadiyah Waru Baki merupakan lembaga pendidikan dasar Islam yang berperan dalam memberikan pendidikan
        dan pembinaan sejak usia dini. Melalui pembelajaran yang menggabungkan pengetahuan umum dan pendidikan agama Islam,
        lembaga ini berupaya membangun fondasi ilmu pengetahuan, karakter, serta akhlak peserta didik.
        """,
        "alamat": "Jl. Waru-Gentan, Dusun III, Waru, Kec. Baki, Kabupaten Sukoharjo, Jawa Tengah 57556",
        "gambar": "mi_muhammadiyah_waru.png"
    },
    
    {
        "nama": "MI Muhammadiyah Siwal",
        "bidang": "pendidikan",
        "deskripsi": """
        MI Muhammadiyah Siwal Baki merupakan salah satu lembaga pendidikan dasar Muhammadiyah di wilayah Baki
        yang berfokus pada pengembangan pendidikan berbasis nilai-nilai Islam. Keberadaannya menjadi bagian
        dari upaya Muhammadiyah dalam memperluas akses pendidikan serta membentuk generasi yang berilmu, mandiri, dan berkarakter Islami.
        """,
        "alamat": "Jalan Blotan No.2, Dusun II, Siwal, Kec. Baki, Kabupaten Sukoharjo, Jawa Tengah 57556",
        "gambar": "mi_muhammadiyah_siwal.png"
    },
    
    {
        "nama": "MI Muhammadiyah Gondang",
        "bidang": "pendidikan",
        "deskripsi": """
        MI Muhammadiyah Gondang Baki merupakan lembaga pendidikan tingkat dasar yang turut berkontribusi dalam penyelenggaraan pendidikan
        Islam di lingkungan masyarakat. Lembaga ini berperan dalam membekali peserta didik dengan pengetahuan, keterampilan dasar,
        serta nilai-nilai keislaman sebagai bekal untuk melanjutkan pendidikan ke jenjang berikutnya.
        """,
        "alamat": "Gondang No.6, Rw. VI, Bakipandeyan, Kec. Baki, Kabupaten Sukoharjo, Jawa Tengah 57556",
        "gambar": "mi_muhammadiyah_gondang.png"
    },
    
    {
        "nama": "MI Muhammadiyah Syafaat Jetis",
        "bidang": "pendidikan",
        "deskripsi": """
        MI Muhammadiyah Syafaat Jetis Baki merupakan lembaga pendidikan dasar Muhammadiyah yang berkomitmen memberikan
        pendidikan dengan berlandaskan ajaran Islam. Lembaga ini menjadi salah satu sarana dakwah Muhammadiyah
        melalui pendidikan, dengan tujuan membentuk peserta didik yang memiliki pengetahuan, kepribadian baik, serta pemahaman agama yang kuat.
        """,
        "alamat": "Daleman RT 01/04, Rw. IV, Jetis, Baki, Sukoharjo Regency, Central Java 57556",
        "gambar": "mi_muhammadiyah_syafaat_jetis.png"
    },
    
    {
        "nama": "Satuan Pelayanan pemenuhan Gizi (SPPG) PCM Baki",
        "bidang": "ekonomi",
        "deskripsi": """
        Satuan Pelayanan pemenuhan Gizi (SPPG) PCM Baki merupakan unit layanan yang bertugas dalam menyelenggarakan
        program pemenuhan gizi bagi anggota PCM dan masyarakat sekitar. Program ini berfokus pada peningkatan kesehatan
        dan nutrisi masyarakat, terutama anak-anak dan ibu hamil.
        """,
        "alamat": "Daleman RT 01/04, Rw. IV, Jetis, Baki, Sukoharjo Regency, Central Java 57556",
        "gambar": "sppg_pcm_baki.png"
    },
]

BERITA = [
    {
        "judul": "Jalan Sehat dan Pengajian Milad Muhammadiyah ke-114 Meriahkan Halaman MIM Waru Baki",
        "slug": "jalan-sehat-dan-pengajian-milad-muhammadiyah-ke-114",
        "ringkasan": (
            "Pimpinan Cabang Muhammadiyah (PCM) Baki menggelar Jalan Sehat dan Pengajian "
            "dalam rangka Milad Muhammadiyah ke-114 pada Ahad, 8 November 2026, "
            "bertempat di Halaman MIM Waru Baki dan terbuka untuk umum."
        ),
        "isi": (
            "Pimpinan Cabang Muhammadiyah (PCM) Baki menyelenggarakan Jalan Sehat dan "
            "Pengajian dalam rangka Milad Muhammadiyah ke-114 dengan tema Tanwir dan "
            "Milad ke-114 Muhammadiyah, \"Bersama Satukan Bangsa\".\n\n"
            "Kegiatan dilaksanakan pada Ahad, 28 Jumadilawal 1448 H bertepatan dengan "
            "8 November 2026 M, mulai pukul 06.30 WIB hingga selesai, di Halaman MIM "
            "Waru Baki. Acara ini terbuka untuk umum sehingga warga dari berbagai "
            "kalangan dapat ikut serta.\n\n"
            "Sebagai mubaligh, panitia menghadirkan H. Agus Tursilo Wisanto, S.H, S.P, M.Pd. "
            "Selain jalan sehat dan pengajian, peserta mendapatkan sejumlah fasilitas, yaitu "
            "voucher belanja di stand bazar, bazar pakaian pantas pakai, bazar UMKM, serta "
            "doorprize menarik.\n\n"
            "Bagi pelaku usaha yang ingin membuka stand pada Bazar UMKM, pendaftaran dapat "
            "menghubungi Eko Tri Atmojo (085799127427) atau Novrita (085293578933). "
            "Informasi umum kegiatan dapat ditanyakan kepada MN Fathoni (085725476111) "
            "atau Muh Ridwan (081548542155).\n\n"
            "Kegiatan ini didukung oleh berbagai pihak, antara lain amal usaha, organisasi "
            "otonom, dan sponsor yang tercantum pada poster kegiatan."
        ),
        "gambar_sampul": "berita_1.jpeg",
        "tanggal_terbit": wib(2026, 10, 20, 9, 0),
        "status": "terbit",
    },
    {
        "judul": "Bazar Pakaian Pantas Pakai Milad Muhammadiyah ke-114 Diserbu Warga",
        "slug": "bazar-pakaian-pantas-pakai-milad-muhammadiyah-ke-114",
        "ringkasan": (
            "Bazar pakaian pantas pakai menjadi salah satu daya tarik rangkaian Milad "
            "Muhammadiyah ke-114 di Halaman MIM Waru Baki."
        ),
        "isi": (
            "Salah satu fasilitas yang disiapkan panitia Milad Muhammadiyah ke-114 PCM Baki "
            "adalah Bazar Pakaian Pantas Pakai. Sejak pagi, meja-meja bazar sudah dipenuhi "
            "tumpukan pakaian berbagai warna yang dikemas rapi.\n\n"
            "Para petugas yang mengenakan jilbab kuning dan tanda pengenal melayani warga "
            "yang datang memilih pakaian. Pakaian layak pakai dengan harga terjangkau ini "
            "diharapkan dapat membantu kebutuhan masyarakat sekaligus menumbuhkan semangat "
            "berbagi.\n\n"
            "Antusiasme warga terlihat sejak awal acara. Bazar ini berlangsung bersamaan "
            "dengan jalan sehat, pengajian, dan Bazar UMKM di lokasi yang sama."
        ),
        "gambar_sampul": "berita_2.jpeg",
        "tanggal_terbit": wib(2026, 11, 8, 14, 0),
        "status": "terbit",
    },
    {
        "judul": "Pemeriksaan Kesehatan Gratis Warnai Milad Muhammadiyah ke-114 di Baki",
        "slug": "pemeriksaan-kesehatan-gratis-milad-muhammadiyah-ke-114",
        "ringkasan": (
            "Tenaga kesehatan melayani pemeriksaan dan pembagian obat bagi peserta, "
            "termasuk anggota Kokam, di sela kegiatan Milad Muhammadiyah ke-114."
        ),
        "isi": (
            "Di sela rangkaian Milad Muhammadiyah ke-114, tenaga kesehatan melayani "
            "pemeriksaan kesehatan dan pembagian obat bagi peserta kegiatan. Layanan "
            "ditempatkan di selasar gedung MIM Waru Baki agar nyaman dan mudah dijangkau.\n\n"
            "Sejumlah anggota Kokam (Komando Kesiapsiagaan) berseragam loreng dan baret merah "
            "tampak antre memperoleh layanan, sementara para petugas menyiapkan obat dan "
            "mencatat hasil pemeriksaan.\n\n"
            "Kehadiran layanan kesehatan ini menunjukkan bahwa Milad tidak hanya diisi "
            "kegiatan keagamaan dan bazar, tetapi juga kepedulian terhadap kesehatan warga."
        ),
        "gambar_sampul": "berita_3.jpeg",
        "tanggal_terbit": wib(2026, 11, 9, 9, 0),
        "status": "terbit",
    },
    {
        "judul": "Ratusan Jamaah Khusyuk Ikuti Pengajian Milad Muhammadiyah ke-114",
        "slug": "ratusan-jamaah-ikuti-pengajian-milad-muhammadiyah-ke-114",
        "ringkasan": (
            "Ratusan jamaah memadati area pengajian di Halaman MIM Waru Baki dalam "
            "rangkaian Milad Muhammadiyah ke-114, Ahad, 8 November 2026."
        ),
        "isi": (
            "Setelah jalan sehat, ratusan jamaah dari berbagai kalangan, mulai dari ibu-ibu, "
            "remaja, hingga anak-anak, duduk lesehan di bawah tenda di Halaman MIM Waru Baki "
            "untuk mengikuti pengajian Milad Muhammadiyah ke-114 pada Ahad, 8 November 2026.\n\n"
            "Mubaligh menyampaikan tausiyah dengan penuh semangat, dan jamaah menyimak dengan "
            "khusyuk. Suasana kebersamaan terasa kuat, sejalan dengan tema Milad "
            "\"Bersama Satukan Bangsa\".\n\n"
            "Pengajian ini menjadi puncak kebersamaan warga Muhammadiyah dan masyarakat "
            "sekitar dalam memperingati usia ke-114 persyarikatan."
        ),
        "gambar_sampul": "berita_4.jpeg",
        "tanggal_terbit": wib(2026, 11, 8, 16, 0),
        "status": "terbit",
    },
        {
        "judul": "PCM Baki Gelar Rakercab dan Pelatihan SatuMu untuk Perkuat Digitalisasi Data",
        "slug": "rakercab-dan-pelatihan-satumu-pcm-baki",
        "ringkasan": (
            "PCM Baki menggelar Rapat Kerja Cabang yang dirangkaikan dengan pelatihan SatuMu "
            "di Tawangmangu, guna menyelaraskan program kerja dan memperkuat pengelolaan "
            "data anggota berbasis digital."
        ),
        "isi": (
            "Pimpinan Cabang Muhammadiyah (PCM) Baki, Sukoharjo, menyelenggarakan Rapat Kerja "
            "Cabang (Rakercab) yang dirangkaikan dengan pelatihan SatuMu di Villa Tawangmangu, "
            "mulai Sabtu, 18 April 2026. Kegiatan berlangsung selama dua hari.\n\n"
            "Peserta berasal dari pimpinan ranting se-Cabang Baki, dengan setiap ranting "
            "mengirimkan dua perwakilan. Rakercab ini menjadi momentum untuk memperkuat "
            "program kerja organisasi sekaligus meningkatkan kapasitas kader, terutama dalam "
            "pengelolaan data secara digital.\n\n"
            "Pada sesi pelatihan, materi disampaikan oleh Dimas Sanjaya dari tim SatuMu "
            "Pimpinan Daerah Muhammadiyah Sukoharjo. Ia menjelaskan bahwa SatuMu adalah sistem "
            "yang dirancang untuk menunjang tertib administrasi serta mengintegrasikan data "
            "anggota Muhammadiyah secara digital. Menurutnya, dengan sistem ini data anggota "
            "dapat dikelola lebih sistematis, akurat, dan terpadu.\n\n"
            "Ketua PCM Baki, M. Mahmudi, menyampaikan bahwa Rakercab bukan sekadar forum "
            "evaluasi, tetapi juga wadah merumuskan langkah strategis ke depan, menyelaraskan "
            "program kerja antarranting, dan memperkuat sinergi dakwah di tingkat cabang. Ia "
            "juga menekankan pentingnya penerapan SatuMu di setiap ranting sebagai bagian dari "
            "transformasi organisasi yang lebih modern dan berbasis data.\n\n"
            "Melalui kegiatan ini, para peserta diharapkan dapat menerapkan hasil Rakercab dan "
            "pelatihan SatuMu di wilayah masing-masing, sehingga organisasi semakin "
            "profesional, tertata, dan berkemajuan.\n\n"
            "Sumber: Suara 'Aisyiyah (suaraaisyiyah.id)."
        ),
        "gambar_sampul": "berita_5.jpg",
        "tanggal_terbit": wib(2026, 4, 19, 10, 0),
        "status": "terbit",
    },
        {
        "judul": "SPPG PCM Baki Siap Beroperasi, Tinggal Menunggu Sertifikat Laik Hygiene dan Sanitasi",
        "slug": "sppg-pcm-baki-siap-beroperasi-menunggu-slhs",
        "ringkasan": (
            "Dapur SPPG milik PCM Baki di Desa Gedongan sudah siap mendukung Program Makan "
            "Bergizi Gratis dan hanya tinggal menunggu Sertifikat Laik Hygiene dan Sanitasi "
            "(SLHS) dari Dinas Kesehatan Kabupaten Sukoharjo."
        ),
        "isi": (
            "Dapur Satuan Pelayanan Pemenuhan Gizi (SPPG) milik Pimpinan Cabang Muhammadiyah "
            "(PCM) Baki dinyatakan siap beroperasi untuk mendukung Program Makan Bergizi Gratis "
            "(MBG). Seluruh persiapan, mulai dari infrastruktur, tenaga kerja, hingga armada "
            "distribusi, telah rampung. Operasional resmi tinggal menunggu Sertifikat Laik "
            "Hygiene dan Sanitasi (SLHS) dari Dinas Kesehatan Kabupaten Sukoharjo.\n\n"
            "Koordinator pembangunan SPPG PCM Baki, Sahono, menjelaskan bahwa dapur yang berlokasi "
            "di Dukuh Turusan, Desa Gedongan, Kecamatan Baki ini dibangun dengan cepat sejak "
            "proposal diajukan ke Badan Gizi Nasional (BGN) pada pertengahan Juli. Waktu "
            "pembangunan yang diberikan adalah 45 hari, dan pada akhir Agustus bangunan telah "
            "selesai 100 persen. Setelah itu, pengurus melanjutkan pengadaan peralatan dapur "
            "dan dua mobil distribusi.\n\n"
            "Pada awal September, BGN menunjuk seorang ASN sebagai Kepala SPPG PCM Baki, "
            "didampingi seorang akuntan dan seorang ahli gizi berstatus PPPK. Dapur ini akan "
            "dijalankan oleh 47 karyawan yang direkrut sesuai juknis BGN dan terbagi dalam "
            "beberapa divisi, yaitu persiapan masak, produksi, pengemasan, distribusi, dan "
            "kebersihan. Meski demikian, SPPG masih menunggu transfer anggaran dari negara dan "
            "penerbitan SLHS. Sahono menyebut pihaknya sudah memperoleh virtual account dari "
            "BGN, tetapi belum dapat menjalankan distribusi resmi.\n\n"
            "SPPG ini akan melayani 3.533 penerima manfaat, yaitu siswa PAUD, RA, BA, dan TK di "
            "17 lembaga (781 siswa), SD/MI di 11 lembaga (1.894 siswa), SMP/MTs (194 siswa), "
            "serta SMA/MA (100 siswa). Layanan juga menjangkau kelompok rentan, yakni ibu hamil, "
            "ibu menyusui, dan balita di Desa Gedongan (228 orang) dan Desa Jetis (336 orang).\n\n"
            "Sahono menegaskan bahwa pengelola menjalankan amanah ini dengan sungguh-sungguh, "
            "sebagai tanggung jawab dunia dan akhirat. Para karyawan pun mengikuti pengajian "
            "setiap pekan keempat agar bekerja dengan hati dan diniatkan sebagai ibadah.\n\n"
            "Ketua PDM Sukoharjo, H. Djumari, mengapresiasi PCM Baki yang dinilai cepat dan tepat "
            "dalam membangun SPPG. Ia mengingatkan agar kualitas layanan dan makanan tetap "
            "dijaga sesuai standar BGN karena program ini menyangkut masa depan generasi bangsa. "
            "Ia juga menegaskan bahwa SPPG berdiri di atas lahan wakaf Muhammadiyah, sesuai "
            "ketentuan PP Muhammadiyah.\n\n"
            "Saat ini Muhammadiyah di Kabupaten Sukoharjo memiliki 9 dapur SPPG, dan baru tiga "
            "yang beroperasi, yakni di Polokarto, Nguter, dan PCM Baki yang segera menyusul "
            "setelah administrasi selesai. Acara peresmian dihadiri para kepala sekolah penerima "
            "manfaat serta unsur pemerintahan kecamatan, yaitu Camat Baki, Danramil, dan "
            "Kapolsek, sebagai bentuk dukungan lintas sektor.\n\n"
            "Sumber: iNews Sragen (sragen.inews.id)."
        ),
        "gambar_sampul": "berita_6.jpg",
        "tanggal_terbit": wib(2025, 10, 1, 15, 0),
        "status": "terbit",
    },
        {
        "judul": "Pengukuhan dan Idiopolitor Pimpinan Cabang Muhammadiyah dan 'Aisyiyah Baki Digelar",
        "slug": "pengukuhan-dan-idiopolitor-pcm-pca-baki",
        "ringkasan": (
            "Pimpinan Cabang Muhammadiyah dan 'Aisyiyah Baki, Sukoharjo, mengikuti kegiatan "
            "pengukuhan dan Idiopolitor (Ideologi dan Politik Organisasi) pada Sabtu, "
            "18 April 2026."
        ),
        "isi": (
            "Pimpinan Cabang Muhammadiyah dan 'Aisyiyah Baki, Sukoharjo, menggelar kegiatan "
            "Pengukuhan dan Idiopolitor pada Sabtu, 18 April 2026.\n\n"
            "Pengukuhan merupakan tahapan penting dalam pelaksanaan amanah organisasi, karena "
            "menandai dimulainya tugas dan tanggung jawab para pimpinan dalam menjalankan "
            "roda persyarikatan. Sementara itu, Idiopolitor atau Ideologi dan Politik "
            "Organisasi adalah materi pembekalan agar para pimpinan memahami ideologi "
            "Muhammadiyah serta sikap organisasi dalam kehidupan berbangsa dan bernegara.\n\n"
            "Dalam sesi foto bersama, para pimpinan tampak kompak mengenakan batik hijau khas "
            "Muhammadiyah, lengkap dengan peci hitam, berdiri di depan spanduk kegiatan. "
            "Suasana acara berlangsung khidmat dan penuh kebersamaan.\n\n"
            "Melalui kegiatan ini, para pimpinan diharapkan semakin memahami arah gerak "
            "organisasi dan siap menjalankan amanah dengan sebaik-baiknya demi kemajuan "
            "dakwah Muhammadiyah dan 'Aisyiyah di Cabang Baki."
        ),
        "gambar_sampul": "berita_7.jpeg",
        "tanggal_terbit": wib(2026, 4, 18, 20, 0),
        "status": "terbit",
    },
]

JADWAL_PCM = [
    (2026, 1, 6, "Rapat Pengurus Harian PCM", "Rumah Pengurus Harian", "Sekretaris PCM"),
    (2026, 1, 13, "Kajian HPT", "PRM Purbayan", "Ketua PRM"),
    (2026, 1, 20, "Rapat Pengurus Lengkap PCM", "MTs Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 1, 27, "Kajian HPT", "PRM Waru 1", "Ketua PRM"),
    (2026, 2, 3, "Rapat Pengurus Harian PCM", "Rumah Bp. Muh. Mahmudi", "Sekretaris PCM"),
    (2026, 2, 10, "Kajian HPT", "PRM Ngrombo", "Ketua PRM"),
    (2026, 2, 17, "Rapat Pengurus Lengkap PCM", "MI Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 3, 31, "Halal-bi-halal", "Belum tersedia", ""),
    (2026, 4, 7, "Rapat Pengurus Harian PCM", "Rumah Bp. Muhammad Ikhsan", "Sekretaris PCM"),
    (2026, 4, 14, "Kajian HPT", "PRM Waru 2", "Ketua PRM"),
    (2026, 4, 21, "Rapat Pengurus Lengkap PCM", "MTs Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 4, 28, "Kajian HPT", "PRM Gentan", "Ketua PRM"),
    (2026, 5, 5, "Rapat Pengurus Harian PCM", "Rumah Bp. MN Al Fathoni", "Sekretaris PCM"),
    (2026, 5, 12, "Kajian HPT", "PRM Waru 3", "Ketua PRM"),
    (2026, 5, 19, "Rapat Pengurus Lengkap PCM", "MI Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 5, 26, "Kajian HPT", "PRM Gedongan", "Ketua PRM"),
    (2026, 6, 2, "Rapat Pengurus Harian PCM", "Rumah Bp. Sartono (Duwet)", "Sekretaris PCM"),
    (2026, 6, 9, "Kajian HPT", "PRM Waru 4", "Ketua PRM"),
    (2026, 6, 16, "Rapat Pengurus Lengkap PCM", "MTs Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 6, 23, "Kajian HPT", "PRM Mancasan", "Ketua PRM"),
    (2026, 6, 30, "Rapat PCM-PRM", "MIM Waru Baki", "Sekretaris PCM"),
    (2026, 7, 7, "Rapat Pengurus Harian PCM", "Rumah Bp. Hari Yudanto", "Sekretaris PCM"),
    (2026, 7, 14, "Kajian HPT", "PRM Bentakan", "Ketua PRM"),
    (2026, 7, 21, "Rapat Pengurus Lengkap PCM", "MI Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 7, 28, "Kajian HPT", "PRM Waru 5", "Ketua PRM"),
    (2026, 8, 4, "Rapat Pengurus Harian PCM", "Rumah Bp. Sahono", "Sekretaris PCM"),
    (2026, 8, 11, "Kajian HPT", "PRM Menuran", "Ketua PRM"),
    (2026, 8, 18, "Rapat Pengurus Lengkap PCM", "MTs Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 8, 25, "Kajian HPT", "PRM Siwal", "Ketua PRM"),
    (2026, 9, 1, "Rapat Pengurus Harian PCM", "Rumah Bp. Ibnu Hambali", "Sekretaris PCM"),
    (2026, 9, 8, "Kajian HPT", "PRM Kadilangu", "Ketua PRM"),
    (2026, 9, 15, "Rapat Pengurus Lengkap PCM", "MI Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 9, 29, "Kajian HPT", "PRM Duwet", "Ketua PRM"),
    (2026, 10, 6, "Rapat Pengurus Harian PCM", "Rumah Bp. Sartono (Purbayan)", "Sekretaris PCM"),
    (2026, 10, 13, "Kajian HPT", "PRM Bakipandeyan", "Ketua PRM"),
    (2026, 10, 20, "Rapat Pengurus Lengkap PCM", "MTs Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 10, 27, "Kajian HPT", "PRM Jetis", "Ketua PRM"),
    (2026, 11, 3, "Rapat Pengurus Harian PCM", "Rumah Bp. Muh. Ridwan", "Sekretaris PCM"),
    (2026, 11, 10, "Kajian HPT", "PRM Kudu", "Ketua PRM"),
    (2026, 11, 17, "Rapat Pengurus Lengkap PCM", "MI Muhammadiyah Waru", "Sekretaris PCM"),
    (2026, 11, 24, "Kajian HPT", "SPPG PCM Baki", "Penanggung jawab SPPG"),
    (2026, 12, 1, "Rapat Pengurus Harian PCM", "Rumah Bp. Fuad Hamdan", "Sekretaris PCM"),
]

AGENDA = [
    {
        "nama_kegiatan": kegiatan,
        "waktu_mulai": wib(tahun, bulan, tanggal, *JAM_AGENDA),
        "tempat": tempat,
        "keterangan": f"Penanggung jawab: {pj}" if pj else "",
    }
    for tahun, bulan, tanggal, kegiatan, tempat, pj in JADWAL_PCM
]

TAUTAN_TERKAIT = [
    {"nama": "PDM Sukoharjo", "url": "https://pdmsukoharjo.or.id/", "urutan": 1},
    {"nama": "PWM Jawa Tengah", "url": "https://muhammadiyahjateng.or.id/", "urutan": 2},
    {"nama": "PP Muhammadiyah", "url": "https://muhammadiyah.or.id", "urutan": 3},
]

DOKUMEN = [
    {
        "judul": "Jadwal Kegiatan Kajian PCM Baki",
        "keterangan": "Jadwal kegiatan kajian rutin Pimpinan Cabang Muhammadiyah Baki.",
        "berkas": "jadwal_kegiatan_kajian.pdf",
    },
    {
        "judul": "Struktur Pimpinan PCM Baki",
        "keterangan": "Susunan pimpinan Pimpinan Cabang Muhammadiyah Baki periode 2022-2027.",
        "berkas": "struktur_pimpinan.pdf",
    },
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
            "dokumen": 0,
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
        # 8. Dokumen (berkas PDF untuk halaman Unduhan)
        # --------------------------------------------------
        for data in DOKUMEN:
            if not (SEED_MEDIA / data["berkas"]).exists():
                self.stdout.write(
                    self.style.WARNING(
                        f"Dokumen '{data['judul']}' dilewati: "
                        f"{data['berkas']} tidak ada di web/seed_media/."
                    )
                )
                continue
            obj, created = Dokumen.objects.get_or_create(
                judul=data["judul"],
                defaults={"keterangan": data.get("keterangan", "")},
            )
            if created or not obj.berkas:
                lampirkan(obj, "berkas", data["berkas"])
            dibuat["dokumen"] += int(created)

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
