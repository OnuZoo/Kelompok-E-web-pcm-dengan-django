from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import re

class ProfilOrganisasi(models.Model):
    nama = models.CharField(max_length=200)
    nama_singkat = models.CharField(max_length=50)
    tagline = models.CharField(max_length=200, blank=True)
    tentang = models.TextField(blank=True)
    sejarah = models.TextField(blank=True)
    visi = models.TextField(blank=True)
    misi = models.TextField(blank=True, help_text="Tulis satu misi per baris.")
    alamat_sekretariat = models.TextField(blank=True)
    telepon = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    jumlah_anggota_ktam = models.PositiveIntegerField(default=0, verbose_name="jumlah anggota ber-KTAM")
    gambar_hero = models.ImageField(upload_to="hero/", blank=True)

    class Meta:
        verbose_name = "profil organisasi"
        verbose_name_plural = "profil organisasi"

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.pk = 1  # selalu satu baris saja
        super().save(*args, **kwargs)

    @property
    def daftar_misi(self):
        return [baris.strip() for baris in self.misi.splitlines() if baris.strip()]

    @property
    def daftar_sejarah(self):
        """Pecah teks sejarah jadi periode untuk timeline.
        Blok dipisah baris kosong; baris pertama = judul;
        '- ' = butir; akhiran ':' = label; lainnya = paragraf."""
        hasil = []
        for blok in re.split(r"\n\s*\n", self.sejarah.replace("\r\n", "\n").strip()):
            baris = [" ".join(b.split()) for b in blok.split("\n")]
            baris = [b for b in baris if b]
            if not baris:
                continue
            isi = []
            for b in baris[1:]:
                if b.startswith("- "):
                    if isi and isi[-1]["jenis"] == "daftar":
                        isi[-1]["butir"].append(b[2:])
                    else:
                        isi.append({"jenis": "daftar", "butir": [b[2:]]})
                elif b.endswith(":"):
                    isi.append({"jenis": "label", "teks": b})
                else:
                    isi.append({"jenis": "p", "teks": b})
            hasil.append({"judul": baris[0], "isi": isi})
        return hasil

class Pimpinan(models.Model):
    nama = models.CharField(max_length=150)
    jabatan = models.CharField(max_length=100)
    periode = models.CharField(max_length=20, default="2022-2027")
    foto = models.ImageField(upload_to="pimpinan/", blank=True)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["urutan"]
        verbose_name_plural = "pimpinan"

    def __str__(self):
        return f"{self.nama} - {self.jabatan}"


class Ranting(models.Model):
    nama = models.CharField(max_length=150, verbose_name="nama ranting")
    ketua = models.CharField(max_length=150, blank=True)
    alamat = models.TextField(blank=True)
    telepon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["nama"]
        verbose_name_plural = "ranting"

    def __str__(self):
        return self.nama


class AmalUsaha(models.Model):
    class Bidang(models.TextChoices):
        PENDIDIKAN = "pendidikan", "Pendidikan"
        KESEHATAN = "kesehatan", "Kesehatan"
        SOSIAL = "sosial", "Sosial"
        EKONOMI = "ekonomi", "Ekonomi"

    nama = models.CharField(max_length=200)
    bidang = models.CharField(max_length=20, choices=Bidang.choices)
    deskripsi = models.TextField(blank=True)
    alamat = models.TextField(blank=True)
    gambar = models.ImageField(upload_to="amal-usaha/", blank=True)

    class Meta:
        ordering = ["bidang", "nama"]
        verbose_name = "amal usaha"
        verbose_name_plural = "amal usaha"

    def __str__(self):
        return self.nama


class BeritaQuerySet(models.QuerySet):
    def terbit(self):
        """Hanya berita berstatus terbit dan tanggalnya sudah tiba."""
        return self.filter(status=Berita.Status.TERBIT, tanggal_terbit__lte=timezone.now())


class Berita(models.Model):
    class Status(models.TextChoices):
        DRAF = "draf", "Draf"
        TERBIT = "terbit", "Terbit"

    judul = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    ringkasan = models.TextField()
    isi = models.TextField()
    gambar_sampul = models.ImageField(upload_to="berita/", blank=True)
    tanggal_terbit = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAF)

    objects = BeritaQuerySet.as_manager()

    class Meta:
        ordering = ["-tanggal_terbit"]
        verbose_name_plural = "berita"

    def __str__(self):
        return self.judul

    def validate_unique(self, exclude=None):
        # Keunikan slug ditangani di save(), jadi form admin tidak menolak judul kembar.
        exclude = set(exclude or []) | {"slug"}
        super().validate_unique(exclude=exclude)

    def save(self, *args, **kwargs):
        dasar = slugify(self.slug or self.judul)[:200] or "berita"
        slug, n = dasar, 2
        while Berita.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{dasar}-{n}"
            n += 1
        self.slug = slug
        super().save(*args, **kwargs)


class Agenda(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    waktu_mulai = models.DateTimeField()
    tempat = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)

    class Meta:
        ordering = ["waktu_mulai"]
        verbose_name_plural = "agenda"

    def __str__(self):
        return self.nama_kegiatan


class Dokumen(models.Model):
    judul = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)
    berkas = models.FileField(upload_to="dokumen/")
    tanggal_unggah = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-tanggal_unggah"]
        verbose_name_plural = "dokumen"

    def __str__(self):
        return self.judul


class PesanMasuk(models.Model):
    nama = models.CharField(max_length=150)
    email = models.EmailField()
    subjek = models.CharField(max_length=200)
    pesan = models.TextField()
    waktu_kirim = models.DateTimeField(auto_now_add=True)
    sudah_dibaca = models.BooleanField(default=False)

    class Meta:
        ordering = ["-waktu_kirim"]
        verbose_name = "pesan masuk"
        verbose_name_plural = "pesan masuk"

    def __str__(self):
        return f"{self.subjek} - {self.nama}"


class TautanTerkait(models.Model):
    nama = models.CharField(max_length=150)
    url = models.URLField()
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["urutan"]
        verbose_name = "tautan terkait"
        verbose_name_plural = "tautan terkait"

    def __str__(self):
        return self.nama