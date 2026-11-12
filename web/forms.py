from django import forms

from .models import PesanMasuk


class PesanForm(forms.ModelForm):
    class Meta:
        model = PesanMasuk
        fields = ["nama", "email", "subjek", "pesan"]
        widgets = {
            "nama": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "subjek": forms.TextInput(attrs={"class": "form-control"}),
            "pesan": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }