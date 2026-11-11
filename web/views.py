from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Agenda, AmalUsaha, Berita, Dokumen, Ranting, ProfilOrganisasi


def beranda(request):
    konteks = {
        "berita_terbaru": Berita.objects.terbit()[:3],
        "agenda_mendatang": Agenda.objects.filter(waktu_mulai__gte=timezone.now())[:3],
        "jumlah_ranting": Ranting.objects.count(),
        "jumlah_amal_usaha": AmalUsaha.objects.count(),
    }
    return render(request, "web/beranda.html", konteks)

def berita(request):
    berita_list = Berita.objects.terbit()
    konteks = {
        "berita_list": berita_list,
    }
    return render(request, "web/berita.html", konteks)

def profil(request):
    profil = ProfilOrganisasi.objects.first()
    return render(request, "web/profil.html", {"profil": profil})


def get_ranting(request):
    ranting_list = Ranting.objects.all()
    konteks = {
        "ranting_list": ranting_list,
    }
    return render(request, "web/ranting.html", konteks)

def get_amal_usaha(request):
    amal_usaha_list = AmalUsaha.objects.all()
    konteks = {
        "amal_usaha_list": amal_usaha_list,
    }
    return render(request, "web/amal_usaha.html", konteks)

def berita_detail(request, slug):
    berita = get_object_or_404(Berita, slug=slug, status=Berita.Status.TERBIT)
    return render(request, "web/berita_detail.html", {"berita": berita})

def unduhan(request):
    daftar_dokumen = Dokumen.objects.all()  # sudah urut terbaru lewat Meta.ordering
    return render(request, "web/unduhan.html", {"daftar_dokumen": daftar_dokumen})

def get_agenda_kegiatan(request):
    sekarang = timezone.now()
    agenda_mendatang = Agenda.objects.filter(waktu_mulai__gte=sekarang).order_by("waktu_mulai")
    agenda_lalu = Agenda.objects.filter(waktu_mulai__lt=sekarang).order_by("-waktu_mulai")
    konteks = {
        "agenda_mendatang": agenda_mendatang,
        "agenda_lalu": agenda_lalu,
    }
    return render(request, "web/agenda_kegiatan.html", konteks)