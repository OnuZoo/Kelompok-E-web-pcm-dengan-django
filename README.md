# Tugas — Website PCM dengan Django

**Mata kuliah:** Pemrograman Web berbasis Framework (TIF1336)
**Jenis:** kelompok, 2–5 mahasiswa · **Tenggat:** pekan ke-8, **17 November 2026** · **Presentasi:** di kelas, pekan ke-8 · **Pengumpulan:** Google Classroom

## Gambaran tugas

Setiap kelompok memilih satu **Pimpinan Cabang Muhammadiyah (PCM) yang benar-benar ada** di daerah tempat tinggal salah satu anggota, lalu membangun website untuk PCM tersebut dengan **data riil**. Website ini harus bisa memperkenalkan organisasi, membagikan berita dan agenda, serta menerima pesan dari masyarakat. Pengurus harus bisa mengelola semua isinya sendiri tanpa menyentuh kode.

Anda membangun website tersebut dengan **Django**, lalu:

| Bagian | Isi | Bobot |
|---|---|---|
| [A](#bagian-a--aplikasi-django) | Aplikasi Django dengan fitur-fitur utama website PCM dan data riil PCM pilihan Anda | 50 |
| [B](#bagian-b--docker) | Menjalankan aplikasi dan database PostgreSQL dengan Docker | 15 |
| [C](#bagian-c--deployment) | Deployment ke **Vercel**, **Render**, atau **Railway**, dengan database **Supabase** atau **Neon** | 20 |
| [D](#yang-dikumpulkan) | Dokumentasi, video demo, dan **presentasi di kelas** | 15 |

Kerjakan berurutan: A dulu sampai berjalan di laptop, lalu B, lalu C.

## Teknologi wajib

- **Python 3.12 atau lebih baru** (di kelas kita memakai 3.14) dan **Django 6.x**
- **uv** untuk mengelola dependensi (`pyproject.toml` + `uv.lock` wajib di-commit)
- **Template Django** (server-side rendering). CSS bebas: Bootstrap, Tailwind, atau CSS buatan sendiri
- **SQLite** untuk pengembangan di laptop, **PostgreSQL** (Supabase atau Neon) untuk produksi
- **Git + GitHub** dalam satu repo kelompok. Setiap anggota melakukan commit dari akunnya sendiri, dan riwayat commit menunjukkan proses pengerjaan (bukan satu commit besar di akhir)

## Memilih PCM dan mengumpulkan data

1. **Pilih PCM.** Pilih PCM riil di daerah tempat tinggal salah satu anggota. Satu PCM hanya untuk satu kelompok: daftarkan pilihan Anda ke dosen paling lambat **pekan ke-7, 27 Oktober 2026**. Yang lebih dulu mendaftar yang dipakai.
2. **Kumpulkan data riil**, mis. dari website atau media sosial resmi PCM/PDM, berita di Suara Muhammadiyah atau media lokal, atau langsung dari pengurus PCM. Data yang dibutuhkan: profil, sejarah, visi dan misi, susunan pimpinan, daftar ranting, amal usaha, serta berita dan agenda terbaru.
3. **Catat sumber setiap data** di README repo Anda (tabel: data → sumber → tanggal diambil).
4. **Minta izin** kepada pengurus PCM jika memakai foto atau data yang belum dipublikasikan, dan sebutkan nama pengurus yang memberi izin di README.
5. **Lindungi data pribadi.** Hanya tampilkan data yang memang sudah dipublikasikan PCM atau yang diizinkan. **Jangan** menampilkan nomor HP pribadi, alamat rumah, NIK, atau data pribadi lain para pengurus tanpa izin. Untuk kontak, pakai kontak resmi sekretariat.
6. **Jika suatu data tidak bisa didapat**, kosongkan atau tulis "belum tersedia". **Jangan mengarang** data dan menyajikannya seolah-olah riil.
7. **Pasang keterangan di footer website**, mis. *"Website ini dibuat untuk tugas kuliah Pemrograman Web berbasis Framework, bukan website resmi PCM …"*. Ini wajib, karena website Anda akan online dengan nama organisasi yang benar-benar ada. **Pengecualian:** jika website dipakai di domain resmi PCM (lihat [bonus](#rubrik-penilaian)) dan pengurus menyetujuinya **secara tertulis**, keterangan ini boleh diganti menjadi *"Dikembangkan oleh mahasiswa … dalam tugas kuliah Pemrograman Web berbasis Framework"*. Sertakan bukti persetujuannya di README repo.

**Logo:** pakai logo Muhammadiyah dari [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Muhammadiyah.svg) **tanpa diubah**. Lisensinya CC BY-SA 4.0, jadi wajib cantumkan atribusi di footer: *"Logo Muhammadiyah: K. H. Siradj Dahlan, vektor oleh Hibensis, via Wikimedia Commons, lisensi CC BY-SA 4.0"*. Foto dari sumber lain juga wajib diberi kredit.

---

## Bagian A — Aplikasi Django

### A1. Model data

Buat model berikut (nama model dan field boleh dalam bahasa Indonesia, mis. `judul`, asalkan konsisten):

| Model | Isi minimal |
|---|---|
| **Profil organisasi** | nama, nama singkat, tagline, tentang, sejarah, visi, misi (satu misi per baris), alamat sekretariat, telepon, email, jumlah anggota ber-KTAM, gambar utama (hero). Hanya boleh ada **satu** baris. |
| **Pimpinan** | nama, jabatan, periode (mis. 2022–2027), foto, urutan tampil |
| **Ranting** | nama ranting, ketua, alamat, telepon (opsional; hanya kontak resmi) |
| **Amal usaha** | nama, bidang (*pilihan*: pendidikan, kesehatan, sosial, ekonomi), deskripsi, alamat, gambar |
| **Berita** | judul, slug (unik, dibuat otomatis dari judul), ringkasan, isi, gambar sampul, tanggal terbit, status terbit (draf/terbit) |
| **Agenda** | nama kegiatan, waktu mulai, tempat, keterangan |
| **Dokumen** | judul, keterangan, berkas (PDF dsb.), tanggal unggah |
| **Pesan masuk** | nama, email, subjek, pesan, waktu kirim, sudah dibaca |
| **Tautan terkait** | nama, URL, urutan |

### A2. Halaman publik

| URL | Isi |
|---|---|
| `/` | **Beranda:** hero dengan gambar utama, kartu statistik (jumlah ranting, jumlah amal usaha, anggota ber-KTAM), 3 berita terbaru, 3 agenda mendatang |
| `/profil/` | Tentang, sejarah, visi, dan misi (misi tampil sebagai daftar bernomor) |
| `/pimpinan/` | Kartu pimpinan dengan foto, jabatan, dan periode, diurutkan sesuai field urutan |
| `/ranting/` | Tabel ranting |
| `/amal-usaha/` | Amal usaha **dikelompokkan per bidang** |
| `/berita/` | Daftar berita yang sudah terbit, **6 per halaman** dengan navigasi halaman |
| `/berita/<slug>/` | Detail berita beserta beberapa berita lainnya. Berita draf atau bertanggal di masa depan harus **404** |
| `/agenda/` | Agenda **akan datang** dan **sudah terlaksana**, dipisah |
| `/unduhan/` | Daftar dokumen dengan tombol unduh |
| `/kontak/` | Alamat sekretariat dan **formulir kontak**. Pesan tersimpan ke database, lalu muncul pesan sukses |

Semua halaman memakai satu **template dasar** dengan:
- header berisi logo, nama singkat, tagline, dan menu navigasi yang **responsif** (tetap rapi di layar HP);
- footer berisi nama, alamat, dan kontak resmi PCM, bagian **"Tautan Persyarikatan"** yang mengambil data dari model Tautan terkait, keterangan tugas kuliah, serta atribusi logo dan foto.

Isi Tautan terkait dengan website resmi **PDM dan PWM tempat PCM Anda berada**, ditambah [PP Muhammadiyah](https://muhammadiyah.or.id). Pastikan setiap URL benar-benar bisa dibuka.

### A3. Panel admin

- Semua model terdaftar di admin dengan `list_display` yang informatif, plus `search_fields` dan/atau `list_filter` jika relevan.
- Profil organisasi tidak bisa ditambah jika sudah ada satu baris, dan tidak bisa dihapus.
- Berita memakai `prepopulated_fields` untuk slug dan `date_hierarchy` untuk tanggal terbit.
- Pesan masuk bersifat **baca-saja** (tidak bisa ditambah dari admin; isi pesan tidak bisa diubah).
- Judul admin diganti, mis. "Admin Website PCM …".

### A4. Konsep Django yang harus terlihat di kode

- [ ] Template inheritance (`{% extends %}`) dan `{% include %}` untuk komponen yang dipakai ulang (mis. kartu berita)
- [ ] URL dengan `app_name` (namespace) dan `{% url %}` di template; tidak ada URL yang ditulis manual
- [ ] **Context processor** yang menyediakan profil organisasi dan tautan terkait ke semua template
- [ ] **ModelForm** untuk formulir kontak, dengan validasi dan **messages framework** untuk pesan sukses
- [ ] `Paginator` di daftar berita
- [ ] **Custom manager** atau method QuerySet untuk berita yang sudah terbit
- [ ] Slug otomatis yang tetap unik jika ada judul yang sama
- [ ] `ImageField`/`FileField` dengan pengaturan `MEDIA_ROOT`/`MEDIA_URL`, serta file statis (`STATIC_ROOT`, `{% static %}`)
- [ ] **Management command** `seed_pcm` yang mengisi **data riil PCM Anda** (beserta gambarnya) ke database kosong, sehingga website langsung terisi setelah instalasi, baik di laptop, di Docker, maupun di produksi
- [ ] Minimal **5 test** (`manage.py test`), mis.: semua halaman publik 200, berita draf 404, formulir kontak menyimpan pesan

### A5. Konfigurasi lewat environment variable

Pengaturan yang berbeda antara laptop dan server **tidak boleh ditulis langsung di `settings.py`**. Bacalah dari environment variable (boleh dibantu `python-dotenv` atau `django-environ`):

| Variabel | Keterangan |
|---|---|
| `SECRET_KEY` | wajib di produksi; jangan pernah di-commit |
| `DEBUG` | `True` di laptop, **`False` di produksi** |
| `ALLOWED_HOSTS` | daftar domain, dipisah koma |
| `CSRF_TRUSTED_ORIGINS` | domain produksi **lengkap dengan `https://`** |
| `DATABASE_URL` | kosong → SQLite; berisi URL PostgreSQL → database cloud (pakai `dj-database-url`) |

Sertakan file `.env.example` berisi nama-nama variabel **tanpa nilai rahasia**, dan masukkan `.env` ke `.gitignore`.

---

## Bagian B — Docker

Tujuannya: siapa pun yang meng-clone repo Anda cukup menjalankan **satu perintah** untuk mendapatkan website lengkap dengan database PostgreSQL.

```bash
docker compose up --build
# buka http://localhost:8000
```

### Yang harus dibuat

1. **`Dockerfile`**
   - Base image resmi Python slim (mis. `python:3.14-slim`).
   - Dependensi diinstal dengan **uv** dari `uv.lock` (lihat [panduan uv untuk Docker](https://docs.astral.sh/uv/guides/integration/docker/)).
   - `collectstatic` dijalankan saat build.
   - Aplikasi dijalankan dengan **Gunicorn**, bukan `runserver`, dan mendengarkan port dari variabel `PORT` (default 8000) agar image yang sama bisa dipakai di platform cloud.
   - Proses berjalan sebagai **user non-root**.
2. **`.dockerignore`**: kecualikan `.venv/`, `.git/`, `.env`, `db.sqlite3`, `media/`, `staticfiles/`, `__pycache__/`.
3. **`compose.yaml`** dengan dua service:
   - `db`: image `postgres:17`, data disimpan di **named volume**, dan memiliki `healthcheck` (`pg_isready`);
   - `web`: dibangun dari `Dockerfile`, membaca `.env`, menunggu `db` sehat (`depends_on` + `condition: service_healthy`), menjalankan `migrate` sebelum Gunicorn, dan menyimpan `media/` di volume.
4. **WhiteNoise** untuk menyajikan file statis saat `DEBUG=False`.

### Cara memeriksa

- [ ] `docker compose up --build` di folder hasil clone yang bersih langsung jalan tanpa langkah manual lain
- [ ] `docker compose exec web uv run python manage.py seed_pcm` dan `createsuperuser` berhasil
- [ ] Halaman admin tetap bergaya (CSS terbaca) dengan `DEBUG=False`
- [ ] Setelah `docker compose down` lalu `up` lagi, data dan gambar unggahan **masih ada**
- [ ] `docker compose down -v` menghapus semua data (jelaskan di README Anda mengapa)

---

## Bagian C — Deployment

Pilih **satu platform** dan **satu database**:

| Platform | Catatan penting |
|---|---|
| [**Vercel**](https://vercel.com/docs/frameworks/full-stack/django) | Mendukung Django tanpa konfigurasi tambahan; jika `STATIC_ROOT` diatur, `collectstatic` berjalan otomatis saat build dan file statis disajikan lewat CDN. Aplikasi berjalan sebagai *function*: filesystem tidak permanen dan ukuran request maksimal **4,5 MB**, jadi file unggahan wajib disimpan di object storage. Tidak ada langkah "release", jadi `migrate` dijalankan dari laptop dengan `DATABASE_URL` produksi. |
| [**Render**](https://render.com/docs/deploy-django) | Web Service dengan *build command* (install, `collectstatic`, `migrate`) dan *start command* Gunicorn, atau langsung memakai `Dockerfile` dari Bagian B. Instance gratis "tidur" setelah tidak ada akses, sehingga request pertama lambat. Disk tidak permanen. |
| [**Railway**](https://docs.railway.com/guides/django) | Bisa langsung memakai `Dockerfile` dari Bagian B. Domain publik dibuat di menu *Networking*. Cek ketentuan kredit/free trial terbaru sebelum mulai. |

| Database | Catatan penting |
|---|---|
| [**Supabase**](https://supabase.com/docs/guides/database/connecting-to-postgres) | Ambil connection string dari tombol *Connect* di dashboard. Koneksi *direct* hanya IPv6; jika jaringan Anda atau platform tidak mendukung IPv6, pakai **Session pooler**. Untuk Vercel (serverless), pakai **Transaction pooler** (port 6543). Proyek gratis bisa dijeda jika lama tidak dipakai. |
| [**Neon**](https://neon.com/docs/guides/django) | Pakai connection string dengan `sslmode=require`. Ada pilihan *pooled* (host berakhiran `-pooler`) dan *direct*. Neon menyarankan koneksi **direct** untuk menjalankan migrasi. |

Jika memakai connection pooler mode *transaction* (Supabase port 6543 atau Neon pooled), tambahkan `"DISABLE_SERVER_SIDE_CURSORS": True` pada pengaturan database dan set `CONN_MAX_AGE` ke `0`. Baca bagian *Transaction pooling and server-side cursors* di [dokumentasi database Django](https://docs.djangoproject.com/en/stable/ref/databases/#transaction-pooling-and-server-side-cursors).

### Masalah file unggahan

Semua platform di atas **tidak menyimpan file secara permanen**: gambar yang diunggah lewat admin akan hilang setelah redeploy atau restart. Simpan media di **object storage**, misalnya **Supabase Storage** (mendukung protokol S3, sehingga bisa dipakai lewat `django-storages`, termasuk jika database Anda di Neon), Cloudinary, atau Cloudflare R2. File statis tetap disajikan oleh WhiteNoise, atau CDN Vercel.

### Syarat deployment

- [ ] Website bisa diakses lewat **HTTPS** di URL publik
- [ ] `DEBUG=False`; halaman yang tidak ada menampilkan 404, bukan halaman error Django berwarna kuning
- [ ] Semua rahasia (`SECRET_KEY`, `DATABASE_URL`, kunci storage) diatur di **environment variable platform**, tidak ada di repo
- [ ] Database produksi adalah PostgreSQL di Supabase/Neon, berisi data riil dari `seed_pcm`
- [ ] Login admin berhasil dan halaman admin bergaya
- [ ] Gambar yang diunggah lewat admin **masih ada setelah redeploy**
- [ ] Pesan dari formulir kontak tersimpan dan terlihat di *table editor* Supabase/Neon

---

## Yang dikumpulkan

Paling lambat **pekan ke-8, 17 November 2026**, melalui Google Classroom:

1. **Link repo GitHub kelompok**. Repo boleh publik; jika privat, undang akun dosen. `README.md` di repo Anda berisi:
   - nama kelompok, serta nama dan NIM setiap anggota;
   - **PCM yang dipilih** (nama dan wilayah) dan **tabel sumber data** (data → sumber → tanggal diambil), termasuk nama pengurus yang memberi izin jika ada;
   - **tabel kontribusi**: apa yang dikerjakan setiap anggota;
   - cara menjalankan di laptop (dengan uv) dan dengan Docker;
   - URL produksi, serta platform dan database yang dipilih beserta **alasan** memilihnya;
   - daftar environment variable yang dibutuhkan (rujuk ke `.env.example`);
   - akun admin demo untuk penilaian (boleh dikirim terpisah, jangan di-commit).
2. **URL produksi** yang tetap menyala sampai penilaian selesai.
3. **Video demo** 5–10 menit (YouTube *unlisted* atau Google Drive) yang memperlihatkan:
   - semua halaman publik di versi produksi, termasuk tampilan di layar HP;
   - menambah berita bergambar dari admin, lalu melihatnya di beranda;
   - mengirim pesan kontak, lalu melihatnya di admin dan di dashboard database;
   - `docker compose up --build` dari folder bersih;
   - environment variable di dashboard platform (nilai rahasia **disamarkan**).
4. **Slide presentasi** (PDF).

## Presentasi (pekan ke-8)

Setiap kelompok mempresentasikan hasilnya di kelas pada **pekan ke-8**, **5 menit presentasi + 5 menit tanya jawab**:

- PCM yang dipilih, cara mengumpulkan data, dan izin yang diperoleh;
- **demo langsung** website versi produksi, termasuk admin;
- arsitektur: Django, Docker, platform, database, dan object storage yang dipakai, serta alasannya;
- kendala terbesar dan cara mengatasinya.

**Setiap anggota wajib berbicara**, dan dosen dapat bertanya kepada anggota mana pun tentang bagian mana pun dari kode. Anggota yang tidak hadir tanpa alasan sah tidak mendapat nilai presentasi.

## Rubrik penilaian

| Komponen | Poin | Nilai penuh jika |
|---|---|---|
| **A. Halaman publik & data riil** | 20 | Semua halaman di A2 ada, rapi dan responsif; isinya data riil PCM yang lengkap, bersumber, dan tanpa data pribadi yang tidak diizinkan |
| **A. Admin** | 10 | Semua ketentuan A3 terpenuhi |
| **A. Konsep Django** | 15 | Semua poin A4 ada di kode, dan test lulus |
| **A. Konfigurasi** | 5 | Ketentuan A5 terpenuhi; `.env.example` lengkap; tidak ada rahasia di repo |
| **B. Docker** | 15 | Semua cek di Bagian B lulus dari hasil clone yang bersih |
| **C. Deployment** | 20 | Semua syarat deployment terpenuhi (media permanen bernilai 5 poin) |
| **D. Dokumentasi & video** | 5 | README repo lengkap (termasuk sumber data dan kontribusi), video jelas dan mencakup semua poin |
| **D. Presentasi** | 10 | Demo produksi berjalan lancar, penjelasan arsitektur tepat, semua anggota menguasai materi saat tanya jawab |

**Bonus** (maks +10, nilai akhir maks 100):

| Tugas | Poin |
|---|---|
| GitHub Actions yang menjalankan test setiap push | +4 |
| Fitur pencarian berita | +3 |
| Custom domain untuk URL produksi | +3 |
| **Domain resmi yang diminta pengurus PCM** (mis. `pcmkartasura.id` atau semisalnya) dipakai sebagai URL produksi, dengan HTTPS | +5 |
| Pengurus PCM menyatakan website layak dipakai (sertakan bukti, mis. surat atau pesan) | +3 |

Untuk bonus domain resmi: domain harus **didaftarkan atas nama PCM** (bukan atas nama mahasiswa) dan dipilih atau disetujui pengurus.

**Pengurangan:**

| Masalah | Poin |
|---|---|
| `SECRET_KEY`, password database, atau kunci storage ada di repo (termasuk di riwayat commit) | −10 |
| Data dikarang lalu disajikan seolah-olah riil, atau data pribadi ditampilkan tanpa izin | −10 |
| `DEBUG=True` di produksi | −5 |
| Keterangan "tugas kuliah, bukan website resmi" (atau penggantinya yang disetujui pengurus, lihat poin 7 di [Memilih PCM](#memilih-pcm-dan-mengumpulkan-data)) atau atribusi logo/foto tidak ada | −5 |
| Anggota tanpa commit atau kontribusi yang tercatat | nilai anggota tersebut dikurangi, sesuai pertimbangan dosen |
| Terlambat | sesuai kebijakan mata kuliah |
| Kode sama dengan kelompok lain | nilai 0 untuk semua kelompok yang terlibat |

## Referensi

- Dokumentasi Django: https://docs.djangoproject.com/
- uv dengan Docker: https://docs.astral.sh/uv/guides/integration/docker/
- Django di Vercel: https://vercel.com/docs/frameworks/full-stack/django
- Django di Render: https://render.com/docs/deploy-django
- Django di Railway: https://docs.railway.com/guides/django
- Koneksi ke Supabase Postgres: https://supabase.com/docs/guides/database/connecting-to-postgres
- Django dengan Neon: https://neon.com/docs/guides/django
- WhiteNoise: https://whitenoise.readthedocs.io/
- django-storages: https://django-storages.readthedocs.io/
