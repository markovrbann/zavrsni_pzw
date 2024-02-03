import factory
from factory.django import DjangoModelFactory
from .models import Predavac, Tecaj, Prebivaliste, Polaznik, TjedanRadnoVrijeme, Raspored, Ocjena

class PredavacFactory(DjangoModelFactory):
    class Meta:
        model = Predavac

    predavac_ime = factory.Faker("first_name")
    predavac_prezime = factory.Faker("last_name")
    predavac_email = factory.Faker("email")
    predavac_brojSati = factory.Faker("random_int", min=1, max=100)

class TecajFactory(DjangoModelFactory):
    class Meta:
        model = Tecaj

    tecaj_naziv = factory.Faker("sentence", nb_words=4)
    tecaj_sadrzaj = factory.Faker("text", max_nb_chars=200)
    tecaj_brojSati = factory.Faker("random_int", min=1, max=100)
    tecaj_nositelj = factory.SubFactory(PredavacFactory)

class PrebivalisteFactory(DjangoModelFactory):
    class Meta:
        model = Prebivaliste

    prebivaliste_nazivMjesta = factory.Faker("city")
    prebivaliste_postanskiBroj = factory.Faker("zipcode")

class PolaznikFactory(DjangoModelFactory):
    class Meta:
        model = Polaznik

    polaznik_ime = factory.Faker("first_name")
    polaznik_prezime = factory.Faker("last_name")
    polaznik_oib = factory.Faker("random_int", min=1000000000, max=9999999999)
    polaznik_prebivaliste = factory.SubFactory(PrebivalisteFactory)

class TjedanRadnoVrijemeFactory(DjangoModelFactory):
    class Meta:
        model = TjedanRadnoVrijeme

    dan_u_tjednu = factory.Faker("random_element", elements=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    termin = factory.Faker("time")

class RasporedFactory(DjangoModelFactory):
    class Meta:
        model = Raspored

    termin = factory.SubFactory(TjedanRadnoVrijemeFactory)
    tecaj = factory.SubFactory(TecajFactory)
    

class OcjenaFactory(DjangoModelFactory):
    class Meta:
        model = Ocjena

    tecaj = factory.SubFactory(TecajFactory)
    polaznik = factory.SubFactory(PolaznikFactory)
    ocjena = factory.Faker("random_element", elements=['A', 'B', 'C', 'D', 'F'])
    polozen_tecaj = factory.Faker("boolean")
