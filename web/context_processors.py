from .models import ProfilOrganisasi, TautanTerkait


def situs(request):
    """Tersedia di semua template: profil organisasi dan tautan terkait."""
    return {
        "profil": ProfilOrganisasi.objects.first(),
        "tautan_terkait": TautanTerkait.objects.all(),
    }