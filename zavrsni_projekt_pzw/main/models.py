from django.db import models
from django.utils import timezone

## Create your models here.


class Predavac(models.Model):
    predavac_ime = models.CharField(max_length=30)
    predavac_prezime = models.CharField(max_length=30)
    predavac_email = models.EmailField()
    predavac_brojSati = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.predavac_ime + ' ' + self.predavac_prezime)


class Tecaj(models.Model):
    tecaj_naziv = models.CharField(max_length=100)
    tecaj_sadrzaj = models.TextField()
    tecaj_brojSati = models.CharField(max_length=10)
    tecaj_nositelj = models.ForeignKey(Predavac, default=1, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.tecaj_naziv + ' (broj sati: ' + self.tecaj_brojSati + ')')
    
class Prebivaliste(models.Model):
    prebivaliste_nazivMjesta = models.CharField(max_length=200)
    prebivaliste_postanskiBroj = models.CharField(max_length=10)
    def __str__(self):
        return '{}'.format(self.prebivaliste_postanskiBroj + ' ' + self.prebivaliste_nazivMjesta)


class Polaznik(models.Model):
    polaznik_ime = models.CharField(max_length=25)
    polaznik_prezime = models.CharField(max_length=50)
    polaznik_oib = models.CharField(max_length=10)
    polaznik_tecaj = models.ManyToManyField(Tecaj)
    polaznik_prebivaliste = models.ForeignKey(Prebivaliste, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.polaznik_ime + ' ' + self.polaznik_prezime)

class TjedanRadnoVrijeme(models.Model):
    dan_u_tjednu = models.CharField(max_length=25)
    termin = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.dan_u_tjednu + ' ' + self.termin)

class Raspored(models.Model):
    termin = models.OneToOneField(
        TjedanRadnoVrijeme,
        on_delete=models.CASCADE,
    )
    tecaj = models.OneToOneField(
        Tecaj,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return '{}'.format(self.tecaj.tecaj_naziv + ' (' + self.termin.dan_u_tjednu + ' ' + self.termin.termin + ')')

class Ocjena(models.Model):
    tecaj = models.ForeignKey(Tecaj, default=1, on_delete=models.CASCADE)
    polaznik = models.ForeignKey(Polaznik, default=1, on_delete=models.CASCADE)
    ocjena = models.CharField(max_length=5)
    polozen_tecaj = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.polaznik.polaznik_ime + ' ' + self.polaznik.polaznik_prezime + ' (Ocjena ' + self.ocjena + ')')