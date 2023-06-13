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
            'id_salonu': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Dostępne w salonie'}),
            'koszt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Koszt wypożyczenia pięcio dniowego'}),
            'wysokosc': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Wysokość użytkownika'}),
            'kolor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kolor roweru'}),
            'przeznaczenie_plciowe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Przeznaczenie płciowe'}),
            'material_ramy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Materiał ramy'}),
            'rodzaj_roweru': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rodzaj roweru'}),
        }

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = '__all__'
        labels = {
            'miasto': '',
            'ulica': '',
        }
        widgets = {
            'miasto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Miasto'}),
            'ulica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ulica'}),
        }