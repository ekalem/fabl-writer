from django import forms
from django.forms import formset_factory # Varsayılan kütüphane hem forms hem de formset_factory isimleri.

from .models import SECENEK # models içindeki SECENEK kısmının formda gözükmesi için çekilir aşağıdaki 12. satırdaki kodla kullanırız.

class SahneForm(forms.Form):
    baslik = forms.CharField(label='Başlık', max_length=100) # en fazla girilecek değer için max_length
    girizgah = forms.CharField(label='Girizgah', widget=forms.Textarea) # label kutunun başına etiket girmek için.
    serim = forms.CharField(label='Serim', widget=forms.Textarea) # widget form kutucuğunun şekli vb. şeyler için.
    dugum = forms.CharField(label='Düğüm', widget=forms.Textarea)
    cozum = forms.CharField(label='Çözüm', widget=forms.Textarea)
    cozum_secenek = forms.ChoiceField(choices=SECENEK) # Aşağıya doğru açılan seçenek gelmesi için ChoiceField türü kullanılır.

class BaglamForm(forms.Form): # Find and Replace yapabilmek için yeni bir sınıf.
    anahtar = forms.CharField(
        label='Fable Element',
        widget=forms.TextInput(attrs={ # TextInput form kutucuğunun içinde örnek yazı yazmak için. Veya varsayılan değer.
            'placeholder': 'Enter the fable element type. eg. Main Character or Place'  # placeholder 'ı bu yazı için kullanmak gerek.'
        })
    )
    deger = forms.CharField(
        label='Find',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the value of Fable Element to find. eg. House'
        })
    )
    extra = forms.CharField(
        label='Replace',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the new value of Fable Element to replace. eg. School'
        })
    )
BaglamFormset = formset_factory(BaglamForm, extra=3)
# Baglam için anahtar first last gibi form alanlarını çoklu göndermek için. Yani Extra karşılığı 3 değil 5 olsa 5 satır gösterir.
