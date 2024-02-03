from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import HomePageView, PredavacView, TecajView, PredavacListView  
from django.test import TestCase, Client
from django.urls import reverse
from main.models import Predavac
from django.test import TestCase
from main.models import Ocjena, Raspored, Tecaj, Polaznik, Prebivaliste, Predavac, TjedanRadnoVrijeme



class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:home')
        self.assertEquals(resolve(url).func.view_class, HomePageView)

    def test_predavaci_url_is_resolved(self):
        url = reverse('main:predavaci')
        self.assertEquals(resolve(url).func.view_class, PredavacView)

    def test_tecajevi_url_is_resolved(self):
        url = reverse('main:tecajevi')
        self.assertEquals(resolve(url).func.view_class, TecajView)

    def test_pretraga_url_is_resolved(self):
        url = reverse('main:pretraga')
        self.assertEquals(resolve(url).func.view_class, PredavacListView)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.predavac_list_url = reverse('main:predavaci')

        self.predavac1 = Predavac.objects.create(
            predavac_ime='Ime1',
            predavac_prezime='Prezime1',
            predavac_email='ime1.prezime1@example.com',
            predavac_brojSati='20'
        )

        self.predavac2 = Predavac.objects.create(
            predavac_ime='Ime2',
            predavac_prezime='Prezime2',
            predavac_email='ime2.prezime2@example.com',
            predavac_brojSati='30'
        )

    def test_predavac_list_GET(self):
        response = self.client.get(self.predavac_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/predavac_list.html')

    def test_predavac_list_contains_predavac(self):
        response = self.client.get(self.predavac_list_url)

        self.assertContains(response, self.predavac1.predavac_ime)
        self.assertContains(response, self.predavac1.predavac_prezime)
        self.assertContains(response, self.predavac2.predavac_ime)
        self.assertContains(response, self.predavac2.predavac_prezime)

class TestModels(TestCase):

    def setUp(self):
        self.prebivaliste = Prebivaliste.objects.create(
            prebivaliste_nazivMjesta='Grad',
            prebivaliste_postanskiBroj='10000'
        )

        self.predavac = Predavac.objects.create(
            predavac_ime='Ime',
            predavac_prezime='Prezime',
            predavac_email='ime.prezime@example.com',
            predavac_brojSati='20'
        )

        self.tecaj = Tecaj.objects.create(
            tecaj_naziv='Tečaj',
            tecaj_sadrzaj='Sadržaj tečaja',
            tecaj_brojSati='10',
            tecaj_nositelj=self.predavac
        )

        self.polaznik = Polaznik.objects.create(
            polaznik_ime='Polaznik',
            polaznik_prezime='Prezimic',
            polaznik_oib='1234567890',
            polaznik_prebivaliste=self.prebivaliste
        )

        self.tjedan_radno_vrijeme = TjedanRadnoVrijeme.objects.create(
            dan_u_tjednu='Ponedjeljak',
            termin='10:00-12:00'
        )

        self.raspored = Raspored.objects.create(
            termin=self.tjedan_radno_vrijeme,
            tecaj=self.tecaj
        )

        self.ocjena = Ocjena.objects.create(
            tecaj=self.tecaj,
            polaznik=self.polaznik,
            ocjena='5',
            polozen_tecaj=True
        )

    def test_ocjena_model(self):
        self.assertEquals(self.ocjena.ocjena, '5')

    def test_raspored_model(self):
        self.assertEquals(str(self.raspored), 'Tečaj (Ponedjeljak 10:00-12:00)')
