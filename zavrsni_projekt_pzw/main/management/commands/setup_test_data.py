import random
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Predavac, Tecaj, Prebivaliste, Polaznik, TjedanRadnoVrijeme, Raspored, Ocjena
from main.factory import PredavacFactory, TecajFactory, PrebivalisteFactory, PolaznikFactory, TjedanRadnoVrijemeFactory, RasporedFactory, OcjenaFactory

NUM_PREDAVACI = 10
NUM_TECAJEVI = 100
NUM_PREBIVALISTA = 20
NUM_POLAZNICI = 50
NUM_TJEDNI_RASPORED = 7
NUM_RASPOREDI = 30
NUM_OCJENE = 50

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Predavac, Tecaj, Prebivaliste, Polaznik, TjedanRadnoVrijeme, Raspored, Ocjena]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PREDAVACI):
            predavac = PredavacFactory()

        for _ in range(NUM_TECAJEVI):
            tecaj = TecajFactory()

        for _ in range(NUM_PREBIVALISTA):
            prebivaliste = PrebivalisteFactory()

        for _ in range(NUM_POLAZNICI):
            polaznik = PolaznikFactory()

        for _ in range(NUM_TJEDNI_RASPORED):
            tjedan_raspozred = TjedanRadnoVrijemeFactory()

        for _ in range(NUM_RASPOREDI):
            raspored = RasporedFactory()

        for _ in range(NUM_OCJENE):
            ocjena = OcjenaFactory()
