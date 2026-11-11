from django import forms

from .models import PesanMasuk


class PesanForm(forms.ModelForm):
    class Meta:
        model = PesanMasuk
        fields = ["nama", "email", "subjek", "pesan"]