# Generated by Django 3.2.12 on 2024-01-17 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prebivaliste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prebivaliste_nazivMjesta', models.CharField(max_length=200)),
                ('prebivaliste_postanskiBroj', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Predavac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predavac_ime', models.CharField(max_length=30)),
                ('predavac_prezime', models.CharField(max_length=30)),
                ('predavac_email', models.EmailField(max_length=254)),
                ('predavac_brojSati', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tecaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecaj_naziv', models.CharField(max_length=100)),
                ('tecaj_sadrzaj', models.TextField()),
                ('tecaj_brojSati', models.CharField(max_length=10)),
                ('tecaj_nositelj', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.predavac')),
            ],
        ),
        migrations.CreateModel(
            name='TjedanRadnoVrijeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dan_u_tjednu', models.CharField(max_length=25)),
                ('termin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Polaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polaznik_ime', models.CharField(max_length=25)),
                ('polaznik_prezime', models.CharField(max_length=50)),
                ('polaznik_oib', models.CharField(max_length=10)),
                ('polaznik_prebivaliste', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.prebivaliste')),
                ('polaznik_tecaj', models.ManyToManyField(to='main.Tecaj')),
            ],
        ),
        migrations.CreateModel(
            name='Ocjena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocjena', models.CharField(max_length=5)),
                ('polozen_tecaj', models.BooleanField(default=True)),
                ('polaznik', models.ManyToManyField(to='main.Polaznik')),
                ('tecaj', models.ManyToManyField(to='main.Tecaj')),
            ],
        ),
        migrations.CreateModel(
            name='Raspored',
            fields=[
                ('tecaj', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.tecaj')),
                ('termin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.tjedanradnovrijeme')),
            ],
        ),
    ]