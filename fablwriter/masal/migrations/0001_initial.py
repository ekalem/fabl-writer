# Generated by Django 2.0.7 on 2018-07-29 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baglam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anantar', models.CharField(max_length=100)),
                ('deger', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fabl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100)),
                ('yazar', models.CharField(max_length=100)),
                ('tarih', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sahne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anahtar', models.CharField(choices=[('G', 'Girizgah'), ('S', 'Serim'), ('D', 'Düğüm'), ('C', 'Çözüm'), ('O', 'Öğüt')], max_length=1)),
                ('deger', models.TextField()),
                ('secenek', models.CharField(choices=[('I', 'İyi'), ('K', 'Kötü')], max_length=1)),
                ('fabl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masal.Fabl')),
            ],
        ),
        migrations.AddField(
            model_name='baglam',
            name='fabl_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masal.Fabl'),
        ),
    ]
