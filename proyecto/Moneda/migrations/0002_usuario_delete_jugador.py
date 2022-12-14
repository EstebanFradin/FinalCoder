# Generated by Django 4.1.3 on 2022-12-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moneda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('balance', models.IntegerField()),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('cantidad_apostar', models.IntegerField(default=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Jugador',
        ),
    ]
