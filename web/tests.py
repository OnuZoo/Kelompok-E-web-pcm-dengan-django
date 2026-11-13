
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Berita, PesanMasuk


class HalamanPublikTests(TestCase):
    """Pengujian halaman publik website PCM Baki."""

    # TEST 1: Halaman beranda berhasil dibuka
    def test_halaman_beranda(self):
        response = self.client.get(
            reverse("web:beranda")
        )

        self.assertEqual(response.status_code, 200)

    # TEST 2: Halaman profil berhasil dibuka
    def test_halaman_profil(self):
        response = self.client.get(
            reverse("web:profil")
        )

        self.assertEqual(response.status_code, 200)

    # TEST 3: Pagination berita maksimal 6 berita per halaman
    def test_pagination_berita(self):
        # Membuat 7 berita terbit untuk pengujian
        for i in range(7):
            Berita.objects.create(
                judul=f"Berita Pengujian {i + 1}",
                ringkasan=f"Ringkasan berita pengujian {i + 1}",
                isi=f"Isi berita pengujian {i + 1}",
                tanggal_terbit=timezone.now() - timedelta(days=i),
                status=Berita.Status.TERBIT,
            )

        # Mengakses halaman pertama
        response = self.client.get(
            reverse("web:berita")
        )

        self.assertEqual(response.status_code, 200)

        page_obj = response.context["page_obj"]

        # Memastikan maksimal 6 berita per halaman
        self.assertEqual(len(page_obj.object_list), 6)

        # Memastikan terdapat 2 halaman
        self.assertEqual(page_obj.paginator.num_pages, 2)

        # Mengakses halaman kedua
        response_page_2 = self.client.get(
            reverse("web:berita"),
            {"page": 2}
        )

        self.assertEqual(response_page_2.status_code, 200)
        self.assertEqual(
            len(response_page_2.context["page_obj"].object_list),
            1
        )

    # TEST 4: Berita terbit bisa diakses, draf dan berita masa depan tidak
    def test_akses_detail_berita(self):
        sekarang = timezone.now()

        # Membuat berita yang sudah terbit
        berita_terbit = Berita.objects.create(
            judul="Berita Terbit Pengujian",
            ringkasan="Ringkasan berita terbit",
            isi="Isi berita terbit",
            tanggal_terbit=sekarang - timedelta(days=1),
            status=Berita.Status.TERBIT,
        )

        # Membuat berita berstatus draf
        berita_draf = Berita.objects.create(
            judul="Berita Draf Pengujian",
            ringkasan="Ringkasan berita draf",
            isi="Isi berita draf",
            tanggal_terbit=sekarang - timedelta(days=1),
            status=Berita.Status.DRAF,
        )

        # Membuat berita dengan tanggal masa depan
        berita_masa_depan = Berita.objects.create(
            judul="Berita Masa Depan Pengujian",
            ringkasan="Ringkasan berita masa depan",
            isi="Isi berita masa depan",
            tanggal_terbit=sekarang + timedelta(days=7),
            status=Berita.Status.TERBIT,
        )

        # Berita terbit harus bisa diakses
        response_terbit = self.client.get(
            reverse(
                "web:berita_detail",
                kwargs={"slug": berita_terbit.slug}
            )
        )

        self.assertEqual(response_terbit.status_code, 200)

        # Berita draf harus menghasilkan 404
        response_draf = self.client.get(
            reverse(
                "web:berita_detail",
                kwargs={"slug": berita_draf.slug}
            )
        )

        self.assertEqual(response_draf.status_code, 404)

        # Berita masa depan harus menghasilkan 404
        response_masa_depan = self.client.get(
            reverse(
                "web:berita_detail",
                kwargs={"slug": berita_masa_depan.slug}
            )
        )

        self.assertEqual(response_masa_depan.status_code, 404)

    # TEST 5: Form kontak berhasil menyimpan pesan
    def test_form_kontak(self):
        data_pesan = {
            "nama": "Pengunjung Pengujian",
            "email": "pengunjung@example.com",
            "subjek": "Pengujian Form Kontak",
            "pesan": "Ini adalah pesan untuk pengujian form kontak.",
        }

        response = self.client.post(
            reverse("web:kontak"),
            data_pesan
        )

        # Memastikan diarahkan ke halaman sukses
        self.assertRedirects(
            response,
            reverse("web:pesan_sukses")
        )

        # Memastikan pesan benar-benar tersimpan
        self.assertEqual(PesanMasuk.objects.count(), 1)

        pesan = PesanMasuk.objects.first()

        self.assertEqual(pesan.nama, data_pesan["nama"])
        self.assertEqual(pesan.email, data_pesan["email"])
        self.assertEqual(pesan.subjek, data_pesan["subjek"])
        self.assertEqual(pesan.pesan, data_pesan["pesan"])
