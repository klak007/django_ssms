from django import forms
from django.forms import ModelForm
from .models import Rower, Klient, Wypozyczenia, Oplata, Salon, Pracownicy

class RowerForm(ModelForm):
    class Meta:
        model = Rower
        fields = '__all__'
        labels = {
            'marka': '',
            'id_salonu': '',
            'koszt': '',
            'wysokosc': '',
            'kolor': '',
            'przeznaczenie_plciowe': '',
            'material_ramy': '',
            'rodzaj_roweru': '',
        }
        widgets = {
            'marka': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marka'}),
            'id_salonu': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Salon'}),
            'koszt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Koszt'}),
            'wysokosc': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Wysokość'}),
            'kolor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kolor'}),
            'przeznaczenie_plciowe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Przeznaczenie płciowe'}),
            'material_ramy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Materiał ramy'}),
            'rodzaj_roweru': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rodzaj roweru'}),
        }
