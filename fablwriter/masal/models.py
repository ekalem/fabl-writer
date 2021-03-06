from django.db import models
from django.conf import settings


SAHNE_TIPLERI = (
    ('B', 'Başlık'),
    ('G', 'Girizgah'),
    ('S', 'Serim'),
    ('D', 'Düğüm'),
    ('C', 'Çözüm'),
    ('O', 'Öğüt'),
)
SECENEK = (
    ('I', 'İyi'),
    ('K', 'Kötü'),
)

class Fabl(models.Model):
    baslik = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    # user silindiği zaman user'ın girdiği fabl vb. içeriklerin de silinmesi için on_delete CASCADE yapılır.
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik

class Baglam(models.Model):
    anahtar = models.CharField(max_length=100)
    deger = models.CharField(max_length=100)
    fabl_id = models.ForeignKey(Fabl, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.fabl_id.baslik+" -- "+self.anahtar+" --> "+self.deger

class Sahne(models.Model):
    anahtar = models.CharField(max_length=1, choices=SAHNE_TIPLERI)
    deger = models.TextField()
    secenek = models.CharField(max_length=1, choices=SECENEK)
    fabl_id = models.ForeignKey(Fabl, on_delete=models.CASCADE)

    def __str__(self):
        return self.fabl_id.baslik+" --> "+self.anahtar

class Published(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    create_date = models.DateTimeField(auto_now_add=True)
