from django import forms
from .models import Medlem, Aktivitet, Pamelding, Betaling


# Skjema for å opprette/endre medlemmer
class MedlemForm(forms.ModelForm):
    class Meta:
        model = Medlem
        fields = ['navn', 'epost', 'telefon', 'aktiv']
        widgets = {
            'navn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fullt navn'
            }),
            'epost': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-postadresse'
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefonnummer'
            }),
            'aktiv': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


# Skjema for å opprette/endre aktiviteter
class AktivitetForm(forms.ModelForm):
    class Meta:
        model = Aktivitet
        fields = ['navn', 'beskrivelse', 'dato', 'sted']
        widgets = {
            'navn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Aktivitetsnavn'
            }),
            'beskrivelse': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Beskrivelse',
                'rows': 4
            }),
            'dato': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sted': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sted'
            }),
        }


# Skjema for å opprette påmeldinger
class PameldingForm(forms.ModelForm):
    class Meta:
        model = Pamelding
        fields = ['medlem', 'aktivitet']
        widgets = {
            'medlem': forms.Select(attrs={
                'class': 'form-control'
            }),
            'aktivitet': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


# Skjema for å opprette/endre betalinger
class BetalingForm(forms.ModelForm):
    class Meta:
        model = Betaling
        fields = ['medlem', 'belop', 'betalingsdato', 'status']
        widgets = {
            'medlem': forms.Select(attrs={
                'class': 'form-control'
            }),
            'belop': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Beløp (kr)',
                'step': '0.01'
            }),
            'betalingsdato': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }