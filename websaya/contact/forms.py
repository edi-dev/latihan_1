from django import forms
from django.forms import ModelForm
from .models import Kontak

class KontakForm(forms.Form):
    nama_lengkap = forms.CharField()
    tanggal_lahir = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years=range(1930,2021),
            attrs={
                'class':'form-control col-sm-4'
            }
        )
    )
    GENDER = [
        ('p', 'Pria'),
        ('w', 'Wanita'),
    ]
    jenis_kelamin = forms.ChoiceField(choices=GENDER)
    alamat = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField(required=False)

class ContactForm(ModelForm):
    class Meta:
        model = Kontak
        fields = '__all__'
        help_texts = {
            'tanggal_lahir': 'bulan/tanggal/tahun'
        }
        widgets = {
            'tanggal_lahir': forms.SelectDateWidget(
                years=range(1940,2021),
                attrs={
                    'class':'form-control col-sm-4'
                }
            )
        }
        labels = {
            'alamat': 'Alamat Lengkap'
        }