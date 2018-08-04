from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Baglam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anahtar', models.CharField(max_length=100)),
                ('deger', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fabl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sahne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anahtar', models.CharField(choices=[('B', 'Başlık'), ('G', 'Girizgah'), ('S', 'Serim'), ('D', 'Düğüm'), ('C', 'Çözüm'), ('O', 'Öğüt')], max_length=1)),
                ('deger', models.TextField()),
                ('secenek', models.CharField(choices=[('I', 'İyi'), ('K', 'Kötü')], max_length=1)),
                ('fabl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masal.Fabl')),
            ],
        ),
    ]
