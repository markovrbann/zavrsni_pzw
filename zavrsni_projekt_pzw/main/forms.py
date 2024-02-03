from django import forms
from .models import *

class PredavacForm(forms.ModelForm):
    class Meta:
        model = Predavac
        fields = ['predavac_ime', 'predavac_prezime', 'predavac_email', 'predavac_brojSati']

class TecajForm(forms.ModelForm):
    class Meta:
        model = Tecaj
        fields = ['tecaj_naziv', 'tecaj_sadrzaj', 'tecaj_brojSati', 'tecaj_nositelj']
        
class PrebivalisteForm(forms.ModelForm):
    class Meta:
        model = Prebivaliste
        fields = ['prebivaliste_nazivMjesta', 'prebivaliste_postanskiBroj']

class PolaznikForm(forms.ModelForm):
    class Meta:
        model = Polaznik
        fields = ['polaznik_ime', 'polaznik_prezime', 'polaznik_oib', 'polaznik_tecaj', 'polaznik_prebivaliste']
        
class RasporedForm(forms.ModelForm):
    class Meta:
        model = Raspored
        fields = ['termin', 'tecaj']
        
class OcjenaForm(forms.ModelForm):
    class Meta:
        model = Ocjena
        fields = ['tecaj', 'polaznik', 'ocjena', 'polozen_tecaj']