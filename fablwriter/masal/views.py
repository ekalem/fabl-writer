<<<<<<< HEAD
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
=======
from random import choice
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FablForm
from masal.models import Baglam, Fabl, Sahne

def home(request):
    fables = Fabl.objects.all()
    return render(request, 'home.html', {
        'title': 'FABLOPİCASSO',
        'fables': fables,
    })

def fabl_create(request):
    form = FablForm()
    if request.method == 'POST':
        form = FablForm(request.POST)
        if form.is_valid():
            baslik = Fabl.objects.create(baslik=form.cleaned_data['baslik'])
            Sahne.objects.create(
                anahtar='B',
                deger=form.cleaned_data['baslik'],
                secenek='I',
                fabl_id=baslik,
            )
            girizgah = Sahne.objects.create(
                anahtar='G',
                deger=form.cleaned_data['girizgah'],
                secenek='I',
                fabl_id=baslik,
            )
            serim = Sahne.objects.create(
                anahtar='S',
                deger=form.cleaned_data['serim'],
                secenek='I',
                fabl_id=baslik,
            )
            dugum = Sahne.objects.create(
                anahtar='D',
                deger=form.cleaned_data['dugum'],
                secenek='I',
                fabl_id=baslik,
            )
            cozum = Sahne.objects.create(
                anahtar='C',
                deger=form.cleaned_data['cozum'],
                secenek=form.cleaned_data['cozum_secenek'],
                fabl_id=baslik,
            )
            return redirect(reverse("publish", args=[baslik.id]))
    return render(request, 'fabl_create.html', {
        'title': 'FABLE-CREATE',
        'form': form,
    })

def fabl_publish(request, id):
    id = Fabl.objects.get(id=id)
    sahnes = Sahne.objects.filter(fabl_id=id)
    return render(request, 'fabl_publish.html', {
        'title': id.baslik,
        'sahnes': sahnes,
>>>>>>> f75797dee37a786e1f07ad5b389ab5cb546c2ef6
    })
