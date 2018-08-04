from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from masal.models import Published


def signup(request): # Kullanıcı kayıt
    if request.method == 'POST': # POST metodunu kullanır.
        form = UserCreationForm(request.POST) # UserCreationForm da varsayılan bir değerdir.
        # Lakin buradaki form değişkenini biz veriyoruz. # Create düğmesine basınca yapılacak işlem. Girilen bilgileri işleyecek.
        # Aşağıda da kontrol edecek.
        if form.is_valid(): # Formdaki alanlar doğru doldurulduysa.
            form.save() # veritabanına kayıt eder.
            # Alttaki satırlar kayıt için gerekli olduğundan yazılmadı. Amacı kullanıcı kayıt olunca
            # girdiği bilgilerle siteye otomatik giriş yapması.
            username = form.cleaned_data.get('username') # Buradaki username Auth.Form'daki varsayılan değer.
            raw_password = form.cleaned_data.get('password1') # Aynı şekilde raw_password, password1 ve password2 değerleri için.
            user = authenticate(username=username,password=raw_password) # Kullanıcıdan alınan username ve password ile bir kullanıcı user oluştur.
            login(request, user) # Alınan bu değerlerle giriş yap.
            return redirect('home') # Anasayfaya yönlendirir. Buradaki home değeri urls.py da verilen name yani ismi.
        else:
            form = UserCreationForm() # Boş form yani kullanıcı kaydı işlemi aç.
            return render(request, 'registration/signup.html', {'form': form}) # Kayıt sayfasına yeniden gönderself.
            # Yukdarı satır sonundaki ilk form, signup.html içindeki form diğer ikinci form ise onun üstündeki satır.
            # signup içine form değişkenini gönder.
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
        # ikinci else ise yukarıdaki ilk if e ait. POST dışında bir şekilde gönderirse formu tekrar POST ile body girişi gerekli.

def about(request): # Bu değişke de about sayfasına göndermek için.
    return render(request, 'about.html')

def profile(request):
    user = request.user
    fables = Published.objects.filter(user_id=user.id) # Published yani yayınlanan tüm nesneleri çek. yukarıda tanımlanan user'ın id'si ne ait olanları çek.
    return render(request, 'profile.html', { # Sonra bunları profil sayfasında göster.
        'fables': fables # Gösterirken de ilk fables profile.html içindeki, diğer fables ise üst satırda atanan.
    })
