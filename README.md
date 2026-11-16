# Website PCM Baki (Django)

Tugas kelompok mata kuliah **Pemrograman Web berbasis Framework (TIF1336)**.

> **Catatan:** Website ini dibuat untuk tugas kuliah Pemrograman Web berbasis Framework, **bukan website resmi** Pimpinan Cabang Muhammadiyah (PCM) Baki.

---

## 1. Identitas Kelompok

**Kelompok E**

| No. | Nama | NIM |
| :-: | ---- | --- |
| 1 | Reyhan Surya Putra | L200240013 |
| 2 | Akmal Zaidan Zidna Azizi | L200240019 |
| 3 | Pramudita Nabiha Hamdi | L200240027 |
| 4 | Muhammad Irsyad Al Farizi | L200240034 |
| 5 | Danang Estu Sambodo | L200240051 |

---

## 2. PCM yang Dipilih

| | |
| --- | --- |
| Nama | Pimpinan Cabang Muhammadiyah (PCM) Baki |
| Kecamatan | Baki |
| Kabupaten | Sukoharjo |
| Provinsi | Jawa Tengah |
| Kode pos | 57556 |

### Tabel sumber data

| Data | Sumber | Tanggal diambil |
| ---- | ------ | --------------- |
| Jadwal kegiatan (agenda) | Ibnu Hambali, S.Pd., M.Si | 10 November 2026 |
| Personalia pimpinan cabang | Ibnu Hambali, S.Pd., M.Si| 10 November 2026 |
| Logo Baki | Muchammad Riduwan | 12 November 2026 |
| Visi dan misi | H. Muhammad Mahmudi, S.Pd | 12 November 2026 |
| Daftar amal usaha (AUM) dan AUM PCM | Ibnu Hambali, S.Pd., M.Si | 12 November 2026 |
| Ranting (struktur organisasi) | H. Muhammad Mahmudi, S.Pd, Ibnu Hambali, S.Pd., M.Si | 12 November 2026 |
| Foto tiap pimpinan | Pengurus PCM Baki | 12 November 2026 |
| Foto kegiatan | Pengurus PCM Baki | 12 November 2026 |
| Riwayat berdiri (sejarah) | Muchammad Riduwan | 12 November 2026 |
| Profil dan tagline | Ibnu Hambali, S.Pd., M.Si | Ibnu Hambali, S.Pd., M.Si |
| Jumlah anggota ber-KTAM |Ibnu Hambali, S.Pd., M.Si |  12 November 2026 |
| Berita | Muchammad Riduwan, Ibnu Hambali, S.Pd., M.Si | 12 November 2026 |
| Kontak sekretariat (alamat, telepon, email) | Ibnu Hambali, S.Pd., M.Si | 9 November 2026 |




### Izin pengurus

Izin penggunaan data dan foto diberikan oleh:

| Nama | Jabatan di PCM Baki | Bentuk izin | Tanggal | Cakupan |
| ---- | ------------------- | ----------- | ------- | ------- |
| H. Muhammad Mahmudi, S.Pd | Ketua | LISAN | 6 November 2026 | Pengambilan Data |
| Ibnu Hambali, S.Pd., M.Si | Sekretaris | LISAN | 9 November 2026 | Data dan Dokumentasi |
| Muchammad Riduwan | Wakil Sekretaris | LISAN |  12 November 2026 | Data dan Dokumentasi |
| Fuad Hamdani, S.Pdi | Wakil Bendahara | Pesan elektronik |12 November 2026 |Data dan Dokumentasi |

---

## 3. Kontribusi Anggota

| Nama | NIM | Yang dikerjakan |
| ---- | --- | --------------- |
| Reyhan Surya Putra | L200240013 | Menginisialisasi proyek Django, membuat konfigurasi environment, model dan migrasi database, mendaftarkan model pada Django Admin, membuat kerangka URL dan views, mengembangkan halaman home dan kontak, mengintegrasikan form kontak, serta mengembangkan CSS dan template dasar.|
| Akmal Zaidan Zidna Azizi | L200240019 | Mengembangkan halaman pimpinan, amal usaha, dan ranting; mengelola data konten organisasi melalui seed_pcm.py; menambahkan foto pimpinan dan data amal usaha; serta memperbaiki tampilan halaman dan animasi. Membuat video demo|
| Pramudita Nabiha Hamdi | L200240027 | Mengembangkan halaman agenda, mengatur URL routing dan views agenda, memperbaiki navigasi agenda, mengembangkan halaman ranting, melakukan kustomisasi tampilan Django Admin menggunakan CSS dan JavaScript, serta menangani proses deployment aplikasi. Observasi kepada narasumber |
| Muhammad Irsyad Al Farizi | L200240034 | Membuat struktur template dasar dan halaman home, mengembangkan halaman profil dan unduhan, mengelola data awal melalui seed_pcm.py, memperbaiki navbar dan konsistensi tampilan, memisahkan komponen template berita, serta menambahkan pengujian Django. Pembuatan PPT materi presentasi|
| Danang Estu Sambodo | L200240051 | Mengembangkan fitur berita dan detail berita, mengatur URL routing dan views berita, mengelola data berita dan media, memperbaiki header dan footer, serta menyiapkan konfigurasi Docker dan deployment Vercel dan Supabase. |



---

## 4. Teknologi

- Python 3.14 dan Django 6.1 (template Django, server-side rendering)
- uv untuk pengelolaan dependensi (`pyproject.toml` dan `uv.lock`)
- Bootstrap 5.3 dan CSS buatan sendiri (`static/web/style.css`)
- Bootstrap 5.3 dan CSS buatan sendiri untuk admin (`static/web/admin_pcm.css`)
- JavaScript animasi (`static/web/animasi.js`)
- JavaScript animasi untuk admin (`static/web/admin_extra.js`)
- SQLite untuk pengembangan di laptop, PostgreSQL untuk Docker dan Supabase untuk produksi
- Gunicorn dan WhiteNoise (file statis)
- Docker dan Docker Compose
- Pillow (unggah gambar), dj-database-url, python-dotenv, psycopg

---

## 5. Fitur

### Halaman publik

| Alamat | Isi |
| ------ | --- |
| `/` | Beranda: dokumentasi pimpinan, statistik (ranting, amal usaha, anggota ber-KTAM), 3 berita terbaru, 3 agenda mendatang |
| `/profil/` | Tentang, sejarah, visi, dan misi |
| `/pimpinan/` | Kartu pimpinan dengan foto, jabatan, dan periode |
| `/ranting/` | daftar ranting |
| `/amal-usaha/` | Amal usaha per bidang |
| `/berita/` | Daftar berita terbit, 6 per halaman |
| `/berita/<slug>/` | Detail berita |
| `/agenda/` | Agenda akan datang dan sudah terlaksana |
| `/unduhan/` | Daftar dokumen untuk diunduh |
| `/kontak/` | Alamat sekretariat dan formulir kontak |

### Panel admin

Pengurus mengelola seluruh isi lewat `/admin/` tanpa menyentuh kode. Profil organisasi hanya boleh satu baris dan tidak bisa dihapus. Pesan masuk bersifat baca-saja.

### Konsep Django yang dipakai

Template inheritance dan `{% include %}`, URL dengan namespace, context processor, ModelForm dengan validasi dan messages framework, Paginator, custom QuerySet untuk berita terbit, slug otomatis yang unik, ImageField dan FileField, file statis dengan WhiteNoise, management command `seed_pcm`, dan konfigurasi lewat environment variable.

---

## 6. Menjalankan di Laptop (dengan uv)

Prasyarat: Git dan [uv](https://docs.astral.sh/uv/).

```bash

git clone https://github.com/OnuZoo/Kelompok-E-web-pcm-dengan-django

cd Kelompok-E-web-pcm-dengan-django

uv sync

uv run python manage.py migrate
uv run python manage.py seed_pcm
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Buka http://127.0.0.1:8000/ dan http://127.0.0.1:8000/admin/.


---

## 7. Menjalankan dengan Docker

Prasyarat: Docker dan Docker Compose.

```bash

docker compose up --build
```

Buka http://localhost:8000. Lalu, di terminal lain:

```bash
docker compose exec web uv run python manage.py seed_pcm
docker compose exec web uv run python manage.py createsuperuser
```


Perintah penting:

| Perintah | Efek |
| -------- | ---- |
| `docker compose down` | Menghentikan dan menghapus container. Data database dan gambar tetap ada di volume. |
| `docker compose up` | Menjalankan kembali dengan data yang sama. |
| `docker compose down -v` | Menghentikan container **dan menghapus semua volume**, jadi data database dan gambar unggahan hilang. Berguna untuk mengulang dari nol. |

Alasan `down -v` menghapus semua data: data PostgreSQL dan file media disimpan di *named volume*, bukan di dalam container. `down` biasa hanya membuang container, sedangkan opsi `-v` ikut membuang volume yang dibuat oleh `compose.yaml`.

Status pengujian Docker dari folder hasil clone yang bersih: BELUM ADA

---

## 8. Environment Variable

Contoh lengkap ada di [`.env.example`](.env.example). File `.env` tidak boleh di-commit.

| Variabel | Keterangan |
| -------- | ---------- |
| `SECRET_KEY` | Kunci rahasia Django. Wajib di produksi dan tidak boleh di-commit. |
| `DEBUG` | `True` di laptop, `False` di produksi. |
| `ALLOWED_HOSTS` | Daftar domain, dipisah koma. |
| `CSRF_TRUSTED_ORIGINS` | Domain produksi lengkap dengan `https://`. |
| `DATABASE_URL` | Kosong berarti SQLite. Berisi URL PostgreSQL berarti database cloud. |
| Variabel object storage | BELUM ADA |

---

## 9. Produksi

| | |
| --- | --- |
| URL produksi | https://pcmbaki.vercel.app/ |
| Platform | Vercel |
| Database | Supabase |
| Object storage untuk gambar | Supabase |

### Alasan memilih platform dan database
karena sudah memiliki pengalaman terhadap platform tersebut 

## 10. Akun Admin Demo

Username dan kata sandi akun admin untuk penilaian dikirim terpisah melalui Google Classroom dan tidak disimpan di repositori ini.

---

