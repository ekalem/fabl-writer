from django.db import models

<<<<<<< HEAD
=======

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

>>>>>>> f75797dee37a786e1f07ad5b389ab5cb546c2ef6
class Fabl(models.Model):
    baslik = models.CharField(max_length=100)

    def __str__(self):
        return self.baslik

class Baglam(models.Model):
    anahtar = models.CharField(max_length=100)
    deger = models.CharField(max_length=100)
<<<<<<< HEAD
=======
    #fabl_id = models.ForeignKey(Fabl, on_delete=models.CASCADE)
>>>>>>> f75797dee37a786e1f07ad5b389ab5cb546c2ef6

    def __str__(self):
        return self.anahtar+" -- "+self.deger

class Sahne(models.Model):
<<<<<<< HEAD
    SAHNE_TIPLERI = (
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
=======
>>>>>>> f75797dee37a786e1f07ad5b389ab5cb546c2ef6
    anahtar = models.CharField(max_length=1, choices=SAHNE_TIPLERI)
    deger = models.TextField()
    secenek = models.CharField(max_length=1, choices=SECENEK)
    fabl_id = models.ForeignKey(Fabl, on_delete=models.CASCADE)

    def __str__(self):
        return self.anahtar+" -- "+self.secenek
