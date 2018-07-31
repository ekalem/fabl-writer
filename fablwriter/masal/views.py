from django.shortcuts import render
from masal.models import Baglam, Fabl
from random import choice

def home(request):
    return render(request, 'home.html')

def insanvehayvan(request):
    karakter_ana = choice([i.deger for i in Baglam.objects.filter(anahtar='karakter_ana')])
    karakter_yetkili = choice([i.deger for i in Baglam.objects.filter(anahtar='karakter_yetkili')])
    karakter_hayvan = choice([i.deger for i in Baglam.objects.filter(anahtar='karakter_hayvan')])
    karakter_kotu = choice([i.deger for i in Baglam.objects.filter(anahtar='karakter_kotu')])
    zaman_belirteci = choice([i.deger for i in Baglam.objects.filter(anahtar='zaman_belirteci')])
    mekan_acik_1 = choice([i.deger for i in Baglam.objects.filter(anahtar='mekan_acik')])
    mekan_kapali_1 = choice([i.deger for i in Baglam.objects.filter(anahtar='mekan_kapali')])
    mekan_kapali_2 = choice([i.deger for i in Baglam.objects.filter(anahtar='mekan_kapali')])
    duygusal_tepki_1 = choice([i.deger for i in Baglam.objects.filter(anahtar='duygusal_tepki')])
    duygusal_tepki_2 = choice([i.deger for i in Baglam.objects.filter(anahtar='duygusal_tepki')])
    uzuv_1 = choice([i.deger for i in Baglam.objects.filter(anahtar='uzuv')])
    uzuv_2 = choice([i.deger for i in Baglam.objects.filter(anahtar='uzuv')])
    nesne_1 = choice([i.deger for i in Baglam.objects.filter(anahtar='nesne')])
    kiyafet = choice([i.deger for i in Baglam.objects.filter(anahtar='kiyafet')])
    sayi = choice(range(10))
    return render(request, 'insanvehayvan.html', {
        'karakter_ana': karakter_ana,
        'karakter_yetkili': karakter_yetkili,
        'karakter_hayvan': karakter_hayvan,
        'karakter_kotu': karakter_kotu,
        'zaman_belirteci': zaman_belirteci,
        'mekan_acik_1': mekan_acik_1,
        'mekan_kapali_1': mekan_kapali_1,
        'mekan_kapali_2': mekan_kapali_2,
        'duygusal_tepki_1': duygusal_tepki_1,
        'duygusal_tepki_2': duygusal_tepki_2,
        'uzuv_1': uzuv_1,
        'uzuv_2': uzuv_2,
        'nesne_1': nesne_1,
        'kiyafet': kiyafet,
        'sayi': sayi,
    })
