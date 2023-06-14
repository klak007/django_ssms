from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=254,
                             help_text='Wymagane. Podaj poprawny adres email.')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields[
            'username'].help_text = 'Wymagane. Maksymalnie 150 znaków. Dozwolone znaki: litery, cyfry oraz @/./+/-/_ .'
        self.fields['username'].label = 'Nazwa użytkownika'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = 'Wymagane. Hasło musi zawierać co najmniej 8 znaków. Nie może być ' \
                                             'powszechnie używanym hasłem. Nie może składać się wyłącznie z cyfr.'
        self.fields['password1'].label = 'Hasło'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = 'Wymagane. Wpisz to samo hasło co wyżej, dla weryfikacji.'
        self.fields['password2'].label = 'Potwierdź hasło'
